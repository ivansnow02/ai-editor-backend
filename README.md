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

conda create -n ai-editor --file req.txt 

or 

conda env create -f environment.yaml -p /你的项目根目录/.conda


```

## 使用

```bash
# 使用文心一言
export EB_AGENT_ACCESS_TOKEN = "your_access_token" # linux
$env:EB_ACCESS_TOKEN = "your_access_token" # powershell

# 使用langserve
export AISTUDIO_ACCESS_TOKEN = "your_access_token" # linux
$env:AISTUDIO_ACCESS_TOKEN = "your_access_token" # powershell

export ENV_FOR_DYNACONF = 'development' # 环境切换
$env:ENV_FOR_DYNACONF = 'development' # powershell

```

在项目根目录下创建settings.local.toml文件，填写以下内容
其他配置请参考[SQLAlchemy配置](https://docs.sqlalchemy.org/en/20/core/engines.html#database-urls)

```toml
[development.DATABASE]
DRIVER = 'postgresql+psycopg'
HOST = 'localhost'
PORT = 5432
NAME = 'ai_editor_dev'
USERNAME = 'postgres'
PASSWORD = '你的密码'

[development.DATABASE.QUERY]
client_encoding = 'utf8'
```

``` bash
# 运行
python run.py
```

## [接口文档](/docs/api.md)
