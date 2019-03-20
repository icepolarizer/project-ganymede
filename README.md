# Should we add Quantum Computing to Python: 파이썬에 양자컴퓨팅 같은 걸 끼얹나

![](https://i.imgur.com/KFpyXF2.jpg)
> 21세기도 10년이 넘게 지나간 지금은 귀에 못이 박히도록 듣는 이야기지만, 어제 접근하기 어려웠던 기술이 오늘 누워서 떡 먹기가 되는 건 지금 컴퓨터 공학계과 기타 등등 바닥에서 유명한 이야기이고, 사실이기도 하다. 양자컴퓨팅도 그와 비슷하게, 누워서 떡 먹기까지는 아니지만, 매우 가까이 접근했다. 최근 MS에서는 양자컴퓨팅을 위한 언어인  Q#을 공개하고, IBM에서는 상용 양자컴퓨터를 출시했다. 아는 사람은 알고 있겠지만, 양자컴퓨터는 일종의 게임 체인저라고 할 수 있다. 모든 보안을 무력화하는 마법의 지팡이는 아니지만, 현대 암호 체계에 위협을 가하기에는 충분하고도 남을 시스템이다. 양자컴퓨터는 최적화 문제의 해법을 찾는 데 최적의 성능을 자랑하고, 조건이 잘 맞추어진다면 고전적 시스템에서는 무차별 대입으로만 풀리는 문제를 순간에 깰 수도 있다. 물론 아직 충분한 큐비트가 주어지지 않았으니 실현된 이야기는 아니다. 하지만 우리는 이것이 아주 근미래의 이야기라고 생각한다. 그런데 한국에는 이 주제에 관해 충분한 관심이 없는 건지, 아니면 물밑에서 작업이 이루어지고 있는 것인지는 모르겠지만, 최소한 일반적인 개발자들에게 관심을 끌고 있지 못하는 것은 사실인 듯하다(기본 개념인 블로흐 구면부터가 한국어 위키피디아에 없다). 우리는 이 점에 흥미를(?) 가져서 연구를 시작했다.

> 김현승(Hyesung Kim - HK)과 나는 이 주제에 대해 대략 2달 전부터 흥미를 가지고 나름 연구를 시작했다. 우리나라에서 양자컴퓨팅에 대한 개발자들의 대중적 접근이 적다는 사실도 도전심리를 자극했다. 거창한 것은 아니다. 나는 프로그래밍에, HK는 물리에 익숙하기 때문에 죽이 잘 맞겠다 싶어서 같이 공부해 보고 있는 정도다.

## 기술 사이드

우리 팀은 일반적으로 유명한 Q#을 사용하지 않았다. 우리나라 개발자들에게 양자컴퓨팅에 대해 물어보면 대부분 막연한 대답 또는 Q#에 대한 이야기가 많았다. 하지만 나는 IBM의 Qiskit을 선택했다. 왜 Q#이 그렇게 인지도가 높은지는 잘 모르겠으나, 나는 Qiskit을 포함한 IBM의 시스템이 MS에 비해 훨씬 더 직관적이라는 결론을 내렸다. IBM은 Qiskit 라이브러리를 파이썬 패키지 저장소에서 지원하고 있으며, 설치만 하면 손쉽게 시뮬레이터에서 큐비트 회로를 작동시킬 수 있다. 그뿐 아니라, 실제 IBM에서 물리적으로 운용하는 Yorktown, Tokyo...등등의 양자컴퓨터 디바이스를 백엔드 삼아 회로를 실행시키는 것도 가능하다. 말 그대로, 개발자라면 지금도 큐비트를 뼛속까지 느낄 수 있다는 것이다.

Our team didn’t used the Q#, which is quite popular (cause it’s made by MS). If we ask the developer community in South Korea about Quantum Computing, they mostly talked about Q#. However, our team chose to use Qiskit from IBM. I do not know why Q# has such reputation, but I concluded that the system of IBM including Qiskit is more strait forward compared to the ones of MS. IBM is supporting the Qiskit library in Python package storage, and if the Qiskit library is downloaded, the qubit circuit can be run in the simulator easily. Also, the users are able to run the circuit by using the quantum computer such as Yorktown, Tokyo, etc operated from IBM as a backend. Which means, the programmers can feel the qubit through their bones.

Qiskit은 3가지 패키지를 내장하고 있는데:

- **Terra** - 가장 기본적인 패키지다. 이걸로 회로를 작성할 수 있다.
- **Aqua** - 확장팩이라 할 수 있고, 이미 정립되어 있는 알고리즘들을 라이브러리에 미리 정의해놓았다.
- **Aer** - 시뮬레이터다. Real Device에서 실험할 때는 이 빠듯한 큐비트들과(20개 넘는 곳이 없고 대부분 16까지만 사용 가능하다...아스키 몇문자 표현하는 것도 무리다) 밀려 있는 queue 때문에 결과를 받아오는 데 시간이 걸린다. 그렇기에 대부분 Aer의 32큐비트 지원 시뮬레이터를 사용하는 편이다.

Qiskit contains 3 kinds of packages:

Terra - Most basic package. It can write circuits

Aqua - Can be understood as a DLC, and it organized the established algorithms in the library

Aer - Simulator. When experimenting in a Real Device it takes time to get a result from the tough qubits (usually can use until 16 qubits….it is hard to even print few ascii code). Therefore, the 32bit supported simulator from Aer is usually used.

이걸 선택한 건 나지만, HK도 괜찮게 평가했다. IBM에서는 API 외에도 Composer를 제공해서 GUI로 큐비트 회로를 작곡하듯이 설계할 수 있게 했다.

IBM의 이쪽 방면에 대한 문서화는 이곳저곳 구멍이 조금씩 나 있다. 튜토리얼 링크들이 깨져 있다거나, 가상환경을 가져와서 그대로 Jupyter Notebook의 예제를 실행했는데 오류가 있다던가. 관리가 완벽하게 이루어지는 것 같지는 않다. 하지만, 의외로 개발자 친화적이게 만들어둔 것들이 많다. 예를 들면, [docker pull qiskit/qiskit-tutorial](이것) 처럼  서버에서 qiskit이 사용될 경우 docker를 사용해서 안정적으로 실행할 수 있게 했다. 이게 굉장히 좋은 것이, 리눅스 서버에 네이티브로 qiskit을 설치하려 할 경우, 아나콘다를 써도 의존성 문제가 대폭발하며 설치를 방해하는데 docker를 사용할 경우 전부 세팅되어 있기 때문에 문제가 없다.

사실 Qiskit뿐만 아니라 다른 좋은 라이브러리들도 많다. 우리도 처음에는 Qiskit만 사용했지만, 점점 여러 가지 기능이나 특성을 필요로 하게 되면서 ProjectQ나 Qutip(이 라이브러리의 개발진에는 고려대학교도 포함되어 있다) 같은 라이브러리들도 많이 사용하게 되었다.






## 이론 사이드

이 부분을 이해하려면 약간의 수학적 지식이 필요한데, 이번 글에서는 그쪽은 제외하고 핵심만 설명하도록 하겠다.

큐비트는 양자컴퓨팅의 근간이다. 이것이 ~~재미없는~~ 비트를 대신한다. 대중적으로 퍼져 있는 큐비트의 설명에는, 큐비트가 0, 1 그리고 0도 1도 아닌 상태...즉 중첩 상태, 이 3가지 상태가 있기 때문에 2개밖에 없는 비트보다 더 빠른 처리가 가능하다...라는데, 엄밀히 따지면 이게 아주 맞는 말은 아니다. 고작 2가 3으로 늘어났다고 해서 안 풀리던 RSA가 풀리진 않는다. 우리가 이용할 수 있는 건 이 중첩 상태가, 0이면서 1이고, 0이 아니면서 1도 아닐 수 있다는 것, 즉 이 애매모호함이다.

You need some mathematical knowledge to understand this part. But, this part will exclude the parts that has these hard math and will explain only the basic concepts. Qubit is the base of quantum computing. This qubit replaces the normal bit. The explanation of qubit that is explained throughoutly is, as qubit has three states, which is 1, 0, and both...which is the superposition state, it can calculate faster than the normal bit which has only two states….is what it is saying, but strictly speaking, this is not 100% true. Having only one more state does not mean you can solve the RSA that you cannot solve with classical computer. The feature that we can use is the superposition state.

활용 가능성 이야기는 나중으로 미루고, 우선 큐비트가 어떻게 작동하는 것인지 설명해 보겠다.

큐비트를 이해하려면 먼저 벡터에 관한 이해가 필요하다. 어렵게 생각할 것은 없다. 그저 수량을 가진 방향, 길이가 주어진 화살표라고만 생각하면 된다. 이는 서로 더하거나 뺄 수 있다. 그런데 이 벡터를 하나의 구면 안에서, 구의 중점에서 바깥 어느 지점으로 뻗은 벡터라고 생각해 보자. 이 벡터가 큐비트의 상태를 나타낸다. 이것이 수직으로 위로 뻗으면 0인 '상태', 즉 |0⟩ 이 된다(디랙 표기법, 혹은 브라-켓 표기법에 따른 것이다). 반대로 수직으로 아래로 뻗으면 |1⟩ 이 된다.

Let me explain how qubit works first. To understand qubit, you need to understand vector. Vector is not a very hard concept. Just think of it as an arrow with a direction and length. This can be added or subtracted from each other (It can also be multiplied in a different way than usual, too). Let us consider a vector starting from a center of a sphere reaching toward a surface of the sphere. This vector indicates the state of the qubit. If it extends vertically upwards, it becomes a 'state' of 0, that is, |0⟩according to Dirac notation, or bracket notation). Conversely, if you extend vertically downward, it becomes l1⟩.

