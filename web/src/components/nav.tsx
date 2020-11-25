/* components/nav.tsx
 * Ian Kollipara
 * 2020.11.24
 * MyFy Navbar
 */

// Imports
import React, { Dispatch, SetStateAction } from "react";
import Pages from "../models/pages";

interface Props {
  onSelect: Dispatch<SetStateAction<Pages>>;
}

// Navbar Component
const Nav = ({ onSelect }: Props): JSX.Element => (
  <div>
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <a className="navbar-brand" href="#">
        MyFy
      </a>
      <button
        className="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbar"
        aria-controls="navbar"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span className="navbar-toggler-icon"></span>
      </button>
    </nav>

    <div className="collapse navbar-collapse" id="navbar">
      <ul className="navbar-nav mr-auto">
        <li className="nav-item">
          <button
            className="btn btn-outline-success"
            onClick={(e: React.MouseEvent<HTMLButtonElement, MouseEvent>) =>
              onSelect(Pages.Home)
            }
          >
            Home
          </button>
        </li>
        <li className="nav-item">
          <button
            className="btn btn-outline-success"
            onClick={(e: React.MouseEvent<HTMLButtonElement, MouseEvent>) =>
              onSelect(Pages.ListeningGraph)
            }
          >
            Listening Graph
          </button>
        </li>
        <li className="nav-item">
          <button
            className="btn btn-outline-success"
            onClick={(e: React.MouseEvent<HTMLButtonElement, MouseEvent>) => {
              window.localStorage.removeItem("token");
              window.location.reload(true);
            }}
          >
            Logout
          </button>
        </li>
      </ul>
    </div>
  </div>
);

export default Nav;
