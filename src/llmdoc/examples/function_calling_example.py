import json
from typing import Dict, Any, List
from ..clients.factory import create_client
from ..tools import AVAILABLE_TOOLS

async def handle_function_call(function_call: Dict[str, Any], provider: str) -> Dict[str, Any]:
    """Handle the function call and return the result."""
    tool_name = function_call.name
    tool_args = json.loads(function_call.arguments)
    
    # Find the appropriate tool
    tool = next(tool for tool in AVAILABLE_TOOLS if tool.name == tool_name)
    
    # Run the tool
    return await tool.run(**tool_args)

async def main(provider: str = "openai"):
    # Create the appropriate client
    client = create_client(provider)
    
    # Get function definitions from tools
    function_definitions = [tool.function_definition for tool in AVAILABLE_TOOLS]
    
    # Example conversation
    messages = [
        {"role": "user", "content": "What's the weather in New York and can you add 2+3+4?"}
    ]
    
    while True:
        # Get response from LLM
        response = await client.chat_completion(
            messages=messages,
            functions=function_definitions
        )
        
        # Get the message from the response
        message = response.choices[0].message
        
        # Check if the model wants to call a function
        if "function_call" in message:
            # Handle the function call
            function_result = await handle_function_call(message.function_call, provider)
            
            # Add the function call and result to the messages
            messages.append({
                "role": "assistant",
                "content": None,
                "function_call": message.function_call
            })
            messages.append({
                "role": "function",
                "name": message.function_call.name,
                "content": json.dumps(function_result)
            })
        else:
            # No function call, just a regular message
            print(f"Assistant: {message.content}")
            break

if __name__ == "__main__":
    import asyncio
    # Example with different providers
    asyncio.run(main("openai"))  # Use OpenAI
    # asyncio.run(main("gemini"))  # Use Gemini
    # asyncio.run(main("anthropic"))  # Use Anthropic