import streamlit as st

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="CBT Kimia - Kelas 11", 
    page_icon="🌸", 
    layout="centered", 
    initial_sidebar_state="collapsed" 
)

# --- 2. TEMA "KERTAS" & GRADASI PINK-PUTIH ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #FFAFBD 0%, #ffc3a0 100%); }
    .block-container {
        background-color: #ffffff !important; border-radius: 20px !important;
        padding: 40px 30px !important; box-shadow: 0 10px 40px rgba(0,0,0,0.1) !important;
        margin-top: 40px !important; margin-bottom: 40px !important; max-width: 850px !important;
    }
    h1, h2, h3, p, span, li, label { color: #333333 !important; }
    div[data-testid="stAlert"] { background-color: #ffe4e6 !important; border: 1px solid #fbcfe8 !important; border-radius: 10px !important; }
    div[data-testid="stAlert"] p, div[data-testid="stAlert"] span { color: #be185d !important; }
    .stTextInput input, .stNumberInput input, div[data-baseweb="select"] > div {
        background-color: #fff0f6 !important; color: #4c0519 !important; border: 1px solid #fbcfe8 !important;
    }
    .stButton button { 
        background: linear-gradient(135deg, #fb7185 0%, #e11d48 100%) !important; 
        color: white !important; font-weight: bold !important; border-radius: 8px !important; border: none !important; transition: 0.3s;
    }
    .stButton button p { color: white !important; }
    .stButton button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(225, 29, 72, 0.4); }
    </style>
""", unsafe_allow_html=True)

# --- 3. DATABASE BANK SOAL KELAS 11 (BAB 1 - BAB 8) ---
DATABASE_SOAL = {
    "1. Senyawa Hidrokarbon": [
        {"tipe": "mcq", "soal": "Perhatikan gambar struktur garis (skeletal) di bawah ini. Nama IUPAC yang paling tepat untuk senyawa tersebut adalah...", "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/2-methylpentane-2D-skeletal.png/200px-2-methylpentane-2D-skeletal.png", "opsi": ["A. n-heksana", "B. 2-metilpentana", "C. 3-metilpentana", "D. 2,2-dimetilbutana"], "jawaban": "B. 2-metilpentana", "pembahasan": "Rantai terpanjang terdiri dari 5 atom C (pentana). Terdapat 1 cabang metil di atom C nomor 2."},
        {"tipe": "hotspot", "soal": "Sebuah senyawa hidrokarbon diuji kemampuannya mengalami oksidasi. Atom karbon *tersier* adalah yang paling reaktif. Manakah area yang menunjukkan Atom Karbon Tersier?", "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Isobutane-2D-flat.png/200px-Isobutane-2D-flat.png", "opsi": ["A. Atom C di ujung kiri", "B. Atom C di ujung kanan", "C. Atom C di tengah yang mengikat 3 atom C lain", "D. Atom C di cabang bawah"], "jawaban": "C. Atom C di tengah yang mengikat 3 atom C lain", "pembahasan": "Atom karbon tersier mengikat langsung 3 atom C lainnya."},
        {"tipe": "matching", "soal": "Pasangkan rumus molekul berikut dengan jenis homolog hidrokarbonnya yang tepat!", "kiri": ["C5H12", "C4H8 (Melingkar)", "C3H4"], "kanan": ["Alkana", "Sikloalkana", "Alkuna", "Alkena"], "jawaban": {"C5H12": "Alkana", "C4H8 (Melingkar)": "Sikloalkana", "C3H4": "Alkuna"}, "pembahasan": "CnH2n+2 = Alkana. CnH2n melingkar = Sikloalkana. CnH2n-2 = Alkuna."},
        {"tipe": "tf", "soal": "Ikatan rangkap dua pada alkena memiliki satu ikatan sigma (kuat) dan satu ikatan pi (lemah) yang mudah putus saat bereaksi.", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Ikatan pi sangat reaktif, membuat alkena mudah mengalami reaksi adisi."},
        {"tipe": "multiselect", "soal": "Reaksi 1-butena + HCl akan menghasilkan produk berdasarkan Aturan Markovnikov. Pilih penyataan yang tepat:", "opsi": ["H terikat ke C nomor 1", "Cl terikat ke C nomor 1", "H terikat ke C nomor 2", "Produk: 2-klorobutana", "Reaksi adisi"], "jawaban": ["H terikat ke C nomor 1", "Produk: 2-klorobutana", "Reaksi adisi"], "pembahasan": "H terikat pada C berikatan rangkap yang sudah memiliki lebih banyak atom H."},
        {"tipe": "short_answer", "soal": "Isomer struktur yang membedakan letak cabang pada rantai utama disebut isomer... (Ketik: rantai/posisi/fungsi)", "opsi": [], "jawaban": "rantai", "pembahasan": "Isomer rantai (rangka) membedakan bentuk rantai lurus dan bercabang."},
        {"tipe": "numeric", "soal": "Berapakah total isomer struktur untuk senyawa heksana (C6H14)?", "opsi": [], "jawaban": 5, "pembahasan": "1 lurus, 2 monosubstitusi metil, 2 disubstitusi dimetil = 5 isomer."},
        {"tipe": "mcq", "soal": "Gas X tak berwarna, diuji dengan air Bromin (Br2) kemerahan, warnanya langsung pudar. Gas X adalah...", "opsi": ["A. Metana", "B. Etana", "C. Etena", "D. Propana"], "jawaban": "C. Etena", "pembahasan": "Etena (alkena) mengalami adisi dengan Bromin memudarkan warnanya."},
        {"tipe": "tf", "soal": "Semua senyawa sikloalkana memiliki rumus molekul yang sama dengan Alkena (CnH2n).", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Sikloalkana dan Alkena saling berisomer fungsi dengan rumus umum CnH2n."},
        {"tipe": "multiselect", "soal": "Syarat mutlak suatu senyawa dapat memiliki isomer geometri (cis-trans):", "opsi": ["Harus memiliki ikatan rangkap dua", "C rangkap harus mengikat 2 gugus yang SAMA", "C rangkap harus mengikat 2 gugus yang BEDA", "Bisa berotasi bebas"], "jawaban": ["Harus memiliki ikatan rangkap dua", "C rangkap harus mengikat 2 gugus yang BEDA"], "pembahasan": "Ikatan C=C kaku, dan tiap ujungnya harus mengikat gugus berbeda."},
        {"tipe": "mcq", "soal": "Zaitsev rule memprediksi produk mayor dari dehidrasi alkohol. Dehidrasi 2-butanol menghasilkan utama...", "opsi": ["A. 1-butena", "B. 2-butena", "C. isobutena", "D. butana"], "jawaban": "B. 2-butena", "pembahasan": "Ikatan rangkap terbentuk pada karbon yang lebih tersubstitusi alkil."},
        {"tipe": "short_answer", "soal": "Kekhasan atom karbon yang bisa membentuk rantai karbon panjang disebut... (Ketik: katenasi)", "opsi": [], "jawaban": "katenasi", "pembahasan": "Katenasi adalah kemampuan membentuk rantai."},
        {"tipe": "matching", "soal": "Pasangkan tipe reaksi hidrokarbon dengan ciri utamanya!", "kiri": ["Substitusi", "Adisi", "Eliminasi"], "kanan": ["Penggantian atom (Alkana)", "Pemutusan ikatan rangkap", "Pembentukan ikatan rangkap"], "jawaban": {"Substitusi": "Penggantian atom (Alkana)", "Adisi": "Pemutusan ikatan rangkap", "Eliminasi": "Pembentukan ikatan rangkap"}, "pembahasan": "Substitusi (tukar), Adisi (tambah), Eliminasi (kurang)."},
        {"tipe": "numeric", "soal": "Pada pembakaran sempurna 1 mol propana (C3H8), dibutuhkan gas oksigen (O2) sebanyak... mol.", "opsi": [], "jawaban": 5, "pembahasan": "C3H8 + 5 O2 -> 3 CO2 + 4 H2O."},
        {"tipe": "mcq", "soal": "Senyawa hidrokarbon berikut yang memiliki titik didih PALING RENDAH (paling volatil) adalah...", "opsi": ["A. n-pentana", "B. 2-metilbutana", "C. 2,2-dimetilpropana", "D. n-heksana"], "jawaban": "C. 2,2-dimetilpropana", "pembahasan": "Semakin banyak cabang, gaya London makin lemah, titik didih makin rendah."},
        {"tipe": "tf", "soal": "Pembakaran tidak sempurna pada mesin bensin selalu menghasilkan gas CO2 sebagai satu-satunya residu karbon.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Menghasilkan gas CO dan partikel padat C (jelaga)."},
        {"tipe": "multiselect", "soal": "Nama IUPAC yang SALAH dan perlu dikoreksi:", "opsi": ["2-etilbutana", "2,2-dimetilpropana", "3-propilheksana", "1-butuna"], "jawaban": ["2-etilbutana", "3-propilheksana"], "pembahasan": "Rantai harus terpanjang. 2-etilbutana salah, harusnya 3-metilpentana."},
        {"tipe": "short_answer", "soal": "Alkana adalah hidrokarbon jenuh, alkena/alkuna adalah hidrokarbon tak... (Ketik satu kata)", "opsi": [], "jawaban": "jenuh", "pembahasan": "Tak jenuh (punya ikatan rangkap)."},
        {"tipe": "mcq", "soal": "Reaksi: C2H6 + Cl2 -> C2H5Cl + HCl adalah contoh reaksi...", "opsi": ["A. Adisi", "B. Eliminasi", "C. Substitusi", "D. Polimerisasi"], "jawaban": "C. Substitusi", "pembahasan": "Atom H digantikan oleh atom Cl."},
        {"tipe": "numeric", "soal": "Berapakah jumlah ikatan pi (π) pada senyawa gas karbit (Asetilena, C2H2)?", "opsi": [], "jawaban": 2, "pembahasan": "Ikatan rangkap 3 = 1 sigma + 2 pi."}
    ],
    "2. Minyak Bumi & Dampak": [
        {"tipe": "hotspot", "soal": "Fraksi yang keluar dari Pipa C (Bagian tengah menara C11-C14) adalah...", "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Crude_Oil_Distillation-fr.svg/300px-Crude_Oil_Distillation-fr.svg.png", "opsi": ["A. Gas LPG", "B. Bensin (Gasoline)", "C. Kerosin (Minyak Tanah) / Avtur", "D. Aspal"], "jawaban": "C. Kerosin (Minyak Tanah) / Avtur", "pembahasan": "Paling atas (gas), bawahnya (Bensin), tengah (Kerosin), bawah (Aspal)."},
        {"tipe": "mcq", "soal": "Prinsip utama pemisahan minyak mentah pada menara distilasi didasarkan pada perbedaan...", "opsi": ["A. Titik leleh", "B. Titik didih", "C. Massa jenis", "D. Kelarutan"], "jawaban": "B. Titik didih", "pembahasan": "Distilasi memisahkan berdasar titik didih."},
        {"tipe": "matching", "soal": "Pasangkan fraksi dengan kegunaannya!", "kiri": ["Bensin (Oktan 92)", "Kerosin murni", "Residu Padat (>C25)"], "kanan": ["Bahan bakar kendaraan", "Bahan bakar pesawat jet", "Pelapis jalan (Aspal)"], "jawaban": {"Bensin (Oktan 92)": "Bahan bakar kendaraan", "Kerosin murni": "Bahan bakar pesawat jet", "Residu Padat (>C25)": "Pelapis jalan (Aspal)"}, "pembahasan": "Kerosin murni diolah jadi avtur untuk pesawat terbang."},
        {"tipe": "tf", "soal": "Angka oktan mengukur kemampuan bensin menahan tekanan mesin tanpa mengalami detonasi dini (knocking).", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Oktan tinggi = mesin tidak ngelitik."},
        {"tipe": "multiselect", "soal": "Zat aditif bensin yang ramah lingkungan penambah oktan:", "opsi": ["TEL (Timbal)", "MTBE", "Bio-Etanol", "Residu merkuri"], "jawaban": ["MTBE", "Bio-Etanol"], "pembahasan": "TEL dilarang karena beracun."},
        {"tipe": "short_answer", "soal": "Komposisi standar untuk angka oktan 100 adalah... (Ketik: isooktana)", "opsi": [], "jawaban": "isooktana", "pembahasan": "Isooktana (100) dan n-heptana (0)."},
        {"tipe": "numeric", "soal": "Bensin setara dengan 80% isooktana dan 20% n-heptana, nilai oktannya?", "opsi": [], "jawaban": 80, "pembahasan": "Angka oktan sesuai persen isooktana."},
        {"tipe": "mcq", "soal": "Gas hasil bakar Belerang (S) di knalpot menyebabkan...", "opsi": ["A. Penipisan Ozon", "B. Hujan Asam", "C. Eutrofikasi", "D. Efek Rumah Kaca"], "jawaban": "B. Hujan Asam", "pembahasan": "SO2 menjadi H2SO4 (hujan asam)."},
        {"tipe": "tf", "soal": "Proses mengubah molekul lurus jadi bercabang di kilang disebut Reforming.", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Reforming menaikkan oktan."},
        {"tipe": "multiselect", "soal": "Polutan udara hasil pembakaran mesin mobil (knalpot):", "opsi": ["CO", "NOx", "O3", "Pb (zaman dulu)"], "jawaban": ["CO", "NOx", "Pb (zaman dulu)"], "pembahasan": "O3 (Ozon) tidak dihasilkan mesin."},
        {"tipe": "short_answer", "soal": "Pembusukan minyak bumi purba terjadi tanpa oksigen, disebut kondisi... (Ketik: anaerob)", "opsi": [], "jawaban": "anaerob", "pembahasan": "Hampa oksigen."},
        {"tipe": "numeric", "soal": "Suhu Cracking Termal minyak berat mencapai... Derajat Celcius (Ketik 500)", "opsi": [], "jawaban": 500, "pembahasan": "Suhu ekstrem 500-700 C."},
        {"tipe": "mcq", "soal": "Gas rumah kaca penyelimut bumi akibat pembakaran sempurna bahan bakar fosil adalah...", "opsi": ["A. Karbon monoksida", "B. Karbon dioksida (CO2)", "C. Oksigen", "D. SO2"], "jawaban": "B. Karbon dioksida (CO2)", "pembahasan": "CO2 gas rumah kaca paling utama."},
        {"tipe": "tf", "soal": "Catalytic converter knalpot mengubah gas CO dan NO menjadi CO2 dan N2.", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Katalis menetralkan emisi gas beracun."},
        {"tipe": "multiselect", "soal": "Bahan Petrokimia (turunan minyak bumi):", "opsi": ["Plastik", "Deterjen", "Kayu murni", "Obat aspirin", "Kain katun"], "jawaban": ["Plastik", "Deterjen", "Obat aspirin"], "pembahasan": "Kayu dan katun alami dari selulosa."},
        {"tipe": "short_answer", "soal": "Gas bumi yang dicairkan untuk dapur disingkat... (3 huruf)", "opsi": [], "jawaban": "lpg", "pembahasan": "Liquefied Petroleum Gas."},
        {"tipe": "mcq", "soal": "Mengapa bensin oktan rendah ngelitik (knocking)?", "opsi": ["A. Bensin kental", "B. Bensin beku", "C. Terbakar sendiri karena tekanan sebelum busi nyala", "D. Tabrakan klep"], "jawaban": "C. Terbakar sendiri karena tekanan sebelum busi nyala", "pembahasan": "Oktan rendah rentan detonasi otomatis."},
        {"tipe": "tf", "soal": "Suhu paling panas di menara distilasi ada di paling atas.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Suhu paling panas di dasar/bawah."},
        {"tipe": "matching", "soal": "Pasangkan polutan dengan dampaknya!", "kiri": ["Gas CO", "Gas SO2 / SO3", "Gas CO2"], "kanan": ["Hujan Asam", "Pemanasan Global", "Keracunan hemoglobin"], "jawaban": {"Gas CO": "Keracunan hemoglobin", "Gas SO2 / SO3": "Hujan Asam", "Gas CO2": "Pemanasan Global"}, "pembahasan": "CO sangat beracun bagi pernapasan."},
        {"tipe": "numeric", "soal": "Persen isooktana pada bensin Oktan 98?", "opsi": [], "jawaban": 98, "pembahasan": "Sesuai angka oktannya."}
    ],
    "3. Termokimia": [
        {"tipe": "hotspot", "soal": "Bagian kurva yang merepresentasikan Energi Aktivasi (Ea) adalah...", "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Activation_energy.svg/300px-Activation_energy.svg.png", "opsi": ["A. Jarak sumbu X ke reaktan", "B. Jarak reaktan ke puncak kurva", "C. Jarak produk ke puncak", "D. Selisih reaktan produk"], "jawaban": "B. Jarak reaktan ke puncak kurva", "pembahasan": "Ea adalah 'bukit' rintangan yang harus dilompati reaktan."},
        {"tipe": "mcq", "soal": "Dinding beker terasa dingin. Pernyataan yang benar:", "opsi": ["A. Eksoterm, sistem menyerap kalor", "B. Endoterm, sistem melepas kalor", "C. Endoterm, sistem menyerap kalor lingkungan", "D. Eksoterm, sistem melepas kalor"], "jawaban": "C. Endoterm, sistem menyerap kalor lingkungan", "pembahasan": "Suhu sekitar turun karena diserap sistem (Endoterm)."},
        {"tipe": "matching", "soal": "Pasangkan notasi Entalpi:", "kiri": ["ΔH°f", "ΔH°c", "ΔH°d"], "kanan": ["Pembakaran 1 mol", "Penguraian 1 mol", "Pembentukan 1 mol"], "jawaban": {"ΔH°f": "Pembentukan 1 mol", "ΔH°c": "Pembakaran 1 mol", "ΔH°d": "Penguraian 1 mol"}, "pembahasan": "f=formation, c=combustion, d=dissociation."},
        {"tipe": "tf", "soal": "Hukum Hess: ΔH hanya bergantung pada keadaan awal dan akhir, bukan jalannya reaksi.", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Pernyataan Hukum Hess."},
        {"tipe": "numeric", "soal": "ΔHf CO2=-394, H2O=-286, CH4=-75. ΔHc pembakaran CH4? (Ketik angkanya: -891)", "opsi": [], "jawaban": -891, "pembahasan": "Kanan - Kiri = (-394 + -572) - (-75) = -891 kJ/mol."},
        {"tipe": "multiselect", "soal": "Karakteristik Reaksi Eksoterm:", "opsi": ["Suhu lingkungan naik", "Suhu lingkungan turun", "ΔH negatif", "Energi produk > reaktan", "Sistem melepas kalor"], "jawaban": ["Suhu lingkungan naik", "ΔH negatif", "Sistem melepas kalor"], "pembahasan": "Melepas kalor, suhu naik, ΔH negatif."},
        {"tipe": "short_answer", "soal": "Alat ukur kalor terisolasi di lab disebut...", "opsi": [], "jawaban": "kalorimeter", "pembahasan": "Kalorimeter (contoh: Bom kalorimeter)."},
        {"tipe": "mcq", "soal": "Energi ikatan: C-H=413, Cl-Cl=242, C-Cl=328, H-Cl=431. Entalpi CH4+Cl2 -> CH3Cl+HCl adalah...", "opsi": ["A. -104", "B. +104", "C. -208", "D. +208"], "jawaban": "A. -104", "pembahasan": "Putus - Bentuk = (413+242) - (328+431) = -104 kJ/mol."},
        {"tipe": "tf", "soal": "Wujud zat (s,l,g) mengubah nilai perubahan entalpi.", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Karena butuh kalor laten tambahan untuk mengubah wujud zat."},
        {"tipe": "numeric", "soal": "Jika A -> B (ΔH = -50). Berapa ΔH untuk 2B -> 2A?", "opsi": [], "jawaban": 100, "pembahasan": "Dibalik jadi positif, dikali 2 = +100."},
        {"tipe": "multiselect", "soal": "Contoh aplikasi eksoterm:", "opsi": ["Fotosintesis", "Pembakaran kayu", "Pencairan es", "Pengelasan termit", "Respirasi seluler"], "jawaban": ["Pembakaran kayu", "Pengelasan termit", "Respirasi seluler"], "pembahasan": "Semuanya menghasilkan panas/energi ke lingkungan."},
        {"tipe": "mcq", "soal": "Cold pack dipukul jadi sangat dingin. Reaksinya:", "opsi": ["A. Endoterm, entalpi (H) sistem bertambah", "B. Eksoterm, entalpi sistem berkurang", "C. Endoterm Ea nol", "D. Eksoterm spontan"], "jawaban": "A. Endoterm, entalpi (H) sistem bertambah", "pembahasan": "Kalor masuk ke sistem, jadi Entalpi sistem (H) membesar."},
        {"tipe": "tf", "soal": "Kalor netralisasi asam kuat basa kuat selalu eksotermik (-).", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Menghasilkan molekul air dan melepas panas."},
        {"tipe": "short_answer", "soal": "Termos air panas adalah sistem...", "opsi": [], "jawaban": "terisolasi", "pembahasan": "Tidak ada pertukaran materi maupun energi."},
        {"tipe": "numeric", "soal": "m=100g, c=4.2, ΔT=5. Q lepas berapa Joule?", "opsi": [], "jawaban": 2100, "pembahasan": "Q = m x c x ΔT = 100 x 4.2 x 5 = 2100 J."},
        {"tipe": "mcq", "soal": "Entalpi standar ΔH°f unsur bebas (O2, N2, Fe) bernilai...", "opsi": ["A. >0", "B. <0", "C. Tak hingga", "D. 0"], "jawaban": "D. 0", "pembahasan": "Kesepakatan baku termodinamika."},
        {"tipe": "tf", "soal": "Energi pemutusan ikatan bersifat endotermik.", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Memutus ikatan yang stabil selalu BUTUH energi."},
        {"tipe": "multiselect", "soal": "Pernyataan Energi Ikatan Rata-rata:", "opsi": ["Diukur wujud gas", "Ikatan pendek = energi besar", "Rangkap 3 lemah", "Energi rata rata putus 1 mol ikatan"], "jawaban": ["Diukur wujud gas", "Ikatan pendek = energi besar", "Energi rata rata putus 1 mol ikatan"], "pembahasan": "Rangkap 3 justru paling kuat dan panjangnya terpendek."},
        {"tipe": "short_answer", "soal": "Kurva profil energi panah ke bawah (produk lebih rendah) adalah reaksi... (Ketik eksoterm)", "opsi": [], "jawaban": "eksoterm", "pembahasan": "Eksoterm (H menurun)."},
        {"tipe": "numeric", "soal": "H2+1/2O2 -> H2O (ΔH = -285 kJ/mol). Kalor bebas dari 2 gram H2 (1 mol)?", "opsi": [], "jawaban": 285, "pembahasan": "1 mol H2 melepas 285 kJ kalor (jangan ketik min, karena ditanya kalor bebas)."}
    ],
    "4. Laju Reaksi": [
        {"tipe": "hotspot", "soal": "Syarat tumbukan molekul efektif selain energi yang cukup adalah...", "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Collision_theory.png/300px-Collision_theory.png", "opsi": ["A. Tidak mengenai inti", "B. Orientasi / Arah tumbukan tepat", "C. Suhu >100", "D. Massa bertambah"], "jawaban": "B. Orientasi / Arah tumbukan tepat", "pembahasan": "Orientasi ruang molekul harus pas di sisi yang reaktif."},
        {"tipe": "mcq", "soal": "Mekanisme kerja katalis adalah...", "opsi": ["A. Naikkan energi kinetik", "B. Ubah jadi eksoterm", "C. Jalur alternatif dengan Ea lebih rendah", "D. Perbesar luas permukaan"], "jawaban": "C. Jalur alternatif dengan Ea lebih rendah", "pembahasan": "Menurunkan hambatan (Ea) agar tumbukan lebih gampang sukses."},
        {"tipe": "matching", "soal": "Pasangkan fenomena dengan faktor penentunya!", "kiri": ["Mengunyah makanan halus", "Simpan daging di freezer", "Tiup arang dengan kipas"], "kanan": ["Suhu", "Luas Permukaan", "Konsentrasi"], "jawaban": {"Mengunyah makanan halus": "Luas Permukaan", "Simpan daging di freezer": "Suhu", "Tiup arang dengan kipas": "Konsentrasi"}, "pembahasan": "Luas permukaan, penurunan suhu hambat reaksi, tambahan kadar O2."},
        {"tipe": "numeric", "soal": "Laju naik 2x tiap 10C. Berapa kali lebih cepat pada 50C dibanding 20C?", "opsi": [], "jawaban": 8, "pembahasan": "Beda suhu 30C (3 interval). 2^3 = 8 kali."},
        {"tipe": "multiselect", "soal": "Dari persamaan v = k [A]^2 [B] :", "opsi": ["Orde total 3", "Laju bergantung produk", "Konsentrasi A di-2-kan, laju jadi 4x", "Katalis ubah [B]"], "jawaban": ["Orde total 3", "Konsentrasi A di-2-kan, laju jadi 4x"], "pembahasan": "Katalis mengubah k, bukan [B]."},
        {"tipe": "tf", "soal": "Suhu menaikkan laju karena suhu menurunkan Ea.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Suhu TIDAK menurunkan Ea. Suhu menaikkan Energi Kinetik Molekul."},
        {"tipe": "short_answer", "soal": "Bentuk padat dengan reaksi paling cepat adalah... (Ketik: serbuk)", "opsi": [], "jawaban": "serbuk", "pembahasan": "Serbuk punya luas sentuh mikroskopis terbesar."},
        {"tipe": "mcq", "soal": "Orde reaktan X = 0. Artinya...", "opsi": ["A. X tak dibutuhkan", "B. Konsentrasi X tidak mengubah laju", "C. X menguap", "D. Laju instan"], "jawaban": "B. Konsentrasi X tidak mengubah laju", "pembahasan": "Sesuatu dipangkat 0 = 1 (konstan)."},
        {"tipe": "tf", "soal": "Satuan Laju Reaksi (v) adalah M/s.", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Konsentrasi dibagi waktu (Molar per sekon)."},
        {"tipe": "numeric", "soal": "[A] naik 2x, [B] tetap, laju naik 4x. Orde zat A?", "opsi": [], "jawaban": 2, "pembahasan": "2^x = 4 -> x = 2."},
        {"tipe": "multiselect", "soal": "Sifat Biokatalisator (Enzim):", "opsi": ["Bisa dipakai berulang", "Bekerja di sembarang suhu (hingga 100C)", "Sangat spesifik", "Turunkan Ea"], "jawaban": ["Bisa dipakai berulang", "Sangat spesifik", "Turunkan Ea"], "pembahasan": "Enzim mati/denaturasi di suhu tinggi."},
        {"tipe": "short_answer", "soal": "Mol per Liter zat yang menempati ruang disebut... (Ketik konsentrasi)", "opsi": [], "jawaban": "konsentrasi", "pembahasan": "Kerapatan molekul / konsentrasi."},
        {"tipe": "mcq", "soal": "Grafik konsentrasi Reaktan terhadap waktu:", "opsi": ["A. Linier naik", "B. Eksponensial menurun mendatar", "C. Datar horizontal", "D. Sinusoidal"], "jawaban": "B. Eksponensial menurun mendatar", "pembahasan": "Reaktan makin lama makin habis secara kurva melandai."},
        {"tipe": "tf", "soal": "Tetapan k adalah mutlak konstan tak bisa diubah apapun.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "k akan berubah jika Suhu / Katalis diubah."},
        {"tipe": "numeric", "soal": "100g gula (Mr=342) di 500 mL air. Molaritas kasarnya (2 desimal)?", "opsi": [], "jawaban": 0.58, "pembahasan": "(100/342)/0.5 = 0.29/0.5 = 0.58 M."},
        {"tipe": "multiselect", "soal": "Faktor mempercepat korosi besi (konsep kinetika):", "opsi": ["Kelembapan tinggi", "Larutan garam/asam", "Cat / minyak", "Suhu tinggi"], "jawaban": ["Kelembapan tinggi", "Larutan garam/asam", "Suhu tinggi"], "pembahasan": "Cat justru menghambat/mencegah kontak."},
        {"tipe": "mcq", "soal": "Variabel bebas menguji Luas Permukaan pada pelarutan CaCO3 adalah...", "opsi": ["A. Suhu HCl dipanaskan/tidak", "B. CaCO3 kepingan vs serbuk", "C. HCl 1M vs 2M", "D. Massa 5g vs 10g"], "jawaban": "B. CaCO3 kepingan vs serbuk", "pembahasan": "Luas permukaan = Bentuk wujud padatan."},
        {"tipe": "short_answer", "soal": "Teori reaksi akibat tabrakan partikel disebut Teori... (Ketik tumbukan)", "opsi": [], "jawaban": "tumbukan", "pembahasan": "Collision Theory."},
        {"tipe": "tf", "soal": "Orde reaksi selalu persis sama dengan koefisien reaksi.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Orde HANYA bisa dicari via eksperimen data lab."},
        {"tipe": "mcq", "soal": "Satuan k jika orde total = 1 ?", "opsi": ["A. M s^-1", "B. s^-1", "C. M^-1 s^-1", "D. M^-2 s^-1"], "jawaban": "B. s^-1", "pembahasan": "v(M/s) = k * [A](M). Maka k = 1/s."}
    ],
    "5. Kesetimbangan Kimia": [
        {"tipe": "hotspot", "soal": "Kapan Kesetimbangan Dinamis tercapai pada kurva laju (v) vs waktu (t)?", "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Chemical_equilibrium_rate_graph.svg/300px-Chemical_equilibrium_rate_graph.svg.png", "opsi": ["A. Kurva v1 dipuncak", "B. Kurva v2 baru naik", "C. Kedua kurva menyatu jadi horizontal", "D. Kurva menyentuh nol"], "jawaban": "C. Kedua kurva menyatu jadi horizontal", "pembahasan": "Kesetimbangan tercapai saat Laju Maju (v1) = Laju Balik (v2)."},
        {"tipe": "mcq", "soal": "N2 + 3H2 ⇌ 2NH3 (ΔH=-92 kJ). Maksimalkan NH3 di industri:", "opsi": ["A. Perbesar volume, naikkan suhu", "B. Turunkan tekanan dan suhu", "C. Perbesar tekanan, turunkan suhu, ambil NH3", "D. Katalis dan suhu sangat tinggi"], "jawaban": "C. Perbesar tekanan, turunkan suhu, ambil NH3", "pembahasan": "Tekanan naik ke mol kecil (kanan). Suhu turun ke eksoterm (kanan)."},
        {"tipe": "tf", "soal": "Katalis menggeser kesetimbangan ke arah produk (yield bertambah).", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Katalis HANYA mempercepat tercapainya setimbang, jumlah produk tetap."},
        {"tipe": "multiselect", "soal": "CaCO3(s) ⇌ CaO(s) + CO2(g). Faktor penggeser kesetimbangan:", "opsi": ["Tambah CaCO3 padat", "Perbesar volume", "Turunkan tekanan", "Tambah CaO padat"], "jawaban": ["Perbesar volume", "Turunkan tekanan"], "pembahasan": "Fase (s) / Padat tidak menggeser arah reaksi."},
        {"tipe": "matching", "soal": "Asas Le Chatelier:", "kiri": ["Konsentrasi reaktan ditambah", "Tekanan diperbesar", "Suhu sistem dinaikkan"], "kanan": ["Bergeser ke endoterm", "Bergeser ke mol gas kecil", "Bergeser ke produk (kanan)"], "jawaban": {"Konsentrasi reaktan ditambah": "Bergeser ke produk (kanan)", "Tekanan diperbesar": "Bergeser ke mol gas kecil", "Suhu sistem dinaikkan": "Bergeser ke endoterm"}, "pembahasan": "Sistem selalu merespon untuk 'melawan' gangguan."},
        {"tipe": "numeric", "soal": "2A ⇌ B + C (wadah 1L). Setimbang: A=0.1, B=0.2, C=0.2. Nilai Kc?", "opsi": [], "jawaban": 4, "pembahasan": "(0.2 * 0.2) / (0.1)^2 = 0.04 / 0.01 = 4."},
        {"tipe": "short_answer", "soal": "Reaksi makroskopis stop, mikroskopis tetap jalan adalah kesetimbangan... (Ketik dinamis)", "opsi": [], "jawaban": "dinamis", "pembahasan": "Partikel terus bereaksi maju-balik sama cepat."},
        {"tipe": "mcq", "soal": "H2(g) + I2(g) ⇌ 2HI(g). Hubungan Kp dan Kc?", "opsi": ["A. Kp > Kc", "B. Kp < Kc", "C. Kp = Kc", "D. Tak tentu"], "jawaban": "C. Kp = Kc", "pembahasan": "Δn = mol gas kanan - kiri = 2 - 2 = 0. Kp = Kc(RT)^0 = Kc."},
        {"tipe": "tf", "soal": "Nilai tetapan K akan berubah jika konsentrasi reaktan diubah di suhu konstan.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "K HANYA BISA BERUBAH OLEH PERUBAHAN SUHU."},
        {"tipe": "numeric", "soal": "1 mol N2O4 terurai 60%. Derajat Disosiasi (Desimal)?", "opsi": [], "jawaban": 0.6, "pembahasan": "60% = 60/100 = 0.6."},
        {"tipe": "multiselect", "soal": "Kesetimbangan Heterogen (lebih dari 1 wujud):", "opsi": ["N2(g) + 3H2(g) ⇌ 2NH3(g)", "C(s) + H2O(g) ⇌ CO(g) + H2(g)", "H2O(l) ⇌ H2O(g)", "CH3COOH(aq) ⇌ H+(aq) + CH3COO-(aq)"], "jawaban": ["C(s) + H2O(g) ⇌ CO(g) + H2(g)", "H2O(l) ⇌ H2O(g)"], "pembahasan": "Campuran padat-gas dan cair-gas."},
        {"tipe": "short_answer", "soal": "Reaksi industri amonia adalah proses... (Ketik haber-bosch)", "opsi": [], "jawaban": "haber-bosch", "pembahasan": "Proses esensial pabrik pupuk dunia."},
        {"tipe": "mcq", "soal": "Suhu 30C Kc=10. Suhu 60C Kc=50. Reaksi maju (kanan) bersifat...", "opsi": ["A. Eksoterm", "B. Endoterm", "C. Katalitik", "D. Reversibel Murni"], "jawaban": "B. Endoterm", "pembahasan": "Suhu naik -> Kc naik (geser kanan). Berarti kanan adalah area Endoterm (menyerap panas)."},
        {"tipe": "tf", "soal": "Menambah gas inert (Helium) ke wadah volume tetap menggeser arah kesetimbangan.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Tekanan total naik, tapi tekanan parsial reaktan tidak berubah."},
        {"tipe": "mcq", "soal": "2NO2 (cokelat) ⇌ N2O4 (bening) ΔH = -58. Didinginkan (es), yang terlihat?", "opsi": ["A. Makin cokelat", "B. Warna cokelat pudar (bening)", "C. Endapan putih", "D. Kaca pecah"], "jawaban": "B. Warna cokelat pudar (bening)", "pembahasan": "Didinginkan -> geser ke eksoterm (kanan / bening)."},
        {"tipe": "multiselect", "soal": "Qc > Kc. Evaluasi sistem:", "opsi": ["Sudah setimbang", "Belum setimbang", "Bergeser ke kiri (reaktan)", "Bergeser ke kanan (produk)"], "jawaban": ["Belum setimbang", "Bergeser ke kiri (reaktan)"], "pembahasan": "Produk kelebihan, dibuang ke kiri sampai Qc=Kc."},
        {"tipe": "short_answer", "soal": "Padat (s) dan cair (l) tak masuk rumus Kc karena konsentrasinya... (Ketik tetap)", "opsi": [], "jawaban": "tetap", "pembahasan": "Konstan dan dimasukkan ke dalam tetapan Kc."},
        {"tipe": "numeric", "soal": "A ⇌ B (Kc = 2). Maka Kc untuk 2B ⇌ 2A ?", "opsi": [], "jawaban": 0.25, "pembahasan": "Dibalik (1/2 = 0.5). Dikali 2 (Dikuadratkan -> 0.5^2 = 0.25)."},
        {"tipe": "mcq", "soal": "Proses Kontak (SO3), kenapa tak pakai tekanan ekstrem padahal menaikkan yield?", "opsi": ["A. SO3 jadi padat", "B. Jadi ozon", "C. Konversi tekanan normal sudah 98%, tekanan ekstrem sangat boros biaya alat", "D. Berubah endoterm"], "jawaban": "C. Konversi tekanan normal sudah 98%, tekanan ekstrem sangat boros biaya alat", "pembahasan": "Cost-benefit industri di dunia nyata."}
    ],
    "6. Asam dan Basa": [
        {"tipe": "mcq", "soal": "Asam adalah 'Zat pendonor proton' dan Basa adalah 'akseptor proton'. Ini Teori...", "opsi": ["A. Arrhenius", "B. Brønsted-Lowry", "C. Lewis", "D. Sorensen"], "jawaban": "B. Brønsted-Lowry", "pembahasan": "Teori Transfer Proton."},
        {"tipe": "hotspot", "soal": "Lemon, Cuka, Air Aki di skala indikator universal ada di area...", "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/PH_Scale.svg/400px-PH_Scale.svg.png", "opsi": ["A. Merah-Kuning (pH 0-6)", "B. Hijau (pH 7)", "C. Biru-Ungu (pH 8-14)"], "jawaban": "A. Merah-Kuning (pH 0-6)", "pembahasan": "Ketiganya asam (pH < 7)."},
        {"tipe": "tf", "soal": "pH air murni SELALU tepat 7.00 di suhu berapapun.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "7.00 hanya di suhu standar 25 C. Suhu naik = pH netral < 7."},
        {"tipe": "multiselect", "soal": "Pasangan Konjugasi dari NH3 + H2O ⇌ NH4+ + OH-", "opsi": ["NH3 dan NH4+", "H2O dan OH-", "NH3 dan H2O", "NH4+ dan OH-"], "jawaban": ["NH3 dan NH4+", "H2O dan OH-"], "pembahasan": "Pasangan asam-basa konjugasi mirip selisih 1 ion H+."},
        {"tipe": "matching", "soal": "Trayek pH & Perubahan Warna Indikator", "kiri": ["PP (8.3 - 10.0)", "MM (4.4 - 6.2)", "BTB (6.0 - 7.6)"], "kanan": ["Tak Warna - Pink", "Merah - Kuning", "Kuning - Biru"], "jawaban": {"PP (8.3 - 10.0)": "Tak Warna - Pink", "MM (4.4 - 6.2)": "Merah - Kuning", "BTB (6.0 - 7.6)": "Kuning - Biru"}, "pembahasan": "Identifikasi visual uji asam basa."},
        {"tipe": "numeric", "soal": "pH dari HCl 0.01 M ?", "opsi": [], "jawaban": 2, "pembahasan": "[H+] = 10^-2. pH = 2."},
        {"tipe": "short_answer", "soal": "Zat yang bisa jadi asam maupun basa (bergantung lawan) disebut zat... (Ketik amfoter)", "opsi": [], "jawaban": "amfoter", "pembahasan": "Atau amfiprotik. Contohnya air H2O."},
        {"tipe": "mcq", "soal": "BF3 bertindak sebagai asam saat reaksi dengan NH3 karena...", "opsi": ["A. Mendonor proton", "B. Menerima PEB (Pasangan Elektron Bebas) dari NH3", "C. Melepas H+", "D. Lakmus merah jadi biru"], "jawaban": "B. Menerima PEB (Pasangan Elektron Bebas) dari NH3", "pembahasan": "Konsep Asam Lewis = Akseptor PEB."},
        {"tipe": "tf", "soal": "Semakin besar nilai Ka, makin kuat sifat asamnya.", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Makin mudah melepas ion H+ di air."},
        {"tipe": "numeric", "soal": "pH NaOH 0.001 M ?", "opsi": [], "jawaban": 11, "pembahasan": "pOH = 3. pH = 14-3 = 11."},
        {"tipe": "multiselect", "soal": "Kelompok Asam Kuat murni:", "opsi": ["HCl", "CH3COOH", "H2SO4", "HNO3", "HF"], "jawaban": ["HCl", "H2SO4", "HNO3"], "pembahasan": "Cuka dan HF adalah asam lemah."},
        {"tipe": "mcq", "soal": "Asam asetat 0.1 M diencerkan 10x lipat air. Derajat ionisasi (α)?", "opsi": ["A. Menurun", "B. Meningkat (Ostwald)", "C. Konstan", "D. Basa"], "jawaban": "B. Meningkat (Ostwald)", "pembahasan": "Hukum pengenceran Ostwald: larutan lemah makin encer makin terionisasi."},
        {"tipe": "short_answer", "soal": "Netralisasi selalu hasilkan Air dan... (Ketik garam)", "opsi": [], "jawaban": "garam", "pembahasan": "Asam + Basa -> Garam + Air."},
        {"tipe": "numeric", "soal": "pH Asam Lemah CH3COOH 0.1 M (Ka = 10^-5)?", "opsi": [], "jawaban": 3, "pembahasan": "[H+] = akar(10^-5 * 0.1) = 10^-3. pH = 3."},
        {"tipe": "tf", "soal": "Campur mol sama Kuat-Kuat selalu pH 7 netral.", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Garam kuat tidak terhidrolisis."},
        {"tipe": "mcq", "soal": "Air hujan alami murni agak asam (pH 5.6) karena larutnya gas...", "opsi": ["A. O2", "B. N2", "C. CO2", "D. Ar"], "jawaban": "C. CO2", "pembahasan": "Membentuk asam karbonat lemah."},
        {"tipe": "multiselect", "soal": "Ciri Basa di kehidupan:", "opsi": ["Terasa licin (soapy)", "Pahit", "Melarutkan karat/besi", "Lakmus merah jadi biru"], "jawaban": ["Terasa licin (soapy)", "Pahit", "Lakmus merah jadi biru"], "pembahasan": "Karat dilarutkan asam korosif."},
        {"tipe": "short_answer", "soal": "Logaritma negatif konsentrasi Hidroksida ditulis... (Ketik poh)", "opsi": [], "jawaban": "poh", "pembahasan": "pOH."},
        {"tipe": "numeric", "soal": "Larutan pOH = 9. pH nya?", "opsi": [], "jawaban": 5, "pembahasan": "14 - 9 = 5."},
        {"tipe": "mcq", "soal": "100mL HCl pH 2 + 900mL air murni. pH akhir?", "opsi": ["A. 1", "B. 3", "C. 4", "D. 11"], "jawaban": "B. 3", "pembahasan": "Volume total 10x lipat. Molaritas jadi 1/10 (10^-3). pH naik jadi 3."}
    ],
    "7. Hidrolisis Garam": [
        {"tipe": "mcq", "soal": "Definisi 'Hidrolisis Garam' secara kimia:", "opsi": ["A. Garam larut fisik murni", "B. Ion dari lemah memecah air hasilkan H+/OH-", "C. Pembentukan garam", "D. Penguapan air laut"], "jawaban": "B. Ion dari lemah memecah air hasilkan H+/OH-", "pembahasan": "Garam dari yang lemah akan bereaksi memutus molekul H2O."},
        {"tipe": "hotspot", "soal": "Kertas lakmus merah di larutan Natrium Asetat (CH3COONa). Warna jadi...", "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Litmus_paper.jpg/300px-Litmus_paper.jpg", "opsi": ["A. Tetap Merah", "B. Jadi Biru", "C. Putih pudar", "D. Terbakar"], "jawaban": "B. Jadi Biru", "pembahasan": "Na(Kuat) dan Cuka(Lemah) = Garam Basa (Biru)."},
        {"tipe": "tf", "soal": "Garam NaCl di air terhidrolisis sempurna.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Ion kuat (Na, Cl) TIDAK BISA terhidrolisis di air. NaCl netral mutlak."},
        {"tipe": "multiselect", "soal": "Garam Hidrolisis dan bersifat ASAM:", "opsi": ["NH4Cl", "Al2(SO4)3", "KNO3", "CH3COOK"], "jawaban": ["NH4Cl", "Al2(SO4)3"], "pembahasan": "Terbentuk dari Asam Kuat dan Basa Lemah."},
        {"tipe": "matching", "soal": "Sifat pH Garam:", "kiri": ["NH4Cl", "CH3COONa", "K2SO4"], "kanan": ["Netral", "Asam (<7)", "Basa (>7)"], "jawaban": {"NH4Cl": "Asam (<7)", "CH3COONa": "Basa (>7)", "K2SO4": "Netral"}, "pembahasan": "Kuat yg menang dominan tentukan pH."},
        {"tipe": "numeric", "soal": "pH CH3COONa 0.1 M (Kw=10^-14, Ka=10^-5)?", "opsi": [], "jawaban": 9, "pembahasan": "[OH-] = 10^-5 -> pOH = 5 -> pH = 9."},
        {"tipe": "short_answer", "soal": "Garam Lemah-Lemah (Amonium asetat) mengalami hidrolisis... (Ketik total)", "opsi": [], "jawaban": "total", "pembahasan": "Kedua ionnya ikut bereaksi memecah air."},
        {"tipe": "mcq", "soal": "Cara tahu garam Lemah-Lemah itu asam/basa/netral?", "opsi": ["A. Sama-sama lemah = netral", "B. Konsentrasi garam", "C. Bandingkan Ka dan Kb", "D. Indikator lakmus khusus"], "jawaban": "C. Bandingkan Ka dan Kb", "pembahasan": "Jika Ka > Kb = Asam. Kb > Ka = Basa."},
        {"tipe": "tf", "soal": "Hidrolisis esensialnya kebalikan dari netralisasi.", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Asam+Basa->Garam+Air (Netral). Garam+Air->Asam+Basa (Hidrolisis)."},
        {"tipe": "numeric", "soal": "pH NH4Cl 0.1 M (Kb=10^-5)?", "opsi": [], "jawaban": 5, "pembahasan": "[H+] = sqrt(10^-14/10^-5 * 0.1) = 10^-5. pH = 5."},
        {"tipe": "multiselect", "soal": "Aplikasi Hidrolisis Garam:", "opsi": ["Tawas (Al2(SO4)3) menjernihkan air", "Pupuk Amonium asamkan tanah", "Pemutih klorin (NaClO) noda basa", "Garam NaCl awetkan ikan"], "jawaban": ["Tawas (Al2(SO4)3) menjernihkan air", "Pupuk Amonium asamkan tanah", "Pemutih klorin (NaClO) noda basa"], "pembahasan": "NaCl pengawet bukan dengan hidrolisis tapi osmosis biologis."},
        {"tipe": "mcq", "soal": "NaCN sangat basa karena...", "opsi": ["A. Na bereaksi air", "B. CN- hidrolisis memecah air hasilkan OH- bebas", "C. Gas HCN volatil", "D. Disosiasi sempurna"], "jawaban": "B. CN- hidrolisis memecah air hasilkan OH- bebas", "pembahasan": "Anion lemah (CN-) terhidrolisis memproduksi ion hidroksida penentu basa."},
        {"tipe": "short_answer", "soal": "Ion asam/basa kuat di air yang cuma numpang lewat adalah ion... (Ketik spektator)", "opsi": [], "jawaban": "spektator", "pembahasan": "Penonton pasif."},
        {"tipe": "mcq", "soal": "Garam NH4CN (Ka HCN = 6.2x10^-10, Kb NH3 = 1.8x10^-5). pH larutannya?", "opsi": ["A. Asam Kuat", "B. Asam Lemah", "C. Basa Lemah (>7)", "D. Netral"], "jawaban": "C. Basa Lemah (>7)", "pembahasan": "Kb > Ka. Basa lebih menang."},
        {"tipe": "tf", "soal": "Pengenceran ekstrem garam NH4Cl dengan air akan mendekatkan pH ke 7.", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Konsentrasi ion H+ hidrolisis merenggang/menurun."},
        {"tipe": "numeric", "soal": "Kh natrium asetat (Kh=Kw/Ka). Ka=10^-5. Nilai Pangkat negatif Kh? (Ketik angkanya: 9)", "opsi": [], "jawaban": 9, "pembahasan": "10^-14 / 10^-5 = 10^-9. Pangkatnya 9."},
        {"tipe": "multiselect", "soal": "Ion yang MENGALAMI HIDROLISIS di air:", "opsi": ["Na+", "CO3^2-", "Cl-", "CN-", "NH4+"], "jawaban": ["CO3^2-", "CN-", "NH4+"], "pembahasan": "Hanya sisa yang Lemah."},
        {"tipe": "mcq", "soal": "Campur 100mL NaOH 0.1M + 100mL HCl 0.1M. pH akhirnya?", "opsi": ["A. 1", "B. 5", "C. 7", "D. 13"], "jawaban": "C. 7", "pembahasan": "Habis sempurna jadi NaCl netral."},
        {"tipe": "short_answer", "soal": "Al3+ terhidrolisis hasilkan ion H+. Larutan bersifat... (Ketik asam)", "opsi": [], "jawaban": "asam", "pembahasan": "Ion H+ = Asam."},
        {"tipe": "tf", "soal": "Baking soda (NaHCO3) hasilkan larutan basa ringan dari hidrolisis HCO3-.", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Bikarbonat (lemah) bereaksi hasilkan OH-."}
    ],
    "8. Larutan Penyangga (Buffer)": [
        {"tipe": "mcq", "soal": "Sifat unggul Buffer (Penyangga) adalah...", "opsi": ["A. Mudah berubah pH", "B. Mempertahankan pH konstan jika ditambah sedikit asam/basa/air", "C. Menetralkan semua racun", "D. Ubah asam kuat jadi air murni"], "jawaban": "B. Mempertahankan pH konstan jika ditambah sedikit asam/basa/air", "pembahasan": "Sistem redam (shock absorber) menahan fluktuasi pH."},
        {"tipe": "hotspot", "soal": "Pada kurva titrasi Asam Lemah dan Basa Kuat, Kapasitas Buffer berada di area...", "gambar": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Titration_curve_strong_acid_weak_base.png/300px-Titration_curve_strong_acid_weak_base.png", "opsi": ["A. Garis vertikal di tengah", "B. Titik ekuivalen", "C. Area landai di bagian awal/bawah", "D. Garis datar ujung atas"], "jawaban": "C. Area landai di bagian awal/bawah", "pembahasan": "Sebelum pH anjlok/melonjak, sisa asam lemah menahan grafik tetap landai horizontal."},
        {"tipe": "tf", "soal": "Asam Kuat berlebih + Basa Lemah sisa = Buffer Asam murni.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "YANG SISA HARUS YANG LEMAH untuk membentuk buffer."},
        {"tipe": "multiselect", "soal": "Komposisi Buffer Asam:", "opsi": ["Asam lemah murni", "Basa konjugasinya", "Asam kuat sisa", "Asam lemah sisa + Basa kuat habis"], "jawaban": ["Asam lemah murni", "Basa konjugasinya", "Asam lemah sisa + Basa kuat habis"], "pembahasan": "Kombinasi Lemah dan Garamnya."},
        {"tipe": "matching", "soal": "Sistem Buffer Tubuh:", "kiri": ["Karbonat (H2CO3 / HCO3-)", "Fosfat (H2PO4- / HPO4^2-)", "Asam Amino/Protein"], "kanan": ["Darah/Ekstraseluler", "Intraseluler (Dalam Sel)", "Jaringan Otot/Darah umum"], "jawaban": {"Karbonat (H2CO3 / HCO3-)": "Darah/Ekstraseluler", "Fosfat (H2PO4- / HPO4^2-)": "Intraseluler (Dalam Sel)", "Asam Amino/Protein": "Jaringan Otot/Darah umum"}, "pembahasan": "Karbonat = darah. Fosfat = dalam sel tubuh."},
        {"tipe": "numeric", "soal": "pH Buffer 0.1 mol CH3COOH + 0.1 mol CH3COONa (Ka=10^-5)?", "opsi": [], "jawaban": 5, "pembahasan": "[H+] = 10^-5 * (0.1/0.1) = 10^-5 -> pH = 5."},
        {"tipe": "short_answer", "soal": "Jika HCl masuk buffer asetat, ia dinetralkan oleh ion... (Ketik ch3coo-)", "opsi": [], "jawaban": "ch3coo-", "pembahasan": "Basa konjugasi menyerang H+ dari asam kuat luar."},
        {"tipe": "mcq", "soal": "Kapasitas penyangga paling optimal (Buffer Ideal) jika...", "opsi": ["A. Asam lemah sangat dominan", "B. Pengenceran ekstrem", "C. Mol asam lemah = Mol basa konjugasi (Rasio 1)", "D. Pakai Indikator PP"], "jawaban": "C. Mol asam lemah = Mol basa konjugasi (Rasio 1)", "pembahasan": "Saat rasio 1 (pH = pKa), buffer paling kuat menahan pH naik maupun turun."},
        {"tipe": "tf", "soal": "Pengenceran air murni merusak nilai pH buffer teoretis.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Air merenggangkan mol dua sisi dengan proporsional, rasio tetap, pH tetap."},
        {"tipe": "numeric", "soal": "pH Buffer Basa: 0.1 mol NH3 + 0.01 mol NH4+ (Kb=10^-5)?", "opsi": [], "jawaban": 10, "pembahasan": "pOH = -log(10^-5 * 0.1/0.01) = -log(10^-4) = 4. pH = 14-4=10."},
        {"tipe": "multiselect", "soal": "Skenario BUKAN Buffer:", "opsi": ["NaOH 0.1M + HCl 0.1M", "HCN 0.2M + NaOH 0.1M", "NH3 0.1M + HCl 0.2M", "CH3COOH + CH3COONa"], "jawaban": ["NaOH 0.1M + HCl 0.1M", "NH3 0.1M + HCl 0.2M"], "pembahasan": "Kuat-kuat, atau kuat sisa = bukan buffer."},
        {"tipe": "short_answer", "soal": "Kondisi pH darah < 7.35 fatal disebut... (Ketik asidosis)", "opsi": [], "jawaban": "asidosis", "pembahasan": "Darah terlalu asam."},
        {"tipe": "mcq", "soal": "Obat tetes mata steril agar tak perih ditambah bahan...", "opsi": ["A. Gula", "B. Asam", "C. Larutan Penyangga (Buffer) Isotonik", "D. Pewarna"], "jawaban": "C. Larutan Penyangga (Buffer) Isotonik", "pembahasan": "Penyangga menahan pH obat sama dengan air mata kornea alami."},
        {"tipe": "tf", "soal": "Asam amino adalah buffer alami karena struktur zwitterion (amfoter).", "opsi": ["True", "False"], "jawaban": "True", "pembahasan": "Bisa menetralisir asam di satu kutub, dan basa di kutub lain."},
        {"tipe": "numeric", "soal": "pKa buffer = 5. Rentang pH maksimal efektifnya adalah... (Ketik 6)", "opsi": [], "jawaban": 6, "pembahasan": "Rentang efektif pKa ± 1. Max = 5+1 = 6."},
        {"tipe": "multiselect", "soal": "Jika buffer NH3/NH4+ ditetesi NaOH (Basa kuat):", "opsi": ["OH- diserang NH4+", "OH- ditangkap NH3", "Terbentuk Air dan NH3 baru", "Mendidih"], "jawaban": ["OH- diserang NH4+", "Terbentuk Air dan NH3 baru"], "pembahasan": "Asam konjugasi NH4+ mengorbankan diri menetralkan basa luar."},
        {"tipe": "mcq", "soal": "Buffer CH3COOH dan CH3COOK. Ion apa yang hanya numpang lewat (spektator)?", "opsi": ["A. CH3COOH", "B. CH3COO-", "C. K+", "D. H+"], "jawaban": "C. K+", "pembahasan": "K+ dari basa kuat tidak bereaksi apapun."},
        {"tipe": "short_answer", "soal": "Persamaan pH buffer klasik medis: Henderson-... (Ketik hasselbalch)", "opsi": [], "jawaban": "hasselbalch", "pembahasan": "Rumus pH = pKa + log(Garam/Asam)."},
        {"tipe": "tf", "soal": "Tetes 1mL HCl di NaCl vs di Buffer Asetat beri dampak drastis sama.", "opsi": ["True", "False"], "jawaban": "False", "pembahasan": "Di NaCl pH anjlok drastis, di Buffer ditahan nyaris tetap."},
        {"tipe": "numeric", "soal": "Darah rasio normal [HCO3-]/[H2CO3] = 20:1. Jika H2CO3 2 mol, HCO3- ada berapa mol?", "opsi": [], "jawaban": 40, "pembahasan": "2 * 20 = 40 mol."}
    ]
}

# --- 4. TAMPILAN HALAMAN UTAMA ---
if "kuis_aktif" not in st.session_state: 
    st.session_state.kuis_aktif = False

# Halaman Awal
if not st.session_state.kuis_aktif:
    st.markdown("<h1 style='text-align: center;'>🎓 Ujian CBT Kimia - Kelas 11</h1>", unsafe_allow_html=True)
    st.write("")
    
    with st.container(border=True):
        st.markdown("### 📜 Aturan Mengerjakan Ujian")
        st.info("""
        1. **Berdoalah** sebelum memulai.
        2. Kuis ini berisi **20 soal HOTS** setiap bab.
        3. Tipe Soal Lengkap: MCQ, Multiselect, True/False, Input Angka, Isian, Hotspot, dan Matching.
        4. Klik tombol **Kembali** jika ingin merevisi.
        5. Hasil dan pembahasan keluar setelah klik kumpulkan.
        """)
        
        st.markdown("---")
        st.markdown("### 📂 Pilih Bab Materi Kelas 11:")
        pilih_bab = st.selectbox("Materi K13 Terarsip:", list(DATABASE_SOAL.keys()), label_visibility="collapsed")
        
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
        st.progress((idx)/len(daftar_soal), text=f"Sedang Dikerjakan: Soal {idx+1} / {len(daftar_soal)}")
        
        with st.container(border=True):
            st.markdown(f"**Pertanyaan {idx+1}:**")
            st.write(curr["soal"])
            if "gambar" in curr:
                st.image(curr["gambar"], width=250)
            st.markdown("---")
            
            jawaban_tersimpan = st.session_state.jawaban_user.get(idx)
            ans = None
            
            # WIDGET SESUAI TIPE
            if curr["tipe"] in ["mcq", "tf", "hotspot"]:
                default_idx = curr["opsi"].index(jawaban_tersimpan) if jawaban_tersimpan in curr["opsi"] else None
                ans = st.radio("Pilih Opsi Terbaik:", curr["opsi"], key=f"q{idx}", index=default_idx)
            elif curr["tipe"] == "multiselect":
                default_vals = jawaban_tersimpan if isinstance(jawaban_tersimpan, list) else []
                ans = st.multiselect("Pilih SEMUA yang Benar:", curr["opsi"], key=f"q{idx}", default=default_vals)
            elif curr["tipe"] == "numeric":
                default_val = jawaban_tersimpan if jawaban_tersimpan is not None else 0
                ans = st.number_input("Ketik Angka Saja:", step=1, key=f"q{idx}", value=default_val)
            elif curr["tipe"] == "short_answer":
                default_val = jawaban_tersimpan if jawaban_tersimpan else ""
                ans = st.text_input("Ketik Kata Jawaban:", key=f"q{idx}", value=default_val)
            elif curr["tipe"] == "matching":
                st.write("Pasangkan dari Kiri ke Kanan:")
                ans = {}
                default_dict = jawaban_tersimpan if isinstance(jawaban_tersimpan, dict) else {}
                for kiri_item in curr["kiri"]:
                    val_lama = default_dict.get(kiri_item, "-- Pilih --")
                    list_kanan = ["-- Pilih --"] + curr["kanan"]
                    idx_default = list_kanan.index(val_lama) if val_lama in list_kanan else 0
                    ans[kiri_item] = st.selectbox(kiri_item, list_kanan, index=idx_default, key=f"match_{idx}_{kiri_item}")
            
            st.write("")
            col1, col2 = st.columns(2)
            
            with col1:
                if idx > 0:
                    if st.button("⏪ Kembali ke Soal", use_container_width=True):
                        st.session_state.jawaban_user[idx] = ans
                        st.session_state.indeks_soal -= 1
                        st.rerun()
                else:
                    if st.button("🛑 Batalkan Ujian", use_container_width=True):
                        st.session_state.kuis_aktif = False
                        st.rerun()
            
            with col2:
                teks_tombol = "Selesai & Kumpulkan 🏁" if idx == len(daftar_soal) - 1 else "Simpan & Lanjut ⏭️"
                if st.button(teks_tombol, use_container_width=True):
                    is_valid = True
                    if ans is None or ans == "" or ans == []: is_valid = False
                    if curr["tipe"] == "matching" and "-- Pilih --" in ans.values(): is_valid = False
                    
                    if is_valid:
                        st.session_state.jawaban_user[idx] = ans
                        st.session_state.indeks_soal += 1
                        st.rerun()
                    else:
                        st.error("⚠️ Anda wajib mengisi/menjodohkan semua!")
                        
    else:
        # --- 6. HASIL & SKOR ---
        skor_akhir = 0
        bobot = 100 / len(daftar_soal)
        
        for i, s in enumerate(daftar_soal):
            jwbn = st.session_state.jawaban_user.get(i)
            is_correct = False
            
            if jwbn is not None:
                if s["tipe"] in ["mcq", "tf", "hotspot", "numeric"]:
                    if str(jwbn).strip().lower() == str(s["jawaban"]).strip().lower(): is_correct = True
                elif s["tipe"] == "multiselect":
                    if isinstance(jwbn, list) and set(jwbn) == set(s["jawaban"]): is_correct = True
                elif s["tipe"] == "short_answer":
                    if str(jwbn).strip().lower() in str(s["jawaban"]).lower(): is_correct = True
                elif s["tipe"] == "matching":
                    if isinstance(jwbn, dict) and jwbn == s["jawaban"]: is_correct = True
            
            if is_correct: skor_akhir += bobot
            
        st.session_state.skor = skor_akhir

        st.balloons()
        st.markdown("<h1 style='text-align: center; color: #be185d !important;'>Ujian Selesai!</h1>", unsafe_allow_html=True)
        
        with st.container(border=True):
            if st.session_state.skor >= 75: 
                st.success(f"### 🎉 Lulus! Skor Anda: {int(st.session_state.skor)}")
            else: 
                st.warning(f"### 📚 Remedial. Skor Anda: {int(st.session_state.skor)}")
            
            st.markdown("---")
            st.markdown("#### 📖 Pembahasan Lengkap")
            for i, s in enumerate(daftar_soal):
                jwbn = st.session_state.jawaban_user.get(i, "-")
                with st.expander(f"Soal {i+1} | Tipe: {s['tipe'].upper()}"):
                    st.write(s['soal'])
                    if "gambar" in s: st.image(s["gambar"], width=200)
                    
                    if s["tipe"] == "matching":
                        st.markdown("**Jawaban Anda:**")
                        st.json(jwbn)
                        st.markdown("**Kunci Standar:**")
                        st.json(s['jawaban'])
                    else:
                        st.markdown(f"**Jawaban:** `{jwbn}` | **Kunci:** `{s['jawaban']}`")
                        
                    st.info(f"**Pembahasan:** {s['pembahasan']}")
                
        st.write("")        
        if st.button("Kembali ke Menu Utama 🏠", use_container_width=True):
            st.session_state.kuis_aktif = False
            st.rerun()