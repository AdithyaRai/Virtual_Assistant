# Astra - A Voice-Controlled Virtual Assistant

## Overview

Astra is a simple voice-controlled virtual assistant built using Python. It leverages the `speech_recognition` library for voice input, `pyttsx3` for text-to-speech output, and other libraries for web browsing, system control, and web scraping.

## Features

*   **Voice-Controlled Commands:**  Interact with the assistant using voice commands.
*   **Web Browsing:** Open websites like Instagram, Snapchat, Facebook, YouTube, and Google.
*   **Google Search:** Perform Google searches and speak a summary of the results.
*   **System Control:**  Shutdown the computer.
*   **Time Announcement:**  Get the current time.
*   **Text-to-Speech Output:**  The assistant speaks responses and information.
*   **Fallback Input:** If voice recognition fails, you can type commands.

## Dependencies

*   **speech\_recognition:** For converting speech to text.
    ```bash
    pip install SpeechRecognition
    ```
*   **pyttsx3:** For converting text to speech.
    ```bash
    pip install pyttsx3
    ```
*   **requests:** For making HTTP requests (used for web scraping).
    ```bash
    pip install requests
    ```
*   **beautifulsoup4:** For parsing HTML (used for web scraping).
    ```bash
    pip install beautifulsoup4
    ```
*   **urllib:** For encoding URLs. (Part of the Python standard library)
*   **webbrowser:** For opening websites. (Part of the Python standard library)
*   **os:** For system commands (like shutdown). (Part of the Python standard library)
*   **datetime:** For getting the current time. (Part of the Python standard library)
*   **sys:** For exiting the program. (Part of the Python standard library)

*   **PyAudio (Windows - Optional):** For microphone support.  If you encounter microphone errors, install PyAudio using `pipwin`.
    ```bash
    pip install pipwin
    pipwin install pyaudio
    ```

## Setup

1.  **Install Python:** Make sure you have Python 3.6 or higher installed.
2.  **Install Dependencies:** Use `pip` to install the required libraries.  Run the following commands in your terminal:
    ```bash
    pip install SpeechRecognition pyttsx3 requests beautifulsoup4
    ```
3.  **(Optional) Install PyAudio (Windows):** If you are on Windows and experience microphone issues, install PyAudio:
    ```bash
    pip install pipwin
    pipwin install pyaudio
    ```
4.  **Download the Code:** Download the `p3.py` file.
5.  **Run the Script:** Execute the script from your terminal:
    ```bash
    python p3.py
    ```

## Usage

1.  **Run the script:** Execute `p3.py` from your terminal.
2.  **Speak Commands:**  Speak commands clearly into your microphone.  Some example commands are:
    *   "Hello"
    *   "What time is it?"
    *   "Astra search \[your search query]" or "Search \[your search query]"
    *   "Open Instagram"
    *   "Shutdown" (requires confirmation)
    *   "Exit" or "Bye"
    *   "Test TTS" (tests the text-to-speech engine)
3.  **Fallback Input:** If the voice recognition fails, the script will prompt you to type the command in the terminal.

## Troubleshooting

*   **Microphone Issues:**
    *   Ensure your microphone is properly connected and configured.
    *   Make sure your operating system grants microphone access to Python.
    *   If you're on Windows, try installing PyAudio using `pipwin`.
*   **Speech Recognition Errors:**
    *   Speak clearly and slowly.
    *   Reduce background noise.
    *   Check your internet connection (speech recognition uses an online service).
*   **TTS Engine Errors:**
    *   Ensure your audio drivers are up to date.
    *   Try a different voice.
*   **Web Scraping Issues:**
    *   If the Google search feature isn't working, it's likely because Google has changed its HTML structure. Inspect the HTML source of a Google search results page and update the class names in the `scrape_google` function accordingly.
*   **Shutdown Issues:**
    *   Ensure you are running the script from a terminal with sufficient privileges to shut down the system.
    *   If the `shutdown` command is not recognized, make sure the full path to `shutdown.exe` is used (e.g., `"C:\\Windows\\System32\\shutdown /s /t 1"`).

## Code Structure

*   **`p3.py`:** The main script containing the virtual assistant logic.
*   **`speak(text)`:**  Function to convert text to speech using `pyttsx3`.
*   **`listen()`:** Function to capture audio from the microphone and convert it to text using `speech_recognition`.
*   **`processCommand(command)`:** Function to process the recognized command and perform the corresponding action.
*   **`scrape_google(query)`:** Function to scrape Google search results (title and snippet) for a given query.

## Important Notes

*   **Web Scraping:** The `scrape_google` function relies on web scraping, which can be fragile and may break if Google changes its HTML structure. Consider using the official Google Search API for a more reliable solution.
*   **Error Handling:** The code includes basic error handling, but you may want to add more robust error handling to catch specific exceptions and provide more informative error messages.
*   **Permissions:** The shutdown command requires appropriate permissions. You may need to run the script as an administrator.
*   **User-Agent:** The `scrape_google` function sets a User-Agent to avoid being blocked by Google. However, Google may still be able to detect that you are using a bot. Consider using a more sophisticated User-Agent rotation technique or using a proxy.

## Disclaimer

This project is for educational purposes only. Use it responsibly and be mindful of the terms of service of any websites you interact with.
