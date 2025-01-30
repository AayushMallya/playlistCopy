# playlistCopy
Spotiy currently has in-built functionality to copy playlists, however the order of the songs gets completely jumbled up.

Most people listen to their playlist by their recently added songs, but spotify doesn't copy over that order or keep track of it when copying to a new playlist; this results in your most 'recent' song being a random one from 2 years ago instead of the one you added yesterday.

This code transfers songs from one playlist to another, while maintaining the integrity of its date added order; this way your most recent songs are your actual most recent.

It also skips over songs that have been taken down or are unavailable, (like any local storage songs added to the playlist).
