import numpy as np
import pandas as pd

data = pd.read_csv("C:\\Python37_Project\\20200603\\student.csv")
data['bmi'] = data['weight'] / ((data['height']/100)*(data['height']/100))
filter = data['sex'] == 'male'
df_male = data[filter]
filter2 = data['sex'] == 'female'
df_female = data[filter2]

male_bmi_mean = df_male['bmi'].mean()
female_bmi_mean = df_female['bmi'].mean()

# while True:
#     print("############## 남녀평균 BMI지수 ##############")
#     n = int(input("알고 싶은 평균 BMI지수의 성별을 입력해주세요. 남자(1) 여자(2) : "))
#     if n==1:
#         print(male_bmi_mean)
#     if n==2:
#         print(female_bmi_mean)

