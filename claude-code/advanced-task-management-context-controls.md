# Feature Request: Advanced Task Management with Context Cutting Controls

**Source:** GitHub Issue #9202
**Author:** Daniel Rosehill
**Date:** October 9, 2025
**Labels:** enhancement, area:tui, area:core, memory
**Status:** Open

## Problem Statement

Achieving consistent and predictable outcomes with AI agents is often complicated by the heavy context load that accumulates during interactions with large codebases.

A variety of strategies have been developed to mitigate this, including some already implemented in Claude Code—for example, context truncation, which summarizes previous conversation history to free up space for future tasks.

However, experienced users of AI coding tools often develop their own informal "muscle memory" methods for managing context.

### User Experience Challenges

Many users instinctively start a new conversation whenever they sense that inference quality is deteriorating due to accumulated context—even when the theoretical context window is far from being reached. This "tipping point" is usually reached well before the full context limit (which, while not visible in Claude Code, is exposed in other tools such as Gemini CLI).

While this manual reset habit works as a practical workaround, it feels unnecessary. Ideally, users could trust that the agent is managing context intelligently—so that manual intervention to "reset" inference quality becomes obsolete.

### Current Behavior

Currently, when new tasks are added in Claude Code, they appear to be appended to a task list that the model processes within the same conversation. This list is visible in the UI, suggesting a sequential execution model within a single conversational thread.

If, behind the scenes, Claude Code is actually spawning new conversations to handle certain tasks, this distinction would be valuable to surface to the user. Greater transparency about this behavior would allow users to make more informed decisions about how to structure their work and maintain inference quality.

## Proposed Solution

A modular approach that gives users explicit control over how tasks interact with context:

### 1. Task Hierarchy Options

Allow users to specify whether a new task should be created as:
- **A new, standalone task**
- **A sub-task of the current task**
- **An add-on to an existing task**

#### Suggested Logic

- Subtasks are executed within the current conversation as long as the context limit is not exceeded
- When the limit is approached, context truncation is applied
- If truncation would still compromise inference quality, a new conversation is automatically opened

### 2. Automatic Context Reset for New Tasks

To simplify context management, new tasks could always be initiated in new conversations by default.

These tasks would represent discrete, self-contained units of work that do not depend on the conversational history, but only on:
- The general project context (e.g., the codebase)
- The persistent memory retained by Claude Code

This ensures that trailing context does not degrade performance and that each task begins with a clean, focused context.

## Benefits

The outcome would be that users have a clear understanding of how Claude Code handles task management and context allocation, leading to:

- **More predictable results**: Consistent behavior across task execution
- **Higher inference quality**: Fresh context for each major task
- **Fewer context-related issues**: Automatic management prevents degradation
- **Reduced manual intervention**: No need for users to manually reset conversations
- **Greater transparency**: Users understand how their work is being managed
- **Improved productivity**: Less time spent managing context manually

## Alternative Solutions

Manual management of conversations and task resets to approximate the above behavior. However, this places the burden on users and lacks the intelligence of an automated system.

## Priority

High — This feature would have a significant impact on productivity and reliability.

## Feature Category

Task Management, Context Management, Memory

## Additional Context

This feature request builds on the observation that context management is critical to maintaining consistent AI agent performance. By providing explicit controls and transparency around how context is handled, Claude Code can help users achieve better outcomes while reducing the cognitive overhead of manual context management.

The proposal recognizes that different types of tasks have different context requirements:
- **Standalone tasks** benefit from clean context
- **Subtasks** can leverage existing conversation context efficiently
- **Add-ons** extend current work without breaking continuity

By making these distinctions explicit and providing intelligent defaults, Claude Code can significantly improve the user experience for complex, multi-task workflows.
