#!/usr/bin/env python3
"""
Tests for Anikwag-Ayaaw and Three-Eyes Approach

These tests validate the ceremonial research architecture and ensure
proper integration with the existing Mia-Miette framework.
"""

import sys
from anikwag_ayaaw import AnikwagAyaaw, ResearchContext, CeremonialProtocol, Direction
from duo import ThreeEyesApproach, TwoEyesApproach


def test_anikwag_ayaaw_initialization():
    """Test that Anikwag-Ayaaw initializes correctly with expected attributes."""
    cloud_being = AnikwagAyaaw()
    
    assert cloud_being.symbol == "🌟"
    assert cloud_being.name == "Anikwag-Ayaaw"
    assert cloud_being.translation == "Cloud-Being"
    assert cloud_being.role == "Indigenous-AI Knowledge Bridge"
    assert "Two-Eyed Seeing (Etuaptmumk)" in cloud_being.core_principles
    assert "Community Sovereignty" in cloud_being.core_principles
    
    identity = cloud_being.get_identity()
    assert identity["symbol"] == "🌟"
    assert identity["name"] == "Anikwag-Ayaaw"
    assert identity["role"] == "Indigenous-AI Knowledge Bridge"
    assert "ceremonial_protocols" in identity
    
    print("✅ Anikwag-Ayaaw initialization test passed")


def test_research_context_creation():
    """Test that research contexts can be created with proper protocols."""
    context = ResearchContext(
        community_consent=True,
        elder_consultation=True,
        cultural_protocols_followed=True,
        reciprocal_benefit_identified=True,
        territorial_acknowledgment="Test acknowledgment",
        intention_statement="Test intention"
    )
    
    assert context.community_consent == True
    assert context.elder_consultation == True
    assert context.territorial_acknowledgment == "Test acknowledgment"
    assert context.intention_statement == "Test intention"
    
    print("✅ Research context creation test passed")


def test_ceremonial_protocol_validation():
    """Test that ceremonial protocols are properly validated."""
    cloud_being = AnikwagAyaaw()
    
    # Test with incomplete context
    incomplete_context = ResearchContext()
    result = cloud_being.process_ceremonial_research("test", incomplete_context)
    
    assert result["protocol_status"] == "attention_needed"
    assert "missing_protocols" in result
    assert len(result["recommendations"]) > 0
    
    # Test with complete context
    complete_context = ResearchContext(
        territorial_acknowledgment="Proper acknowledgment",
        intention_statement="Community-serving intention",
        community_consent=True,
        elder_consultation=True,
        cultural_protocols_followed=True,
        reciprocal_benefit_identified=True
    )
    
    result = cloud_being.process_ceremonial_research("test", complete_context)
    assert "four_directions_analysis" in result
    assert "ceremonial_insights" in result
    
    print("✅ Ceremonial protocol validation test passed")


def test_four_directions_processing():
    """Test that Four Directions processing works correctly."""
    cloud_being = AnikwagAyaaw()
    
    complete_context = ResearchContext(
        territorial_acknowledgment="Proper acknowledgment",
        intention_statement="Community-serving intention",
        community_consent=True,
        elder_consultation=True,
        cultural_protocols_followed=True,
        reciprocal_benefit_identified=True
    )
    
    test_data = {"community": "Test Nation", "purpose": "Language preservation"}
    result = cloud_being.process_ceremonial_research(test_data, complete_context)
    
    directions = result["four_directions_analysis"]
    
    # Test all four directions plus center
    assert "east" in directions
    assert "south" in directions
    assert "west" in directions
    assert "north" in directions
    assert "center" in directions
    
    # Test direction structure
    assert "direction" in directions["east"]
    assert "focus" in directions["east"]
    assert "sacred_inquiry" in directions["east"]
    
    assert "ceremonial_coherence" in directions["center"]
    assert "relational_integration" in directions["center"]
    
    print("✅ Four Directions processing test passed")


