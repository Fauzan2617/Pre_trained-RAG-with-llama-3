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

