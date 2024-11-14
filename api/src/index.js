import { ApolloServer } from '@apollo/server';
import { readFileSync } from 'fs';
import { expressMiddleware } from '@apollo/server/express4';
import express from 'express';
import dotenv from 'dotenv';

dotenv.config();

const app = express();

app.use(express.json());

const typeDefs = readFileSync('src/schema/schema.graphql').toString('utf-8');
import resolvers from './resolvers/index.js';

const server = new ApolloServer({
    typeDefs,
    resolvers,
});
await server.start();

app.use('/graphql', expressMiddleware(server));

app.listen(8000, () => {
    console.log(`🚀 API Gateway ready at http://localhost:8000`);
});
