
#=======================Updated=========================

# @title Start Server **using ngrok**
# @markdown This cell will start the server, the first time that you run it will download the models, so it can take a while (~1-2 minutes)

# @markdown ---
# @markdown You'll need a ngrok account, but <font color=green>**it's free**</font> and easy to create!
# @markdown ---
# @markdown **1** - Create a <font color=green>**free**</font> account at [ngrok](https://dashboard.ngrok.com/signup) or **login with Google/Github account**\
# @markdown **2** - If you didn't logged in with Google/Github, you will need to **verify your e-mail**!\
# @markdown **3** - Click [this link](https://dashboard.ngrok.com/get-started/your-authtoken) to get your auth token, and place it here:
Token = '2eBYUmrtlxKX2SF84pOI7YSiGwo_4unsK1zCnHq1i2RNuZte3' # @param {type:"string"}
# @markdown **4** - *(optional)* Change to a region near to you or keep at United States if increase latency\
# @markdown `Default Region: ap - Asia/Pacific (Singapore)`
Region = "ap - Asia/Pacific (Singapore)" # @param ["ap - Asia/Pacific (Singapore)", "au - Australia (Sydney)","eu - Europe (Frankfurt)", "in - India (Mumbai)","jp - Japan (Tokyo)","sa - South America (Sao Paulo)", "us - United States (Ohio)"]

#@markdown **5** - *(optional)* Other options:
ClearConsole = True  # @param {type:"boolean"}
Play_Notification = False  # @param {type:"boolean"}

# ---------------------------------
# DO NOT TOUCH ANYTHING DOWN BELOW!
# ---------------------------------


from pyngrok import conf, ngrok
MyConfig = conf.PyngrokConfig()
MyConfig.auth_token = Token
MyConfig.region = Region[0:2]
#conf.get_default().authtoken = Token
#conf.get_default().region = Region
conf.set_default(MyConfig);

import subprocess, threading, time, socket, urllib.request
PORT = 8000

from pyngrok import ngrok
ngrokConnection = ngrok.connect(PORT)
public_url = ngrokConnection.public_url

from IPython.display import clear_output
from IPython.display import Audio, display
def play_notification_sound():
    display(Audio(url='https://raw.githubusercontent.com/hinabl/rmvpe-ai-kaggle/main/custom/audios/notif.mp3', autoplay=True))


def wait_for_server():
    while True:
        time.sleep(0.5)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', PORT))
        if result == 0:
            break
        sock.close()
    if ClearConsole:
        clear_output()
    print("--------- SERVER READY! ---------")
    print("Your server is available at:")
    print(public_url)
    print("---------------------------------")
    if Play_Notification==True:
      play_notification_sound()

threading.Thread(target=wait_for_server, daemon=True).start()

mainpy=codecs.decode('ZZIPFreireFVB.cl','rot_13')
mainname=codecs.decode('ZZIPFreireFVB','rot_13')
!mv {mainpy} HVoice.py
!sed -i "s/MMVCServerSIO/HVoice/" HVoice.py
!python3 HVoice.py \
  -p {PORT} \
  --https False \
  --content_vec_500 pretrain/checkpoint_best_legacy_500.pt \
  --content_vec_500_onnx pretrain/content_vec_500.onnx \
  --content_vec_500_onnx_on false \
  --hubert_base pretrain/hubert_base.pt \
  --hubert_base_jp pretrain/rinna_hubert_base_jp.pt \
  --hubert_soft pretrain/hubert/hubert-soft-0d54a1f4.pt \
  --nsf_hifigan pretrain/nsf_hifigan/model \
  --crepe_onnx_full pretrain/crepe_onnx_full.onnx \
  --crepe_onnx_tiny pretrain/crepe_onnx_tiny.onnx \
  --rmvpe pretrain/rmvpe.pt \
  --model_dir model_dir \
  --samples samples.json

ngrok.disconnect(ngrokConnection.public_url)