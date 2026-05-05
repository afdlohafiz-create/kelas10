import streamlit as st

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="CBT Kimia - Kelas 10", 
    page_icon="🎓", 
    layout="centered", 
    initial_sidebar_state="collapsed" 
)

# --- 2. TEMA "KERTAS UJIAN" & BIRU CERAH (ANTI SAKIT MATA) ---
st.markdown("""
    <style>
    /* 1. Background Layar: Gradasi Biru Langit Cerah */
    .stApp {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    }
    
    /* Animasi Gelembung Halus di Background */
    .bubbles { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none; }
    .bubble { position: absolute; bottom: -100px; background: rgba(255, 255, 255, 0.3); border: 1px solid rgba(255, 255, 255, 0.6); border-radius: 50%; animation: float 8s infinite ease-in; }
    .bubble:nth-child(1) { left: 15%; width: 40px; height: 40px; animation-duration: 9s; }
    .bubble:nth-child(2) { left: 35%; width: 20px; height: 20px; animation-duration: 5s; animation-delay: 2s; }
    .bubble:nth-child(3) { left: 55%; width: 50px; height: 50px; animation-duration: 11s; animation-delay: 1s; }
    .bubble:nth-child(4) { left: 75%; width: 30px; height: 30px; animation-duration: 6s; animation-delay: 3s; }
    .bubble:nth-child(5) { left: 85%; width: 25px; height: 25px; animation-duration: 8s; animation-delay: 0s; }
    @keyframes float { 0% { transform: translateY(0); opacity: 1; } 100% { transform: translateY(-1200px); opacity: 0; } }

    /* 2. Papan Kertas Utama (Solid White) */
    .block-container {
        background-color: #ffffff !important;
        border-radius: 20px !important;
        padding: 40px 30px !important;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2) !important;
        margin-top: 40px !important;
        margin-bottom: 40px !important;
        max-width: 850px !important;
    }

    /* 3. Memaksa SEMUA teks di dalam kertas menjadi Hitam/Gelap */
    h1, h2, h3, p, span, li, label {
        color: #1e293b !important;
    }
    
    /* 4. Kotak Info & Peringatan (Biru Muda) */
    div[data-testid="stAlert"] {
        background-color: #e0f2fe !important;
        border: 1px solid #bae6fd !important;
        border-radius: 10px !important;
    }
    div[data-testid="stAlert"] p, div[data-testid="stAlert"] span {
        color: #0369a1 !important;
    }

    /* 5. Input Form & Dropdown (Agar terlihat di Dark Mode) */
    .stTextInput input, .stNumberInput input, div[data-baseweb="select"] > div {
        background-color: #f8fafc !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
    }
    
    /* 6. Desain Tombol Biru Elegan */
    .stButton button { 
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%) !important; 
        color: white !important; 
        font-weight: bold !important; 
        border-radius: 8px !important; 
        border: none !important;
        padding: 10px !important;
        transition: 0.3s;
    }
    .stButton button p { color: white !important; } /* Teks tombol tetap putih */
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(2, 132, 199, 0.4);
    }
    </style>
    
    <!-- Memasukkan Animasi Gelembung ke HTML -->
    <div class="bubbles">
        <div class="bubble"></div><div class="bubble"></div>
        <div class="bubble"></div><div class="bubble"></div><div class="bubble"></div>
    </div>
""", unsafe_allow_html=True)

