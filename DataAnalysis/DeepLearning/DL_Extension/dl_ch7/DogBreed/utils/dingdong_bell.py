import sys
sys.path.append('/home/jungyujin/workspace/TIL/DataAnalysis/DeepLearning/DL_Extension/api-dingdong')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dingdong import SlackMessenger
from pathlib import Path

def post_dingdong(epoch, log, stack_dataframe):
  dingdong_text = f"train_loss: {log['loss']} \n val_loss: {log['val_loss']} \n train_acc: {log['accuracy']} \n val_acc: {log['val_accuracy']} \n train_top_k_acc: {log['top_k_acc']} \n val_top_k_acc: {log['val_top_k_acc']}"
  dingdong_bell = SlackMessenger()
  dingdong_bell.alarm_msg(title=f"epoch: {epoch}", alarm_text=dingdong_text, colour="#F7DC6F")
  
  sns.set()
  plt.figure(figsize=(20, 8))
  
  plt.subplot(1, 2, 1)
  plt.title('Loss')
  plt.plot('epoch', 'loss', data=stack_dataframe, label='train_loss')
  plt.plot('epoch', 'val_loss', data=stack_dataframe, label='val_loss')
  plt.legend(loc='upper right')
  
  plt.subplot(1, 2, 2)
  plt.title('Accuracy')
  plt.plot('epoch', 'accuracy', data=stack_dataframe, label='train_acc')
  plt.plot('epoch', 'val_accuracy', data=stack_dataframe, label='val_acc')
  plt.legend(loc='lower right')
  
  plt.savefig('./saved/dingdong.png', facecolor='#eeeeee', bbox_inches='tight')
  dingdong_image_path = f'{Path.cwd()}/saved/dingdong.png'
  dingdong_bell.send_file(file_title=f'epoch{epoch}_dingdong', file_path=dingdong_image_path)
