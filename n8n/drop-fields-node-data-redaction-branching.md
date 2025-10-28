# Drop Fields Node for Data Redaction and Branching

**Request Date:** August 19, 2025
**Source:** [n8n Community Forum](https://community.n8n.io/t/drop-fields-node-for-data-redaction-and-branching/171717)
**Category:** Data Transformation

## Overview

A feature request to add capability for excluding specific fields from JSON arrays within n8n workflows. This functionality would enable more efficient data redaction and branching for different stakeholder groups where compliance or exposure restrictions require limiting visible information.

## Use Case

Maintaining a GitHub repository with system prompt configurations where most are open source, but some contain personal data. Currently requires boolean flags to control workflow branching with manual mapping of which fields to retain for public-facing branches.

## Current Workaround

Multiple Set field nodes are chained together, each mapping only the desired input fields to keep. This approach is verbose and maintenance-intensive.

## Proposed Solution

Two implementation options:

### Option 1: Dedicated Field Redaction Node
Create a specialized node specifically for dropping/excluding fields from data objects.

### Option 2: Enhance Existing Set Node
Add a "field exclusion" mode to the existing Set node that allows users to identify fields to drop rather than fields to preserve. This would be the inverse of the current field mapping approach.

## Benefits

- Simplifies data redaction workflows
- Reduces node count in complex workflows
- Improves maintainability of branching logic
- Better compliance with data exposure restrictions
- More intuitive workflow design for data filtering scenarios
