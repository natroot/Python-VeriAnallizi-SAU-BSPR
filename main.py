# 1. Pandas Kütüphanesini İçe Aktarma
import pandas as pd

# 2. CSV Dosyasını Okuma
df_yucel = pd.read_csv('YUCEL_DF.csv')

# 3. Veri Setinin İlk 5 Satırını Görme
print(df_yucel.head())

# 4. Veri Seti ile İlgili Özet Bilgiler
df_yucel.info()

# 5. Pandas ve Python Versiyonlarını Kontrol Etme
print(pd.__version__)  # Pandas versiyonu
import sys
print(sys.version)  # Python versiyonu
