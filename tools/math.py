from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two integers."""
    return a - b

@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide two integers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    mcp.run(transport="streamable-http")