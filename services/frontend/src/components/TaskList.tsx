import type { Task } from "@/lib/api";

export function TaskList({ tasks }: { tasks: Task[] }) {
  if (tasks.length === 0) {
    return <p>No tasks yet.</p>;
  }
  return (
    <ul>
      {tasks.map((task) => (
        <li key={task.id}>
          <strong>{task.title}</strong> — {task.status}
          <p>{task.description}</p>
        </li>
      ))}
    </ul>
  );
}
