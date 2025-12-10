# MCP Server - Deployment

A simple MCP (Model Context Protocol) server that provides tools for basic operations.

## Installation

Install using `uvx`:

```bash
uvx --from git+https://github.com/sri-thyagarajan/mcpserver.git mcp-server
```

## Configuration

Add this to your MCP client configuration:

```json
{
  "add": {
    "command": "/Users/sthyagarajan/.local/bin/uvx",
    "args": [
      "--from",
      "git+https://github.com/sri-thyagarajan/mcpserver.git",
      "mcp-server"
    ]
  }
}
```

## Tools

- `add_two_numbers`: Adds two integers together

