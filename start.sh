#!/bin/bash
export GROQ_API_KEY=$GROQ_API_KEY
export MODEL=$MODEL
printf "GOOGLE_GENAI_USE_VERTEXAI=FALSE\nGOOGLE_API_KEY=dummy\nGROQ_API_KEY=$GROQ_API_KEY\nMODEL=$MODEL\n" > /app/adk_agent/mcp_location_app/.env
cat /app/adk_agent/mcp_location_app/.env
python /app/adk_agent/location_mcp_server/server.py &
sleep 8
cd /app/adk_agent
adk web --host 0.0.0.0 --port 8080