import { Request, Response, NextFunction } from "express";
import * as songsService from "./songs.service";

export async function getAll(req: Request, res: Response, next: NextFunction) {
  try {
    const filters = {
      q: req.query.q as string | undefined,
      genre: req.query.genre as string | undefined,
      artist: req.query.artist as string | undefined,
      minDuration: req.query.minDuration
        ? parseInt(req.query.minDuration as string, 10)
        : undefined,
      maxDuration: req.query.maxDuration
        ? parseInt(req.query.maxDuration as string, 10)
        : undefined,
    };

    const songs = await songsService.listSongs(filters);
    res.json(songs);
  } catch (err) {
    next(err);
  }
}
