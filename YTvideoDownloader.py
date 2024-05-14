#Importing the Youtube library from pytube
from pytube import YouTube

#fuction that takes two arguments
def download_video(url, save_path):
    try:
         # Creating a YouTube object for the provided URL
        yt = YouTube(url)

         # Filtering the streams to include only progressive MP4 streams
        streams = yt.streams.filter(progressive=True, file_extension="mp4")

         # Getting the stream with the highest resolution
        highest_res_stream = streams.get_highest_resolution()

         # Downloading the selected stream to the specified save path
        highest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully!")

    except Exception as e:
        print(e)
#url of the video that you want to download
url = "https://youtu.be/K87aFjB7Ff0?si=NNDFBmHkHRSfooWN"

# path for download the video
save_path = "C:/Users/3com/Downloads"

#calling the function
download_video(url, save_path)
