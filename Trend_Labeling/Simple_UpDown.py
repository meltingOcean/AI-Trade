# 파라미터로 받은 판다스 데이터프레임에 일별 상승하락 트렌드 속성을 추가한다.
# 단순히 종가가 다음날에 상승했으면 1, 같거나 하락했으면 -1 로 레이블링한다. 
def simple_updown(self, dataframe): 
    dataframe['pct_change'] = dataframe['Close'].pct_change() # 일별 수익률을 계산
    dataframe.dropna(inplace = True) # 결측치 제거
    dataframe['UD_Trend'] = dataframe['pct_change'].map(lambda x : 1 if x>0 else -1 ) # 가격이 전날 대비 상승했으면 1, 같거나 하락했으면 -1 로 레이블링한다.
    dataframe['UD_Trend'] = dataframe['UD_Trend'].shift(-1) # 다음날 트렌드를 예측해야하므로 다음날 트렌드를 앞으로 한 행 당긴다
    dataframe.dropna(inplace = True) # 결측치 제거
    