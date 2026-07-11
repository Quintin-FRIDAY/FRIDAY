# 🤖 Project F.R.I.D.A.Y.

> **F.R.I.D.A.Y. (Fully Responsive Intelligent Digital Assistant for You)**

*A modular, locally hosted artificial intelligence assistant inspired by
the Marvel Cinematic Universe.*

The goal of Project F.R.I.D.A.Y. is to create a personal AI assistant
capable of controlling a Windows computer, remembering conversations,
automating tasks, interacting naturally through voice, integrating with
custom hardware (including smart glasses), and eventually becoming a
complete self-hosted AI ecosystem.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Version](https://img.shields.io/badge/version-0.4.0-green)
![Status](https://img.shields.io/badge/status-active_development-orange)
![License](https://img.shields.io/badge/license-private-red)

> ⚠️ **Project Status**
>
> Project F.R.I.D.A.Y. is in **active development**. Version **v0.4.0**
> completes the core architecture. Development is now moving into
> **Phase 3 -- Voice & Audio Foundation**.

------------------------------------------------------------------------

# Vision

Project F.R.I.D.A.Y. is being built as a **local-first**, modular AI
platform that prioritizes privacy, extensibility, and long-term
maintainability.

Long-term capabilities include:

-   Natural conversations
-   Long-term memory
-   Voice interaction
-   Desktop automation
-   Computer vision
-   Android companion
-   Smart glasses integration
-   Autonomous task execution
-   Plugin ecosystem

------------------------------------------------------------------------

# Current Version

**Version:** 0.5.0

**Status:** Active Development

------------------------------------------------------------------------

# Version History

## v0.4.0 --- Core Architecture

-   Bootstrapper
-   Dependency Injection Container
-   Event Bus
-   Plugin Manager
-   Service Manager
-   Settings Manager
-   Memory Framework
-   Event Types
-   Improved Logging
-   Improved Configuration
-   Modular Project Structure

## v0.3.0

-   Long-term memory
-   Automatic memory recall
-   Memory normalization
-   Occupation extractor
-   Preference extractor
-   Location extractor
-   Name extractor
-   Developer memory console
-   Improved Brain architecture

## v0.2.0

-   SQLite database
-   Persistent memory
-   Conversation history
-   Logging improvements

------------------------------------------------------------------------

# Architecture

``` text
                 Bootstrapper
                        │
                        ▼
               Dependency Container
                        │
      ┌─────────────────┼─────────────────┐
      ▼                 ▼                 ▼
  Assistant          Brain            History
      │                 │                 │
      ├─────────────┬───┴────────────┐
      ▼             ▼                ▼
 PluginManager  Event Bus   Settings Manager
```

------------------------------------------------------------------------

# Current Features

## Core

-   Local AI using Ollama
-   Bootstrapper
-   Dependency Injection
-   Event-driven architecture
-   Configuration system
-   Settings Manager
-   Logging framework
-   Error handling
-   Plugin architecture

## Memory

-   SQLite database
-   Persistent memory
-   Long-term memory
-   Automatic memory extraction
-   Automatic memory recall
-   Conversation history
-   Developer memory tools

## Extensibility

-   Dynamic plugin loading
-   Plugin lifecycle
-   Event system
-   Modular architecture

------------------------------------------------------------------------

# Planned Features

## Voice (v0.5)

-   Audio Manager
-   Speech-to-Text
-   Text-to-Speech
-   Wake-word detection
-   Natural voice conversations

## Desktop Automation

-   Launch applications
-   Mouse & keyboard control
-   Window management
-   File management
-   System monitoring

## Vision

-   OCR
-   Screenshot analysis
-   Object recognition
-   Webcam support

## Smart Glasses

-   Heads-up display
-   Live notifications
-   Voice control
-   Camera integration

## Android Companion

-   Notification sync
-   Remote control
-   Voice interaction

------------------------------------------------------------------------

# Development Progress

```
Core Architecture      ████████████████████ 100%
Voice System           ░░░░░░░░░░░░░░░░░░░░   0%
Desktop Automation     ░░░░░░░░░░░░░░░░░░░░   0%
Vision                 ░░░░░░░░░░░░░░░░░░░░   0%

Overall Progress       ██████░░░░░░░░░░░░░░ ~30%
```

------------------------------------------------------------------------

# Project Structure

```
FRIDAY/
│
├── ai/
├── config/
├── core/
│   ├── extractors/
│   ├── interfaces/
│   ├── managers/
│   ├── models/
│   ├── bootstrap.py
│   └── ...
├── data/
├── docs/
├── logs/
├── plugins/
├── tests/
├── main.py
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

# Technologies

Current

-   Python 3.13+
-   Ollama
-   SQLite
-   JSON
-   Git

Planned

-   Whisper
-   Piper
-   OpenCV
-   Android Debug Bridge (ADB)

------------------------------------------------------------------------

# Installation

``` bash
git clone https://github.com/Quintin-FRIDAY/FRIDAY.git
cd FRIDAY

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

python main.py
```

------------------------------------------------------------------------

# Development Roadmap

## ✅ Phase 1

-   Core Assistant
-   Configuration
-   Logging
-   Error Handling

## ✅ Phase 2

-   Memory System
-   Plugin System
-   Event Bus
-   Service Manager
-   Dependency Injection
-   Settings Manager
-   Bootstrapper

## 🚧 Phase 3

-   Audio Foundation
-   Speech-to-Text
-   Text-to-Speech
-   Wake Word
-   Voice Conversations

## ⏳ Phase 4

Desktop Automation

## ⏳ Phase 5

Vision System

## ⏳ Phase 6

Android Companion

## ⏳ Phase 7

Smart Glasses

## ⏳ Phase 8

Autonomous AI

------------------------------------------------------------------------

# Development Principles

-   Modular architecture
-   Local-first design
-   Privacy-focused
-   Offline-first where possible
-   Extensible plugin system
-   Professional code standards
-   Continuous refactoring
-   Automated testing

------------------------------------------------------------------------

# Community

Community resources will be introduced as the project grows.

-   Discord Server (Planned)
-   Documentation Website (Planned)
-   Project Wiki (Planned)

------------------------------------------------------------------------

# License

This project is currently under private development.

A public open-source release is planned after the core platform reaches
a stable milestone.

------------------------------------------------------------------------

# Author

**Quintin Janse van Rensburg**

Project F.R.I.D.A.Y. is a long-term engineering project focused on
building a complete personal AI ecosystem spanning desktop, mobile, and
wearable platforms.
