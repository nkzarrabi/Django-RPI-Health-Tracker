// src/components/SleepWalkingComponent.js
import React from 'react';
import { useQuery } from '@apollo/client';
import { GET_SLEEPWALKING_EVENTS } from '../queries';

function SleepwalkingComponent() {
  const { loading, error, data } = useQuery(GET_SLEEPWALKING_EVENTS);

  if (loading) return <p>Loading...</p>;
  if (error) {
    console.error("GraphQL Error:", error);
    return <p>Error :(</p>;
  }

  return (
    <div>
      <h1>Sleepwalking Events</h1>
      {data.allSleepwalkingEvents.map(({ id, startTime, endTime, intensity }) => (
        <div key={id}>
          <p>Sleepwalking from {startTime} to {endTime} - Intensity: {intensity}</p>
        </div>
      ))}
    </div>
  );
}

export default SleepwalkingComponent;

