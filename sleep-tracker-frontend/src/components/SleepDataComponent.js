// src/components/SleepDataComponent.js
import React from 'react';
import { useQuery } from '@apollo/client';
import { GET_SLEEP_DATA } from '../queries';

function SleepDataComponent() {
  const { loading, error, data } = useQuery(GET_SLEEP_DATA);

  if (loading) return <p>Loading...</p>;
  if (error) {
    console.error("GraphQL Error:", error);
    return <p>Error :(</p>;
  }

  return (
    <div>
      <h1>Sleep Data</h1>
      {data.allSleepData.map(({ id, startTime, endTime, sleepScore }) => (
        <div key={id}>
          <p>Sleep from {startTime} to {endTime} with score: {sleepScore}</p>
        </div>
      ))}
    </div>
  );
}

export default SleepDataComponent;
