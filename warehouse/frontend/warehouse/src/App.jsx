import { useState } from "react";
import Login from "./components/Login";
import Packages from "./components/Packages";

function App() {
  const [token, setToken] = useState("");

  // if there is no token, show the login page
  if (token === "") {
    return <Login setToken={setToken} />;
  }

  // if there is a token, show the packages page
  return <Packages token={token} setToken={setToken} />;
}

export default App;
