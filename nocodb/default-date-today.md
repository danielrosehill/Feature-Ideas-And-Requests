# Feature Request: Default Date Value to Today

**Source:** [nocodb/nocodb Issue #9224](https://github.com/nocodb/nocodb/issues/9224)
**Date:** August 13, 2024
**Status:** Closed (Completed)
**Labels:** 🔦 Type: Feature
**Reactions:** 2 👍

---

## Summary

Request for the ability to configure a default value for date parameters to be today's date.

## Use Case

A common database need: "the ability to configure default parameters for a date column type with today's date."

The practical application involves data entry workflows where most entries use the current date, with occasional retrospective entries.

## Proposed Solution

> "Just as you can configure a default option in dropdowns, it would be great if there were an option to have a default value for the date field to default to today."

The suggestion mirrors existing functionality in dropdown fields, applying the same principle to date columns.

## Resolution

**Developer Response (dstala, August 26, 2024):**
> "This feature is supported now. Should be available from next OSS release."

The issue was marked as **COMPLETED** and closed on August 26, 2024.

## Status

**IMPLEMENTED** - This feature has been added to NocoDB and is available in the OSS release.

## Benefits

1. Reduces repetitive data entry
2. Speeds up workflow for current-date entries
3. Maintains flexibility for backdated entries
4. Consistent with existing default value patterns
5. Improves user experience for common use cases

## Implementation

Date columns can now be configured with a default value of today's date, similar to how dropdown fields have default options.
