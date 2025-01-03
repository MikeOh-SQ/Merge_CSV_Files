# CSV 파일 통합 스크립트

이 저장소는 지정된 폴더 내의 여러 CSV 파일을 하나로 통합하는 파이썬 스크립트를 제공합니다. 통합 과정에서 파일 이름을 기준으로 정렬하며, 중복 데이터를 제거합니다.

## 주요 기능

- 지정된 폴더 내 CSV 파일 자동 탐색
- 파일 이름 기준 정렬 후 데이터 통합
- 중복 데이터 제거
- 통합된 데이터 저장

## 설치 방법

1. 이 저장소를 클론합니다:
   ```bash
   git clone <repository_url>
   ```

2. 필요한 파이썬 패키지를 설치합니다:
   ```bash
   pip install pandas
   ```

## 사용 방법

1. 스크립트를 실행하기 전에 아래 설정을 확인하세요:
   - `folder_path`: CSV 파일들이 저장된 폴더 경로
   - `output_file`: 통합된 파일의 이름 (기본값: `파일이름.csv`)

2. 스크립트를 실행합니다:
   ```bash
   python merge_csv_files.py
   ```

3. 출력 내용:
   - 통합된 CSV 파일이 지정된 폴더에 저장됩니다.
   - 통합된 데이터는 중복이 제거된 상태입니다.

## 의존성

- Python 3.6+
- 라이브러리:
  - `pandas`

아래 명령어로 의존성을 설치하세요:
```bash
pip install pandas
```

## 파일 설명

- `merge_csv_files.py`: 여러 CSV 파일을 통합하고 중복을 제거한 후 저장하는 메인 스크립트
- 저장된 파일: 통합된 데이터가 포함된 CSV 파일 (`파일이름.csv`)

## 데이터 처리 과정

1. 지정된 폴더 내 모든 `.csv` 파일을 탐색
2. 파일 이름 기준으로 정렬
3. 각 파일을 읽어 데이터프레임으로 변환 후 통합
4. 중복 데이터 제거
5. 통합된 데이터 저장

## 주의 사항

- 폴더 경로가 올바른지 확인하세요.
- CSV 파일 형식이 올바르지 않을 경우 스크립트가 실패할 수 있습니다.

## 감사의 말

- 데이터 처리 및 통합에 사용된 `pandas` 라이브러리에 감사드립니다.
