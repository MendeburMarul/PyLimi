from gtts import gTTS
from subprocess import Popen
import random
import playsound
import os
import re
import webbrowser
import smtplib
import subprocess as sp
import main

##################################################################

Lunar = r"C:\Users\mustafa\AppData\Local\Programs\lunarclient\Lunar client.exe"
Edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
Chrome = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

##################################################################

print('Merhabalar, size nasıl yardım edebilirim?')

def komut():
    a = input('girdi> ')
    return a

def yaz(audio_string):
    tts = gTTS(text=audio_string, lang='tr') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(f"limi: {audio_string}") # print what app said
    os.remove(audio_file) # remove audio file

def asistan(komut):

    if 'Merhaba' in komut or 'Gunaydin' in komut or 'Günaydın' in komut:
        greetings = ['merhaba','Sanada iyi günler']
        greet = greetings[random.randint(0,len(greetings)-1)]
        yaz(greet)

    elif 'youtube' in komut:
        search_term = komut.split(" ")[1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        yaz(f'{search_term} için youtube´da bulduklarım')
        
    elif 'THT' in komut or 'THT profilini aç' in komut or 'TurkHackTeam Profili' in komut:
        url = "https://www.turkhackteam.org/members/915491.html"
        webbrowser.get().open(url)
        yaz('Senin için MendeburMarul adlı kullanıcının TurkHackTeam profilini açtım. Burdan TurkHackTeam Forumuna devam edebilirsin')

    elif 'Soyle' in komut or 'Söyle' in komut:
        soz = komut.split(" ")[1]
        yaz(soz)
        
    elif 'Aç' in komut or 'Ac' in komut:
        d_a = komut.split(" ")[1]
        if 'Lunar' in d_a:
            sp.Popen(Lunar)
            yaz('Senin için Lunar Clienti açıyorum.')
            
        if 'Edge' in d_a:
            sp.Popen(Edge)
            yaz('Senin için Edge adlı tarayıcıyı açıyorum.')
            
        if 'Chrome' in d_a:
            sp.Popen(Chrome)
            yaz('Senin için Chrome adlı tarayıcıyı açıyorum.')
                                    
while True:
    asistan(komut())
