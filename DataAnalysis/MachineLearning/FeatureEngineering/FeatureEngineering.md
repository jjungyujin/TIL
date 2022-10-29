# Feature Engineering

## 데이터처리 전략

1. 모판은 흔들리지 않는다
2. 하나의 셀은 다시 실행해도 같은 결과
3. 전처리 완료 후 함수화
4. column list 관리
5. 데이터는 type별로 관리
6. 데이터 노트 작성

### 데이터모판 만들기

데이터를 하나의 판으로 다루기  
train, test의 각 columns에 같은 전처리 적용  
train, test의 데이터 수를 index로 기억하여 split

### 데이터 타입

- Numeric : 정량적 측정 가능, 단위가 있는 데이터
- Nominal : 범주로 분류가 가능
- Ordinal : 범주로 분류가 가능하면서 순서가 있음

### 데이터 노트 작성

주로 엑셀 활용  
데이터처리 내용 및 방향 정리  
데이터에 대한 아이디어 정리

### Issue 1. 결측치

그룹별 다른 대표값으로 채우기 : `fillna, groupby, transform`  
관련 있는 feature 찾기

### Issue 2. labeling된 데이터

category data

> one-hot Encoding : `get_dumies`

ordinary data

> `map` 함수로 범주형 데이터로 만들어준 후 one-hot Encoding

Data Binning (데이터 구간 나누기)

> `pd.cut(df['column'], bins, labels)`

label encoding by sklearn

> 새로운 데이터 입력 시 기존 labeling 규칙을 그대로 적용해야함  
> `fit` & `transform` : 규칙 생성과 적용

### Issue 3. Scale 차이

scaler : `MinMax, Standardization, Normalization`

## Generation & Selection

feature를 많이 만들어낸 후 correlation 확인  
너무 많은 feature는 overfitting의 원인 - selection 필요

## Feature Generation

### Log Transformations

선형모델은 데이터가 정규분포일 때 적합  
데이터의 분포가 극단적으로 모였을 때 정규분포와 유사해지도록 데이터 변형  
`np.log, np.exp` 함수 사용

### Mean Encoding

y값에 대한 분포 활용  
category별 분포의 값을 취할 수 있음  
overfitting 방지를 위해 smoothing 사용
|job|job_mean|target|
|---|---|---|
|Doctor|0.5|0|
|Doctor|0.5|1|
|Doctor|0.5|0|
|Doctor|0.5|1|
|Teacher|1|1|
|Teacher|1|1|

### Interaction feature

기존 features 조합으로 새로운 feature 생성  
ex) categorical combination

> Pclass, Embarked -> Embarked_Pclass  
> One-hot Encoding 처리

## Feature Selection

### 주의사항

- 예측시에도 확보 가능한 feature 인가 ?
- scale은 일정한가, 비율적 표현이 가능한가 ?
- 새롭게 등장하는 category data는 ?
- 너무 극단적인 분포는 아닌가 ?

### 삭제해야할 feature

- correlation이 너무 높은 feature
- 전처리가 완료된 str feature
- ID와 같은 feature
