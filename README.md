# 📈 Bütçe Takip Uygulaması

## 🌟 Proje Hakkında
Bütçe Takip Uygulaması, **günlük gelir ve giderleri takip ederek finansal durumunuzu gözlemlemenizi sağlayan** modern ve kullanıcı dostu bir web uygulamasıdır. 

Bu uygulama sayesinde:
- 📅 **Günlük gelir ve giderleri ekleyebilir,**
- 🔬 **Gelir-gider dengenizi çizgi grafiği ile görsel olarak takip edebilir,**
- 📃 **Tüm işlemleri tablo halinde listeleyerek detaylı rapor alabilirsiniz.**

Bu proje, **Flask (Python), HTML, CSS ve JavaScript (Chart.js)** teknolojilerini kullanarak geliştirildi.

---

## 🛠️ Teknolojiler
Bu proje aşağıdaki teknolojiler ve kütüphaneleri kullanır:

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Grafik Kütüphanesi:** Chart.js
- **Stil Kütüphanesi:** Google Fonts (Poppins)

---

## 🛠️ Kurulum
Proje bilgisayarınıza çekmek ve çalıştırmak için aşağıdaki adımları izleyin:

### ✅ 1. Depoyu Klonlayın
```bash
git clone https://github.com/bektas-sari/gelir-gider-takip-v1.git
cd gelir-gider-takip-v1
```

### ✅ 2. Sanal Ortamı Olusturun ve Flask'i Yükleyin
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
dot venv/Scripts/activate  # Windows
pip install -r requirements.txt
```

### ✅ 3. Uygulamayı Çalıştırın
```bash
python app.py
```

**Uygulama tarayıcıda şu adreste çalışacaktır:** [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📈 Kullanım Kılavuzu

1. **Gelir/Gider Ekleme**: Formu kullanarak bir **gün, açıklama ve tutar** girin, **gelir mi gider mi olduğunu** seçin ve "Ekle" butonuna basın.
2. **Grafik Takibi**: Grafikte **günlük net bakiye değişimini** takip edebilirsiniz.
3. **İşlem Geçmişi**: Tüm eklenen işlemler **tarih, açıklama ve miktar** olarak tabloda listelenir.

---

## 🛠️ Geliştirme

### 📚 Yeni Özellikler Eklemek
Bu projeye yeni özellikler ekleyebilirsiniz. İşte bazı öneriler:

- **Kategori bazlı gider takibi** (kira, yiyecek, fatura vb.)
- **Aylık bütçe planlama ve uyarı sistemi**
- **PDF veya Excel rapor alma**
- **E-posta bildirimleri**

### 🔧 Kod Yapısı
- **`app.py`**: Flask backend
- **`templates/index.html`**: Ana sayfa
- **`static/style.css`**: Tasarım dosyası
- **`static/script.js`**: Grafik ve veri güncelleme

---

## 🚀 Katkıda Bulunma
Projeye katkıda bulunmak istiyorsanız:
1. Depoyu forklayın (Üstte "Fork" butonu)
2. Yeni bir branch oluşturun: `git checkout -b yeni-ozellik`
3. Değişiklikleri yapın ve commit atın: `git commit -m "Yeni özellik eklendi"`
4. Deponuza push edin: `git push origin yeni-ozellik`
5. Bir **Pull Request (PR)** oluşturun!

---

## 📢 Lisans
MIT Lisansı altında dağıtılmaktadır.

---
## 👤 Geliştirici

**Bektas Sari**  
Email: bektas.sari@gmail.com  <br>
GitHub: https://github.com/bektas-sari <br>
LinkedIn: www.linkedin.com/in/bektas-sari <br>
Researchgate: https://www.researchgate.net/profile/Bektas-Sari-3 <br>
Academia: https://independent.academia.edu/bektassari <br>

**✨ Finansal durumunuzu kontrol altına almak için bu uygulamayı kullanın! ✨** 
