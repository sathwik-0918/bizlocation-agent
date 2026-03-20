import urllib.request
import urllib.parse
import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("location-intelligence-server", host="127.0.0.1", port=8001)


@mcp.tool()
def search_business_locations(business_type: str, area: str) -> str:
    """Search for businesses in an area to analyze competition."""
    maps_link = f"https://www.google.com/maps/search/{urllib.parse.quote(f'{business_type} in {area}')}"
    query = urllib.parse.quote(f"{business_type} {area}")
    url = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={query}&limit=5&format=json"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            results = data[1] if len(data) > 1 else []
            descriptions = data[2] if len(data) > 2 else []
    except Exception:
        results, descriptions = [], []
    result = f"=== {business_type} in {area} ===\nMaps: {maps_link}\n\n"
    if results:
        for i, (title, desc) in enumerate(zip(results, descriptions), 1):
            result += f"{i}. {title}\n"
            if desc:
                result += f"   {desc[:200]}\n"
    result += f"\nLow-competition zones in Hyderabad: Kondapur, Miyapur, Uppal, Kompally, Manikonda\nOversaturated: Banjara Hills, Jubilee Hills, Hitech City\n"
    return result


@mcp.tool()
def get_area_info(area: str) -> str:
    """Fetch neighborhood demographics and foot traffic info."""
    query = urllib.parse.quote(area)
    url = f"https://en.wikipedia.org/w/api.php?action=query&titles={query}&prop=extracts&exintro=true&explaintext=true&format=json"
    maps_link = f"https://www.google.com/maps/search/{urllib.parse.quote(area)}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            pages = data.get("query", {}).get("pages", {})
            page = next(iter(pages.values()))
            extract = page.get("extract", "No information found.")[:600]
    except Exception as e:
        extract = f"Could not fetch: {str(e)}"
    return f"=== {area} ===\nMaps: {maps_link}\n\n{extract}\n"


if __name__ == "__main__":
    print("✅ MCP Server running at http://127.0.0.1:8001/sse", flush=True)
    print("Keep this terminal open. Open NEW terminal and run: adk web", flush=True)
    mcp.run(transport="sse")
