# Feature Request: Digital Zoom/Pan Presets

**Source:** [dermotduffy/advanced-camera-card Issue #2132](https://github.com/dermotduffy/advanced-camera-card/issues/2132)
**Date:** July 19, 2025
**Status:** Open
**Label:** Feature Request

---

## Summary

Request for the ability to save multiple digital zoom and pan positions as presets within the Advanced Camera Card integration for Home Assistant.

## Use Case

Using IP cameras (RearLink and TP-Link models) without native PTZ support to monitor a newborn. Currently relying on the card's digital zoom capabilities but losing configured zoom settings when switching between camera views.

## Problem

Carefully configured zoom views are lost when switching between different camera views, requiring manual readjustment each time.

## Requested Functionality

The feature should enable:
- Saving specific zoom/pan coordinates as named presets
- Persistence of presets across different camera view switches
- Quick restoration to preferred zoom levels without manual readjustment
- Similar functionality to home positions on traditional PTZ cameras

## Quote

> "Save digital zoom positions as preset positions within your software...prevent the loss of a carefully configured zoom view"

## Developer Response

The maintainer (Dermot Duffy) informed that single pan/zoom "home" presets already exist via configuration parameters, though multiple presets are not currently supported. A single configurable home position would address the specific needs described.

## Benefits

1. Eliminates need for manual readjustment
2. Provides PTZ-like functionality for non-PTZ cameras
3. Improves usability for monitoring applications
4. Saves time when switching between camera views
