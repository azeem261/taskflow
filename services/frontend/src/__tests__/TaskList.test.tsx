import { describe, expect, it } from "vitest";
import { render, screen } from "@testing-library/react";
import { TaskList } from "@/components/TaskList";

describe("TaskList", () => {
  it("renders an empty state when there are no tasks", () => {
    render(<TaskList tasks={[]} />);
    expect(screen.getByText("No tasks yet.")).toBeInTheDocument();
  });

  it("renders a task's title and status", () => {
    render(
      <TaskList
        tasks={[
          {
            id: "1",
            title: "Write tests",
            description: "Cover the happy path",
            status: "todo",
            owner: "alice@example.com",
          },
        ]}
      />
    );
    expect(screen.getByText("Write tests")).toBeInTheDocument();
    expect(screen.getByText(/todo/)).toBeInTheDocument();
  });
});
