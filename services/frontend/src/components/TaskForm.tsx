"use client";

import { useState, type FormEvent } from "react";
import { createTask, type Task } from "@/lib/api";

export function TaskForm({ onCreated }: { onCreated: (task: Task) => void }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    const token = localStorage.getItem("token") ?? "";
    const task = await createTask(token, { title, description });
    onCreated(task);
    setTitle("");
    setDescription("");
  }

  return (
    <form onSubmit={handleSubmit} aria-label="task-form">
      <label htmlFor="title">Title</label>
      <input
        id="title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        required
      />
      <label htmlFor="description">Description</label>
      <textarea
        id="description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <button type="submit">Add task</button>
    </form>
  );
}
