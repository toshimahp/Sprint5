import { useState } from "react";

function Login({ setToken }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  async function handleLogin() {
    const response = await fetch("http://127.0.0.1:8001/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username: username, password: password }),
    });

    if (response.status === 200) {
      const data = await response.json();
      setToken(data.access_token);
    } else {
      setMessage("Wrong username or password");
    }
  }

  return (
    <div>
      <h2>Login</h2>

      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <br />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <br />

      <button onClick={handleLogin}>Login</button>

      <p>{message}</p>
    </div>
  );
}

export default Login;