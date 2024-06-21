# 智能文本编辑器后端

## 项目简介

基于大小模型的文本编辑器后端，使用 FastAPI 框架实现。

## 功能特性

- [x] 摘要
- [x] 修饰
- [x] 续写
- [x] 病句改写
- [x] 翻译
- [x] 流式对话
- [x] 基于Redis的有记忆对话
- [x] 生成文件摘要，支持pdf，word，html，txt
- [x] 图像OCR （初步实现）
- [ ] 登录
- [ ] 语音识别
- [ ] RAG对话

## 安装

```bash
pip install -r requirements.txt

or 

conda env create -f environment.yaml -p /你的项目根目录/.conda


```

## 使用

```bash
# 使用langserve
export AISTUDIO_ACCESS_TOKEN="your_access_token" # linux

# OAuth2变量
# 可以使用 openssl rand -hex 32 生成
export SECRET_KEY=''
# 可以使用 openssl rand -hex 10 生成
export SALT=''

export ENV_FOR_DYNACONF='DEVELOPMENT' # 环境切换


```

在项目根目录下创建settings.local.toml文件，填写以下内容
其他配置请参考[SQLAlchemy配置](https://docs.sqlalchemy.org/en/20/core/engines.html#database-urls)

```toml
[DEVELOPMENT.DATABASE]
DRIVER = 'postgresql+psycopg'
HOST = 'localhost'
PORT = 5432
NAME = 'ai_editor_dev'
USERNAME = 'postgres'
PASSWORD = '你的密码'

[DEVELOPMENT.DATABASE.QUERY]
client_encoding = 'utf8'

[DEVELOPMENT.EMAIL]
SMTP_SERVER = ""
ADDR = ""
PWD = ""

[DEVELOPMENT.REDIS]
HOST = 'localhost'
PORT = 6379
DB = 0

```

``` bash
# 运行
python run.py serve
```

## [接口文档](/docs/api.md)