그런데, 이 벡터가 수직이 아닌 상태로 다른 어딘가를 향하면 이것이 바로 Superpsition, 즉 중첩 상태가 된다. 엄밀히 말하면 정해진 위치가 있지만, 일단은 그렇게 생각하자. 이 순간, 양자의 행방은~~진실은 저 너머에~~ 알 길이 없게 된다. 정말 모른다. 애초에 결정되기 전까지는 어느 값도 아니고, 어느 값도 아니기에 그 확률을 특정 방향으로 조정하는 것도 무리다.

이런 표현법을 통틀어 「 블로흐 구면<sup>Bloch Sphere</sup>」 이라 한다.

 When this vector heads on a direction that is not either vertically upwards or downwards, it becomes a superposition state. Specifically speaking, there is a specific direction, but let’s not think of it right now. In this moment, the output of this qubit is unknown until it is observed. As before it is observed it is neither 1 or 0, it is hard to even handle with the possibilities, too. 

We call this figure a Bloch Sphere.

![By Smite-Meister - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=5829358](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Bloch_sphere.svg/136px-Bloch_sphere.svg.png)





이 블로흐 구면은 너무도 유용해서, 양자를 직관적으로 이해하는 데 적격이라고 생각한다. 사실 양자가 저런 벡터 모양으로 생긴 것은 당연히 아니다. 하지만 큐비트를 생각할 때는 그냥 스위치 대신 저걸 생각하면 편하다.

