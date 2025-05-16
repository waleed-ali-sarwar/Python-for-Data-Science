# Python YouTube Downloader Console Application

## Overview
A console-based application to download YouTube videos using the `yt-dlp` library. The program allows the user to specify video quality and provides options to download multiple videos sequentially.

---

## Libraries Used
1.  OS  - For directory management and file path operations.
2.  yt-dlp  - A YouTube downloading library that supports multiple formats and quality settings.

---

## Features
- Download YouTube videos in the desired quality (Best, Worst, Custom).
- Allows downloading multiple videos in a single session.
- Displays download progress with speed and ETA.
- Includes `help` option for user guidance.
- Graceful exit using the `exit` command.

---

## How to Run
1. Ensure that Python is installed on your system.
2. Install the `yt-dlp` library using:
    bash
   pip install yt-dlp
    
3. Save the program file as `app.py`.
4. Open the command line and run the program:
   python app.py
    

---

## Usage
- To start downloading, enter a valid YouTube URL.
- Choose the desired quality by selecting one of the provided options.
- Type `help` to view usage instructions.
- Type `exit` to terminate the program.

---

## Example Custom Format:
- Example of a custom format string:
   
  bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best
   

---
Created by Waleed Ali Sarwar - www.linkedin.com/in/waleed-ali-sarwar
