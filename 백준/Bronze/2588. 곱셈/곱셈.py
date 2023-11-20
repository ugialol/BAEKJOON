a=int(input())
b=input()               # b는 문자열의 형식으로 입력(인덱스 번호 사용을 위해)
print(a*int(b[2]))      # b의 2번쨰인덱스 번호의 값과 a를 곱함,int로 b[2]를 정수로 전환 
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b))