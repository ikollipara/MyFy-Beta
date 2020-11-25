/* components/listeningGraph.tsx
 * Ian Kollipara
 * 2020.11.24
 * MyFy Listening Graph Page
 */

// Imports
import React, { useEffect, useState } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
} from "recharts";

interface GraphValues {
  name: string;
  data: [number, number];
}

// Listening Graph Page
const ListeningGraph = (): JSX.Element => {
  const [allGenres, setAllGenres] = useState<Array<string>>([]);
  const [currentGraphValues, setCurrentGraphValues] = useState<
    Array<GraphValues>
  >([
    {
      name: "",
      data: [0, 0],
    },
  ]);

  const onGenreSelect = (
    e: React.MouseEvent<HTMLButtonElement>,
    genre: string
  ): void => {
    e.preventDefault();
    fetch(
      `api/listening_graph?genre=${genre}&access_token=${
        JSON.parse(window.localStorage.getItem("token") as string).access_token
      }`
    )
      .then((res) => res.json())
      .then((json) => setCurrentGraphValues(json));
  };

  useEffect(() => {
    fetch(
      `api/total_genres?access_token=${
        JSON.parse(window.localStorage.getItem("token") as string).access_token
      }`
    )
      .then((res) => res.json())
      .then((json) => setAllGenres(json.genres));
  }, [allGenres]);

  return (
    <div>
      <div>
        {allGenres &&
          allGenres.map((genre) => (
            <button
              onClick={(e: React.MouseEvent<HTMLButtonElement>) =>
                onGenreSelect(e, genre)
              }
              type="button"
            >
              {genre}
            </button>
          ))}
      </div>
      <p>{allGenres}</p>
      {currentGraphValues[0].name && (
        <LineChart
          width={500}
          height={300}
          data={currentGraphValues}
          margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="data" stroke="#888d48" />
        </LineChart>
      )}
    </div>
  );
};

export default ListeningGraph;
