#회귀분석
import pandas as pd
import numpy as np

data = pd.read_csv('./cardata.csv', delimiter=",", encoding="EUC-KR")  #1. 데이터 불러오기 - 인코딩방식을 UTF로 두는 경우 오류 발생
print(data.columns) #데이터에서 칼럼값만 시험출력

#2. 결측값 제거 - replace함수를 사용할 수도 있다. fillna() ->  Replace all NaN elements with specified values.
#data.fillna(0) # 값이 존재하지 않는 부분(NaN)은 0으로 채움
data = data.dropna(axis=0) #결측값이 존재하는 행 제거 <- data 변수에 다시 넣어야 하나?

#3. column의 값들을 영어로 변경
data.rename(columns={"가격":"price", "회사명":"company", "년식":"year", "종류":"type", "연비":"mileage", "마력":"horsepower", "토크":"torque",
 "연료":"fuel", "하이브리드":"hybrid", "배기량":"displacement", "중량":"mass", "변속기":"transmission"}, inplace=True)
print(data.columns) #칼럼 값들을 영어로 변경 후 칼럼값 출력 (이 중 LPG 칼럼값은 변경하지 않음)

''' Tip!
data.columns = ["price", "company", "year", "type", "mileage", "horsepower", "torque", "fuel", "LPG", "hybrid", "displacement", "mass", "transmission"]
를 써서 한번에 column값을 변경해도 된다. 이 때에는 LPG칼럼부분도 추가해주자
'''

#5. 'gasoline' 및 'diesel' column 추가 - 해당 칼럼은 numpy모듈을 이용해 결측값으로 추가한다. (NaN)
data["gasoline"] = np.nan
data["diesel"] = np.nan
print(data) #결과 출력

#6,7번 다른 방식 시도
data['gasoline'] = np.where(data["fuel"]=="가솔린", 1, 0)
data['diesel'] = np.where(data["fuel"]=="디젤", 1, 0)
print(data)

#6, 7. 각 행의 값을 읽어와 fuel 부분의 값에 따른 gasoline 및 diesel 칼럼 값 수정
for i, row in data.iterrows():
    val = row["fuel"]
    if(val=="가솔린"):
        data.loc[i,"gasoline"] = 1
        data.loc[i,"diesel"] = 0
    elif(val=="디젤"):
        data.loc[i,"gasoline"] = 0
        data.loc[i,"diesel"] = 1
    else:   #fuel의 값이 LPG인 경우 gasoline과 diesel 칼럼값을 모두 0으로 변경
        data.loc[i,"gasoline"] = 0
        data.loc[i,"diesel"] = 0

print(data) #결과 확인

#9. fuel 변수 제거. 삭제는 del data["fuel"]을 쓸 수도 있음
data = data.drop(["fuel"], axis=1)
print(data)