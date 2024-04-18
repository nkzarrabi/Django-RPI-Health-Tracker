import React from 'react';
import { ApolloProvider } from '@apollo/client';  // Corrected import
import client from './ApolloClient';
import SleepDataComponent from './components/SleepDataComponent';

function App() {
  return (
    <ApolloProvider client={client}>
      <div className="App">
        <h1>Sleep Tracker</h1>
        <SleepDataComponent />
      </div>
    </ApolloProvider>
  );
}

export default App;
