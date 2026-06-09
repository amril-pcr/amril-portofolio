import streamlit as st

st.set_page_config(
    page_title="Portfolio Amril",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background: linear-gradient(135deg,#141E30,#243B55);
}
.title {
    text-align:center;
    color:white;
    font-size:50px;
    font-weight:bold;
}
.sub {
    text-align:center;
    color:#00e5ff;
    font-size:22px;
}
.card {
    background-color: rgba(255,255,255,0.08);
    padding:20px;
    border-radius:15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">🚀 AMRIL</p>', unsafe_allow_html=True)
st.markdown('<p class="sub">Mahasiswa Teknik Elektro - Politeknik Caltex Riau</p>', unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns([1,2])

with col1:
    st.image("https://i.pravatar.cc/300", width=250)

with col2:
    st.subheader("📋 Data Diri")
    st.write("**NIM :** 2420307003")
    st.write("**Jurusan :** Teknik Elektro")
    st.write("**Hobi :** Coding dan Mancing")
    st.write("**Email :** amril24trse@mahasiswa.pcr.ac.id")
    st.write("**No HP :** 08971722424")
    st.write("**Lokasi :** Pekanbaru, Riau")

st.divider()

st.subheader("💻 Skill")
st.progress(90, text="Python")
st.progress(85, text="Arduino")
st.progress(80, text="ESP32")
st.progress(75, text="SQL")

st.divider()

st.subheader("📂 Proyek")
st.success("Website Monitoring Sensor ESP32")
st.success("Data Logger Raspberry Pi")
st.success("Sistem Monitoring Suhu & Kelembaban")

st.divider()

st.subheader("📞 Kontak")
st.link_button("WhatsApp", "https://wa.me/628971722424")
st.link_button("Email", "mailto:amril24trse@mahasiswa.pcr.ac.id")

st.caption("© 2026 Portfolio Amril")