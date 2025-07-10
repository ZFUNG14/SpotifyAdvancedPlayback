# Spotify Advanced Playback Control Plugin (WIP)

### 🎵 Work In Progress: Currently in early development!

This project aims to evolve into a plugin that provides advanced playback control on Spotify through automated actions and smarter queue management. It’s inspired by my personal desire for more flexibility and precision when listening to music.

By the end of development, I hope to implement the following key features:

1. Context-aware playback chaining

   Automatically queue specific songs to follow one another when certain tracks are played. This is especially useful for fans of music albums where some songs are meant to flow seamlessly into the next. In shuffle mode, this feature ensures those transitions still happen the way the artist intended.

2. Improved queue manipulation

   Offer greater control over managing songs in the queue. For example, if you add several songs to the end of the queue and want one of them to play next, you currently have to drag it manually to the top. This plugin will make it easier to prioritize newly added songs without interrupting your listening flow.

### ✅ Current Functionality

As of now, the project is still a small Python program that uses the Spotify Web API to:

1. Search for an artist by name and Retrieve and display their top 10 most streamed tracks in Australia

### 📁 Files

- main2.py: Core script that lets you input an artist's name in the terminal and returns their top 10 songs.
- main.py: A minimal script to verify that your Spotify API credentials are working. It prints an access token.
- .env: You need to add this file yourself (see instructions below).

### 🚀 How to Use

1. Clone the repository

```
git clone https://github.com/yourusername/spotify-playback-plugin.git
cd spotify-playback-plugin
```

2. Set up the `.env` file. Create a `.env` file in the root of the project with the following:

```
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
```

You can get these from the [Spotify Developer Dashboard.](https://developer.spotify.com.com)

3. Run the program by using `python main2.py
`. Follow the prompt by entering the artist name and you shall see the top 10 most listened song of that artist!

### 🛠️ Future Plans

This is just the beginning! I'm still learning how to integrate deeper features using Spotify's API. Planned improvements include:

1. Queue automation based on triggers
2. Custom playback rules and routines

### 📚 Learning Notes

This project is part of my ongoing exploration of APIs and automation. Any suggestions or contributions are welcome!
