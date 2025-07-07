from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import subprocess
import os

# -------- Tool 1: Requirement Collector --------
class RequirementInput(BaseModel):
    topic: str = Field(..., description="Type of project to build")
    language: str = Field(..., description="Programming language to use")
    extra: str = Field(..., description="Any additional preferences or features")

class RequirementCollectorTool(BaseTool):
    name: str = "RequirementCollectorTool"
    description: str = "Collects user requirements for the project"
    args_schema: Type[BaseModel] = RequirementInput

    def _run(self, topic: str, language: str, extra: str) -> str:
        return (
            f"Project Type: {topic}\n"
            f"Programming Language: {language}\n"
            f"Preferences: {extra}"
        )


# -------- Tool 2: Developer --------
class CodeGeneratorTool(BaseTool):
    name: str = "CodeGeneratorTool"
    description: str = "Generates starter code from project requirements"
    args_schema: Type[BaseModel] = RequirementInput

    def _run(self, topic: str, language: str, extra: str) -> str:
        return f"# {language} project for: {topic}\nprint('Hello from {topic}')\n# Extra: {extra}"


# -------- Tool 3: Tester --------
class CodeTesterInput(BaseModel):
    code: str = Field(..., description="Code to test")

class CodeTesterTool(BaseTool):
    name: str = "CodeTesterTool"
    description: str = "Tests the generated code for syntax and basic functionality"
    args_schema: Type[BaseModel] = CodeTesterInput

    def _run(self, code: str) -> str:
        try:
            compile(code, '<string>', 'exec')
            return "✅ Code passed basic syntax test."
        except Exception as e:
            return f"❌ Syntax error found: {e}"


# -------- Tool 4: File Manager --------
class FileSaverInput(BaseModel):
    code: str = Field(..., description="Code to save")
    path: str = Field(..., description="Full path to save the file")


class FileSaverTool(BaseTool):
    name: str = "FileSaverTool"
    description: str = "Saves code to user-specified location"
    args_schema: Type[BaseModel] = FileSaverInput

    def _run(self, code: str, path: str) -> str:
        try:
            # Ensure parent directories exist
            directory = os.path.dirname(path)
            os.makedirs(directory, exist_ok=True)

            with open(path, 'w') as f:
                f.write(code)

            return f"✅ Code saved to: {path}"

        except Exception as e:
            return f"❌ Failed to save file: {e}"
# -------- Tool 5: Runner --------
class CodeRunnerInput(BaseModel):
    path: str = Field(..., description="Path to the file to run")

class CodeRunnerTool(BaseTool):
    name: str = "CodeRunnerTool"
    description: str = "Runs the saved code file"
    args_schema: Type[BaseModel] = CodeRunnerInput

    def _run(self, path: str) -> str:
        try:
            result = subprocess.run(["python3", path], capture_output=True, text=True)
            return result.stdout or result.stderr
        except Exception as e:
            return f"❌ Execution error: {e}"
