import * as songsRepository from "./songs.repository";
import type { SongFilters } from "./songs.repository";

export async function listSongs(filters: SongFilters) {
  return songsRepository.findAll(filters);
}