This bloch sphere is so useful, I think this is the easiest way to understand a quantum. Well, a quantum itself actually does not look like a vector, but it is easy to think of this instead of a switch when you think of a qubit.

그리고 큐비트를 제어하려면 당연히 제어할 매개체가 필요하다. 이 매개체로는 게이트 방식과 어널링 방식이 존재하는데, 어널링도 획기적인 방법(외판원 문제에 이게 사용된다는 이야기를 들은 적이 있다) 이기는 하지만, 우리는 게이트를 사용할 것이다. IBM부터가 게이트 시스템을 차용했고, 일단 지금으로써는 게이트가 보편적으로 사용된다. 정확히 알고 있는 사실은 아니지만, 게이트에 비해 어널링은 기존의 절차적 프로그래밍이 쉽지 않다. 나이오븀을 사용한 양자의 상호 간섭을 이용하는데, 게이트를 이용하여 비트 단위의 절차적 루틴을 짜는 것이 일단은 더 접근성이 높다고 본다.

And of course, you need a tool to handle a qubit. There is a gate and an anuling for these tools, and even though anuling is a marvelous way to handle it, we decided to use a gate because IBM uses a gate system. I am not sure about this but using anuling is not easy to follow the previous programming. It uses a mutual inference of quantums, but we thought using a gate to program by qubit has higher accessibility.

