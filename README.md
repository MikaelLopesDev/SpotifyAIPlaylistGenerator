### 🎵 Spotify AI Playlist Generator

---

### 🚀 Project Overview

This project is an **intelligent playlist generator** that leverages the Spotify API in conjunction with a **Large Language Model (LLM)** from Google to create personalized music playlists. Instead of relying solely on standard recommendation algorithms, this system uses the power of AI to understand and enhance your musical preferences.

The process is fully automated and designed for efficiency:
1.  The Python script authenticates with the user's Spotify account using **OAuth 2.0** and the **Spotipy library**.
2.  It retrieves the user's top artists and tracks over a specified time range, utilizing the `current_user_top_artists` and `current_user_top_tracks` endpoints.
3.  This user data is then sent to the **Gemini 2.5 Flash model** via the Google GenAI API. The model, guided by a specific system instruction, generates a list of new music recommendations.
4.  The script then uses the `sp.search` endpoint to find the unique track IDs for each recommended song.
5.  Finally, it creates a new playlist and populates it with the recommended tracks using the `playlist_add_items` endpoint, providing a seamless user experience.

The core objective is to transform the music discovery experience by offering an intelligent, automated, and personalized way to find new music you'll love.

### ✨ Key Features

-   **Personalized Recommendations**: The LLM analyzes your top listening data (artists and tracks) to suggest new songs that align with your taste.
-   **Automated Playlist Generation**: The recommended tracks are automatically added to a new playlist created directly in your Spotify account.
-   **Genre-Specific Recommendations**: The system can be instructed to generate a list of songs limited to a specific genre, allowing for targeted music discovery.
-   **LLM Integration**: Utilizes the **Google Gemini 2.5 Flash** model to provide sophisticated, context-aware, and creative music recommendations.
-   **Robust API Handling**: Manages authentication and data retrieval from the Spotify and Google APIs, handling requests and processing responses in **JSON format**.
-   **Modular Codebase**: The project is structured with a class-based approach, making it easy to understand, extend, and maintain.
