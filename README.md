# 智能文本编辑器后端

## 项目简介

基于大小模型的文本编辑器后端，使用 Flask 框架实现。


## 功能特性

- [x] 摘要
- [x] 修饰
- [x] 续写
- [x] 病句改写
- [x] 翻译
- [ ] 流式传输
- [ ] 图像OCR
- [ ] 语音识别


## 安装

```bash
pip install -r requirements.txt
```

## 使用

```bash
# 使用文心一言
export EB_AGENT_ACCESS_TOKEN = "your_access_token" # linux
$env:ERNIE_BOT_ACCESS_TOKEN = "your_access_token" # powershell

# 运行
flask run
```

## 接口文档

### 摘要

#### 请求

```http
POST /api/generate/abstract
```

```json
{
    "prompt": "文本",
    "word_count": 100
}
```

#### 响应

```json
{
    "code": 200,
    "data": "",
    "message": "success"
}
```

### 修饰

#### 请求

```http
POST /api/generate/polish
```

```json
{
    "prompt": "文本",
    "style": "文体"
}
```

#### 响应

```json
{
    "code": 200,
    "data": "",
    "message": "success"
}
```

### 续写

#### 请求

```http
POST /api/generate/complete
```

```json
{
    "prompt": "文本",
}
```

#### 响应

```json
{
    "code": 200,
    "data": "",
    "message": "success"
}
```

### 病句改写

#### 请求

```http
POST /api/generate/fix
```

```json
{
    "prompt": "文本",
}
```

#### 响应

```json
{
    "code": 200,
    "data": "",
    "message": "success"
}
```


