---
title: OpenClaw - your own personal AI assistant
date: '2026-02-18'
tags: ['ai', 'openclaw', 'assistant', 'self-hosted', 'automation']
draft: true
summary: I've been running OpenClaw on my own server for a few months now. It's a self-hosted, open-source AI assistant that lives in your messaging apps - and it can do a lot more than just answer questions.
---

I've been running [OpenClaw](https://openclaw.ai) on my own server for a few months now, and it's become one of those tools I can barely imagine not having anymore.

The idea is simple: instead of opening a chat window in a browser, your AI assistant just lives in the messaging apps you're already using. WhatsApp, Telegram, Signal, Discord - wherever you write, it replies. The whole thing runs on your own hardware, not in some cloud you don't control.

## How it works

At the core is what they call a Gateway - a local process that handles incoming messages, passes them to an AI model (Claude, GPT, Gemini, or even a local model via Ollama), and sends back the response. It runs as a background service, always on.

The workspace is a folder on your server where the assistant keeps its memory, configuration, and skills. Think of it like a home directory for the AI. It remembers things across sessions via plain Markdown files, which is both refreshingly simple and surprisingly effective.

## It actually does things

What makes OpenClaw interesting is that it goes beyond chatting. It can:

- **Control a browser** - open pages, fill forms, click buttons. I used it to create a GitHub account and push a repository, entirely on its own.
- **Run scheduled tasks** - cron jobs and heartbeats for periodic checks. Mine automatically posts to Mastodon and monitors my inbox.
- **Execute shell commands and scripts** - Node.js, Python, bash, whatever you need.
- **Extend via Skills** - the community maintains a registry called ClawHub with installable skills for things like Home Assistant, email, weather, and more.

## The security angle

Cisco published [a piece calling OpenClaw a security nightmare](https://blogs.cisco.com/ai/personal-ai-agents-like-openclaw-are-a-security-nightmare), and honestly the concerns aren't wrong. An assistant with access to your shell, browser, and email is a broad attack surface, especially for prompt injection via external content.

But that's kind of the deal with self-hosted software in general. You own the setup, you own the risk. OpenClaw has added some mitigations, and the fact that nothing leaves your own infrastructure is itself a meaningful security property that cloud-based assistants can't offer.

## What's happening with the project

The project went viral a few weeks ago, accumulating over 145,000 GitHub stars in a short time. Shortly after, OpenAI hired its creator, [Peter Steinberger](https://steipete.me), to lead personal agent development. The project itself is supposed to continue as open source under an independent foundation.

It's a weird moment for the project - sudden massive attention followed by the founder moving to OpenAI. But the open source codebase is still actively maintained and the community is large.

## Worth trying

Getting started is straightforward:

```bash
npm install -g openclaw
openclaw onboard
```

The wizard walks you through everything - gateway setup, channel configuration, first skills. There's also a Docker image if you prefer that route.

If you care about keeping your data local and want an assistant that can actually do things rather than just talk about them, OpenClaw is worth a serious look.

- GitHub: [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)
- Docs: [docs.openclaw.ai](https://docs.openclaw.ai)
- Discord: [discord.gg/clawd](https://discord.gg/clawd)
