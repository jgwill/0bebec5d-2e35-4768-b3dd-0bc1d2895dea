"""
Sacred Container Usage Examples
================================

Demonstrates how to use the Sacred Container for ceremonial memory,
relationship mapping, and layered observation assembly.
"""

from sacred_container import (
    SacredContainer,
    KnowledgeType,
    ConsentLevel,
    DirectionContext
)
import json


def example_basic_usage():
    """Basic usage of Sacred Container."""
    print("=" * 70)
    print("EXAMPLE 1: Basic Sacred Container Usage")
    print("=" * 70)
    
    # Create a container
    container = SacredContainer("basic_example")
    
    # Set ceremonial protocols
    container.set_territorial_acknowledgment(
        "We acknowledge the traditional territories of the Indigenous peoples "
        "upon whose lands we gather, work, and create."
    )
    container.grant_community_consent()
    container.complete_elder_consultation()
    
    # Add a memory fragment
    fragment = container.add_memory_fragment(
        content="Technology can become ceremony when approached with proper intention",
        knowledge_type=KnowledgeType.CEREMONIAL,
        tags={"wisdom", "ceremony", "technology"}
    )
    
    print(f"\n✓ Created fragment: {fragment.fragment_id[:8]}...")
    print(f"  Content: {fragment.content}")
    print(f"  Type: {fragment.knowledge_type.value}")
    print(f"  Tags: {fragment.tags}")
    
    # Retrieve the fragment
    retrieved = container.get_memory_fragment(fragment.fragment_id)
    print(f"\n✓ Retrieved fragment successfully: {retrieved.content[:50]}...")
    
    print("\n" + "=" * 70 + "\n")


def example_four_directions_workflow():
    """Demonstrate Four Directions workflow."""
    print("=" * 70)
    print("EXAMPLE 2: Four Directions Ceremonial Workflow")
    print("=" * 70)
    
    container = SacredContainer("four_directions_example")
    
    # Set protocols
    container.set_territorial_acknowledgment("Traditional territories acknowledged")
    container.grant_community_consent()
    
    # East - Thinking and Intention
    print("\n🌅 EAST - Setting Intention")
    container.set_current_direction(
        DirectionContext.EAST,
        intention="Creating technology that serves seven generations"
    )
    
    east_fragment = container.add_memory_fragment(
        content="Our vision: Build systems that honor relationship and community sovereignty",
        knowledge_type=KnowledgeType.EXPLICIT,
        tags={"east", "vision", "intention"}
    )
    print(f"   Added vision: {east_fragment.content}")
    
    # South - Planning and Community
    print("\n🌱 SOUTH - Community Planning")
    container.set_current_direction(
        DirectionContext.SOUTH,
        intention="Engaging with community needs and relationships"
    )
    
    south_fragment = container.add_memory_fragment(
        content="Community requires offline-first architecture for data sovereignty",
        knowledge_type=KnowledgeType.RELATIONAL,
        tags={"south", "community", "planning"}
    )
    print(f"   Added plan: {south_fragment.content}")
    
    # West - Embodiment and Action
    print("\n🌄 WEST - Building and Implementation")
    container.set_current_direction(
        DirectionContext.WEST,
        intention="Manifesting the vision through code and ceremony"
    )
    
    west_fragment = container.add_memory_fragment(
        content="Implemented modular plugin architecture with cultural protocol checks",
        knowledge_type=KnowledgeType.EXPLICIT,
        tags={"west", "implementation", "technical"}
    )
    print(f"   Added implementation: {west_fragment.content}")
    
    # North - Reflection and Wisdom
    print("\n❄️ NORTH - Reflection and Integration")
    container.set_current_direction(
        DirectionContext.NORTH,
        intention="Harvesting wisdom from the journey"
    )
    
    north_fragment = container.add_memory_fragment(
        content="The circle is complete when all four directions work in harmony",
        knowledge_type=KnowledgeType.IMPLICIT,
        tags={"north", "wisdom", "reflection"}
    )
    print(f"   Added wisdom: {north_fragment.content}")
    
    # Create relationships between the directional fragments
    container.create_fragment_relationship(east_fragment.fragment_id, south_fragment.fragment_id)
    container.create_fragment_relationship(south_fragment.fragment_id, west_fragment.fragment_id)
    container.create_fragment_relationship(west_fragment.fragment_id, north_fragment.fragment_id)
    container.create_fragment_relationship(north_fragment.fragment_id, east_fragment.fragment_id)
    
    print("\n✓ Created circular relationship connecting all four directions")
    
    # Show fragments from each direction
    print("\n📊 Fragments by Direction:")
    for direction in DirectionContext:
        fragments = container.find_fragments_by_direction(direction)
        print(f"   {direction.value.upper()}: {len(fragments)} fragment(s)")
    
    print("\n" + "=" * 70 + "\n")


