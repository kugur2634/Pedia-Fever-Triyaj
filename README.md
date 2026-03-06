# Pedia-Fever-Triyaj: Yapay Zeka Destekli Ateşli Çocuklarda Karar Destek Sistemi

## Projenin Amacı
Pedia-Fever-Triyaj, çocuk doktorlarının yoğunluğunu azaltmak ve ebeveynlere doğru yönlendirme yapmak için geliştirilmiş bir **Makine Öğrenmesi (Machine Learning)** projesidir. Ebeveynler evde çocuklarının/bebeklerinin sağlık durumuyla ilgili sıklıkla endişe duyarlar. Bu projede ebeveynlerin doktorla veya hastaneyle iletişime geçmeden önce yapay zeka algoritması kullanan bir sisteme çocuklarının/bebeklerinin mevcut verilerini girip karşılığında belirli direktifler/öneriler almaları amaçlanmıştır. Bu sayede ebeveynlerin endişeleri bilimsel bir ön değerlendirmeyle giderilirken, hem alandaki doktorların hem de ebeveynlerin gereksiz yoğunluğunun ve zaman kaybının da önüne geçilmesi hedeflenmektedir. Sadece veriden öğrenen kör bir model olmak yerine, Pediatri alanında uzman olan bir doktorla çalışılıp sistemin içine tıp kuralları entegre edilmiş **Hibrit bir Karar Destek Sistemi** olarak tasarlanmıştır. Projedeki ana amaç, bu sistemi bir mobil aplikasyon aracılığı ile ebeveynlerin evde kullanmasıdır.

## Öne Çıkan Özellikler (Klinik Güvenlik Duvarları)
Bu sistem, modelin yanlış tahmin yapmasını engellemek için klinik uzman direktifleriyle "Guardrail" (Güvenlik Duvarı) mantığıyla donatılmıştır:
* **Hipotermi Kalkanı:** Sistem 35°C altındaki girişlerde modele gitmeden doğrudan "Acil Hipotermi" uyarısı verir.
* **Dinamik Yaş Kontrolü:** 6 aydan küçük bebekler için tıbbi olarak yanıltıcı olan "Timpanik (Kulak) Ölçüm" seçeneği arayüzden otomatik olarak kaldırılır, kullanıcı hatası engellenir.
* **İnteraktif Arayüz:** Streamlit kullanılarak son kullanıcının kolayca kullanabileceği web tabanlı bir uygulama geliştirilmiştir.

## 🛠️ Kullanılan Teknolojiler
* **Python** (Veri işleme ve modelleme)
* **Scikit-Learn** (Random Forest Classifier)
* **Pandas & NumPy** (Veri manipülasyonu ve sentetik veri üretimi)
* **Streamlit** (Web arayüzü geliştirme)
* **Joblib** (Model persistency - modelin kaydedilip çağrılması)

## 🗺️ Gelecek Yol Haritası (Roadmap)
Bu proje şu an bir MVP (Minimum Viable Product) aşamasındadır. Gelecek geliştirmeler şunları kapsar:
1. Sınıf dengesizliklerini gidermek için veri setine **SMOTE-Tomek** boru hattının (pipeline) entegre edilmesi.
2. "Nedeni bilinmeyen ateş (FUO)" senaryolarını kapsayacak şekilde global ve geniş çaplı açık kaynak medikal veri setlerine geçiş yapılması.
3. Kusma, ishal, öksürük, döküntü, ateşin süresi gibi yeni özelliklerin (features) modele dahil edilmesi.
