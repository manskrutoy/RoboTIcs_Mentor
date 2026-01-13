"""AI integration module for Google Gemini API communication."""

from .gemini_client import GeminiClient
from .prompts import SYSTEM_PROMPT

__all__ = ["GeminiClient", "SYSTEM_PROMPT"]
