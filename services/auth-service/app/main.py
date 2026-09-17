from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.auth import create_access_token, hash_password, verify_password
from app.database import Base, engine, get_db
from app.models import User
from app.schemas import LoginRequest, SignupRequest, TokenResponse, UserResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="auth-service")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def signup(payload: SignupRequest, db: Session = Depends(get_db)):
    user = User(email=payload.email, hashed_password=hash_password(payload.password))
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
    db.refresh(user)
    return user


@app.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if user is None or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token(subject=user.email)
    return TokenResponse(access_token=token)
