import os

# 檔案分類規則
file_types = {  
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Music": [".mp3", ".wav"],
    "Others": []
}

print("檔案整理程式開始執行...")

# 檢查Downloads資料夾
if not os.path.exists("Downloads"):
    print("找不到Downloads資料夾!")
    exit()

# 讀取檔案清單
file_list = os.listdir("Downloads")
print("找到的檔案:", file_list)

# 開始整理檔案
for file_name in file_list:
    file_path = os.path.join("Downloads", file_name)
    
    # 只處理檔案，跳過資料夾
    if not os.path.isfile(file_path):
        continue
    
    # 取得副檔名
    name, ext = os.path.splitext(file_name)
    ext = ext.lower()
    
    # 決定要放到哪個資料夾
    folder_name = "Others"  # 預設分類
    
    for folder, extensions in file_types.items():
        if ext in extensions:
            folder_name = folder
            break
    
    # 建立目標資料夾
    target_folder = os.path.join("Downloads", folder_name)
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        print(f"建立資料夾: {folder_name}")
    
    # 移動檔案
    old_location = os.path.join("Downloads", file_name)
    new_location = os.path.join(target_folder, file_name)
    
    os.rename(old_location, new_location)
    print(f"移動 {file_name} 到 {folder_name} 資料夾")

print("檔案整理完成!")