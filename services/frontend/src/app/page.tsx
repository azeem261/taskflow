import Link from "next/link";

export default function Home() {
  return (
    <main>
      <h1>TaskFlow</h1>
      <p>
        <Link href="/login">Log in</Link> to manage your tasks.
      </p>
    </main>
  );
}
