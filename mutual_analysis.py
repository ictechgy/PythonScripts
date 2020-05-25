"""
Created on Thu Jan 10 2019

@author: jinhongAn
상호분석 모듈
"""

#import
import os, shutil

#destination
dir_name = "E:\\sangho"
os.chdir(dir_name)

#file_list
file_list = os.listdir()


#operation
for file_name in file_list:
    print(file_name + "파일에 대해 작업합니다.")
    file = open(file_name, "r")

    content_list = file.readlines()[8:]  #리스트 슬라이싱. 8번인덱스(9번째 줄)부터 끝까지만 남겨둔다.

    number_list = []
    for line in content_list:
        number_list.append(line.split()[6].rstrip(".[A-Z]"))  #메소드 체이닝 + 정규표현식 사용
    
    #121, 382, 387, 391, 392이 number_list에 있는지 확인해야 한다.
    check = {"121", "382", "387", "391", "392"} #집합자료형
    number_set=set(number_list) #해당 파일의 상호작용 숫자값 또한 집합자료형으로 바꿉니다.
    
    if check.intersection(number_set) == check:  #두 집합의 교집합을 보고, check에 해당하는 결과가 나오는지 획인
        shutil.copy2(file_name, "E:\\sangho_result\\Y\\"+file_name)
    else:
        shutil.copy2(file_name, "E:\\sangho_result\\N\\"+file_name)

    file.close()