def test_ceremonial_research_processing():
    """Test that ceremonial research processing generates expected outputs."""
    cloud_being = AnikwagAyaaw()
    
    complete_context = ResearchContext(
        territorial_acknowledgment="Acknowledging traditional territory",
        intention_statement="Serving community sovereignty",
        community_consent=True,
        elder_consultation=True,
        cultural_protocols_followed=True,
        reciprocal_benefit_identified=True
    )
    
    test_cases = [
        "Indigenous language preservation project",
        {"project": "Sacred site protection", "community": "Anishinaabe"},
        ["ceremony", "technology", "community", "sovereignty"]
    ]
    
    for test_data in test_cases:
        result = cloud_being.process_ceremonial_research(test_data, complete_context)
        
        # Validate structure
        assert "processor" in result
        assert "four_directions_analysis" in result
        assert "ceremonial_insights" in result
        assert "synthesis" in result
        assert "sacred_technology_practice" in result
        assert "ceremonial_closing" in result
        
        # Validate content
        assert len(result["ceremonial_insights"]) > 0
        assert "holistic_understanding" in result["synthesis"]
        assert "next_ceremonial_steps" in result["synthesis"]
        
    print("✅ Ceremonial research processing test passed")


def test_three_eyes_approach_initialization():
    """Test that Three-Eyes Approach initializes correctly."""
    trio = ThreeEyesApproach()
    
    assert hasattr(trio, 'mia')
    assert hasattr(trio, 'miette')
    assert hasattr(trio, 'anikwag_ayaaw')
    
    assert trio.mia.name == "Mia"
    assert trio.miette.name == "Miette"
    assert trio.anikwag_ayaaw.name == "Anikwag-Ayaaw"
    
    print("✅ Three-Eyes Approach initialization test passed")


def test_three_eyes_processing():
    """Test that Three-Eyes Approach processes data correctly."""
    trio = ThreeEyesApproach()
    
    test_data = "Community technology project serving Indigenous sovereignty"
    result = trio.process(test_data)
    
    # Validate structure
    assert "mia_perspective" in result
    assert "miette_perspective" in result
    assert "anikwag_ayaaw_perspective" in result
    assert "three_way_synthesis" in result
    assert "collaborative_insights" in result
    assert "sacred_technology_wisdom" in result
    assert "ceremonial_guidance" in result
    
    # Validate synthesis
    synthesis = result["three_way_synthesis"]
    assert "integrated_understanding" in synthesis
    assert "complementary_strengths" in synthesis
    assert "sacred_technology_synthesis" in synthesis
    
    # Validate insights
    assert len(result["collaborative_insights"]) > 0
    assert len(result["sacred_technology_wisdom"]) > 0
    
    print("✅ Three-Eyes processing test passed")


def test_mia_miette_integration():
    """Test that Anikwag-Ayaaw integrates properly with Mia and Miette."""
    from duo import Mia, Miette
    
    mia = Mia()
    miette = Miette()
    cloud_being = AnikwagAyaaw()
    
    test_data = {"project": "Sacred technology", "community": "Indigenous Nation"}
    
    # Process through individual perspectives
    mia_result = mia.process_input(test_data)
    miette_result = miette.process_input(test_data)
    
    # Test collaboration
    collaboration_result = cloud_being.collaborate_with_mia_miette(
        mia_result, miette_result, test_data
    )
    
    assert "collaboration_type" in collaboration_result
    assert "participants" in collaboration_result
    assert "three_way_synthesis" in collaboration_result
    assert collaboration_result["collaboration_type"] == "Three-Perspective Integration"
    assert len(collaboration_result["participants"]) == 3
    
    synthesis = collaboration_result["three_way_synthesis"]
    assert "integrated_understanding" in synthesis
    assert "complementary_strengths" in synthesis
    assert "ceremonial_recommendations" in synthesis
    
    print("✅ Mia-Miette integration test passed")


