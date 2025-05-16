import yt_dlp
import os

# Function to download a YouTube video
# Arguments:
# - url: The YouTube video URL
# - output_path: The directory to save the downloaded video
# - quality: Desired quality ('best', 'worst', or custom format)
def download_youtube_video(url, output_path='./downloads', quality='best'):
    """
    Download a YouTube video using yt-dlp
    """
    
    # Ensure the output directory exists
    os.makedirs(output_path, exist_ok=True)
    
    # Download options
    ydl_opts = {
        'format': quality,
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False,
        'progress_hooks': [progress_hook],
    }
    
    try:
        # Initiating download
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading: {url}")
            ydl.download([url])
        print("\nDownload completed successfully!")
    except Exception as e:
        print(f"\nError downloading video: {e}")

# Function to display download progress
def progress_hook(d):
    """
    Displays download progress in percentage and speed
    """
    if d['status'] == 'downloading':
        progress = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        print(f"\rDownloading: {progress} at {speed}, ETA: {eta}", end='')

# Main function to handle user inputs and control the flow
if __name__ == "__main__":
    print("------------------------")
    print("YouTube Video Downloader")
    print("- For Personal Use Only. \n- This program is for educational purposes only.")
    print("------------------------")
    print("For exit, type 'exit'. For help, type 'help'.")
    
    while True:
        # Get YouTube URL or command from user
        url = input("Enter YouTube video URL (or type 'exit' to quit, 'help' for help): ").strip()
        
        # Help option
        if url.lower() == 'help':
            print("\nHELP:")
            print("1. Enter a valid YouTube video URL to start the download, By Pressing Mouse Right-Click Paste the Copied link on it.")
            print("2. Select the desired video quality: Best, Worst, or Custom.")
            print("3. After download completes, you can choose to download another video or exit.")
            print("4. Type 'exit' to terminate the program.")
            print("5. If you want to cancel downloading during the download process: Press - Ctrl + C. \n")
            continue
        
        # Exit option
        if url.lower() == 'exit':
            print("Exiting program. Goodbye!")
            break
        
        # Quality selection
        print("\nQuality options:")
        print("1. Best quality (default)")
        print("2. Worst quality")
        print("3. Custom format (advanced)")
        choice = input("Choose quality option (1-3, default 1): ").strip()
        
        # Determine quality setting
        if choice == '2':
            quality = 'worst'
        elif choice == '3':
            quality = input("Enter custom format (e.g., 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'): ")
        else:
            quality = 'best'
        
        # Start download
        download_youtube_video(url, quality=quality)
        
        # Prompt for another download
        another = input("\nDo you want to download another video? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Exiting program. Goodbye!")
            break
