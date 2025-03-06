from typing import Dict, Any, List
from pydantic import BaseModel, Field
from .base import BaseTool

class CalculatorParams(BaseModel):
    """Parameters for the calculator function."""
    operation: str = Field(..., description="The mathematical operation to perform")
    numbers: List[float] = Field(..., description="List of numbers to perform the operation on")

class CalcTool(BaseTool):
    """Tool for performing basic mathematical operations."""
    
    name = "calculator"
    description = "Perform basic mathematical operations on a list of numbers"
    parameters_schema = CalculatorParams
    
    async def run(self, operation: str, numbers: List[float]) -> Dict[str, Any]:
        """Execute the calculator operation."""
        if operation == "add":
            result = sum(numbers)
        elif operation == "multiply":
            result = 1
            for num in numbers:
                result *= num
        else:
            raise ValueError(f"Unsupported operation: {operation}")
        
        return {
            "operation": operation,
            "numbers": numbers,
            "result": result
        }