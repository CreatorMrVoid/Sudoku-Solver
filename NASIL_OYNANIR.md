# Sudoku Oyunu - Nasıl Oynanır?

## Hızlı Başlangıç

### Oyunu Çalıştırma

1. Terminal/Command Prompt'u açın
2. Proje klasörüne gidin:
   ```bash
   cd C:\Users\ASUS\Desktop\465_tp
   ```
3. Oyunu başlatın:
   ```bash
   python sudoku_game.py
   ```

### Oyun Arayüzü

Oyun açıldığında bir pencere görünecek:
- **Üst kısım**: Kontrol paneli (boyut, zorluk, algoritma seçimi)
- **Orta kısım**: Sudoku tahtası (9x9 veya 3x3 grid)
- **Alt kısım**: Durum mesajları ve algoritma metrikleri

## Nasıl Oynanır?

### 1. Yeni Bulmaca Oluşturma

- **Board Size**: 3x3 (mini) veya 9x9 (standart) seçin
- **Difficulty**: Easy, Medium veya Hard seçin
- **"New Puzzle"** butonuna tıklayın

### 2. Bulmaca Çözme

**Manuel Çözüm:**
- Boş hücrelere tıklayın
- 1-9 arası sayı girin (3x3 için 1-3)
- Enter tuşuna basın
- Hatalı girişler kırmızı renkle vurgulanır

**İpucu Alma:**
1. Boş bir hücreye tıklayın
2. **"Get Hint"** butonuna tıklayın
3. Seçili algoritma size bir değer önerir

**Otomatik Çözüm:**
- **Algorithm** menüsünden bir algoritma seçin:
  - Constraint Propagation
  - AC-3
  - Backtracking
- **"Solve"** butonuna tıklayın
- Algoritma bulmacayı çözer ve metrikleri gösterir

### 3. Algoritma Karşılaştırma

- **"Compare Algorithms"** butonuna tıklayın
- Üç algoritma da çalışır ve sonuçlar karşılaştırılır:
  - Çözme süresi
  - Ziyaret edilen düğüm sayısı
  - Backtrack sayısı
  - Domain azaltma sayısı

### 4. Diğer Özellikler

- **Clear**: Tahtayı orijinal haline döndürür
- **Check**: Mevcut çözümün doğru olup olmadığını kontrol eder

## Kontroller

| Özellik | Açıklama |
|---------|----------|
| **Fare ile tıklama** | Hücre seçme |
| **Klavye girişi** | Sayı girme (1-9) |
| **Enter** | Değeri onaylama |
| **Backspace/Delete** | Hücreyi temizleme |

## Zorluk Seviyeleri

- **Easy**: %50 hücre dolu (kolay)
- **Medium**: %35 hücre dolu (orta)
- **Hard**: %25 hücre dolu (zor)

## Algoritma Seçimi

1. **Constraint Propagation**: Hızlı, basit bulmacalar için ideal
2. **AC-3**: Orta zorlukta bulmacalar için iyi
3. **Backtracking**: En güçlü, tüm bulmacaları çözebilir

## İpuçları

- Önce kolay bulmacalarla başlayın
- Farklı algoritmaları deneyin
- "Compare Algorithms" ile performans farklarını görün
- Hatalı girişler kırmızı renkle gösterilir

## Sorun Giderme

**Oyun açılmıyor:**
- Python 3.7+ yüklü olduğundan emin olun
- tkinter yüklü olmalı (genelde Python ile gelir)

**Hata mesajı alıyorsanız:**
```bash
python --version  # Python versiyonunu kontrol edin
```

## Ekran Görüntüleri

Oyun penceresi şu şekilde görünür:
```
┌─────────────────────────────────────────┐
│ [3x3▼] [Easy▼] [Algorithm▼] [Buttons] │
├─────────────────────────────────────────┤
│                                         │
│          SUDOKU TAHTASI                │
│         (9x9 veya 3x3 grid)            │
│                                         │
├─────────────────────────────────────────┤
│ Status: Ready to play!                 │
│ Metrics: No metrics available          │
└─────────────────────────────────────────┘
```

