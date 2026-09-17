import { SignupForm } from "@/components/SignupForm";
import { CheckSquareIcon } from "@/components/icons";

export default function SignupPage() {
  return (
    <main className="page">
      <span className="brand" style={{ justifyContent: "center", marginBottom: "1.5rem" }}>
        <CheckSquareIcon />
        TaskFlow
      </span>
      <h1 style={{ textAlign: "center" }}>Create your account</h1>
      <div className="card">
        <SignupForm />
      </div>
    </main>
  );
}
