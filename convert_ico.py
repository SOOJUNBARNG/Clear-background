from PIL import Image

def convert_png_to_ico(input_path, output_path):
    # PNG画像を開く
    img = Image.open(input_path)
    
    # アイコンに含まれるサイズを指定（一般的なサイズセット）
    # 指定しない場合は、元の画像サイズに基づいて自動生成されます
    icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    
    # 指定したサイズを含めてICOとして保存
    img.save(output_path, format='ICO', sizes=icon_sizes)
    print(f"変換完了: {output_path}")

# 実行
convert_png_to_ico('job_cropped.png', 'job_ico.ico')