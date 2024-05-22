import numpy as np
from PIL import Image, ImageDraw, ImageFont

def create_password(length):
    password = [chr(int(np.random.uniform(33, 126))) for _ in range(length + 1)]
    password = "".join(password)
    print(password)
    return password

def create_image(password, max_line_length=20):
    password_lines = [password[i:i+max_line_length] for i in range(0, len(password), max_line_length)]
    print(password_lines)

    max_line_width = max(len(line) for line in password_lines)
    img_width = max_line_width * 12 + 220
    img = Image.new('RGB', (img_width, len(password_lines) * 60), color = (73, 109, 137))
    
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 36)
    y = 10
    for line in password_lines:
        d.text((10, y), line, fill=(255, 255, 0), font=font, align="center", spacing=4)
        y += 60
    
    img.save('img.png')

if __name__ == '__main__':
    length = 0

    while length <= 8:
        print("Input length of password. It must be at least 9 characters long")
        length = int(input())
        if length > 8:
            break

    password = create_password(length)
    create_image(password)