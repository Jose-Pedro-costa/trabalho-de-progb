TRUNCATE TABLE songs RESTART IDENTITY;

INSERT INTO songs (title, artist, album, genre, duration_seconds, cover_url, preview_url) VALUES
('Sunrise Over the Bay', 'Luna Waves', 'Coastal Dreams', 'Ambient', 214, 'https://picsum.photos/seed/song1/300', NULL),
('Midnight Drive', 'Neon Pulse', 'City Lights', 'Electronic', 198, 'https://picsum.photos/seed/song2/300', NULL),
('Coffee Shop Jazz', 'The Blue Notes', 'Morning Sessions', 'Jazz', 245, 'https://picsum.photos/seed/song3/300', NULL),
('Forest Walk', 'Nature Collective', 'Green Paths', 'Ambient', 312, 'https://picsum.photos/seed/song4/300', NULL),
('Electric Horizon', 'Synthwave Kids', 'Retro Future', 'Synthwave', 187, 'https://picsum.photos/seed/song5/300', NULL),
('Rainy Day Blues', 'Sarah Lane', 'Quiet Moments', 'Blues', 256, 'https://picsum.photos/seed/song6/300', NULL),
('Upbeat Morning', 'Happy Beats', 'Daily Energy', 'Pop', 172, 'https://picsum.photos/seed/song7/300', NULL),
('Deep Focus', 'Study Mode', 'Concentration', 'Lo-fi', 301, 'https://picsum.photos/seed/song8/300', NULL),
('Ocean Waves', 'Coastal Sounds', 'Nature Series', 'Ambient', 420, 'https://picsum.photos/seed/song9/300', NULL),
('Guitar Sunset', 'Acoustic Soul', 'Evenings', 'Acoustic', 203, 'https://picsum.photos/seed/song10/300', NULL),
('Club Night', 'DJ Spark', 'Weekend Vibes', 'House', 231, 'https://picsum.photos/seed/song11/300', NULL),
('Quiet Library', 'Soft Piano', 'Study Hours', 'Classical', 278, 'https://picsum.photos/seed/song12/300', NULL);
