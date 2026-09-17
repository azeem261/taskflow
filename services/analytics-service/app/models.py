from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class StatusCount(Base):
    __tablename__ = "status_counts"

    status: Mapped[str] = mapped_column(String(50), primary_key=True)
    count: Mapped[int] = mapped_column(Integer, default=0)
