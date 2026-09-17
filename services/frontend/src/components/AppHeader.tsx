"use client";

import { useRouter } from "next/navigation";
import { CheckSquareIcon, LogOutIcon } from "@/components/icons";

export function AppHeader() {
  const router = useRouter();

  function handleLogout() {
    localStorage.removeItem("token");
    router.push("/login");
  }

  return (
    <header className="app-header">
      <span className="brand">
        <CheckSquareIcon />
        TaskFlow
      </span>
      <button type="button" className="btn-secondary" onClick={handleLogout}>
        <span style={{ display: "inline-flex", alignItems: "center", gap: 6 }}>
          <LogOutIcon width={16} height={16} />
          Log out
        </span>
      </button>
    </header>
  );
}