위 설명에서 어느 정도 감을 잡았을 수도 있겠지만, 게이트 방식은 양자를 말 그대로 게이트에 통과시키는 식으로, 게이트를 순서대로 배치해서 그 안으로 큐비트를 통과시키면 그 배치 순서에 따라 큐비트의 상태가 변화한다. 이를 이용해서 루틴을 짤 수 있다. 게이트는 여러 가지가 있는데, X게이트 같이 축을 반전시키는 게이트도 존재하고, H게이트(Hadamard Gate)처럼 양자를 Superposition 상태로 만드는 게이트도 존재한다. 또한, 「 양자 얽힘<sup>Quantum Entanglement</sup>」도 게이트로 구현되어 있다. 양자 얽힘은 두 양자가 다른 위치에도 불구하고 하나의 물리적 계, 엄밀히는 Hamiltonian system 안에 존재해서 그 계 안의 에너지 총량은 항상 동일하다는 이론이다. 이를 이용하면 두 양자가 서로에게 상호작용을 하게 만들 수 있는데, Entanglement Gate가 그 역할을 한다. 이 게이트는 2개의 노드로 이루어져 있으며, 이들을 각각 큐비트 앞에 배치하면 된다. 

As you may have guessed from the explanation above, the gate method literally passes the qbit through the gate, so that when the gates are arranged in order and the qubit passes through, the state of the qubit changes according to the order of arrangement. You can use this to create routines. There are various gates, such as an X gate, which reverses the axis, and there exists a gate that makes both of them superposition, like a H gate (Hadamard Gate). "Quantum entanglement" is also implemented as a gate. Quantum entanglement is the theory that both quantums are present in one physical system, strictly in the Hamiltonian system, despite the different locations, the total energy in the system is always the same. This allows the two entities to interact with one another. The Entanglement Gate consists two nodes, each of which is placed in front of the qubit.

이렇게 하면, 한 큐비트가 |1⟩ 인지 여부에 따라 다른 노드의 큐비트가 반전된다.



> 예를 들어, 큐비트 A, B가 서로 얽혀 있을 때, 큐비트 A가 |0⟩ 이고 B가 |0⟩ 이다. 그런데 A가 X게이트(NOT게이트)를 통과해서 |1⟩ 이 되었다. 이후 이 두 큐비트가 Entanglement 게이트를 통과하면, B도 |1⟩ 가 된다. 반면 이 회로에서 X게이트를 제거하면 B의 상태는 |0⟩ 그대로다.

그리고, 이런 회로를 모두 통과한 후에는 결국 관측이 필요하다. 관측 없이는 결과가 있을 리 만무하다. 하지만 회로 설계시 관측 순간은 신중하게 생각해야 한다. 관측 후에는 양자의 특성을 사용할 수 없다. 관측자에 의해 관측되는 순간 양자의 상태는 완전히 하나로 수렴하며, 이렇게 되면 끝이다. 더 이상 바뀌지 않는다. 그러므로 관측은 모든 연산이 끝나고 최종적으로 해야 한다. 이 비트를 변수로 친다면, 디버거처럼 실행 중에 변수를 추적하는 것은 불가능한 셈이다.

In this way, the qubits of other nodes are inverted depending on whether one qubit is |1 ⟩. For example, when the entangled qubits A and B are both in |0⟩. As A passes through the X gate (NOT gate) and becomes |1⟩, then if these two qubits pass through the Entanglement gate, then B also becomes |1⟩. On the other hand, when the X gate is removed from this circuit, the state of B is |0⟩. And after all these circuits have passed, observations are needed. Without observations, there is no result. However, the moment of observation should be thought carefully when designing the circuit. The state of a qubit cannot be changed after observation. The state of the moment when observed by the observer converges completely into one, and that is the end. It does not change anymore. Therefore, observations should be done at the end of every computation. If you use this bit as a variable, it is impossible to trace the variable during execution like a debugger.



## 연구 진행 현황

현재 연구되고 있는 주제들은 다음과 같다. 이들 중에는 실현 가능성이 있는 것도 있고, 그저 문득 떠오른 생각에 의한 실험도 있다.

1. 큐비트를 이용한 딥러닝의 활성화 함수, 신경망 구현
2. 양자컴퓨팅을 이용한 암호화 문제 공략
3. Grover 알고리즘을 이용한 탐색 문제 해결
4. 큐비트를 이용한 난수 생성



