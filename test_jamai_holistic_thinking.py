"""
Tests for JamAI Holistic Thinking Integration
"""

import unittest
import json
from jamai_holistic_thinking import (
    JamAIHolisticComposer,
    MusicalDirection,
    InstrumentVoice,
    MusicalFragment,
    MusicalRelationship,
    generate_jamai_spiral
)


class TestJamAIHolisticComposer(unittest.TestCase):
    """Test suite for JamAI Holistic Composer."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.composer = JamAIHolisticComposer()
    
    def test_initialization(self):
        """Test composer initialization."""
        self.assertEqual(self.composer.key, "E minor")
        self.assertIsNone(self.composer.tempo)
        self.assertIsNone(self.composer.time_signature)
        self.assertEqual(len(self.composer.fragments), 0)
        self.assertEqual(len(self.composer.relationships), 0)
    
    def test_set_ceremonial_story(self):
        """Test setting ceremonial story."""
        story = "A story of collaboration and beauty"
        self.composer.set_ceremonial_story(story)
        self.assertEqual(self.composer.ceremonial_story, story)
    
    def test_set_musical_parameters(self):
        """Test setting musical parameters."""
        self.composer.set_musical_parameters(
            key="D major",
            tempo=120,
            time_signature="4/4"
        )
        self.assertEqual(self.composer.key, "D major")
        self.assertEqual(self.composer.tempo, 120)
        self.assertEqual(self.composer.time_signature, "4/4")
    
    def test_compose_directional_thinking(self):
        """Test generation of Four Directions thinking."""
        intention = "Test composition intention"
        self.composer.set_ceremonial_story("Test story")
        
        result = self.composer.compose_directional_thinking(intention)
        
        self.assertIn("composition_intention", result)
        self.assertIn("ceremonial_story", result)
        self.assertIn("musical_parameters", result)
        self.assertIn("four_directions", result)
        self.assertIn("center", result)
        
        # Check all four directions are present
        self.assertIn("EAST", result["four_directions"])
        self.assertIn("SOUTH", result["four_directions"])
        self.assertIn("WEST", result["four_directions"])
        self.assertIn("NORTH", result["four_directions"])
    
    def test_east_direction_structure(self):
        """Test East direction thinking structure."""
        intention = "New beginning composition"
        result = self.composer.compose_directional_thinking(intention)
        east = result["four_directions"]["EAST"]
        
        self.assertEqual(east["direction"], "EAST")
        self.assertEqual(east["element"], "air")
        self.assertEqual(east["color"], "yellow")
        self.assertIn("musical_intention", east)
        self.assertIn("compositional_elements", east)
        self.assertIn("relational_thinking", east)
        self.assertIn("questions_for_contemplation", east)
    
    def test_south_direction_structure(self):
        """Test South direction thinking structure."""
        intention = "Heart-centered composition"
        result = self.composer.compose_directional_thinking(intention)
        south = result["four_directions"]["SOUTH"]
        
        self.assertEqual(south["direction"], "SOUTH")
        self.assertEqual(south["element"], "fire")
        self.assertEqual(south["color"], "red")
        self.assertIn("musical_development", south)
        self.assertIn("compositional_elements", south)
        self.assertIn("relational_thinking", south)
    
    def test_west_direction_structure(self):
        """Test West direction thinking structure."""
        intention = "Transformation composition"
        result = self.composer.compose_directional_thinking(intention)
        west = result["four_directions"]["WEST"]
        
        self.assertEqual(west["direction"], "WEST")
        self.assertEqual(west["element"], "water")
        self.assertEqual(west["color"], "black")
        self.assertIn("musical_transformation", west)
        self.assertIn("compositional_elements", west)
    
    def test_north_direction_structure(self):
        """Test North direction thinking structure."""
        intention = "Wisdom composition"
        result = self.composer.compose_directional_thinking(intention)
        north = result["four_directions"]["NORTH"]
        
        self.assertEqual(north["direction"], "NORTH")
        self.assertEqual(north["element"], "earth")
        self.assertEqual(north["color"], "white")
        self.assertIn("wisdom_transmission", north)
        self.assertIn("compositional_elements", north)
        self.assertIn("seven_generations_reflection", north)
    
    def test_center_integration(self):
        """Test center integration structure."""
        intention = "Integrated composition"
        result = self.composer.compose_directional_thinking(intention)
        center = result["center"]
        
        self.assertEqual(center["position"], "CENTER")
        self.assertIn("integration_principles", center)
        self.assertIn("compositional_wholeness", center)
        self.assertIn("beauty_as_structure", center)
        self.assertIn("ceremonial_integrity", center)
    
    def test_generate_spiral_json(self):
        """Test JSON spiral generation."""
        intention = "Test spiral generation"
        self.composer.set_ceremonial_story("Test ceremonial story")
        
        json_output = self.composer.generate_spiral_json(intention)
        
        # Verify it's valid JSON
        parsed = json.loads(json_output)
        self.assertIn("four_directions", parsed)
        self.assertIn("center", parsed)
    
    def test_add_musical_fragment(self):
        """Test adding musical fragments."""
        content = {"melody": "C-D-E", "duration": "quarter notes"}
        fragment = self.composer.add_musical_fragment(
            content=content,
            direction=MusicalDirection.EAST,
            voice=InstrumentVoice.MIA_FLUTE,
            intention="Opening melody"
        )
        
        self.assertEqual(len(self.composer.fragments), 1)
        self.assertEqual(fragment.direction, MusicalDirection.EAST)
        self.assertEqual(fragment.voice, InstrumentVoice.MIA_FLUTE)
        self.assertEqual(fragment.intention, "Opening melody")
        self.assertIsNotNone(fragment.id)
    
    def test_create_relationship(self):
        """Test creating musical relationships."""
        relationship = self.composer.create_relationship(
            from_voice=InstrumentVoice.MIA_FLUTE,
            to_voice=InstrumentVoice.KEIKO_PIANO,
            relationship_type="harmonizes_with",
            description="Flute harmonizes with piano foundation"
        )
        
        self.assertEqual(len(self.composer.relationships), 1)
        self.assertEqual(relationship.from_voice, InstrumentVoice.MIA_FLUTE)
        self.assertEqual(relationship.to_voice, InstrumentVoice.KEIKO_PIANO)
        self.assertEqual(relationship.relationship_type, "harmonizes_with")
        self.assertIsNotNone(relationship.id)
    
    def test_get_fragments_by_direction(self):
        """Test filtering fragments by direction."""
        self.composer.add_musical_fragment(
            {"melody": "A-B-C"},
            MusicalDirection.EAST,
            InstrumentVoice.MIA_FLUTE,
            "Dawn melody"
        )
        self.composer.add_musical_fragment(
            {"melody": "D-E-F"},
            MusicalDirection.SOUTH,
            InstrumentVoice.YAJI_CLARINET,
            "Heart melody"
        )
        self.composer.add_musical_fragment(
            {"melody": "G-A-B"},
            MusicalDirection.EAST,
            InstrumentVoice.KEIKO_PIANO,
            "Another dawn melody"
        )
        
        east_fragments = self.composer.get_fragments_by_direction(MusicalDirection.EAST)
        self.assertEqual(len(east_fragments), 2)
        
        south_fragments = self.composer.get_fragments_by_direction(MusicalDirection.SOUTH)
        self.assertEqual(len(south_fragments), 1)
    
    def test_get_fragments_by_voice(self):
        """Test filtering fragments by voice."""
        self.composer.add_musical_fragment(
            {"melody": "C-D-E"},
            MusicalDirection.EAST,
            InstrumentVoice.MIA_FLUTE,
            "Flute melody 1"
        )
        self.composer.add_musical_fragment(
            {"melody": "F-G-A"},
            MusicalDirection.SOUTH,
            InstrumentVoice.MIA_FLUTE,
            "Flute melody 2"
        )
        self.composer.add_musical_fragment(
            {"melody": "B-C-D"},
            MusicalDirection.WEST,
            InstrumentVoice.KEIKO_PIANO,
            "Piano melody"
        )
        
        flute_fragments = self.composer.get_fragments_by_voice(InstrumentVoice.MIA_FLUTE)
        self.assertEqual(len(flute_fragments), 2)
        
        piano_fragments = self.composer.get_fragments_by_voice(InstrumentVoice.KEIKO_PIANO)
        self.assertEqual(len(piano_fragments), 1)
    
    def test_export_composition_data(self):
        """Test exporting composition data."""
        self.composer.set_ceremonial_story("Test story")
        self.composer.set_musical_parameters(key="C major", tempo=100)
        
        self.composer.add_musical_fragment(
            {"melody": "C-D-E"},
            MusicalDirection.EAST,
            InstrumentVoice.MIA_FLUTE,
            "Test fragment"
        )
        
        self.composer.create_relationship(
            InstrumentVoice.MIA_FLUTE,
            InstrumentVoice.KEIKO_PIANO,
            "supports",
            "Test relationship"
        )
        
        data = self.composer.export_composition_data()
        
        self.assertIn("ceremonial_story", data)
        self.assertIn("musical_parameters", data)
        self.assertIn("fragments", data)
        self.assertIn("relationships", data)
        self.assertEqual(len(data["fragments"]), 1)
        self.assertEqual(len(data["relationships"]), 1)
    
    def test_musical_fragment_to_dict(self):
        """Test MusicalFragment serialization."""
        content = {"melody": "C-D-E", "rhythm": "quarter notes"}
        fragment = MusicalFragment(
            content=content,
            direction=MusicalDirection.SOUTH,
            voice=InstrumentVoice.YAJI_CLARINET,
            intention="Test intention"
        )
        
        fragment_dict = fragment.to_dict()
        
        self.assertIn("id", fragment_dict)
        self.assertIn("content", fragment_dict)
        self.assertIn("direction", fragment_dict)
        self.assertIn("voice", fragment_dict)
        self.assertIn("intention", fragment_dict)
        self.assertIn("relationships", fragment_dict)
        self.assertIn("created_at", fragment_dict)
        
        self.assertEqual(fragment_dict["direction"], "SOUTH")
        self.assertEqual(fragment_dict["voice"], "yaji_clarinet")


class TestConvenienceFunctions(unittest.TestCase):
    """Test convenience functions."""
    
    def test_generate_jamai_spiral(self):
        """Test the convenience function for spiral generation."""
        intention = "Test composition"
        story = "Test story"
        
        json_output = generate_jamai_spiral(
            composition_intention=intention,
            ceremonial_story=story,
            key="F major"
        )
        
        # Verify it's valid JSON
        parsed = json.loads(json_output)
        self.assertIn("composition_intention", parsed)
        self.assertIn("ceremonial_story", parsed)
        self.assertIn("four_directions", parsed)
        self.assertEqual(parsed["musical_parameters"]["key"], "F major")


class TestInstrumentVoiceEnum(unittest.TestCase):
    """Test InstrumentVoice enum."""
    
    def test_all_voices_present(self):
        """Test that all expected instrument voices are defined."""
        expected_voices = [
            "MIA_FLUTE", "YAJI_CLARINET", "JAVIER_CLARINET",
            "KEIKO_PIANO", "AI_VOICE_1", "AI_VOICE_2"
        ]
        
        for voice_name in expected_voices:
            self.assertTrue(hasattr(InstrumentVoice, voice_name))


class TestMusicalDirectionEnum(unittest.TestCase):
    """Test MusicalDirection enum."""
    
    def test_all_directions_present(self):
        """Test that all four directions are defined."""
        expected_directions = ["EAST", "SOUTH", "WEST", "NORTH"]
        
        for direction_name in expected_directions:
            self.assertTrue(hasattr(MusicalDirection, direction_name))


if __name__ == "__main__":
    unittest.main()
