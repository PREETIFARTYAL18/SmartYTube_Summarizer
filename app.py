import streamlit as st
from summarizer import get_transcript, summarize_text

st.set_page_config(page_title="SmartTube Summarizer", page_icon="🎥")

st.title("🎥 SmartTube Summarizer")
st.subheader("Summarize any YouTube video in seconds using AI!")

url = st.text_input("🔗 Enter YouTube Video URL:")

if st.button("Summarize Video"):
    if url:
        try:
            with st.spinner("Fetching transcript and summarizing..."):
                transcript = get_transcript(url)
                summary = summarize_text(transcript)
            st.success("Summary generated successfully!")
            st.markdown("### 📝 Summary:")
            st.write(summary)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter a valid YouTube URL.")
