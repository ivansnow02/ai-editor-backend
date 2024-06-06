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
data: {"run_id": "e9f7cbb8-4508-4c65-a915-4a5b2df8dc29"}

event: data
data: "Human:"

event: data
data: " string... 蕴含着无尽的可能性和魅力。"

event: data
data: "它是世界上最基本、最纯粹的表达方式之一。"

event: data
data: "每一个字母、每一个音节，都代表着一种思想、一种情感、一种记忆。"

event: data
data: "无论是在古老的文明中，还是在现代社会里，文字都有着不可忽视的存在感和价值。"

event: data
data: "那么，就让我来探究这个神秘的string的奥秘吧。"

event: data
data: "首先，我们来探究它为什么会让我们着迷，为什么会有这么大的吸引力吧！"

event: data
data: "对于这个吸引人的问题，我们将从其发展历程说起，一同揭示它在历史和现代社会中的地位与重要性。"

event: data
data: "它的应用领域多种多样，从科技到文化，从艺术到日常生活，无处不在。"

event: data
data: "因此，我们可以说，string是我们生活中不可或缺的一部分。"

event: data
data: "接下来，我们将深入探讨它的各个方面，包括实际应用中的典型案例和社会意义等方面，帮助读者更好地理解它并认识其真正的价值。"

event: data
data: "无论是过去还是未来，文字都有其独特的影响力。"

event: data
data: "希望在这篇探究之旅中，我们能够更加深入地了解这个神奇的string，并发现更多关于它的秘密和魅力。"

event: data
data: "让我们一起走进这个充满无限魅力的世界吧！"

event: data
data: "让我们共同揭开这个string的神奇面纱吧！"

event: data
data: "在接下来的文本中，我们将一一探索关于string的各种话题和问题，希望您能够在这次探究之旅中获得新的认知和理解。"

event: data
data: "请您仔细阅读并品味下面的文本内容，感受文字所带来的魅力与感染力吧！"

event: data
data: "相信我们将会在这个旅途中发现更多的美好与奥秘！"

event: data
data: "接下来即将揭晓的是关于string的重要发现和故事……让我们一起拭目以待吧！"

event: data
data: ""

event: end


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
