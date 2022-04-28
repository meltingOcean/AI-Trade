import numpy as np
import pandas as pd

import matplotlib.dates as mdates

from PIL import Image
import os
from pathlib import Path
import shutil


def removeOutput(filepath):
    if(Path(filepath)).is_file():
        os.remove(filepath)
        
def candlechart_generator(csv_path, seq_len, tre_len, dimension, use_volume):
    print("Converting ohlc to candlestick")
    
    # 데이터프레임으로 일일주가데이터 불러오기, 결측치 제거
    df = pd.read_csv(csv_path, parse_dates=True, index_col=0)
    df.fillna(0)
    df = df[df.Open !=0]
    df.reset_index(inplace=True)
    df['Date'] = df['Date'].map(mdates.date2num) # Y-M-D 포멧에서 num 포멧으로 변경
    
    # 파일을 저장할 디렉토리 명과 파일이름 지정
    symbol = csv_path.split('\\')[-1][0:-4]
    filedir = os.getcwd() + '\\dataset\\candle_chart\\{}\\seq{}_dim{}_vol{}\\'.format(
                                symbol, seq_len, dimension, use_volume) # ex) seq30_dim536_volFalse
    
    # 디렉토리가 없을시 생성, 이미 디렉토리가 있다면 내용물 삭제하고 다시 생성
    if not os.path.exists(filedir):
        os.makedirs(filedir)
    else:
        shutil.rmtree(filedir)
        os.makedirs(filedir)
    
    for i in range(0, len(df)-seq_len-tre_len):
        pix_data = np.zeros([dimension, dimension, 3], dtype=np.uint8)
        tmp_df = df.iloc[i:i + seq_len]
        seq_upper = np.max([tmp_df['Open'].max(), tmp_df['Close'].max(), tmp_df['High'].max(), tmp_df['Low'].max()]) # 구간 최대 경계값
        seq_lower = np.min([tmp_df['Open'].min(), tmp_df['Close'].min(), tmp_df['High'].min(), tmp_df['Low'].min()]) # 구간 최소 경계값
        seq_differ = seq_upper - seq_lower
        
        for j in range(0, seq_len):
            if tmp_df.iloc[j]['Open'] < tmp_df.iloc[j]['Close']:
                pix_color = [255, 0, 0] # red-color
            else:
                pix_color = [0, 0, 255] # blue-color
                
            high_pos = int(dimension * (tmp_df.iloc[j]['High'] - seq_lower)  / seq_differ)
            low_pos = int(dimension * (tmp_df.iloc[j]['Low'] - seq_lower) / seq_differ)
            pix_data[low_pos:high_pos, 3*j + 1] = pix_color
            
            open_pos = int(dimension * (tmp_df.iloc[j]['Open'] - seq_lower)  / seq_differ)
            close_pos = int(dimension * (tmp_df.iloc[j]['Close'] - seq_lower)  / seq_differ)
            pix_data[np.min([close_pos, open_pos]):np.max([close_pos, open_pos]), [3*j, 3*j+2]] = pix_color
        
        filename = '{}-{}'.format(symbol, i)
        filepath = filedir + filename
            
        image = Image.fromarray(pix_data, 'RGB')
        image.save(filepath+'.png', 'png')
    print("Converting finished")
    
    return filedir
    