import streamlit as st

# --- Konfigurasi Halaman ---
# Menggunakan layout "wide" agar mirip dengan aplikasi desktop
st.set_page_config(
    page_title="AI Guru Toolkits Multi-Editor",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- Data Prompt (Dari <select id="komponen">) ---
# Saya telah mengekstrak semua <option> dari HTML Anda ke dalam dictionary Python.
# Key adalah teks yang dilihat pengguna, Value adalah template prompt.
PROMPT_OPTIONS = {
    "Ringkasan Pembelajaran Mendalam": """Buatkan informasi mengenai aktivitas pembelajaran, dimulai dari info umum (judul), Tujuan pembelajaran (dengan Taksonomi SOLO, dimulai dari uni-struktural), Fase pengalaman belajar (memahami, menerapkan, merefleksikan), Asesmen, Alternatif Media/Teknologi Pembelajaran, Penerapan Prinsip Pembelajaran (berkesadaran/mindful-reflective) selain/exclude meditasi-pernafasan, bermakna (meaningful) dan menggembirakan(joyful)), Dimensi profil lulusan yang dapat dikaitkan (Kedelapan dimensi tersebut adalah: keimanan dan ketakwaan kepada Tuhan YME, kewargaan, penalaran kritis, kreativitas, kolaborasi, kemandirian, kesehatan, dan komunikasi. ) disertai penjelasan singkat
------------------
Contoh dan format:
Sistem Pencernaan (IPA SD)

TUJUAN PEMBELAJARAN
Siswa mampu mengidentifikasi organ dan enzim utama sistem pencernaan, menjelaskan hubungan proses pencernaan secara berurutan, serta menganalisis dampak pola makan terhadap kesehatan pencernaan dan merumuskan solusinya.

Rincian Tujuan (Taksonomi SOLO)

Unistruktural: Mengidentifikasi satu organ utama sistem pencernaan dan fungsinya (mis. lambung mencerna protein).
Multistruktural: Menyebutkan beberapa organ pencernaan dan enzim terkait beserta fungsinya.
Relasional: Menjelaskan hubungan antara organ, enzim, dan proses pencernaan dalam urutan yang logis.
Extended-Abstrak: Menganalisis dampak pola makan terhadap kesehatan pencernaan dan mengusulkan solusi untuk meningkatkan fungsi sistem pencernaan.

PENGALAMAN BELAJAR
1. MEMAHAMI

Fungsi: Mencerna makanan, menyerap nutrisi, buang sisa.
Organ:
Mulut: Mengunyah, amilase (karbohidrat).
Kerongkongan: Peristaltik.
Lambung: Pepsin (protein).
Usus Halus: Serap nutrisi (lipase, tripsin).
Usus Besar: Serap air, bentuk feses.
Anus: Buang feses.

Proses: Mekanis (kunyah, aduk), kimiawi (enzim), penyerapan, eliminasi.

2. MENERAPKAN

Buat Diagram: Sketsa alur makanan dan fungsi organ.
Analisis Makanan: Pilih menu (mis. nasi, ayam), identifikasi nutrisi dan organ pencerna.
Kuis: Enzim lemak? (Lipase) Organ serap air? (Usus besar)

3. MEREFLEKSIKAN

Pertanyaan: Mengapa pencernaan penting? Bagaimana diet memengaruhi usus?
Tindakan: Catat pola makan 1 hari, rencanakan perubahan (mis. tambah serat).
Kesehatan: Pelajari maag/sembelit, hubungkan dengan gaya hidup.

ALTERNATIF ASESMEN
Unistruktural: Sebutkan satu organ pencernaan dan fungsinya (contoh: Lambung mencerna protein).
Multistruktural: Tulis 3 organ pencernaan, enzim, dan nutrisi yang dicerna (mis. Mulut - Amilase - Karbohidrat).
Relasional: Buat poster proses pencernaan nasi dari mulut hingga usus halus, sertakan organ dan enzim terkait.
Extended-Abstrak: Buat rencana makan harian yang mendukung kesehatan pencernaan, jelaskan alasan pilihan makanan berdasarkan fungsi sistem pencernaan.


ALTERNATIF PEMANFAATAN MEDIA/PERAGA
Digital:
- Video animasi 2D/3D alur makanan.
- Augmented Reality (AR) organ pencernaan.
- Quiz interaktif (Kahoot, Quizizz).
- Aplikasi simulasi enzim dan reaksi kimia.
Non-digital / Hand-on:
- Pipa paralon + balon (model peristaltik).
- Model clay/foam organ pencernaan.
- Percobaan amilase pada roti (mengunyah sampai manis).
- Poster kertas manila dan spidol.
- Puzzle susun alur pencernaan.
PENERAPAN PRINSIP PEMBELAJARAN
DIMENSI PROFIL LULUSAN 
------------------------------
Topik materi pelajaran:""",
    "Ide Pembelajaran Mendalam (1)": """Saya meminta bantuan Anda untuk merancang sebuah rencana pembelajaran inovatif dan mendalam untuk topik materi pelajaran. Tuliskan pada bagian awal berupa tabel tujuan pembelajaran dengan menggunakan taksonomi SOLO dimulai dari uni-struktural(kolom 1: Level taksonomi SOLO, kolom 2 tujuan pembelajaran: kolom 3: Fase pembelajaran . Rencana pembelajaran secara umum harus terstruktur secara sistematis melalui tiga fase PENGALAMAN BELAJAR utama, yaitu MEMAHAMI, MENERAPKAN, dan MEREFLEKSIKAN. Untuk setiap fase tersebut, mohon rumuskan Tujuan Pembelajaran yang jelas, terukur, dan dikaitkan dengan level yang relevan dalam SOLO Taxonomy (misalnya, pra-struktural, uni-struktural, multi-struktural, relasional, atau abstrak diperluas) yang mencerminkan kedalaman pemahaman yang diharapkan. Tuliskan juga tujuan pembelajaran ini di awal, sebelum masuk tahapan belahar. Sangat penting bahwa setiap fase dan aktivitas di dalamnya secara eksplisit mengintegrasikan dan menerapkan tiga pendekatan pembelajaran mendalam: Mindful-Reflective Learning, di mana peserta didik memahami tujuan pembelajaran, termotivasi secara intrinsik, serta aktif meregulasi diri dalam merencanakan, melaksanakan, dan mengevaluasi cara belajar mereka secara reflektif; Meaningful Learning, di mana peserta didik menerapkan pengetahuan dalam situasi nyata, proses belajar berorientasi pada transfer belajar dan pemahaman mendalam (bukan hafalan), serta mengaktifkan pengetahuan awal; dan Joyful Learning, yang menciptakan suasana belajar positif, menantang, menyenangkan, memotivasi, dan melibatkan peserta didik secara kognitif serta emosional. Mohon sajikan ide aktivitas untuk setiap fase dalam format tabel yang terstruktur, mencakup kolom-kolom berikut: Fase Pengalaman Belajar (MEMAHAMI/MENERAPKAN/MEREFLEKSIKAN), Tujuan Pembelajaran (beserta level SOLO yang disebutkan), Penjelasan Singkat Fase (menguraikan kontribusi fase terhadap pemahaman topik dan bagaimana prinsip mindful, meaningful, joyful diterapkan secara umum di fase tersebut), Aktivitas Pembelajaran Spesifik (menjelaskan langkah-langkah kegiatan dengan menggunakan strategi dan alat/media pembelajaran yang bervariasi, dari yang sederhana hingga teknologi canggih, yang sesuai dengan topik materi), Asesmen (menjelaskan bagaimana kemajuan atau pencapaian tujuan pembelajaran diukur pada fase tersebut, baik formatif maupun sumatif), dan daftar Alat/Media Pembelajaran yang digunakan dalam aktivitas. Setelah penyajian tabel, saya meminta Anda untuk memberikan penjelasan akhir yang komprehensif mengenai bagaimana ketiga prinsip pembelajaran mendalam tersebut (mindful-reflective learning, meaningful learning, dan joyful learning) secara spesifik diterapkan dan terintegrasi dalam keseluruhan rancangan pembelajaran untuk topik materi yang telah dipilih, serta menjelaskan bagaimana setiap prinsip mendukung pencapaian tujuan pembelajaran pada masing-masing fase. Pada fase MEMAHAMI mencakup pengetahuan esensial, pengetahuan aplikatif dan pengetahuan nilai/karakter. Pada fase MENERAPKAN mencakup pada pemahaman yang lebih mendalam dan aplikasinya. Pada fase MEREFLEKSIKAN mencakup refleksi pembelajaran dan regulasi diri dan contoh praktis penerapan materi yang dipelajari dalam kehidupan sehari-hari baik untuk kehidupan pribadi maupun sosial-masyarakat  (contoh setelah belajar Sistem Pencernaan, siswa dapat mengatur menu makanan sehat sehari-hari dll). Pastikan output yang Anda berikan menggunakan bahasa yang profesional, jelas, dan mudah dipahami, Tuliskan alternatif Asesmen terkait tujuan pembelajaran, Alternatif Media/Teknologi Pembelajaran (digital dan non-digital), Penerapan Prinsip Pembelajaran (berkesadaran/mindful-reflective) selain/exclude meditasi-pernafasan, bermakna (meaningful) dan menggembirakan(joyful)), Dimensi profil lulusan yang dapat dikaitkan (Kedelapan dimensi tersebut adalah: keimanan dan ketakwaan kepada Tuhan YME, kewargaan, penalaran kritis, kreativitas, kolaborasi, kemandirian, kesehatan, dan komunikasi. ) disertai penjelasan singkat  Dibagian akhir tambahkan informasi kaitannya tentang oleh pikir, olah rasa dan olah raga dengan mengaitkan relevansi ke topik materi. Materi pelajaran adalah pada topik/tema berikut :  """,
    "Ide 3 Fase Pengalaman Belajar": """Saya meminta bantuan Anda untuk merancang 3 fase pembelajaran yaitu (1) Fase Memahami. (2)Fase Menerapkan dan (3) Fase Merefleksikan. Peran: Anda adalah seorang desainer instruksional dan fasilitator ahli. Tugas: Buatkan sebuah aktivitas pembelajaran mengenai topik yang akan saya berikan. mulailah dengan analisis tugas mencakup aspek utama: pertama, mendefinisikan konten dan tugas dengan mengidentifikasi kebutuhan kinerja, menentukan tugas yang harus dicapai, mengenali keterampilan serta pengetahuan yang diperlukan, dan memilih tugas untuk pengembangan instruksi; setelah itu jelaskan poin *(1) FASE MEMAHAMI* dan *(2) FASE MENERAPKAN*, ,masing2 fase berisi poin-poin mengidentifikasi langkah-langkah rumit dan menentukan urutan pelaksanaan serta pembelajaran tugas; kaitkan dengan tujuan pembelajaran, penguraian komponen operasional, identifikasi jenis pengetahuan (deklaratif, struktural, prosedural), pemilihan tugas prioritas, serta perancangan aktivitas, strategi, dan media pembelajaran yang sesuai; Target peserta adalah siswa/murid. lanjutkan *(3) FASE MEREFLEKSIKAN* yaitu buatkan aktivitas refleksi pembelajaran mengenai topik yang diberikan. Fokus Dimensi Refleksi: Aktivitas harus mencakup Dimensi Kognitif (Analisis Kritis Pengalaman Belajar Rekonstruksi Pengetahuan- Identifikasi Pola Pikir dan Asumsi), Dimensi Metakognitif (Kesadaran Proses Berpikir Sendiri - Evaluasi Strategi Pembelajaran-Pengaturan dan Monitoring Pemahaman), Dimensi Afektif (Eksplorasi Emosi Selama Proses Belajar- Refleksi Sikap dan Motivasi- Pengembangan Kesadaran Diri), Dimensi Praktis (Transformasi Pengalaman menjadi Praktik- Perencanaan Tindakan Perbaikan- Aplikasi Pembelajaran ke Konteks Nyata dan karier masa depan) dan Dimensi Sosial (Interpretasi Pengalaman dalam Konteks Sosial- Kolaborasi dan Berbagi Pemahaman). aktivitas dapat berupa daftar pertanyaan reflektif yang bisa langsung dijawab peserta atau dalam bentuk instruksi/penugasan. setelah itu susun penilaian/asesmen untuk mengukur kemampuan individu dalam pemahaman dan  kinerja menyelesaikan tugas. Format output: tuliskan analisis konten-tugas, judul tiap fase serta Penilaian/Asesmen dengan format Heading-2. Materi pelajaran adalah pada topik/tema berikut :  """,
    "Tujuan Pembelajaran": """Tujuan Pembelajaran dan indikator ketuntasan. Buat dalam tabel dengan setiap tujuan pembelajaran terdiri dari 1 atau lebih indikator.""",
    "Tujuan Pembelajaran (Dimensi Bloom)": """Tujuan Pembelajaran yang dituliskan dalam tabel dengan menggabungkan 2 dimensi (tuliskan tujuan pembelajaran dalam tabel dengan kombinasi dimensi pengetahuan (4 baris tabel: faktual-konseptual-prosedural-metakognitif) dan dimensi kognitif (6 kolom tabel: mengingat, memahami, mengaplikasi, menganalisis, mengevaluasi, kreasi)). (Di bagian bawah,tuliskan contoh soal untuk masing-masing tahap). Topik :""",
    "Tujuan Pembelajaran (Taksonomi SOLO 1)": """Tujuan Pembelajaran yang dituliskan dalam tabel dengan  SOLO taxonomy (4 baris, uni-struktural, multi struktural,relasional, extended-abstract) kolom kedua tuliskan indikator).Setelah itu buatkan Di bagian bawah tuliskan indikator, konsep kisi-kisi asesmen dan contoh soal untuk masing-masing tahap). Topik materi: """,
    "Tujuan Pembelajaran (Taksonomi SOLO 2)": """Tujuan Pembelajaran yang dituliskan dalam tabel dengan menggabungkan 2 dimensi (tuliskan tujuan pembelajaran dalam tabel dengan kombinasi dimensi pengetahuan (4 baris tabel: faktual-konseptual-prosedural-metakognitif) dan dimensi SOLO taxonomy (4 kolom, uni-struktural, multi struktural,relasional, extended-abstract)).Setelah itu buatkan konsep kisi-kisi asesmen berdasar SOLO taxonomy tersebut. (Di bagian bawah,tuliskan contoh indikator pencapaian kompetensi dan contoh soal untuk masing-masing tahap). Topik materi: """,
    "Uraian Materi": """Daftar Jabaran/uraian sub-materi penting Pembelajaran """,
    "Materi Prasyarat": """Daftar materi/pengetahuan/skill prasyarat yang perlu dikuasai siswa sebelum pembelajaran """,
    "Masalah Belajar Siswa": """Masalah pembelajaran kesalahan pemahaman dan titik kritis yang sering dihadapi siswa """,
    "Pertanyaan Pemantik": """Daftar Pertanyaan pemantik (guiding questions) (judul gunakan heading H2 dan tanpa subheading lain) yang memandu mengantarkan ke materi pembelajaran """,
    "Bahan Motivasi Belajar Siswa": """Daftar poin motivasi Mengapa  penting dan perlu bagi siswa untuk mempelajari materi ini (jika perlu, berikan contoh serta manfaat di kehidupan nyata serta karir masa depan) """,
    "Ide Aktivitas Pemantik Awal Belajar": """Aktivitas Pemantik Belajar (lesson hook)""",
    "Ide Pembelajaran Mendalam (2)": """Saya membutuhkan saran profesional dari Anda untuk merancang sebuah ide pembelajaran yang inovatif dan mendalam, yang difokuskan pada topik materi pelajaran. Mohon awali dengan menyusun sebuah paragraf yang menjelaskan Tujuan Pembelajaran secara komprehensif untuk topik tersebut, dan secara eksplisit mengaitkan berbagai tingkatan pencapaian tujuan ini dengan level-level yang relevan dalam SOLO Taxonomy (Structure of Observed Learning Outcome oleh Biggs and Collis, 1982), lengkap dengan rincian bagaimana setiap tahapan SOLO (mulai dari pra-struktural hingga abstrak diperluas) dapat tercermin dalam pemahaman peserta didik terhadap topik ini. Setelah itu, saya meminta Anda untuk mengembangkan ide aktivitas pembelajaran yang terstruktur dalam tiga fase utama: MEMAHAMI, MENERAPKAN, dan MEREFLEKSIKAN. Penting bagi setiap fase untuk secara holistik mengintegrasikan tiga pengalaman belajar kunci. Pertama, pada fase MEMAHAMI, fokuskan pada pencapaian pemahaman mendalam: rancanglah aktivitas yang dimulai dengan minimal tiga pertanyaan pemantik yang efektif untuk topik tersebut, yang bertujuan agar peserta didik memahami tujuan pembelajaran, termotivasi secara intrinsik, serta mampu mengaktifkan pengetahuan awal dan prasyarat mereka; sertakan juga bagaimana guru dapat menyampaikan setidaknya tiga poin motivasi tentang pentingnya mempelajari topik materi ini. Kedua, pada fase MENERAPKAN, tekankan pada penerapan atau aplikasi nyata (hands-on): rancanglah aktivitas di mana peserta didik secara aktif menerapkan pengetahuan mengenai materi pelajaran dalam berbagai situasi nyata, berikan minimal tiga contoh detail tentang bagaimana hal ini dapat dilakukan sesuai dengan materi, dan usulkan contoh konkret proyek atau pembelajaran berbasis masalah (Project/Problem-Based Learning) yang relevan dan menantang. Ketiga, pada fase MEREFLEKSIKAN, fasilitasi pembelajaran reflektif: rancanglah aktivitas yang memungkinkan peserta didik untuk membahas minimal tiga hikmah atau pelajaran penting yang telah mereka peroleh, berikan contoh bagaimana pembelajaran ini dapat ditransfer ke konteks yang berbeda atau dikaitkan dengan minimal tiga topik atau pelajaran lain, serta jelaskan bagaimana aktivitas tersebut mendukung pengembangan metakognisi peserta didik, di mana mereka aktif meregulasi diri dalam merencanakan, melaksanakan, dan mengevaluasi cara belajar mereka secara reflektif. Sebagai penutup, mohon jelaskan secara rinci dan dengan contoh praktis bagaimana ketiga prinsip pembelajaran fundamental—yaitu (a) mindful learning (kesadaran penuh dalam proses belajar), (b) meaningful learning (pembelajaran yang bermakna, menekankan pemahaman mendalam bukan sekadar menghafal informasi, serta melibatkan aktivasi pengetahuan awal dan pengembangan minat-bakat), dan (c) joyful learning (menciptakan suasana belajar yang positif, menggembirakan, menantang, menyenangkan, memotivasi, serta melibatkan peserta didik secara kognitif dan emosional)—secara konkret diterapkan dan terjalin dalam setiap fase pembelajaran (MEMAHAMI, MENERAPKAN, MEREFLEKSIKAN) dan setiap aktivitas yang telah Anda rancang sebelumnya. Pastikan seluruh penjelasan dan contoh selalu dikaitkan secara langsung dan relevan dengan topik materi yang telah ditentukan.  Dibagian akhir tambahkan informasi kaitannya tentang oleh pikir, olah rasa dan olah raga dengan mengaitkan relevansi ke topik materi. Materi pelajaran adalah pada topik/tema berikut : """,
    "Ide Pembelajaran Mendalam (3)": """saran profesional tentang ide pembelajaran dengan menuliskan paragraf terkait tujuan pembelajaran dikaitkan dengan SOLO taxonomy (the SOLO (structure of observed learning outcome) taxonomy developed by Biggs and Collis (1982) ) tuliskan rincian sesuai tahapannya. Setelah itu Kemudian  tulis ide aktivitas dgn menerapkan pendekatan pembelajaran mendalam yang  berdasar 3 PRINSIP PEMBELAJARAN dikombinasikan 3 PENGALAMAN BELAJAR. PRINSIP Pembelajaran yaitu (PRINSIP 1) pembelajaran berkesadaran (mindful-reflektif learning) (Peserta didik memahami tujuan pembelajaran dan termotivasi secara intrinsik untuk belajar. Peserta didik aktif meregulasi diri dalam belajar, merencanakan, melaksanakan, dan mengevaluasi reflektif cara belajar mereka.) , (PRINSIP 2) pembelajaran bermakna (meaningful learning) (Peserta didik menerapkan pengetahuan dalam situasi nyata,Proses belajar berorientasi pada kemampuan mengaplikasikan pengetahuan (learning tansfer), pemahaman mendalam bukan hanya menghafal informasi, melibatkan aktivasi pengetahuan awal), dan (PRINSIP 3) pembelajaran yang menggembirakan (joyful learning) (suasana belajar yang positif, menantang, menyenangkan, dan memotivasi, terlibat secara kognitif dan emosional). Prinsip tersebut dikombinasikan dengan 3 PENGALAMAN BELAJAR yaitu (PENGALAMAN 1) pemahaman mendalam, siswa termotivasi,terinspirasi,tidak hanya menghafal materi, (PENGALAMAN 2) aplikasi/penerapan dalam kehidupan nyata an bermanfaat secara nyata dan (PENGALAMAN 3) Refleksi, mampu melakukan refleksi hasil belajar, koneksi atau mengaitkan dengan konteks dan topik keilmuan lain dan kaitan dengan pembelajaran kelanjutan berikutnya. Jelaskan masing-masing poin tsb dalam tabel 3 baris pengalaman belajar dan 3 kolom prinsip pembelajaran. Jelaskan menuliskan rancangan aktivitas pembelajaran dengan menerapkan fase MEMAHAMI, MENERAPKAN, MEREFLEKSIKAN. dengan selalu dikaitkan dengan topik materi. Dibagian akhir tambahkan informasi kaitannya tentang oleh pikir, olah rasa dan olah raga dengan mengaitkan relevansi ke topik materi. Materi pelajaran adalah pada topik/tema berikut : """,
    "Ide Aktivitas Inti": """alternatif langkah (step-by-step) Aktivitas Belajar dari awal ketika siswa belum paham materi hingga akhirnya siswa paham konsep dan penerapannya. berikan cara dan trik yang memudahkan siswa belajar. fokuskan pada langkah didaktik-pedagogi dan spesifik pada materi """,
    "Ide Aktivitas Untuk Materi Sulit": """alternatif langkah (step-by-step) strategi Belajar dari awal ketika siswa belum paham materi hingga akhirnya siswa paham konsep dan penerapannya. berikan cara dan trik yang memudahkan siswa belajar (gunakan peraga jika perlu). fokuskan pada langkah didaktik-pedagogi dan spesifik pada materi yang disertai contoh-contoh yang memudahkan pemahaman dan gunakan prinsip yang sesuai dengan cara otak/kognisi bekerja. Jelaskan rasional/argumen mengapa guru perlu melakukan langkah tersebut misalnya untuk mengatasi miskonsepsi, kesulitan pemahaman materi, dan hambatan belajar terkait topik materi. """,
    "Ide Pembelajaran Berdiferensiasi (Kemampuan Siswa)": """Ide pembelajaran berdiferensiasi (differentiated instruction) untuk kelompok siswa yang memiliki kemampuan dan karakteristik yang berbeda beserta tugas yang sesuai. Tulis dalam tabel.""",
    "Ide Pembelajaran Berdiferensiasi (Proses-Konten-Produk)": """Ide pembelajaran berdiferensiasi (differentiated instruction) untuk kelompok siswa dalam kategori diferensiasi konten, proses dan produk. Tulis dalam tabel.""",
    "Ide Pembelajaran dg Gamifikasi": """Buatlah rencana aktivitas pembelajaran yang menerapkan pendekatan gamifikasi untuk suatu materi. Rincikan tujuan pembelajaran, deskripsi aktivitas, mekanisme permainan, aturan main, cara pemberian hadiah atau poin, serta metode evaluasi hasil belajar siswa. Sertakan contoh konkret seperti jenis tantangan, level atau tingkatan, fitur interaktif, dan bagaimana gamifikasi ini dapat meningkatkan motivasi dan pemahaman siswa terhadap materi tersebut. Topik materi: """,
    "Ide Pembelajaran Berbasis Pemecahan-Masalah (PBL)": """Ide pembelajaran berbasis problem-solving melibatkan investigasi dan penerapan konsep. Berikan statemen problem/masalah yang menantang dan menarik dengan bahasa yang mudah dipahami.""",
    "Ide Pembelajaran Berbasis Inkuiri": """Ide pembelajaran berbasis inquiry-based learning. Berikan langkah-langkah dengan detail.""",
    "Ide Pembelajaran Berbasis Proyek (PjBL)": """Ide pembelajaran berbasis project based learning dengan penerapan konsep dari mata pelajaran dan gunakan sintaks PjBL. tuliskan tujuan pembelajaran dan detail project yang harus dikerjakan. Tuliskan relevansi projek tsb dengan 4 kriteria kunci PjBL (dalam bentuk tabel 2 kolom 4 baris) berisi statemen pertanyaan penuntun (guiding question) yang jelas, konten materi pelajaran yang relevan, produk autentik yang dihasilkan dan kerja kolaboratif siswa. berikan arahan langkah yang harus dilakukan siswa. di akhir, berikan  alternatif langkah project yang mungkin dilakukan siswa sesuai sintaks PjBL (tuliskan dalam tabel). Tuliskan alternatif solusi jenis projek yang dapat dilakukan siswa, jika siswa tidak dapat menemukan idenya sendiri. """,
    "Ide pembelajaran (UBD)": """Ide pembelajaran yang dirancang dengan berbasis UBD (understanding by design). Berikan langkah-langkah tahapan dengan detail. Buatkan aktivitas pembelajaran melalui urutan fase pengenalan konsep, pengemb""",
}

# --- Dimensi Profil Lulusan (dari prompt dan HTML) ---
ALL_DIMENSIONS = [
    "Keimanan dan ketakwaan kepada Tuhan YME",
    "Kewargaan",
    "Penalaran kritis",
    "Kreativitas",
    "Kolaborasi",
    "Kemandirian",
    "Kesehatan",
    "Komunikasi",
]

# --- Inisialisasi Session State ---
# Diperlukan untuk menyimpan nilai editor dan item tersimpan
if "editor1_content" not in st.session_state:
    st.session_state.editor1_content = ""
if "editor2_content" not in st.session_state:
    st.session_state.editor2_content = ""
if "saved_items" not in st.session_state:
    st.session_state.saved_items = {} # Dict untuk menyimpan {judul: konten}

# --- Header / Navbar ---
logo_url = "https://blogger.googleusercontent.com/img/a/AVvXsEiauoRQ7i9fcn7yR25Se_NteOxPGJkajAdKl1nhb50wxUY8bzz93j4o-1wPpaBCLPiuM8T-lJtBi1S_3tUv5nKhsWmoMOWtR5r34de5osbK-d8m0S6YncVyNi2xRZyfenLKmTNdBVta5JjVKnYnSBPQCYnMZferjot6AJDjk3q4fMbFx3czh4Be-QWJigI0=s454"
st.logo(logo_url)
st.title("AI Guru Toolkits")
st.markdown("---")


# --- Layout Utama Aplikasi (3 kolom) ---
# Mirip dengan col-md-3, col-md-5, col-md-4
col_input, col_editor1, col_editor2 = st.columns([3, 5, 4])

# --- Kolom 1: Input ---
with col_input:
    st.header("🤖 AI Toolkit Pembelajaran")
    
    # 1. Dropdown Komponen
    selected_prompt_name = st.selectbox(
        "Pilih Komponen Toolkit:",
        options=PROMPT_OPTIONS.keys(),
        label_visibility="collapsed"
    )
    
    # 2. Input Topik Materi
    topik_materi = st.text_input("Topik Materi Pelajaran:")
    
    # 3. Checkbox Dimensi (menggunakan multiselect)
    st.markdown("##### Dimensi Profil Lulusan")
    selected_dimensions = st.multiselect(
        "Pilih dimensi yang relevan:",
        options=ALL_DIMENSIONS,
        label_visibility="collapsed"
    )
    
    # 4. Tombol Generate
    if st.button("🚀 Generate", use_container_width=True, type="primary"):
        # --- LOGIKA INTI ---
        # 1. Dapatkan template prompt yang dipilih
        base_prompt = PROMPT_OPTIONS[selected_prompt_name]
        
        # 2. Format dimensi yang dipilih
        dimensions_text = "Tidak ada dimensi yang dipilih."
        if selected_dimensions:
            dimensions_text = "\n- " + "\n- ".join(selected_dimensions)
            
        # 3. Gabungkan semua input menjadi satu prompt akhir
        # (Format ini meniru cara kerja aplikasi asli Anda)
        final_prompt_to_send = (
            f"{base_prompt}\n"
            f"{topik_materi}\n\n"
            f"DIMENSI PROFIL LULUSAN YANG DIKAITKAN:\n"
            f"{dimensions_text}"
        )
        
        # 4. SIMULASI: Tampilkan prompt di Editor 1
        # DI DUNIA NYATA: Anda akan mengirim 'final_prompt_to_send' ke API AI
        # dan menempatkan *respons* AI di 'st.session_state.editor1_content'.
        st.session_state.editor1_content = final_prompt_to_send
        st.toast("Prompt berhasil di-generate di Editor 1!")

# --- Kolom 2: Editor 1 (Hasil Generate) ---
with col_editor1:
    st.subheader("Editor 1: Hasil Generate")

    # Area Teks untuk Editor 1
    # 'key' diperlukan agar Streamlit bisa melacak perubahan
    st.session_state.editor1_content = st.text_area(
        "Hasil 1",
        value=st.session_state.editor1_content,
        height=400,
        key="editor1_textarea",
        label_visibility="collapsed"
    )

    # Tombol Aksi untuk Editor 1
    action_cols_1 = st.columns(2)
    
    # Tombol Bersihkan 1
    if action_cols_1[0].button("Clear Editor 1", use_container_width=True):
        st.session_state.editor1_content = ""
        st.rerun() # Muat ulang script untuk membersihkan teks

    # Tombol Pindahkan ke Editor 2
    if action_cols_1[1].button("Salin ke Editor 2 ➡️", use_container_width=True):
        st.session_state.editor2_content = st.session_state.editor1_content
        st.toast("Teks disalin ke Editor 2!")
        st.rerun()

    st.divider()

    # Fungsionalitas Simpan
    st.markdown("##### Simpan Hasil dari Editor 1")
    save_cols = st.columns([3, 1])
    save_name = save_cols[0].text_input("Simpan sebagai:", label_visibility="collapsed", placeholder="Beri nama file...")
    
    if save_cols[1].button("Simpan", use_container_width=True):
        if not save_name:
            st.warning("Silakan masukkan nama file untuk menyimpan.")
        elif not st.session_state.editor1_content:
            st.warning("Editor 1 kosong, tidak ada yang disimpan.")
        else:
            st.session_state.saved_items[save_name] = st.session_state.editor1_content
            st.success(f"Berhasil menyimpan '{save_name}'!")
            st.rerun()


# --- Kolom 3: Editor 2 (Catatan) & Hasil Tersimpan ---
with col_editor2:
    st.subheader("Editor 2: Catatan / Edit")

    # Area Teks untuk Editor 2
    st.session_state.editor2_content = st.text_area(
        "Hasil 2",
        value=st.session_state.editor2_content,
        height=400,
        key="editor2_textarea",
        label_visibility="collapsed"
    )
    
    # Tombol Bersihkan 2
    if st.button("Clear Editor 2", use_container_width=True):
        st.session_state.editor2_content = ""
        st.rerun()

    st.divider()

    # --- Bagian Hasil Tersimpan ---
    st.subheader("📁 Hasil Tersimpan")
    
    if not st.session_state.saved_items:
        st.info("Belum ada item yang disimpan. Gunakan 'Simpan' di Editor 1.")
    else:
        # Tampilkan setiap item yang tersimpan
        for item_name in list(st.session_state.saved_items.keys()):
            item_cols = st.columns([3, 1, 1])
            
            with item_cols[0]:
                st.markdown(f"**{item_name}**")
            
            with item_cols[1]:
                # Tombol Muat (Load)
                if st.button("Muat", key=f"load_{item_name}", use_container_width=True):
                    # Muat ke Editor 1
                    st.session_state.editor1_content = st.session_state.saved_items[item_name]
                    st.toast(f"'{item_name}' dimuat ke Editor 1.")
                    st.rerun()
            
            with item_cols[2]:
                # Tombol Hapus (Delete)
                if st.button("Hapus", key=f"delete_{item_name}", type="secondary", use_container_width=True):
                    del st.session_state.saved_items[item_name]
                    st.toast(f"'{item_name}' telah dihapus.")
                    st.rerun()
