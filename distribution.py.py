#pdbqt 모듈 
import os, string

#파이썬은 try-catch가 아닌 try-except 구문을 사용한다. finally 사용 가능하며 else 구문도 존재함. 자바도 else있나

try:
	os.chdir('C:\\Users\\USER-PC\\Desktop\\Python_Task_ji\\pdbqt_files') #pdbqt 파일들만 이 디렉토리에 모아놓기
except:
	print("해당 디렉토리가 존재하지 않아서 작업디렉토리를 변경할 수 없습니다.")
	quit() #또는 import sys 한 후 sys.exit() 가능. 프로그램을 추가적으로 실행시키지 않고 바로 종료시키기

#궁금한건, os로 작업디렉토리를 지정하는 것은 어떤 의미가 있는가 이다. 저런거 지정안하면 기본 작업디렉토리는 어디로 지정되는거지? 보통 절대경로 다 써줘야 했는데..
	
f_list=os.listdir() #해당 디렉토리의 모든 파일들을 리스트 형태로 받아옴

if(not f_list):  #비어있는 리스트는 false값을 지님. len(list) 값이 0이 나오면 이 또한 비어있는 리스트라고 볼 수 있음
	print("해당 디렉토리에 아무파일도 존재하지 않습니다. 디렉토리 내에 파일이 존재하는지 확인하십시오")
	quit() 

for file in f_list:  #반복문으로서 리스트에 있는 하나하나의 구성요소값(파일이름)을 하나씩 file변수에 대입
	try:
		f=open(file,"rt") #파일이름을 가지고 해당 파일의 핸들값 생성(그냥 그 파일을 이제 f라는 이름으로 다루겠다고 생각하면 됨. rt는 read text라고 해서 텍스트읽기로 열겠다고 지정)
		
		context = f.readlines()   #해당 파일의 내용을 줄단위로 구분해서 리스트로 가져오기
	
		if(not context):
			print(file+"파일의 내용이 비어있습니다.")
			continue
		
		line2 = context[1]  #두번째 줄 내용 읽기
		number_s = line2.split()[3]
		number = int(float(number_s.lstrip('-')))
		#이 부분에서 오류 발생. 내 생각에는 이 값을 문자값으로 읽어오는게 아니라 숫자값으로 읽어들이는 거 아닐까 생각함
		#number= -1*int(number_s) 이걸로 바꿔봤는데도 문제발생. 문제도 아닌건가?  type()으로 number_s 확인해보니 str로서 문자열로 들어오는 것을 확인할 수 있었다.
		#아 먼저 float으로 바꿔서 실수형태로 값을 바꾼 다음에 int로 바꿔야 하는구나. 처음에는 number = int(number_s.strip('-')) 로 했었음

		dest='C:\\Users\\USER-PC\\Desktop\\Python_Task_ji\\'+str(number)  #이 부분에서도 number값을 그냥 더하게 시키려니까 오류떴었음. 자바처럼 자동 문자열 변환되는게 아닌가봄

		if(not os.path.isdir(dest)):  #숫자값에 대한 디렉토리가 존재하지 않는다면 해당 디렉토리 생성
			os.mkdir(dest)
	
		
		dest+='\\'+file
		#dest = dest + '\\' + file   #기존 dest에 있던 내용에 추가적인 내용을 덧붙어서 dest에 재대입
		make=open(dest,'wt')
		for line in context:
			make.write(line)   #개행 알아서 잘 됨
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
print("\n파일 분류 작업 완료.")

#위의 방법은 프로그램 자체적으로 파일의 내용을 복사하도록 만들었음(한줄씩 복사해냄)
#이 방법 외에 shutil라이브러리(shell util)를 사용하여 shutil.copy() 또는 shutil.move()를 사용할 수도 있음.
