#!/usr/bin/env python3
"""
Tests for SpiritWeaver Platform

Validates the Four Directions Compass AI functionality and ensures
proper ceremonial protocols and community sovereignty features.
"""

import sys
from spiritweaver_platform import (
    SpiritWeaverPlatform, DirectionMode, CeremonialContext,
    EastSpiritualAgent, SouthCommunityAgent, WestTechnicalAgent, NorthReflectionAgent
)


def test_platform_initialization():
    """Test that SpiritWeaver platform initializes correctly."""
    platform = SpiritWeaverPlatform()
    
    assert platform.name == "SpiritWeaver: Four Directions Compass AI"
    assert len(platform.agents) == 4
    assert DirectionMode.EAST in platform.agents
    assert DirectionMode.SOUTH in platform.agents
    assert DirectionMode.WEST in platform.agents
    assert DirectionMode.NORTH in platform.agents
    assert platform.session_active == False
    
    print("✅ Platform initialization test passed")


def test_directional_agents_initialization():
    """Test that all four directional agents initialize correctly."""
    east = EastSpiritualAgent()
    south = SouthCommunityAgent()
    west = WestTechnicalAgent()
    north = NorthReflectionAgent()
    
    assert east.name == "Dawn Keeper"
    assert east.direction == DirectionMode.EAST
    assert len(east.sacred_questions) > 0
    
    assert south.name == "Community Weaver"
    assert south.direction == DirectionMode.SOUTH
    assert len(south.learning_modalities) > 0
    
    assert west.name == "Builder of Bridges"
    assert west.direction == DirectionMode.WEST
    assert len(west.technical_capabilities) > 0
    
    assert north.name == "Wisdom Keeper"
    assert north.direction == DirectionMode.NORTH
    assert len(north.reflection_frameworks) > 0
    
    print("✅ Directional agents initialization test passed")


def test_session_initiation():
    """Test that sessions can be initiated properly."""
    platform = SpiritWeaverPlatform()
    
    result = platform.initiate_session(
        intention="Testing the sacred technology platform",
        starting_direction=DirectionMode.EAST
    )
    
    assert result["platform"] == "SpiritWeaver: Four Directions Compass AI"
    assert result["session_status"] == "initiated"
    assert result["starting_direction"] == DirectionMode.EAST.value
    assert "ceremonial_opening" in result
    assert "agent_greeting" in result
    assert platform.session_active == True
    assert platform.current_direction == DirectionMode.EAST
    
    print("✅ Session initiation test passed")


def test_direction_switching():
    """Test that direction switching works correctly."""
    platform = SpiritWeaverPlatform()
    
    # Initiate session
    platform.initiate_session("Testing direction switching", DirectionMode.EAST)
    
    # Switch to South
    transition = platform.switch_direction(
        DirectionMode.SOUTH,
        "Moving from vision to community engagement"
    )
    
    assert "transition" in transition
    assert DirectionMode.SOUTH.value in transition["transition"]
    assert transition["new_agent"] == "Community Weaver"
    assert platform.current_direction == DirectionMode.SOUTH
    
    # Switch to West
    transition = platform.switch_direction(DirectionMode.WEST, "Moving to technical building")
    assert platform.current_direction == DirectionMode.WEST
    
    # Switch to North
    transition = platform.switch_direction(DirectionMode.NORTH, "Moving to reflection")
    assert platform.current_direction == DirectionMode.NORTH
    
    print("✅ Direction switching test passed")


def test_east_agent_processing():
    """Test East direction agent inquiry processing."""
    east = EastSpiritualAgent()
    
    context = CeremonialContext(
        intention="Testing spiritual guidance",
        direction_focus=DirectionMode.EAST,
        community_present=False,
        elder_consultation=False,
        sacred_protocols_active=True,
        timestamp="2024-10-03T12:00:00"
    )
    
    result = east.process_inquiry("What is our purpose in creating this technology?", context)
    
    assert result["direction"] == "East - Spiritual/Visioning"
    assert result["agent"] == "Dawn Keeper"
    assert "spiritual_guidance" in result
    assert "intention_alignment" in result
    assert "sacred_questions" in result
    assert "ceremonial_practice" in result
    
    print("✅ East agent processing test passed")


