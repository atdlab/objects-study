# chapter5. 책임 할당하기

### 책임에 초점을 맞추자

- `어떤 객체`에게 `어떤 책임`을 할당하나?

### 책임 할당 과정은 일종의 트레이드오프 활동

- 동일한 문제를 해결할 수 있는 다양한 책임 할당 방법 존재
- 상황과 문맥에 따라 판단하자
- 다양한 관점에서 설계를 평가할 수 있어야 한다

## 01. 책임 주도 설계를 향해

- 데이터보다 `행동`을 먼저 결정하라
- `협력`이라는 문맥 안에서 `책임`을 결정하라

### 데이터보다 행동을 먼저 결정하라

- 객체에게 중요한 것 = 외부에 제공하는 `행동` = 객체의 `책임`
- 객체는 협력에 참여하기 위해 존재하며 협력 안에서 수행하는 `책임`이 `객체의 존재가치`를 증명한다
- `데이터 중심 설계`
    - “이 객체가 포함해야 하는 `데이터`가 무엇인가”
    - “`데이터를 처리`하는 데 필요한 오퍼레이션은 무엇인가”
- `책임 중심 설계`
    - “이 객체가 `수행해야 하는 책임`은 무엇인가”
    - “이 `책임을 수행`하는 데 필요한 데이터는 무엇인가”

### 협력이라는 문맥 안에서 책임을 결정하라

- 객체에게 할당된 책임이 협력에 어울리지 않는다면 그 책임은 나쁜 것이다
- 객체의 입장에서 책임이 어색해보이더라도 협력에 적합하다면 그 책임은 좋은 것이다

<aside>
💡 책임은 객체의 입장이 아니라 객체가 참여하는 `협력에 적합`해야 한다

</aside>

### 협력에 적합하다는 건

- 메시지 수신자가 아니라 `메시지 전송자`에게 적합한 책임
- 메시지를 전송하는 클라이언트의 의도에 적합한 책임
- 메시지를 결정한 후에 객체를 선택해야 한다
- 객체가 메시지를 선택하는 것이 아니라 메시지가 객체를 선택하게 해야 한다

### 책임 주도 설계

- 시스템이 사용자에게 제공해야 하는 기능인 `시스템 책임`을 파악한다
- 시스템 책임을 `더 작은 책임`으로 분할한다
- 분할된 책임을 수행할 수 있는 적절한 객체 또는 역할을 찾아 `책임을 할당`한다
- 객체가 책임을 수행하는 도중 다른 객체의 도움이 필요한 경우 이를 책임질 `적절한 객체 또는 역할`을 찾는다

> 책임을 결정한 후에 책임을 수행할 객체를 찾자
>

## 02. 책임 할당을 위한 GRASP 패턴

- GRASP
    - General Responsibility Assignment Software Pattern
    - 일반적인 책임 할당을 위한 소프트웨어 패턴

### 올바른 도메인 모델이란 존재하지 않는다

- 도메인 모델이 올바른 구현을 이끌어낼 수만 있다면 올바르다고 표현
- 도메인 모델의 개념과 관계는 구현의 기반이 돼야 한다
- 도메인 모델이 구현을 염두에 두고 구조화되는 것이 바람직하다는 것을 의미

### 정보 전문가에게 책임을 할당하라

- 애플리케이션이 제공해야 하는 기능 = 애플리케이션의 책임
- 영화를 예매하는 기능을 제공해야 한다 = 영화를 예매할 책임이 있다
    - 이 메시지를 수신할 적합한 객체를 찾아라

### INFORMATION EXPERT(정보 전문가) 패턴

- 정보와 행동을 최대한 가까운 곳에 위치시키기 때문에 캡슐화를 유지할 수 있다
- 필요한 정보를 가진 객체들로 책임이 분산 → 응집력
- 결합도가 낮아져 간결하고 유지보수하기 쉬운 시스템 구축 가능

