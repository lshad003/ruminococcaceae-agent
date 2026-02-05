#!/usr/bin/env python3
"""
Custom analysis workflows for Ruminococcaceae project
"""

import os
import sys
from multi_ai_agent import MultiAIAgent

class RuminococcaceaeAnalyzer:
    """Specialized analyzer for Ruminococcaceae research"""
    
    def __init__(self):
        self.agent = MultiAIAgent()
        print("\n🦠 Ruminococcaceae Analysis System Ready")
    
    def design_pipeline(self, data_type, sample_info):
        """Design a complete bioinformatics pipeline"""
        query = f"""
        I have {data_type} data for Ruminococcaceae analysis.
        Sample information: {sample_info}
        
        Please provide:
        1. Complete step-by-step pipeline with tool names and parameters
        2. Quality control checkpoints
        3. Expected outputs at each stage
        4. Ruminococcaceae-specific considerations
        """
        return self.agent.analyze_ruminococcaceae('bioinformatics', query)
    
    def literature_review(self, topic):
        """Get critical biological interpretation from literature"""
        query = f"""
        Provide a critical review of: {topic}
        
        Include:
        1. Current understanding and recent findings
        2. Controversies or gaps in knowledge
        3. Methodological considerations
        4. Implications for Ruminococcaceae research
        """
        return self.agent.analyze_ruminococcaceae('literature', query)
    
    def statistical_design(self, experiment_description):
        """Design statistical analysis approach"""
        query = f"""
        Experimental design: {experiment_description}
        
        Recommend:
        1. Appropriate statistical tests
        2. Sample size considerations
        3. Multiple testing corrections
        4. Visualization strategies
        5. Python/R code examples if applicable
        """
        return self.agent.analyze_ruminococcaceae('analysis', query)
    
    def compare_to_lachnospiraceae(self, analysis_aspect):
        """Compare Ruminococcaceae to your existing Lachnospiraceae work"""
        query = f"""
        I've previously analyzed Lachnospiraceae family. 
        Now working on Ruminococcaceae.
        
        Compare and contrast regarding: {analysis_aspect}
        
        Provide:
        1. Key similarities in analysis approach
        2. Important differences to consider
        3. Family-specific considerations
        4. How results might be interpreted differently
        """
        return self.agent.analyze_ruminococcaceae('bioinformatics', query)


def interactive_mode():
    """Interactive analysis session"""
    analyzer = RuminococcaceaeAnalyzer()
    
    print("\n" + "="*60)
    print("RUMINOCOCCACEAE ANALYSIS ASSISTANT")
    print("="*60)
    print("\nAvailable commands:")
    print("  1 - Design bioinformatics pipeline")
    print("  2 - Literature review")
    print("  3 - Statistical analysis design")
    print("  4 - Compare to Lachnospiraceae")
    print("  q - Quit")
    print("="*60)
    
    while True:
        choice = input("\nWhat would you like to do? (1-4 or q): ").strip()
        
        if choice == 'q':
            print("\n👋 Goodbye!")
            break
            
        elif choice == '1':
            data_type = input("What type of data? (e.g., '16S amplicon', 'metagenome'): ")
            sample_info = input("Sample information: ")
            print("\n🔬 Designing pipeline...\n")
            result = analyzer.design_pipeline(data_type, sample_info)
            print(result)
            
        elif choice == '2':
            topic = input("Literature review topic: ")
            print("\n📚 Reviewing literature...\n")
            result = analyzer.literature_review(topic)
            print(result)
            
        elif choice == '3':
            experiment = input("Describe your experiment: ")
            print("\n📊 Designing statistical approach...\n")
            result = analyzer.statistical_design(experiment)
            print(result)
            
        elif choice == '4':
            aspect = input("What aspect to compare?: ")
            print("\n🔍 Comparing families...\n")
            result = analyzer.compare_to_lachnospiraceae(aspect)
            print(result)
            
        else:
            print("Invalid choice. Please try again.")
        
        # Ask if user wants to save the output
        save = input("\n💾 Save this output to file? (y/n): ").strip().lower()
        if save == 'y':
            filename = input("Filename (will be saved in results/): ")
            os.makedirs('results', exist_ok=True)
            with open(f'results/{filename}', 'w') as f:
                f.write(result)
            print(f"✓ Saved to results/{filename}")


def example_workflow():
    """Example automated workflow"""
    analyzer = RuminococcaceaeAnalyzer()
    
    print("\n" + "="*60)
    print("EXAMPLE WORKFLOW: Complete Ruminococcaceae Analysis")
    print("="*60)
    
    # Step 1: Pipeline design
    print("\n[STEP 1: Pipeline Design]")
    pipeline = analyzer.design_pipeline(
        "16S V4 amplicon sequencing",
        "50 gut microbiome samples from dietary intervention study"
    )
    print(pipeline[:500] + "...\n")
    
    # Step 2: Literature context
    print("\n[STEP 2: Literature Context]")
    lit_review = analyzer.literature_review(
        "Role of Ruminococcaceae in dietary fiber metabolism"
    )
    print(lit_review[:500] + "...\n")
    
    # Step 3: Statistical approach
    print("\n[STEP 3: Statistical Design]")
    stats = analyzer.statistical_design(
        "Compare Ruminococcaceae abundance between high-fiber and low-fiber diet groups (n=25 each)"
    )
    print(stats[:500] + "...\n")
    
    print("\n✅ Example workflow completed!")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "interactive":
        interactive_mode()
    else:
        example_workflow()
        print("\n💡 To use interactive mode, run:")
        print("   python scripts/ruminococcaceae_analysis.py interactive")
