import os
import dotenv
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from . import tools

dotenv.load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "NOT SET")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

print(f"=== AGENT STARTING ===", flush=True)
print(f"GROQ KEY starts with: {GROQ_API_KEY[:10]}...", flush=True)

location_toolset = tools.get_location_mcp_toolset()

SYSTEM_INSTRUCTION = """
You are a Business Location Intelligence Agent.
Help users find the best area to open a business in any city.
Always use your tools:
1. Call search_business_locations to find competitors
2. Call get_area_info to understand the neighborhood
3. Give a clear recommendation with Google Maps link
"""

root_agent = LlmAgent(
    model=LiteLlm(model="groq/llama-3.3-70b-versatile"),
    name="business_location_finder_agent",
    instruction=SYSTEM_INSTRUCTION,
    tools=[location_toolset],
)

print(f"=== AGENT READY ===", flush=True)
