import type { Task } from "@/lib/api";
import { TrashIcon } from "@/components/icons";

const STATUS_LABEL: Record<Task["status"], string> = {
  todo: "To do",
  in_progress: "In progress",
  done: "Done",
};

const STATUS_OPTIONS = Object.keys(STATUS_LABEL) as Task["status"][];

type TaskListProps = {
  tasks: Task[];
  onStatusChange: (taskId: number, status: Task["status"]) => void;
  onDelete: (taskId: number) => void;
};

export function TaskList({ tasks, onStatusChange, onDelete }: TaskListProps) {
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
          <div className="task-actions">
            <label className="visually-hidden" htmlFor={`status-${task.id}`}>
              Status for {task.title}
            </label>
            <select
              id={`status-${task.id}`}
              value={task.status}
              onChange={(e) => onStatusChange(task.id, e.target.value as Task["status"])}
            >
              {STATUS_OPTIONS.map((status) => (
                <option key={status} value={status}>
                  {STATUS_LABEL[status]}
                </option>
              ))}
            </select>
            <button
              type="button"
              className="btn-icon"
              aria-label={`Delete ${task.title}`}
              onClick={() => onDelete(task.id)}
            >
              <TrashIcon width={16} height={16} />
            </button>
          </div>
        </li>
      ))}
    </ul>
  );
}
