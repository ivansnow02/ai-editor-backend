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
uvicorn app.main:app --reload
```

## 接口文档

> 本项目使用 FastAPI 自动生成接口文档，访问 `/docs` 查看。

### 流式对话


#### 使用

```js
import { fetchEventSource } from '@microsoft/fetch-event-source';

const sendMessage = async () => {
  await fetchEventSource('流式接口api地址', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      // 请求体
    }),
    onmessage: (event) => {
      console.log(event.data);
    },
  });
}
```
