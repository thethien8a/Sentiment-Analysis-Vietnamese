import pandas as pd
import os

df = pd.read_csv('comment_data/Tram_dung_chan_Jack.csv', encoding='utf-8')
print("Số dòng gốc:", len(df))

df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

output_path = 'comment_data/Tram_dung_chan_Jack_shuffled.xlsx'

if os.path.exists(output_path):
    print(f"File {output_path} đã tồn tại.")
else:
    df_shuffled.to_excel(output_path, index=False, engine='openpyxl')
    print(f"Đã tạo file: {output_path}")