"""
Created on Sun Jan 13 2019

@author: jinhongAn
"""

def bisearch(list, n):  #숫자로 구성된 list를 매개변수로 받는다. n은 찾고자 하는 값
    list.sort() #list를 오름차순으로 정렬
    num = len(list) #list의 요소개수 얻기
    
    pl = 0
    pr = num -1
    
    while(pl<=pr):
        pc = (pl + pr)/2
        x = list[pc]
        if n < x:
            pr = pc-1
        elif x < n:
            pl = pc+1
        else:
            return pc   #일치하는 값을 찾은 경우 해당 인덱스번호를 반환
    return -1 #일치하는 값을 찾지 못한 경우 -1을 반환

#이진검색 함수를 위와같이 만들었으나 파이썬에서는 bisect모듈에서 bisect라는 함수를 제공함.
#또한 C언어에서는 위의 방식보다 다소 복잡하게 만들어야 함

import os, shutil

dir_name = "E:\\sangho"
os.chdir(dir_name)

file_list = os.listdir()

for file_name in file_list:
    print(file_name + "파일에 대해 작업합니다.")
    file = open(file_name, "r")

    content_list = file.readlines()[8:]  

    number_list = []
    for line in content_list:
        number_list.append(int(line.split()[6].rstrip(".[A-Z]")))
    
    check_list = [121, 382, 387, 391, 392]

    for check in check_list:
        flag = bisearch(number_list, check)
        if flag == -1:
            shutil.copy2(file_name, "E:\\sangho_result\\N\\"+file_name)
            break
    if flag != -1: shutil.copy2(file_name, "E:\\sangho_result\\Y\\"+file_name)

    file.close()
