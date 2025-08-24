# MCP server stub
try:
    from mcp.server.fastmcp import FastMCP
except Exception:
    class FastMCP:
        def __init__(self,name): pass
        def tool(self):
            def deco(fn): return fn
            return deco
        def run(self): print('FastMCP stub')
from .tools import interpret_file,summarize
mcp=FastMCP('cpa')
mcp.tool()(interpret_file)
mcp.tool()(summarize)
if __name__=='__main__': mcp.run()
