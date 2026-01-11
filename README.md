# 🎙️ Audio Summarizer with TextRank

Aplikasi web berbasis **Streamlit** yang memungkinkan pengguna untuk merangkum konten dari file video atau audio secara otomatis. Proyek ini menggabungkan kekuatan **OpenAI Whisper** untuk transkripsi akurat dan algoritma **TextRank** untuk ekstraksi ringkasan yang cerdas.



---

## 🚀 Alur Kerja Aplikasi

1.  **Transkripsi:** Menggunakan model **Whisper** dari OpenAI untuk mengubah suara menjadi teks (Speech-to-Text).
2.  **Peringkasan (TextRank):** * Teks dipecah menjadi kalimat menggunakan `nltk`.
    * Setiap kalimat diubah menjadi *vector embedding* menggunakan model `all-MiniLM-L6-v2`.
    * Membangun graf kedekatan antar kalimat berdasarkan *cosine similarity*.
    * Menjalankan algoritma **PageRank** untuk menentukan kalimat mana yang paling representatif sebagai ringkasan.

---

## ✨ Fitur Utama

* 📤 **Multi-format Upload:** Mendukung file mp4, mp3, wav, m4a, dan lainnya.
* 🎧 **Auto-Conversion:** Konversi otomatis ke format standar (WAV mono 16kHz) menggunakan `ffmpeg`.
* 🤖 **Flexible Whisper Model:** Pilihan ukuran model Whisper (Tiny, Base, Small, dll.) sesuai kebutuhan kecepatan vs akurasi.
* 🧠 **Smart Summarization:** Ekstraksi kalimat paling penting tanpa menghilangkan konteks utama.
* 🖥️ **User-Friendly UI:** Tampilan bersih dan interaktif menggunakan Streamlit.

---

## 🛠️ Cara Menjalankan secara Lokal

### 1. Clone Repositori
```bash
git clone [URL-REPO]
cd audio-summarize-with-textrank

```

### 2. Instal FFmpeg (Wajib)

Aplikasi ini memerlukan FFmpeg untuk pemrosesan audio:

* **macOS:** `brew install ffmpeg`
* **Ubuntu/Debian:** `sudo apt-get update && sudo apt-get install ffmpeg`
* **Windows:** Unduh melalui [ffmpeg.org](https://ffmpeg.org/download.html) dan tambahkan ke PATH sistem.

### 3. Setup Virtual Environment

```bash
python -m venv venv
# Aktifkan venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

```

### 4. Instal Dependensi

```bash
pip install -r requirements.txt

```

### 5. Jalankan Aplikasi

```bash
streamlit run app.py

```

Akses di browser melalui: `http://localhost:8501`

---

## ☁️ Deployment (Streamlit Cloud)

Aplikasi ini siap di-deploy ke **Streamlit Cloud**:

1. Fork repositori ini ke akun GitHub Anda.
2. Buka dashboard Streamlit Cloud dan klik **"New app"**.
3. Pilih repositori dan set file utama ke `app.py`.
4. **Penting:** Pastikan file `packages.txt` ada di repositori agar sistem Cloud menginstal `ffmpeg` secara otomatis.
5. Klik **Deploy** dan tunggu proses hingga selesai!

---

## 📦 Tech Stack

| Komponen | Teknologi |
| --- | --- |
| **Antarmuka (UI)** | `Streamlit` |
| **Speech-to-Text** | `OpenAI Whisper`, `PyTorch` |
| **Audio Processing** | `ffmpeg-python` |
| **NLP & Ranking** | `Sentence-Transformers`, `NetworkX`, `NLTK`, `Scikit-learn` |
| **Data Handling** | `NumPy`, `Pandas` |
