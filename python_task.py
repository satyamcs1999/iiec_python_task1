import pyttsx3
import os

print("#############################################################")
print("                    Service Provider Bot")
print("#############################################################")
pyttsx3.speak("Welcome")

while True:
  print("Type what you want me to do : ", end='')
  requirement = input()
  
  if ("run" in requirement) and ("chrome" in p):
    os.system("chrome")
    
  elif (("run" in requirement) or ("execute" in requirement)) and (("notepad" in requirement) or ("editor" in requirement)):
    os.system("notepad")
    
  elif (("run" in requirement) and ("player" in requirement) and ("media" in requirement)):
    os.system("wmplayer")
    
  elif (("run" in requirement) or ("execute" in requirement)) and (("notepad++" in requirement) or ("editor" in requirement)):
    os.system("notepad++")
    
  elif (("run" in requirement) or ("execute" in requirement)) and (("ie" in requirement) or ("internet explorer" in requirement)):
    os.system("iexplore")
    
  elif (("run" in requirement) or ("execute" in requirement)) and (("putty" in requirement) or ("PuTTY" in requirement)):
    os.system("putty")
   
  elif (("start" in requirement) or ("run" in requirement)) and (("adobe reader" in requirement) or ("Adobe Reader" in requirement)):
    os.system("AcroRd32")
    
  elif (("start" in requirement) or ("run" in requirement)) and (("DOSBox" in requirement) or ("dosbox" in requirement)):
    os.system("DOSBox")
    
  elif (("start" in requirement) or ("run" in requirement)) and (("Edge" in requirement) or ("Microsoft Edge" in requirement) or("microsoft edge" in requirement)):
    os.system("msedge")

  elif (("start" in requirement) or ("run" in requirement)) and (("teamviewer" in requirement) or ("TeamViewer" in requirement)):
    os.system("TeamViewer")

  elif (("start" in requirement) or ("run" in requirement)) and (("word" in requirement) or ("Word" in requirement) or ("MS Word" in requirement) or ("Microsoft Word" in requirement)):
    os.system("start winword")
    
  elif (("start" in requirement) or ("run" in requirement)) and (("powerpoint" in requirement) or ("Powerpoint" in requirement) or ("MS Powerpoint" in requirement) or ("Microsoft Powerpoint" in requirement)):
    os.system("start powerpnt")
    
  elif (("start" in requirement) or ("run" in requirement)) and (("excel" in requirement) or ("Excel" in requirement) or ("MS Excel" in requirement) or ("Microsoft Excel" in requirement)):
    os.system("start excel")
  
  elif (("start" in requirement) or ("run" in requirement) or ("open" in requirement)) and (("control panel" in requirement) or ("Control Panel" in requirement)):
    os.system("control panel")
    
  elif (("start" in requirement) or ("run" in requirement) or ("open" in requirement)) and (("camera" in requirement) or ("Camera" in requirement)):
    os.system("start microsoft.windows.camera:")
    
  elif (("start" in requirement) or ("run" in requirement)) and (("bluetooth" in requirement) or ("Bluetooth" in requirement)):
    os.system("fsquirt")
    
  elif (("listen" in requirement) or ("start" in requirement) or ("open" in requirement)) and (("spotify" in requirement) or ("Spotify" in requirement) or ("music" in requirement)):
    os.system("start spotify.exe")
    
  elif (("start" in requirement) or ("open" in requirement)) and (("whatsapp" in requirement) or ("WhatsApp" in requirement) or ("Whatsapp" in requirement)):
    os.system("start whatsapp:")
    
  elif (("start" in requirement) or ("run" in requirement)) and (("slack" in requirement) or ("Slack" in requirement)):
    os.system("start slack:")
    
  elif (("start" in requirement) or ("run" in requirement)) and (("todoist" in requirement) or ("Todoist" in requirement)):
    os.system("start todoist:")

  elif (("start" in requirement) or ("run" in requirement)) and (("vscode" in requirement) or ("VSCode" in requirement) or ("Visual Studio Code" in requirement)):
    os.system("start vscode:")    
    
  elif (("exit" in requirement) or ("quit" in requirement)):
    break
  
  else:
    print("Option currently unavailable")
  
  