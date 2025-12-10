from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Deployment")


@mcp.tool()
def add_two_numbers(a: int, b: int) -> int:
    """
    Adds two numbers
    Args:
        a (int): The first number
        b (int): The second number
    Returns:
        int: The sum of the two numbers
    """
    return a + b

if __name__ == "__main__":
    mcp.run()