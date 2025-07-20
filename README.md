# SmartYTube_Summarizer
SmartTube Summarizer is an AI-powered Python tool that extracts YouTube video transcripts and generates concise summaries using HuggingFace Transformers. Built with Streamlit, it's perfect for students, researchers, and professionals.

# Features

- 🔗 Accepts YouTube video links
- 📝 Extracts available subtitles/transcripts using `youtube-transcript-api`
- 🤖 Summarizes content using `facebook/bart-large-cnn` transformer model
- 💻 User-friendly interface with Streamlit
- ⚠️ Handles errors for unavailable transcripts

# File Structure

├── app.py # Streamlit app interface
├── summarizer.py # Transcript extraction & summarization logic
├── requirements.txt # Python dependencies

# 🛠echnologies Used

- Python 3.x
- Streamlit
- HuggingFace Transformers (BART)
- youtube-transcript-api

## 🔧 Installation

# 1. Clone the Repository
git clone https://github.com/your-username/SmartTubeSummarizer.git
cd SmartTubeSummarizer
# 2. Create Virtual Environment (Optional but Recommended)
python -m venv env
env\Scripts\activate    # For Windows
# 3. Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt
# 4. Fix Keras Conflict (Important)
pip uninstall keras -y
pip install keras==2.11.0
pip install tensorflow==2.11.0
# ▶️ Running the App
streamlit run app.py
Open the browser at: http://localhost:8501

# Sample YouTube Links (With Transcripts)
Try using one of these videos:

https://www.youtube.com/watch?v=2ePf9rue1Ao

https://www.youtube.com/watch?v=3TBx5P0vUew

https://www.youtube.com/watch?v=7_LPdttKXPc

#  Limitations
Only works with videos that have publicly available subtitles

Long transcripts are summarized in chunks due to model limits

Language is limited to English for now

# Future Enhancements
Download summary as .txt or audio (gTTS)
Support for multi-language transcripts
Summary formatting (bullet points, highlights)
Deployment on Streamlit Cloud

# Author
Preeti Fartyal

📄 License
This project is licensed under the MIT License.

