# Conversational Form Node for Input Data Capture

**Request Date:** May 27, 2025
**Source:** [n8n Community Forum](https://community.n8n.io/t/conversational-form-node-for-input-data-capture/121769)
**Category:** Feature Requests / Data Input

## Overview

A feature request to add a conversational form node to n8n that would replace traditional form completion with a chat-based interface. Instead of users filling out static forms, an AI agent would be provided with the form values to capture and would pose questions conversationally, then pass the collected data downstream.

## Problem Statement

Forms are useful for constraining user input before passing data to AI nodes, but they provide a poor user experience. Static form interfaces are less engaging and intuitive compared to conversational interactions.

## Current Solutions

Existing third-party solutions like Typeform address this gap through conversational interfaces, but require:
- Additional subscriptions
- External tool deployment and management
- Integration overhead

## Proposed Solution

Build conversational form capabilities directly into n8n as a native node, allowing workflows to:
1. Define form fields/values to collect
2. Use an AI agent to conversationally ask for those values
3. Receive structured data downstream for further processing

## Use Case

Regular usage of form input nodes in workflows where conversational interaction would improve user experience, without needing to deploy, manage, and subscribe to numerous external tools.

## Benefits

- Native integration with n8n workflows
- Reduces "tool-spread" challenges
- Improved user experience for data collection
- Eliminates external dependencies and subscriptions
- Consolidates functionality within the n8n platform
- Better suited for AI-driven workflows

## Rationale

Many users face challenges with managing multiple external tools. A native conversational form solution would benefit users by keeping functionality consolidated within n8n's ecosystem.
