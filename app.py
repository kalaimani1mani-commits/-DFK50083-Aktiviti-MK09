import streamlit as st

# ------------------------------------------
# DFK50083 Aktiviti MK09
# Kalkulator BMI Klinik - Pengendalian Pengecualian
# ------------------------------------------

st.title("Kalkulator BMI Klinik")

st.write("Sila masukkan maklumat pesakit di bawah untuk mengira Indeks Jisim Badan (BMI).")

# 1. Input dari pengguna
berat_input = st.text_input("Berat (kg)")
tinggi_input = st.text_input("Tinggi (meter)")

# 2. Butang untuk mengira BMI
if st.button("Kira BMI"):
    try:
        # Menukar input kepada nombor (float)
        berat = float(berat_input)
        tinggi = float(tinggi_input)

        # Pengiraan BMI - berpotensi ZeroDivisionError jika tinggi = 0
        bmi = berat / (tinggi * tinggi)

    except ValueError:
        # Jika pengguna memasukkan huruf/abjad dan bukan nombor
        st.error("Ralat: Sila masukkan nilai nombor yang sah untuk berat dan tinggi.")

    except ZeroDivisionError:
        # Jika pengguna memasukkan 0.0 pada tinggi
        st.error("Ralat: Tinggi tidak boleh bernilai kosong (0). Sila masukkan nilai tinggi yang betul.")

    except Exception as e:
        # Blok pukal (catch-all) untuk ralat-ralat lain yang tidak dijangka
        st.error(f"Ralat tidak dijangka telah berlaku: {e}")

    else:
        # Jika pengiraan berjaya tanpa sebarang ralat
        st.success(f"Pengiraan berjaya! BMI pesakit ialah: {bmi:.2f}")

    finally:
        # Sentiasa dipaparkan tidak kira sama ada pengiraan berjaya atau gagal
        st.info("Sistem selesai memproses permintaan anda.")

st.divider()

# 3. Bahagian Simulasi FileNotFoundError - Papar Rekod Lama
st.subheader("Rekod Pesakit Lama")

if st.button("Papar Rekod Lama"):
    try:
        with open("rekod_pesakit.txt", "r") as fail:
            kandungan = fail.read()
            st.text(kandungan)

    except FileNotFoundError:
        # Jika fail rekod_pesakit.txt tiada dalam sistem
        st.warning("Fail rekod belum diwujudkan.")