# --- 3. DATABASE BANK SOAL KELAS 10 (FULL 120 SOAL) ---
DATABASE_SOAL = {
    "1. Hakikat Kimia & Metode Ilmiah": [
        {"tipe": "mcq", "soal": "Dalam metode ilmiah, jika eksperimen gagal membuktikan hipotesis awal, langkah ilmuwan adalah...", "opsi": ["A. Memanipulasi data", "B. Menolak hipotesis dan merumuskan hipotesis baru", "C. Mengubah teori", "D. Berhenti"], "jawaban": "B. Menolak hipotesis dan merumuskan hipotesis baru", "pembahasan": "Sikap ilmiah menuntut objektivitas. Hipotesis yang ditolak adalah dasar untuk revisi."},
        {"tipe": "tf", "soal": "Jika menumpahkan asam pekat, langsung netralkan dengan NaOH.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Memicu reaksi eksotermik. Bilas dengan air mengalir."},
        {"tipe": "multiselect", "soal": "Pilih alat ukur presisi (volumetrik):", "opsi": ["Gelas Kimia", "Labu Ukur", "Buret", "Labu Erlenmeyer", "Pipet Volume"], "jawaban": ["Labu Ukur", "Buret", "Pipet Volume"], "pembahasan": "Gelas kimia dan erlenmeyer skalanya tidak akurat."},
        {"tipe": "short_answer", "soal": "Simbol tengkorak bersilang menandakan bahan bersifat... (Ketik kata)", "opsi": [], "jawaban": "beracun", "pembahasan": "Simbol Toxic berarti beracun."},
        {"tipe": "mcq", "soal": "Peran kimia dalam biologi terlihat pada...", "opsi": ["A. Serat sintetis", "B. Microchip", "C. Metabolisme enzim", "D. Avtur"], "jawaban": "C. Metabolisme enzim", "pembahasan": "Proses enzimatis adalah Biokimia."},
        {"tipe": "tf", "soal": "Cara membaui gas di tabung reaksi adalah mendekatkan hidung tepat di atasnya.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Sangat berbahaya! Harus dikibas-kibaskan (wafting)."},
        {"tipe": "short_answer", "soal": "Dugaan sementara terhadap rumusan masalah disebut...", "opsi": [], "jawaban": "hipotesis", "pembahasan": "Hipotesis adalah jawaban sementara."},
        {"tipe": "multiselect", "soal": "Sikap ilmiah peneliti kimia:", "opsi": ["Jujur data", "Subjektif", "Terbuka kritik", "Keras kepala", "Rasa ingin tahu"], "jawaban": ["Jujur data", "Terbuka kritik", "Rasa ingin tahu"], "pembahasan": "Harus objektif dan inovatif."},
        {"tipe": "mcq", "soal": "Prosedur membuat asam sulfat encer dari pekat adalah...", "opsi": ["A. Air ke asam", "B. Asam pekat ke air sambil diaduk", "C. Campur sekaligus", "D. Panaskan air"], "jawaban": "B. Asam pekat ke air sambil diaduk", "pembahasan": "Add Acid to Water. Mencegah percikan eksotermik."},
        {"tipe": "numeric", "soal": "Berapa banyak jenis variabel utama dalam eksperimen? (Bebas, Terikat, Kontrol)", "opsi": [], "jawaban": 3, "pembahasan": "Ada 3 variabel utama."},
        {"tipe": "mcq", "soal": "Lemari asam (Fume Hood) tepat digunakan saat...", "opsi": ["A. Menimbang kristal", "B. Melarutkan gula", "C. Mereaksikan gas beracun", "D. Mengukur suhu"], "jawaban": "C. Mereaksikan gas beracun", "pembahasan": "Lemari asam menghisap gas berbahaya."},
        {"tipe": "tf", "soal": "Zat sintetis selalu bahaya, zat alami selalu aman.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Bisa ular (alami) mematikan, obat (sintetis) menyembuhkan."},
        {"tipe": "multiselect", "soal": "Kontribusi kimia di bidang medis:", "opsi": ["Vaksin", "Pestisida", "Radioisotop", "Alat pacu jantung", "Baja ringan"], "jawaban": ["Vaksin", "Radioisotop", "Alat pacu jantung"], "pembahasan": "Pestisida pertanian, baja ringan konstruksi."},
        {"tipe": "mcq", "soal": "Mengumpulkan informasi dari kejadian nyata disebut...", "opsi": ["A. Eksperimen", "B. Observasi", "C. Hipotesis", "D. Analisis"], "jawaban": "B. Observasi", "pembahasan": "Langkah pertama metode ilmiah."},
        {"tipe": "short_answer", "soal": "Simbol Flammable menandakan bahan mudah...", "opsi": [], "jawaban": "terbakar", "pembahasan": "Mudah menyala (alkohol, eter)."},
        {"tipe": "mcq", "soal": "Data angka pasti disebut data...", "opsi": ["A. Kualitatif", "B. Subjektif", "C. Kuantitatif", "D. Relatif"], "jawaban": "C. Kuantitatif", "pembahasan": "Kuantitas = numerik."},
        {"tipe": "tf", "soal": "Tumpahan zat korosif dilap dengan kain lap.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Gunakan spill kit atau penetral, kain akan hancur."},
        {"tipe": "multiselect", "soal": "Peralatan tahan panas tinggi:", "opsi": ["Cawan porselen", "Buret", "Kaca arloji", "Tabung pyrex", "Gelas ukur plastik"], "jawaban": ["Cawan porselen", "Tabung pyrex"], "pembahasan": "Plastik dan buret rusak dipanaskan."},
        {"tipe": "mcq", "soal": "Variabel yang dipertahankan tetap disebut variabel...", "opsi": ["A. Bebas", "B. Terikat", "C. Kontrol", "D. Pengganggu"], "jawaban": "C. Kontrol", "pembahasan": "Kontrol menjaga validitas eksperimen."},
        {"tipe": "short_answer", "soal": "Jas lab putih agar bahan kimia yang ... lebih terlihat.", "opsi": [], "jawaban": "tumpah", "pembahasan": "Bercak mudah dideteksi."}
    ],
    "2. Struktur Atom & SPU": [
        {"tipe": "mcq", "soal": "Sinar alfa yang memantul (Eksperimen Rutherford) membuktikan atom memiliki...", "opsi": ["A. Ruang hampa", "B. Inti padat bermuatan positif", "C. Elektron", "D. Neutron"], "jawaban": "B. Inti padat bermuatan positif", "pembahasan": "Pantulan akibat tolakan inti padat."},
        {"tipe": "tf", "soal": "C-12 dan C-14 beda sifat kimianya karena massa neutronnya beda.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Sifat kimia ditentukan jumlah elektron, bukan massa neutron."},
        {"tipe": "numeric", "soal": "Ion X^2+ punya 18 elektron & 20 neutron. Massa atom X?", "opsi": [], "jawaban": 40, "pembahasan": "Proton = 18+2=20. Massa = 20+20=40."},
        {"tipe": "multiselect", "soal": "Prinsip Mekanika Kuantum:", "opsi": ["Orbital = probabilitas terbesar", "1 orbital isi 2 elektron", "Posisi presisi dapat dihitung", "Subkulit d punya 5 orbital"], "jawaban": ["Orbital = probabilitas terbesar", "1 orbital isi 2 elektron", "Subkulit d punya 5 orbital"], "pembahasan": "Posisi pasti mustahil ditentukan (Heisenberg)."},
        {"tipe": "short_answer", "soal": "Tak ada 2 elektron dengan 4 bil.kuantum sama adalah larangan...", "opsi": [], "jawaban": "pauli", "pembahasan": "Asas Pauli."},
        {"tipe": "mcq", "soal": "Energi ionisasi: 738, 1451, 7733. Golongan unsur?", "opsi": ["A. IA", "B. IIA", "C. IIIA", "D. VIIA"], "jawaban": "B. IIA", "pembahasan": "Lonjakan besar di pelepasan ke-3, berarti valensinya 2."},
        {"tipe": "numeric", "soal": "Jumlah elektron tak berpasangan Kromium (Cr, Z=24)?", "opsi": [], "jawaban": 6, "pembahasan": "Anomali 4s1 3d5. Total 6."},
        {"tipe": "tf", "soal": "Se-golongan ke bawah, energi ionisasi makin kecil karena shielding effect.", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Kulit bertambah menghalangi tarikan inti."},
        {"tipe": "multiselect", "soal": "Isoelektronik (10e): O^2-, F^-, Ne, Na^+.", "opsi": ["Keempat isoelektronik", "Ukuran Na^+ terbesar", "Ukuran O^2- terbesar", "Ionisasi Ne tertinggi"], "jawaban": ["Keempat isoelektronik", "Ukuran O^2- terbesar", "Ionisasi Ne tertinggi"], "pembahasan": "Proton terkecil (O=8) ukurannya merenggang terbesar."},
        {"tipe": "short_answer", "soal": "Isi orbital sejajar sebelum berpasangan adalah aturan...", "opsi": [], "jawaban": "hund", "pembahasan": "Aturan Hund."},
        {"tipe": "mcq", "soal": "Jari-jari Klorin < Natrium karena...", "opsi": ["A. Wujud gas", "B. Muatan inti Cl lebih kuat", "C. Beda kulit", "D. Na stabil"], "jawaban": "B. Muatan inti Cl lebih kuat", "pembahasan": "Proton seperiode bertambah, atom mengerut."},
        {"tipe": "tf", "soal": "Gas mulia keelektronegatifan terbesar.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Gas mulia nol. Tertinggi Halogen."},
        {"tipe": "multiselect", "soal": "Sifat Logam Transisi:", "opsi": ["Beragam biloks", "Katalis", "Berwarna", "Paramagnetik", "Reaktif air dingin"], "jawaban": ["Beragam biloks", "Katalis", "Berwarna", "Paramagnetik"], "pembahasan": "Tidak reaktif air dingin."},
        {"tipe": "short_answer", "soal": "Fosforus (Z=15) di golongan... (Format: VA, VIA)", "opsi": [], "jawaban": "va", "pembahasan": "Valensi 5 di blok p."},
        {"tipe": "numeric", "soal": "Nilai azimuth (l) maksimal di kulit N (n=4)?", "opsi": [], "jawaban": 3, "pembahasan": "s,p,d,f = 0,1,2,3."},
        {"tipe": "mcq", "soal": "Afinitas elektron Cl lebih negatif dari F karena...", "opsi": ["A. Atom F terlalu kecil jadi tolakan besar", "B. Elektronegatif Cl besar", "C. F gas mulia", "D. Inti F lemah"], "jawaban": "A. Atom F terlalu kecil jadi tolakan besar", "pembahasan": "Anomali ukuran Fluor yang terlalu rapat."},
        {"tipe": "tf", "soal": "Kuantum magnetik atur putaran elektron.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Magnetik = orientasi orbital. Putaran = spin."},
        {"tipe": "multiselect", "soal": "Atom ns2 np5 adalah:", "opsi": ["Halogen", "Ion -1", "Molekul diatomik", "Konduktor"], "jawaban": ["Halogen", "Ion -1", "Molekul diatomik"], "pembahasan": "Non-logam isolator."},
        {"tipe": "mcq", "soal": "Setelah 4s, elektron masuk ke...", "opsi": ["A. 4p", "B. 3d", "C. 5s", "D. 4d"], "jawaban": "B. 3d", "pembahasan": "Aufbau."},
        {"tipe": "short_answer", "soal": "Partikel ringan pengeliling inti...", "opsi": [], "jawaban": "elektron", "pembahasan": "Massa diabaikan."}
    ],
    "3. Ikatan Kimia & Bentuk Molekul": [
        {"tipe": "mcq", "soal": "BF3 stabil meski hanya 6 elektron valensi. Ini disebut...", "opsi": ["A. Perluasan oktet", "B. Penyimpangan oktet tidak lengkap", "C. Ikatan ion", "D. Ikatan hidrogen"], "jawaban": "B. Penyimpangan oktet tidak lengkap", "pembahasan": "Boron mencapai kestabilan dengan 6e."},
        {"tipe": "short_answer", "soal": "Tarikan elektrostatis kation dan anion disebut ikatan...", "opsi": [], "jawaban": "ion", "pembahasan": "Ikatan ion/elektrovalen."},
        {"tipe": "tf", "soal": "Syarat ikatan ion adalah melibatkan gas mulia.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Gas mulia sukar bereaksi. Syaratnya beda elektronegatifan besar."},
        {"tipe": "multiselect", "soal": "Molekul POLAR ikatannya tapi NON-POLAR sifatnya (simetris):", "opsi": ["CO2", "H2O", "CCl4", "NH3"], "jawaban": ["CO2", "CCl4"], "pembahasan": "Bentuk simetris meniadakan dipol."},
        {"tipe": "mcq", "soal": "Cairan ditarik penggaris listrik statis. Cairan itu adalah...", "opsi": ["A. H2O (Polar)", "B. CCl4 (Nonpolar)", "C. O2 cair", "D. Bensin"], "jawaban": "A. H2O (Polar)", "pembahasan": "Sifat molekul polar terimbas medan listrik."},
        {"tipe": "numeric", "soal": "Ikatan koordinasi di SO3 (oktet murni)?", "opsi": [], "jawaban": 2, "pembahasan": "1 rangkap dua, 2 koordinasi donor S."},
        {"tipe": "mcq", "soal": "Bentuk molekul AX3E2 (IF3) adalah...", "opsi": ["A. Segitiga planar", "B. Bentuk T", "C. Linear", "D. Oktahedral"], "jawaban": "B. Bentuk T", "pembahasan": "Bipiramida trigonal buang 2 ekuatorial jadi T-shape."},
        {"tipe": "tf", "soal": "CH4 dan NH3 punya sudut ikatan 109.5 persis sama.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "NH3 punya PEB menekan sudut jadi 107."},
        {"tipe": "numeric", "soal": "Jumlah PEB Xenon di XeF4?", "opsi": [], "jawaban": 2, "pembahasan": "8 valensi - 4 pakai = sisa 4e (2 PEB)."},
        {"tipe": "short_answer", "soal": "Teori bentuk molekul karena gaya tolak pasangan valensi disingkat...", "opsi": [], "jawaban": "vsepr", "pembahasan": "Valence Shell Electron Pair Repulsion."},
        {"tipe": "multiselect", "soal": "Zat dengan Ikatan Hidrogen antarmolekul:", "opsi": ["H2O", "H2S", "HF", "NH3", "CH4"], "jawaban": ["H2O", "HF", "NH3"], "pembahasan": "H terikat ke F, O, atau N."},
        {"tipe": "mcq", "soal": "H2O cair 100C, H2S gas -60C karena...", "opsi": ["A. Ikatan kovalen H2O kuat", "B. H2O punya ikatan hidrogen", "C. S lebih berat", "D. H2S ionik"], "jawaban": "B. H2O punya ikatan hidrogen", "pembahasan": "Ikatan antarmolekul H2O sangat kuat."},
        {"tipe": "tf", "soal": "Gaya London tidak ada di molekul polar.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Gaya London ada di SEMUA jenis molekul."},
        {"tipe": "multiselect", "soal": "Sifat kristal ionik:", "opsi": ["Titik leleh tinggi", "Rapuh dipukul", "Lelehan konduktor", "Lunak"], "jawaban": ["Titik leleh tinggi", "Rapuh dipukul", "Lelehan konduktor"], "pembahasan": "Isolator di fase padat."},
        {"tipe": "mcq", "soal": "Zat X padat isolator, leleh konduktor terang. Ikatan...", "opsi": ["A. Polar", "B. Ionik", "C. Logam", "D. Nonpolar"], "jawaban": "B. Ionik", "pembahasan": "Sifat khas lelehan ion."},
        {"tipe": "numeric", "soal": "Momen dipol molekul simetris sempurna SF6?", "opsi": [], "jawaban": 0, "pembahasan": "Resultan dipol 0."},
        {"tipe": "short_answer", "soal": "Tarik awan elektron bebas dan ion positif di kisi kristal adalah ikatan...", "opsi": [], "jawaban": "logam", "pembahasan": "Teori lautan elektron."},
        {"tipe": "mcq", "soal": "Hibridisasi PCl5 (AX5) adalah...", "opsi": ["A. sp3", "B. sp3d", "C. sp3d2", "D. dsp3"], "jawaban": "B. sp3d", "pembahasan": "5 orbital = s + ppp + d."},
        {"tipe": "tf", "soal": "Dipol-dipol terjadi antar molekul nonpolar murni.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Dipol-dipol untuk molekul POLAR."},
        {"tipe": "multiselect", "soal": "Molekul AX4 tetrahedral murni:", "opsi": ["CH4", "CCl4", "NH3", "H2O"], "jawaban": ["CH4", "CCl4"], "pembahasan": "Tanpa PEB."}
    ],
    "4. Larutan Elektrolit & Non-Elektrolit": [
        {"tipe": "mcq", "soal": "Lampu X redup, Y terang. Kesimpulan?", "opsi": ["A. X non", "B. X lemah, Y kuat", "C. Sama", "D. Y non"], "jawaban": "B. X lemah, Y kuat", "pembahasan": "Cahaya identifikasi kekuatan ionisasi."},
        {"tipe": "tf", "soal": "Padatan NaCl adalah konduktor baik.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Padatan ionnya tidak bebas bergerak."},
        {"tipe": "multiselect", "soal": "Kovalen polar yang MENGHANTARKAN arus di air:", "opsi": ["HCl", "CH3COOH", "NH3", "Sukrosa"], "jawaban": ["HCl", "CH3COOH", "NH3"], "pembahasan": "Sukrosa non-elektrolit."},
        {"tipe": "short_answer", "soal": "Teori ionisasi dicetuskan oleh...", "opsi": [], "jawaban": "arrhenius", "pembahasan": "Svante Arrhenius."},
        {"tipe": "numeric", "soal": "Derajat ionisasi % jika 1.5 mol urai dari 2 mol?", "opsi": [], "jawaban": 75, "pembahasan": "1.5/2 = 75%."},
        {"tipe": "mcq", "soal": "Leleh P konduktor, leleh Q isolator. Di air keduanya konduktor. Jenis P & Q?", "opsi": ["A. P ionik, Q polar", "B. Semua ionik", "C. P polar, Q ionik", "D. Semua nonpolar"], "jawaban": "A. P ionik, Q polar", "pembahasan": "Polar cair (Q) murni isolator, tapi larut air jadi elektrolit."},
        {"tipe": "multiselect", "soal": "Larutan NON-ELEKTROLIT:", "opsi": ["Glukosa", "Urea", "Etanol", "NaCl"], "jawaban": ["Glukosa", "Urea", "Etanol"], "pembahasan": "Tidak pecah jadi ion."},
        {"tipe": "tf", "soal": "Asam kuat adalah elektrolit kuat.", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Terion sempurna."},
        {"tipe": "numeric", "soal": "Total ion dari ionisasi Fe2(SO4)3 ?", "opsi": [], "jawaban": 5, "pembahasan": "2 + 3 = 5 partikel."},
        {"tipe": "short_answer", "soal": "Pemecahan molekul di air jadi ion positif negatif disebut...", "opsi": [], "jawaban": "ionisasi", "pembahasan": "Disosiasi / Ionisasi."},
        {"tipe": "mcq", "soal": "NH3 basa elektrolit lemah karena...", "opsi": ["A. Molekulnya pecah", "B. Bereaksi air hasilkan NH4+ dan OH-", "C. Melepas H+", "D. Larut fisik"], "jawaban": "B. Bereaksi air hasilkan NH4+ dan OH-", "pembahasan": "Reaksi hidrolisis amonia."},
        {"tipe": "tf", "soal": "Semua kovalen polar PASTI elektrolit di air.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Air, gula, alkohol sangat polar tapi non-elektrolit."},
        {"tipe": "multiselect", "soal": "Lampu mati menandakan:", "opsi": ["Non-elektrolit", "Ionisasi=0", "Sangat lemah ion tak cukup", "Asam kuat"], "jawaban": ["Non-elektrolit", "Ionisasi=0", "Sangat lemah ion tak cukup"], "pembahasan": "Zat lemah kadang lampu mati tapi ada gelembung."},
        {"tipe": "short_answer", "soal": "Derajat ionisasi senyawa kuat sempurna adalah...", "opsi": [], "jawaban": "1", "pembahasan": "100% = 1."},
        {"tipe": "mcq", "soal": "Air hujan industri (gelembung ada, lampu mati).", "opsi": ["A. Kuat", "B. Lemah", "C. Non-elektrolit", "D. Garam"], "jawaban": "B. Lemah", "pembahasan": "Kandungan asam polusi sangat encer."},
        {"tipe": "numeric", "soal": "Valensi H+ lepas dari H3PO4 sempurna?", "opsi": [], "jawaban": 3, "pembahasan": "Triprotik."},
        {"tipe": "tf", "soal": "Gula larut putus jadi C, H, O.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Hanya terikat hidrogen dengan pelarut, struktur utuh."},
        {"tipe": "multiselect", "soal": "Larutan 1M mana paling terang (ion terbanyak)?", "opsi": ["H2SO4", "CaCl2", "NaCl", "CH3COOH"], "jawaban": ["H2SO4", "CaCl2"], "pembahasan": "Menghasilkan 3 ion/molekul."},
        {"tipe": "mcq", "soal": "Derajat: A(0), B(0.8), C(0.1). Urutan dari paling lemah:", "opsi": ["A. A-B-C", "B. A-C-B", "C. B-C-A", "D. C-B-A"], "jawaban": "B. A-C-B", "pembahasan": "0 < 0.1 < 0.8."},
        {"tipe": "short_answer", "soal": "Zat yang dilarutkan ke air disebut...", "opsi": [], "jawaban": "terlarut", "pembahasan": "Zat terlarut / solute."}
    ],
    "5. Reaksi Reduksi-Oksidasi (Redoks)": [
        {"tipe": "mcq", "soal": "Pada Mg + O2 -> MgO, Mg bertindak sebagai...", "opsi": ["A. Oksidator", "B. Reduktor", "C. Katalis", "D. Produk"], "jawaban": "B. Reduktor", "pembahasan": "Mg mengalami oksidasi, sehingga menjadi agen pereduksi (reduktor)."},
        {"tipe": "tf", "soal": "Biloks H selalu +1 di semua senyawa.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Di senyawa Hidrida logam (misal NaH), biloks H = -1."},
        {"tipe": "numeric", "soal": "Biloks atom Cr di ion dikromat (Cr2O7^2-)?", "opsi": [], "jawaban": 6, "pembahasan": "2(Cr) + 7(-2) = -2 -> 2(Cr) = +12 -> Cr = +6."},
        {"tipe": "multiselect", "soal": "Oksidator kuat (biloks unsur pusat maksimum):", "opsi": ["KMnO4", "K2Cr2O7", "H2S", "HNO3 pekat"], "jawaban": ["KMnO4", "K2Cr2O7", "HNO3 pekat"], "pembahasan": "KMnO4 (Mn +7), K2Cr2O7 (Cr +6), HNO3 (N +5)."},
        {"tipe": "short_answer", "soal": "Reaksi satu unsur jadi reduktor sekaligus oksidator disebut reaksi...", "opsi": [], "jawaban": "autoredoks", "pembahasan": "Atau disebut reaksi disproporsionasi."},
        {"tipe": "mcq", "soal": "Cu2+ + Zn -> Cu + Zn2+. Pernyataan yang benar:", "opsi": ["A. Cu2+ melepas 2 elektron", "B. Zn reduksi", "C. Cu2+ bertindak sebagai oksidator", "D. Zn oksidator"], "jawaban": "C. Cu2+ bertindak sebagai oksidator", "pembahasan": "Cu2+ menangkap elektron (reduksi) sehingga menjadi oksidator."},
        {"tipe": "tf", "soal": "Karat pada besi adalah contoh reaksi redoks.", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Oksidasi logam besi oleh oksigen lingkungan."},
        {"tipe": "numeric", "soal": "Selisih biloks S di H2SO4 dan H2S? (Angka mutlak)", "opsi": [], "jawaban": 8, "pembahasan": "+6 dan -2. Selisih = 8."},
        {"tipe": "multiselect", "soal": "Bukan termasuk reaksi redoks:", "opsi": ["HCl + NaOH -> NaCl + H2O", "AgNO3 + NaCl -> AgCl + NaNO3", "Pembakaran gas metana"], "jawaban": ["HCl + NaOH -> NaCl + H2O", "AgNO3 + NaCl -> AgCl + NaNO3"], "pembahasan": "Asam basa dan pengendapan tidak memindahkan elektron."},
        {"tipe": "short_answer", "soal": "Nama IUPAC untuk Fe2O3 adalah Besi(...) oksida. Angka romawinya:", "opsi": [], "jawaban": "iii", "pembahasan": "Biloks Fe = +3, jadi Besi(III) oksida."},
        {"tipe": "mcq", "soal": "2S2O3^2- + I2 -> S4O6^2- + 2I-. Zat yang direduksi:", "opsi": ["A. S2O3^2-", "B. I2", "C. S4O6^2-", "D. I-"], "jawaban": "B. I2", "pembahasan": "I2 (biloks 0) jadi I- (biloks -1). Mengalami penurunan."},
        {"tipe": "tf", "soal": "Biloks molekul unsur bebas seperti O3 adalah 3.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Biloks semua unsur bebas murni adalah NOL."},
        {"tipe": "numeric", "soal": "Biloks O dalam Hidrogen peroksida (H2O2)?", "opsi": [], "jawaban": -1, "pembahasan": "Dalam peroksida, aturan biloks O = -1."},
        {"tipe": "multiselect", "soal": "Penerapan reaksi redoks di sekitar kita:", "opsi": ["Fotosintesis tumbuhan", "Baterai HP", "Pemutih pakaian", "Penyulingan air"], "jawaban": ["Fotosintesis tumbuhan", "Baterai HP", "Pemutih pakaian"], "pembahasan": "Menyuling air murni perubahan fisika."},
        {"tipe": "short_answer", "soal": "Zat yang teroksidasi bertindak sebagai agen... (reduktor/oksidator)", "opsi": [], "jawaban": "reduktor", "pembahasan": "Mengalami oksidasi = Mereduksi lawannya = Reduktor."},
        {"tipe": "mcq", "soal": "Senyawa dengan N biloks terendah:", "opsi": ["A. NO2", "B. N2O", "C. NH3", "D. HNO3"], "jawaban": "C. NH3", "pembahasan": "Di NH3, biloks N adalah -3 (minimumnya)."},
        {"tipe": "tf", "soal": "F- adalah reduktor terkuat karena paling elektronegatif.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Fluorin (F2) sangat mudah menangkap elektron, jadi ia OKSIDATOR terkuat."},
        {"tipe": "numeric", "soal": "Tentukan biloks atom Karbon pada ion CO3^2-!", "opsi": [], "jawaban": 4, "pembahasan": "C + 3(-2) = -2 -> C = +4."},
        {"tipe": "multiselect", "soal": "Mencegah korosi besi secara aktif/pasif:", "opsi": ["Pengecatan", "Galvanisasi zink", "Perlindungan katodik (Magnesium)", "Melapisi tembaga murni"], "jawaban": ["Pengecatan", "Galvanisasi zink", "Perlindungan katodik (Magnesium)"], "pembahasan": "Melapisi tembaga (kurang reaktif) mempercepat korosi besi jika tergores."},
        {"tipe": "short_answer", "soal": "Elektroda tempat terjadinya pelepasan elektron (oksidasi) disebut...", "opsi": [], "jawaban": "anoda", "pembahasan": "KRAO (Katoda Reduksi, Anoda Oksidasi)."}
    ],
    "6. Stoikiometri Kimia": [
        {"tipe": "mcq", "soal": "Hukum Kekekalan Massa dikemukakan oleh...", "opsi": ["A. Dalton", "B. Proust", "C. Lavoisier", "D. Avogadro"], "jawaban": "C. Lavoisier", "pembahasan": "Antoine Lavoisier membakar zat di ruang tertutup."},
        {"tipe": "tf", "soal": "Hukum Proust nyatakan perbandingan massa unsur senyawa murni selalu tetap.", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Misal H2O dimanapun selalu 1:8 massanya."},
        {"tipe": "numeric", "soal": "Jumlah mol 36 gram H2O? (Mr=18)", "opsi": [], "jawaban": 2, "pembahasan": "36 / 18 = 2 mol."},
        {"tipe": "multiselect", "soal": "Kondisi STP gas:", "opsi": ["Suhu 0 C (273 K)", "Tekanan 1 atm", "Volume 22.4 L/mol", "Suhu 25 C"], "jawaban": ["Suhu 0 C (273 K)", "Tekanan 1 atm", "Volume 22.4 L/mol"], "pembahasan": "Standard Temperature and Pressure."},
        {"tipe": "short_answer", "soal": "Hukum Perbandingan Berganda dikemukakan oleh... (Nama belakang)", "opsi": [], "jawaban": "dalton", "pembahasan": "John Dalton."},
        {"tipe": "mcq", "soal": "10 L N2 bereaksi berlebih jadi NO. Volume NO dihasilkan?", "opsi": ["A. 5 L", "B. 10 L", "C. 20 L", "D. 30 L"], "jawaban": "C. 20 L", "pembahasan": "N2 + O2 -> 2NO. Koefisien 1 banding 2. Maka 10L jadi 20L."},
        {"tipe": "tf", "soal": "Pada RTP (25 C), volume 1 mol gas persis 22.4 L.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "RTP volumenya ~24.4 L. 22.4 L itu saat STP (0 C)."},
        {"tipe": "numeric", "soal": "Massa 0.5 mol NaOH? (Mr=40)", "opsi": [], "jawaban": 20, "pembahasan": "0.5 x 40 = 20 gram."},
        {"tipe": "multiselect", "soal": "Mol digunakan untuk menghitung jumlah unit makroskopik berupa:", "opsi": ["Atom", "Molekul", "Ion", "Densitas zat"], "jawaban": ["Atom", "Molekul", "Ion"], "pembahasan": "Menghitung jumlah partikel, bukan densitas/massa jenis."},
        {"tipe": "short_answer", "soal": "Rumus perbandingan atom paling sederhana dalam senyawa disebut rumus...", "opsi": [], "jawaban": "empiris", "pembahasan": "Rumus Empiris (RE)."},
        {"tipe": "mcq", "soal": "Kadar persen massa Karbon di CH4? (Ar C=12, H=1)", "opsi": ["A. 25%", "B. 50%", "C. 75%", "D. 80%"], "jawaban": "C. 75%", "pembahasan": "(12 / 16) x 100% = 75%."},
        {"tipe": "tf", "soal": "Partikel 1 mol O2 sama persis dengan 1 mol H2O.", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "1 mol = selalu 6.022 x 10^23 partikel (Bilangan Avogadro)."},
        {"tipe": "numeric", "soal": "Volume 10 mol gas CO2 di STP?", "opsi": [], "jawaban": 224, "pembahasan": "10 mol x 22.4 L/mol = 224 L."},
        {"tipe": "multiselect", "soal": "Variabel PV = nRT yang benar spesifikasinya:", "opsi": ["P = Tekanan (atm)", "V = Volume (L)", "T = Suhu Celcius", "R = Tetapan gas ideal"], "jawaban": ["P = Tekanan (atm)", "V = Volume (L)", "R = Tetapan gas ideal"], "pembahasan": "Suhu T harus dalam Kelvin mutlak, bukan Celcius."},
        {"tipe": "short_answer", "soal": "Massa 1 mol zat yang nilainya sama dengan Mr disebut massa...", "opsi": [], "jawaban": "molar", "pembahasan": "Molar Mass (gr/mol)."},
        {"tipe": "mcq", "soal": "2H2 + O2 -> 2H2O. 4 mol H2 campur 5 mol O2. Apa yang sisa?", "opsi": ["A. H2", "B. O2", "C. Keduanya habis", "D. H2O"], "jawaban": "B. O2", "pembahasan": "4 mol H2 hanya butuh 2 mol O2. Berarti O2 sisa 3 mol."},
        {"tipe": "tf", "soal": "Koefisien reaksi adalah perbandingan massa nyata dalam gram.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Itu perbandingan mol / volume gas, bukan perbandingan massa secara gram."},
        {"tipe": "numeric", "soal": "Massa atom N di 100 kg Urea CO(NH2)2 murni? (Mr=60, Ar N=14). (Bulatkan ke kg terdekat)", "opsi": [], "jawaban": 47, "pembahasan": "N ada 2 = 28. (28/60) x 100 = 46.67 (bulat 47)."},
        {"tipe": "multiselect", "soal": "Cari rumus molekul senyawa organik butuh data:", "opsi": ["Mr (Massa Molar)", "Rumus Empiris", "Warna zat"], "jawaban": ["Mr (Massa Molar)", "Rumus Empiris"], "pembahasan": "(Rumus Empiris)n = Massa Molar (Mr)."},
        {"tipe": "short_answer", "soal": "Pereaksi yang habis duluan disebut pereaksi...", "opsi": [], "jawaban": "pembatas", "pembahasan": "Membatasi jumlah produk yang dihasilkan."}
    ]
}

# --- 4. TAMPILAN HALAMAN UTAMA ---
if "kuis_aktif" not in st.session_state: 
    st.session_state.kuis_aktif = False

# Halaman Awal (Pilih Bab & Aturan)
if not st.session_state.kuis_aktif:
    st.markdown("<h1 style='text-align: center; color: white !important;'>🎓 Ujian CBT Kimia - Kelas 10</h1>", unsafe_allow_html=True)
    st.write("")
    
    with st.container(border=True):
        st.markdown("### 📜 Aturan Mengerjakan Ujian")
        st.info("""
        1. **Berdoalah** sebelum memulai ujian.
        2. Kuis ini berisi **20 soal HOTS** untuk setiap babnya.
        3. Terdapat berbagai tipe soal: Pilihan Ganda (1 jawaban), Multiselect (jawaban bisa lebih dari 1), True/False, Isian Singkat, dan Input Angka.
        4. Anda bisa kembali (Back) ke soal sebelumnya untuk mengecek jawaban.
        5. Nilai akhir dan pembahasan lengkap akan terbuka otomatis setelah Anda mengumpulkan ujian.
        """)
        
        st.markdown("---")
        st.markdown("### 📂 Silakan Pilih Bab Materi:")
        pilih_bab = st.selectbox("Daftar Materi Kimia K13:", list(DATABASE_SOAL.keys()), label_visibility="collapsed")
        
        st.write("")
        if st.button("Mulai Kerjakan Ujian 🚀", use_container_width=True):
            st.session_state.soal_siap = DATABASE_SOAL[pilih_bab]
            st.session_state.kuis_aktif = True
            st.session_state.indeks_soal = 0
            st.session_state.jawaban_user = {}
            st.rerun()

else:
    # --- 5. MESIN KUIS AKTIF ---
    daftar_soal = st.session_state.soal_siap
    idx = st.session_state.indeks_soal
    
    if idx < len(daftar_soal):
        curr = daftar_soal[idx]
        st.progress((idx)/len(daftar_soal), text=f"Sedang Mengerjakan: Soal {idx+1} dari {len(daftar_soal)}")
        
        with st.container(border=True):
            # Tampilkan Soal
            st.markdown(f"**Pertanyaan {idx+1}:**")
            st.write(curr["soal"])
            st.markdown("---")
            
            # Ambil jawaban lama jika user mundur (Kembali)
            jawaban_tersimpan = st.session_state.jawaban_user.get(idx)
            ans = None
            
            # Tampilkan Input sesuai Tipe Soal
            if curr["tipe"] in ["mcq", "tf"]:
                default_idx = curr["opsi"].index(jawaban_tersimpan) if jawaban_tersimpan in curr["opsi"] else None
                ans = st.radio("Pilih Opsi Terbaik:", curr["opsi"], key=f"q{idx}", index=default_idx)
            
            elif curr["tipe"] == "multiselect":
                default_vals = jawaban_tersimpan if isinstance(jawaban_tersimpan, list) else []
                ans = st.multiselect("Pilih SEMUA jawaban yang Benar:", curr["opsi"], key=f"q{idx}", default=default_vals)
            
            elif curr["tipe"] == "numeric":
                default_val = jawaban_tersimpan if jawaban_tersimpan is not None else 0
                ans = st.number_input("Ketik Jawaban (Angka Saja):", step=1, key=f"q{idx}", value=default_val)
            
            elif curr["tipe"] == "short_answer":
                default_val = jawaban_tersimpan if jawaban_tersimpan else ""
                ans = st.text_input("Ketik Kata Kunci Jawaban:", key=f"q{idx}", value=default_val)
            
            st.write("")
            
            # --- TOMBOL NAVIGASI (KEMBALI & LANJUT) ---
            col1, col2 = st.columns(2)
            
            # Tombol KEMBALI / BATAL
            with col1:
                if idx > 0:
                    if st.button("⏪ Kembali ke Soal Sebelumnya", use_container_width=True):
                        # Simpan jawaban sementara saat ini
                        if ans is not None and ans != "" and ans != []:
                            st.session_state.jawaban_user[idx] = ans
                        st.session_state.indeks_soal -= 1
                        st.rerun()
                else:
                    if st.button("🛑 Batalkan Ujian", use_container_width=True):
                        st.session_state.kuis_aktif = False
                        st.rerun()
            
            # Tombol SIMPAN & LANJUT
            with col2:
                teks_tombol = "Selesai & Kumpulkan 🏁" if idx == len(daftar_soal) - 1 else "Simpan & Lanjut ⏭️"
                if st.button(teks_tombol, use_container_width=True):
                    if ans is not None and ans != "" and ans != []:
                        st.session_state.jawaban_user[idx] = ans
                        st.session_state.indeks_soal += 1
                        st.rerun()
                    else:
                        st.error("⚠️ Anda wajib mengisi/memilih jawaban terlebih dahulu!")
                        
    else:
        # --- 6. HALAMAN HASIL & SKOR KUIS ---
        # Kalkulasi Skor
        skor_akhir = 0
        bobot = 100 / len(daftar_soal)
        
        for i, s in enumerate(daftar_soal):
            jwbn = st.session_state.jawaban_user.get(i)
            is_correct = False
            if jwbn is not None:
                if s["tipe"] in ["mcq", "tf", "numeric"]:
                    if str(jwbn).strip().lower() == str(s["jawaban"]).strip().lower(): is_correct = True
                elif s["tipe"] == "multiselect":
                    if isinstance(jwbn, list) and set(jwbn) == set(s["jawaban"]): is_correct = True
                elif s["tipe"] == "short_answer":
                    if str(jwbn).strip().lower() in str(s["jawaban"]).lower(): is_correct = True
            
            if is_correct: skor_akhir += bobot
            
        st.session_state.skor = skor_akhir

        # Menampilkan UI Hasil
        st.balloons()
        st.markdown("<h1 style='text-align: center; color: white !important;'>Ujian Telah Selesai!</h1>", unsafe_allow_html=True)
        
        with st.container(border=True):
            if st.session_state.skor >= 75: 
                st.success(f"### 🎉 Lulus! Skor Akhir Anda: {int(st.session_state.skor)}")
            else: 
                st.warning(f"### 📚 Remedial. Skor Akhir Anda: {int(st.session_state.skor)}")
            
            st.markdown("---")
            st.markdown("#### 📖 Ulasan & Pembahasan Lengkap")
            for i, s in enumerate(daftar_soal):
                jwbn = st.session_state.jawaban_user.get(i, "-")
                with st.expander(f"Soal {i+1} | Tipe: {s['tipe'].upper()}"):
                    st.write(s['soal'])
                    st.markdown(f"**Jawaban Anda:** `{jwbn}`")
                    st.markdown(f"**Kunci Standar:** `{s['jawaban']}`")
                    st.info(f"**Pembahasan:** {s['pembahasan']}")
                
        st.write("")        
        if st.button("Selesai & Kembali ke Menu Utama 🏠", use_container_width=True):
            st.session_state.kuis_aktif = False
            st.rerun()