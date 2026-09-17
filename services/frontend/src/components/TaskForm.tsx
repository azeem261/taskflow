"use client";

import { useState, type FormEvent } from "react";
import { createTask, type Task } from "@/lib/api";

export function TaskForm({ onCreated }: { onCreated: (task: Task) => void }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setIsSubmitting(true);
    try {
      const token = localStorage.getItem("token") ?? "";
      const task = await createTask(token, { title, description });
      onCreated(task);
      setTitle("");
      setDescription("");
    } catch {
      setError("Couldn't add that task. Try again.");
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <form onSubmit={handleSubmit} aria-label="task-form">
      <div className="field">
        <label htmlFor="title">Title</label>
        <input id="title" value={title} onChange={(e) => setTitle(e.target.value)} required />
      </div>
      <div className="field">
        <label htmlFor="description">Description</label>
        <textarea
          id="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
      </div>
      <button type="submit" className="btn-primary" disabled={isSubmitting} aria-busy={isSubmitting}>
        {isSubmitting ? "Adding…" : "Add task"}
      </button>
      {error && <p role="alert">{error}</p>}
    </form>
  );
}
