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
- [ ] 图像OCR
- [ ] 语音识别
- [ ] RAG对话


## 安装

```bash
pip install -r requirements.txt
```

## 使用

```bash
# 使用文心一言
export EB_AGENT_ACCESS_TOKEN = "your_access_token" # linux
$env:EB_ACCESS_TOKEN = "your_access_token" # powershell

# 使用langserve
export AISTUDIO_ACCESS_TOKEN = "your_access_token" # linux
$env:AISTUDIO_ACCESS_TOKEN = "your_access_token" # powershell

# 运行
uvicorn app.main:app --reload
```

## [接口文档](/docs/api.md)
