from .calc_tool import CalcTool
from .weather_tool import WeatherTool
from .calendar_tool import CalendarTool

__all__ = ['CalcTool', 'WeatherTool', 'CalendarTool']

# List of all available tools
AVAILABLE_TOOLS = [
    CalcTool(),
    WeatherTool(),
    CalendarTool()
]