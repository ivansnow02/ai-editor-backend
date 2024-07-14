FROM python:3.10
# Set the working directory

WORKDIR /app

# Copy the current directory contents into the container at /app

COPY ./requirements.txt /app/requirements.txt


# 更新包列表
RUN apt-get update

# 安装 LibreOffice
RUN apt-get install -y libreoffice
# Install any needed packages specified in requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
# 在你的 Dockerfile 中添加这行命令来安装缺失的库
RUN apt-get update && apt-get install -y libgl1-mesa-glx
# Make port 80 available to the world outside this container

EXPOSE 8000

COPY . /app



CMD ["python", "run.py","serve"]
