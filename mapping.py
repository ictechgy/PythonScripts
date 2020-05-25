microArray = open("C:\\Users\\USER-PC\\Desktop\\Python Task\\resultsmicroarray.txt", "rt")
id_name = open("C:\\Users\\USER-PC\\Desktop\\Python Task\\ID_NAME.txt", "rt")

result = open("C:\\Users\\USER-PC\\Desktop\\Python Task\\result.txt", "wt")

while(True):
    microLine = microArray.readline()
    if not microLine:
        break
    micro_a_line = microLine.split() 
    quotesID = micro_a_line[0]
    id = quotesID.strip("\"")

    name=""
    while(True):
        a_line = id_name.readline()
        if not a_line:
            name = "unKnown"
            break
        splited_line = a_line.split() 
        if id==splited_line[0]:
            name=splited_line[1] 
            break
    result_line = micro_a_line[0] + "\t" + micro_a_line[1] + "\t" + name + "\n"
    result.writelines(result_line)
    id_name.seek(0)

microArray.close()
id_name.close()
result.close()

'''
현재 이 코드는 시간복잡도가 O(n)이다. 즉 microArray의 줄 수가 늘어날 수록 검색을 해야할 기본값이 늘어나기도 하지만 id_name의 줄 수가 늘어날수록
검색을 해야할 줄 수도 비례적으로 늘어난다.
위에서는 id_name쪽에 선형검색을 실시하는 방식인데, 만약 이 파일이 오름차순/내림차순 정렬되어있었더라면 이진검색을 수행할 수도 있었을 것이다.

또 한가지의 방법은, microArray의 id값과 일치하는 것을 id_name파일에서 찾았을 경우 해당 줄을 삭제시킨다면 이후에 검색하는 것은 시간이 갈수록 빨라질 수 있을 것이다.

또다른 방법들이 있을까?
'''