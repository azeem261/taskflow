import { describe, expect, it, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import { TaskList } from "@/components/TaskList";

describe("TaskList", () => {
  it("renders an empty state when there are no tasks", () => {
    render(<TaskList tasks={[]} onStatusChange={vi.fn()} onDelete={vi.fn()} />);
    expect(screen.getByText(/no tasks yet/i)).toBeInTheDocument();
  });

  it("renders a task's title and status", () => {
    render(
      <TaskList
        tasks={[
          {
            id: 1,
            title: "Write tests",
            description: "Cover the happy path",
            status: "todo",
            owner: "alice@example.com",
          },
        ]}
        onStatusChange={vi.fn()}
        onDelete={vi.fn()}
      />
    );
    expect(screen.getByText("Write tests")).toBeInTheDocument();
    expect(screen.getByText("To do", { selector: "span" })).toBeInTheDocument();
  });
});
