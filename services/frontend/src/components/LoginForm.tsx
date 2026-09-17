"use client";

import { useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import { login } from "@/lib/api";

export function LoginForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    try {
      const token = await login(email, password);
      localStorage.setItem("token", token);
      router.push("/tasks");
    } catch {
      setError("Invalid email or password");
    }
  }

  return (
    <form onSubmit={handleSubmit} aria-label="login-form">
      <label htmlFor="email">Email</label>
      <input
        id="email"
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />
      <label htmlFor="password">Password</label>
      <input
        id="password"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      />
      <button type="submit">Log in</button>
      {error && <p role="alert">{error}</p>}
    </form>
  );
}