def test_south_agent_processing():
    """Test South direction agent inquiry processing."""
    south = SouthCommunityAgent()
    
    context = CeremonialContext(
        intention="Testing community guidance",
        direction_focus=DirectionMode.SOUTH,
        community_present=True,
        elder_consultation=True,
        sacred_protocols_active=True,
        timestamp="2024-10-03T12:00:00"
    )
    
    result = south.process_inquiry("How can we connect learners with elders?", context)
    
    assert result["direction"] == "South - Community/Relationships"
    assert result["agent"] == "Community Weaver"
    assert "community_guidance" in result
    assert "learning_opportunities" in result
    assert "relationship_building" in result
    assert "mentorship_connections" in result
    
    print("✅ South agent processing test passed")


def test_west_agent_processing():
    """Test West direction agent inquiry processing."""
    west = WestTechnicalAgent()
    
    context = CeremonialContext(
        intention="Testing technical guidance",
        direction_focus=DirectionMode.WEST,
        community_present=False,
        elder_consultation=False,
        sacred_protocols_active=True,
        timestamp="2024-10-03T12:00:00"
    )
    
    result = west.process_inquiry("What architecture supports offline learning?", context)
    
    assert result["direction"] == "West - Technical/Building"
    assert result["agent"] == "Builder of Bridges"
    assert "technical_guidance" in result
    assert "architecture_recommendations" in result
    assert "implementation_steps" in result
    assert "cultural_technical_integration" in result
    
    # Check specific technical recommendations
    arch = result["architecture_recommendations"]
    assert "primary_pattern" in arch
    assert "data_sovereignty" in arch
    assert "offline_capability" in arch
    
    print("✅ West agent processing test passed")


def test_north_agent_processing():
    """Test North direction agent inquiry processing."""
    north = NorthReflectionAgent()
    
    context = CeremonialContext(
        intention="Testing reflection guidance",
        direction_focus=DirectionMode.NORTH,
        community_present=True,
        elder_consultation=True,
        sacred_protocols_active=True,
        timestamp="2024-10-03T12:00:00"
    )
    
    result = north.process_inquiry("What have we learned from this journey?", context)
    
    assert result["direction"] == "North - Reflection/Integration"
    assert result["agent"] == "Wisdom Keeper"
    assert "wisdom_synthesis" in result
    assert "integration_guidance" in result
    assert "evaluation_framework" in result
    assert "ceremonial_closure" in result
    
    # Check synthesis contains all directions
    synthesis = result["wisdom_synthesis"]
    assert "east_vision" in synthesis
    assert "south_community" in synthesis
    assert "west_technical" in synthesis
    
    print("✅ North agent processing test passed")


def test_comprehensive_guidance():
    """Test comprehensive guidance from all four directions."""
    platform = SpiritWeaverPlatform()
    
    result = platform.get_comprehensive_guidance("Building Indigenous language learning platform")
    
    assert result["topic"] == "Building Indigenous language learning platform"
    assert result["platform"] == "SpiritWeaver: Four Directions Compass AI"
    assert "four_directions_wisdom" in result
    assert "integrated_wisdom" in result
    
    # Verify all four directions provided guidance
    wisdom = result["four_directions_wisdom"]
    assert DirectionMode.EAST.value in wisdom
    assert DirectionMode.SOUTH.value in wisdom
    assert DirectionMode.WEST.value in wisdom
    assert DirectionMode.NORTH.value in wisdom
    
    # Check integrated wisdom
    integrated = result["integrated_wisdom"]
    assert "holistic_understanding" in integrated
    assert "east_contribution" in integrated
    assert "south_contribution" in integrated
    assert "west_contribution" in integrated
    assert "north_contribution" in integrated
    assert "center_integration" in integrated
    
    print("✅ Comprehensive guidance test passed")


def test_session_history_tracking():
    """Test that session history is properly tracked."""
    platform = SpiritWeaverPlatform()
    
    # Initiate session
    platform.initiate_session("Testing history tracking", DirectionMode.EAST)
    
    # Process some inquiries
    platform.process_with_current_direction("What is our vision?")
    platform.switch_direction(DirectionMode.SOUTH, "Moving to community")
    platform.process_with_current_direction("How do we build relationships?")
    
    # Check history
    assert len(platform.session_history) > 0
    assert all("direction" in entry for entry in platform.session_history)
    assert all("inquiry" in entry for entry in platform.session_history)
    
    print("✅ Session history tracking test passed")


