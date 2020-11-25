/* web/App.tsx
 * Ian Kollipara
 * 2020.11.24
 * React Main App
 */

// Imports
import React, { useState } from "react";
import Nav from "./components/nav";
import Pages from "./models/pages";
import Home from "./components/home";
import Login from "./components/login";
import ListeningGraph from "./components/listeningGraph";

// Main App Function
const App: React.FC = (): JSX.Element => {
  const [currentPage, setCurrentPage] = useState<Pages>(
    window.localStorage.getItem("token") ? Pages.Home : Pages.Login
  );

  return (
    <div>
      {currentPage === Pages.Login ? (
        <div>
          <Home />
          <Login onSelect={setCurrentPage} />
        </div>
      ) : (
        <div>
          <Home />
          <div className="container">
            <div className="row">
              <div className="col-sm"></div>
              <div className="col-sm">
                <div className="col-sm"></div>
                <div className="d-flex flex-column justify-content-center align-content-center">
                  <button
                    className="btn btn-outline-success"
                    onClick={(
                      e: React.MouseEvent<HTMLButtonElement, MouseEvent>
                    ) => setCurrentPage(Pages.ListeningGraph)}
                  >
                    Listening Graph
                  </button>
                  <button
                    className="btn btn-outline-success"
                    onClick={(
                      e: React.MouseEvent<HTMLButtonElement, MouseEvent>
                    ) => {
                      window.localStorage.removeItem("token");
                      window.location.reload(true);
                    }}
                  >
                    Logout
                  </button>
                </div>
              </div>
              <div className="col-sm"></div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default App;
