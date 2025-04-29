# Image Frame CLI

Bu Python script'i, komut satırı arayüzü (CLI) kullanarak resimlerinize özelleştirilebilir çerçeveler eklemenizi sağlar. Çerçeve kalınlığı, saydamlığı, rengi, köşe yuvarlaklığı ve isteğe bağlı gürültü efekti gibi parametreleri ayarlayabilirsiniz.

## Özellikler

*   **Özelleştirilebilir Çerçeve:** Kalınlık, renk ve saydamlık ayarları.
*   **Yuvarlak Köşeler:** Çerçeveye yumuşak köşeler ekleme seçeneği.
*   **Gürültü Efekti:** Çerçeveye doku katmak için gri tonlamalı gürültü ekleme.
*   **Otomatik Dosya Adlandırma:** İşlenen resimler, orijinal adın sonuna `_framed` eklenerek kaydedilir.
*   **CLI Kontrolü:** Tüm ayarlar komut satırı argümanları ile yönetilir.

## Kurulum

1.  **Depoyu Klonlayın (isteğe bağlı):**
    ```bash
    git clone https://github.com/yusufokuducu/ImageditCLI
    cd ImageditCLI
    ```
2.  **Gerekli Kütüphaneleri Yükleyin:**
    Python 3.x ve pip'in kurulu olduğundan emin olun.
    ```bash
    pip install -r requirements.txt
    ```
    Bu komut, `Pillow` ve `numpy` kütüphanelerini yükleyecektir.

## Kullanım

Script'i çalıştırmak için aşağıdaki temel formatı kullanın:

```bash
python frame.py <resim_dosya_yolu> [seçenekler]
```

**Temel Örnek:**

Varsayılan ayarlarla (20px kalınlık, 0.7 saydamlık, 0.1 gürültü, siyah renk, 10px radius) bir resme çerçeve eklemek için:

```bash
python frame.py path/to/your/image.jpg
```

**Gelişmiş Örnek:**

Özelleştirilmiş parametrelerle çerçeve eklemek:

```bash
python frame.py path/to/your/image.png --kalinlik 30 --saydamlik 0.5 --renk 255,0,0 --radius 15 --gurultu 0.05
```

Bu komut, 30 piksel kalınlığında, %50 saydamlıkta, kırmızı renkte, 15 piksel köşe yuvarlaklığına sahip ve 0.05 seviyesinde gürültü içeren bir çerçeve ekler.

## Argümanlar

*   `resim_yolu`: (Zorunlu) İşlenecek resmin dosya yolu.
*   `--kalinlik` veya `-k`: Çerçeve kalınlığı (piksel olarak). Varsayılan: `20`.
*   `--saydamlik` veya `-s`: Çerçeve saydamlığı (0.0 ile 1.0 arasında bir değer). Varsayılan: `0.7`.
*   `--gurultu` veya `-g`: Çerçeveye eklenecek gri tonlamalı gürültü seviyesi (0.0 ile 1.0 arasında bir değer). Varsayılan: `0.1`. Gürültü istemiyorsanız `0` kullanın.
*   `--renk` veya `-r`: Çerçeve rengi (R,G,B formatında, virgülle ayrılmış). Varsayılan: `0,0,0` (siyah). Örnek: `255,128,0` (turuncu).
*   `--radius`: Çerçeve köşelerinin yuvarlaklık yarıçapı (piksel olarak). Varsayılan: `10`. Negatif olamaz.

Script'i argümansız çalıştırırsanız (`python frame.py`), yardım menüsü gösterilir.

## Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen bir "issue" açın veya "pull request" gönderin.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakınız (eğer varsa).
