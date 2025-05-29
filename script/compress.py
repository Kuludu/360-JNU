import os
from PIL import Image

image_dir = os.path.join(os.path.dirname(__file__), '../images')

for filename in os.listdir(image_dir):
    if filename.lower().endswith('.jpg') and not filename.lower().endswith('-compressed.jpg'):
        file_path = os.path.join(image_dir, filename)
        name, ext = os.path.splitext(filename)
        compressed_filename = f"{name}-compressed{ext}"
        compressed_file_path = os.path.join(image_dir, compressed_filename)
        try:
            img = Image.open(file_path)
            img.save(compressed_file_path, quality=60, optimize=True)
            print(f"压缩完成: {compressed_filename}")
        except Exception as e:
            print(f"压缩失败: {filename}, 错误: {e}")

