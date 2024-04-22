import { ApolloClient, InMemoryCache, HttpLink } from '@apollo/client';
import Cookies from 'js-cookie';

const client = new ApolloClient({
    // -------------------
    // # Required Fields #
    // -------------------
    // URI - GraphQL Endpoint
    uri: 'http://192.168.4.85:8000/graphql/',
    // Cache
    cache: new InMemoryCache(),
  
    // -------------------
    // # Optional Fields #
    // -------------------
    // DevBrowserConsole
    connectToDevTools: true,
    // Else
    credentials: 'same-origin',
    
    headers: {
      'X-CSRFToken': Cookies.get('csrftoken')
    }
  });
export default client;
