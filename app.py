
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Guru Toolkits Multi-Editor</title>
    <!-- Font -->
    <link href="https://fonts.googleapis.com/css?family=Merriweather" rel="stylesheet">
    <!-- SimpleMDE CSS dan JS -->
    <link href="https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/simplemde/latest/simplemde.min.js"></script>
    <!-- Bootstrap CSS -->
    <link crossorigin="anonymous" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet"/>
    <!-- jQuery dan Markdown-it (digunakan SimpleMDE, tapi dipertahankan jika ada kebutuhan lain) -->
    <script src="https://cdn.staticfile.org/jquery/3.6.3/jquery.min.js"></script>
    <script src="https://cdn.staticfile.org/markdown-it/13.0.1/markdown-it.min.js"></script>

    <style>
        body {
            font-family: 'Merriweather', serif;
            font-size: 14px;
            background-color: #f8f9fa;
            color: #333;
        }
        h1, h2 {
            color: darkblue;
            font-size: 20px;
            font-weight: bold;
        }
        h3 {
            font-size: 16px;
            font-weight: bold;
            color: DodgerBlue;
        }
        .navbar {
            background-color: #ffffff;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            padding: 10px 20px;
        }
        .navbar-brand {
            font-size: 24px;
            font-weight: bold;
            color: #333;
        }
        .container-fluid {
            padding: 20px;
        }
        .form-control {
            border-radius: 5px;
            border: 1px solid #ddd;
        }
        .btn-warning {
            background-color: #ffc107;
            border-color: #ffc107;
            color: #000;
        }
        .btn-warning:hover {
            background-color: #e0a800;
            border-color: #d39e00;
        }
        .kompetensi-container {
            display: flex;
            flex-wrap: wrap;
            gap: 10px 15px;
            border: 1px solid #ddd;
            padding: 15px;
            border-radius: 5px;
            margin-top: 5px;
            background-color: #ffffff;
        }
        .kompetensi-item {
            display: flex;
            align-items: center;
        }

        /* --- STYLING BARU UNTUK HASIL DINAMIS --- */
        .result-card {
            background-color: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 20px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
        }
        .result-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
            padding-bottom: 10px;
            border-bottom: 1px solid #eee;
        }
        .result-actions button {
            margin-left: 8px;
            padding: 5px 12px;
            border-radius: 4px;
            font-size: 12px;
            transition: all 0.2s;
        }
        /* Menyesuaikan SimpleMDE agar terlihat baik */
        .CodeMirror {
            min-height: 200px; /* Tinggi minimum editor */
            height: auto; /* Biarkan tumbuh */
            border-radius: 0 0 5px 5px;
        }
        .editor-toolbar {
            border-radius: 5px 5px 0 0 !important;
            border-bottom: none !important;
            background-color: #f7f7f7;
        }
        .editor-statusbar {
            border-radius: 0 0 5px 5px !important;
        }
        
        /* --- STYLING UNTUK HASIL TERSIMPAN --- */
        .saved-items-container {
            margin-top: 20px;
        }
        .saved-items-list {
            max-height: 300px; /* Batasi tinggi, tambahkan scroll jika perlu */
            overflow-y: auto;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px;
            background-color: #ffffff;
        }
        .saved-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px;
            border-bottom: 1px solid #eee;
            font-size: 13px;
        }
        .saved-item:last-child {
            border-bottom: none;
        }
        .saved-item-title {
            cursor: pointer;
            font-weight: bold;
            color: #0056b3;
            flex-grow: 1;
            margin-right: 10px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .saved-item-title:hover {
            text-decoration: underline;
        }
        .saved-item-actions button {
            background: #dc3545;
            color: white;
            border: none;
            border-radius: 3px;
            padding: 2px 6px;
            font-size: 11px;
            cursor: pointer;
        }
        .saved-item-actions button:hover {
            background: #c82333;
        }
    </style>
</head>
<body>
    <!-- Navbar Minimalis -->
    <nav class="navbar navbar-expand-lg navbar-light bg-grey" style="background-color: #e3f2fd;">
        <a class="navbar-brand" href="#">
            <img src="https://blogger.googleusercontent.com/img/a/AVvXsEiauoRQ7i9fcn7yR25Se_NteOxPGJkajAdKl1nhb50wxUY8bzz93j4o-1wPpaBCLPiuM8T-lJtBi1S_3tUv5nKhsWmoMOWtR5r34de5osbK-d8m0S6YncVyNi2xRZyfenLKmTNdBVta5JjVKnYnSBPQCYnMZferjot6AJDjk3q4fMbFx3czh4Be-QWJigI0=s454" height="50" class="d-inline-block align-top" alt="Logo AI Guru">
            AI Guru Toolkits
        </a>
    </nav>

    <div class="container-fluid">
        <div class="row">
            <!-- Kolom Input (kiri) -->
            <div class="col-md-3">
                <h3>AI Toolkit Pembelajaran Mendalam</h3>
                <select class="form-control" id="komponen">
                <option style='background-color: #aaffa0; color: #000;' value='Buatkan informasi mengenai aktivitas pembelajaran, dimulai dari info umum (judul), Tujuan pembelajaran (dengan Taksonomi SOLO, dimulai dari uni-struktural), Fase pengalaman belajar (memahami, menerapkan, merefleksikan), Asesmen, Alternatif Media/Teknologi Pembelajaran, Penerapan Prinsip Pembelajaran (berkesadaran/mindful-reflective) selain/exclude meditasi-pernafasan, bermakna (meaningful) dan menggembirakan(joyful)), Dimensi profil lulusan yang dapat dikaitkan (Kedelapan dimensi tersebut adalah: keimanan dan ketakwaan kepada Tuhan YME, kewargaan, penalaran kritis, kreativitas, kolaborasi, kemandirian, kesehatan, dan komunikasi. ) disertai penjelasan singkat\n------------------\nContoh dan format:\nSistem Pencernaan (IPA SD)\n\nTUJUAN PEMBELAJARAN\nSiswa mampu mengidentifikasi organ dan enzim utama sistem pencernaan, menjelaskan hubungan proses pencernaan secara berurutan, serta menganalisis dampak pola makan terhadap kesehatan pencernaan dan merumuskan solusinya.\n\nRincian Tujuan (Taksonomi SOLO)\n\nUnistruktural: Mengidentifikasi satu organ utama sistem pencernaan dan fungsinya (mis. lambung mencerna protein).\nMultistruktural: Menyebutkan beberapa organ pencernaan dan enzim terkait beserta fungsinya.\nRelasional: Menjelaskan hubungan antara organ, enzim, dan proses pencernaan dalam urutan yang logis.\nExtended-Abstrak: Menganalisis dampak pola makan terhadap kesehatan pencernaan dan mengusulkan solusi untuk meningkatkan fungsi sistem pencernaan.\n\nPENGALAMAN BELAJAR\n1. MEMAHAMI\n\nFungsi: Mencerna makanan, menyerap nutrisi, buang sisa.\nOrgan:\nMulut: Mengunyah, amilase (karbohidrat).\nKerongkongan: Peristaltik.\nLambung: Pepsin (protein).\nUsus Halus: Serap nutrisi (lipase, tripsin).\nUsus Besar: Serap air, bentuk feses.\nAnus: Buang feses.\n\nProses: Mekanis (kunyah, aduk), kimiawi (enzim), penyerapan, eliminasi.\n\n2. MENERAPKAN\n\nBuat Diagram: Sketsa alur makanan dan fungsi organ.\nAnalisis Makanan: Pilih menu (mis. nasi, ayam), identifikasi nutrisi dan organ pencerna.\nKuis: Enzim lemak? (Lipase) Organ serap air? (Usus besar)\n\n3. MEREFLEKSIKAN\n\nPertanyaan: Mengapa pencernaan penting? Bagaimana diet memengaruhi usus?\nTindakan: Catat pola makan 1 hari, rencanakan perubahan (mis. tambah serat).\nKesehatan: Pelajari maag/sembelit, hubungkan dengan gaya hidup.\n\nALTERNATIF ASESMEN\nUnistruktural: Sebutkan satu organ pencernaan dan fungsinya (contoh: Lambung mencerna protein).\nMultistruktural: Tulis 3 organ pencernaan, enzim, dan nutrisi yang dicerna (mis. Mulut - Amilase - Karbohidrat).\nRelasional: Buat poster proses pencernaan nasi dari mulut hingga usus halus, sertakan organ dan enzim terkait.\nExtended-Abstrak: Buat rencana makan harian yang mendukung kesehatan pencernaan, jelaskan alasan pilihan makanan berdasarkan fungsi sistem pencernaan.\n\n\nALTERNATIF PEMANFAATAN MEDIA/PERAGA\nDigital:\n- Video animasi 2D/3D alur makanan.\n- Augmented Reality (AR) organ pencernaan.\n- Quiz interaktif (Kahoot, Quizizz).\n- Aplikasi simulasi enzim dan reaksi kimia.\nNon-digital / Hand-on:\n- Pipa paralon + balon (model peristaltik).\n- Model clay/foam organ pencernaan.\n- Percobaan amilase pada roti (mengunyah sampai manis).\n- Poster kertas manila dan spidol.\n- Puzzle susun alur pencernaan.\nPENERAPAN PRINSIP PEMBELAJARAN\nDIMENSI PROFIL LULUSAN \n------------------------------\nTopik materi pelajaran:'>Ringkasan Pembelajaran Mendalam</option>
  <option style='background-color: #aaffa0; color: #000;' value=' Saya meminta bantuan Anda untuk merancang sebuah rencana pembelajaran inovatif dan mendalam untuk topik materi pelajaran. Tuliskan pada bagian awal berupa tabel tujuan pembelajaran dengan menggunakan taksonomi SOLO dimulai dari uni-struktural(kolom 1: Level taksonomi SOLO, kolom 2 tujuan pembelajaran: kolom 3: Fase pembelajaran . Rencana pembelajaran secara umum harus terstruktur secara sistematis melalui tiga fase PENGALAMAN BELAJAR utama, yaitu MEMAHAMI, MENERAPKAN, dan MEREFLEKSIKAN. Untuk setiap fase tersebut, mohon rumuskan Tujuan Pembelajaran yang jelas, terukur, dan dikaitkan dengan level yang relevan dalam SOLO Taxonomy (misalnya, pra-struktural, uni-struktural, multi-struktural, relasional, atau abstrak diperluas) yang mencerminkan kedalaman pemahaman yang diharapkan. Tuliskan juga tujuan pembelajaran ini di awal, sebelum masuk tahapan belahar. Sangat penting bahwa setiap fase dan aktivitas di dalamnya secara eksplisit mengintegrasikan dan menerapkan tiga pendekatan pembelajaran mendalam: Mindful-Reflective Learning, di mana peserta didik memahami tujuan pembelajaran, termotivasi secara intrinsik, serta aktif meregulasi diri dalam merencanakan, melaksanakan, dan mengevaluasi cara belajar mereka secara reflektif; Meaningful Learning, di mana peserta didik menerapkan pengetahuan dalam situasi nyata, proses belajar berorientasi pada transfer belajar dan pemahaman mendalam (bukan hafalan), serta mengaktifkan pengetahuan awal; dan Joyful Learning, yang menciptakan suasana belajar positif, menantang, menyenangkan, memotivasi, dan melibatkan peserta didik secara kognitif serta emosional. Mohon sajikan ide aktivitas untuk setiap fase dalam format tabel yang terstruktur, mencakup kolom-kolom berikut: Fase Pengalaman Belajar (MEMAHAMI/MENERAPKAN/MEREFLEKSIKAN), Tujuan Pembelajaran (beserta level SOLO yang disebutkan), Penjelasan Singkat Fase (menguraikan kontribusi fase terhadap pemahaman topik dan bagaimana prinsip mindful, meaningful, joyful diterapkan secara umum di fase tersebut), Aktivitas Pembelajaran Spesifik (menjelaskan langkah-langkah kegiatan dengan menggunakan strategi dan alat/media pembelajaran yang bervariasi, dari yang sederhana hingga teknologi canggih, yang sesuai dengan topik materi), Asesmen (menjelaskan bagaimana kemajuan atau pencapaian tujuan pembelajaran diukur pada fase tersebut, baik formatif maupun sumatif), dan daftar Alat/Media Pembelajaran yang digunakan dalam aktivitas. Setelah penyajian tabel, saya meminta Anda untuk memberikan penjelasan akhir yang komprehensif mengenai bagaimana ketiga prinsip pembelajaran mendalam tersebut (mindful-reflective learning, meaningful learning, dan joyful learning) secara spesifik diterapkan dan terintegrasi dalam keseluruhan rancangan pembelajaran untuk topik materi yang telah dipilih, serta menjelaskan bagaimana setiap prinsip mendukung pencapaian tujuan pembelajaran pada masing-masing fase. Pada fase MEMAHAMI mencakup pengetahuan esensial, pengetahuan aplikatif dan pengetahuan nilai/karakter. Pada fase MENERAPKAN mencakup pada pemahaman yang lebih mendalam dan aplikasinya. Pada fase MEREFLEKSIKAN mencakup refleksi pembelajaran dan regulasi diri dan contoh praktis penerapan materi yang dipelajari dalam kehidupan sehari-hari baik untuk kehidupan pribadi maupun sosial-masyarakat  (contoh setelah belajar Sistem Pencernaan, siswa dapat mengatur menu makanan sehat sehari-hari dll). Pastikan output yang Anda berikan menggunakan bahasa yang profesional, jelas, dan mudah dipahami, Tuliskan alternatif Asesmen terkait tujuan pembelajaran, Alternatif Media/Teknologi Pembelajaran (digital dan non-digital), Penerapan Prinsip Pembelajaran (berkesadaran/mindful-reflective) selain/exclude meditasi-pernafasan, bermakna (meaningful) dan menggembirakan(joyful)), Dimensi profil lulusan yang dapat dikaitkan (Kedelapan dimensi tersebut adalah: keimanan dan ketakwaan kepada Tuhan YME, kewargaan, penalaran kritis, kreativitas, kolaborasi, kemandirian, kesehatan, dan komunikasi. ) disertai penjelasan singkat  Dibagian akhir tambahkan informasi kaitannya tentang oleh pikir, olah rasa dan olah raga dengan mengaitkan relevansi ke topik materi. Materi pelajaran adalah pada topik/tema berikut :  '>Ide Pembelajaran Mendalam (1)</option>
                                  
 <option style='background-color: #aaffa0; color: #000;' value=' Saya meminta bantuan Anda untuk merancang 3 fase pembelajaran yaitu (1) Fase Memahami. (2)Fase Menerapkan dan (3) Fase Merefleksikan. Peran: Anda adalah seorang desainer instruksional dan fasilitator ahli. Tugas: Buatkan sebuah aktivitas pembelajaran mengenai topik yang akan saya berikan. mulailah dengan analisis tugas mencakup aspek utama: pertama, mendefinisikan konten dan tugas dengan mengidentifikasi kebutuhan kinerja, menentukan tugas yang harus dicapai, mengenali keterampilan serta pengetahuan yang diperlukan, dan memilih tugas untuk pengembangan instruksi; setelah itu jelaskan poin *(1) FASE MEMAHAMI* dan *(2) FASE MENERAPKAN*, ,masing2 fase berisi poin-poin mengidentifikasi langkah-langkah rumit dan menentukan urutan pelaksanaan serta pembelajaran tugas; kaitkan dengan tujuan pembelajaran, penguraian komponen operasional, identifikasi jenis pengetahuan (deklaratif, struktural, prosedural), pemilihan tugas prioritas, serta perancangan aktivitas, strategi, dan media pembelajaran yang sesuai; Target peserta adalah siswa/murid. lanjutkan *(3) FASE MEREFLEKSIKAN* yaitu buatkan aktivitas refleksi pembelajaran mengenai topik yang diberikan. Fokus Dimensi Refleksi: Aktivitas harus mencakup Dimensi Kognitif (Analisis Kritis Pengalaman Belajar Rekonstruksi Pengetahuan- Identifikasi Pola Pikir dan Asumsi), Dimensi Metakognitif (Kesadaran Proses Berpikir Sendiri - Evaluasi Strategi Pembelajaran-Pengaturan dan Monitoring Pemahaman), Dimensi Afektif (Eksplorasi Emosi Selama Proses Belajar- Refleksi Sikap dan Motivasi- Pengembangan Kesadaran Diri), Dimensi Praktis (Transformasi Pengalaman menjadi Praktik- Perencanaan Tindakan Perbaikan- Aplikasi Pembelajaran ke Konteks Nyata dan karier masa depan) dan Dimensi Sosial (Interpretasi Pengalaman dalam Konteks Sosial- Kolaborasi dan Berbagi Pemahaman). aktivitas dapat berupa daftar pertanyaan reflektif yang bisa langsung dijawab peserta atau dalam bentuk instruksi/penugasan. setelah itu susun penilaian/asesmen untuk mengukur kemampuan individu dalam pemahaman dan  kinerja menyelesaikan tugas. Format output: tuliskan analisis konten-tugas, judul tiap fase serta Penilaian/Asesmen dengan format Heading-2. Materi pelajaran adalah pada topik/tema berikut :  '>Ide 3 Fase Pengalaman Belajar</option>
              
                
                
                
<option value='Tujuan Pembelajaran dan indikator ketuntasan. Buat dalam tabel dengan setiap tujuan pembelajaran terdiri dari 1 atau lebih indikator.'>Tujuan Pembelajaran</option>
<option value='Tujuan Pembelajaran yang dituliskan dalam tabel dengan menggabungkan 2 dimensi (tuliskan tujuan pembelajaran dalam tabel dengan kombinasi dimensi pengetahuan (4 baris tabel: faktual-konseptual-prosedural-metakognitif) dan dimensi kognitif (6 kolom tabel: mengingat, memahami, mengaplikasi, menganalisis, mengevaluasi, kreasi)). (Di bagian bawah,tuliskan contoh soal untuk masing-masing tahap). Topik :'>Tujuan Pembelajaran (Dimensi Bloom) </option>
<option value='Tujuan Pembelajaran yang dituliskan dalam tabel dengan  SOLO taxonomy (4 baris, uni-struktural, multi struktural,relasional, extended-abstract) kolom kedua tuliskan indikator).Setelah itu buatkan Di bagian bawah tuliskan indikator, konsep kisi-kisi asesmen dan contoh soal untuk masing-masing tahap). Topik materi: '>Tujuan Pembelajaran (Taksonomi SOLO 1)</option>
<option value='Tujuan Pembelajaran yang dituliskan dalam tabel dengan menggabungkan 2 dimensi (tuliskan tujuan pembelajaran dalam tabel dengan kombinasi dimensi pengetahuan (4 baris tabel: faktual-konseptual-prosedural-metakognitif) dan dimensi SOLO taxonomy (4 kolom, uni-struktural, multi struktural,relasional, extended-abstract)).Setelah itu buatkan konsep kisi-kisi asesmen berdasar SOLO taxonomy tersebut. (Di bagian bawah,tuliskan contoh indikator pencapaian kompetensi dan contoh soal untuk masing-masing tahap). Topik materi: '>Tujuan Pembelajaran (Taksonomi SOLO 2)</option>
<!-- <option value='Tujuan Pembelajaran yang dituliskan dalam tabel dengan menggabungkan 2 dimensi (tuliskan tujuan pembelajaran dalam tabel dengan kombinasi dimensi Berkesadaran/Mindful, Bermakna/Meaningful, Menggembirakan/Joyful (3 kolom tabel) dan dimensi  Memahami, Mengaplikasi/menerapkan, Merefleksi (dalam 3 baris tabel) dan .Setelah itu buatkan konsep kisi-kisi asesmen berdasar tabel tersebut. Topik materi: '>Tujuan Pembelajaran (Deep Learning)</option> -->

<option value='Daftar Jabaran/uraian sub-materi penting Pembelajaran '>Uraian Materi</option>
<option value='Daftar materi/pengetahuan/skill prasyarat yang perlu dikuasai siswa sebelum pembelajaran '>Materi Prasyarat</option>
<option value='Masalah pembelajaran kesalahan pemahaman dan titik kritis yang sering dihadapi siswa '>Masalah Belajar Siswa</option>
<option value='Daftar Pertanyaan pemantik (guiding questions) (judul gunakan heading H2 dan tanpa subheading lain) yang memandu mengantarkan ke materi pembelajaran '>Pertanyaan Pemantik</option>
<option value=' Daftar poin motivasi Mengapa  penting dan perlu bagi siswa untuk mempelajari materi ini (jika perlu, berikan contoh serta manfaat di kehidupan nyata serta karir masa depan) '>Bahan Motivasi Belajar Siswa</option>
<!-- <option value="Pertanyaan esensial terkait materi pelajaran yang ada kaitannya dengan penerapan dunia nyata">Pertanyaan Esensial</option> -->



<option  style="background-color: #FFFf00; color: #000;">&#9472;&#9472;&#9472;&#9472;Ide Aktivitas Pembelajaran&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;</option>



<option value='Aktivitas Pemantik Belajar (lesson hook)'>Ide Aktivitas Pemantik Awal Belajar</option>


<option style='background-color: #aaffa0; color: #000;' value=' Saya meminta bantuan Anda untuk merancang sebuah rencana pembelajaran inovatif dan mendalam untuk topik materi pelajaran. Tuliskan pada bagian awal berupa tabel tujuan pembelajaran dengan menggunakan taksonomi SOLO (kolom 1: Level taksonomi SOLO, kolom 2 tujuan pembelajaran: kolom 3: Fase pembelajaran . Rencana pembelajaran secara umum harus terstruktur secara sistematis melalui tiga fase utama, yaitu MEMAHAMI, MENERAPKAN, dan MEREFLEKSIKAN. Untuk setiap fase tersebut, mohon rumuskan Tujuan Pembelajaran yang jelas, terukur, dan dikaitkan dengan level yang relevan dalam SOLO Taxonomy (misalnya, pra-struktural, uni-struktural, multi-struktural, relasional, atau abstrak diperluas) yang mencerminkan kedalaman pemahaman yang diharapkan. Tuliskan juga tujuan pembelajaran ini di awal, sebelum masuk tahapan belahar. Sangat penting bahwa setiap fase dan aktivitas di dalamnya secara eksplisit mengintegrasikan dan menerapkan tiga pendekatan pembelajaran mendalam: Mindful-Reflective Learning, di mana peserta didik memahami tujuan pembelajaran, termotivasi secara intrinsik, serta aktif meregulasi diri dalam merencanakan, melaksanakan, dan mengevaluasi cara belajar mereka secara reflektif; Meaningful Learning, di mana peserta didik menerapkan pengetahuan dalam situasi nyata, proses belajar berorientasi pada transfer belajar dan pemahaman mendalam (bukan hafalan), serta mengaktifkan pengetahuan awal; dan Joyful Learning, yang menciptakan suasana belajar positif, menantang, menyenangkan, memotivasi, dan melibatkan peserta didik secara kognitif serta emosional. Mohon sajikan ide aktivitas untuk setiap fase dalam format tabel yang terstruktur, mencakup kolom-kolom berikut: Fase Pembelajaran (MEMAHAMI/MENERAPKAN/MEREFLEKSIKAN), Tujuan Pembelajaran (beserta level SOLO yang disebutkan), Penjelasan Singkat Fase (menguraikan kontribusi fase terhadap pemahaman topik dan bagaimana prinsip mindful(sadar dengan tujuan dan aktivitas), bermakna/meaningful, menggembirakan/joyful diterapkan secara umum di fase tersebut), Aktivitas Pembelajaran Spesifik (menjelaskan langkah-langkah kegiatan dengan menggunakan strategi dan alat/media pembelajaran yang bervariasi, dari yang sederhana hingga teknologi canggih, yang sesuai dengan topik materi), Asesmen (menjelaskan bagaimana kemajuan atau pencapaian tujuan pembelajaran diukur pada fase tersebut, baik formatif maupun sumatif), dan daftar Alat/Media Pembelajaran yang digunakan dalam aktivitas. Setelah penyajian tabel, saya meminta Anda untuk memberikan penjelasan akhir yang komprehensif mengenai bagaimana ketiga prinsip pembelajaran mendalam tersebut (mindful-reflective learning, meaningful learning, dan joyful learning) secara spesifik diterapkan dan terintegrasi dalam keseluruhan rancangan pembelajaran untuk topik materi yang telah dipilih, serta menjelaskan bagaimana setiap prinsip mendukung pencapaian tujuan pembelajaran pada masing-masing fase. Pastikan output yang Anda berikan menggunakan bahasa yang profesional, jelas, dan mudah dipahami, dengan fokus pada kedalaman materi, keterkaitan yang kuat antar elemen (fase, tujuan, prinsip, aktivitas, asesmen), serta menunjukkan variasi dalam strategi dan alat/media pembelajaran yang diusulkan.  Dibagian akhir tambahkan informasi kaitannya tentang oleh pikir, olah rasa dan olah raga dengan mengaitkan relevansi ke topik materi. Materi pelajaran adalah pada topik/tema berikut :  '>Ide Pembelajaran Mendalam (1)</option>
<option style='background-color: #aaffa0; color: #000;' value=' Saya membutuhkan saran profesional dari Anda untuk merancang sebuah ide pembelajaran yang inovatif dan mendalam, yang difokuskan pada topik materi pelajaran. Mohon awali dengan menyusun sebuah paragraf yang menjelaskan Tujuan Pembelajaran secara komprehensif untuk topik tersebut, dan secara eksplisit mengaitkan berbagai tingkatan pencapaian tujuan ini dengan level-level yang relevan dalam SOLO Taxonomy (Structure of Observed Learning Outcome oleh Biggs and Collis, 1982), lengkap dengan rincian bagaimana setiap tahapan SOLO (mulai dari pra-struktural hingga abstrak diperluas) dapat tercermin dalam pemahaman peserta didik terhadap topik ini. Setelah itu, saya meminta Anda untuk mengembangkan ide aktivitas pembelajaran yang terstruktur dalam tiga fase utama: MEMAHAMI, MENERAPKAN, dan MEREFLEKSIKAN. Penting bagi setiap fase untuk secara holistik mengintegrasikan tiga pengalaman belajar kunci. Pertama, pada fase MEMAHAMI, fokuskan pada pencapaian pemahaman mendalam: rancanglah aktivitas yang dimulai dengan minimal tiga pertanyaan pemantik yang efektif untuk topik tersebut, yang bertujuan agar peserta didik memahami tujuan pembelajaran, termotivasi secara intrinsik, serta mampu mengaktifkan pengetahuan awal dan prasyarat mereka; sertakan juga bagaimana guru dapat menyampaikan setidaknya tiga poin motivasi tentang pentingnya mempelajari topik materi ini. Kedua, pada fase MENERAPKAN, tekankan pada penerapan atau aplikasi nyata (hands-on): rancanglah aktivitas di mana peserta didik secara aktif menerapkan pengetahuan mengenai materi pelajaran dalam berbagai situasi nyata, berikan minimal tiga contoh detail tentang bagaimana hal ini dapat dilakukan sesuai dengan materi, dan usulkan contoh konkret proyek atau pembelajaran berbasis masalah (Project/Problem-Based Learning) yang relevan dan menantang. Ketiga, pada fase MEREFLEKSIKAN, fasilitasi pembelajaran reflektif: rancanglah aktivitas yang memungkinkan peserta didik untuk membahas minimal tiga hikmah atau pelajaran penting yang telah mereka peroleh, berikan contoh bagaimana pembelajaran ini dapat ditransfer ke konteks yang berbeda atau dikaitkan dengan minimal tiga topik atau pelajaran lain, serta jelaskan bagaimana aktivitas tersebut mendukung pengembangan metakognisi peserta didik, di mana mereka aktif meregulasi diri dalam merencanakan, melaksanakan, dan mengevaluasi cara belajar mereka secara reflektif. Sebagai penutup, mohon jelaskan secara rinci dan dengan contoh praktis bagaimana ketiga prinsip pembelajaran fundamental—yaitu (a) mindful learning (kesadaran penuh dalam proses belajar), (b) meaningful learning (pembelajaran yang bermakna, menekankan pemahaman mendalam bukan sekadar menghafal informasi, serta melibatkan aktivasi pengetahuan awal dan pengembangan minat-bakat), dan (c) joyful learning (menciptakan suasana belajar yang positif, menggembirakan, menantang, menyenangkan, memotivasi, serta melibatkan peserta didik secara kognitif dan emosional)—secara konkret diterapkan dan terjalin dalam setiap fase pembelajaran (MEMAHAMI, MENERAPKAN, MEREFLEKSIKAN) dan setiap aktivitas yang telah Anda rancang sebelumnya. Pastikan seluruh penjelasan dan contoh selalu dikaitkan secara langsung dan relevan dengan topik materi yang telah ditentukan.  Dibagian akhir tambahkan informasi kaitannya tentang oleh pikir, olah rasa dan olah raga dengan mengaitkan relevansi ke topik materi. Materi pelajaran adalah pada topik/tema berikut : '>Ide Pembelajaran Mendalam (2)</option>
<option style='background-color: #aaffa0; color: #000;' value=' saran profesional tentang ide pembelajaran dengan menuliskan paragraf terkait tujuan pembelajaran dikaitkan dengan SOLO taxonomy (the SOLO (structure of observed learning outcome) taxonomy developed by Biggs and Collis (1982) ) tuliskan rincian sesuai tahapannya. Setelah itu Kemudian  tulis ide aktivitas dgn menerapkan pendekatan pembelajaran mendalam yang  berdasar 3 PRINSIP PEMBELAJARAN dikombinasikan 3 PENGALAMAN BELAJAR. PRINSIP Pembelajaran yaitu (PRINSIP 1) pembelajaran berkesadaran (mindful-reflektif learning) (Peserta didik memahami tujuan pembelajaran dan termotivasi secara intrinsik untuk belajar. Peserta didik aktif meregulasi diri dalam belajar, merencanakan, melaksanakan, dan mengevaluasi reflektif cara belajar mereka.) , (PRINSIP 2) pembelajaran bermakna (meaningful learning) (Peserta didik menerapkan pengetahuan dalam situasi nyata,Proses belajar berorientasi pada kemampuan mengaplikasikan pengetahuan (learning tansfer), pemahaman mendalam bukan hanya menghafal informasi, melibatkan aktivasi pengetahuan awal), dan (PRINSIP 3) pembelajaran yang menggembirakan (joyful learning) (suasana belajar yang positif, menantang, menyenangkan, dan memotivasi, terlibat secara kognitif dan emosional). Prinsip tersebut dikombinasikan dengan 3 PENGALAMAN BELAJAR yaitu (PENGALAMAN 1) pemahaman mendalam, siswa termotivasi,terinspirasi,tidak hanya menghafal materi, (PENGALAMAN 2) aplikasi/penerapan dalam kehidupan nyata an bermanfaat secara nyata dan (PENGALAMAN 3) Refleksi, mampu melakukan refleksi hasil belajar, koneksi atau mengaitkan dengan konteks dan topik keilmuan lain dan kaitan dengan pembelajaran kelanjutan berikutnya. Jelaskan masing-masing poin tsb dalam tabel 3 baris pengalaman belajar dan 3 kolom prinsip pembelajaran. Jelaskan menuliskan rancangan aktivitas pembelajaran dengan menerapkan fase MEMAHAMI, MENERAPKAN, MEREFLEKSIKAN. dengan selalu dikaitkan dengan topik materi. Dibagian akhir tambahkan informasi kaitannya tentang oleh pikir, olah rasa dan olah raga dengan mengaitkan relevansi ke topik materi. Materi pelajaran adalah pada topik/tema berikut : '>Ide Pembelajaran Mendalam (3)</option>


<option value='alternatif langkah (step-by-step) Aktivitas Belajar dari awal ketika siswa belum paham materi hingga akhirnya siswa paham konsep dan penerapannya. berikan cara dan trik yang memudahkan siswa belajar. fokuskan pada langkah didaktik-pedagogi dan spesifik pada materi '>Ide Aktivitas Inti</option>
<option value='alternatif langkah (step-by-step) strategi Belajar dari awal ketika siswa belum paham materi hingga akhirnya siswa paham konsep dan penerapannya. berikan cara dan trik yang memudahkan siswa belajar (gunakan peraga jika perlu). fokuskan pada langkah didaktik-pedagogi dan spesifik pada materi yang disertai contoh-contoh yang memudahkan pemahaman dan gunakan prinsip yang sesuai dengan cara otak/kognisi bekerja. Jelaskan rasional/argumen mengapa guru perlu melakukan langkah tersebut misalnya untuk mengatasi miskonsepsi, kesulitan pemahaman materi, dan hambatan belajar terkait topik materi. '>Ide Aktivitas Untuk Materi Sulit</option>



<option value='Ide pembelajaran berdiferensiasi (differentiated instruction) untuk kelompok siswa yang memiliki kemampuan dan karakteristik yang berbeda beserta tugas yang sesuai. Tulis dalam tabel.'>Ide Pembelajaran Berdiferensiasi (Kemampuan Siswa)</option>
<option value='Ide pembelajaran berdiferensiasi (differentiated instruction) untuk kelompok siswa dalam kategori diferensiasi konten, proses dan produk. Tulis dalam tabel.'>Ide Pembelajaran Berdiferensiasi (Proses-Konten-Produk)</option>

<option value='Buatlah rencana aktivitas pembelajaran yang menerapkan pendekatan gamifikasi untuk suatu materi. Rincikan tujuan pembelajaran, deskripsi aktivitas, mekanisme permainan, aturan main, cara pemberian hadiah atau poin, serta metode evaluasi hasil belajar siswa. Sertakan contoh konkret seperti jenis tantangan, level atau tingkatan, fitur interaktif, dan bagaimana gamifikasi ini dapat meningkatkan motivasi dan pemahaman siswa terhadap materi tersebut. Topik materi: '>Ide Pembelajaran dg Gamifikasi</option>
<option value='Ide pembelajaran berbasis problem-solving melibatkan investigasi dan penerapan konsep. Berikan statemen problem/masalah yang menantang dan menarik dengan bahasa yang mudah dipahami.'>Ide Pembelajaran Berbasis Pemecahan-Masalah (PBL)</option>
<option value='Ide pembelajaran berbasis inquiry-based learning. Berikan langkah-langkah dengan detail.'>Ide Pembelajaran Berbasis Inkuiri</option>
<option value='Ide pembelajaran berbasis project based learning dengan penerapan konsep dari mata pelajaran dan gunakan sintaks PjBL. tuliskan tujuan pembelajaran dan detail project yang harus dikerjakan. Tuliskan relevansi projek tsb dengan 4 kriteria kunci PjBL (dalam bentuk tabel 2 kolom 4 baris) berisi statemen pertanyaan penuntun (guiding question) yang jelas, konten materi pelajaran yang relevan, produk autentik yang dihasilkan dan kerja kolaboratif siswa. berikan arahan langkah yang harus dilakukan siswa. di akhir, berikan  alternatif langkah project yang mungkin dilakukan siswa sesuai sintaks PjBL (tuliskan dalam tabel). Tuliskan alternatif solusi jenis projek yang dapat dilakukan siswa, jika siswa tidak dapat menemukan idenya sendiri. '>Ide Pembelajaran Berbasis Proyek (PjBL)</option>
<option value='Ide pembelajaran yang dirancang dengan berbasis UBD (understanding by design). Berikan langkah-langkah tahapan dengan detail. Buatkan aktivitas pembelajaran melalui urutan fase pengenalan konsep, pengembangan/elaborasi konsep, penguatan (reinforcement) dan penerapan (application), dan penilaian (berikan penjelasan dsingkat di masing-masing fase.'>Ide Pembelajaran Berbasis UBD-1</option>
<option value='Ide pembelajaran ang dirancang dengan berbasis UBD (understanding by design). komponennya adalah 1. Desired Results(Hasil yang diharapkan)\nEstablised goals(Tujuan)\nEnduring Understanding(Pemahaman bermakna)\nEssential questions(Pertanyaan Kunci)\nStudents will know(Siswa mengetahui/Akuisi konten)\nStudents will able to(Siswa mampu/terampil)\n\n2. Assesment evidence(Bukti)\nPerformance tasks(Tugas Performa)\nOther evidence(Bukti lain)\n\n3. Learning plan\nLearning activities\nAktivitas pembelajaran adalah kegiatan yang dirancang untuk membantu siswa mencapai tujuan pembelajaran. Berikut adalah beberapa contoh learning activities:\n• Membaca teks yang relevan dengan topik pembelajaran\n• Mengerjakan soal-soal latihan untuk memperkuat pemahaman konsep\n• Membuat proyek atau presentasi untuk menunjukkan pemahaman\n• Berdiskusi dengan teman-teman untuk memperluas wawasan\n• Mengerjakan eksperimen atau simulasi untuk memahami konsep secara lebih dalam\n\nFramework WHERETO\nW: What (Apa yang ingin dicapai?)\nH: How (Bagaimana cara mencapainya?)\nE: Evidence (Apa bukti yang diperlukan untuk menunjukkan pencapaian. Pemanfaatan alat peraga/TIK)\nR: Reasoning (Bagaimana cara berpikir untuk mencapai tujuan?)\nE: Evaluation (Bagaimana cara mengevaluasi hasil?)\nT: Transfer (Bagaimana cara menerapkan pengetahuan ke situasi lain?)\nO: Opportunity (Apa kesempatan yang diperlukan untuk mencapai tujuan?)(berikan penjelasan dsingkat di masing-masing fase.Tuliskan istilah bahasa inggris dengan diterjemahkan ke bahasa indonesia.'>Ide Pembelajaran Berbasis UBD-2</option>
<option value='alternatif langkah (step-by-step) pembelajaran yang melibatkan peningkatan kompetensu literasi siswa melalui topik materi  pembelajaran. fokuskan pada langkah yang sesuai pada materi yang disertai contoh-contoh yang dapat mencapai tujuan pembelajaran sekaligus meningkatkan kemampuan literasinya. di akhir, jelaskan literasi yang dilatihkan dalam materi pelajaran yang bersangkutan. Berikan alternatif untuk asesmen literasinya tsb. Topik materi pelajaran :'>Ide Aktivitas Pembelajaran Literasi (1)</option>
<option value='ide pembelajaran yang melibatkan peningkatan kompetensi literasi siswa melalui topik materi pembelajaran. fokuskan pada literasi terkait fakta/konsep/prosedur/metakognitif yang sesuai pada materi yang dipelajari disertai contoh-contoh dan aktivitas yang dapat mencapai tujuan pembelajaran sekaligus meningkatkan kemampuan literasinya. di akhir, jelaskan literasi yang dilatihkan dalam materi pelajaran yang bersangkutan. Berikan alternatif untuk asesmen literasinya tsb. Topik materi pelajaran :'>Ide Aktivitas Pembelajaran Literasi (2)</option>
<option value='ide pembelajaran yang melibatkan peningkatan kompetensi numerasi siswa melalui topik materi pembelajaran. fokuskan pada numerasi terkait fakta/konsep/prosedur yang sesuai pada materi yang dipelajari disertai contoh-contoh yang dapat mencapai tujuan pembelajaran sekaligus meningkatkan kemampuan numerasi. di akhir, jelaskan kemampuan numerasi yang dilatihkan dalam materi pelajaran yang bersangkutan. Berikan alternatif untuk asesmen numerasi tsb. Topik materi pelajaran :'>Ide Aktivitas Pembelajaran Numerasi 1</option>
<option value='ide pembelajaran yang melibatkan peningkatan kompetensi literasi sains siswa melalui topik materi pembelajaran. fokuskan pada literasi sains terkait aspek saintifik yaitu nominal, fungsional, konseptual dan prosedural, dan multidimensi pada materi yang dipelajari disertai contoh-contoh yang dapat mencapai tujuan pembelajaran sekaligus meningkatkan kemampuan literasi sains. di akhir, jelaskan kemampuan saintifik yang dilatihkan dalam materi pelajaran yang bersangkutan. Berikan alternatif untuk asesmen numerasi tsb. Topik materi pelajaran :'>Ide Aktivitas Pembelajaran Literasi Sains</option>
<option value='Berikan beberapa ide praktis projek STEM yang melibatkan siswa untuk berdiskusi dan eksplorasi ide menantang. Jelaskan komponen topik mapel STEM dan Art serta skill-softskill yang terkait projek tsb. kemudian tuliskan challenge-statement dan jelaskan deskripsi dan langkah/proses dari proyek tsb. Topik utama mencakup '>Ide Pembelajaran STEM</option>
<option value='Ide pembelajaran berbasis penerapan konsep Computational Thinking dalam penyelesaian masalah. Melibatkan proses dekomposisi, pengenalan pola, abstraksi, representasi data, algoritma. (tuliskan dalam tabel). Buatkan tugas siswa yang menantang dan relevan dengan langkah tersebut '>Ide Pembelajaran dengan Computational-Thinking</option>
<option value='Your task is to create a comprehensive, engaging, and well-structured lesson plan on the given subject. The lesson plan should be designed for a 60-minute class session and should cater to a specific grade level or age group. Begin by stating the lesson objectives, which should be clear, measurable, and aligned with relevant educational standards. Then what the indicators of the objectives. Next, provide a detailed outline of the lesson, breaking it down into an introduction, main activities, and a conclusion. For each section, describe the teaching methods, learning activities, and resources you will use to effectively convey the content and engage the students. Finally, describe the assessment methods you will employ to evaluate students’ understanding and mastery of the lesson objectives. The lesson plan should be well-organized, easy to follow, and promote active learning and critical thinking.(gunakan respon bahasa indonesia)'>Ide Aktivitas Pembelajaran Kreatif</option>
<option value='Buatkan sebuah lesson plan untuk aktivitas pembelajaran Isi lesson plan meliputi  bbrp {komponen} berikut: Learning Objectives/tujuan pembelajaran, daftar indikator ketercapaian/ketuntasan dari tujuan pembelajaran, motivasi utk belajar materi, Outline Materi, Media/Alat/Bahan, Daftar materi prasyarat (materi prior knowledge yang harus dikuasai), Procedure (termasuk durasi waktu dan buatkan contoh soal/latihan serta strategi yang efektif. berikan penekanan pada konsep yang penting), Assessment (10 soal essay), Extension Activities (tuliskan sub judul komponen ini dengan kode markdown tebal/bold) warna biru. Berikan contoh, strategi dan penjelasan yang memudahkan pemahaman."+"Gunakan bahasa Indonesia. Format output: \n**Judul\n \n\n**Tujuan Pembelajaran\n \n\n**Indikator\n \n\n**Motivasi\n  \n\n**Daftar Materi\n \n**Materi Prasyarat\n \n\n**Media/Alat/Bahan\n \n\n**Aktivitas\ \n\n**Asesmen\n \n\n**Aktivitas lanjutan. berikan 5 soal essay di asesmen. tambahkan \n\n---\n\n di setiap {komponen}. gunakan format markdown bullet list untuk setiap isi {komponen}.Use bahasa indonesia. topiknya adalah: '>RPP-Modul Ajar-Lesson Plan</option>


<option  style="background-color: #FFFf00; color: #000;">&#9472;&#9472;&#9472;&#9472;Materi Ajar&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;</option>
<option value=' Tulisan bahan bacaan dalam bentuk tulisan komprehensif mencakup materi fundamental/penting (berisi 800+ kata)'>Bahan Bacaan</option>
<option value=' Tampilkan gambar yang diembedded dengan dengan format !![](https://image.pollinations.ai/prompt/{keyword}) . Jangan tambahkan spasi pada format tsb . Keyword ditulis dalam bahasa inggris, ganti spasi dengan hypen. Instruksi utama: Tulis sebuah cerita (500 kata lebih) untuk belajar literasi dengan judul menarik sesuai keyword. tuliskan 1 chapter dengan gaya penulisan seperti buku “Bedtime Math: The Truth Comes Out” (book that helps kids learn math/science through engaging stories and real-life scenarios) dengan tambahan 5 pertanyaan/soal untuk latihan kemampuan literasi di akhir. Jangan menambahkan informasi lain. Buatkan keyword gambar dengan gaya visual menarik dengan berdasar deskripsi atau topik berikut:'>Cerita Bacaan Literasi</option>
<option value=' Tuliskan sebuah cerita untuk meningkatkan skill numerasi siswa (500 kata lebih) dengan judul menarik sesuai keyword. tuliskan 1 chapter terkait keterampilan numerasi (math problem solving) dengan gaya penulisan seperti buku “Bedtime Math: The Truth Comes Out” (book that helps kids learn math/science through engaging stories and real-life scenarios) dengan tambahan 5 pertanyaan/soal untuk latihan numerasi matematika di akhir. Jangan menambahkan informasi lain. Buatkan keyword gambar dengan gaya visual menarik dengan berdasar deskripsi atau topik berikut:'>Cerita Bacaan Numerasi</option>
<option value=' Tulisan daftar pengetahuan kunci penting (key takeaways) fundamental/penting yang dapat dimanfaatkan atau menjadi dasar untuk pengetahuan lanjutan atau dalam pemanfaatan di dunia nyata. Topik materi:'>Pengetahuan Kunci</option>
<option value=' contoh-contoh dan analogi untuk membantu siswa memahami materi '>Contoh dan Analogi</option>
<option value=' Beberapa alternatif  Media pembelajaran, deskripsi media dan langkah pembelajaran menggunakan media tsb.'>Media Pembelajaran</option>
<option value=' outline berisi poin-poin penting untuk presentasi disertai rincian penjelasan secukupnya'>Outline Materi Presentasi</option>
<option value=' lembar kerja (LKPD) siswa (student worksheet). berisi petunjuk, pengamatan, langkah aktivitas, pertanyaan menantang utk diskusi kelompok, soal evaluasi dll.'>LKPD</option>
<option value=' cara atau teknik yang mudah untuk menghafalkan materi (dengan contoh detail) '>Cara Menghafal</option>
<option value='Daftar glosarium penting dan penjelasan singkat. Tulis dalam tabel.'>Glosarium</option>
<option value=' Skrip naratif untuk membuat video pembelajaran berisi kalimat per kalimat narasi untuk menjelaskan pembelajaran secara deskriptif dan mudah dipahami. tuliskan dalam sebuah tabel 3 kolom dilengkapi dengan naskah transkrip narasi dan deskripsi visualnya. Gunakan style formal/resmi dan tone yang menggugah. tuliskan semuanya dalam satu buah tabel'>Skrip Video Pembelajaran</option>

<option  style="background-color: #FFFf00; color: #000;">&#9472;&#9472;&#9472;&#9472;Asesmen&#9472;&#9472;&#9472;&#9472;&#9472;&#9472;</option>
<option value='daftar kriteria untuk rubrik penilaian terhadap kompetensi siswa terhadap topik/materi pelajaran. '>Kriteria Rubrik Penilaian</option>
<option value='materi prasyarat (Prerequisisi) dan Outline kisi/kisi soal asesmen terhadap Pengetahuan prasyarat dan keterampilan prasyarat tersebut'>Kisi-kisi Asesmen/Penilaian Awal</option>
<option value='Outline kisi/kisi soal asesmen (meliputi aspek Pengetahuan Umum,Penyelesaian Masalah (Problem-Solving),Analisis-Evaluasi,Keterampilan Menerapkan Pengetahuan,Sikap) berikan satu atau lebih deskripsi soal pada setiap kriteria. Topik materinya  adalah: '>Kisi-kisi Asesmen/Penilaian Sumatif</option>

<option value=' saran profesional tentang ide asesmen pembelajaran dengan menuliskan paragraf terkait tujuan pembelajaran dikaitkan dengan SOLO taxonomy (the SOLO (structure of observed learning outcome) taxonomy developed by Biggs and Collis (1982) ) tuliskan rincian sesuai tahapannya. Setelah itu Kemudian  tulis ide asesmen siswa dgn menerapkan pendekatan pembelajaran mendalam yang  berdasar 3 PRINSIP PEMBELAJARAN dikombinasikan 3 PENGALAMAN BELAJAR. PRINSIP Pembelajaran yaitu (PRINSIP 1) pembelajaran berkesadarn (mindful-reflektif learning) (Peserta didik memahami tujuan pembelajaran dan termotivasi secara intrinsik untuk belajar. Peserta didik aktif meregulasi diri dalam belajar, merencanakan, melaksanakan, dan mengevaluasi reflektif cara belajar mereka.) , (PRINSIP 2) pembelajaran bermakna (meaningful learning) (Peserta didik menerapkan pengetahuan dalam situasi nyata,Proses belajar berorientasi pada kemampuan mengaplikasikan pengetahuan (learning tansfer), pemahaman mendalam bukan hanya menghafal informasi, melibatkan aktivasi pengetahuan awal), dan (PRINSIP 3) pembelajaran yang menggembirakan (joyful learning) (suasana belajar yang positif, menantang, menyenangkan, dan memotivasi, terlibat secara kognitif dan emosional). Prinsip tersebut dikombinasikan dengan 3 PENGALAMAN BELAJAR yaitu (PENGALAMAN 1) pemahaman mendalam, siswa termotivasi,terinspirasi,tidak hanya menghafal materi, (PENGALAMAN 2) aplikasi/penerapan dalam kehidupan nyata an bermanfaat secara nyata dan (PENGALAMAN 3) Refleksi, mampu melakukan refleksi hasil belajar, koneksi atau mengaitkan dengan konteks dan topik keilmuan lain dan kaitan dengan pembelajaran kelanjutan berikutnya. Jelaskan masing-masing poin tsb dalam tabel 3 baris pengalaman belajar dan 3 kolom prinsip pembelajaran.'>Asesmen Pembelajaran Deep Learning (2)</option>

<option value=' 5 (lima) buah soal pilihan ganda dan jawabannya dengan menerapkan variasi level kognitif tinggi (high order) pada taksonomi Bloom (tuliskan soal tanpa format heading dan berikan kunci jawaban.). tulis 5 soal dengan struktur format penulisan seperti berikut (gunakan format penulisannya, gantilah isi dari placeholder []):[1. Tulis soal disini]\na) [opsi Jawaban  a]\nb) [Jawaban pilihan b]\nc) [Jawaban pilihan c]\nd) [Jawaban pilihan d]\n\n[2. Tulis soal disini]\na) [Jawaban pilihan a]\nb) [Jawaban pilihan b]\nc) [Jawaban pilihan c]\nd) [Jawaban pilihan d]\n\n[3. Tulis soal disini]\na) [Jawaban pilihan a]\nb) [Jawaban pilihan b]\nc) [Jawaban pilihan c]\nd) [Jawaban pilihan d]\n\nKunci:\n[Jawaban kunci 1]\n[Jawaban kunci 2]\n[Jawaban kunci 3]'>Soal Pilihan Ganda</option>
<option value=' Tuliskan materi prasyarat (prerequisite) apa saja yang harus dikuasai sebelum belajara {materi} berikut ini dan dan buatkan soal untuk masing-masing materi prasyarat tersebut. Tuliskan dalam tabel 2 kolom, kolom pertama adalah prasyarat, kolom kedua berisi soal-soal untuk materi prasyarat.  '>Soal Prasyarat</option>
<option value=' Soal esai untuk dikerjakan siswa dengan menerapkan level kognitif higher order thinking (tuliskan soal tanpa format heading dan tanpa keterangan level kognitif)'>Soal Esai</option>
<option value=' Soal cerita (word problems) untuk dikerjakan siswa dengan menerapkan level kognitif higher order thinking (tuliskan soal tanpa format heading)'>Soal Cerita</option>
<option value=' Soal mengisi fill the blank'>Soal Isian</option>
<option value=' Soal atau pertanyaan menantang untuk menjadi bahan diskusi kelas atau diskusi kelompok (tuliskan soal tanpa format heading)'>Pertanyaan Diskusi</option>
<option value='Buatkan soal literasi pada suatu topik materi. Fokus pada kemampuan literasi: Soal literasi harus berfokus pada kemampuan membaca, menulis, dan memahami teks, bukan hanya mengingat fakta atau informasi.Menggunakan bahasa yang jelas dan singkat: Soal harus menggunakan bahasa yang jelas, singkat, dan tidak bermakna ganda.Memiliki stimulus yang relevan: Stimulus yang digunakan harus relevan dengan topik dan tujuan soal.Mengukur kemampuan yang spesifik: Soal harus mengukur kemampuan literasi yang spesifik, seperti kemampuan membaca pemahaman, kemampuan menulis, atau kemampuan menganalisis teks.Topik materinya adalah: '>Soal Literasi</option>
<option value='Buatkan soal numerasi pada suatu topik materi. Fokus pada kemampuan numerasi: Soal numerasi harus berfokus pada kemampuan menggunakan angka dan konsep matematika, bukan hanya mengingat fakta atau informasi.Menggunakan bahasa yang jelas dan singkat: Soal harus menggunakan bahasa yang jelas, singkat, dan tidak bermakna ganda.Memiliki konteks yang relevan: Konteks soal harus relevan dengan kehidupan sehari-hari atau bidang studi yang spesifik.Mengukur kemampuan yang spesifik: Soal harus mengukur kemampuan numerasi yang spesifik, seperti kemampuan menghitung, mengukur, atau menganalisis data.Topik materinya adalah: '>Soal Numerasi</option>
<option value='Buatkan soal sains  pada suatu topik materi. Fokus pada kemampuan sains: Soal numerasi harus berfokus pada kemampuan menggunakan langkah saintifik, bukan hanya mengingat fakta atau informasi.Menggunakan bahasa yang jelas dan singkat: Soal harus menggunakan bahasa yang jelas, singkat, dan tidak bermakna ganda.Memiliki konteks yang relevan: Konteks soal harus relevan dengan kehidupan sehari-hari atau bidang studi yang spesifik.Mengukur kemampuan yang spesifik: Soal harus mengukur kemampuan sains yang terkait nominal, fungsional, konseptual dan prosedural, dan multidimensi.Topik materinya adalah: '>Soal Literasi Sains</option>
<option value=' Buatkan daftar Tugas (asignment) bagi siswa untuk melatih kecakapan/keterampilan memecahkan masalah nyata disertai kriteria keberhsilan.'>Penugasan</option>
<option value=' Soal untuk latihan pemahaman dan jawaban penjelasan '>Soal Latihan</option>
<option value=' Lembar penilaian diri siswa dalam penguasaan materi '>Penilaian Diri</option>
<option value=' Lembar observasi penilaian siswa dalam penguasaan materi '>Penilaian Observasi</option>
<option value=' Jabaran dari konsep/variabel (tuliskan deskripsi atau definisi operasional), dimensi dan indikator yang sesuai dalam tabel. setelah itu sarankan pengukuran yang dapat dilakukan. Konsep/masalah yang akan diteliti adalah: '>Konsep/Variabel, Dimensi, Indikator Instrumen</option>
<option value='  '>Pertanyaan Umum</option>
                </select>

                <br/>
                <h3>Profil Kompetensi:</h3>
                <div class="kompetensi-container">
                    <div class="kompetensi-item">
                        <input type="checkbox" id="iman_takwa" name="kompetensi[]" value="Iman dan takwa">
                        <label for="iman_takwa">&nbsp Iman dan takwa</label>
                    </div>
                    <div class="kompetensi-item">
                        <input type="checkbox" id="kewargaan" name="kompetensi[]" value="Kewargaan">
                        <label for="kewargaan">&nbsp Kewargaan</label>
                    </div>
                    <div class="kompetensi-item">
                        <input type="checkbox" checked id="penalaran_kritis" name="kompetensi[]" value="Penalaran Kritis">
                        <label for="penalaran_kritis">&nbsp Penalaran Kritis</label>
                    </div>
                    <div class="kompetensi-item">
                        <input type="checkbox" checked id="kreativitas" name="kompetensi[]" value="Kreativitas">
                        <label for="kreativitas">&nbspKreativitas</label>
                    </div>
                    <div class="kompetensi-item">
                        <input type="checkbox" id="kolaborasi" name="kompetensi[]" value="Kolaborasi">
                        <label for="kolaborasi">&nbspKolaborasi</label>
                    </div>
                    <div class="kompetensi-item">
                        <input type="checkbox" id="kemandirian" name="kompetensi[]" value="Kemandirian">
                        <label for="kemandirian">&nbspKemandirian</label>
                    </div>
                    <div class="kompetensi-item">
                        <input type="checkbox" id="kesehatan" name="kompetensi[]" value="Kesehatan">
                        <label for="kesehatan">&nbspKesehatan</label>
                    </div>
                    <div class="kompetensi-item">
                        <input type="checkbox" id="komunikasi" name="kompetensi[]" value="Komunikasi">
                        <label for="komunikasi">&nbspKomunikasi</label>
                    </div>
                </div>

                <br>
                <select class="form-control" id="jenjang" required>
                    <option value="">Pilih Jenjang Kelas</option>
                    <option value="tk/paud">TK/PAUD</option>
                    <option value="sd kelas 1 - 2">A-SD Kelas 1-2</option>
                    <option value="sd kelas 3 - 4">B-SD Kelas 3-4</option>
                    <option value="sd kelas 5 - 6">C-SD Kelas 5-6</option>
                    <option value="SMP kelas 7 8 9">D-SMP Kelas 7-9</option>
                    <option value="SMA kelas 10">E-SMA/K Kelas 10</option>
                    <option value="SMA kelas 11-12">F-SMA/K Kelas 11-12</option>
                </select>

                <br>
                <textarea class="form-control" id="userInput" rows="3" placeholder="Topik materi"></textarea>
                <br>
                <button class="btn btn-warning btn-block" id="sendButton">SUBMIT</button>
                <br>
                <div id="loading" style="display:none;"><h1>LOADING...</h1><img height='200' src='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivL2OzreT_aLKW6K2aiRvsdStE1NiWdirOeWbbJjAwm6Ui7S7UiVCO_SALoD6ABs1mxzrYI1yEr4xAE2xzyOtUuIJZWLuRUxS8SsPeexSKFhwHR7V9HlywhORhtW2SbfIp5lTEohAzzyerakBYy65rkpUFflYh_5IfAaPYS0RSu2SwljQsEikWtkvHrwGw/s1600/loadingtech.gif' width='200'/></div>
            
                <!-- --- AREA HASIL TERSIMPAN BARU --- -->
                <div class="saved-items-container">
                    <h3>Hasil Tersimpan:</h3>
                    <div id="savedItemsContainer" class="saved-items-list">
                        <!-- Item tersimpan akan dimuat di sini oleh JS -->
                    </div>
                </div>
                <!-- --- AKHIR AREA HASIL TERSIMPAN --- -->

            </div>

            <!-- Kolom Hasil (kanan) - Diubah menjadi kontainer hasil dinamis -->
            <div class="col-md-9" id="resultsContainer">
                <h3 class="text-secondary mb-4">Hasil AI akan ditampilkan di sini:</h3>
            </div>
        </div>
    </div>

    <script>
        // Global map untuk menyimpan instans SimpleMDE
        const mdeInstances = {};
        let resultCounter = 0;
        const STORAGE_KEY = 'aiGuruToolkitSavedResults'; // Kunci LocalStorage

        // --- FUNGSI HELPER LOCALSTORAGE ---

        /**
         * Mengambil semua item dari LocalStorage
         */
        function getSavedItems() {
            const items = localStorage.getItem(STORAGE_KEY);
            return items ? JSON.parse(items) : [];
        }

        /**
         * Menyimpan array item ke LocalStorage
         */
        function saveItems(items) {
            localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
        }

        /**
         * Merender daftar item tersimpan di sidebar
         */
        function renderSavedList() {
            const items = getSavedItems();
            const container = document.getElementById('savedItemsContainer');
            container.innerHTML = ''; // Kosongkan daftar

            if (items.length === 0) {
                container.innerHTML = '<p class="text-muted" style="font-size: 12px;">Belum ada hasil tersimpan.</p>';
                return;
            }

            items.forEach(item => {
                const itemHtml = `
                    <div class="saved-item" id="saved-${item.id}">
                        <span class="saved-item-title" title="${item.title}" onclick="loadSavedItem('${item.id}')">
                            ${item.title}
                        </span>
                        <div class="saved-item-actions">
                            <button onclick="deleteSavedItem('${item.id}')">Hapus</button>
                        </div>
                    </div>
                `;
                container.innerHTML += itemHtml;
            });
        }

        /**
         * Fungsi Jendela: Menyimpan hasil ke LocalStorage
         */
        window.saveResult = function(id) {
            const mde = mdeInstances[id];
            if (!mde) return;

            const content = mde.value();
            if (!content || content.trim() === "") {
                alert('Tidak ada konten untuk disimpan.');
                return;
            }

            // Buat judul dari baris pertama (maks 40 karakter)
            let title = content.substring(0, 40).split('\n')[0].replace(/#/g, '').trim() || 'Hasil Tanpa Judul';
            
            // Minta konfirmasi judul
            const promptedTitle = prompt('Masukkan nama untuk hasil ini:', title);
            if (promptedTitle === null) return; // Batal
            
            title = promptedTitle.trim() || 'Hasil Tanpa Judul';

            const newId = new Date().getTime().toString();
            const newItem = { id: newId, title: title, content: content };

            const items = getSavedItems();
            items.unshift(newItem); // Tambahkan ke awal
            saveItems(items);
            
            renderSavedList(); // Perbarui daftar
            alert('Hasil berhasil disimpan!');
        }

        /**
         * Fungsi Jendela: Memuat item tersimpan ke editor baru
         */
        window.loadSavedItem = function(itemId) {
            const items = getSavedItems();
            const itemToLoad = items.find(item => item.id === itemId);

            if (itemToLoad) {
                // Buat kartu baru dan isi dengan konten
                const newMde = createNewResultCard(itemToLoad.content, `Tersimpan #${resultCounter + 1}: `);
                // Beri judul pada kartu
                const cardHeader = document.querySelector(`#card-${newMde.id.replace('mde-', '')} .result-header h4`);
                if(cardHeader) {
                    cardHeader.textContent = itemToLoad.title;
                }
            }
        }

        /**
         * Fungsi Jendela: Menghapus item dari LocalStorage
         */
        window.deleteSavedItem = function(itemId) {
            if (!confirm('Anda yakin ingin menghapus item tersimpan ini?')) return;

            let items = getSavedItems();
            items = items.filter(item => item.id !== itemId);
            saveItems(items);
            renderSavedList(); // Perbarui daftar
        }


        // --- FUNGSI INTI APLIKASI ---

        document.getElementById("sendButton").addEventListener("click", function() {
            var komponen = document.getElementById("komponen").value;
            var userInput = document.getElementById("userInput").value;
            var jenjang = document.getElementById("jenjang").value;
            var kompetensiTerpilih = ambilKompetensi();

            var message = "Tuliskan " + komponen + " " + userInput + " " + jenjang + ". Kaitkan dengan Profil kompetensi " + kompetensiTerpilih + " (Jawablah dengan Bahasa Indonesia!) tulis judul dengan format h1";

            if (message && userInput.trim() !== "") {
                document.getElementById("loading").style.display = "block";
                fetchMessages(message);
            } else {
                // Mengganti alert dengan tampilan UI yang lebih baik jika memungkinkan
                const container = document.getElementById('resultsContainer');
                container.insertAdjacentHTML('afterbegin', '<div class="alert alert-danger">Mohon isi topik materi terlebih dahulu.</div>');
            }
        });

        // Fungsi untuk menangani penghapusan hasil
        window.deleteResult = function(id) {
            // Mengganti alert dengan konfirmasi di UI jika memungkinkan
            if (confirm('Anda yakin ingin menghapus hasil #' + id.split('-')[1] + ' ini?')) {
                const card = document.getElementById(`card-${id}`);
                if (card) {
                    // Hancurkan instans SimpleMDE untuk membersihkan memori
                    if (mdeInstances[id]) {
                        mdeInstances[id].toTextArea();
                        delete mdeInstances[id];
                    }
                    // Hapus kartu dari DOM
                    card.remove();
                }
            }
        }

        // Fungsi untuk menangani penyalinan hasil (diperbarui untuk menyalin HTML yang di-render)
        window.copyResult = function(id) {
            const mde = mdeInstances[id];
            if (mde) {
                // Mengambil HTML yang di-render (Preview Area)
                const renderedContent = mde.markdown(mde.value());

                // Fungsi untuk menyalin HTML ke clipboard
                function copyHtmlToClipboard(html) {
                    // Menggunakan API Clipboard jika tersedia, jika tidak, fallback ke execCommand
                    if (navigator.clipboard && navigator.clipboard.write) {
                        const blob = new Blob([html], { type: 'text/html' });
                        const item = new ClipboardItem({ 'text/html': blob });
                        navigator.clipboard.write([item]).then(() => {
                            alert('Konten terformat (HTML) berhasil disalin ke clipboard!');
                        }).catch(err => {
                            console.error('Gagal menyalin menggunakan API Clipboard:', err);
                            // Fallback jika API Clipboard gagal
                            fallbackCopyHtml(html);
                        });
                    } else {
                        fallbackCopyHtml(html);
                    }
                }

                // Fallback untuk menyalin HTML
                function fallbackCopyHtml(html) {
                    const tempDiv = document.createElement('div');
                    tempDiv.innerHTML = html;
                    tempDiv.style.position = 'absolute';
                    tempDiv.style.left = '-9999px';
                    document.body.appendChild(tempDiv);

                    const selection = window.getSelection();
                    const range = document.createRange();
                    range.selectNodeContents(tempDiv);
                    selection.removeAllRanges();
                    selection.addRange(range);

                    try {
                        document.execCommand('copy');
                        alert('Konten terformat (HTML) berhasil disalin ke clipboard! (via fallback)');
                    } catch (err) {
                        console.error('Gagal menyalin (execCommand):', err);
                        alert('Gagal menyalin teks terformat. Silakan salin secara manual.');
                    } finally {
                        selection.removeAllRanges();
                        document.body.removeChild(tempDiv);
                    }
                }

                copyHtmlToClipboard(renderedContent);

            }
        }

        /**
         * Fungsi Baru: Membuat kartu hasil baru
         * @param {string} content - Konten awal untuk editor
         * @param {string} titlePrefix - Awalan untuk judul kartu
         * @returns {SimpleMDE} Instans MDE yang baru dibuat
         */
        function createNewResultCard(content, titlePrefix = "Hasil ke-") {
            resultCounter++;
            const newId = `mde-${resultCounter}`;
            const container = document.getElementById('resultsContainer');

            // 1. Buat struktur kartu (Tombol "Simpan" ditambahkan)
            const cardHtml = `
                <div class="result-card" id="card-${newId}">
                    <div class="result-header">
                        <h4 class="text-primary">${titlePrefix}${resultCounter}</h4>
                        <div class="result-actions">
                            <button class="btn btn-primary btn-sm" onclick="saveResult('${newId}')">Simpan</button>
                            <button class="btn btn-success btn-sm" onclick="copyResult('${newId}')">Salin</button>
                            <button class="btn btn-danger btn-sm" onclick="deleteResult('${newId}')">Hapus</button>
                        </div>
                    </div>
                    <textarea id="${newId}" rows="10"></textarea>
                </div>
            `;

            // Prepend kartu baru ke kontainer (yang terbaru di atas)
            container.insertAdjacentHTML('afterbegin', cardHtml);

            // 2. Inisialisasi SimpleMDE pada textarea baru
            const newMde = new SimpleMDE({
                element: document.getElementById(newId),
                spellChecker: false,
                toolbar: ["bold", "italic", "heading", "|", "quote", "unordered-list", "ordered-list", "|", "link", "image", "|", "preview", "side-by-side", "fullscreen"]
            });

            // Simpan instans secara global
            mdeInstances[newId] = newMde;
            newMde.value(content);

            // Tentukan apakah akan auto-preview
            if (content !== "Memuat hasil... Mohon tunggu sebentar.") {
                newMde.togglePreview(); // Auto-preview jika memuat dari storage
            }

            // Gulir ke hasil baru
            document.getElementById(`card-${newId}`).scrollIntoView({ behavior: 'smooth' });

            return newMde;
        }


        function fetchMessages(message) {
            // 1. Buat kartu baru dengan status loading
            const newMde = createNewResultCard("Memuat hasil... Mohon tunggu sebentar.");

            const settings = {
//                url: "https://taraka.id/apigate/cr-gpt-oss.php", // Endpoint diperbarui
//                url: "https://taraka.id/apigate/nvidia.php", // Endpoint diperbarui
//                url: "https://taraka.id/apigate/hf.php", // Endpoint diperbarui
                url: "https://taraka.id/apigate/nvidia.php",
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                data: JSON.stringify({
                    prompt: message
                }),
                dataType: "text" // Memberitahu jQuery agar mengharapkan teks
            };

            $.ajax(settings).done(function(response) {
                const resultText = response || "Tidak ada hasil yang dikembalikan."; 

                // 2. Atur konten pada MDE yang sudah ada
                newMde.value(resultText);
                newMde.togglePreview(); // Aktifkan preview secara otomatis

                document.getElementById("loading").style.display = "none";
            }).fail(function(jqXHR, textStatus, errorThrown) {
                // Buat pesan error yang lebih detail
                let errorMessage = "Gagal memuat hasil dari API.\n\n";
                errorMessage += "Status: " + textStatus + "\n";
                errorMessage += "Error: " + errorThrown + "\n";
                errorMessage += "Response Code: " + (jqXHR.status || 'N/A') + "\n";
                errorMessage += "Response Text: " + (jqXHR.responseText || 'Tidak ada respons') + "\n";
                
                console.error("AJAX Error:", {
                    jqXHR: jqXHR,
                    textStatus: textStatus,
                    errorThrown: errorThrown
                });

                newMde.value(errorMessage); // Tampilkan error detail di editor
                document.getElementById("loading").style.display = "none";
            });
        }

        // Fungsi untuk mengambil nilai checkbox yang dipilih
        function ambilKompetensi() {
            const semuaCheckbox = document.querySelectorAll('input[name="kompetensi[]"]:checked');
            const nilaiTerpilih = Array.from(semuaCheckbox).map(checkbox => checkbox.value);
            const hasilString = nilaiTerpilih.join(', ');
            return hasilString;
        }

        // --- INISIALISASI ---
        // Muat daftar item tersimpan saat halaman dibuka
        document.addEventListener('DOMContentLoaded', (event) => {
            renderSavedList();
        });
    </script>
    <!-- Histats.com START (html only)-->
    <a alt='free statistics' href='https://www.histats.com/viewstats/?SID=4767358&f=2' target='_blank'><div id='histatsC'><img border='0' src='//s4is.histats.com/stats/i/4767358.gif?4767358&103'/></div></a>
    <!-- Histats.com END -->
    <!-- Statcounter code for mtamim http://mtamim.com on Blogger -->
    <script type='text/javascript'>
    //<![CDATA[
    var sc_project=12953963;
     var sc_invisible=1;
     var sc_security="51347e8a";
     //]]>
    </script>
    <script async='async' src='https://www.statcounter.com/counter/counter_xhtml.js' type='text/javascript'></script>
    <noscript><div class='statcounter'><a class='statcounter' href='https://statcounter.com/' title='Web Analytics Made Easy - Statcounter'><img alt='Web Analytics Made Easy - Statcounter' class='statcounter' referrerpolicy='no-referrer-when-downgrade' src='https://c.statcounter.com/12953963/0/51347e8a/1/'/></a></div></noscript>
    <!-- End of Statcounter Code -->
</body>
</html>