def test_session_closure():
    """Test that sessions can be properly closed."""
    platform = SpiritWeaverPlatform()
    
    # Initiate and use session
    platform.initiate_session("Testing closure", DirectionMode.EAST)
    platform.process_with_current_direction("Test inquiry")
    
    # Close session
    closure = platform.close_session()
    
    assert closure["session_status"] == "closing"
    assert "session_summary" in closure
    assert "ceremonial_closing" in closure
    assert "final_guidance" in closure
    assert platform.session_active == False
    assert platform.current_direction is None
    
    # Check ceremonial closing includes all directions
    closing_text = " ".join(closure["ceremonial_closing"])
    assert "East" in closing_text
    assert "South" in closing_text
    assert "West" in closing_text
    assert "North" in closing_text
    
    print("✅ Session closure test passed")


def test_cultural_protocol_features():
    """Test that cultural protocol features are present."""
    platform = SpiritWeaverPlatform()
    
    # Test that East agent has sacred questions
    east = platform.agents[DirectionMode.EAST]
    assert hasattr(east, 'sacred_questions')
    assert len(east.sacred_questions) > 0
    
    # Test that South agent has learning modalities
    south = platform.agents[DirectionMode.SOUTH]
    assert hasattr(south, 'learning_modalities')
    assert 'elder_connection' in south.learning_modalities
    
    # Test that West agent has cultural-technical integration
    west = platform.agents[DirectionMode.WEST]
    assert hasattr(west, 'technical_capabilities')
    
    # Test that North agent has evaluation frameworks
    north = platform.agents[DirectionMode.NORTH]
    assert hasattr(north, 'reflection_frameworks')
    assert 'cultural_appropriateness' in north.reflection_frameworks
    
    print("✅ Cultural protocol features test passed")


def test_learning_technology_references():
    """Test that learning technology features are referenced."""
    south = SouthCommunityAgent()
    
    # Check learning modalities exist
    assert 'storytelling' in south.learning_modalities
    assert 'ceremony' in south.learning_modalities
    assert 'language_practice' in south.learning_modalities
    assert 'elder_connection' in south.learning_modalities
    assert 'place_based' in south.learning_modalities
    
    # Check descriptions are meaningful
    for modality, description in south.learning_modalities.items():
        assert len(description) > 10
        assert isinstance(description, str)
    
    print("✅ Learning technology references test passed")


def test_technical_architecture_features():
    """Test that technical architecture features are present."""
    west = WestTechnicalAgent()
    
    # Check technical capabilities
    assert 'edge_computing' in west.technical_capabilities
    assert 'spiral_visualization' in west.technical_capabilities
    assert 'pronunciation_ai' in west.technical_capabilities
    assert 'multi_agent' in west.technical_capabilities
    
    # Test architecture recommendations
    context = CeremonialContext(
        intention="Testing technical features",
        direction_focus=DirectionMode.WEST,
        community_present=False,
        elder_consultation=False,
        sacred_protocols_active=True,
        timestamp="2024-10-03T12:00:00"
    )
    
    result = west.process_inquiry("offline edge computing visualization", context)
    arch = result["architecture_recommendations"]
    
    assert "offline_capability" in arch
    assert "data_sovereignty" in arch
    
    print("✅ Technical architecture features test passed")


def test_edge_cases():
    """Test edge cases and error handling."""
    platform = SpiritWeaverPlatform()
    
    # Test processing without active session
    result = platform.process_with_current_direction("test")
    assert "error" in result
    
    # Test switching direction without active session
    result = platform.switch_direction(DirectionMode.SOUTH, "test")
    assert "error" in result
    
    # Test closing non-existent session
    result = platform.close_session()
    assert "message" in result
    
    # Test initiation with different starting directions
    for direction in DirectionMode:
        platform = SpiritWeaverPlatform()
        result = platform.initiate_session(f"Testing {direction.value}", direction)
        assert result["session_status"] == "initiated"
        assert result["starting_direction"] == direction.value
    
    print("✅ Edge cases test passed")


def run_all_tests():
    """Run all tests and report results."""
    tests = [
        test_platform_initialization,
        test_directional_agents_initialization,
        test_session_initiation,
        test_direction_switching,
        test_east_agent_processing,
        test_south_agent_processing,
        test_west_agent_processing,
        test_north_agent_processing,
        test_comprehensive_guidance,
        test_session_history_tracking,
        test_session_closure,
        test_cultural_protocol_features,
        test_learning_technology_references,
        test_technical_architecture_features,
        test_edge_cases
    ]
    
    print("🧪 Running SpiritWeaver Platform Tests...\n")
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"❌ {test.__name__} failed: {e}")
            failed += 1
    
    print(f"\n📊 Test Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed! SpiritWeaver Platform is working beautifully.")
        print("🌟 Four Directions wisdom flows through the sacred technology.")
        return True
    else:
        print("⚠️  Some tests failed. Please review the implementation.")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
