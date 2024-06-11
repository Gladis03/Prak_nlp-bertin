import pandas as pd
import streamlit as st
from googleapiclient.discovery import build
import os

# YouTube API Key
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
youTubeApiKey = "YOUR_YOUTUBE_API_KEY"

# Function to get all comments and replies
def get_all_comment(video_id):
    youtube = build('youtube','v3', developerKey=youTubeApiKey)
    data_video = [["Nama", "Komentar", "Waktu", "Likes", "Reply Count"]]
    param_comment = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults="100",
        textFormat="plainText"
    )

    while True:
        data_comment = param_comment.execute()
        for item in data_comment["items"]:
            name = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            published_at = item["snippet"]["topLevelComment"]["snippet"]["publishedAt"]
            likes = item["snippet"]["topLevelComment"]["snippet"]["likeCount"]
            replies = item["snippet"]["totalReplyCount"]
            data_video.append([name, comment, published_at, likes, replies])

            if replies > 0:
                parent = item["snippet"]["topLevelComment"]["id"]
                param_replies = youtube.comments().list(
                    part="snippet",
                    maxResults="100",
                    parentId=parent,
                    textFormat="plainText"
                )
                data_replies = param_replies.execute()
                for reply in data_replies["items"]:
                    reply_name = reply["snippet"]["authorDisplayName"]
                    reply_comment = reply["snippet"]["textDisplay"]
                    reply_published_at = reply["snippet"]["publishedAt"]
                    reply_likes = reply["snippet"]["likeCount"]
                    data_video.append([reply_name, reply_comment, reply_published_at, reply_likes, ""])

        if 'nextPageToken' in data_comment:
            next_token = data_comment['nextPageToken']
            param_comment = youtube.commentThreads().list_next(param_comment, data_comment)
        else:
            break

    df = pd.DataFrame({
        "Nama": [i[0] for i in data_video],
        "Komentar": [i[1] for i in data_video],
        "Waktu": [i[2] for i in data_video],
        "Likes": [i[3] for i in data_video],
        "Reply Count": [i[4] for i in data_video]
    })

    return df

# Streamlit App
def main():
    st.title("YouTube Comment Scraper")

    video_id = st.text_input("Enter YouTube Video ID:")
    if st.button("Scrape Comments"):
        if video_id:
            df = get_all_comment(video_id)
            st.write(df)

if __name__ == "__main__":
    main()
