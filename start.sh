#!/bin/bash
echo "Creating .env..."
cat > /app/adk_agent/mcp_location_app/.env << EOF
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=dummy
GROQ_API_KEY=${GROQ_API_KEY}
MODEL=${MODEL}
EOF
python /app/adk_agent/location_mcp_server/server.py &
sleep 8
cd /app/adk_agent
exec adk web --host 0.0.0.0 --port ${PORT:-8080}
