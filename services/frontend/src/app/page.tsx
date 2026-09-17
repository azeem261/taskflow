import Link from "next/link";
import { CheckSquareIcon } from "@/components/icons";

export default function Home() {
  return (
    <main className="page">
      <span className="brand" style={{ justifyContent: "center", marginBottom: "1.5rem" }}>
        <CheckSquareIcon />
        TaskFlow
      </span>
      <div className="card" style={{ textAlign: "center" }}>
        <h1>Stay on top of your work</h1>
        <p>A small, focused task tracker built to practice microservices.</p>
        <div style={{ display: "flex", gap: "0.75rem", justifyContent: "center", marginTop: "1.5rem" }}>
          <Link href="/login" className="btn-secondary" style={{ textDecoration: "none" }}>
            Log in
          </Link>
          <Link href="/signup" className="btn-primary" style={{ marginTop: 0, textDecoration: "none" }}>
            Sign up
          </Link>
        </div>
      </div>
    </main>
  );
}
