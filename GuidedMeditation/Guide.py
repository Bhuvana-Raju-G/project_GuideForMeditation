import datetime
from speaker import *
from meditate import *

today=datetime.date.today()
print(today)
speakout("today's date is ")
speakout(today)

lis=[Dirga_Pranayama(),Nadi_Shodana_Pranayama(),Anuloma_Viloma_Pranayama(),Surya_Bhedana_Pranayama(),Ujjayi_Paranayama(),Bhramari_Pranayama(),Simhaasana_Pranayama(),Kapalabhati_Pranayama(),Bhastrika_Pranayama(),Sitkar_Pranayama()]
p_count=1
for i in lis:
    print("Pranayama ",p_count)
    i
    p_count+1