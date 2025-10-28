# Feature Request: Category for National Security Events

**Source:** [nielsfaber/alarmo Issue #1156](https://github.com/nielsfaber/alarmo/issues/1156)
**Date:** May 11, 2025
**Status:** Closed (September 17, 2025)
**Labels:** feature_request, Stale

---

## Summary

Proposal to add a dedicated alert category for national security events within Alarmo, a Home Assistant alarm management application.

## Context

Living in Israel and using a "Red Alert" extension that delivers notifications from the national emergency system regarding rocket and drone threats. Alarmo currently auto-detects these sensors but categorizes them as "environmental"—the same classification used for smoke detectors and similar devices.

## Core Issue

> "Rather than ring up all my own automations for the sensor class, wouldn't it make much more sense to regard it as another type of security warning?"

The concern is that lumping national security alerts with environmental sensors creates inappropriate response scenarios where "a burglar trespassing would cause the same response as a fire alarm or missile attack."

## Broader Application

This feature would benefit users globally who integrate various national emergency sensors (tornado alerts, etc.) into their home automation systems.

## Developer Response

Project maintainer Niels Faber indicated the environmental category was acceptable but recommended leveraging Alarmo's "areas" functionality as an alternative workaround, allowing users to configure distinct actions for different alert scenarios.

The issue was closed without implementing the requested new category.

## Rationale

1. National security alerts warrant distinct categorization
2. Different alert types should trigger different response automations
3. Environmental sensors (smoke, CO2) have different urgency profiles than security threats
4. Global applicability for various emergency alert systems
