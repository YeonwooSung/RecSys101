# Note - Recommendation System

## Collaborative Filtering vs Content Based Filtering

- Collaborative Filtering 모델의 핵심 가정은 나와 비슷한 취향을 가진 유저들은 어떠한 아이템에 대해 비슷한 선호도를 가질 것이라는 점이다.

- CB 모델의 경우, 유저-아이템의 상호작용 데이터 없이도, 아이템 자체의 이름, 카테고리, 상세 설명, 이미지 등을 활용해 유사성을 판단하고 비슷한 아이템을 추천할 수 있다.

## Matrix Factorization

- MF는 Collaborative Filtering 기법들 중 모델 기반 협업 필터링 기법의 가장 대표적인 방법들 중 하나인 latent factor model에 사용되는 기법이다.

- 주어진 user-item 행렬에 대해서 공백 값을 계산하기 위해 주어진 행렬을 근사하기 위해 행렬 U와 V를 계산하고, UxV^T의 계산을 통해 근사 행렬 계산

- 근사 행렬 계산을 위해서 인수 분해 과정을 계속 진행하면서 U와 V의 값을 수렴할 때까지 업데이트 시킴
