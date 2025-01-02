import os
import pandas as pd

# 폴더 경로 지정
folder_path = "/CSV폴더/"  # 통합하려는 CSV 파일들이 있는 폴더 경로로 변경
output_file = "파일이름름.csv"  # 통합된 파일 이름

# 폴더 내 파일 목록 가져오기
file_list = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# 파일 이름 기준 정렬 (날짜 이름 기준)
file_list.sort()

# CSV 파일 읽어서 데이터프레임에 추가
merged_data = pd.DataFrame()

for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)
    data = pd.read_csv(file_path)
    merged_data = pd.concat([merged_data, data], ignore_index=True)

# 중복 데이터 제거
merged_data = merged_data.drop_duplicates()

# 통합된 데이터 저장
output_path = os.path.join(folder_path, output_file)
merged_data.to_csv(output_path, index=False)

print(f"통합 완료: {output_path}")
