from abc import ABC, abstractmethod

class Tool(ABC):
    """Base class for all tools."""
    name = ""
    description = ""
    parameters = {}  # JSON Schema

    @abstractmethod
    def execute(self, params):
        """Execute the tool. Returns string output."""
        ...

    def get_schema(self):
        """Return OpenAI function calling schema."""
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.parameters,
            },
        }


