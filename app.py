import os
import sys

def organize_files():
    """
    智慧檔案整理腳本
    自動將 Downloads 資料夾中的檔案按照類型分類
    """
    
    # 定義分類規則 - key 是資料夾名稱, value 是該分類包含的副檔名列表
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".doc", ".docx", ".txt"],
        "Music": [".mp3", ".wav"],
        "Others": []  # 其他未分類檔案
    }
    
    # 設定 Downloads 資料夾路徑
    downloads_folder = "Downloads"
    
    # 檢查 Downloads 資料夾是否存在
    if not os.path.exists(downloads_folder):
        print(f"錯誤：找不到 {downloads_folder} 資料夾")
        print("請先建立 Downloads 資料夾並放入測試檔案")
        return
    
    print(f"開始整理 {downloads_folder} 資料夾...")
    
    # 讀取 Downloads 資料夾裡的所有項目
    try:
        items = os.listdir(downloads_folder)
    except Exception as e:
        print(f"讀取資料夾時發生錯誤: {e}")
        return
    
    # 統計移動的檔案數量
    moved_files = 0
    
    # 遍歷每個項目
    for item in items:
        item_path = os.path.join(downloads_folder, item)
        
        # 只處理檔案，跳過資料夾
        if os.path.isfile(item_path):
            # 取出副檔名
            _, file_extension = os.path.splitext(item)
            file_extension = file_extension.lower()  # 轉成小寫避免大小寫問題
            
            # 決定檔案要放到哪個分類資料夾
            target_folder = "Others"  # 預設分類
            
            for folder_name, extensions in file_types.items():
                if file_extension in extensions:
                    target_folder = folder_name
                    break
            
            # 建立目標資料夾路徑
            target_folder_path = os.path.join(downloads_folder, target_folder)
            
            # 檢查目標資料夾是否存在，不存在就建立
            if not os.path.exists(target_folder_path):
                try:
                    os.makedirs(target_folder_path)
                    print(f"建立資料夾: {target_folder_path}")
                except Exception as e:
                    print(f"建立資料夾失敗: {e}")
                    continue
            
            # 移動檔案
            source_path = item_path
            destination_path = os.path.join(target_folder_path, item)
            
            try:
                # 檢查目標位置是否已有同名檔案
                if os.path.exists(destination_path):
                    print(f"警告: {destination_path} 已存在，跳過 {item}")
                    continue
                
                os.rename(source_path, destination_path)
                print(f"移動 {item} → {target_folder}/")
                moved_files += 1
                
            except Exception as e:
                print(f"移動檔案 {item} 時發生錯誤: {e}")
    
    print(f"\n整理完成！共移動了 {moved_files} 個檔案")
    print("最終資料夾結構:")
    
    # 顯示最終的資料夾結構
    show_folder_structure(downloads_folder)

def show_folder_structure(folder_path, indent=""):
    """
    顯示資料夾結構
    """
    try:
        items = sorted(os.listdir(folder_path))
        for item in items:
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                print(f"{indent}├── {item}/")
                show_folder_structure(item_path, indent + "│   ")
            else:
                print(f"{indent}├── {item}")
    except Exception as e:
        print(f"讀取資料夾結構時發生錯誤: {e}")

if __name__ == "__main__":
    print("=== 智慧檔案整理腳本 ===")
    print("這個腳本會自動整理 Downloads 資料夾中的檔案")
    print()
    
    # 執行檔案整理
    organize_files()