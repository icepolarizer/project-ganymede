import numpy as np # 1번째 줄
from momment

#sigmoid function

def nonlin(x, deriv=False): # 4번째 줄
  if (deriv==True): # 5번쨰 줄
    return x*(1-x)
  return 1/(1+np.exp(-x))

#input dataset

X = np.array([ [0,0,1], #10번째 줄
                [0,1,1],
                [1,0,1],
                [1,1,1]])


# 결과 데이터값
y = np.array([[0,0,1,1]]).T #16번째 줄

# 계산을 위한 시드 설정
# 실험의 편의를 위해 항상 같은 값이 나오게 한다.
np.random.seed(1) #20번째 줄

# weights를 랜덤적으로 mean of 0으로 초기화하자.
syn0 = 2*np.random.random((3,1)) - 1 # 23번째 줄

for iter in range(10000): #25번째줄

    # forwad propagation
    l0 = X # 25번째 줄 # 28번째 줄
    l1 = nonlin(np.dot(l0, syn0)) # 29번째 줄

    # 우리가 얼마나 놓쳤는가?
    l1_error = y- l1 # 32번째 줄

    # 우리가 놓친 것들과
    # 11 의 시그모이드 경사와 곱하기.
    l1_delta = l1_error * nonlin(l1, True) # 36번째 줄

    # weight 업뎃
    syn0 += np.dot(l0.T, l1_delta)

print ("Output After Traing")
print (l1)
