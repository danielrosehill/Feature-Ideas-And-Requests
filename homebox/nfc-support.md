# Feature Request: NFC Support for Inventory Management

**Source:** [sysadminsmedia/homebox Issue #441](https://github.com/sysadminsmedia/homebox/issues/441)
**Date:** January 4, 2025
**Status:** Closed (Converted to Discussion #537)
**Label:** ⬆️ Enhancement
**Reactions:** 4 👍

---

## Summary

Request for improved NFC tag creation workflow and potential in-app NFC writing capabilities for Homebox inventory management.

## Problem Statement

Currently using NFC tags for inventory management in Homebox but finding the workflow cumbersome. The process requires manually copying item URLs to clipboard before writing tags—a tedious process that doesn't scale well for large inventories.

## Proposed Solutions

### Idea 1: Copy-to-Clipboard Button

A simple button (potentially beside the QR code button) to copy an item's URL directly to the clipboard, streamlining tag creation without navigating through share menus repeatedly.

### Idea 2: Dedicated NFC Tag Creation Tool

An in-app utility featuring:
- Text field for item ID entry (no hashtag prefix requirement)
- Dynamic display of matched item title for verification
- Copy-to-clipboard button for the item URL
- Optional "write to NFC" button that could integrate with Android's default NFC writing app

## Context

> "It's faster to tap an NFC tag than it is to go into your camera app, scan a barcode"

NFC tags provide quick identification for inventory items. Both barcode and NFC approaches have merit, and the requester offered to assist with implementation.

## Community Interest

4 upvotes from users indicating demand for this feature.

## Outcome

The issue was converted to a discussion (#537) for broader community input.

## Benefits

1. Streamlined NFC tag creation workflow
2. Faster inventory item access compared to barcode scanning
3. Reduced manual steps for large-scale tagging
4. Better scalability for extensive inventories
5. Improved user experience for mobile inventory management

## Implementation Considerations

- Copy-to-clipboard functionality (simple, immediate value)
- Optional NFC writing integration
- Item ID lookup with verification
- Mobile-first design for practical inventory management
