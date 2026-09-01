import React from "react";
import { createRoot } from "react-dom/client";
import "./style.css";

const WEB="https://convertflow-seven-delta.vercel.app/";
function App(){return <main><div className="logo">Convert<span>Flow</span></div><h1>Convert anything, anywhere.</h1><p>Fast file conversion and powerful browser tools, now available as a desktop and mobile app.</p><button onClick={()=>location.href=WEB}>Open ConvertFlow</button><small>The app connects to the official ConvertFlow web service.</small></main>}
createRoot(document.getElementById("root")).render(<App/>);
