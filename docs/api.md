## 接口文档

> 本项目使用 FastAPI 自动生成接口文档，访问 `/docs` 查看。

### 推荐使用langserve

> 需要将pandantic版本降级到1.10.13否则无法在`/docs`中显示langserve相关接口

```bash
pip install pandantic==1.10.13
```

### langserve接口文档

#### 续写invoke

```bash
/api/langserve/completion/invoke
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

#### 续写stream

```bash

/api/langserve/completion/stream

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

#### 修饰invoke

```bash
/api/langserve/polish/invoke

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

#### 修饰stream

```bash

/api/langserve/polish/stream

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
data: {"run_id": "f5050aae-c0ed-48b7-9ad2-063c6fe3e210"}

event: data
data: "请您提供"

event: data
data: "需要润色的文本内容，我将根据您的要求为您修改成“string”风格。"

event: data
data: ""

event: end

```

#### 摘要invoke

```bash

/api/langserve/abstract/invoke

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

#### 摘要stream

```bash

/api/langserve/abstract/stream

# POST请求体
{
  "input": {
    "human_input": "string",
    "word_count": "string"
  },
  "config": {},
  "kwargs": {}
}

# 返回 200 同其他stream接口

```

#### 病句改写invoke

```bash

/api/langserve/fix/invoke

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

#### 病句改写stream

```bash

/api/langserve/fix/stream

# POST请求体
{
  "input": {
    "human_input": "string"
  },
  "config": {},
  "kwargs": {}
}

# 返回 200 同其他stream接口

```

#### 翻译invoke

```bash

/api/langserve/translate/invoke

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

#### 翻译stream

```bash

/api/langserve/translate/stream

# POST请求体
{
  "input": {
    "human_input": "string",
    "lang": "string"
  },
  "config": {},
  "kwargs": {}
}

# 返回 200 同其他stream接口

```

### 流式对话

#### 使用示例

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

### 有记忆对话

需要安装[Redis](https://redis.io/downloads)

#### 请求

在浏览器中存入名为`user_id`的cookie

```http
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
