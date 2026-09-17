"use client";

import { useEffect, useState } from "react";
import { fetchTasks, type Task } from "@/lib/api";
import { TaskForm } from "@/components/TaskForm";
import { TaskList } from "@/components/TaskList";

export default function TasksPage() {
  const [tasks, setTasks] = useState<Task[]>([]);

  useEffect(() => {
    const token = localStorage.getItem("token") ?? "";
    fetchTasks(token).then(setTasks).catch(() => setTasks([]));
  }, []);

  return (
    <main>
      <h1>Your tasks</h1>
      <div className="card">
        <TaskForm onCreated={(task) => setTasks((prev) => [...prev, task])} />
      </div>
      <div style={{ marginTop: 24 }}>
        <TaskList tasks={tasks} />
      </div>
    </main>
  );
}
