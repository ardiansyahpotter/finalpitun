#=================Updated=================
# @title **[1]** Clone repository and install dependencies
# @markdown This first step will download the latest version of Voice Changer and install the dependencies. **It can take some time to complete.**
import os
import time
import subprocess
import threading
import shutil
import base64
import codecs



#@markdown ---
# @title **[Optional]** Connect to Google Drive
# @markdown Using Google Drive can improve load times a bit and your models will be stored, so you don't need to re-upload every time that you use.

Use_Drive=True #@param {type:"boolean"}
notebook_env=0
# Check what platform the notebook is running on
if os.path.exists('/content'):
  notebook_env=1
  print("Welcome to ColabMod")
  from google.colab import drive

elif os.path.exists('/kaggle/working'):
  notebook_env=3
  print("Welcome to Kaggle Mod")
else:
  notebook_env=3
  print("Welcome!")



externalgit=codecs.decode('uggcf://tvguho.pbz/j-bxnqn/ibvpr-punatre.tvg','rot_13')
rvctimer=codecs.decode('uggcf://tvguho.pbz/uvanoy/eipgvzre.tvg','rot_13')
pathloc=codecs.decode('ibvpr-punatre','rot_13')

from IPython.display import clear_output, Javascript

def update_timer_and_print():
    global timer
    while True:
        hours, remainder = divmod(timer, 3600)
        minutes, seconds = divmod(remainder, 60)
        timer_str = f'{hours:02}:{minutes:02}:{seconds:02}'
        print(f'\rTimer: {timer_str}', end='', flush=True)  # Print without a newline
        time.sleep(1)
        timer += 1
timer = 0
threading.Thread(target=update_timer_and_print, daemon=True).start()

!pip install colorama --quiet
from colorama import Fore, Style

print(f"{Fore.CYAN}> Cloning the repository...{Style.RESET_ALL}")
!git clone --depth 1 $externalgit &> /dev/null
if Use_Drive==True:
  if not os.path.exists('/content/drive'):
    drive.mount('/content/drive')

    !mkdir -p /content/drive/MyDrive/voice-changer/server/model_dir
    !rm -rf /content/voice-changer/server/model_dir

    drive_dir = "/content/drive/MyDrive/voice-changer/server/model_dir"
    colab_dir = "/content/voice-changer/server/model_dir"
    time.sleep(5)

    os.symlink(drive_dir,colab_dir,True)
  # %cd /content/drive/MyDrive
print(f"{Fore.GREEN}> Successfully cloned the repository!{Style.RESET_ALL}")
%cd $pathloc/server/

#custom sub
if notebook_env==1:
  !sed -i "s/-.-.-.-/Colab.Mod/" '../client/demo/dist/assets/gui_settings/version.txt'
elif notebook_env==2:
  !sed -i "s/-.-.-.-/Kaggle.Mod/" '../client/demo/dist/assets/gui_settings/version.txt'
elif notebook_env==3:
  !sed -i "s/-.-.-.-/Online.Mod/" '../client/demo/dist/assets/gui_settings/version.txt'
else:
  !sed -i "s/-.-.-.-/Online.Mod/" '../client/demo/dist/assets/gui_settings/version.txt'
  print("Notebook Env Not Found")


print(f"{Fore.CYAN}> Installing libportaudio2...{Style.RESET_ALL}")
!apt-get -y install libportaudio2 -qq
!sudo apt-get update
!sudo apt-get install portaudio19-dev -y

!sed -i '/torch==/d' requirements.txt
!sed -i '/torchaudio==/d' requirements.txt
!sed -i '/numpy==/d' requirements.txt

# Enabled FCPE
# !sed -i '/from voice_changer.RVC.pitchExtractor.RMVPEPitchExtractor import RMVPEPitchExtractor/a\from voice_changer.RVC.pitchExtractor.FcpePitchExtractor import FcpePitchExtractor' voice_changer/RVC/pitchExtractor/PitchExtractorManager.py

print(f"{Fore.CYAN}> Installing pre-dependencies...{Style.RESET_ALL}")
# Install dependencies that are missing from requirements.txt and pyngrok
!pip install faiss-gpu fairseq pyngrok --quiet
!pip install pyworld --no-build-isolation --quiet
# Install webstuff
import asyncio
import re
!pip install gdown
!pip install torchfcpe
print(f"{Fore.CYAN}> Installing dependencies from requirements.txt...{Style.RESET_ALL}")
!pip install -r requirements.txt --quiet
clear_output()
print(f"{Fore.GREEN}> Successfully installed all packages!{Style.RESET_ALL}")