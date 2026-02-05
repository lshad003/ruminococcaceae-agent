#!/usr/bin/env python3
"""
Multi-AI Agent for Ruminococcaceae Analysis
Orchestrates Claude and Gemini for different tasks
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic
import google.generativeai as genai

# Load API keys
load_dotenv('configs/api_keys.env')

class MultiAIAgent:
    """Agent that routes tasks to appropriate AI models"""
    
    def __init__(self):
        # Initialize AI clients
        self.claude = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
        self.gemini = genai.GenerativeModel('gemini-2.5-flash')
        
        print("✓ Multi-AI Agent initialized")
        print("  - Claude Sonnet 4: Ready for bioinformatics & analysis")
        print("  - Gemini 2.5 Flash: Ready for literature review & biological interpretation")
    
    def ask_claude(self, prompt, system_prompt=None):
        """Use Claude for bioinformatics tasks"""
        messages = [{"role": "user", "content": prompt}]
        
        kwargs = {
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 2000,
            "messages": messages
        }
        
        if system_prompt:
            kwargs["system"] = system_prompt
        
        response = self.claude.messages.create(**kwargs)
        return response.content[0].text
    
    def ask_gemini(self, prompt):
        """Use Gemini for literature review and biological interpretation"""
        response = self.gemini.generate_content(prompt)
        return response.text
    
    def analyze_ruminococcaceae(self, task_type, query):
        """
        Route Ruminococcaceae analysis tasks to appropriate AI
        
        Args:
            task_type: 'bioinformatics', 'literature', or 'analysis'
            query: The question or task to perform
        """
        print(f"\n{'='*60}")
        print(f"Task Type: {task_type.upper()}")
        print(f"{'='*60}\n")
        
        if task_type == 'bioinformatics':
            print("🔬 Using Claude for bioinformatics pipeline...\n")
            system = "You are an expert bioinformatician specializing in microbiome analysis and metagenomics."
            return self.ask_claude(query, system_prompt=system)
        
        elif task_type == 'literature':
            print("📚 Using Gemini for literature review...\n")
            enhanced_query = f"""As a microbiome research expert, provide a critical biological 
            interpretation with recent literature context: {query}
            
            Focus on Ruminococcaceae family and gut microbiome ecology."""
            return self.ask_gemini(enhanced_query)
        
        elif task_type == 'analysis':
            print("📊 Using Claude for statistical analysis...\n")
            system = "You are a data scientist specializing in microbiome statistics and analysis."
            return self.ask_claude(query, system_prompt=system)
        
        else:
            return "Error: task_type must be 'bioinformatics', 'literature', or 'analysis'"


def main():
    """Test the multi-AI agent"""
    agent = MultiAIAgent()
    
    print("\n" + "="*60)
    print("MULTI-AI AGENT TEST")
    print("="*60)
    
    # Test 1: Bioinformatics question (Claude)
    print("\n[TEST 1: Bioinformatics Pipeline]")
    response1 = agent.analyze_ruminococcaceae(
        'bioinformatics',
        'What bioinformatics pipeline steps should I use to analyze Ruminococcaceae 16S amplicon data?'
    )
    print(response1[:400] + "...\n")
    
    # Test 2: Literature review (Gemini)
    print("\n[TEST 2: Literature Review]")
    response2 = agent.analyze_ruminococcaceae(
        'literature',
        'What is the ecological role of Ruminococcaceae in the human gut microbiome?'
    )
    print(response2[:400] + "...\n")
    
    # Test 3: Analysis question (Claude)
    print("\n[TEST 3: Statistical Analysis]")
    response3 = agent.analyze_ruminococcaceae(
        'analysis',
        'What statistical tests should I use to compare Ruminococcaceae abundance between two groups?'
    )
    print(response3[:400] + "...\n")
    
    print("\n" + "="*60)
    print("✅ SUCCESS! Both AI models working perfectly!")
    print("="*60)
    print("\n💡 Next steps:")
    print("  1. Commit this working agent to GitHub")
    print("  2. Create custom analysis scripts for your Ruminococcaceae data")
    print("  3. (Optional) Add OpenAI API key later if needed")


if __name__ == "__main__":
    main()
