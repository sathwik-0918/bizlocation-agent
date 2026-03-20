#!/bin/bash
python bizlocation_agent/adk_agent/location_mcp_server/server.py &
sleep 3
cd bizlocation_agent/adk_agent
adk web --host 0.0.0.0 --port ${PORT:-8080}
