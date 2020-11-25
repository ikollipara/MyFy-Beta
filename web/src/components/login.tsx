/* components/login.tsx
 * Ian Kollipara
 * 2020.11.24
 * MyFy Login Page
 */

// Imports
import React, { Dispatch, SetStateAction, useEffect } from "react";
import Pages from "../models/pages";

interface Props {
  onSelect: Dispatch<SetStateAction<Pages>>;
}

// Login Page
const Login = ({ onSelect }: Props): JSX.Element => {
  const onLoginClick = (e: React.MouseEvent<HTMLButtonElement>): void => {
    e.preventDefault();
    window.location.replace("/auth/?redirect=http://localhost:8080");
  };

  // Get the User Token
  useEffect(() => {
    fetch("http://localhost:8080/auth/get_token")
      .then((res) => res.json())
      .then((json: object) => {
        // Put the token in user storage
        window.localStorage.setItem("token", JSON.stringify(json));
        onSelect(Pages.Home);
      })
      .catch((err) => console.log(`Error: ${err}`));
  });

  return (
    <div className="container">
      <div className="row">
        <div className="col-sm"></div>
        <div className="col-sm d-inline-flex flex-row justify-content-center">
          <button
            className="btn btn-outline-success"
            onClick={(e: React.MouseEvent<HTMLButtonElement>) =>
              onLoginClick(e)
            }
          >
            Login
          </button>
        </div>
        <div className="col-sm"></div>
      </div>
    </div>
  );
};
export default Login;
