# Feature Request: Background Process Management

**Source:** [google-gemini/gemini-cli Issue #6963](https://github.com/google-gemini/gemini-cli/issues/6963)
**Date:** August 24, 2025
**Status:** Open
**Labels:** area/core, kind/enhancement
**Reactions:** 1 👍

---

## Summary

Request for the ability to maintain conversations with commands running in the background, allowing users to continue interacting with the agent without interrupting long-running commands.

## Problem Statement

When using Ctrl+C to pause conversation, it terminates both the dialogue and any background script execution. This makes it impossible to check on lengthy installation processes (e.g., PyTorch on Ubuntu) without risking data loss from interrupting operations like Docker pulls.

## Current Limitation

The tool is currently very effective for server-side debugging, but the inability to monitor long-running processes without halting execution significantly limits utility for extended operations.

## Proposed Solution

Implement process isolation similar to agentic IDEs like Windsurf, potentially by:
- Spawning background processes that operate independently from the active conversation thread
- Maintaining a registry of running tasks
- Allowing conversation to continue while processes execute in the background

## Use Case

Monitoring status of long-running operations (installations, builds, deployments) without halting execution or losing progress.

## Benefits

1. Enhanced utility for extended operations
2. Ability to check status without interrupting processes
3. Better workflow for server-side debugging and maintenance
4. Improved user experience for multi-step operations
