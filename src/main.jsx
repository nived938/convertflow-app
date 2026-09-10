import React from "react";
import { createRoot } from "react-dom/client";
import "./style.css";

function App() {
  return (
    <main aria-label="ConvertFlow">
      <div className="mark" aria-hidden="true">CF</div>
      <h1>ConvertFlow</h1>
      <p>Loading the official ConvertFlow service…</p>
    </main>
  );
}

createRoot(document.getElementById("root")).render(<App />);
