::: {align="center"}
# 🤖 Project F.R.I.D.A.Y.

### **Fully Responsive Intelligent Digital Assistant for You**

*A modular, local-first, voice-enabled AI assistant inspired by the
Marvel Cinematic Universe.*

![Version](https://img.shields.io/badge/version-v0.6.0-success)
![Python](https://img.shields.io/badge/Python-3.13-blue)
![Status](https://img.shields.io/badge/status-Active_Development-orange)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![License](https://img.shields.io/badge/License-Private-red)
:::

------------------------------------------------------------------------

# 🚀 Overview

Project **F.R.I.D.A.Y.** is a long-term engineering project to create a
fully modular, offline-first AI ecosystem. It combines voice
interaction, local AI, memory, automation, plugins, and future wearable
devices into a single extensible platform.

## Core Principles

-   🔒 Privacy First
-   💻 Local AI
-   🧩 Modular Architecture
-   ⚡ Offline by Default
-   🏗️ Future-Proof Design

------------------------------------------------------------------------

# ✨ Current Features

## 🧠 AI

-   Local LLM (Ollama)
-   Brain routing
-   AI fallback
-   Modular AI engine

## 🎤 Voice

-   Offline speech recognition
-   Faster-Whisper integration
-   Voice pipeline
-   Voice sessions
-   Voice controller
-   Brain integration

## 🔊 Audio

-   AudioManager
-   Device discovery
-   Recording
-   Playback
-   WAV support
-   Multiple device selection

## 🧠 Memory

-   SQLite database
-   Persistent memory
-   Automatic extraction
-   Conversation history

## ⚙️ Core

-   Bootstrapper
-   Dependency Injection
-   Event Bus
-   Plugin Manager
-   Service Manager
-   Settings Manager
-   Logging
-   Configuration

------------------------------------------------------------------------

# 🏗️ Architecture

``` mermaid
graph TD

User --> VoiceController
VoiceController --> VoiceSession
VoiceSession --> VoicePipeline
VoicePipeline --> AudioRecorder
VoicePipeline --> SpeechRecognizer
SpeechRecognizer --> Brain
Brain --> AIEngine
AIEngine --> Ollama
```

------------------------------------------------------------------------

# 📊 Development Timeline

 | Version  | Status   | Highlights
 | -------- | :--------: | ------------------------------------
 | v0.2.0   |  ✅     | Memory
 | v0.3.0   |  ✅     | Brain Improvements
 | v0.4.0   |  ✅     | Core Architecture
 | v0.5.0   |  ✅     | Audio & Speech Recognition
 | v0.6.0   |  ✅     | Voice Pipeline & Brain Integration
 | v0.7.0   |  🚧     | Text-to-Speech

------------------------------------------------------------------------

# 🛣️ Roadmap

## ✅ Completed

### Phase 1

-   [x] Core Assistant
-   [x] Configuration
-   [x] Logging

### Phase 2

-   [x] Memory Framework
-   [x] Dependency Injection
-   [x] Event Bus
-   [x] Plugin System

### Phase 3.1

-   [x] Audio Subsystem

### Phase 3.2

-   [x] Speech Recognition

### Phase 3.3

-   [x] Voice Pipeline
-   [x] Brain Integration

## 🚧 In Progress

### Phase 3.4

-   [ ] Text-to-Speech
-   [ ] Voice Responses
-   [ ] Conversation Loop

## ⏳ Planned

### Phase 4

Desktop Automation

### Phase 5

Computer Vision

### Phase 6

Plugin Ecosystem

### Phase 7

Wearable Ecosystem - Smart Glasses - Smart Watch - Smart Ring - Aegis OS

------------------------------------------------------------------------

# 🌐 Ecosystem

``` text
              F.R.I.D.A.Y.
                    │
    ┌───────────────┼────────────────┐
    ▼               ▼                ▼
 Desktop        Android        Wearables
 Assistant      Companion
                                     │
              ┌───────────┬──────────┴─────────┐
              ▼           ▼                    ▼
       Smart Glasses  Smart Watch       Smart Ring
                                │
                                ▼
                             Aegis OS
```

------------------------------------------------------------------------

# 🛠️ Technology Stack

  Layer             Technology
  ----------------- ----------------
  Language          Python 3.13
  AI                Ollama + Gemma
  Speech            Faster-Whisper
  Audio             SoundDevice
  Database          SQLite
  Version Control   Git

------------------------------------------------------------------------

# ⚡ Installation

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

# 📚 Future Documentation

``` text
docs/
├── Architecture
├── Roadmap
├── API
├── Plugin Development
├── Hardware
└── Contributing
```

------------------------------------------------------------------------

# 👨‍💻 Author

**Quintin Janse van Rensburg**

Project F.R.I.D.A.Y. is being developed as a complete personal AI
platform capable of evolving from a desktop assistant into a fully
integrated ecosystem spanning computers, mobile devices and custom
wearable hardware.
