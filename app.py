import streamlit as st
import whisper
import ffmpeg
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import networkx as nx
import nltk
import os
from tempfile import NamedTemporaryFile
import shutil


# Setup NLTK
nltk.download("punkt_tab")

# Streamlit UI
st.set_page_config(page_title="Audio and Video Summarizer with Whisper", layout="wide")
st.title("Audio → Text → Summary")
st.markdown("This app transcribes an audio file using **Whisper** and summarizes it with **BERT-based TextRank**.")

uploaded_file = st.file_uploader("Upload your audio file (mp4,mp3, etc):", type=["mp4","mp3", "wav", "m4a", "webm"])

if uploaded_file is not None:
    with NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name
        output_wav = "audio_clean.wav"
    ffmpeg.input(tmp_path).output(
        output_wav,
        ac=1,          
        ar=16000,      
        format="wav" 
    ).run(overwrite_output=True)
    ffmpeg.input(tmp_path).output(output_wav, ac=1, ar=16000).run(overwrite_output=True)


    # Select
    model_size = st.selectbox(
    "Choose Whisper model size:",
    ["tiny", "base", "small"],
    index=2
)

    # Transcribe 
if st.button("Transcribe and Summarize"):
        with st.spinner("Transcribing audio using Whisper..."):
            model = whisper.load_model(model_size)
            result = model.transcribe(output_wav, fp16=False, language="en")
            text = result["text"]

        st.subheader("Transcribed Text:")
        st.write(text)

        # Summarization
        st.markdown("---")
        st.subheader("Summarized Text")

        def textrank_with_embeddings(text, n_sentences=8):
            sentences = nltk.sent_tokenize(text)
            if len(sentences) <= n_sentences:
                return text
            model = SentenceTransformer("all-MiniLM-L6-v2")
            embeddings = model.encode(sentences)
            sim_matrix = cosine_similarity(embeddings)
            nx_graph = nx.from_numpy_array(sim_matrix)
            scores = nx.pagerank(nx_graph)
            ranked = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
            return " ".join([s for _, s in ranked[:n_sentences]])

        with st.spinner("Summarizing text... "):
            summary = textrank_with_embeddings(text, n_sentences=8)

        st.success("Summary generated successfully!")
        st.write(summary)

        # Download Button
        st.download_button("Download Summary", summary, file_name="summary.txt")

        # Cleanup
        os.remove(tmp_path)
else:
    st.info("Please upload an audio file to start.")











