# yoskfetch

Bu Python programı, çalıştırıldığı ortamın sistem bilgilerini ve ASCII sanatı renkli bir şekilde konsola yazdırır. Sistem bilgilerini daha eğlenceli bir şekilde görselleştirmek isteyenler için geliştirilmiştir.

## [Exe Olarak Kullan](https://github.com/yoskasss/yoskfetch/blob/main/README.md#exe-olarak-kullanma) / / / / / / / [Python Üzerinden Kullan](https://github.com/yoskasss/yoskfetch?tab=readme-ov-file#kullan%C4%B1m)

## Özellikler

- Sistem bilgilerini (işletim sistemi, kernel, cihaz adı vb.) gösterir.
- Çalıştırılma ortamını algılar (örn: `Command Prompt`, `PowerShell`, `.exe`).
- Renkli ASCII sanatını konsola yazdırır.
- Renk seçimini kullanıcı tarafından özelleştirilebilir hale getirir.

## Gereksinimler

- Python 3.7 veya daha yeni bir sürüm
- [Rich](https://github.com/Textualize/rich) kütüphanesi (renkli çıktı için)

Rich kütüphanesini yüklemek için aşağıdaki komutu çalıştırabilirsiniz:
```bash
pip install rich
```
## Kullanım
### Komut Satırından Çalıştırma

Programı çalıştırmak için aşağıdaki komutu kullanabilirsiniz:
```python
python yoskfetch.py [-c <renk>]
```
### Seçenekler

    -c, --color: ASCII art için renk seçimi. Örneğin, red, green, blue, yellow, magenta gibi Rich destekli renkleri kullanabilirsiniz. Varsayılan renk white (beyazdır).

### Örnekler

#### Varsayılan renk ile çalıştırma:
```python
python yoskfetch.py
```
#### Yeşil renk ile çalıştırma:
```python
python yoskfetch.py -c green
```
#### Mavi renk ile çalıştırma:
```python
python yoskfetch.py --color blue
```


# Exe Olarak Kullanma
## [İndirme Linki](https://www.dosya.tc/server/s9u5ar/yoskfetch.zip.html)
[![Kurulum Videosu](https://www.pngrepo.com/png/209296/180/play-button.png)](https://www.youtube.com/watch?v=q3L7W8XrPfw&ab)
