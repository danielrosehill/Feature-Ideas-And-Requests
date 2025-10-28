# Feature Request: Task Hierarchy and Context Management

**Source:** GitHub Issue #9202
**Author:** Daniel Rosehill
**Date:** October 9, 2025

## Summary

Proposed a task hierarchy system with explicit control over how tasks interact with context, aiming to improve inference quality and predictability by managing context load intelligently without requiring manual conversation resets.

## Problem Statement

Achieving consistent and predictable outcomes with AI agents is often complicated by the heavy context load that accumulates during interactions with large codebases.

A variety of strategies have been developed to mitigate this, including some already implemented in Claude Code—for example, context truncation, which summarizes previous conversation history to free up space for future tasks.

However, experienced users of AI coding tools often develop their own informal "muscle memory" methods for managing context.

### Current Pain Points

- Users instinctively start new conversations when sensing inference quality deterioration due to accumulated context
- The "tipping point" is usually reached well before the full context limit
- Manual reset habits work as a practical workaround but feel unnecessary
- Lack of transparency about whether Claude Code spawns new conversations for certain tasks
- Users cannot make informed decisions about how to structure their work

## Proposed Solution

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

New tasks could always be initiated in new conversations by default:
- Tasks represent discrete, self-contained units of work that do not depend on conversational history
- Only depend on:
  - The general project context (e.g., the codebase)
  - The persistent memory retained by Claude Code
- Ensures that trailing context does not degrade performance
- Each task begins with a clean, focused context

## Benefits

- Clear understanding of how Claude Code handles task management and context allocation
- More predictable results
- Higher inference quality
- Fewer issues caused by degraded context
- Users can trust that the agent is managing context intelligently
- Manual intervention to "reset" inference quality becomes obsolete

## Alternative Solutions

Manual management of conversations and task resets to approximate the above behavior.

## Priority

High — This feature would have a significant impact on productivity and reliability.

## Feature Category

Other

## Additional Context

Currently, when new tasks are added in Claude Code, they appear to be appended to a task list that the model processes within the same conversation. This list is visible in the UI, suggesting a sequential execution model within a single conversational thread.

If, behind the scenes, Claude Code is actually spawning new conversations to handle certain tasks, this distinction would be valuable to surface to the user. Greater transparency about this behavior would allow users to make more informed decisions.
