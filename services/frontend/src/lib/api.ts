const AUTH_URL = process.env.NEXT_PUBLIC_AUTH_URL ?? "http://localhost:8001";
const TASKS_URL = process.env.NEXT_PUBLIC_TASKS_URL ?? "http://localhost:8002";

export type Task = {
  id: number;
  title: string;
  description: string;
  status: "todo" | "in_progress" | "done";
  owner: string;
};

export async function login(email: string, password: string): Promise<string> {
  const res = await fetch(`${AUTH_URL}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  if (!res.ok) throw new Error("Login failed");
  const data = await res.json();
  return data.access_token as string;
}

export async function signup(email: string, password: string): Promise<void> {
  const res = await fetch(`${AUTH_URL}/signup`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  if (!res.ok) {
    if (res.status === 409) throw new Error("An account with that email already exists");
    throw new Error("Signup failed");
  }
}

export async function fetchTasks(token: string): Promise<Task[]> {
  const res = await fetch(`${TASKS_URL}/tasks`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!res.ok) throw new Error("Failed to load tasks");
  return res.json();
}

export async function createTask(
  token: string,
  task: Pick<Task, "title" | "description">
): Promise<Task> {
  const res = await fetch(`${TASKS_URL}/tasks`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(task),
  });
  if (!res.ok) throw new Error("Failed to create task");
  return res.json();
}

export async function updateTaskStatus(
  token: string,
  taskId: number,
  status: Task["status"]
): Promise<Task> {
  const res = await fetch(`${TASKS_URL}/tasks/${taskId}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({ status }),
  });
  if (!res.ok) throw new Error("Failed to update task");
  return res.json();
}

export async function deleteTask(token: string, taskId: number): Promise<void> {
  const res = await fetch(`${TASKS_URL}/tasks/${taskId}`, {
    method: "DELETE",
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!res.ok) throw new Error("Failed to delete task");
}
