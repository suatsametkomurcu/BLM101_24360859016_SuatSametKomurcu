# BLM101 Dönem Projesi - RLE (Run-Length Encoding)

## Öğrenci Bilgileri
- **Ad Soyad:** Suat Samet Kömürcü
- **Öğrenci No:** 24360859016
- **Bölüm:** Bilgisayar Mühendisliği

## Proje Konusu
Bu projede **Run-Length Encoding (RLE)** yöntemi ile **kayıpsız sıkıştırma** gerçekleştirilmiştir.
RLE; ardışık tekrar eden karakterleri **(tekrar sayısı + karakter)** biçiminde temsil ederek bazı veri türlerinde boyutu azaltmayı hedefler.

## İçerik
- `sunum.pdf` : Proje sunumu (29 sayfa)
- `src/rle.py` : RLE encode/decode uygulaması
- `README.md` : Bu dosya

## Çalıştırma
Python 3 ile çalıştırılır:

```bash
python src/rle.py
```

Program menüsü:
1) Encode (Sıkıştır)  
2) Decode (Aç)  
3) Çıkış

## Örnek
- Girdi: `AAAAABBBCCDAA`
- Encode: `5A3B2C1D2A`
- Decode: `AAAAABBBCCDAA`

## Sıkıştırma Oranı
Kod içinde basit bir metin temelli oran hesaplanır:

- `oran(%) = (1 - encoded_len / original_len) * 100`

Pozitif değer küçülmeyi, negatif değer büyümeyi ifade eder.

## Notlar / Kenar Durumlar
- Boş girdi için encode sonucu boştur.
- Decode formatı hatalıysa (sayı yok, karakter eksik vb.) program hata mesajı verir.
- RLE, özellikle **tekrarın yüksek olduğu** verilerde avantajlıdır; tekrar az ise veri büyüyebilir.

## YouTube Sunum Linki
> Buraya YouTube linkini ekle (Unlisted önerilir): **PASTE_LINK_HERE**

## GitHub Repo
> Repo linkini buraya koy: https://github.com/suatsametkomurcu/BLM101_24360859016_SuatSametKomurcu

## Kaynakça
- BLM101 Dönem Projesi yönergesi (ders dokümanı).
- Veri Depolama ve Sıkıştırma Algoritmaları - RLE Sıkıştırıcı (ders dokümanı).
- Brookshear, J. G. & Brylow, D. (2014). *Computer Science: An Overview (12th Global Edition)*, Bölüm 1.4 ve 1.9.
- Salomon, D. (2007). *Data Compression: The Complete Reference*.
- Wikipedia: Run-length encoding.
- Chatgpt.
- Gemini.
