#!/usr/bin/env python3
"""
Simple example of using the Two-Eyes Approach with your own data.

This script demonstrates how to use Mia and Miette to analyze different types of data
from both Western analytical and Indigenous emergent perspectives.
"""

from duo import TwoEyesApproach, Mia, Miette


def simple_example():
    """
    Basic example showing how to process data through both perspectives.
    """
    print("🌟 Simple Two-Eyes Approach Example 🌟\n")
    
    # Initialize the duo
    duo = TwoEyesApproach()
    
    # Your data to analyze
    my_data = {
        "project": "Community Garden App",
        "purpose": "Connecting neighbors through shared growing",
        "features": ["plant tracking", "harvest sharing", "community events"],
        "values": ["sustainability", "community", "growth", "sharing"]
    }
    
    print(f"📊 Analyzing: {my_data}\n")
    
    # Process through both perspectives
    result = duo.process(my_data)
    
    # Show each perspective
    print("🧠 Mia's Architectural Analysis:")
    mia_analysis = result["mia_perspective"]["analysis"]
    print(f"   • Structure Type: {mia_analysis['structural_analysis']['type']}")
    print(f"   • Complexity: {mia_analysis['structural_analysis']['complexity']}")
    print(f"   • Patterns Found: {', '.join(mia_analysis['design_patterns']) or 'None'}")
    print(f"   • Recommendations: {len(result['mia_perspective']['recommendations'])} suggestions")
    
    print("\n🌸 Miette's Emergent Story:")
    miette_result = result["miette_perspective"]
    essence = miette_result["narrative"]["elements"]["essence"]
    themes = ", ".join(miette_result["connections"]["universal_themes"])
    print(f"   • Essence: {essence}")
    print(f"   • Universal Themes: {themes}")
    print(f"   • Energy Flow: {miette_result['connections']['energy_flow']}")
    
    print("\n🤝 Collaborative Insights:")
    for insight in result["collaborative_insights"][:3]:  # Show first 3 insights
        print(f"   • {insight}")
    
    print("\n💫 Synthesis:")
    synthesis = result["synthesis"]
    print(f"   • Integration Point: {synthesis['integration_points'][0]}")
    print(f"   • Next Steps: {len(synthesis['holistic_next_steps'])} suggestions")


def individual_perspectives_example():
    """
    Example showing how to use Mia and Miette individually.
    """
    print("\n" + "="*60)
    print("🔍 Individual Perspectives Example 🔍\n")
    
    # Initialize each perspective separately
    mia = Mia()
    miette = Miette()
    
    # Some code to analyze
    code_snippet = """
def connect_neighbors(garden_data):
    '''Building bridges between people through plants'''
    for plot in garden_data:
        if plot.needs_help():
            notify_nearby_gardeners(plot)
    return community_strength + 1
    """
    
    print(f"🧠 {mia.name} analyzes the code:")
    mia_result = mia.process_input(code_snippet)
    print(f"   Structural complexity: {mia_result['analysis']['structural_analysis']['complexity']}")
    print(f"   Patterns: {', '.join(mia_result['analysis']['design_patterns'])}")
    print(f"   Recommendation: {mia_result['recommendations'][0] if mia_result['recommendations'] else 'Code is well-structured'}")
    
    print(f"\n🌸 {miette.name} senses the story:")
    miette_result = miette.process_input(code_snippet)
    essence = miette_result["narrative"]["elements"]["essence"]
    wisdom = miette_result["wisdom"][0] if miette_result["wisdom"] else "Code carries intention"
    print(f"   Essence: {essence}")
    print(f"   Wisdom: {wisdom}")


if __name__ == "__main__":
    simple_example()
    individual_perspectives_example()
    print("\n✨ Remember: Both ways of seeing are valuable and can strengthen each other! ✨")