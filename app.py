import streamlit as st
import requests

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="AI Guru Toolkit",
    layout="wide",
)

# --- KONSTANTA API (SESUAI DOKUMENTASI BARU) ---
API_URL = "https://taraka.id/apigate/nvidia.php" 

# --- Data Prompt (Dipersingkat untuk kejelasan) ---
PROMPT_OPTIONS = {
    "Ringkasan Pembelajaran Mendalam": """Buatkan informasi mengenai aktivitas pembelajaran, dimulai dari info umum (judul), Tujuan pembelajaran (dengan Taksonomi SOLO, dimulai dari uni-struktural), Fase pengalaman belajar (memahami, menerapkan, merefleksikan), Asesmen, Alternatif Media/Teknologi Pembelajaran, Penerapan Prinsip Pembelajaran (berkesadaran/mindful-reflective) selain/exclude meditasi-pernafasan, bermakna (meaningful) dan menggembirakan(joyful)), Dimensi profil lulusan yang dapat dikaitkan (Kedelapan dimensi tersebut adalah: keimanan dan ketakwaan kepada Tuhan YME, kewargaan, penalaran kritis, kreativitas, kolaborasi, kemandirian, kesehatan, dan komunikasi. ) disertai penjelasan singkat
------------------
Contoh dan format:
Sistem Pencernaan (IPA SD)
... (dst) ...
PENERAPAN PRINSIP PEMBELAJARAN
DIMENSI PROFIL LULUSAN 
------------------------------
Topik materi pelajaran:""",
    "Ide Pembelajaran Mendalam (1)": """Saya meminta bantuan Anda untuk merancang sebuah rencana pembelajaran inovatif... (dst)""",
    "Ide 3 Fase Pengalaman Belajar": """Saya meminta bantuan Anda untuk merancang 3 fase pembelajaran... (dst)""",
    "Tujuan Pembelajaran": """Tujuan Pembelajaran dan indikator ketuntasan. Buat dalam tabel... (dst)""",
    # Tambahkan sisa opsi prompt Anda di sini
}

# --- Dimensi Profil Lulusan ---
ALL_DIMENSIONS = [
    "Keimanan dan ketakwaan kepada Tuhan YME", "Kewargaan", "Penalaran kritis",
    "Kreativitas", "Kolaborasi", "Kemandirian", "Kesehatan", "Komunikasi",
]

# --- Inisialisasi Session State ---
if "ai_result" not in st.session_state:
    st.session_state.ai_result = ""
if "loading" not in st.session_state:
    st.session_state.loading = False

