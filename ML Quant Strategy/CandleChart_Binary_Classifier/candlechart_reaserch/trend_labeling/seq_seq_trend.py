import pandas as pd
import numpy as np
import os
import matplotlib.dates as mdates
from pathlib import Path

def removeOutput(filepath):
    if(Path(filepath)).is_file():
        os.remove(filepath)
    
def seq_seq_trend(csv_path, seq_len, tre_len, gap=0, seq_mode='close_mean', tre_mode='close_mean'):
    print("Creating label . . .")
    print("type : Sequence to Sequence")
    print("sequence_length : {}, trend_sequence_length : {}, gap : {}".format(seq_len, tre_len, gap))
    
    # 데이터프레임으로 일일주가데이터 불러오기, 결측치 제거
    df = pd.read_csv(csv_path, parse_dates=True, index_col=0)
    df.fillna(0)
    df = df[df.Open != 0]
    df.reset_index(inplace=True)
    df['Date'] = df['Date'].map(mdates.date2num) # Y-M-D 포멧에서 num 포멧으로 변경
        
    # 파일을 저장할 디렉토리 명과 파일이름 지정
    filedir = os.getcwd() + '\\dataset\\labeled_data\\'
    filename = "{}_label_seq{}_tseq{}_gap{}.txt".format(csv_path.split('\\')[-1][0:-4], seq_len, tre_len, gap) # ex) KRX_005930_label_seq30_tseq10_gap0
    filepath = filedir + filename
        
    # 디렉토리가 없을시 생성, 같은이름의 파일 제거
    if not os.path.exists(filedir):
        os.makedirs(filedir)
    removeOutput(filepath)

    # 레이블링
    for i in range(0, len(df) - tre_len - seq_len - gap):
        seq_df = df[i : i + seq_len]
        tre_df = df[i + seq_len + gap : i + seq_len + gap + tre_len]
        seq_sum = 0
        tre_sum = 0
        
        for j in range(seq_len):
            seq_sum = seq_sum + seq_df['Close'].iloc[j]
        seq_mean = seq_sum / seq_len
        
        for j in range(tre_len):
            tre_sum = tre_sum + tre_df['Close'].iloc[j]
        tre_mean = tre_sum / tre_len

        tmp_rtn = tre_mean - seq_mean
        
        if tmp_rtn > 0:
            label = 1
        else:
            label = 0
        # 레이블링한 sequence를 한 라인으로 파일에 입력        
        with open(filepath, 'a') as the_file:
            the_file.write("{}--{},{}".format(filename[0:-4], i, label))
            the_file.write("\n")

    print("Create label finished.")
    return filepath