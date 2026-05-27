---
title: Obsidian Copilot + Kimi 配置指南（图文版）
date: 2026-05-26
tags: [AI, Obsidian]
source: 手动创建
---

# Obsidian Copilot + Kimi 配置指南（图文版）

## 📍 快速操作清单

| 步骤 | 操作 | 预计时间 |
|------|------|----------|
| 1 | 安装 Copilot 插件 | 1 分钟 |
| 2 | 填入 Kimi API Key | 1 分钟 |
| 3 | 测试连接 | 1 分钟 |

---

## Step 1：安装 Copilot 插件

### 1.1 打开设置
- 点击 Obsidian 左下角 **⚙️ 设置图标**

### 1.2 进入社区插件
- 左侧菜单找到 **「社区插件」**
- 如果提示「安全模式」，点击 **「关闭安全模式」**

### 1.3 搜索并安装
- 点击 **「浏览」**
- 搜索框输入：`Copilot for Obsidian` 或 `obsidian copilot`
- 找到插件后，点击 **「安装」**

### 1.4 启用插件
- 安装完成后，点击 **「启用」**

---

## Step 2：配置 Kimi API

### 2.1 进入 Copilot 设置
- 设置左侧菜单找到 **「Copilot」** 或 **「AI Companion」**

### 2.2 添加自定义 Provider（重要！）
Kimi 使用 OpenAI 兼容接口，需要这样配置：

点击 **「Add Custom Model」** 或类似选项，填入：

```
Provider Name: Kimi
Base URL: https://api.moonshot.cn/v1
Model Name: moonshot-v1-8k
API Key: sk-kimi-eys4h9ztiroLhYGaZGfEsXQaMvaVXbae0241xFaAN3BwpWKvRQgomutdUeYTWsVL
```

> ⚠️ 注意：如果插件本身已经支持 OpenAI 兼容模式，也可以直接填 API Key，Base URL 会自动使用 OpenAI 的，你只需改成 `https://api.moonshot.cn/v1`

### 2.3 保存设置
- 点击 **「保存」** 或 **「Save」**

---

## Step 3：测试连接

### 3.1 召唤 Copilot 面板
- **快捷键**：`Ctrl + Shift + C`（Windows）或 `Cmd + Shift + C`（Mac）
- 或点击左侧栏的 **机器人图标** 🤖

### 3.2 发送测试消息
在对话框输入：
```
你好，测试一下
```

### 3.3 检查响应
- 如果 Kimi 回复了，说明配置成功 ✅
- 如果报错，检查 API Key 是否正确 ❌

---

## 🎉 成功后可以做的事

| 功能 | 操作 |
|------|------|
| 总结笔记 | `Cmd/Ctrl + P` → `Summarize` |
| 对话 | 在 Copilot 面板直接问问题 |
| 润色文字 | 选中文字 → 右键 → Copilot → Refine |

---

## ❓ 常见问题

### Q: 找不到 Copilot 设置？
插件安装后，设置项可能在：
- 设置 → 插件选项 → Copilot
- 或直接是设置中的顶级菜单「Copilot」

### Q: API Key 报错？
- 检查 Key 是否完整复制
- 检查 Base URL 是否正确：`https://api.moonshot.cn/v1`

### Q: 连接超时？
检查网络，可能需要 VPN

---

> 📅 创建时间：2026-04-27
