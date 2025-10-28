# Feature Request: Scalable Conversation Storage Database

**Source:** [Mintplex-Labs/anything-llm Issue #2583](https://github.com/Mintplex-Labs/anything-llm/issues/2583)
**Date:** November 4, 2024
**Status:** Closed (Completed)
**Labels:** enhancement, feature request

---

## Summary

Request for the ability to store conversations in a custom endpoint to enable parallel exploration of conversation history through connected systems like wikis and knowledge management platforms.

## Primary Request

The ability to "store conversations in a custom endpoint" for integration with external knowledge management systems.

## Key Requirements

- Individual outputs should be grouped into their constituent conversations
- Support for scalable database storage solutions
- Suggested database options: PostgreSQL or MongoDB

## Use Case

Enable parallel exploration of conversation history through connected systems like wikis and knowledge management platforms, rather than being limited to the built-in interface.

## Developer Response

Project maintainer Timothy Carambat noted:

1. **Current Solution:** Users can already leverage the existing `/v1/system/export-chats` API endpoint to extract conversation data for upload to preferred databases

2. **Design Philosophy:** SQLite remains the primary choice for the current implementation due to zero-configuration requirements—particularly important since the desktop application deployment cannot reasonably require external database setup from end users

3. **Future Plans:** Additional database support is tracked separately (issue #2574). Prisma schema portability between SQLite and PostgreSQL exists with minor adjustments needed.

## Resolution

The feature can be achieved using the existing API endpoint for chat export, allowing users to integrate with their preferred database systems.

## Benefits

1. Integration with external knowledge management platforms
2. Scalable storage for large conversation histories
3. Advanced search and analysis capabilities
4. Cross-platform conversation exploration
5. Custom data retention policies

## Alternative Implementation

Use the `/v1/system/export-chats` API endpoint to:
- Extract conversation data programmatically
- Upload to preferred database (PostgreSQL, MongoDB, etc.)
- Build custom interfaces for conversation exploration
- Integrate with existing knowledge management workflows
