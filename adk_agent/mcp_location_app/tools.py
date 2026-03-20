import os
import dotenv
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseConnectionParams

dotenv.load_dotenv()

def get_location_mcp_toolset():
    return MCPToolset(
        connection_params=SseConnectionParams(
            url="http://127.0.0.1:8001/sse",
        ),
    )
