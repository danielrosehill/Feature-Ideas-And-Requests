# Feature Request: Frontend Speech-to-Text Configuration

**Source:** [danny-avila/LibreChat Issue #5252](https://github.com/danny-avila/LibreChat/issues/5252)
**Date:** January 10, 2025
**Status:** Closed (Converted to Discussion #5253)
**Labels:** ✨ enhancement

---

## Summary

Request to move speech-to-text configuration from YAML files to the application's user interface for easier management and more reliable settings persistence.

## Primary Request

> "The ability to configure speech-to-text within the app itself rather than having to do so via the YAML configuration files."

## Problem

Currently, users must edit configuration files directly, which is described as cumbersome and unreliable for maintaining settings.

## Technical Insights

**Performance Considerations:**
- Extensive hands-on experience with STT services suggests cloud-based Whisper API often outperforms locally-hosted models for typical deployments lacking high-spec hardware
- Cost considerations for Whisper API integration are noted as manageable

**Provider Recommendations:**

The requester identifies underutilized ASR alternatives worth integrating:
- Amazon
- DeepGram
- Speechmatics

These vendors reportedly deliver superior voice recognition compared to browser-native options.

## Outcome

The issue was converted to a discussion thread (#5253) for broader community engagement.

## Benefits

1. Easier configuration without editing YAML files
2. More reliable settings persistence
3. Better user experience for non-technical users
4. Access to superior ASR providers
5. Improved voice recognition quality over browser-native options

## Impacted Component

General application configuration

## Additional Value

Expanding STT provider options beyond current offerings to include enterprise-grade services that outperform browser-native implementations.
