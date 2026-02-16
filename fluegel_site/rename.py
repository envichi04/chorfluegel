import os

# --- 設定 ---
target_word = "第"
new_word = '\n第'
# 実行するディレクトリ（'.' はこのプログラムがある場所を指します）
base_path = '.'

def replace_in_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # HTMLファイルだけを対象にする
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                
                # ファイルを読み込む
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 文字列を置換
                if target_word in content:
                    new_content = content.replace(target_word, new_word)
                    
                    # 上書き保存
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    print(f"置換完了: {file_path}")

if __name__ == "__main__":
    print(f"'{target_word}' を '{new_word}' に置換します。開始...")
    replace_in_files(base_path)
    print("すべての処理が完了しました。")