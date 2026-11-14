import { useState, useEffect } from "react";

function Packages({ token, setToken }) {
  const [packages, setPackages] = useState([]);

  async function getPackages() {
    const response = await fetch("http://127.0.0.1:8001/packages", {
      headers: { token: token },
    });

    if (response.status === 200) {
      const data = await response.json();
      setPackages(data);
    } else {
      // token expired or invalid, go back to login
      setToken("");
    }
  }

  // load packages when the page opens
  useEffect(() => {
    getPackages();
  }, []);

  return (
    <div>
      <h2>All Packages</h2>
      <button onClick={() => setToken("")}>Logout</button>

      <div className="table">
        <div className="row header">
          <div>ID</div>
          <div>Name</div>
          <div>Destination</div>
          <div>Weight</div>
          <div>Arrival Date</div>
          <div>Status</div>
        </div>
        {packages.map((p) => (
          <div className="row" key={p.package_id}>
            <div>{p.package_id}</div>
            <div>{p.name}</div>
            <div>{p.destination}</div>
            <div>{p.weight}</div>
            <div>{p.arrival_date}</div>
            <div>{p.status}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Packages;