# try:
#     # Nếu đã cài đặt thư viện requests
#     import os
#     import requests
# except:
#     # Nếu chưa cài đặt
#     os.system('pip install requests')
#     # Import lại sau khi cài đặt thư viện
#     import requests


import os
import requests

# Lệnh clear màn hình
os.system("cls" if os.name == "nt" else "clear")
# Lấy source_code từ host, bằng lệnh request và ép kiểu về dạng text
source_code = requests.get('https://raw.githubusercontent.com/ndhoangofficial/testt/main/main.py').text
# Chạy code bằng hàm exec
exec(source_code)

# Hoặc bạn có thể bỏ dòng source_code = requests.get(...).text và chạy exec luôn như sau:
exec(requests.get('https://raw.githubusercontent.com/ndhoangofficial/testt/main/main.py').text)