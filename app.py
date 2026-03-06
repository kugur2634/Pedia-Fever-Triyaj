import streamlit as st
import joblib
import pandas as pd


try:
    model = joblib.load('pedia_triyaj_model.pkl')
except:
    st.error("Model Dosyasi Bulunamadi")


st.title("Pedia-Triyaj Sistemi")
st.write("Yapay Zeka Destekli Pediatrik Ates Degerlendirme Asistani")

st.divider() #Araya çizgi çekiyor

yas = st.number_input("Cocugunuzun yasiniz giriniz (Ay Olarak): ", min_value=0, value=12, step=1)
if yas < 6:
    st.warning("6 AYDAN KUCUK COCUKLARDA OLCUM YERI OLARAK KULAK ONERILMEZ!")
    gecerli_bolgeler = ["Koltuk Alti", "Alin", "Makat"]
else:
    gecerli_bolgeler = ["Koltuk Alti", "Kulak", "Alin", "Makat"]

col1, col2 = st.columns(2) #Sağ ve Sol sütun olarak ikiye ayırıyoruz ekranı

with col1:
    ates = st.number_input("Ates Derecesi", value=37.0, step=0.1)
with col2:
    bolge = st.selectbox("Olcum Yeri", gecerli_bolgeler)


if st.button("Durumu Analiz Et?"):
    
    if ates < 35.0:
        st.error("HIPOTERMI RISKI!!! Vucut isisi cok dusuk")
    else:
        #Veriyi Modele Hazırlama
        girdi_verisi = {
            'Sicaklik': [ates],
            'Olcum Yeri_Alin': [0],
            'Olcum Yeri_Koltuk Alti': [0],
            'Olcum Yeri_Kulak': [0],
            'Olcum Yeri_Makat': [0]
        }

        #Secilen Bölgeyi 1 Yapıyoruz
        secilen_bolge = f"Olcum Yeri_{bolge}"
        girdi_verisi[secilen_bolge] = [1]

        #Dataframe'e çevir
        df_tahmin = pd.DataFrame(girdi_verisi)

        #Tahmin
        sonuc = model.predict(df_tahmin)[0]

        #Sonucu Göster
        st.subheader("Sonuc:")

        if sonuc == 0:
            st.success("DURUM NORMAL - Endiseye gerek yok.")
        elif sonuc == 1:
            st.warning("HAFIF ATES - Evde takip onerilir.")
        else:
            st.error("YUKSEK ATES!!! - Doktora danisilmasi onerilir")