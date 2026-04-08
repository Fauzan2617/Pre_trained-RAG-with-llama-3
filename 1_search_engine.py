# Digunakan untuk membaca file berbasis text
from langchain_community.document_loaders import TextLoader
# Digunakan dalam memecah text menggunakan splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
# Memmuat model dari hungging face
from langchain_huggingface import HuggingFaceEmbeddings
# bertugas sebagai vector database
from langchain_chroma import Chroma
# digunakan dalam path 
import os

#===========================
# 1. Load Data
#===========================
print ("Memuat Dokument....")

# Membuat loader untuk membaca file database "katalog_produk.txt"
loader = TextLoader("katalog_produk.txt")

# Membaca isi file dan mengubahnya jadi format Document (format LangChain)
documents = loader.load()

#===========================
# 2. chunking (memecah teks jadi bgaian kecil)
#===========================

print ("Memecah dokument menjadi chunks")

# Membuat objek text splitter
text_splitter = RecursiveCharacterTextSplitter (
    chunk_size = 200, # Maksimal 200 karakter per potongan
    chunk_overlap = 50 # setiap potongan overlap 50 karakter agar konteks tidak hilang
)

# Fungsi memecah document menjadi beberapa bagian
chunks = text_splitter.split_documents(documents)

#========================
# 3. Embedding (Ubah teks jadi angka)
#========================

print ("Mengunduh/Memuat model embedding Hungging Face...")

# Menggunakan model embedding gratis dari hungging face
# Model ini akan mengubah teks menjadi vektor
embeddings = HuggingFaceEmbeddings (
    model_name = "all-MiniLM-L6-v2" # model ringan dan cepat hanya untuk embedding
)

#=====================
# 4. Simpan Ke Vector Database
#=====================

print ("Menyimpan ke vector Database...")

# Membuat vector database menggunakan Chroma 
vectorstore = Chroma.from_documents(
    documents = chunks,             # Data yang dipecah    
    embedding = embeddings,         # Model untuk mengubah teks menjadi vektor 
    persist_directory = "./db"      # Lokasi penyimpanan database
)

# Menampilkan log bahwa proses selesai
print ("Selesai Database vektor berhasil dibuat di folder '/db'.")
