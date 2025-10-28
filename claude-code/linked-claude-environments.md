# Feature Request: The Ability to Link Multiple Claude Code Environments

**Source:** GitHub Issue #10069
**Author:** Daniel Rosehill
**Date:** October 21, 2025
**Labels:** enhancement, area:core
**Status:** Open
**Community Reactions:** +1 (1)

## Problem Statement

Consider this common usage scenario:

A user utilizes Claude Code to SSH into a remote environment (either on the LAN or elsewhere). That remote environment (environment 2) also has Claude CLI installed. This configuration often results from experimenting with different approaches: running Claude on the server versus using MCP or direct SSH to connect from a local Claude Code instance.

Currently, there is no way for Claude Code to "remember" or intelligently manage these networked Claude Code environments, similar to how bash aliases work for remote connections.

## Proposed Solution

Create a system where Claude Code can discover, register, and intelligently interact with other Claude Code installations on remote environments.

### Workflow

1. **User connects to an environment** via SSH or other method
2. **Claude detects the presence of another Claude installation** by finding artifacts like:
   - `.claude` directory
   - `CLAUDE.md` files
   - Claude CLI binary
   - Configuration files
3. **Claude prompts the user**: "Would you like me to remember this environment? Please give it a name."
4. **Claude stores environment metadata**:
   - Environment name (user-defined)
   - Connection parameters (IP address, authentication method)
   - Detected Claude Code version and capabilities
   - Available slash commands
   - Configuration details
5. **Remote can be recalled for connection** independently of whether it's defined in the user's SSH config or aliases

### Intelligent Environment Awareness

When connecting to a registered Claude-enabled environment, the connecting Claude agent could:
- Inspect and utilize the remote environment's slash commands
- Understand the remote's configuration and capabilities
- Coordinate operations between local and remote Claude instances
- Provide enhanced context about the remote environment's state

## Potential Advantages

- **Greater flexibility** than configuring traditional SSH aliases
- **Environment awareness**: The connecting agent knows to expect another Claude-enabled environment
- **Command discovery**: Can inspect and utilize remote slash commands
- **Consistent behavior**: Provides certainty around how Claude behaves when it finds another Claude installation
- **Simplified workflows**: No need to manually configure connections in multiple places
- **Enhanced coordination**: Potential for local and remote Claude instances to work together

## Use Cases

1. **Development across multiple machines**: Seamlessly work between local workstation and remote development server
2. **LAN-based workflows**: Connect to home server or NAS running Claude Code
3. **Cloud development environments**: Manage connections to cloud-based development instances
4. **Team environments**: Share and discover Claude-enabled environments within a team

## Implementation Considerations

- **Security**: Ensure proper authentication and encryption for remote connections
- **Discovery mechanism**: How to safely detect remote Claude installations
- **Configuration storage**: Where to store remote environment metadata
- **Connection management**: Handle connection failures, timeouts, and reconnection
- **Version compatibility**: Handle different Claude Code versions across environments

## Priority

Low — Nice to have, but could significantly enhance multi-environment workflows.

## Feature Category

Configuration and Settings, Remote Development

## Additional Context

This feature would complement existing SSH and MCP capabilities by providing a Claude-native way to manage and interact with distributed Claude Code environments. It represents a step toward more sophisticated multi-environment workflows where Claude Code can intelligently coordinate across different machines and contexts.
