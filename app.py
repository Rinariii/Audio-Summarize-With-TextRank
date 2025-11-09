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

# === Setup NLTK ===
nltk.download("punkt")

# === Streamlit UI ===
st.set_page_config(page_title="🎧 Audio Summarizer (Whisper + BERT)", layout="wide")
st.title("🎙️ Audio → Text → Summary")
st.markdown("This app transcribes an audio file using **Whisper** and summarizes it with **BERT-based TextRank**.")

# === Upload audio file ===
uploaded_file = st.file_uploader("📁 Upload your audio file (mp3, wav, m4a, webm, etc):", type=["mp3", "wav", "m4a", "webm"])

if uploaded_file is not None:
    # === Save temp file ===
    with NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    # === Convert to WAV ===
    output_wav = "audio_clean.wav"
    ffmpeg.input(tmp_path).output(output_wav, ac=1, ar=16000).run(overwrite_output=True)

    # === Select model ===
    model_size = st.selectbox("Choose Whisper model size:", ["tiny", "base", "small", "medium", "large"], index=2)

    # === Transcribe ===
    if st.button("🚀 Transcribe and Summarize"):
        with st.spinner("Transcribing audio using Whisper... ⏳"):
            model = whisper.load_model(model_size)
            result = model.transcribe(output_wav, fp16=False, language="en")
            text = result["text"]

        st.subheader("📝 Transcribed Text:")
        st.write(text)

        # === TextRank Summarization ===
        st.markdown("---")
        st.subheader("🧠 Summarized Text (TextRank + BERT Embedding)")

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

        with st.spinner("Summarizing text... 🤖"):
            summary = textrank_with_embeddings(text, n_sentences=8)

        st.success("✅ Summary generated successfully!")
        st.write(summary)

        # === Download Button ===
        st.download_button("💾 Download Summary", summary, file_name="summary.txt")

        # Cleanup
        os.remove(tmp_path)
else:
    st.info("⬆️ Please upload an audio file to start.")
