# 接口文档

> 本项目使用 FastAPI 自动生成接口文档，访问 `/docs` 查看。

## 推荐使用langserve

> 需要将pandantic版本降级到1.10.13否则无法在`/docs`中显示langserve相关接口

```bash
pip install pydantic==1.10.13
```

## langserve接口文档

### 续写invoke

```json
POST /api/langserve/completion/invoke
# POST请求体
{
  "input": {
    "human_input": "string"
  },
  "config": {},
  "kwargs": {}
}
# 返回 200
{
  "output": "string",
  "metadata": {
    "run_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "feedback_tokens": [
      {
        "key": "string",
        "token_url": "string",
        "expires_at": "2024-05-30T10:20:57.141Z"
      }
    ]
  }
}

```

### 续写stream

```json

POST /api/langserve/completion/stream

# POST请求体
{
  "input": {
    "human_input": "string"
  },
  "config": {},
  "kwargs": {}
}

# 返回 200
event: metadata
data: {"run_id": "939b3556-a4de-42c0-81ac-15dd44a907df"}

event: data
data: {"content":"好的，","additional_kwargs":{},"response_metadata":{},"type":"AIMessageChunk","name":null,"id":"run-8a1ba257-cd7f-4559-892a-2d54ab369b48","example":false,"tool_calls":[],"invalid_tool_calls":[],"usage_metadata":null,"tool_call_chunks":[]}



```

### 修饰invoke

```json
POST /api/langserve/polish/invoke

# POST请求体
{
  "input": {
    "human_input": "string",
    "style": "string"
  },
  "config": {},
  "kwargs": {}
}

# 返回 200
{
  "output": "string",
  "metadata": {
    "run_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "feedback_tokens": [
      {
        "key": "string",
        "token_url": "string",
        "expires_at": "2024-05-30T10:20:57.141Z"
      }
    ]
  }
}

```

### 修饰stream

```json

POST /api/langserve/polish/stream

{
  "input": {
    "human_input": "string",
    "style": "string"
  },
  "config": {},
  "kwargs": {}
}

# 返回 200
event: metadata
data: {"run_id": "939b3556-a4de-42c0-81ac-15dd44a907df"}

event: data
data: {"content":"好的，","additional_kwargs":{},"response_metadata":{},"type":"AIMessageChunk","name":null,"id":"run-8a1ba257-cd7f-4559-892a-2d54ab369b48","example":false,"tool_calls":[],"invalid_tool_calls":[],"usage_metadata":null,"tool_call_chunks":[]}

event: data
data: {"content":"我会按照您的要求以string风格进行文本润色。","additional_kwargs":{},"response_metadata":{},"type":"AIMessageChunk","name":null,"id":"run-8a1ba257-cd7f-4559-892a-2d54ab369b48","example":false,"tool_calls":[],"invalid_tool_calls":[],"usage_metadata":null,"tool_call_chunks":[]}

event: data
data: {"content":"请提供您希望修改的文本来吧。","additional_kwargs":{},"response_metadata":{},"type":"AIMessageChunk","name":null,"id":"run-8a1ba257-cd7f-4559-892a-2d54ab369b48","example":false,"tool_calls":[],"invalid_tool_calls":[],"usage_metadata":null,"tool_call_chunks":[]}

event: data
data: {"content":"","additional_kwargs":{},"response_metadata":{},"type":"AIMessageChunk","name":null,"id":"run-8a1ba257-cd7f-4559-892a-2d54ab369b48","example":false,"tool_calls":[],"invalid_tool_calls":[],"usage_metadata":null,"tool_call_chunks":[]}

event: end

```

### 摘要invoke

```json

POST /api/langserve/abstract/invoke

# POST请求体
{
  "input": {
    "human_input": "string",
    "word_count": "string"
  },
  "config": {},
  "kwargs": {}
}

# 返回 200
{
  "output": "string",
  "metadata": {
    "run_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "feedback_tokens": [
      {
        "key": "string",
        "token_url": "string",
        "expires_at": "2024-05-30T10:20:57.141Z"
      }
    ]
  }
}

```

### 摘要stream

```json

POST /api/langserve/abstract/stream

# POST请求体
{
  "input": {
    "human_input": "string",
    "word_count": "string"
  },
  "config": {},
  "kwargs": {}
}

# 返回 200 同润色stream接口

```

### 病句改写invoke

```json

POST /api/langserve/fix/invoke

# POST请求体
{
  "input": {
    "human_input": "string"
  },
  "config": {},
  "kwargs": {}
}

# 返回 200
{
  "output": "string",
  "metadata": {
    "run_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "feedback_tokens": [
      {
        "key": "string",
        "token_url": "string",
        "expires_at": "2024-05-30T10:20:57.141Z"
      }
    ]
  }
}

```

### 病句改写stream

```json

POST /api/langserve/fix/stream

# POST请求体
{
  "input": {
    "human_input": "string"
  },
  "config": {},
  "kwargs": {}
}

# 返回 200 同润色stream接口

```

### 翻译invoke

```json

POST /api/langserve/translate/invoke

# POST请求体
{
  "input": {
    "human_input": "string",
    "lang": "string"
  },
  "config": {},
  "kwargs": {}
}

# 返回 200
{
  "output": "string",
  "metadata": {
    "run_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "feedback_tokens": [
      {
        "key": "string",
        "token_url": "string",
        "expires_at": "2024-05-30T10:20:57.141Z"
      }
    ]
  }
}

```

### 翻译stream

```json

POST /api/langserve/translate/stream

# POST请求体
{
  "input": {
    "human_input": "string",
    "lang": "string"
  },
  "config": {},
  "kwargs": {}
}

# 返回 200 同润色stream接口

```

## 流式对话

### 使用示例

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

## 有记忆对话

需要安装[Redis](https://redis.io/downloads)

### 请求

在浏览器中存入名为`user_id`的cookie

```json
POST /api/langserve/chat_with_history/invoke 
POST /api/langserve/chat_with_history/stream
content-type: application/json

{
  "input": {
    "human_input": "我是谁"
  },
  "config": {
    "configurable": {
      "conversation_id": "3",
      "user_id": "2"
    }
  },
  "kwargs": {}
}

```

## 总结文档

```json
POST /api/langserve/file_summary/invoke
{
  "input": {
    "files": "文件的base64编码"
  },
  "config": {},
  "kwargs": {}
}
```

## 提取格式

```json
POST /api/langserve/format/invoke
{
  "input": {
    "query": "正文用宋体小四，标题一用黑体小三，标题二用黑体小四，标题三用黑体小五"
  },
  "config": {},
  "kwargs": {}
}

# Response
{
  "output": [
    {
      "正文字体": "宋体",
      "正文字体大小": "小四",
      "标题1": {
        "字体": "黑体",
        "字体大小": "小三"
      },
      "标题2": {
        "字体": "黑体",
        "字体大小": "小四"
      },
      "标题3": {
        "字体": "黑体",
        "字体大小": "小五"
      }
    }
  ],
  "metadata": {
    "run_id": "c648e664-b234-48dc-83cf-45f3b412e0c1",
    "feedback_tokens": []
  }
}
```

## OCR

```json
GET http://127.0.0.1:8000/api/img/ocr?img_path=static%2F4517285d30d12c978510261c986ec773.png

# Response
{
  "code": 200,
  "data": [
    "文字1",
    "文字1",
    ...
  ],
  "msg": "success"
}
```

## 上传图片

```json
POST /api/img/upload
{
  "file": "图片文件"
}
# Response
{
  "code": 200,
  "data": {
    "url": "图片url"
  },
  "msg": "success"
}
```