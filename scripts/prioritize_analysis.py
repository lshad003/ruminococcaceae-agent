#!/usr/bin/env python3
from ruminococcaceae_analysis import RuminococcaceaeAnalyzer

analyzer = RuminococcaceaeAnalyzer()

response = analyzer.agent.analyze_ruminococcaceae(
    'analysis',
    """I have 284 high-quality herptile Ruminococcaceae MAGs.
    
    I want to publish this work, but I need to be strategic about time/resources.
    
    What is the MINIMUM analysis pipeline that would:
    1. Still be publishable in a good journal
    2. Show what's unique about herptile Ruminococcaceae
    3. Can be completed in 2-3 months
    
    Prioritize the analyses from the full plan. What can I skip? What's essential?
    """
)

print(response)
