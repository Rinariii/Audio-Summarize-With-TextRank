# Audio Summarizer with Text Rank

App web sederhana dengan Streamlit untuk membuat summary dari video/audio 

Aplikasi ini melakukan dua hal utama:
1.  **Transkrip:** Menggunakan model **Whisper** dari OpenAI untuk mengubah audio yang diunggah menjadi teks.
2.  **Peringkasan:** Menggunakan algoritma **TextRank** yakni *sentence embeddings* (`all-MiniLM-L6-v2`) untuk mengekstrak kalimat-kalimat paling penting dari transkrip tersebut.

## Cara Menjalankan
1.  **Clone Repositori**
    ```bash
    git clone [URL-REPO]
    cd audio-summarize-with-textrank
    ```

2.  **Instal FFmpeg**
    * **macOS:**
        ```bash
        brew install ffmpeg
        ```
    * **Ubuntu/Debian:**
        ```bash
        sudo apt-get update
        sudo apt-get install ffmpeg
        ```

3.  **Buat Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate
    # Untuk Windows: venv\Scripts\activate
    ```

4.  **Instal Packages**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Jalankan Aplikasi Streamlit**
    ```bash
    streamlit run app.py
    ```
    Buka `http://localhost:8501` di browser.

## Cara Deploy ke Streamlit 

1.  Fork repository ini ke akun GitHub.
2.  Di dashboard Streamlit, klik "New app".
3.  Hubungkan akun GitHub Anda dan pilih repositori ini.
4.  Pastikan file utamanya adalah `app.py`.
5.  Streamlit akan otomatis mendeteksi `requirements.txt` dan `packages.txt`. File `packages.txt` sangat penting untuk menginstal `ffmpeg` di *container*.
6.  Klik "Deploy".

## Fitur Aplikasi

1.  **Unggah File:** mengunggah file audio/video (mp4,mp3, wav, m4a, dll.).
2.  **Konversi Audio:** File tersebut dikonversi menggunakan `ffmpeg` menjadi format WAV mono 16kHz.
3.  **Transkripsi:** memilih ukuran model Whisper.
4.  **Peringkasan (TextRank):**
    * Transkrip dipecah menjadi kalimat-kalimat individual menggunakan `nltk`.
    * Setiap kalimat diubah menjadi vektor (embedding) menggunakan `sentence-transformers`.
    * Matriks kesamaan (cosine similarity) dihitung antar semua kalimat.
    * Grafik dibuat (`networkx`) di mana kalimat adalah node dan kesamaan adalah bobot tepian.
    * Algoritma PageRank (`nx.pagerank`) dijalankan pada grafik ini untuk "memperingkat" kalimat yang paling representatif/penting.
5.  **Tampilan:** Aplikasi menampilkan transkrip lengkap dan ringkasan.

## Dependency yang dipakai

* **UI:** `streamlit`
* **Transkripsi:** `openai-whisper`, `torch`
* **Pemrosesan Audio:** `ffmpeg-python`, `pydub` (dan `ffmpeg` di level sistem)
* **Peringkasan:** `sentence-transformers`, `scikit-learn`, `networkx`, `nltk`, `numpy`