**1. 큐비트를 이용한 딥러닝의 활성화 함수, 신경망 구현**

조사 중에 이미 이와 유사한 개념인 QNN(Quantum Neural Network)가 존재한다는 것을 알게 되었다. 사실 아직 이건 실험 단계일 뿐, 쓸 만하지는 않다. 하지만 매우 흥미롭다고 느껴서, 블로흐 구면의 축의 기울기, 즉 양자의 확률을 신경망의 가중치에 대입하는 시도를 해 보았다.

**2. 양자컴퓨팅을 이용한 암호화 문제 공략**

사실상 양자 컴퓨터가 각광받는 이유가 이것이나 다름없다. 상식을 초월하는 고성능의 컴퓨터를 요구하는 몇 가지 분야(기상 예측, 신약 개발 등을 위한 화학 시뮬레이션 등등...)들 중 하나가 바로 암호학이다. 빠른 연산 속도는 곧 더 빠른 무차별 대입 속도와 더 긴 키를 의미한다. 아직 우리의 연구 주제는 암호학으로는 깊게 들어가지 않았다. 하지만, RSA의 보안을 뚫을 강력한 열쇠인「양자컴퓨터를 이용한 소인수분해」는 깊게 연구 중이고, 사실 가장 흥미롭다고 생각하고 있다. 굳이 암호학이 아니더라도, 소수는 정말 흥미로운 수학적 개념이고, 이를 양자컴퓨터로 접근한다는 건 전율을 느끼게 해준다. 그래서 우리는 암호의 해결보다「양자컴퓨터와 소수」, 이 두 가지를 이어보는 데 집중했다. 

그 결과는 당장 괄목할 만한 성과는 아니었다. 그래도 근미래에 반드시 흥미로운 결과가 될 것이라고 우리는 생각한다. 이는 양자컴퓨터가 당장은 그렇게 많은 큐비트를 지원하지 않기 때문이다. 하지만 소인수분해 시 양자컴퓨터는 많은 개수의 큐비트를 요구한다. 그렇기에 지금은 시뮬레이터를 사용할 수밖에 없는데, 시뮬레이터는 실제 양자컴퓨터가 아니므로 당연히 느리다. 그러므로 당장 속도만 놓고 보면 가상환경에서는 고전적 컴퓨터보다도 훨씬 느리다. 이는 양자컴퓨터의 하드웨어 성능이 더 발전하면 충분히 해결될 것이다.

**4. 큐비트를 이용한 난수 생성**

이 주제도 충분히 흥미롭다. 암호학에 관심이 있는 사람들이라면 알고 있겠지만, 완전난수 생성은 수학적으로는  불가능에 가깝기 때문에 대부분은 seed를 난수 생성함수에 넣어서 ~~유사난수~~의사난수를 생성한다. 고전적 컴퓨터에서 완전난수를 생성하려면 (라플라스의 악마는 없다고 가정하고) 컴퓨터에 주사위를 넣는 수밖에 없다는 소리까지 나오는데...진짜 주사위가 나타난 셈이다.

