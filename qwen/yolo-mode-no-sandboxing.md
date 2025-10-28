# Feature Request: YOLO Mode - Easily Configurable No-Sandboxing Mode

**Source:** [QwenLM/Qwen-Agent Issue #698](https://github.com/QwenLM/Qwen-Agent/issues/698)
**Date:** August 28, 2025
**Status:** Open
**Reactions:** 2 👍

---

## Summary

Request for an optional, fully configurable mode that removes filesystem sandboxing restrictions in Qwen-Agent, allowing for unrestricted access in controlled experimental environments.

## Context

I'm really impressed with Qwen so far and (using both Claude Code and Gemini CLI daily as well) find the model often doing a great job at debugging and general sysadmin tasks.

I am almost certainly in a tiny minority here, but there are **certain contexts** in which I would find it helpful to remove the filesystem sandboxing completely.

**Context:** I'm working on my homelab machine which has ZFS level snapshotting.

This is the box that I use to "learn fast and break things" with. I'll supervise Qwen's actions as I always do. But the guiding principle here is that less restrictions are better.

## Current Issue

I tried playing around with the sandboxing environment parameter (all my systems are on Linux) and couldn't seem to get it to hold.

## Proposed Solution

It would be useful to be able to configure the sandboxing through a slash command which left a persistent memory setting in Qwen's data storage on the host.

9/10 times I would stick with the (default) conservative method and expose directories deliberately. But there are instances in which a fully permissive posture would actually be the preferred configuration.

## Use Case

- **Environment:** Homelab machine with ZFS snapshots
- **Purpose:** Experimental learning and rapid prototyping
- **Safety:** Supervised usage with filesystem-level snapshots for rollback
- **Frequency:** 10% of use cases require unrestricted access, 90% use conservative defaults

## Benefits

1. Persistent configuration through slash command
2. Flexibility for advanced users in controlled environments
3. Maintains default conservative settings for typical usage
4. Enables "learn fast and break things" workflows with proper safety nets