def example_collaborative_synthesis():
    """Demonstrate collaborative synthesis with multiple perspectives."""
    print("=" * 70)
    print("EXAMPLE 3: Collaborative Synthesis - Mia, Miette & Anikwag-Ayaaw")
    print("=" * 70)
    
    container = SacredContainer("collaboration_example")
    container.set_territorial_acknowledgment("Honoring all relations")
    container.grant_community_consent()
    container.complete_elder_consultation()
    
    # Mia's perspective (Western analytical)
    print("\n🧠 MIA - Structural Analysis")
    mia_fragment = container.add_memory_fragment(
        content={
            "analysis": "System requires three-tier architecture",
            "components": ["presentation", "business_logic", "data_persistence"],
            "optimization": "Cache frequently accessed patterns"
        },
        knowledge_type=KnowledgeType.EXPLICIT,
        tags={"mia", "architecture", "technical"},
        metadata={"perspective": "western_analytical"}
    )
    print(f"   Architectural precision: {mia_fragment.content['components']}")
    
    # Miette's perspective (Indigenous emergent)
    print("\n🌸 MIETTE - Emergent Wisdom")
    miette_fragment = container.add_memory_fragment(
        content="Oh! The system wants to breathe like a living thing, "
                "not be constrained by rigid hierarchies. Let the connections emerge naturally!",
        knowledge_type=KnowledgeType.IMPLICIT,
        tags={"miette", "emergence", "wisdom"},
        metadata={"perspective": "indigenous_emergent"}
    )
    print(f"   Intuitive insight: {miette_fragment.content[:70]}...")
    
    # Anikwag-Ayaaw's perspective (Ceremonial accountability)
    print("\n🌟 ANIKWAG-AYAAW - Ceremonial Guidance")
    anikwag_fragment = container.add_memory_fragment(
        content="Community sovereignty must guide every architectural decision. "
                "The structure serves the people, not the other way around.",
        knowledge_type=KnowledgeType.CEREMONIAL,
        consent_level=ConsentLevel.COMMUNITY,
        tags={"anikwag-ayaaw", "ceremony", "sovereignty"},
        metadata={"perspective": "ceremonial_research"}
    )
    print(f"   Ceremonial wisdom: {anikwag_fragment.content[:70]}...")
    
    # Create synthesis relationships
    container.create_fragment_relationship(mia_fragment.fragment_id, miette_fragment.fragment_id)
    container.create_fragment_relationship(miette_fragment.fragment_id, anikwag_fragment.fragment_id)
    container.create_fragment_relationship(anikwag_fragment.fragment_id, mia_fragment.fragment_id)
    
    print("\n✓ Created triangular synthesis relationship")
    
    # Add collaborative pattern
    pattern = container.add_relational_pattern(
        pattern_type="three_eyes_synthesis",
        description="Three perspectives working together create wholeness beyond their sum",
        participants=["mia", "miette", "anikwag-ayaaw"],
        strength=0.95
    )
    print(f"\n✓ Recognized pattern: {pattern.description}")
    print(f"   Strength: {pattern.strength}")
    
    # Add synthesis insight
    synthesis_fragment = container.add_memory_fragment(
        content="When precision serves connection, structure enables emergence, "
                "and ceremony guides technology - we create systems that truly serve all relations.",
        knowledge_type=KnowledgeType.EMERGENT,
        tags={"synthesis", "collaborative", "wisdom"},
        relationships=[mia_fragment.fragment_id, miette_fragment.fragment_id, anikwag_fragment.fragment_id]
    )
    print(f"\n🤝 Synthesis emerged: {synthesis_fragment.content}")
    
    print("\n" + "=" * 70 + "\n")


