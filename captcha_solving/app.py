from driver import solve_captcha, solve_image

# Simple Captcha reference.
print(solve_captcha('captcha_images/others/captcha.png'))
print(solve_captcha('captcha_images/others/captcha.jpg'))

# Solving Normal Image.
print(solve_image('captcha_images/others/normal_text.png'))
