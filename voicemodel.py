#@title **[Optional]** Upload a voice model (Run this before running the Voice Changer)
import os
import sys
import json
import requests

model_slot = "2" #@param ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199']

!rm -rf model_dir/$model_slot
#@markdown **[Optional]** Add an icon to the model
icon_link = "https://pbs.twimg.com/profile_images/1744159012294193152/9jxz4UPm_400x400.jpg" #@param {type:"string"}
icon_link = '"'+icon_link+'"'
!mkdir model_dir
!mkdir model_dir/$model_slot
#@markdown Put your model's download link here `(must be a zip file)` only supports **huggingface.co** & **google drive**<br>
model_link = "https://huggingface.co/Stevenojob/furina_JP/blob/main/furina_jp.zip"  #@param {type:"string"}

if model_link.startswith("https://www.weights.gg") or model_link.startswith("https://weights.gg"):
  print("Links from weights.gg is no longer supported.")
  sys.exit()
elif model_link.startswith("https://drive.google.com"):
  model_link = '"'+model_link+'"'
  !gdown $model_link --fuzzy -O model.zip
  print("Model from Drive")
elif model_link.startswith("https://huggingface.co"):
  model_link = model_link
  model_link = '"'+model_link+'"'
  !curl -L $model_link > model.zip
  print("Model from hugginface Link")
else:
  model_link = model_link
  model_link = '"'+model_link+'"'
  !curl -L -O $model_link
  !mv ./*.pth model_dir/$model_slot/
  print('Model(.pth) or a direct model link.')

# Conditionally set the iconFile based on whether icon_link is empty
if icon_link == '""':
    iconFile = ""
    print("icon_link is empty, so no icon file will be downloaded.")
else:
    iconFile = "icon.png"
    !curl -L $icon_link > model_dir/$model_slot/icon.png


!unzip model.zip -d model_dir/$model_slot

!mv model_dir/$model_slot/*/* model_dir/$model_slot/
!rm -rf model_dir/$model_slot/*/
!rm -rf model.zip
#@markdown **Model Voice Convertion Setting**
Tune = 9 #@param {type:"slider",min:-50,max:50,step:1}
Index = 0.7 #@param {type:"slider",min:0,max:1,step:0.1}

param_link = ""
if param_link == "":
  paramset = requests.get("https://pastebin.com/raw/SAKwUCt1").text
  exec(paramset)

clear_output()
print("\033[93mModel with the name of "+model_name+" has been Imported to slot "+model_slot)