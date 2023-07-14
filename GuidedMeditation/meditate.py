from speaker import *
from names import *



#1
def Dirga_Pranayama():
    print("Dirga Pranayama")
    #speakout(DirgaPranayama)
    print("breath in slowly and breath out slowly".capitalize())
    speakout("let us start the Dirga pranayama")
    speakout("breath in slowly and breath our Slowly")
    for i in range(3):
        print("Cycle  - ",i)
        speakout("breath in slowly")
        counter(3)
        speakout("Breath out Slowly ")
        counter(3)
    return    

#2
def Nadi_Shodana_Pranayama():
    print("Nadi Shodhana Pranayama")
    #speakout(NadiShodanaPranayama)
    print("Close right nostril with right thumb to inhale from left Nostril and vice versa".capitalize())
    speakout("let us start the Nadi shodhana pranayama")
    speakout("close right nossle with right thumb to inhale and vice versa")
    for i in range(3):
        print("Cycle  - ",i)
        speakout("Close Right nossle with right thumb and inhale from left")
        counter(3)
        speakout("Exhale from left nossle")
        counter(3)
    speakout("time to switch")
    
    for i in range(3):
        print("Cycle'  - ",i)
        speakout("Close left nossle with right pinky finger and inhale")
        counter(3)
        speakout("Exhale from right nossle")
        counter(3)
    return     
    
#3
def Anuloma_Viloma_Pranayama():
    print("Anuloma Viloma Pranayama")
    #speakout(AnulomaVilomaPranayama)
    print("Alternative Nostrils breathing along with retention of  breadth".capitalize())
    speakout("let us start the Anuloma Viloma pranayama")
    speakout("Alternative Nostrils breathing along with retention of  breadth")
    for i in range(3):
        print("Cycle  - ",i)
        speakout("close left  nossle and breath in slowly using  right nostril")
        counter(3)
        speakout("hold breath")
        counter(3)
        speakout("close right nosse and  breath out from left nossle")
        counter(3)
        speakout("time to switch")
        speakout("close right  nossle and breath in slowly using right nostril")
        counter(3)
        speakout("hold breath")
        counter(3)
        speakout("close left  nossle and  breath out from right nossle")
        counter(3)
    return    
    
    
#4
def Surya_Bhedana_Pranayama():
    print("Surya Bhedana Pranayama")
    #speakout(SuryaBhedanaPranatama)
    print("Right Nossle Breathing-Close left nostril ,inhale from right nostril - hold by closing both nostrils-breath out from left nostril".capitalize())
    speakout("let us start Surya Bhedana Pranayama")
    speakout("Right Nossle Breathing")
    for i in range(3):
        print("Cycle  - ",i)
        speakout("close left nostril inhale from right nostril")
        counter(3)
        speakout("hold by closing both nostrils ")
        counter(5)
        speakout("breath out from left nostril")
        counter(3)
    return 
            
#5
def Ujjayi_Paranayama():
    print("Ujayyani Pranayama")
    #speakout(UjjayiPranayama)
    print("Ocean Breath,inhale through mouth and hold and exhale through nose".capitalize())
    speakout("let us start Ujjayi pranayama ")
    speakout("Ocean Breath,inhale through mouth and hold and exhale through nose")
    for i in range(3):
        print("Cycle  - ",i)
        speakout("inhale through mouth")
        counter(5)
        speakout("hold ")
        counter(3)
        speakout("exhale through nose")
        counter(3)
    return 



#6
def Bhramari_Pranayama():
    print("Bhramari  Pranayama")
    #speakout(BhrmariPranayama)
    print("Bee Breath,close ears with thumb , place index finger on eyebrows and gently apply pressure on sides of nose")
    speakout("let us start Bhramari  pranayama ")
    speakout("Bee Breath,close ears with thumb , place index finger on eyebrows and gently apply pressure on sides of nose")
    for i in range(2):
        pass
    return 
    
#7
def Sitkar_Pranayama():
    print("Sitkar  Pranayama")
    #spekaout(SitkarPranayama)
    print("Sitkar Pranayama .gently touch upeer nad lower teeth .inhale and exhale from gaps of teeth ".capitalize())
    speakout("Sitkar Pranayama .gently touch upeer nad lower teeth .inhale and exhale from gaps of teeth ")
    for i in range(3):
        print("Cycle  - ",i)
        speakout("inhale form gaps")
        counter(3)
        speakout("exhale from gaps")
        counter(3)
    return
#8
def Bhastrika_Pranayama():
    print("Bhastrika Pranayama")
    #speakout(BhastrikaPranayama)
    print("inhale normally and exhale forcefully by making nasal sound".capitalize())
    speakout("inhale normally and exhale forcefully by making nasal sound")
    for i in range(3):
        print("Cycle  - ",i)
        speakout("inhale")
        counter(3)
        speakout("exhale forcefully")
        counter(2)
    return

#9
def Kapalabhati_Pranayama():
    print("Kapalbhati Pranayama")
    #speakout(KapalabhatiPranayama)
    print("kapala bhati pranayama.inhale normally and exhale by pushing stomach inside".capitalize)
    speakout("kapala bhati pranayama.inhale normally and exhale by pushing stomach inside")
    for i in range(3):
        print("Cycle  - ",i)
        speakout("inhale normally")
        counter(3)
        speakout("exhale by pushing stomach inside")
        counter(3)
    return


#10
def Simhaasana_Pranayama():
    print("Simhaasna Pranayama")
    #speakout(SimhasanaPranayama)
    print(" breath in through nose and breath out making ha sound from mouth".capitalize())
    speakout("let us start simhasana prayanama, breath in through nose and breath out making ha sound from mouth")
    for i in range(3):
        print("Cycle  - ",i)
        speakout("breath in")
        counter(3)
        speakout("breath out making haa sound")
        counter(3)
    return
     
    
"""
def rest():
    speakout("rest started")
    print("rest")
    for i in range(10):
        speakout("rest")
    speakout("let us start ")
    speakout("rest ended")
    return

def in_right_ex_left():
    speakout("Exrecise 1")
    print("1")
    a="close left  nossle inhale from the right Nossle"
    b="close right  nossle exhale from the left nossle"
    for i in range(0,2):
        speakout(a)
        speakout(b) 
    print("1")
    return 

def in_left_ex_right():
    speakout("Exercise 2")
    print("2")
    b="close right nossle inhale from the left Nossle"
    a="close left nossle exhale from the right nossle"
    for i in range(0,2):
        speakout(a)
        speakout(b) 
    print("2")
    return  
    """      