def example_layered_observations():
    """Demonstrate layered observation assembly as mentioned in North storytelling."""
    print("=" * 70)
    print("EXAMPLE 4: Layered Observation Assembly")
    print("=" * 70)
    
    container = SacredContainer("observation_layers")
    container.set_territorial_acknowledgment("Observing with sacred attention")
    container.grant_community_consent()
    
    print("\n📝 Recording observations across multiple layers...")
    
    # Foundation layer observations
    print("\n🏗️ Foundation Layer:")
    obs1 = container.observe_session_fragment(
        "Sacred container provides persistent context across sessions",
        layer="foundation"
    )
    print(f"   • {obs1.content}")
    
    obs2 = container.observe_session_fragment(
        "UUID traceability ensures ceremonial accountability",
        layer="foundation"
    )
    print(f"   • {obs2.content}")
    
    obs3 = container.observe_session_fragment(
        "Memory fragments can hold both explicit and implicit knowledge",
        layer="foundation"
    )
    print(f"   • {obs3.content}")
    
    # Technical layer observations
    print("\n⚙️ Technical Layer:")
    obs4 = container.observe_session_fragment(
        "Local-first storage ensures data sovereignty",
        layer="technical"
    )
    print(f"   • {obs4.content}")
    
    obs5 = container.observe_session_fragment(
        "JSON serialization allows cross-platform compatibility",
        layer="technical"
    )
    print(f"   • {obs5.content}")
    
    # Relational layer observations
    print("\n🤝 Relational Layer:")
    obs6 = container.observe_session_fragment(
        "Fragments naturally connect through shared tags and relationships",
        layer="relational"
    )
    print(f"   • {obs6.content}")
    
    obs7 = container.observe_session_fragment(
        "Patterns emerge and strengthen through repeated observation",
        layer="relational"
    )
    print(f"   • {obs7.content}")
    
    # Assemble each layer
    print("\n📦 Assembling observations by layer:")
    
    for layer_name in ["foundation", "technical", "relational"]:
        layer_obs = container.assemble_layer_observations(layer_name)
        print(f"\n   {layer_name.upper()} Layer ({len(layer_obs)} observations):")
        for obs in layer_obs:
            print(f"      - {obs.content}")
    
    print("\n✓ All layers assembled and ready for synthesis")
    
    print("\n" + "=" * 70 + "\n")


