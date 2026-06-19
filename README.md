# 🦙 Pre-trained RAG with Llama 3

Sebuah implementasi sistem **Retrieval-Augmented Generation (RAG)** menggunakan *Large Language Model* **Llama 3**. Sistem ini dirancang secara khusus untuk membaca, memahami, dan mencari informasi secara cerdas dari sebuah *knowledge base* lokal berupa katalog produk. 

Proyek ini sangat ideal untuk diimplementasikan sebagai inti dari *chatbot* layanan pelanggan atau mesin pencari internal bisnis (seperti untuk asisten virtual Kedai Diens), di mana AI dapat menjawab pertanyaan spesifik terkait ketersediaan, deskripsi, atau harga produk berdasarkan data yang diberikan.

---

## 📁 Struktur Repositori

Berdasarkan arsip repositori, proyek ini terdiri dari beberapa file utama:

- `1_search_engine.py` : Skrip utama Python yang mengeksekusi *pipeline* RAG. Skrip ini bertugas memproses dokumen, melakukan pencarian berbasis vektor, dan menghubungkan konteks yang ditemukan (dari katalog) ke dalam *prompt* Llama 3.
- `katalog_produk.txt` : Dokumen *knowledge base* yang berisi informasi lengkap mengenai daftar produk. File ini menjadi acuan utama AI agar tidak berhalusinasi saat menjawab.
- `requirements.txt` : Daftar *library* dan dependensi Python yang dibutuhkan untuk menjalankan *script* mesin pencari ini.
- `.gitignore` : Berkas konfigurasi Git untuk mengabaikan file sementara atau konfigurasi lokal agar tidak ter-*commit* ke repositori.

---

## ⚙️ Persyaratan Sistem (Prerequisites)

Untuk menjalankan proyek RAG ini, pastikan Anda menggunakan lingkungan (*environment*) Python yang sudah terisolasi. Instal semua dependensi yang disyaratkan dengan menjalankan perintah berikut di terminal:

```bash
pip install -r requirements.txt
```

---

## 🚀 Cara Menjalankan

1. **Siapkan Data:** Buka file `katalog_produk.txt` dan pastikan data produk yang ada di dalamnya sudah aktual. Anda bisa menambahkan atau memodifikasi daftar produk sesuai kebutuhan operasional.
2. **Jalankan Mesin Pencari:** Setelah dependensi terinstal, jalankan sistem pencarian dengan mengeksekusi file Python utamanya:
   ```bash
   python 1_search_engine.py
   ```
3. Sistem RAG akan mulai memproses teks katalog dan siap menerima *query* atau pertanyaan terkait produk tersebut dengan memanfaatkan kemampuan *reasoning* dari Llama 3.

---

## 💡 Arsitektur Singkat
Sistem ini menggunakan pendekatan *RAG (Retrieval-Augmented Generation)*, yang berarti:
1. **Retrieval:** Saat ada pertanyaan (misal: "Apa menu terlaris?"), sistem akan mencari paragraf paling relevan di dalam `katalog_produk.txt`.
2. **Augmented Generation:** Informasi relevan tersebut disisipkan ke Llama 3, sehingga Llama 3 memberikan jawaban akurat berdasarkan data katalog Anda, bukan dari data acak di internet.
