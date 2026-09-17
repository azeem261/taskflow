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
        <Link href="/login" className="btn-primary" style={{ display: "inline-block", textDecoration: "none" }}>
          Log in
        </Link>
      </div>
    </main>
  );
}
