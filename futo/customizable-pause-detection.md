# Feature Request: Customizable Pause Detection for Voice Input

**Source:** [futo-org/android-keyboard Issue #984](https://github.com/futo-org/android-keyboard/issues/984)
**Date:** December 27, 2024
**Status:** Open
**Labels:** Enhancement, QoL, Voice Input
**Assigned to:** abb128

---

## Summary

Proposal to add configurable pause detection settings for the keyboard's voice input feature to accommodate different user preferences and use cases.

## Use Case

When using voice-to-text for documentation authoring, frequent pauses are needed to think. Manual control over dictation start/stop is preferred rather than automatic cutoff after silence, as premature termination requires restarting the process repeatedly.

## Problem

Current automatic pause detection and microphone cutoff works well for brief voice captures but is problematic for longer dictation sessions where thoughtful pauses are necessary.

## Proposed Solution

Implement two voice input modes:

### 1. Short Input Mode
- Maintains current automatic pause detection
- Automatic microphone cutoff for brief voice captures
- Ideal for quick messages and short inputs

### 2. Extended Input Mode
- Allows manual microphone control for longer dictations
- Prevents automatic termination during thoughtful pauses
- User controls when to stop recording

## Implementation Options

The proposal suggests either:
- Two separate voice input icons on the keyboard
- A user-toggleable setting with keyboard preference defaults
- On-the-fly switching based on immediate needs

## Community Feedback

A commenter (weedy) suggested refinement: rather than dual buttons cluttering the keyboard, implement an in-session toggle appearing when the interface prompts "try saying something," allowing users to switch modes without multiple interface elements.

## Benefits

1. Flexibility for different dictation use cases
2. Accommodates both quick inputs and extended documentation
3. Reduces frustration from premature cutoff
4. Maintains efficiency for brief voice inputs
5. Better support for content creation workflows

## User Type

Users who engage in longer-form dictation, documentation authoring, or content creation with natural pauses for thinking.
