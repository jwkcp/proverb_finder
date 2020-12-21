# 개요

낱글자로 이루어진 가로 세로 2차원 배열 형태의 글자 행렬이 있다. 여기에서 말이 되는 속담을 최대한 많이 찾아라.  

## 목표

너무 많은 시간을 들이지 말고 그냥 파이썬으로 사람보다 빨리 많이 찾아보는 것이다. OCR인식을 하거나, 소스를 다듬거나, 여러 예외처리 구분을 넣을 수 있지만 그런 거 다 빼고 그냥 재미로 빨리 찾아보는 것이다. 일정 수준의 정확도만 필요하다(내 시간도 소중하니까) 배보다 배꼽이 더 커지면 안된다.  

## 규칙

1. 가로 세로 낱글자는 정사각행렬이 아니다.
2. 띄어쓰기를 하지 않는다.
3. 속담은 아래와 같은 방향으로 나타날 수 있다.  

- 가로 (왼쪽에서 오른쪽)
- 가로 (오른쪽에서 왼쪽)
- 세로 (왼쪽에서 오른쪽)
- 세로 (오른쪽에서 왼쪽)
- 대각선 (오른쪽 위에서 왼쪽 아래)
- 대각선 (왼쪽 위에서 오른쪽 아래)

---

# 전처리

## src.txt(낱글자 행렬) 만들기
구글 독스로 OCR을 해보았으나 글자 상태가 안좋아 정확도가 많이 떨어졌다. 그렇다고 OCR 라이브러리도 다른 시도를 하는 건 위에서 말한 `목표`를 벗어난다. 눈과 손을 쓰기로 한다. 3분 안에 칠 수 있다. 이 파일은 대략 이렇게 생겼다.  

[![2020-12-21-6-18-00.png](https://i.postimg.cc/NFnf2vpJ/2020-12-21-6-18-00.png)](https://postimg.cc/T5rXBF8g)

## dict.txt(속담사전) 만들기
속담 모음집(여기서는 dict.txt)을 만들기 위해 여러 인터넷 사이트의 속담을 긁어 모았다. 대표적으로 아래 2개 사이트가 양이 많았고 여기 저기서 마구 마구 긁어 모은 후 vscode의 replace 기능(정규식도 되니까)과 엑셀의 기능을 이용해 공백, 특수문자, 빈 행, 중복 속담 등을 제거했다.  
- https://namu.wiki/w/%EC%86%8D%EB%8B%B4/%ED%95%9C%EA%B5%AD
- https://ko.wikiquote.org/wiki/%ED%95%9C%EA%B5%AD_%EC%86%8D%EB%8B%B4

그렇게 나온 파일이 `dict.txt`이다. 속담 모음집이 필요하신 분은 이걸 다운받아 활용하시면 나름 도움이 될 수 있을 것 같다. 이 파일은 이렇게 생겼다.  

[![2020-12-21-6-18-10.png](https://i.postimg.cc/66bQmCtr/2020-12-21-6-18-10.png)](https://postimg.cc/8sWDFJFc)

---

# 사용 방법

아래와 같이 주어진 가로 세로 낱글자 행렬이 있다. 

[![2020-12-21-5-55-52.png](https://i.postimg.cc/m2crfhg0/2020-12-21-5-55-52.png)](https://postimg.cc/3dTh28pB)

터미널에 `python main.py src.txt dict.txt`로 입력하면 말이 되는 속담의 결과를 보여준다.

- main.py: 소스파일
- src.txt: 위 가로 세로 낱글자 행렬을 글자로 입력한 파일
- dict.txt: 속담 모음집

## 결과

[![2020-12-21-6-26-30.gif](https://i.postimg.cc/cH9dPNyx/2020-12-21-6-26-30.gif)](https://postimg.cc/qhKfCSvS)

총 949개 속담사전 목록을 검사했고 사람보다 빨리 찾았다. :)
