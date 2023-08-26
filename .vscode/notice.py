import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# todo : DATA 뽑기

# TODO : SPEC과 비교해서 보내줄 데이터 판단

# TODO : 한줄씩 확인해서 알림 발송

# data = {
#     'EQP': ['Alice', 'Bob', 'Charlie', 'David'],
#     'HEAD': [25, 30, 22, 28],
#     'PAD': [28, 17, 32, 37]
# }

# df = pd.DataFrame(data)

# spec = {
#     'EQP': ['Alice', 'Bob', 'Charlie', 'David'],
#     'HEAD': [20, 28, 20, 30],
#     'PAD': [20, 28, 20, 30]
# }

# # HEAD이 spec 이상인 행 필터링
# HEAD_filtered = df[df['HEAD'] >= 28]

# # PAD가 30 이상인 행 필터링
# PAD_filtered = df[df['PAD'] >= 30]

# # 결과 출력
# print("HEAD이 28 이상인 사람:")
# for index, row in HEAD_filtered.iterrows():
#     print(f"EQP: {row['EQP']}, HEAD 값: {row['HEAD']}")

# print("\nPAD가 30 이상인 사람:")
# for index, row in PAD_filtered.iterrows():
#     print(f"EQP: {row['EQP']}, PAD 값: {row['PAD']}")


data = {
    'EQP': ['KCCU05', 'KFOX01', 'KSOX01', 'KUCU01'],
    'HEAD': ['2023-05-10', '2023-05-20', '2023-08-23', '2023-07-22'],
    'PAD': ['2023-08-20', '2023-08-20', '2023-08-23', '2023-08-22'],
    'DISK': ['2023-08-20', '2023-08-20', '2023-08-23', '2023-08-22']
}

df = pd.DataFrame(data)

spec_data = {
    'EQP': ['KCCU05', 'KFOX01', 'KSOX01', 'KUCU01'],
    'HEAD': [90, 90, 90, 90],
    'PAD': [5, 5, 5, 5],
    'DISK': [5, 5, 5, 5]
}


spec_df = pd.DataFrame(spec_data)
filtered_rows = []

# for col, value in filter_conditions.items():
#     filtered_rows.append(df[df[col] >= value])

# for i, filtered_df in enumerate(filtered_rows):
#     col_name = list(filter_conditions.keys())[i]
#     print(f"{col_name}이 {filter_conditions[col_name]} 이상인 사람:")
#     for index, row in filtered_df.iterrows():
#         print(f"EQP: {row['EQP']}, {col_name} 값: {row[col_name]}")
#     print()

# 비교해서 큰 값을 찾아 출력
for index, row in df.iterrows():
    name = row['EQP']
    comparison_result = []

    for col in df.columns[1:]:
        col_df = row[col]
        col_spec_df = spec_df[spec_df['EQP'] == name][col].values[0]
        col_df_date = datetime.strptime(col_df, '%Y-%m-%d').date()
        col_spec_df_date = (
            datetime.now() - timedelta(days=int(col_spec_df))).date()

        if col_df_date < col_spec_df_date:
            comparison_result.append((col, col_df, col_spec_df))

    if comparison_result:
        print(f"{name}:")
        for col, col_df, col_spec_df in comparison_result:
            print(f" - {col}: 교체일 = {col_df} (Spec = {col_spec_df})")
