import streamlit as st

# ===== Fungsi Utama =====
def hitung_rata_rata(nilai_list):
    return sum(nilai_list) / len(nilai_list) if nilai_list else 0

def tentukan_grade(nilai):
    if nilai >= 85: return "A"
    elif nilai >= 75: return "B"
    elif nilai >= 65: return "C"
    elif nilai >= 50: return "D"
    else: return "E"

def cek_kelulusan(nilai):
    return "✅ Lulus" if nilai >= 70 else "❌ Tidak Lulus"

# ===== Tampilan Utama =====
st.set_page_config(page_title="Penilaian Akademik", page_icon="📘", layout="centered")
st.title("📘 Aplikasi Penilaian Akademik Sederhana")
st.sidebar.success("Gunakan menu di bawah untuk navigasi")

# Sidebar navigasi
page = st.sidebar.radio(
    "📑 Pilih Halaman",
    ["Page 1 - Penilaian Nilai Mata Kuliah",
     "Page 2 - Evaluasi Kelulusan",
     "Page 3 - Rapor Digital",
     "Page 4 - Presensi Penentu Kelulusan"]
)

# ===== Halaman 1 =====
if page == "Page 1 - Penilaian Nilai Mata Kuliah":
    st.header("📝 Penilaian Nilai Mata Kuliah")
    st.info("Masukkan nilai tugas, kuis, UTS, dan UAS untuk menghitung rata-rata dan grade.")

    col1, col2 = st.columns(2)
    with col1:
        tugas = st.number_input("Nilai Tugas", 0, 100, 0)
        kuis = st.number_input("Nilai Kuis", 0, 100, 0)
    with col2:
        uts = st.number_input("Nilai UTS", 0, 100, 0)
        uas = st.number_input("Nilai UAS", 0, 100, 0)

    if st.button("🚀 Hitung Grade"):
        nilai = [tugas, kuis, uts, uas]
        rata = hitung_rata_rata(nilai)
        grade = tentukan_grade(rata)

        st.success(f"📊 Rata-rata: {round(rata, 2)}")
        st.write(f"🏅 Grade: **{grade}**")

# ===== Halaman 2 =====
elif page == "Page 2 - Evaluasi Kelulusan":
    st.header("🎓 Evaluasi Kelulusan")
    st.info("Masukkan nilai akhir untuk mengetahui status kelulusan.")

    nilai_akhir = st.number_input("Nilai Akhir", 0, 100, 0)
    if st.button("🔍 Cek Kelulusan"):
        st.write("Status:", cek_kelulusan(nilai_akhir))

# ===== Halaman 3 =====
elif page == "Page 3 - Rapor Digital":
    st.header("📄 Rapor Digital")
    st.info("Masukkan nilai beberapa mata kuliah untuk membuat rapor sederhana.")

    jumlah = st.number_input("Jumlah Mata Kuliah", 1, 10, 3)
    data = []
    for i in range(jumlah):
        matkul = st.text_input(f"Nama Mata Kuliah {i+1}", key=f"matkul{i}")
        nilai = st.number_input(f"Nilai {i+1}", 0, 100, 0, key=f"nilai{i}")
        data.append({"Mata Kuliah": matkul, "Nilai": nilai})

    if st.button("📊 Generate Rapor"):
        st.subheader("📋 Hasil Rapor")
        # tampilkan tabel rapor
        st.table(data)

        # hitung rata-rata dan grade
        rata = hitung_rata_rata([d["Nilai"] for d in data])
        grade = tentukan_grade(rata)

        st.success(f"Rata-rata: {round(rata, 2)}")
        st.write(f"🏅 Grade Akhir: **{grade}**")

# ===== Halaman 4 =====
elif page == "Page 4 - Presensi Penentu Kelulusan":
    st.header("📅 Presensi Penentu Kelulusan")
    st.info("Kelulusan ditentukan berdasarkan jumlah alfa (tidak hadir). Maksimal 3 kali alfa.")

    alfa = st.number_input("Jumlah Alfa (Tidak Hadir)", 0, 20, 0)
    if st.button("📌 Cek Status Presensi"):
        if alfa > 3:
            st.error("❌ Status: Tidak Lulus (Alfa lebih dari 3 kali)")
        else:
            st.success("✅ Status: Lulus (Alfa maksimal 3 kali)")