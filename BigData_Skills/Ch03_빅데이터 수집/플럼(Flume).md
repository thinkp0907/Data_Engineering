# 빅데이터 수집

빅데이터 시스템 구축은 **수집**에서부터 시작된다. 빅데이터 프로젝트에서는 여러 공정 단계가 있는데, 그중 수집이 전체 고정 과정의 절반 이상을 차지한다.



![image-20210408105322482](https://github.com/thinkp0907/Data_Engineering/blob/main/BigData_Skills/img/%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%88%98%EC%A7%91%20%EC%A0%88%EC%B0%A8.PNG)

**[빅데이터 수집 절차]**

최근에는 수집 기술들이 매우 빠르게 발전하고 있다. 과거에 빅데이터의 전형적인 프로세싱은 **수직/적재 후, 맵리듀스 기반의 주기적인 배치성 분석**을 수행하는 것이었으나 이제는 수집과 동시에 분석을 수행하는 **ESP(Event Stream Processing)**/**CEP(Complex Event Processing)** 기술들이 빅데이터의 수집 영역에 적용되고 있는 추세다.



## 빅데이터 수집에 활용할 기술

### 플럼

#### 플럼 소개

플럼(Flume)은 빅데이터를 수집할 때 다양한 수집 요구사항들을 해결하기 위한 기능으로 구성된 소프트웨어다. 데이터를 원천으로부터 수집할 때 통신 프로토콜, 메시지 포맷, 발생 주기, 데이터 크기 등으로 많은 고민을 하게 되는데 플럼은 이러한 고민을 쉽게 해결할 수 있는 기능과 아키텍처를 제공한다. 



| 주요 구성 요서 | 설명                                                         |
| -------------- | ------------------------------------------------------------ |
| Source         | 다양한 원천 시스템의 데이터를 수집하기 위해 Avro, Thrift, JMS, Spool Dir, Kafka등 여러 주요 컴포넌트를 제공하며, 수집한 데이터를 Channel로 전달 |
| Sink           | 수집한 데이터를 Channel로부터 전달받아 최종 목적지에 저장하기 위한 기능으로 HDFS, Hive, Logger, Avro, ElasticSearch, Thrift등을 제공 |
| Channel        | Source와 Sink를 연결하며, 데이터를 버퍼링하는 컴포넌트로 메모리, 파일, 데이터베이스를 채널의 저장소로 활용 |
| Interceptor    | Source와 Channel 사이에서 데이터 필터링 및 가공하는 컴포넌트로서 Timestamp, Host, Regex Filtering 등을 기본 제공하며, 필요 시 사용자 정의 Interceptor를 추가 |
| Agent          | Source -> (Interceptor) -> Channel -> Sink 컴포넌트 순으로 구성된 작업 단위로 독립된 인스턴스로 생성 |

#### 플럼 아키텍처

플럼 메커니즘은 Source, Channel, Sink만을 활용하는 매우 단순하면서 직관적인 구조를 갖는다. 플럼의 Source에서 데이터를 로드하고, Channel에서 데이터를 임시 저장해 놓았다가, Sink를 통해 목적지에 데이터를 최종 적재한다. 이러한 메커니즘을 기반으로 플럼은 수집 요건에 따라 다양한 분산 아키텍처 구조로 확대할 수 있으며, 아래의 대표적인 4가지 구성 방안을 소개한다.

![image-20210408110630230](https://github.com/thinkp0907/Data_Engineering/blob/main/BigData_Skills/img/%ED%94%8C%EB%9F%BC%20%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98%20%EC%9C%A0%ED%98%951.PNG)

**[플럼 아키텍처 유형1]**

**플럼 아키텍처 유형1**은 가장 단순한 플럼 에이전트 구성이다. 원천 데이터를 특벼한 처리 없이 단순 수집/적재 할 때 주로 활용한다.

![image-20210408110930975](https://github.com/thinkp0907/Data_Engineering/blob/main/BigData_Skills/img/%ED%94%8C%EB%9F%BC%20%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98%20%EC%9C%A0%ED%98%952.PNG)

**[플럼 아키텍처 유형2]**

**플럼 아키텍처 유형2**는 원천 데이터를 수집할 때 Interceptor를 추가해 데이터를 가공하고, 데이터의 특성에 따라 Channel에서 다수의 Sink 컴포넌트로 라우팅이 필요할 때 구성한다. 또한 한 개의 플럼 에이전트 안에서 두 개 이상의 Source-Channel-Sink 컴포넌트 구성 및 관리도 가능하다.



![플럼 아키텍처 유형3](https://github.com/thinkp0907/Data_Engineering/blob/main/BigData_Skills/img/%ED%94%8C%EB%9F%BC%20%EC%95%84%ED%82%A4%ED%85%8D%EC%B2%98%20%EC%9C%A0%ED%98%953.PNG)

**[플럼 아키텍처 유형3]**

**플럼 아키텍처 유형3**은 플럼 에이전트에서 수집한 데이터를 플럼 에이전트 2, 3에 전송할 때 로드밸런싱, 복제, 페일오버(failover)등의 기능을 선택적으로 수행할 수 있다. 수집해야 할 원천 시스템은 한 곳이지만 높은 성능과 안정성이 필요할 때 주로 사용되는 아키텍처다.



![image-20210408112034134](C:\Users\Chorlock\AppData\Roaming\Typora\typora-user-images\image-20210408112034134.png)

**[플럼 아키텍처 유형4]**

**플럼 아키텍처 유형4**는 수집해야 할 원천 시스템이 다양하고 대규모의 데이터가 유입될 때 사용하는 플럼의 분산 아키텍처다. 플럼 에이전트 1, 2, 3, 4에서 수집한 데이터를 플럼 에이전트 5에서 집계(aggregation)하고, 이때 플럼 에이전트 6으로 이중화해서 성능과 안정성을 보장하는 구성이다.



#### 플럼 활용 방안

플럼은 진행할 파일럿 프로젝트 '스마트카'에서 발생하는 로그를 직접 수집하는 역할을 담당한다. 발생하는 로그 유형에 따라 두 가지 플럼 에이전트를 구성할 것이다.



첫 번째로 100대의 스마트카에 대한 상태 정보 로그 파일이 로그 시뮬레이터를 통해 매일 생성된다. 이렇게 만들어진 상태 정보 파일을 플럼 에이전트가 일 단위로 수집해서 하둡에 적재하고 향후 대규모 배치 분석에 활용한다.

![image-20210408113404763](https://github.com/thinkp0907/Data_Engineering/blob/main/BigData_Skills/img/%EC%8A%A4%EB%A7%88%ED%8A%B8%EC%B9%B4%EC%97%90%EC%84%9C%EC%9D%98%20%ED%94%8C%EB%9F%BC%20%ED%99%9C%EC%9A%A9%20%EB%B0%A9%EC%95%881.PNG)

**['스마트카'에서의 플럼 활용 방안1 - 스마트카 상태 정보의 일 단위 수집]**

두 번째로 스마트카 운전자 100명의 운행 정보를 실시간으로 기록하는 로그 파일이 로그 시뮬레이터에 의해 만들어지는데, 이때 발생과 동시에 플럼 에이전트가 수집해서 카프카에 전송한다.



![image-20210408113545412](https://github.com/thinkp0907/Data_Engineering/blob/main/BigData_Skills/img/%EC%8A%A4%EB%A7%88%ED%8A%B8%EC%B9%B4%EC%97%90%EC%84%9C%EC%9D%98%20%ED%94%8C%EB%9F%BC%20%ED%99%9C%EC%9A%A9%20%EB%B0%A9%EC%95%882.PNG)

**['스마트카'에서의 플럼 활용 방안2 - 스마트카 운전자의 운행 정보를 실시간으로 수집]**



