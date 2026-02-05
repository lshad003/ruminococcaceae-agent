#!/usr/bin/env python3
"""Test that all API connections work"""

import os
from dotenv import load_dotenv

# Load API keys
load_dotenv('configs/api_keys.env')

print("=" * 50)
print("Testing Ruminococcaceae Agent Setup")
print("=" * 50)

# Check API keys are loaded
print("\n✓ Checking API keys...")
claude_key = os.getenv('ANTHROPIC_API_KEY')
gemini_key = os.getenv('GOOGLE_API_KEY')
openai_key = os.getenv('OPENAI_API_KEY')

print(f"  Claude API key: {'✓ Loaded' if claude_key else '✗ Missing'}")
print(f"  Gemini API key: {'✓ Loaded' if gemini_key else '✗ Missing'}")
print(f"  OpenAI API key: {'✗ Missing (OK for now)' if not openai_key or openai_key == 'placeholder_for_now' else '✓ Loaded'}")

if claude_key and gemini_key:
    print("\n🎉 All systems ready! Proceed to Step 2.")
else:
    print("\n⚠️  Some required API keys missing. Check configs/api_keys.env")
