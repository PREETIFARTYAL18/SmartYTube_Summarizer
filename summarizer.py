import torch
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline

summarizer_model = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")
def extract_video_id(url):
    if "v=" in url:
        return url.split("v=")[-1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")[0]
    else:
        raise ValueError("Invalid YouTube URL")


from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable

def get_transcript(video_url):
    video_id = extract_video_id(video_url)
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry['text'] for entry in transcript])
    except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable):
        raise Exception("Transcript not available for this video.")



def summarize_text(text):
    # Chunking because transformer models have input size limits
    max_len = 1000
    chunks = [text[i:i+max_len] for i in range(0, len(text), max_len)]
    summary = ""
    for chunk in chunks:
        result = summarizer_model(chunk, max_length=130, min_length=30, do_sample=False)
        summary += result[0]['summary_text'] + " "
    return summary.strip()

