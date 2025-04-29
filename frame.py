from PIL import Image, ImageDraw, ImageFilter
import argparse
import numpy as np
import os
import sys

def cerceve_ekle(resim_yolu, cerceve_kalinligi=20, saydamlik=0.7, gurutu_seviyesi=0.1, renk=(0, 0, 0), radius=10):
    """
    Bir resme çerçeve ekler ve kaydedir.

    Args:
        resim_yolu (str): Resmin yolu.
        cerceve_kalinligi (int): Çerçevenin kalınlığı (piksel).
        saydamlik (float): Çerçevenin saydamlık oranı (0.0 - 1.0).
        gurutu_seviyesi (float): Çerçevenin gürültü seviyesi (0.0 - 1.0).
        renk (tuple): RGB renk değeri (0-255 arası)
        radius (int): Köşelerin yuvarlaklık derecesi
    
    Returns:
        str: Kaydedilen dosyanın yolu
    """
    try:
        # Resmi aç
        resim = Image.open(resim_yolu)
        
        # RGB modunda mı kontrol et, değilse dönüştür
        if resim.mode != "RGB":
            resim = resim.convert("RGB")
        
        # Çerçeve ölçülerini hesapla
        genislik, yukseklik = resim.size
        cerceve_genislik = genislik + 2 * cerceve_kalinligi
        cerceve_yukseklik = yukseklik + 2 * cerceve_kalinligi
        
        # RGBA modunda çerçeve oluştur
        cerceve = Image.new("RGBA", (cerceve_genislik, cerceve_yukseklik), (0, 0, 0, 0))
        cerceve_draw = ImageDraw.Draw(cerceve)
        
        # Yarı saydamlık için alfa değeri hesapla
        alpha = int(255 * saydamlik)
        renk_with_alpha = (renk[0], renk[1], renk[2], alpha)
        
        # Yumuşak köşeler için yuvarlak dikdörtgen çiz
        cerceve_draw.rounded_rectangle(
            (0, 0, cerceve_genislik, cerceve_yukseklik),
            radius=radius,  # Köşe yarıçapı
            fill=renk_with_alpha,
            outline=None
        )
        
        # Gürültü efekti ekle (sadece eğer gürültü seviyesi > 0 ise)
        if gurutu_seviyesi > 0:
            cerceve_numpy = np.array(cerceve)
            # Sadece RGB kanallarına gürültü ekle, alpha kanalını koru
            for i in range(3):  # RGB kanalları için döngü
                gurultu_kanal = np.random.normal(0, gurutu_seviyesi * 255, (cerceve_yukseklik, cerceve_genislik)).astype(np.int16)
                # Mevcut değerlere ekle ve sınırla (0-255)
                cerceve_numpy[:, :, i] = np.clip(cerceve_numpy[:, :, i].astype(np.int16) + gurultu_kanal, 0, 255).astype(np.uint8)
            
            cerceve = Image.fromarray(cerceve_numpy)
        
        # RGB formatında bir sonuç resmi oluştur
        sonuc = Image.new("RGB", (cerceve_genislik, cerceve_yukseklik), (255, 255, 255))
        
        # Önce çerçeveyi ekle (RGBA)
        sonuc.paste(cerceve, (0, 0), cerceve)
        
        # Sonra orijinal resmi ekle
        sonuc.paste(resim, (cerceve_kalinligi, cerceve_kalinligi))
        
        # Dosya adını ve uzantısını ayır
        dosya_adi, dosya_uzantisi = os.path.splitext(resim_yolu)
        
        # Yeni dosya adını oluştur
        yeni_dosya_adi = f"{dosya_adi}_framed{dosya_uzantisi}"
        
        # Sonucu kaydet
        sonuc.save(yeni_dosya_adi)
        print(f"Çerçeve eklendi ve kaydedildi: {yeni_dosya_adi}")
        return yeni_dosya_adi
        
    except FileNotFoundError:
        print(f"Hata: Resim dosyası bulunamadı: {resim_yolu}")
        return None
    except Exception as e:
        print(f"Hata: İşlem sırasında bir hata oluştu: {e}")
        return None

def main():
    # Komut satırı argümanlarını tanımla
    parser = argparse.ArgumentParser(description='Resimlere çerçeve ekleyen program.')
    parser.add_argument('resim_yolu', type=str, help='İşlenecek resmin dosya yolu')
    parser.add_argument('--kalinlik', '-k', type=int, default=20, help='Çerçeve kalınlığı (piksel olarak, varsayılan: 20)')
    parser.add_argument('--saydamlik', '-s', type=float, default=0.7, help='Çerçeve saydamlığı (0.0-1.0 arası, varsayılan: 0.7)')
    parser.add_argument('--gurultu', '-g', type=float, default=0.1, help='Gürültü seviyesi (0.0-1.0 arası, varsayılan: 0.1)')
    parser.add_argument('--renk', '-r', type=str, default='0,0,0', help='Çerçeve rengi (R,G,B formatında, varsayılan: 0,0,0)')
    parser.add_argument('--radius', type=int, default=10, help='Köşe yuvarlaklığı (piksel olarak, varsayılan: 10)')
    
    # Eğer hiç argüman verilmemişse yardım göster
    if len(sys.argv) == 1:
        parser.print_help()
        return
        
    # Argümanları ayrıştır
    args = parser.parse_args()
    
    try:
        # Renk değerlerini ayrıştır
        renk = tuple(map(int, args.renk.split(',')))
        if len(renk) != 3:
            raise ValueError("Renk formatı doğru değil. Örnek: 255,0,0 (kırmızı)")
            
        # Değerleri kontrol et
        if not (0 <= args.saydamlik <= 1):
            raise ValueError("Saydamlık değeri 0.0 ile 1.0 arasında olmalıdır.")
        if not (0 <= args.gurultu <= 1):
            raise ValueError("Gürültü seviyesi 0.0 ile 1.0 arasında olmalıdır.")
        if args.kalinlik <= 0:
            raise ValueError("Çerçeve kalınlığı pozitif bir sayı olmalıdır.")
        if args.radius < 0:
            raise ValueError("Köşe yuvarlaklığı negatif olamaz.")
        
        # Çerçeve ekle
        cerceve_ekle(args.resim_yolu, args.kalinlik, args.saydamlik, args.gurultu, renk, args.radius)
        
    except ValueError as e:
        print(f"Hata: {e}")
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")

if __name__ == "__main__":
    main()