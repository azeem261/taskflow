import type { ReactNode } from "react";

export const metadata = {
  title: "TaskFlow",
  description: "Practice microservices task manager",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
