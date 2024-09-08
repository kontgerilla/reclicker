İstediğin scriptler için bir **README.md** dosyası şu şekilde olabilir:

---

# HUNTER Mouse Logger & Repeater

Bu projede iki adet Python scripti bulunmaktadır. İlk script fare tıklamalarını kaydeder ve bir dosyaya yazar. İkinci script ise kaydedilen bu tıklama konumlarına giderek otomatik tıklama işlemi yapar.

## Gereksinimler

Bu scriptler için aşağıdaki Python kütüphanelerine ihtiyacınız var:

- `pynput`: Fare ve klavye olaylarını dinlemek için.
- `colorama`: Konsol çıktısına renk katmak için.

Gerekli kütüphaneleri yüklemek için şu komutları kullanabilirsiniz:

```bash
pip install pynput
pip install colorama
```
ya da
```bash
pip install -r requirements.txt
```

## Kullanım

### 1. **Tıklama Konumlarını Kaydetme**

`mouse_logger.py` adlı ilk script, fare ile yaptığınız tıklamaların konumlarını kaydeder ve `esc` tuşuna basıldığında bu konumları `click_positions.txt` dosyasına yazar.

#### Çalıştırma:

```bash
python mouse_logger.py
```

#### Çalışma Mantığı:
- Fare tıklamaları yakalanır ve tıklanan her bir konum ekranda gösterilir.
- `esc` tuşuna bastığınızda tıklanan tüm konumlar `click_positions.txt` dosyasına kaydedilir.

### 2. **Tıklama Konumlarını Tekrarlama**

`mouse_repeater.py` adlı ikinci script, `click_positions.txt` dosyasından aldığı tıklama konumlarına giderek bu konumlara otomatik olarak sol tıklama yapar. Kullanıcıdan kaç kez tekrar yapılacağı sorulur. `q` tuşuna basıldığında ise script durur.

#### Çalıştırma:

```bash
python mouse_repeater.py
```

#### Çalışma Mantığı:
- `click_positions.txt` dosyasından tıklama konumları okunur.
- Kullanıcı, kaç kez tıklama işleminin tekrar etmesi gerektiğini belirtir.
- Belirlenen sayıda tıklama işlemi gerçekleştirilir.
- `q` tuşuna basıldığında script durur.

### Dosyalar

- **mouse_logger.py**: Fare tıklama konumlarını kaydeden script.
- **mouse_repeater.py**: Kaydedilen konumlara otomatik tıklamalar yapan script.
- **click_positions.txt**: İlk script tarafından kaydedilen ve ikinci script tarafından okunan tıklama konumlarının saklandığı dosya.

## Örnek Kullanım

1. `mouse_logger.py` ile fare tıklamalarını kaydedin.
2. `click_positions.txt` dosyası otomatik olarak oluşturulacak.
3. `mouse_repeater.py` scriptini çalıştırarak, belirtilen konumlara otomatik tıklama yapın.

## Ekstra Bilgiler

- **Çıkış Yapma**: Her iki scriptte de `q` tuşuna basarak çıkış yapabilirsiniz.
- **Log Dosyası**: Fare tıklama konumları ve tıklama işlemleri kaydedildiği dosya: `click_positions.txt`.

---

Bu README dosyası, projeyi başkalarına tanıtmak ve adım adım nasıl kullanılacağını açıklamak için uygundur.