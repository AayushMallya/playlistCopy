# Goal
Spotiy currently has in-built functionality to copy playlists, however the order of the songs gets completely jumbled up.

Most people listen to their playlist by their recently added songs, but spotify doesn't copy over that order or keep track of it when copying to a new playlist; this results in your most 'recent' song being a random one from 2 years ago instead of the one you added yesterday.

# Current Functionality
This code transfers songs from one playlist to another, while maintaining the integrity of its date added order; this way your most recent songs are your actual most recent.
It also skips over songs that have been taken down or are unavailable, (like any local storage songs added to the playlist).

# Bug to Note
For larger playlists, (for example mine was ~1200 songs), the spotify auth token may timeout partway through copying. 
This is in part why the code compares the contents of playlists, so you can just rerun the program and it will pickup where it left off.
