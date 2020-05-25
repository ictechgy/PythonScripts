#특정 string 기준으로 파일 분류 
import os

os.chdir("E:\\Splitter")

file = open("split.sdf", "rt")

save_number = 1

context = []
for line in file.readlines():
    context.append(line)
    if line == "$$$$\n":
        f=open(str(save_number)+".sdf", "w")
        for line2 in context:
            f.write(line2)
        f.close()
        save_number+=1
        context = []   #context.clear()

print("작업이 종료되었습니다.")
file.close()