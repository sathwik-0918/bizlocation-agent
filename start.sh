#!/bin/bash
# Start MCP server in background
python /app/adk_agent/location_mcp_server/server.py &
sleep 3
# Start ADK web from the correct directory
cd /app/adk_agent
adk web --host 0.0.0.0 --port ${PORT:-8080}
