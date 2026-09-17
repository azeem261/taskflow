"use client";

import { useEffect, useState } from "react";
import { fetchTasks, type Task } from "@/lib/api";
import { AppHeader } from "@/components/AppHeader";
import { TaskForm } from "@/components/TaskForm";
import { TaskList } from "@/components/TaskList";

export default function TasksPage() {
  const [tasks, setTasks] = useState<Task[]>([]);

  useEffect(() => {
    const token = localStorage.getItem("token") ?? "";
    fetchTasks(token).then(setTasks).catch(() => setTasks([]));
  }, []);

  return (
    <>
      <AppHeader />
      <main className="page-wide">
        <h1>Your tasks</h1>
        <div className="card">
          <TaskForm onCreated={(task) => setTasks((prev) => [...prev, task])} />
        </div>
        <TaskList tasks={tasks} />
      </main>
    </>
  );
}
