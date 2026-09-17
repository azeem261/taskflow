"use client";

import { useEffect, useState } from "react";
import { deleteTask, fetchTasks, updateTaskStatus, type Task } from "@/lib/api";
import { AppHeader } from "@/components/AppHeader";
import { TaskForm } from "@/components/TaskForm";
import { TaskList } from "@/components/TaskList";

export default function TasksPage() {
  const [tasks, setTasks] = useState<Task[]>([]);

  useEffect(() => {
    const token = localStorage.getItem("token") ?? "";
    fetchTasks(token).then(setTasks).catch(() => setTasks([]));
  }, []);

  async function handleStatusChange(taskId: number, status: Task["status"]) {
    const token = localStorage.getItem("token") ?? "";
    const previous = tasks;
    setTasks((prev) => prev.map((t) => (t.id === taskId ? { ...t, status } : t)));
    try {
      await updateTaskStatus(token, taskId, status);
    } catch {
      setTasks(previous);
    }
  }

  async function handleDelete(taskId: number) {
    const token = localStorage.getItem("token") ?? "";
    const previous = tasks;
    setTasks((prev) => prev.filter((t) => t.id !== taskId));
    try {
      await deleteTask(token, taskId);
    } catch {
      setTasks(previous);
    }
  }

  return (
    <>
      <AppHeader />
      <main className="page-wide">
        <h1>Your tasks</h1>
        <div className="card">
          <TaskForm onCreated={(task) => setTasks((prev) => [...prev, task])} />
        </div>
        <TaskList tasks={tasks} onStatusChange={handleStatusChange} onDelete={handleDelete} />
      </main>
    </>
  );
}
