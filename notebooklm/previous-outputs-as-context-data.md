# Feature Request: Previous Outputs as Context Data

**Request Date:** October 2025
**Source:** [Reddit r/notebooklm](https://www.reddit.com/r/notebooklm/comments/1oihj1l/feature_request_previous_outputs_are_context_data/)
**Category:** Feature Requests / Memory & Context Management

## Overview

A feature request to enable NotebookLM to maintain persistent memory over prior outputs, allowing the AI to reference both the guiding context data and the work it has done previously. This would enable truly iterative deep research workflows.

## Use Case: Deep Research for Major Life Projects

NotebookLM is ideal for "deep research" tasks aimed at ideating solutions to major ongoing life projects such as:
- Job hunt / career development
- Mental health / therapy work
- Health problems and specialist identification
- Other complex, long-term problems requiring thoughtful iteration

These are not one-off questions but major projects that require ongoing thoughtful experimentation to really ideate and drill down.

## Current Workflow Pattern

The existing workflow that works well with NotebookLM:
1. Record lengthy voice notes (sometimes multiple)
2. Use AI speech-to-text transcription
3. Lightly clean up transcripts and reformat them for use as context data
4. Upload context to NotebookLM for analysis

This pattern allows speaking for an hour to gather contextual information that would be tedious to type by hand, without needing to handle technical complexity like chunking and embeddings.

## The Missing Piece: Output Memory

NotebookLM currently provides excellent retrieval over context data, but lacks **persistent memory over prior outputs**.

### Why This Matters

**Example: Career Development & Job Hunting**

A powerful pattern is asking the AI to ideate good-fit potential employers and organize them for later review. However, when run repetitively without output memory, the AI tends to repeat the same ideas over and over again, missing the long-tail thinking that AI can provide.

**The Solution: Memory Over Both Context AND Prior Work**

When the AI knows both:
1. Your guiding context data
2. The work it has done previously

This combination yields truly powerful deep research utilities that can iterate without repetition.

## Comparison with Claude Code

Claude Code currently enables this pattern by:
- Organizing repos into context data and output storage
- Indexing both context and outputs before providing subsequent analyses
- Building on previous work iteratively

## Proposed Solution

Enable NotebookLM to:
1. Track and index previous outputs as part of the notebook's knowledge base
2. Reference prior analyses when generating new insights
3. Avoid repeating previously provided suggestions
4. Build iteratively on previous work

## Benefits

- Enables true iterative deep research workflows
- Prevents repetitive outputs in ongoing projects
- Unlocks long-tail thinking and comprehensive exploration
- Makes NotebookLM ideal for complex, multi-session research projects
- Better serves users working on major life projects requiring sustained AI assistance
- Leverages NotebookLM's cloud-based, visual interface for persistent research workflows

## Impact

This feature would transform NotebookLM from a context-retrieval tool into a true research companion capable of sustained, memory-aware iteration over complex problems.
