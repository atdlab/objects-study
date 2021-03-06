# CHAPTER.01 객체, 설계

1. 객체 사이의 의존성이 높은 경우 객체 하나를 변경 할 때 다른 객체들도 변경이 되어야만 한다. 이런 경우 결합도가 높다고 말한다. 결합도가 높으면 두 객체가 함께 변경되어야 하기 때문에 결합도를 낮춰 변경이 용이한 설계를 해야 한다.
2. 객체는 서로 긴밀하게 연결되어 있을 필요가 없다. 자율성을 높여 다른 객체가 다른 객체의 세부 한 사항을 알 수 없도록 캡슐화 한다. 캡슐화가 되어있는 객체는 변경하기 쉽다. 객체 내부로의 접근을 막으면 설계를 쉽게 변경 할 수 있다.
3. 코드는 객체 내부의 상태를 캡슐화 하고 오직 메시지를 통해서 만 상호작용 해야 한다. 밀접하게 연관된 작업만 수행하고 연관성 없는 작업은 다른 객체에게 위임하는 응집도가 높게 설계해야 한다.
4. 수동적인 코드를 자율적인 코드로 바꿔야 한다. 그래야지 응집도가 높아지기 때문이다.
5. 작은 메서드로 코드를 분리하자. 코드의 중복을 제거하고, 표현력을 높일 수 있다.
6. 훌륭한 객체 지향 설계란 소프트웨어를 구성하는 모든 객체들이 자율적으로 행동하는 설계를 가리킨다. 능동적이고 자율적이게 구현 해야 한다.

## 티켓 판매 애플리케이션 구현하기

```jsx
이벤트에 당첨된 사람은 초대장을 받는다. 
초대장은 티켓으로 교환 될 수 있다. 초대장이 없는 사람은 돈을 지불하고 티켓을 받을 수 있다.
티켓으로 공연을 볼 수 있다.   
```