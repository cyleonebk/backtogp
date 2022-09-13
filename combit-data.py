import pandas as pd
import os

dir = r"D:\User\Downloads\BTC-1H"
# wk = os.walk( dir, topdown=False)
file_list = os.listdir(dir)
for name in file_list:
    csv_file = os.path.join(dir, name)
    pd_file = pd.read_csv(csv_file)
    pd_file.to_csv(os.path.join(dir, "btc-1h-combine.csv"), index=False, header=False, mode='a+')

# print(file_list)
# for root, dirs, files in wk:
#     for name in files:
#         pd.read_csv(os.path.join(root, name))
