import { pool } from "../db";

export interface SongFilters {
  q?: string;
  genre?: string;
  artist?: string;
  minDuration?: number;
  maxDuration?: number;
}

export async function findAll(filters: SongFilters = {}) {
  const conditions: string[] = [];
  const values: any[] = [];
  let idx = 1;

  if (filters.q) {
    conditions.push(`(title ILIKE $${idx} OR artist ILIKE $${idx})`);
    values.push(`%${filters.q}%`);
    idx++;
  }
  if (filters.genre) {
    conditions.push(`genre ILIKE $${idx}`);
    values.push(filters.genre);
    idx++;
  }
  if (filters.artist) {
    conditions.push(`artist ILIKE $${idx}`);
    values.push(`%${filters.artist}%`);
    idx++;
  }
  if (filters.minDuration !== undefined) {
    conditions.push(`duration_seconds >= $${idx}`);
    values.push(filters.minDuration);
    idx++;
  }
  if (filters.maxDuration !== undefined) {
    conditions.push(`duration_seconds <= $${idx}`);
    values.push(filters.maxDuration);
    idx++;
  }

  const where = conditions.length > 0 ? `WHERE ${conditions.join(" AND ")}` : "";

  const result = await pool.query(
    `
    SELECT id, title, artist, album, genre, duration_seconds,
           cover_url, preview_url, created_at
    FROM songs
    ${where}
    ORDER BY title ASC
    `,
    values
  );

  return result.rows;
}
