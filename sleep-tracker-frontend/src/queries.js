// src/queries.js
import { gql } from '@apollo/client';

export const GET_SLEEP_DATA = gql`
  query GetSleepData {
    allSleepData {
      id
      startTime
      endTime
      sleepScore
    }
  }
`;
