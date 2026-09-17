import { LoginForm } from "@/components/LoginForm";
import { CheckSquareIcon } from "@/components/icons";

export default function LoginPage() {
  return (
    <main className="page">
      <span className="brand" style={{ justifyContent: "center", marginBottom: "1.5rem" }}>
        <CheckSquareIcon />
        TaskFlow
      </span>
      <h1 style={{ textAlign: "center" }}>Log in</h1>
      <div className="card">
        <LoginForm />
      </div>
    </main>
  );
}
