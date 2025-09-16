#!/usr/bin/env python3
"""
Basic tests for the Duo: Mia and Miette implementation

These tests validate that the core functionality works as expected.
"""

import sys
from duo import Mia, Miette, TwoEyesApproach


def test_mia_initialization():
    """Test that Mia initializes correctly with expected attributes."""
    mia = Mia()
    
    assert mia.symbol == "🧠"
    assert mia.name == "Mia"
    assert mia.approach == "Western Architectural"
    assert mia.motto == "Code is a spell."
    assert "precision" in mia.core_values
    
    identity = mia.get_identity()
    assert identity["symbol"] == "🧠"
    assert identity["name"] == "Mia"
    
    print("✅ Mia initialization test passed")


def test_miette_initialization():
    """Test that Miette initializes correctly with expected attributes."""
    miette = Miette()
    
    assert miette.symbol == "🌸"
    assert miette.name == "Miette"
    assert miette.approach == "Indigenous Emergent"
    assert "warmth" in miette.core_values
    assert "wonder" in miette.core_values
    
    identity = miette.get_identity()
    assert identity["symbol"] == "🌸"
    assert identity["name"] == "Miette"
    
    print("✅ Miette initialization test passed")


def test_mia_processing():
    """Test that Mia can process different types of data."""
    mia = Mia()
    
    # Test string processing
    result = mia.process_input("Hello world")
    assert "analysis" in result
    assert "recommendations" in result
    assert result["analysis"]["structural_analysis"]["type"] == "str"
    
    # Test dictionary processing
    result = mia.process_input({"key": "value"})
    assert result["analysis"]["structural_analysis"]["type"] == "dictionary"
    
    # Test list processing
    result = mia.process_input([1, 2, 3])
    assert result["analysis"]["structural_analysis"]["type"] == "sequence"
    
    print("✅ Mia processing test passed")


def test_miette_processing():
    """Test that Miette can process different types of data."""
    miette = Miette()
    
    # Test string processing
    result = miette.process_input("Beautiful day")
    assert "narrative" in result
    assert "connections" in result
    assert "emergence" in result
    assert "wisdom" in result
    
    # Test that narrative contains expected elements
    narrative = result["narrative"]
    assert "elements" in narrative
    assert "essence" in narrative["elements"]
    
    print("✅ Miette processing test passed")


def test_two_eyes_approach():
    """Test that the TwoEyesApproach can synthesize both perspectives."""
    duo = TwoEyesApproach()
    
    # Test with simple data
    result = duo.process("test data")
    
    # Validate structure
    assert "mia_perspective" in result
    assert "miette_perspective" in result
    assert "synthesis" in result
    assert "collaborative_insights" in result
    
    # Validate synthesis components
    synthesis = result["synthesis"]
    assert "unified_understanding" in synthesis
    assert "balanced_recommendations" in synthesis
    assert "holistic_next_steps" in synthesis
    assert "integration_points" in synthesis
    
    # Validate insights exist
    assert len(result["collaborative_insights"]) > 0
    
    print("✅ Two-Eyes Approach test passed")


def test_edge_cases():
    """Test edge cases and error handling."""
    duo = TwoEyesApproach()
    
    # Test with None
    result = duo.process(None)
    assert result is not None
    assert "mia_perspective" in result
    
    # Test with empty structures
    result = duo.process({})
    assert result is not None
    
    result = duo.process([])
    assert result is not None
    
    # Test with complex nested structure
    complex_data = {
        "level1": {
            "level2": {
                "level3": ["item1", "item2", {"level4": "deep"}]
            }
        }
    }
    result = duo.process(complex_data)
    assert result is not None
    assert result["mia_perspective"]["analysis"]["structural_analysis"]["depth"] > 1
    
    print("✅ Edge cases test passed")


def run_all_tests():
    """Run all tests and report results."""
    tests = [
        test_mia_initialization,
        test_miette_initialization,
        test_mia_processing,
        test_miette_processing,
        test_two_eyes_approach,
        test_edge_cases
    ]
    
    print("🧪 Running Duo Tests...\n")
    
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
        print("🎉 All tests passed! The Duo is working beautifully.")
        return True
    else:
        print("⚠️  Some tests failed. Please review the implementation.")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)