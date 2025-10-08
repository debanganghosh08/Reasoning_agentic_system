# File: agent_backend/tools.py

from google.adk.tools import tool
import math

@tool
def calculator(expression: str) -> str:
    """
    A tool to evaluate a mathematical expression.
    Use this for any calculations involving numbers.
    Example expression: "(100 + 50) * 2"
    
    Args:
        expression: The mathematical expression to evaluate.

    Returns:
        The result of the calculation as a string.
    """
    print(f"--- Calling Calculator with expression: {expression} ---")
    try:
        # A safer version of eval to prevent malicious code execution
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed_names["abs"] = abs
        
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return f"The result is: {result}"
    except Exception as e:
        return f"Error: Could not evaluate the expression due to {e}"