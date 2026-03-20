#!/bin/bash
export GROQ_API_KEY=
export MODEL=
export GOOGLE_GENAI_USE_VERTEXAI=FALSE
export GOOGLE_API_KEY=dummy
mkdir -p /app/adk_agent/mcp_location_app
printf 'GOOGLE_GENAI_USE_VERTEXAI=FALSE\nGOOGLE_API_KEY=dummy\nGROQ_API_KEY=%s\nMODEL=%s\n' "" "" > /app/adk_agent/mcp_location_app/.env
cat /app/adk_agent/mcp_location_app/.env
python /app/adk_agent/location_mcp_server/server.py &
echo "Waiting for MCP server..."
sleep 10
echo "Starting ADK web..."
cd /app/adk_agent
exec adk web --host 0.0.0.0 --port 
