# Recommendation System

추천시스템이란 User와 Item으로 구성된 시스템이다.

- 특정 User가 좋아할 Item을 추천
- 비슷한 Item을 좋아할 User를 추천

Item이든 User든 관심 가질만 한 정보를 추천한다.
이때, Item은 각 플랫폼마다 정의하는 종류가 다를 것이다.

추천시스템은 profiling을 한 User와 Item을 통해 적절한 것을 추천한다.
또, 추천시스템은 User와 Item의 관계를 파악하고 점수화한다.

## 추천 점수

- 분석된 User와 Item 정보를 바탕으로 추천점수 계산
- User 또는 Item 프로필에서 어떤 정보를 사용할 지에 따라 추천 알고리즘을 결정
- 사용자 또는 아이템을 추천하기 위해 각각의 사용자 또는 아이템에 대한 정량화된 기준이 필요

## 추천시스템 vs 검색 서비스

- 추천시스템은 Push Information
- 검색 서비스는 Pull Information

추천시스템은 랭킹 문제 또는 예측 문제라고 정의할 수 있다.

## 추천 시스템의 한계

### Scalability

학습 또는 분석에 사용한 data와는 전혀 다른 실전 data

### Cold-start problem

추천시스템을 위한 data 부족

### Privacy preserving

개인정보등이 제일 중요하지만, 직접적으로 사용하기 어려움

### 기타 문제점들

- Mobile devices and Usage Contexts
- Long-term Short-term User preferencs
