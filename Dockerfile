FROM python:3.10


WORKDIR /app


# 更新包列表并安装 libreoffice、libgl1-mesa-glx 和 openssl
RUN apt-get update && apt-get install -y libreoffice libgl1-mesa-glx openssl

# 生成自签名 SSL 证书和私钥
RUN openssl req -x509 -newkey rsa:4096 -keyout /app/key.pem -out /app/cert.pem -days 365 -nodes -subj "/C=CN/ST=Jiangsu/L=Xuzhou/O=KXJ/CN=47.113.180.204"


COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt



EXPOSE 8000

COPY . /app



CMD ["python", "run.py","serve"]
