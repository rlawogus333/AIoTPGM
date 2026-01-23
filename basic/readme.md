# Python · OpenCV · YOLO · AI Practice Repository

이 레포지토리는 **Python 기반 AI / 컴퓨터 비전 실습 기록용 저장소**입니다.  
파이썬 기초부터 데이터 분석, 시각화, OpenCV 영상처리, YOLO 객체 탐지,  
그리고 TensorFlow / Keras 기반 딥러닝 모델링까지 단계적으로 연습한 코드들을 정리합니다.

단순 코드 모음이 아니라  
👉 **개념 이해 → 실습 → 결과 확인 → 재현 가능성 확보**  
를 목표로 구성했습니다.

---

## 🧩 사용 기술 스택

- **Language**: Python
- **Data / Math**: NumPy, Pandas
- **Visualization**: Matplotlib
- **Computer Vision**: OpenCV
- **Object Detection**: YOLO
- **Deep Learning**: TensorFlow, Keras

---

## 📁 레포지토리 구성

> 폴더명은 주제 기준으로 구성되어 있으며,  
> 각 폴더 안에는 `.py` 또는 `.ipynb` 실습 파일이 포함됩니다.



---

## 🧪 실습 내용 요약

### 1️⃣ Python
- 기본 문법, 자료구조
- 함수, 클래스(OOP)
- 파일 입출력, 예외 처리

### 2️⃣ NumPy
- ndarray 구조 이해
- 행렬 연산 및 벡터화
- 브로드캐스팅 개념

### 3️⃣ Pandas
- 데이터 로딩 및 정제
- 결측치 처리
- groupby / merge / apply

### 4️⃣ Matplotlib
- Line / Bar / Histogram
- Subplot 구성
- 데이터 비교 시각화

### 5️⃣ OpenCV
- 이미지 읽기/저장
- 색공간 변환(BGR, Gray)
- Blur, Edge Detection
- Contour, Feature Detection
- 영상/웹캠 처리

### 6️⃣ YOLO
- 객체 탐지 추론(Inference)
- Bounding Box 시각화
- 데이터셋 구조 및 라벨 포맷 이해
- YOLO 기반 실습 코드 정리

### 7️⃣ TensorFlow / Keras
- 모델 구조 설계
- 학습 및 평가
- Loss / Optimizer 이해
- 모델 저장 및 로드

---

## ⚙️ 실행 환경

- Python 3.9 이상 권장
- 가상환경 사용 권장

### 가상환경 생성
```bash
python -m venv .venv


### 가상환경 활성화
# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate


### 라이브러리 설치
pip install -r requirements.txt


### requirements.txt 예시
numpy
pandas
matplotlib
opencv-python
tensorflow
keras
tqdm
