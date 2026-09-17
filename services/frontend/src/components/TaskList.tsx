import type { Task } from "@/lib/api";

const STATUS_LABEL: Record<Task["status"], string> = {
  todo: "To do",
  in_progress: "In progress",
  done: "Done",
};

export function TaskList({ tasks }: { tasks: Task[] }) {
  if (tasks.length === 0) {
    return (
      <div className="empty-state">
        <p style={{ margin: 0 }}>No tasks yet — add your first one above.</p>
      </div>
    );
  }
  return (
    <ul className="task-list">
      {tasks.map((task) => (
        <li key={task.id}>
          <div className="task-title-row">
            <strong>{task.title}</strong>
            <span className={`status status-${task.status}`}>{STATUS_LABEL[task.status]}</span>
          </div>
          {task.description && <p>{task.description}</p>}
        </li>
      ))}
    </ul>
  );
}
