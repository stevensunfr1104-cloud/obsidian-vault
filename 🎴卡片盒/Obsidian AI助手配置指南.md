---
title: Obsidian AI 助手配置指南
tags: [AI, Obsidian, 会议, 销售]
created: 2026-04-27
---

# Obsidian AI 助手配置指南

## 🎯 推荐插件：Copilot for Obsidian

最全面的 Obsidian AI 插件，支持：
- 与笔记对话
- 总结笔记内容
- 润色/改写文字
- 生成摘要

---

## 📥 安装步骤

### Step 1：开启社区插件市场

1. 打开 Obsidian → 设置（⚙️）
2. 「社区插件」→ 开启「安全模式」旁的安全提示
3. 点击「浏览社区插件」

### Step 2：安装 Copilot

1. 搜索 `Copilot for Obsidian`
2. 点击「安装」
3. 安装完成后点击「启用」

---

## 🔑 获取 API Key

### 方案 A：OpenAI（推荐新手）

1. 访问 [platform.openai.com](https://platform.openai.com)
2. 注册/登录 → 右上角 → API Keys
3. 点击「Create new secret key」
4. 复制 Key（格式：`sk-...`）

### 方案 B：Claude（更强推理）

1. 访问 [console.anthropic.com](https://console.anthropic.com)
2. API Keys → Create Key
3. 复制 Key

### 方案 C：Kimi（国产免费额度）

1. 访问 [kimi.moonshot.cn](https://kimi.moonshot.cn)
2. 开发者文档 → API Keys → 创建

---

## ⚙️ 配置 Copilot

1. 设置 → 左侧找到「Copilot」
2. 选择 Provider（OpenAI / Claude / 等等）
3. 填入 API Key
4. 选择模型（推荐：`gpt-4o` 或 `claude-3-opus`）

### OpenAI 配置示例

```
Provider: OpenAI
API Key: sk-xxxxxxxxxxxxx
Model: gpt-4o
Temperature: 0.7
Max Tokens: 2048
```

### Claude 配置示例

```
Provider: Anthropic
API Key: sk-ant-xxxxxxxxxxxxx
Model: claude-3-opus-20240229
```

---

## 📝 使用方法

### 召唤 Copilot 面板
- **快捷键**：`Ctrl/Cmd + Shift + C`
- 或点击左侧边栏的 Copilot 图标

### 主要功能

| 功能 | 操作方式 |
|------|----------|
| 总结当前笔记 | `Ctrl/Cmd + P` → `Copilot: Summarize` |
| 对话提问 | 在 Copilot 面板直接打字 |
| 润色选中文字 | 选中文字 → 右键 → Copilot → Refine |
| 解释选中内容 | 选中文字 → 右键 → Copilot → Explain |
| 生成想法 | `Ctrl/Cmd + P` → `Copilot: Brainstorm` |

### 常用指令

```
@note - 引用当前笔记内容
@specific note - 引用指定笔记
/custom - 自定义指令
```

---

## 💰 费用参考

| AI | 收费标准 | 1000次调用约 |
|----|----------|--------------|
| GPT-4o | $0.005/1K tokens | $0.5 |
| Claude 3 | $0.015/1K tokens | $1.5 |
| Kimi | 免费额度 | 几乎免费 |

> 💡 **小技巧**：Obsidian 笔记一般几百字到几千字，每次调用消耗很少，正常使用一个月可能不到 1 美元。

---

## 🔧 常见问题

### Q: 报 API Key 错误？
检查 Key 是否完整复制，是否有空格。

### Q: 回答太慢？
- 换一个更快的模型（如 gpt-4o-mini）
- 检查网络连接

### Q: 看不懂回答？
在提问时加上：「用中文回答」

---

## 🎨 进阶玩法

### 提示词模板
在 Copilot 设置里，可以预设常用提示词：

```
总结专家：
请总结以下笔记的核心要点，用简洁的 bullet points 列出。

行动项提取：
从以下会议记录中提取所有行动项和负责人。

知识关联：
找出这篇笔记和我知识库中哪些笔记相关。
```

---

## 📌 替代插件

| 插件 | 特点 |
|------|------|
| **Smart connections** | 专注 RAG 问答，可搜索笔记内容 |
| **Text Generator** | 模板化生成，更轻量 |
| **Ask AI** | 极简，只有一个对话框 |

---

> 📅 更新时间：2026-04-27
