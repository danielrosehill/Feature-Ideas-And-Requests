# Feature Request: System Prompt for Report Generation

**Request Date:** October 2025
**Source:** [Reddit r/notebooklm](https://www.reddit.com/r/notebooklm/comments/1oih0z5/feature_request_system_prompt_for_report/)
**Category:** Feature Requests / Report Generation

## Overview

A feature request to enable notebook-level system prompts and custom report templates in NotebookLM, allowing users to define consistent stylistic instructions and formatting rules that apply to all generated reports without needing to specify them in every individual prompt.

## Use Case Description

Working with a book author to ideate short-form content created from longer-form text. The process helps with:
- Ideating social media posts
- Populating an internal wiki
- Creating outlines for long-form writing
- Adapting content for different formats and audiences

## Current Experience

The **Reports → Create** button is a fantastic mechanism for generating content, but it has limitations:

### Current Friction

Unless explicitly prompted against it, NotebookLM will tend to format reports as "In his book, X says..." This third-person referential style is:
- Not wanted for the intended use case
- Not useful when creating content from one's own material
- Requires manual correction in every custom prompt

### The Problem

When using NotebookLM to create summaries of one's own long-form content for different formats and audiences, the constant references to "the book" or "the author" create unnecessary friction and inconsistency.

## Proposed Solution

### Notebook-Level System Prompt

Enable users to define a system prompt for each notebook that specifies:
- **Purpose**: "The purpose of this notebook is [description]"
- **Stylistic Instructions**: Consistent desired format rules that apply to all reports
- **Voice Guidelines**: Writing perspective (first person, third person, etc.)
- **Content Rules**: What to include/exclude from generated content

### Example Configuration

```
Purpose: Creating short-form content from a book manuscript for various audiences
Rules:
- Don't refer to "the book" (we know the material is based on that)
- Write reports in the third person
- Focus on actionable insights
- Use conversational tone
```

### Custom Report Templates (Extension)

As an extension, allow users to create custom report format templates. The concatenated prompt sent to Gemini would be structured as:

```
System Prompt (project context) + Template + Specific Request
```

This would enable consistent, repeatable report generation with minimal per-request customization.

## Benefits

- **Consistency**: All reports adhere to the same stylistic guidelines
- **Efficiency**: No need to repeat formatting instructions in every custom prompt
- **Flexibility**: Different notebooks can have different purposes and styles
- **Professionalism**: Outputs are immediately usable without manual editing
- **Scalability**: Supports creating content for multiple formats and audiences
- **Better UX**: Reduces friction in content generation workflows

## Impact

This feature would make NotebookLM significantly more powerful for content creators, authors, and professionals who need to consistently repurpose long-form content into various short-form formats while maintaining specific style guidelines and avoiding repetitive prompt engineering.
