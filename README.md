# yoskfetch

Bu Python programı, çalıştırıldığı ortamın sistem bilgilerini ve ASCII sanatı renkli bir şekilde konsola yazdırır. Sistem bilgilerini daha eğlenceli bir şekilde görselleştirmek isteyenler için geliştirilmiştir.


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
python sistem_bilgisi.py [-c <renk>]
```
### Seçenekler

    -c, --color: ASCII art için renk seçimi. Örneğin, red, green, blue, yellow, magenta gibi Rich destekli renkleri kullanabilirsiniz. Varsayılan renk white (beyazdır).

### Örnekler

#### Varsayılan renk ile çalıştırma:
```python
python sistem_bilgisi.py
```
#### Yeşil renk ile çalıştırma:
```python
python sistem_bilgisi.py -c green
```
#### Mavi renk ile çalıştırma:
```python
python sistem_bilgisi.py --color blue
```


# Exe Olarak Kullanma
