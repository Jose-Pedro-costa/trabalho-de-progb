CREATE TABLE IF NOT EXISTS songs (
  id                SERIAL PRIMARY KEY,
  title             TEXT NOT NULL,
  artist            TEXT NOT NULL,
  album             TEXT,
  genre             TEXT,
  duration_seconds  INTEGER NOT NULL CHECK (duration_seconds > 0),
  cover_url         TEXT,
  preview_url       TEXT,
  created_at        TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_songs_title ON songs (title);
CREATE INDEX IF NOT EXISTS idx_songs_artist ON songs (artist);
CREATE INDEX IF NOT EXISTS idx_songs_genre ON songs (genre);
