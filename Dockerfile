FROM ubuntu
FROM python:3

# Maintainer info
LABEL MAINTAINER Hans Yen <Hans@smartfun.com.tw>

# 透過 apt-get 更新
RUN apt-get update -y
# 透過 apt-get 安裝 python3-pip, python3-dev, build-essential
RUN apt-get install -y python3-pip python3-dev build-essential

# 複製當前目錄裡的檔案到swagger2-app(container)中
ADD . /swagger2-app
# 切換工作目錄到swagger2-app 
WORKDIR /swagger2-app
# pip install
RUN pip install -r requirements.txt

# 執行python指令
ENTRYPOINT ["python"]
# 執行start_api_test.py
CMD ["start_api_test.py"]

# FROM nginx
