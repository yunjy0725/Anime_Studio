<img width="1672" height="941" alt="anime_studio_result (2)" src="https://github.com/user-attachments/assets/c44c7d33-714c-4651-b2ba-2de6151406e6" />
# 🎨 Anime Studio

**AI-powered Anime Style Photo Converter**

사진을 업로드하거나 직접 촬영하면 AI를 활용해 다양한 애니메이션 그림체로 변환해 주는 웹 애플리케이션입니다.

사용자가 원하는 그림체를 선택하여 자신만의 애니메이션 스타일 이미지를 만들어 볼 수 있습니다.

---

## ✨ 주요 기능

- 📁 **사진 업로드**: 원하는 이미지 파일 업로드
- 📷 **카메라 촬영**: 웹캠을 이용한 사진 촬영
- 🎨 **다양한 그림체 선택**: 디즈니풍, 픽사풍, 한국 웹툰풍
- 🖼️ **이미지 변환**: OpenAI 이미지 API를 활용한 AI 이미지 변환
- 🔍 **변환 결과 미리보기**: 원본 사진과 변환된 이미지 비교
- 💾 **이미지 다운로드**: 변환된 결과를 PNG 파일로 저장

---

## 🎭 그림체별 변환 결과

각 그림체를 선택하여 직접 테스트한 결과입니다.

### 1. 디즈니풍 (Disney Style)

부드러운 색감과 자연스러운 얼굴 표현을 중심으로 한 애니메이션 스타일입니다.

<img width="1672" height="941" alt="anime_studio_result" src="https://github.com/user-attachments/assets/1dd221ea-adce-43e9-b2d9-c651ebf1a552" />


![Disney Style](images/disney.png)

### 2. 픽사풍 (Pixar Style)

입체적인 3D 애니메이션 표현과 개성 있는 얼굴 비율이 특징입니다.

코와 눈, 입 등의 특징이 과장되게 표현될 수 있으며, 풍부한 표정과 생동감 있는 캐릭터 느낌을 구현합니다.

<img width="1672" height="941" alt="anime_studio_result (2)" src="https://github.com/user-attachments/assets/48ab8e19-3d47-4ccf-a46c-a9735ee3793d" />


![Pixar Style](images/pixar.png)

### 3. 한국 웹툰풍 (Korean Webtoon Style)

깔끔한 선화와 선명한 색감, 한국 웹툰 특유의 캐릭터 표현을 적용한 스타일입니다.

<img width="1672" height="941" alt="anime_studio_result (3)" src="https://github.com/user-attachments/assets/8bcd7cc3-3aff-484f-ab5f-023c59a13018" />


![Korean Webtoon Style](images/webtoon.png)

---

## 🛠️ 기술 스택 (Tech Stack)

| 구분 | 사용 기술 |
|---|---|
| Programming Language | Python |
| Web Framework | Streamlit |
| AI Image Generation | OpenAI Image API |
| Image Processing | Pillow |
| Version Control | Git & GitHub |

---

## 📂 프로젝트 구조

```text
Anime_Studio/
│
├── add.py
├── requirements.txt
├── .gitignore
│
└── images/
    ├── disney.png
    ├── pixar.png
    └── webtoon.png
```

---

## 🚀 실행 방법 (Installation)

### 1. 저장소 복제

```bash
git clone https://github.com/yunjy0725/Anime_Studio.git
```

### 2. 프로젝트 폴더 이동

```bash
cd Anime_Studio
```

### 3. 라이브러리 설치

```bash
pip install -r requirements.txt
```

### 4. API 키 설정

프로젝트 폴더에 `.streamlit/secrets.toml` 파일을 생성하고 OpenAI API 키를 설정합니다.

```toml
OPENAI_API_KEY = "본인의_API_KEY"
```

### 5. 애플리케이션 실행

```bash
streamlit run add.py
```

---

## 📖 사용 방법 (How to Use)

1. 웹 애플리케이션에 접속합니다.
2. 사진을 업로드하거나 카메라로 직접 촬영합니다.
3. 원하는
