import "dotenv/config";
import express from "express";
import songsRoutes from "./songs/songs.routes";
import { errorHandler } from "./errors/errorHandler";
import { loadConfig } from "./config";

const config = loadConfig();
const app = express();

app.use(songsRoutes);

// 404
app.use((req, res) => {
  res.status(404).json({
    error: { code: "ROUTE_NOT_FOUND", message: "A rota solicitada não existe." },
  });
});

app.use(errorHandler);

app.listen(config.port, () => {
  console.log(`Servidor rodando em http://localhost:${config.port}`);
});
