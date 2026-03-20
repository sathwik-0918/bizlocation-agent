import dotenv
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseConnectionParams

dotenv.load_dotenv()

def get_location_mcp_toolset():
    tools = MCPToolset(
        connection_params=SseConnectionParams(
            url="http://127.0.0.1:8001/sse",
        ),
    )
    print("✅ Location MCP Toolset connected via SSE.")
    return tools
