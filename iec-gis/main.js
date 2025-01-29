import './style.css';
import {Map, View} from 'ol';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import { SparqlEndpointFetcher } from 'fetch-sparql-endpoint';

// const sparqlFetcher = new SparqlEndpointFetcher({
//   // A custom HTTP method for issuing (non-update) queries, defaults to POST. Update queries are always issued via POST.
//   method: 'POST',
//   // A set of additional parameters that well be added to fetchAsk, fetchBindings & fetchTriples requests
//   additionalUrlParams: new URLSearchParams({ infer: 'true', sameAs: 'false' }),
//   // Optional default headers that will be included in each request
//   defaultHeaders: new Headers(),
//   // A custom fetch-API-supporting function
//   fetch,
//   // A custom RDFJS data factory
//   dataFactory: DataFactory,
//   // If variable names in bindings should be prefixed with '?', defaults to false
//   prefixVariableQuestionMark: false,
//   // Timeout for setting up server connection (Once a connection has been made, and the response is being parsed, the timeout does not apply anymore).
//   timeout: 5000,
// });

const map = new Map({
  target: 'map',
  layers: [
    new TileLayer({
      source: new OSM()
    })
  ],
  view: new View({
    center: [0, 0],
    zoom: 2
  })
});


// const bindingsStream = sparqlFetcher.fetchBindings('https://dbpedia.org/sparql', 'SELECT * WHERE { ?s ?p ?o } LIMIT 100');

// bindingsStream.on('data', bindings => console.log(bindings));
