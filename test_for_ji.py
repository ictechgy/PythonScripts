import os, string

try:
	os.chdir('E:\\Python\\pdbqt_files') #pdbqt 파일들만 이 디렉토리에 모아놓기
except:
	print("해당 디렉토리가 존재하지 않아서 작업디렉토리를 변경할 수 없습니다.")
	quit() 
	
f_list=os.listdir()

if(not f_list): 
	print("해당 디렉토리에 아무파일도 존재하지 않습니다. 디렉토리 내에 파일이 존재하는지 확인하십시오")
	quit() 

for file in f_list:  
	try:
		f=open(file,"rt") 
		
		context = f.readlines()
	
		if(not context):
			print(file+"파일의 내용이 비어있습니다.")
			continue
		
		line2 = context[1] 
		number_s = line2.split()[3]
		number = int(float(number_s.lstrip('-')))
		

		dest='E:\\Python\\pdbqt_files\\'+str(number)

		if(not os.path.isdir(dest)): 
			os.mkdir(dest)
	
		
		dest+='\\'+file
		make=open(dest,'wt')
		for line in context:
			make.write(line)
		make.close()
		
	except(FileNotFoundError):
		print(file+"파일이 존재하지 않거나 열 수 없습니다. 파일이 있는지 확인하고, 권한을 확인하십시오.")
	except(IndexError):
		print(file+" - 이 파일에 두번째 줄이 존재하지 않거나 split 및 데이터 파싱작업 중 오류가 발생하였습니다.")
	except(ValueError):
		print("데이터값을 정수로 형변환하는 도중 오류가 발생하였습니다. 파일의 값을 확인하십시오. 파일명 : " + file)
	except(OSError):
		print("OS모듈 관련 오류 발생")
	except:
		print("오류 발생. 확인 필요")
	finally:
		if(f is not None):
			f.close	
print("파일 분류 작업 완료.")

#위의 방법은 프로그램 자체적으로 파일의 내용을 복사하도록 만들었음(한줄씩 복사해냄)
#이 방법 외에 shutil라이브러리(shell util)를 사용하여 shutil.copy() 또는 shutil.move()를 사용할 수도 있음.
