# Self-Driving-Simulation
Udemy Courses : Develop Autonomous car with Python 

Certification : [Certification Self-Driving Car.pdf](https://github.com/user-attachments/files/16236361/Certification.Self-Driving.Car.pdf)

*- upload data on master branch!!*

### Learning Objectives

| 항목                                                         | 설명                                                                 |
|--------------------------------------------------------------|----------------------------------------------------------------------|
| 기본 개념 학습                                                | 자율 주행 자동차의 기본 개념, 기술, 가능성 및 제한 사항을 이해 |
| 자율 주행 기능 작동 방식 이해                                  | 자율 주행 기능이 작동하는 방식을 학습하고 자동차의 스스로 운전 능력을 이해 |
| PyGame와 NEAT을 활용한 시뮬레이션            | PyGame과 NEAT을 사용하여 자율 주행 자동차 시뮬레이션 프로젝트를 처음부터 구축|
| 자율 주행 자동차 테스트                                       | 자율 주행 자동차 판단, 센서 통합 및 충돌 방지 기능 테스트 |

### Project Structure 

프로젝트는 다음과 같은 구조로 진행됩니다:
- **autonomous_car.py**: 메인 실행 파일, 자율 주행 자동차 시뮬레이션 코드
- **neat_config.txt**: NEAT 알고리즘 설정 파일
- **cartrack.png** : GIMP Tool 활용하여 주행 맵 제작
- **GreenCarAsset.png** : 시뮬레이션 차량 icon 

### How to Execution Self-Driving Simulation 

1. **환경 설정**: 필요한 라이브러리 설치 및 설정
   
|||
|:---:|:---|
|**Develop EnV**|<img src="https://img.shields.io/badge/VISUAL STUDIO CODE-007ACC?style=for-the-badge&logo=VisualStudioCode&logoColor=white">|
|**Language**|<img src="https://img.shields.io/badge/python 3.11.4-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">|
|**Library**|<img src="https://github.com/user-attachments/assets/a347d5e0-0c90-492a-9add-15f12b8e2354" width=100 height=50> <img src= "https://github.com/user-attachments/assets/9d908855-2edc-42c7-ad3b-80973d475251" width=300 height=50>|

2. **실행 방법**
```sh
git clone https://github.com/AUTO-KKYU/Self-Driving-Simulation.git
git branch
git checkout master
```
- before execute the file, check the cartrack and configuration, car abs path
```sh
python3 autonomous car.py
```
### Summary of Fuction in this code [autonomous car.py]

| 함수 이름                   | 기능 요약                                                                                   |
|----------------------------|---------------------------------------------------------------------------------------------|
| `autonomouscar.__init__`   | 자율 주행 자동차 객체 초기화                                                                  |
| `autonomouscar.initialize` | 자동차 초기 설정 수행                                                                        |
| `autonomouscar.position`   | 자동차 위치를 화면에 그림                                                                     |
| `autonomouscar.avoid_collision` | 충돌을 피하기 위해 장애물과의 충돌 여부 확인                                                  |
| `autonomouscar.radardetection` | 레이더로부터 장애물까지의 거리를 감지                                                        |
| `autonomouscar.positionupdate` | 자동차의 위치 및 각도 업데이트                                                               |
| `autonomouscar.radar_data` | 레이더 데이터를 반환                                                                         |
| `autonomouscar.add_reward` | 주행 거리에 따른 보상 계산                                                                   |
| `autonomouscar.check_alive` | 자동차 생존 여부 확인                                                                        |
| `run_autonomouscar`        | NEAT 알고리즘을 사용하여 자율 주행 자동차 시뮬레이션 실행                                     |
| `simulation`               | NEAT 설정을 사용하여 자율 주행 자동차 시뮬레이션 실행 및 최적화된 자동차 반환                  |

### Simulation Video 

## 이미지 예시

<table>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/dd9f92d8-2adf-4d58-8318-7911e5c39351" width="480" height="320">
    </td>
    <td>
      <img src="https://github.com/user-attachments/assets/5c9f9e94-ef5f-45c9-a047-12de40bad777" width="480" height="320">
    </td>
  </tr>
  <tr>
    <td align="center">Self-Driving Simulation</td>
    <td align="center">Radar Visualization -> Until Reaching an Obstacle</td>
  </tr>
</table>




