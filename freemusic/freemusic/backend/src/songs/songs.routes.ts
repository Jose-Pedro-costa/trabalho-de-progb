import { Router } from "express";
import * as songsController from "./songs.controller";

const router = Router();
router.get("/api/songs", songsController.getAll);
export default router;