신은 주사위 놀이를 하지 않는다고 아인슈타인이 말한 적이 있는데. 바로 그 신의 주사위가 우리 손에 들어온 것이다. 그것도 자동화가 매우 손쉬운 주사위다. 우리는 이보다 더 좋은 난수 생성기는 없을 것 같다고 생각해서 이걸로 생성한 난수를 random.org 처럼 웹사이트에 적용해보기로 했고, 그 결과가 [Momment](http://momment.xyz)였다.



**또다른 가능성: Grover 알고리즘**

> Grover 알고리즘은 컴퓨터공학자 *Lov Grover*가 1996년에 개발한 알고리즘이며, 데이터베이스 탐색에 특화된 알고리즘이다. 제작자 본인의 논문은 [https://arxiv.org/pdf/quant-ph/9605043.pdf]() 에서 확인해보시길.

Grover 알고리즘은 위 설명대로 탐색 특화 알고리즘이다. 사실 현재까지의 탐색 알고리즘 중 기본은 이진 탐색 알고리즘이고, 굳이 이진탐색을 쓸 수 없는 상황이 아니라면 예외없이 사용된다. 정렬된 리스트에 한하여 이진탐색의 시간 복잡도는 ![equation](https://latex.codecogs.com/gif.latex?O%28%5Clog%20n%29) 이니 당연하다. 하지만 아까 말한 '이진탐색을 쓸 수 없는 상황' 이 많다는 게 문제다. 어느 문제든 이진탐색을 적용하기 위해서는 정렬 알고리즘도 실과 바늘처럼 따라다닌다. 이렇게 될 경우, 극히 거대한 양의 데이터는 탐색이 아니라 정렬부터 불가능할 것이다. 이럴 때는 순차 탐색밖에 없다. Brute Force도 마찬가지다.  그러니 일단은 순차 탐색과 연결해서 생각해 보자. 순차 탐색의 시간 복잡도는 ![equation](https://latex.codecogs.com/gif.latex?O%28n%29)이다. 그런데 이 경우, Grover 알고리즘을 사용하면 이는 ![eqation](https://latex.codecogs.com/gif.latex?O%28%5Csqrt%20n%29) 으로 둔갑한다. 이것이 이 매직박스의 능력이다. 이 Grover 알고리즘 안에는 오라클<sup>Oracle</sup> 이라는 모듈이 존재하는데(여러분들이 생각하는 그 오라클이 아니다), 이것의 구조를 변형함으로써 알고리즘의 입력값을 만든다. 그러면 이 알고리즘의 루틴은 다음과 같다:

1. 입력을 받는다.
2. Oracle로 표현한다.
3. ????
4. PROFIT!

**Current Progress**  
We are currently working on following topics. Some of them has enough potential and realistic possibility, and some of them are just the prototypes that came from our imagination. 
1. Building Activation functions and neural networks with qubits.
2. Cracking cryptographic problems using Quantum Computing
3. Solving and making faster search problem, using the Grover Algorithm
4. Creating random numbers with qubits

**Building Activation functions and neural networks with qubits.**  
While researching about this, we discovered that the similar concept already exists. In fact, this is in the stage of experiment and is not very useful. However, we thought it’s brilliant and clever. So we at least tried to apply qubit’s probability to neural network’s weight. 

**Cracking cryptographic problems using Quantum Computing.**  
This is actually the reason why Quantum Computer is in the spotlight. Cryptography is one of the subject which requires the enormously high capacity of the computer resources. Faster operation speed equals to faster Brute-Force attack and longer key. Though we are not making enough research about cryptography. However, we are highly interested in factorization of large number using quantum computer. And actually, this is our favourite research topic. Even if I forget about cryptography, Prime Number is one of the astonishing concepts of Mathematics, and solving them makes us feel a shudder. So we’ve decided to sterlingly focus on ‘Quantum Computer and Prime Numbers’, instead of Cryptography. 
Currently, we couldn’t accomplish the eye-catching result. Though we still believe it will produce much interesting things in the near future. It’s because we don’t have the enough quantum hardware resources. Basically, we don’t have enough qubits, while the factorization algorithm sometimes requires over thousands of qubits and gates. So there is no other way except using the simulator. And simulator is, of course, much slower that real device. So, we can say that Quantum Algorithm is much slower than classical computer, in case of the simulator. And we do believe that these will be fixed soon, since Quantum Computer’s hardware performance is still rising.


**Another Possibility: The Grover Algorithm**  
The Grover algorithm is an algorithm developed by computer engineer Lov Grover in 1996 and is specialized in database search. Please check the author's paper at https://arxiv.org/pdf/quant-ph/9605043.pdf.
The Grover algorithm is a search specialized algorithm as described above. In fact, the basic search algorithm to date is the binary search algorithm, and it is used without exception unless the binary search can not be used. The time complexity of binary searches is O(logN). But the problem is that there are many situations that I can not use the binary search. In order to apply a binary search in any problem, the sorting algorithm follows the thread and needle. In this case, an extremely large amount of data would be impossible to even sort before search. In this case, there is only sequential search, which Brute Force is included in. So let's think about the sequential navigation. The time complexity of the sequential search is O(log n). But if you use Grover algorithm, it changes to O(n)^(½). This is the ability of this magic box. Within this Grover algorithm, there is a module called Oracle (not the Oracle you think), and it changes the structure of it to create the input values ​​of the algorithm. The routine for this algorithm is then:


Get input
Describe with oracle
????
Profit!!
