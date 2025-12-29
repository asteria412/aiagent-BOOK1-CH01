# 기본 : 데이터 다 읽어오기 
'''
import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string()) 
'''

# 예제 : 특정 칼로리만 뽑아라! (by. 제미나이)
# 400 칼로리 이상의 데이터만 뽑아줌 

import pandas as pd

df = pd.read_csv('data.csv')

# 데이터 걸러내기 (필터링)
# "칼로리(Calories)가 400보다 큰" 운동 기록만 뽑아서 high_cal 변수에
high_cal = df[df['Calories'] > 400]

# 비교 체험: 그냥 print vs to_string()

print("▼ [1] 그냥 print 했을 때 (데이터가 많으면 중간이 ...으로 생략됨)")
print(high_cal)

print("\n" + "="*30 + "\n") # 보기 좋게 구분선 넣기

print("▼ [2] to_string() 썼을 때 (생략 없이 100% 다 보여줌)")
print(high_cal.to_string())