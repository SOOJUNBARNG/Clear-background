# from rembg import remove
# from PIL import Image
# import io

# # 1. 入力画像を開く
# input_path = 'logo.png'  # 背景を消したい画像
# output_path = 'logo_output.png' # 保存先（背景を透明にするためpngを推奨）

# input_image = Image.open(input_path)

# # 2. 背景を削除
# output_image = remove(input_image)

# # 3. 保存
# output_image.save(output_path)

from rembg import remove
from PIL import Image
import numpy as np

def process_image(input_path, output_path):
    # 1. 画像を読み込み
    img = Image.open(input_path).convert("RGBA")

    # 2. rembgでAIによる背景削除を実行
    # (これだけで多くの背景は消えますが、残った白を次で処理します)
    img = remove(img)

    # 3. numpy配列に変換して「白」を透明にする
    data = np.array(img)
    
    # RGBAの各チャンネルを取得
    r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
    
    # 「真っ白(255, 255, 255)」に該当するピクセルを探す
    # 完全に白に近い色も消したい場合は 250 などの閾値を調整してください
    white_areas = (r > 250) & (g > 250) & (b > 250)
    
    # 白い部分のアルファチャンネル（透明度）を 0 に設定
    data[white_areas, 3] = 0

    # 4. 画像を保存
    result = Image.fromarray(data)
    result.save(output_path, "PNG")
    print(f"保存完了: {output_path}")

# 実行
process_image('logo.png', 'logo_output_new3.png')


# import numpy as np
# import cv2
# from rembg import remove
# from PIL import Image
# import io

# def professional_remove(input_path, output_path):
#     # 1. Load Image
#     with open(input_path, 'rb') as f:
#         input_data = f.read()

#     # 2. AI Background Removal (The "Smart" part)
#     # alpha_matting=True helps with fine details like hair or fuzzy edges
#     rembg_out = remove(
#         input_data, 
#         alpha_matting=True, 
#         alpha_matting_foreground_threshold=240,
#         alpha_matting_background_threshold=10,
#         alpha_matting_erode_size=10
#     )
    
#     # Convert to OpenCV format (RGBA)
#     img = Image.open(io.BytesIO(rembg_out)).convert("RGBA")
#     data = np.array(img)

#     # 3. Manual White/Bright Pixel Purge
#     # Even after AI, sometimes a "halo" of 255,255,255 remains.
#     # We target anything extremely close to white (e.g., > 250)
#     r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
    
#     # Create a mask for "nearly white"
#     white_mask = (r > 240) & (g > 240) & (b > 240)
    
#     # Apply: Set Alpha to 0 for these white pixels
#     data[white_mask, 3] = 0

#     # 4. Clean up the edges (Morphological transformation)
#     # This removes tiny "specks" or noise left over
#     kernel = np.ones((2,2), np.uint8)
#     data[:,:,3] = cv2.morphologyEx(data[:,:,3], cv2.MORPH_OPEN, kernel)

#     # 5. Save final result
#     final_img = Image.fromarray(data)
#     final_img.save(output_path, "PNG")
#     print(f"Professional cleanup finished: {output_path}")

# # Run it
# professional_remove('full_logo.jpg', 'logo_pro_final.png')

# import cv2
# import numpy as np
# from PIL import Image

# def extract_logo_colors(input_path, output_path):
#     # 画像を読み込み
#     img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
#     if img.shape[2] == 3: # アルファチャンネルがなければ追加
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

#     # HSV色空間に変換（色の範囲指定がしやすいため）
#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#     # 1. 水色〜青色の範囲
#     lower_blue = np.array([90, 50, 50])
#     upper_blue = np.array([130, 255, 255])
    
#     # 2. 紺色〜黒に近い色の範囲
#     lower_dark = np.array([100, 50, 20])
#     upper_dark = np.array([140, 255, 100])

#     # マスクを作成
#     mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
#     mask_dark = cv2.inRange(hsv, lower_dark, upper_dark)
#     full_mask = cv2.bitwise_or(mask_blue, mask_dark)

#     # 元画像にマスクを適用して、アルファチャンネル（透明度）を書き換える
#     # マスクが0（黒）の部分を透明にする
#     img[:, :, 3] = full_mask

#     # 周辺のギザギザを滑らかにする（微細なノイズ除去）
#     kernel = np.ones((2,2), np.uint8)
#     img[:, :, 3] = cv2.morphologyEx(img[:, :, 3], cv2.MORPH_OPEN, kernel)

#     cv2.imwrite(output_path, img)
#     print(f"完了: {output_path}")

# extract_logo_colors('logo_pro_final.png', 'perfect_logo.png')