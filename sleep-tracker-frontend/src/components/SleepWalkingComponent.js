// src/components/SleepWalkingComponent.js
import React , { useEffect } from 'react';
import { useQuery } from '@apollo/client';
import { GET_SLEEPWALKING_EVENTS } from '../queries';
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';

function SleepwalkingComponent() {
  const { loading, error, data, refetch } = useQuery(GET_SLEEPWALKING_EVENTS);

  // Refetch the data every 5 seconds
  useEffect(() => {
    const intervalId = setInterval(() => {
      refetch();
    }, 5000);

    // Clean up the interval on unmount
    return () => clearInterval(intervalId);
  }, [refetch]);

  if (loading) return <p>Loading...</p>;
  if (error) {
    console.error("GraphQL Error:", error);
    return <p>Error :(</p>;
  }

  // Sample data for when the database is empty
  const sampleData = [
    { id: '1', startTime: '2022-01-01T00:00:00Z', endTime: '2022-01-01T01:00:00Z', intensity: 5 },
    { id: '2', startTime: '2022-01-02T00:00:00Z', endTime: '2022-01-02T01:30:00Z', intensity: 7 },
    // Add more sample events as needed
  ];

  const events = data.allSleepwalkingEvents.length > 0 ? data.allSleepwalkingEvents : sampleData;

  // Prepare the data for the bar chart
  const chartData = events.map(({ id, startTime, endTime, intensity }) => {
    // Calculate the duration of the event in minutes
    const duration = (new Date(endTime) - new Date(startTime)) / 1000 / 60;
    return {
      name: `Event ${id}`,
      Intensity: intensity,
      Duration: duration,
    };
  });

  return (
    <div>
      <h1>Sleepwalking Events</h1>
      <BarChart width={500} height={300} data={chartData}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="Intensity" fill="#8884d8" />
        <Bar dataKey="Duration" fill="#82ca9d" />
      </BarChart>
    </div>
  );
}

export default SleepwalkingComponent;