# Sudoku Oyunu - Kurulum ve Çalıştırma Rehberi

## 📋 Gereksinimler

- **Python 3.7 veya üzeri** (tkinter genelde Python ile birlikte gelir)
- **Windows/Linux/Mac** işletim sistemi

## 🚀 Hızlı Başlangıç

### 1. Python Kontrolü

Terminal/Command Prompt'ta Python'un yüklü olup olmadığını kontrol edin:

```bash
python --version
```

veya

```bash
python3 --version
```

Eğer Python yüklü değilse: https://www.python.org/downloads/ adresinden indirin.

### 2. Oyunu Çalıştırma

**Windows:**
```bash
cd C:\Users\ASUS\Desktop\465_tp
python sudoku_game.py
```

**Linux/Mac:**
```bash
cd ~/Desktop/465_tp
python3 sudoku_game.py
```

## 🎮 Oyun Nasıl Oynanır?

### İlk Açılış

Oyun açıldığında bir **pencere** görünecek:
- ✅ Grafik arayüz (GUI) ile çalışır
- ✅ Fare ve klavye ile oynanabilir
- ✅ Gerçek zamanlı geri bildirim

### Oyun Arayüzü

```
┌─────────────────────────────────────────────────┐
│  [3x3▼] [Easy▼] [Algorithm▼]  [Butonlar]     │
├─────────────────────────────────────────────────┤
│                                                 │
│              SUDOKU TAHTASI                    │
│            (9x9 veya 3x3 grid)                 │
│                                                 │
│    [1] [2] [3]  │  [4] [5] [6]  │  [7] [8] [9]│
│    [4] [5] [6]  │  [7] [8] [9]  │  [1] [2] [3]│
│    [7] [8] [9]  │  [1] [2] [3]  │  [4] [5] [6]│
│    ────────────┼───────────────┼──────────────│
│    ...                                         │
│                                                 │
├─────────────────────────────────────────────────┤
│ Status: Ready to play!                         │
│ Metrics: Runtime: 0.00s | Nodes: 0             │
└─────────────────────────────────────────────────┘
```

### Adım Adım Oynama

#### 1️⃣ Yeni Bulmaca Oluştur

1. **Board Size** menüsünden seçin:
   - `3x3` = Mini Sudoku (kolay, başlangıç için)
   - `9x9` = Standart Sudoku

2. **Difficulty** menüsünden seçin:
   - `Easy` = Kolay (%50 dolu)
   - `Medium` = Orta (%35 dolu)
   - `Hard` = Zor (%25 dolu)

3. **"New Puzzle"** butonuna tıklayın

#### 2️⃣ Bulmacayı Çöz

**Manuel Çözüm:**
- Boş bir hücreye **fare ile tıklayın**
- **1-9** arası bir sayı yazın (3x3 için 1-3)
- **Enter** tuşuna basın
- Hatalı girişler **kırmızı** renkle gösterilir

**İpucu Alma:**
1. Boş bir hücreye tıklayın
2. **"Get Hint"** butonuna tıklayın
3. Seçili algoritma size bir değer önerir

**Otomatik Çözüm:**
1. **Algorithm** menüsünden bir algoritma seçin
2. **"Solve"** butonuna tıklayın
3. Algoritma bulmacayı çözer

#### 3️⃣ Algoritma Karşılaştırma

- **"Compare Algorithms"** butonuna tıklayın
- Üç algoritma da çalışır ve sonuçlar gösterilir:
  - Hangi algoritma daha hızlı?
  - Kaç düğüm ziyaret edildi?
  - Kaç backtrack yapıldı?

### Kontroller

| Tuş/Aksiyon | Açıklama |
|------------|----------|
| **Fare tıklama** | Hücre seçme |
| **1-9 tuşları** | Sayı girme |
| **Enter** | Değeri onaylama |
| **Backspace/Delete** | Hücreyi temizleme |
| **Tab** | Sonraki hücreye geçme |

### Butonlar

| Buton | Açıklama |
|-------|----------|
| **New Puzzle** | Yeni bulmaca oluştur |
| **Get Hint** | Seçili hücre için ipucu al |
| **Solve** | Seçili algoritma ile çöz |
| **Compare Algorithms** | Tüm algoritmaları karşılaştır |
| **Clear** | Tahtayı sıfırla |
| **Check** | Çözümü kontrol et |

## 🎯 Algoritma Seçimi

### Constraint Propagation
- ✅ En hızlı
- ✅ Basit bulmacalar için ideal
- ⚠️ Zor bulmacaları tam çözemeyebilir

### AC-3
- ✅ Orta hız
- ✅ Orta zorlukta bulmacalar için iyi
- ✅ Domain azaltma yapar

### Backtracking
- ✅ En güçlü
- ✅ Tüm bulmacaları çözebilir
- ⚠️ Zor bulmacalarda yavaş olabilir

## 💡 İpuçları

1. **Başlangıç için**: 3x3 Easy ile başlayın
2. **Öğrenmek için**: Farklı algoritmaları deneyin
3. **Performans için**: "Compare Algorithms" kullanın
4. **Hata kontrolü**: Kırmızı hücreler çakışan değerleri gösterir

## ❓ Sorun Giderme

### Oyun açılmıyor

**Hata:** `ModuleNotFoundError: No module named 'tkinter'`

**Çözüm:**
- Linux'ta: `sudo apt-get install python3-tk`
- Mac'te: Python'u yeniden yükleyin
- Windows'ta: Genelde sorun olmaz

### Python bulunamıyor

**Hata:** `'python' is not recognized`

**Çözüm:**
- `python3` deneyin
- Python PATH'e eklenmiş mi kontrol edin

### Pencere görünmüyor

**Çözüm:**
- Başka bir pencerenin arkasında olabilir
- Taskbar'da kontrol edin
- Yeniden başlatın

## 📊 Örnek Oyun Akışı

1. ✅ Oyunu başlat: `python sudoku_game.py`
2. ✅ 9x9, Easy seç
3. ✅ "New Puzzle" tıkla
4. ✅ Birkaç hücreyi manuel doldur
5. ✅ "Get Hint" ile ipucu al
6. ✅ "Compare Algorithms" ile karşılaştır
7. ✅ "Solve" ile otomatik çöz
8. ✅ "Check" ile kontrol et

## 🎨 Görsel Özellikler

- ✅ **Renkli hücreler**: 
  - Beyaz = Boş/Doğru
  - Gri = Orijinal (değiştirilemez)
  - Kırmızı = Hatalı/Çakışan
- ✅ **Gerçek zamanlı geri bildirim**
- ✅ **Metrik gösterimi**: Algoritma performansı

## 📝 Notlar

- Oyun **pencere içinde** çalışır (GUI)
- **SFML kullanılmıyor**, tkinter kullanılıyor (Python standart kütüphanesi)
- Tüm özellikler **pencerede** mevcut
- **Fare ve klavye** ile tam kontrol

## 🎓 Eğitim Amaçlı

Bu oyun SENG 465 dersi için yapılmıştır ve şunları gösterir:
- Constraint Satisfaction Problem (CSP) çözümü
- Üç farklı AI algoritması
- Algoritma performans karşılaştırması
- Oyun geliştirme teknikleri

