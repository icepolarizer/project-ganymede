# 파이썬에 양자컴퓨팅 같은 걸 끼얹나
![](https://i.imgur.com/KFpyXF2.jpg)
> 21세기도 10년이 넘게 지나간 지금은 귀에 못이 박히도록 듣는 이야기지만, 어제 접근하기 어려웠던 기술이 오늘 누워서 떡 먹기가 되는 건 지금 컴퓨터 공학계과 기타 등등 바닥에서 유명한 이야기이고, 사실이기도 하다. 양자컴퓨팅도 그와 비슷하게, 누워서 떡 먹기까지는 아니지만, 매우 가까이 접근했다. 최근 MS에서는 양자컴퓨팅을 위한 언어인  Q#을 공개하고, IBM에서는 상용 양자컴퓨터를 출시했다. 아는 사람은 알고 있겠지만, 양자컴퓨터는 일종의 게임 체인저라고 할 수 있다. 모든 보안을 무력화하는 마법의 지팡이는 아니지만, 현대 암호 체계에 위협을 가하기에는 충분하고도 남을 시스템이다. 양자컴퓨터는 최적화 문제의 해법을 찾는 데 최적의 성능을 자랑하고, 조건이 잘 맞추어진다면 고전적 시스템에서는 무차별 대입으로만 풀리는 문제를 순간에 깰 수도 있다. 물론 아직 충분한 큐비트가 주어지지 않았으니 실현된 이야기는 아니다. 하지만 우리는 이것이 아주 근미래의 이야기라고 생각한다. 그런데 한국에는 이 주제에 관해 충분한 관심이 없는 건지, 아니면 물밑에서 작업이 이루어지고 있는 것인지는 모르겠지만, 최소한 일반적인 개발자들에게 관심을 끌고 있지 못하는 것은 사실인 듯하다. 우리는 이 점에 흥미를(?) 가져서 연구를 시작했다. 

> 김현승(Hyesung Kim - HK)과 나는 이 주제에 대해 대략 2달 전부터 흥미를 가지고 나름 연구를 시작했다. 우리나라에서 양자컴퓨팅에 대한 개발자들의 대중적 접근이 적다는 사실도 도전심리를 자극했다. 거창한 것은 아니다. 나는 프로그래밍에, HK는 물리에 익숙하기 때문에 죽이 잘 맞겠다 싶어서 같이 공부해 보고 있는 정도다.

## 기술 사이드

우리 팀은 일반적으로 유명한 Q#을 사용하지 않았다. 우리나라 개발자들에게 양자컴퓨팅에 대해 물어보면 대부분 막연한 대답 또는 Q#에 대한 이야기가 많았다. 하지만 나는 IBM의 Qiskit을 선택했다. 왜 Q#이 그렇게 인지도가 높은지는 잘 모르겠으나, 나는 Qiskit을 포함한 IBM의 시스템이 MS에 비해 훨씬 더 직관적이라는 결론을 내렸다. IBM은 Qiskit 라이브러리를 파이썬 패키지 저장소에서 지원하고 있으며, 설치만 하면 손쉽게 시뮬레이터에서 큐비트 회로를 작동시킬 수 있다. 그뿐 아니라, 실제 IBM에서 물리적으로 운용하는 Yorktown, Tokyo...등등의 양자컴퓨터 디바이스를 백엔드 삼아 회로를 실행시키는 것도 가능하다. 말 그대로, 개발자라면 지금도 큐비트를 뼛속까지 느낄 수 있다는 것이다.

Qiskit은 3가지 패키지를 내장하고 있는데:

- **Terra** - 가장 기본적인 패키지다. 이걸로 회로를 작성할 수 있다.
- **Aqua** - 확장팩이라 할 수 있고, 이미 정립되어 있는 알고리즘들을 라이브러리에 미리 정의해놓았다.
- **Aer** - 시뮬레이터다. Real Device에서 실험할 때는 이 빠듯한 큐비트들과(20개 넘는 곳이 없고 대부분 16까지만 사용 가능하다...아스키 몇문자 표현하는 것도 무리다) 밀려 있는 queue 때문에 결과를 받아오는 데 시간이 걸린다. 그렇기에 대부분 Aer의 32큐비트 지원 시뮬레이터를 사용하는 편이다.

이걸 선택한 건 나지만, HK도 괜찮게 평가했다. IBM에서는 API 외에도 Composer를 제공해서 GUI로 큐비트 회로를 작곡하듯이 설계할 수 있게 했다. 



## 이론 사이드

이 부분을 이해하려면 약간의 수학적 지식이 필요한데, 이번 글에서는 그쪽은 제외하고 핵심만 설명하도록 하겠다.

큐비트는 양자컴퓨팅의 근간이다. 이것이 ~~재미없는~~ 비트를 대신한다. 대중적으로 퍼져 있는 큐비트의 설명에는, 큐비트가 0, 1 그리고 0도 1도 아닌 상태...즉 중첩 상태, 이 3가지 상태가 있기 때문에 2개밖에 없는 비트보다 더 빠른 처리가 가능하다...라는데, 엄밀히 따지면 이게 아주 맞는 말은 아니다. 고작 2가 3으로 늘어났다고 해서 안 풀리던 RSA가 풀리진 않는다. 우리가 이용할 수 있는 건 이 중첩 상태가, 0이면서 1이고, 0이 아니면서 1도 아닐 수 있다는 것, 즉 이 애매모호함이다. 

활용 가능성 이야기는 나중으로 미루고, 우선 큐비트가 어떻게 작동하는 것인지 설명해 보겠다.

큐비트를 이해하려면 먼저 벡터에 관한 이해가 필요하다. 어렵게 생각할 것은 없다. 그저 수량을 가진 방향, 길이가 주어진 화살표라고만 생각하면 된다. 이는 서로 더하거나 뺄 수 있다. 그런데 이 벡터를 하나의 구면 안에서, 구의 중점에서 바깥 어느 지점으로 뻗은 벡터라고 생각해 보자. 이 벡터가 큐비트의 상태를 나타낸다. 이것이 수직으로 위로 뻗으면 0인 '상태', 즉 |0⟩ 이 된다(디랙 표기법, 혹은 브라-켓 표기법에 따른 것이다). 반대로 수직으로 아래로 뻗으면 |1⟩ 이 된다.

그런데, 이 벡터가 수직이 아닌 상태로 다른 어딘가를 향하면 이것이 바로 Superpsition, 즉 중첩 상태가 된다. 엄밀히 말하면 정해진 위치가 있지만, 일단은 그렇게 생각하자. 이 순간, 양자의 행방은~~진실은 저 너머에~~ 알 길이 없게 된다. 정말 모른다. 애초에 결정되기 전까지는 어느 값도 아니고, 어느 값도 아니기에 그 확률을 특정 방향으로 조정하는 것도 무리다.

이런 표현법을 통틀어 「 블로흐 구면<sup>Bloch Sphere</sup>」 이라 한다.

![By Smite-Meister - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=5829358](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Bloch_sphere.svg/1024px-Bloch_sphere.svg.png){ width=50% }