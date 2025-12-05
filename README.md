# 🕸️ Python Web Tarayıcı (Eğitim Projesi)

Bu repo, Python ile web scraping ve temel web tarayıcı (crawler) mantığını öğrenmek için adım adım geliştirilmiş bir projedir.  
Amaç, önce en basit seviyeden başlayarak sonra multi-threading kullanarak daha hızlı ve gelişmiş bir tarayıcı oluşturmaktır.

Bu proje 3 aşamada evrilmiştir:

---

## 📌 **V1 – Basit Seviye: Tek Sayfadan Link Toplama**

Bu aşamada sadece bir web sayfasına istek gönderilip `<a>` etiketleri içerisindeki `href` değerleri toplanmıştır.

- Sadece tek sayfa taranır  
- `BeautifulSoup` ile HTML parse edilir  
- `http` ile başlayan linkler filtrelenir  
- Basit, giriş seviyesi scraping örneğidir  

Kodun amacı: **Web scraping mantığını anlamak.**

---

## 📌 **V2 – Orta Seviye: Threadsiz Çok Sayfa Tarayıcısı**

Bu aşamada:

- Ana sayfadaki linkler toplanır  
- Bulunan her linke tekrar istek gönderilir  
- Her sayfadaki linkler tek tek çıkarılır  
- Duplicate (tekrar eden) linkler temizlenir  
- Tüm işlem *tek thread* üzerinde yapılır → yavaştır  

Bu sürüm, gerçek bir tarayıcının çalışma mantığını gösterir ancak performans düşüktür.

Kodun amacı:  
**Çoklu sayfa taramayı öğrenmek ve crawler mantığını kavramak.**

---

## 📌 **V3 – Gelişmiş Seviye: Multi-thread Web Tarayıcı (Hızlı)**

Bu aşama projeyi hızlandırmak için çok iş parçacığı (thread) kullanır.

Yapılan geliştirmeler:

- Ana sayfadaki linkler toplanır  
- Her link için ayrı bir thread oluşturulur  
- Thread’ler aynı anda çalışarak çok daha hızlı tarama yapar  
- `threading.Lock()` ile thread-safe liste yazımı sağlanır  
- Duplicate linkler `dict.fromkeys()` ile temizlenir  
- Süre ölçümü eklenmiştir (`time()`)

Bu sürüm, **gerçek bir web tarayıcısının performanslı versiyonudur.**

Kodun amacı:  
**Multi-threading mantığını öğrenmek ve web tarayıcısını hızlandırmak.**

---

## 🛠️ Kullanılan Teknolojiler

| Teknoloji | Açıklama |
|----------|----------|
| `requests` | HTTP istekleri için |
| `BeautifulSoup (bs4)` | HTML parse etmek için |
| `threading` | Paralel tarama yapmak için |
| `time` | Basit süre ölçümü için |

---

## 🚀 Çalıştırmak İçin

1. Gerekli paketleri yükleyin:
   ```bash
   pip install requests beautifulsoup4
   ```
2) Projeyi bilgisayarınıza indirin

GitHub üzerinden:
```bash
git clone https://github.com/znuzhg/web-link-toplayici.git
```

veya ZIP olarak indirip klasöre çıkarabilirsiniz.

3) Proje klasörüne gidin
```bash
cd REPO_ADI
```
5) Python dosyasını çalıştırın
```bash
python main.py
```
---
7) Çıktıyı inceleyin
---
Program çalıştığında terminalde:

Toplam bulunan link sayısı

Linklerin kendisi

Tarama süresi (sn)

görüntülenecektir.
---
🎯 Öğrenme Hedefleri
---
Bu proje sayesinde:
---
Web scraping nedir, nasıl yapılır?

HTML nasıl parse edilir?

Linkler nasıl filtrelenir?

Duplicate link nasıl temizlenir?

Crawler nasıl çalışır?

Threading ile performans nasıl artırılır?

Sorularına pratik yanıt veren somut bir proje elde edilmiş oldu.
---
---
📌 Geliştirme Planı (İsteğe Bağlı)
---
İleride projeye şunlar eklenebilir:
---
domain filtering (sadece site içi linkleri tarama)

depth limit (2. seviye, 3. seviye tarama)

robots.txt uyumluluğu

ThreadPoolExecutor ile daha temiz threading

asyncio + aiohttp ile ultra hızlı tarama

JSON / CSV çıktı sistemi
---
---
👤 Geliştiren
Bu proje eğitim amaçlıdır ve Python öğrenme sürecinde adım adım geliştirilmiştir.

Hazırlayan: Znuzhg Onyvxpv
---
