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
export const GET_SLEEPWALKING_EVENTS = gql`
  query GetSleepwalkingEvents {
    allSleepwalkingEvents {
      id
      startTime
      endTime
      intensity
    }
  }
`;
