import ReactDOM from "react-dom/client";
import React from "react";
import "./input.css";
// import "../dist/input.css";
import App from "./App";

// ReactDOM.render(<App />, document.getElementById('root'));

// React 18에서 사용하는 방식으로 변경
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
// ReactDOM.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>,
//   document.getElementById("root")
// );

// reportWebVitals();a

// const root = ReactDOM.createRoot(document.getElementById("root"));
// root.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>
// );
