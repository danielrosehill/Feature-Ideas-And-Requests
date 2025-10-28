# Feature Request: Keyboard Shortcuts for Voice Capture Control

**Source:** [mkiol/dsnote Issue #230](https://github.com/mkiol/dsnote/issues/230)
**Date:** March 13, 2025
**Status:** Closed (Completed)

---

## Summary

Request for implementing keyboard shortcuts to start and stop voice recording in DSNote.

## Original Request

While the application has a "text to active window" feature that enhances its utility for browser-based work, using it lacks keyboard shortcut support, making it impractical for daily use.

> "It's difficult to use it for this purpose, however, without a keyboard shortcut."

## Resolution

The issue was resolved through discussion with the maintainer (mkiol), who confirmed that **keyboard shortcuts are already implemented**, though with platform-specific limitations.

## Platform Support

- **X11:** Shortcuts function fully
- **Wayland:** Support added in version 4.8.0 Beta, requiring XDG Portal with GlobalShortcuts API (currently supported on KDE Plasma)
- **GNOME 48+:** Global shortcuts now supported on Fedora 42, accessible via GNOME settings

## Outcome

The maintainer also committed to improving documentation clarity regarding where users configure these shortcuts across different desktop environments.

## Benefits

1. Hands-free voice recording initiation
2. Seamless integration with browser-based workflows
3. Improved accessibility for daily use
4. Better productivity for dictation-heavy work

## Note

This feature request was successfully resolved - keyboard shortcuts already exist and documentation is being improved.
