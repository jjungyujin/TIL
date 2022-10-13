# 머신러닝

컴퓨터가 알아서 데이터로부터 규칙을 발견하도록 하는 것

## ML Process

1. data 확보
2. data cleaning, feature engineering, EDA
3. train data
4. ML model
5. model test
6. evaluation

## 데이터

### 독립변수와 종속변수

종속변수 (dependent variable)

- 독립변수에 영향을 받는 특성
- (소문자) y
- A.k.a target variable, output variable, label

독립변수(independent variable)

- 종속변수에 영향을 주는 것으로 여겨지는 특성들
- (대문자) X
- a.k.a predictor, input variable, regressor

### 데이터로 해볼 수 있는 질문

예측(Prediction)

- 독립변수가 주어진 상태에서 종속변수의 값을 추측

추론(Inference)

- 독립변수와 종속변수간의 설명가능한 관계 파악
- 생성과정을 설명할 수 있는 명확한 모델이 있을 때 가능
- 모든 모델에서 추론이 가능하진 않음

### 예측과 추론의 trade-off

예측에 특화된 모델은 추론 능력이 떨어지고  
추론에 특화된 모델은 예측 능력이 떨어짐

## 모형

예측과 추론을 위해서는 데이터를 활용하여 모형을 만들어야 함  
독립변수와 종속변수의 관계에 대한 가설을 수학적으로 표현

### 패러미터

모델안에서 독립변수와 종속변수 간의 관계를 표현하기 위해 조절할 수 있는 매개변수

### 모델의 학습

학습 : 주어진 데이터를 가장 잘 나타내는 패러미터를 찾아가는 과정

### 모형의 분류

예측해야 하는 값이 실수인가 ?

- 회귀 (Regression)
- 분류 (Classification)

정답을 알고있는 데이터인가 ?

- 지도학습 (Supervised Learning)
- 비지도 학습 (UnSupervised Learning)

패러미터로 모델을 표현할 수 있는가 ?

- Parametric Method
- Non-parametric Method