# --- Fungsi Panggilan API (DIPERBAIKI TOTAL) ---
def call_taraka_api(prompt_text):
    """
    Fungsi untuk memanggil API Taraka.id
    (Disesuaikan dengan dokumentasi curl yang baru).
    """
    
    # 1. Headers (Sesuai dokumentasi baru)
    headers = {
        "Content-Type": "application/json",
    }
    # --- Tidak ada API Key / Authorization di sini ---
    # Jika ternyata diperlukan, tambahkan di 'headers'
    
    # 2. Data/Payload (Sesuai dokumentasi baru)
    # Kita tambahkan system prompt default yang relevan untuk konteks aplikasi
    system_prompt = "Anda adalah AI Guru, asisten ahli dalam desain pembelajaran dan pedagogi untuk guru di Indonesia. Jawab dengan lengkap dan terstruktur."
    
    data = {
        "prompt": prompt_text,
        "system": system_prompt
    }

    # 3. Lakukan Panggilan API
    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=120)
        
        # Cek jika ada error HTTP (spt 401, 403, 404, 500)
        response.raise_for_status() 

        # 4. Ambil Hasil (Sesuai dokumentasi baru)
        # Dokumentasi menunjukkan respons-nya adalah Teks Murni, BUKAN JSON.
        # Kita bersihkan tanda kutip jika API mengembalikannya ("Hasil" -> Hasil)
        ai_content = response.text.strip().strip('"') 
        
        if not ai_content:
            st.error("API mengembalikan respons kosong.")
            return None
            
        return ai_content

    except requests.exceptions.HTTPError as http_err:
        # Tampilkan pesan error yang lebih jelas dari server
        st.error(f"HTTP error terjadi: {http_err}. Respon server: {response.text}")
    except requests.exceptions.ConnectionError as conn_err:
        st.error(f"Error Koneksi: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        st.error(f"Permintaan Timeout: {timeout_err}")
    except requests.exceptions.RequestException as err:
        st.error(f"Error request API: {err}")
    except Exception as e:
        st.error(f"Terjadi error yang tidak terduga: {e}")
        
    return None

# --- UI Sidebar (Input) ---
with st.sidebar:
    st.image("https://blogger.googleusercontent.com/img/a/AVvXsEiauoRQ7i9fcn7yR25Se_NteOxPGJkajAdKl1nhb50wxUY8bzz93j4o-1wPpaBCLPiuM8T-lJtBi1S_3tUv5nKhsWmoMOWtR5r34de5osbK-d8m0S6YncVyNi2xRZyfenLKmTNdBVta5JjVKnYnSBPQCYnMZferjot6AJDjk3q4fMbFx3czh4Be-QWJigI0=s454", width=100)
    st.header("🤖 AI Toolkit Pembelajaran")
    
    # 1. Dropdown Komponen
    selected_prompt_name = st.selectbox(
        "Pilih Komponen Toolkit:",
        options=list(PROMPT_OPTIONS.keys()) # Ubah ke list
    )
    
    # 2. Input Topik Materi
    topik_materi = st.text_input("Topik Materi Pelajaran:", placeholder="Contoh: Sistem Pencernaan")
    
    # 3. Checkbox Dimensi
    st.markdown("##### Dimensi Profil Lulusan")
    selected_dimensions = st.multiselect(
        "Pilih dimensi yang relevan:",
        options=ALL_DIMENSIONS
    )
    
    st.divider()
    
    # 4. Tombol Generate
    if st.button("🚀 Generate", use_container_width=True, type="primary"):
        if not topik_materi:
            st.warning("Silakan masukkan Topik Materi Pelajaran.")
        else:
            # Set status loading
            st.session_state.loading = True
            st.session_state.ai_result = "" # Kosongkan hasil lama
            
            # --- Membangun Prompt (Sama seperti sebelumnya) ---
            base_prompt = PROMPT_OPTIONS[selected_prompt_name]
            dimensions_text = "Tidak ada dimensi yang dipilih."
            if selected_dimensions:
                dimensions_text = "\n- " + "\n- ".join(selected_dimensions)
            
            final_prompt_to_send = (
                f"{base_prompt} "
                f"{topik_materi}\n\n"
                f"DIMENSI PROFIL LULUSAN YANG DIKAITKAN:\n"
                f"{dimensions_text}"
            )
            
            # --- Memanggil API ---
            # (Ini akan berjalan saat tombol ditekan)
            ai_response = call_taraka_api(final_prompt_to_send)
            
            if ai_response:
                st.session_state.ai_result = ai_response
            
            # Selesai loading
            st.session_state.loading = False
            st.rerun() # Jalankan ulang skrip untuk menampilkan hasil

# --- UI Halaman Utama (Hasil) ---
st.title("AI Guru Toolkits")
st.markdown("Hasil generate akan muncul di bawah ini.")
st.divider()

# Tampilkan hasil dalam 1 kolom utama
if st.session_state.loading:
    with st.spinner("🤖 AI sedang berpikir, mohon tunggu..."):
        # Tahan tampilan spinner saat loading
        pass
elif st.session_state.ai_result:
    st.markdown("### Hasil Generate AI")
    st.markdown(st.session_state.ai_result) # Tampilkan sebagai markdown
else:
    st.info("Silakan isi input di sidebar kiri dan klik 'Generate'.")