<aside>
💡 책임을 수행하는 객체가 정보를 ‘알고' 있다고 해서 그 정보를 ‘저장'하고 있을 필요는 없다

</aside>

- 객체는 해당 정보를 제공할 수 있는 다른 객체를 알고 있거나 필요한 정보를 계산해서 제공할 수도 있다

### 예매하라 메시지

- `상영`에 예매하라 메시지 전송
- 예매하기 위해서는 예매 가격을 알아야함
- 상영은 예매 가격을 계산하기 위한 정보를 모름
- 외부의 객체에게 도움을 요청하자 → 새로운 메시지 생성

### 가격을 계산하라 메시지

- 영화 가격을 계산하는 데 필요한 정보를 알고 있는 전문가를 찾자
- `Movie` 가 가격을 계산하자
- 가격 계산하기 위해선 할인 가능 여부 판단 후
- 할인 정책에 따라 금액을 계산한다
- 할인 조건에 따라 할인 가능 여부 판단은 Movie 가 하기 어려움
- 할인 여부를 판단하라 → 새로운 메시지 생성

### 할인 여부를 판단하라 메시지

- 할인 여부를 판단하는 데 필요한 정보를 알고 있는 전문가를 찾자
- `DiscountCondition` 은 할인 여부를 판단하는 데 필요한 모든 정보를 알고 있음
- 외부의 도움 없이 스스로 가능 → 새로운 메시지 생성 X

### LOW COUPLING (낮은 결합도) 패턴

- 어떻게 하면 의존성을 낮추고 재사용성을 증가시킬 수 있을까?
- 설계의 전체적인 결합도가 낮게 유지되도록 `책임을 할당`하라
- 현재의 책임 할당을 검토하거나 여러 설계 대안들이 있을 경우 낮은 결합도를 유지할 수 있는 설계 선택

### Movie VS Screening

- DiscountCondition 이 누구와 협력해야 할까?
- Movie 는 DiscountCondition 의 목록을 속성으로 포함
- Movie 와 DiscountCondition 은 이미 결합되어 있다
- Movie 를 선택하면 결합도를 추가하지 않아도 됨

### HIGH COHESION (높은 응집도) 패턴

- 어떻게 복잡성을 관리할 수 있는 수준으로 유지할 것인가?
- 높은 응집도를 유지할 수 있게 `책임을 할당`하라

### Movie VS Screening

- Screening : 예매하라
- Movie : 영화 요금을 계산하라
- Screening 이 DiscountCondition 을 떠안으면?
- Screening - 영화 요금 계산 관련 책임 추가..
    - Screening 은 DiscountCondition 이 할인 여부를 판단할 수 있음과
    - Movie 가 이 할인 여부를 필요로 한다는 사실을 알고 있어야 함
- 예매 요금 계산 방식 변경될 경우 → Screening 도 함께 변경…

### CREATOR (창조자) 패턴

- 어떤 객체에게 객체 생성 책임을 할당해야 하는가?
- 이미 결합돼 있는 객체에게 생성 책임을 할당하는 것은 설계의 전체적인 결합도에 영향을 미치지 않음
- CREATOR 패턴은 이미 존재하는 객체 사이의 관계를 이용 → 낮은 결합도

### POLYMORPHISM

- 객체의 타입에 따라 변하는 로직이 있을 때 로직을 담당할 책임을 어떻게 할당해야 하는가?
- 타입을 명시적으로 정의하고 각타입에 다형적으로 행동하는 책임 할당
- POLYMORPHISM 패턴은 객체의 타입을 검사해서 타입에 따라
    - 여러 대안들을 수행하는 조건적인 논리를 사용하지 말라고 경고함
    - 대신 다형성을 통해 새로운 변화를 다루기 쉽게 확장하라고 권고


### PROTECTED VARIATIONS (변경 보호) 패턴

- 설계에서 변하는 것이 무엇인지 고려하고 변하는 개념을 캡슐화하라