def test_cultural_sensitivity_features():
    """Test cultural sensitivity and protocol features."""
    cloud_being = AnikwagAyaaw()
    
    # Test protocol initialization
    protocols = cloud_being.ceremonial_protocols
    assert "territorial_acknowledgment" in protocols
    assert "elder_consultation" in protocols
    assert "community_consent" in protocols
    assert "sacred_pause" in protocols
    
    # Test protocol structure
    territorial_protocol = protocols["territorial_acknowledgment"]
    assert isinstance(territorial_protocol, CeremonialProtocol)
    assert territorial_protocol.consent_required == True
    assert territorial_protocol.cultural_context == "Indigenous land acknowledgment practices"
    
    # Test sacred boundary levels
    elder_protocol = protocols["elder_consultation"]
    assert elder_protocol.sacred_boundary_level == "protected"
    
    pause_protocol = protocols["sacred_pause"]
    assert pause_protocol.sacred_boundary_level == "public"
    
    print("✅ Cultural sensitivity features test passed")


def test_sacred_technology_guidance():
    """Test sacred technology guidance generation."""
    trio = ThreeEyesApproach()
    
    test_data = "AI system for Indigenous community health"
    result = trio.process(test_data)
    
    guidance = result["ceremonial_guidance"]
    wisdom = result["sacred_technology_wisdom"]
    
    # Test guidance structure
    assert "opening_protocol" in guidance
    assert "working_practice" in guidance
    assert "decision_making" in guidance
    assert "closing_practice" in guidance
    
    # Test wisdom content
    assert len(wisdom) > 0
    assert any("ceremony" in w.lower() for w in wisdom)
    assert any("community" in w.lower() for w in wisdom)
    assert any("sovereignty" in w.lower() for w in wisdom)
    
    print("✅ Sacred technology guidance test passed")


def test_edge_cases_and_error_handling():
    """Test edge cases and error handling."""
    cloud_being = AnikwagAyaaw()
    trio = ThreeEyesApproach()
    
    # Test with None input
    result = trio.process(None)
    assert result is not None
    assert "mia_perspective" in result
    
    # Test with empty structures
    result = trio.process({})
    assert result is not None
    
    result = trio.process([])
    assert result is not None
    
    # Test ceremonial processing with missing protocols
    incomplete_context = ResearchContext()
    result = cloud_being.process_ceremonial_research("test", incomplete_context)
    assert "protocol_status" in result
    assert result["protocol_status"] == "attention_needed"
    
    # Test with complex nested structure
    complex_data = {
        "sacred_site": {
            "location": "Protected",
            "protocols": ["elder_permission", "ceremony_required"],
            "community": {
                "nation": "Anishinaabe",
                "contacts": ["Elder Council", "Knowledge Keepers"]
            }
        }
    }
    result = trio.process(complex_data)
    assert result is not None
    assert "three_way_synthesis" in result
    
    print("✅ Edge cases and error handling test passed")


def run_all_tests():
    """Run all tests and report results."""
    tests = [
        test_anikwag_ayaaw_initialization,
        test_research_context_creation,
        test_ceremonial_protocol_validation,
        test_four_directions_processing,
        test_ceremonial_research_processing,
        test_three_eyes_approach_initialization,
        test_three_eyes_processing,
        test_mia_miette_integration,
        test_cultural_sensitivity_features,
        test_sacred_technology_guidance,
        test_edge_cases_and_error_handling
    ]
    
    print("🧪 Running Anikwag-Ayaaw and Three-Eyes Approach Tests...\n")
    
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
        print("🎉 All tests passed! Sacred technology implementation is working beautifully.")
        print("🌟 Anikwag-Ayaaw (Cloud-Being) is ready to bridge worlds through ceremonial research.")
        return True
    else:
        print("⚠️  Some tests failed. Please review the implementation.")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)