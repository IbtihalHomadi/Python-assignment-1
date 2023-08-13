import pytube

#downloads a Youtube video the given URL

def download_youtube_video(video_url):

    #Creat a Youtube object.
    youtube=pytube.YouTube(video_url)

    #Get the video's title and duration.
    title=youtube.title
    duration =youtube.duration

    #Get the video's stream.
    stream= youtube.streams

    #choose the highest resolution stream.
    stream = stream.get_highest_resolution()

    #start the downlod.
    stream.download()
    #print  message to the console.
    print("Download of {} ({}) completed.".format(title,duration))

if __name__ == "__main__":
    #Get the video.
    vedeo_url = input("Enter the Youtube video URL:")
    download_youtube_video(video_url)
    
