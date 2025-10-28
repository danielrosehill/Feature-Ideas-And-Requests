# Feature Request: AI-Powered Product Recognition

**Source:** [sysadminsmedia/homebox Issue #685](https://github.com/sysadminsmedia/homebox/issues/685)
**Date:** May 9, 2025
**Status:** Closed as Not Planned

---

## Summary

Proposal to integrate AI capabilities into Homebox to automatically extract product information from uploaded photos.

## Proposed Solution

Users would configure an OpenAI API key in settings. Upon uploading a product image, a button labeled "send to OCR" would trigger image analysis. The system would send the photo to OpenAI or Ollama with instructions to:

- Identify the product and manufacturer
- Retrieve approximate retail pricing (RRP)
- Transcribe serial numbers and unique identifiers
- Extract abbreviated product specifications
- Return structured data that populates item fields

## Performance Note

> "OpenAI is pretty efficient at this kind of task and could return the info in three seconds"

Personal experience processing 400 inventory items efficiently was shared as evidence of feasibility.

## Developer Response

Project maintainer tankerkiller125 declined, stating the feature extends beyond Homebox's scope while encouraging third-party tool development using the available APIs.

## Contributor Interest

All three contribution checkboxes were marked:
- Willing to help implement and maintain
- Willing to sponsor development

## Benefits

1. Dramatically speeds up inventory cataloging
2. Reduces manual data entry errors
3. Automatically captures product details and specifications
4. Extracts serial numbers and identifiers
5. Provides pricing information for insurance/valuation
6. Scales efficiently for large inventories

## Technical Approach

- Integration with OpenAI or local Ollama models
- User-configurable API keys
- Optional feature activation
- Structured data return for field population