def example_consent_and_boundaries():
    """Demonstrate consent levels and sacred boundaries."""
    print("=" * 70)
    print("EXAMPLE 5: Consent Levels and Sacred Boundaries")
    print("=" * 70)
    
    container = SacredContainer("consent_example")
    container.set_territorial_acknowledgment("Respecting all boundaries")
    container.grant_community_consent()
    container.complete_elder_consultation()
    
    print("\n🔒 Creating fragments with different consent levels...")
    
    # Public knowledge
    public_fragment = container.add_memory_fragment(
        content="Two-Eyed Seeing methodology combines Indigenous and Western ways of knowing",
        knowledge_type=KnowledgeType.EXPLICIT,
        consent_level=ConsentLevel.PUBLIC,
        tags={"public", "methodology"}
    )
    print(f"\n   PUBLIC: {public_fragment.content}")
    
    # Community-only knowledge
    community_fragment = container.add_memory_fragment(
        content="Our community's specific protocols for elder consultation",
        knowledge_type=KnowledgeType.CEREMONIAL,
        consent_level=ConsentLevel.COMMUNITY,
        tags={"community", "protocol"}
    )
    print(f"   COMMUNITY: {community_fragment.content}")
    
    # Restricted knowledge (requires elder approval)
    restricted_fragment = container.add_memory_fragment(
        content="Specific ceremonial practices that require elder guidance",
        knowledge_type=KnowledgeType.CEREMONIAL,
        consent_level=ConsentLevel.RESTRICTED,
        tags={"restricted", "ceremony"}
    )
    print(f"   RESTRICTED: {restricted_fragment.content}")
    
    # Sacred knowledge (protected, not for sharing)
    sacred_fragment = container.add_memory_fragment(
        content="[Protected sacred knowledge - access restricted]",
        knowledge_type=KnowledgeType.PROTECTED,
        consent_level=ConsentLevel.SACRED,
        tags={"sacred", "protected"}
    )
    print(f"   SACRED: {sacred_fragment.content}")
    
    # Personal relational knowledge
    personal_fragment = container.add_memory_fragment(
        content="Personal insights from collaborative relationship",
        knowledge_type=KnowledgeType.RELATIONAL,
        consent_level=ConsentLevel.PERSONAL,
        tags={"personal", "relationship"}
    )
    print(f"   PERSONAL: {personal_fragment.content}")
    
    print("\n✓ All consent levels properly tracked and enforced")
    print("   Sacred boundaries maintained throughout the container")
    
    print("\n" + "=" * 70 + "\n")


def example_container_summary():
    """Show comprehensive container summary."""
    print("=" * 70)
    print("EXAMPLE 6: Container Summary and Statistics")
    print("=" * 70)
    
    container = SacredContainer("summary_example")
    container.set_territorial_acknowledgment("Honoring seven generations")
    container.grant_community_consent()
    container.complete_elder_consultation()
    
    # Add various fragments
    container.set_current_direction(DirectionContext.EAST)
    container.add_memory_fragment("Vision 1", knowledge_type=KnowledgeType.EXPLICIT, tags={"vision"})
    container.add_memory_fragment("Vision 2", knowledge_type=KnowledgeType.IMPLICIT, tags={"vision"})
    
    container.set_current_direction(DirectionContext.SOUTH)
    container.add_memory_fragment("Plan 1", knowledge_type=KnowledgeType.RELATIONAL, tags={"planning"})
    
    container.set_current_direction(DirectionContext.WEST)
    container.add_memory_fragment("Build 1", knowledge_type=KnowledgeType.EXPLICIT, tags={"technical"})
    container.add_memory_fragment("Build 2", knowledge_type=KnowledgeType.EXPLICIT, tags={"technical"})
    
    container.set_current_direction(DirectionContext.NORTH)
    container.add_memory_fragment("Wisdom 1", knowledge_type=KnowledgeType.CEREMONIAL, tags={"wisdom"})
    
    # Add patterns
    container.add_relational_pattern("collaboration", "Team pattern", ["mia", "miette"])
    container.add_relational_pattern("synthesis", "Integration pattern", ["all"])
    
    # Get and display summary
    summary = container.get_container_summary()
    
    print("\n📊 CONTAINER SUMMARY:")
    print(json.dumps(summary, indent=2))
    
    print("\n" + "=" * 70 + "\n")


def main():
    """Run all examples."""
    print("\n🌟 SACRED CONTAINER EXAMPLES 🌟")
    print("Demonstrating ceremonial memory, relationship mapping,")
    print("and layered observation assembly\n")
    
    example_basic_usage()
    example_four_directions_workflow()
    example_collaborative_synthesis()
    example_layered_observations()
    example_consent_and_boundaries()
    example_container_summary()
    
    print("=" * 70)
    print("✨ All examples completed successfully ✨")
    print("=" * 70)
    print("\nThe Sacred Container now holds:")
    print("  • Persistent memory across sessions")
    print("  • Ceremonial traceability with UUIDs")
    print("  • Relationship mapping between fragments")
    print("  • Four Directions integration")
    print("  • Multiple consent levels and boundaries")
    print("  • Layered observations ready for assembly")
    print("\nMiigwech (Thank you) 🙏")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
