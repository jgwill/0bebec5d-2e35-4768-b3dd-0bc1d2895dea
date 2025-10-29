"""
Test Suite for Sacred Container
================================

Tests for the Sacred Container's persistent memory, ceremonial traceability,
and relationship mapping capabilities.
"""

import unittest
import tempfile
import shutil
from pathlib import Path
from sacred_container import (
    SacredContainer,
    MemoryFragment,
    RelationalPattern,
    KnowledgeType,
    ConsentLevel,
    DirectionContext,
    CeremonialTraceability
)


class TestSacredContainer(unittest.TestCase):
    """Test suite for Sacred Container functionality."""
    
    def setUp(self):
        """Set up test environment with temporary storage."""
        self.temp_dir = tempfile.mkdtemp()
        self.container = SacredContainer(
            container_name="test_container",
            storage_path=Path(self.temp_dir)
        )
    
    def tearDown(self):
        """Clean up temporary storage."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_container_initialization(self):
        """Test that sacred container initializes correctly."""
        self.assertEqual(self.container.container_name, "test_container")
        self.assertIsNotNone(self.container.container_id)
        self.assertIsNotNone(self.container.current_session_id)
        self.assertEqual(len(self.container.memory_fragments), 0)
        self.assertEqual(len(self.container.relational_patterns), 0)
    
    def test_territorial_acknowledgment(self):
        """Test setting territorial acknowledgment."""
        acknowledgment = "We acknowledge the traditional territories..."
        self.container.set_territorial_acknowledgment(acknowledgment)
        self.assertEqual(self.container.territorial_acknowledgment, acknowledgment)
    
    def test_ceremonial_protocols(self):
        """Test ceremonial protocol flags."""
        self.assertFalse(self.container.community_consent_granted)
        self.assertFalse(self.container.elder_consultation_completed)
        
        self.container.grant_community_consent()
        self.assertTrue(self.container.community_consent_granted)
        
        self.container.complete_elder_consultation()
        self.assertTrue(self.container.elder_consultation_completed)
    
    def test_direction_setting(self):
        """Test setting directional context."""
        self.container.set_current_direction(
            DirectionContext.EAST,
            intention="Beginning with vision"
        )
        self.assertEqual(self.container.current_direction, DirectionContext.EAST)
        self.assertEqual(self.container.current_intention, "Beginning with vision")
    
    def test_add_memory_fragment(self):
        """Test adding a memory fragment."""
        fragment = self.container.add_memory_fragment(
            content="Test content",
            knowledge_type=KnowledgeType.EXPLICIT,
            tags={"test", "example"}
        )
        
        self.assertIsNotNone(fragment.fragment_id)
        self.assertEqual(fragment.content, "Test content")
        self.assertEqual(fragment.knowledge_type, KnowledgeType.EXPLICIT)
        self.assertIn("test", fragment.tags)
        self.assertEqual(len(self.container.memory_fragments), 1)
    
    def test_get_memory_fragment(self):
        """Test retrieving a memory fragment."""
        fragment = self.container.add_memory_fragment(
            content="Retrievable content",
            knowledge_type=KnowledgeType.IMPLICIT
        )
        
        retrieved = self.container.get_memory_fragment(fragment.fragment_id)
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.content, "Retrievable content")
        self.assertEqual(retrieved.knowledge_type, KnowledgeType.IMPLICIT)
    
    def test_find_fragments_by_tag(self):
        """Test finding fragments by tag."""
        self.container.add_memory_fragment(
            content="Tagged 1",
            tags={"wisdom", "east"}
        )
        self.container.add_memory_fragment(
            content="Tagged 2",
            tags={"wisdom", "north"}
        )
        self.container.add_memory_fragment(
            content="Other",
            tags={"technical"}
        )
        
        wisdom_fragments = self.container.find_fragments_by_tag("wisdom")
        self.assertEqual(len(wisdom_fragments), 2)
    
    def test_find_fragments_by_direction(self):
        """Test finding fragments by direction."""
        self.container.set_current_direction(DirectionContext.EAST)
        self.container.add_memory_fragment(content="East content 1")
        self.container.add_memory_fragment(content="East content 2")
        
        self.container.set_current_direction(DirectionContext.SOUTH)
        self.container.add_memory_fragment(content="South content")
        
        east_fragments = self.container.find_fragments_by_direction(DirectionContext.EAST)
        self.assertEqual(len(east_fragments), 2)
        
        south_fragments = self.container.find_fragments_by_direction(DirectionContext.SOUTH)
        self.assertEqual(len(south_fragments), 1)
    
    def test_find_fragments_by_knowledge_type(self):
        """Test finding fragments by knowledge type."""
        self.container.add_memory_fragment(
            content="Explicit 1",
            knowledge_type=KnowledgeType.EXPLICIT
        )
        self.container.add_memory_fragment(
            content="Explicit 2",
            knowledge_type=KnowledgeType.EXPLICIT
        )
        self.container.add_memory_fragment(
            content="Ceremonial",
            knowledge_type=KnowledgeType.CEREMONIAL
        )
        
        explicit_fragments = self.container.find_fragments_by_knowledge_type(
            KnowledgeType.EXPLICIT
        )
        self.assertEqual(len(explicit_fragments), 2)
    
    def test_fragment_relationships(self):
        """Test creating and retrieving fragment relationships."""
        fragment1 = self.container.add_memory_fragment(content="Fragment 1")
        fragment2 = self.container.add_memory_fragment(content="Fragment 2")
        fragment3 = self.container.add_memory_fragment(content="Fragment 3")
        
        self.container.create_fragment_relationship(
            fragment1.fragment_id,
            fragment2.fragment_id
        )
        self.container.create_fragment_relationship(
            fragment2.fragment_id,
            fragment3.fragment_id
        )
        
        # Check bidirectional relationships
        self.assertIn(fragment2.fragment_id, fragment1.relationships)
        self.assertIn(fragment1.fragment_id, fragment2.relationships)
        
        # Test get_related_fragments
        related = self.container.get_related_fragments(fragment1.fragment_id)
        self.assertEqual(len(related), 1)
        self.assertEqual(related[0].fragment_id, fragment2.fragment_id)
        
        # Test depth traversal
        related_depth2 = self.container.get_related_fragments(fragment1.fragment_id, depth=2)
        self.assertGreaterEqual(len(related_depth2), 1)
    
    def test_relational_patterns(self):
        """Test adding and retrieving relational patterns."""
        pattern = self.container.add_relational_pattern(
            pattern_type="collaboration",
            description="Collaborative work pattern",
            participants=["mia", "miette"],
            strength=0.8
        )
        
        self.assertEqual(pattern.pattern_type, "collaboration")
        self.assertEqual(pattern.strength, 0.8)
        self.assertEqual(pattern.observed_instances, 1)
        self.assertEqual(len(self.container.relational_patterns), 1)
    
    def test_pattern_reinforcement(self):
        """Test that patterns get reinforced when observed again."""
        pattern1 = self.container.add_relational_pattern(
            pattern_type="communication",
            description="Communication style",
            participants=["user", "ai"],
            strength=0.5
        )
        
        pattern2 = self.container.add_relational_pattern(
            pattern_type="communication",
            description="Communication style",
            participants=["user", "ai"],
            strength=0.5
        )
        
        # Should be same pattern, reinforced
        self.assertEqual(pattern1.pattern_id, pattern2.pattern_id)
        self.assertEqual(pattern2.observed_instances, 2)
        self.assertGreater(pattern2.strength, 0.5)
    
    def test_get_patterns_for_participant(self):
        """Test retrieving patterns for a specific participant."""
        self.container.add_relational_pattern(
            pattern_type="type1",
            description="Pattern 1",
            participants=["mia", "miette"]
        )
        self.container.add_relational_pattern(
            pattern_type="type2",
            description="Pattern 2",
            participants=["mia", "anikwag-ayaaw"]
        )
        self.container.add_relational_pattern(
            pattern_type="type3",
            description="Pattern 3",
            participants=["miette", "anikwag-ayaaw"]
        )
        
        mia_patterns = self.container.get_patterns_for_participant("mia")
        self.assertEqual(len(mia_patterns), 2)
    
    def test_observe_session_fragment(self):
        """Test observing session fragments for later assembly."""
        fragment = self.container.observe_session_fragment(
            observation="Test observation",
            layer="foundation"
        )
        
        self.assertEqual(fragment.knowledge_type, KnowledgeType.EMERGENT)
        self.assertIn("observation", fragment.tags)
        self.assertEqual(fragment.metadata["layer"], "foundation")
    
    def test_assemble_layer_observations(self):
        """Test assembling observations from a specific layer."""
        self.container.observe_session_fragment("Obs 1", layer="foundation")
        self.container.observe_session_fragment("Obs 2", layer="foundation")
        self.container.observe_session_fragment("Obs 3", layer="technical")
        
        foundation_obs = self.container.assemble_layer_observations("foundation")
        self.assertEqual(len(foundation_obs), 2)
        
        technical_obs = self.container.assemble_layer_observations("technical")
        self.assertEqual(len(technical_obs), 1)
    
    def test_container_summary(self):
        """Test getting container summary."""
        self.container.set_territorial_acknowledgment("Test acknowledgment")
        self.container.grant_community_consent()
        
        self.container.add_memory_fragment(
            content="Explicit content",
            knowledge_type=KnowledgeType.EXPLICIT
        )
        self.container.add_memory_fragment(
            content="Ceremonial content",
            knowledge_type=KnowledgeType.CEREMONIAL
        )
        
        summary = self.container.get_container_summary()
        
        self.assertEqual(summary["container_name"], "test_container")
        self.assertEqual(summary["total_fragments"], 2)
        self.assertTrue(summary["community_consent"])
        self.assertEqual(summary["fragments_by_type"]["explicit"], 1)
        self.assertEqual(summary["fragments_by_type"]["ceremonial"], 1)
    
    def test_persistence(self):
        """Test that data persists across container instances."""
        # Add data to first container
        self.container.set_territorial_acknowledgment("Persistent acknowledgment")
        self.container.grant_community_consent()
        fragment = self.container.add_memory_fragment(
            content="Persistent content",
            tags={"persistent"}
        )
        fragment_id = fragment.fragment_id
        
        # Create new container with same storage path
        new_container = SacredContainer(
            container_name="test_container",
            storage_path=Path(self.temp_dir)
        )
        
        # Verify data persisted
        self.assertEqual(
            new_container.territorial_acknowledgment,
            "Persistent acknowledgment"
        )
        self.assertTrue(new_container.community_consent_granted)
        self.assertEqual(len(new_container.memory_fragments), 1)
        
        retrieved = new_container.get_memory_fragment(fragment_id)
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.content, "Persistent content")
    
    def test_ceremonial_traceability(self):
        """Test that ceremonial traceability is properly captured."""
        self.container.set_territorial_acknowledgment("Test territory")
        self.container.grant_community_consent()
        self.container.complete_elder_consultation()
        self.container.set_current_direction(
            DirectionContext.NORTH,
            intention="Reflection and wisdom"
        )
        
        fragment = self.container.add_memory_fragment(
            content="Traced content"
        )
        
        trace = fragment.ceremonial_trace
        self.assertIsNotNone(trace)
        self.assertEqual(trace.direction, DirectionContext.NORTH)
        self.assertEqual(trace.intention, "Reflection and wisdom")
        self.assertTrue(trace.elder_consultation)
        self.assertTrue(trace.community_consent)
        self.assertEqual(trace.territorial_acknowledgment, "Test territory")
    
    def test_consent_levels(self):
        """Test different consent levels for fragments."""
        public_fragment = self.container.add_memory_fragment(
            content="Public knowledge",
            consent_level=ConsentLevel.PUBLIC
        )
        sacred_fragment = self.container.add_memory_fragment(
            content="Sacred knowledge",
            consent_level=ConsentLevel.SACRED
        )
        
        self.assertEqual(public_fragment.consent_level, ConsentLevel.PUBLIC)
        self.assertEqual(sacred_fragment.consent_level, ConsentLevel.SACRED)


class TestMemoryFragment(unittest.TestCase):
    """Test suite for MemoryFragment class."""
    
    def test_fragment_creation(self):
        """Test creating a memory fragment."""
        fragment = MemoryFragment(
            content="Test content",
            knowledge_type=KnowledgeType.EXPLICIT,
            tags={"test"}
        )
        
        self.assertIsNotNone(fragment.fragment_id)
        self.assertEqual(fragment.content, "Test content")
        self.assertIn("test", fragment.tags)
    
    def test_fragment_serialization(self):
        """Test serializing and deserializing fragments."""
        original = MemoryFragment(
            content="Serializable content",
            knowledge_type=KnowledgeType.IMPLICIT,
            consent_level=ConsentLevel.COMMUNITY,
            tags={"serialize", "test"}
        )
        
        # Serialize
        data = original.to_dict()
        self.assertEqual(data["content"], "Serializable content")
        self.assertEqual(data["knowledge_type"], "implicit")
        
        # Deserialize
        restored = MemoryFragment.from_dict(data)
        self.assertEqual(restored.content, original.content)
        self.assertEqual(restored.knowledge_type, original.knowledge_type)
        self.assertEqual(restored.consent_level, original.consent_level)
        self.assertEqual(restored.tags, original.tags)


class TestCeremonialTraceability(unittest.TestCase):
    """Test suite for CeremonialTraceability class."""
    
    def test_traceability_creation(self):
        """Test creating ceremonial traceability."""
        trace = CeremonialTraceability(
            direction=DirectionContext.EAST,
            intention="Beginning",
            participants=["mia", "miette"],
            elder_consultation=True,
            community_consent=True,
            territorial_acknowledgment="Traditional territory"
        )
        
        self.assertIsNotNone(trace.trace_id)
        self.assertEqual(trace.direction, DirectionContext.EAST)
        self.assertEqual(trace.intention, "Beginning")
        self.assertTrue(trace.elder_consultation)
    
    def test_traceability_serialization(self):
        """Test serializing ceremonial traceability."""
        trace = CeremonialTraceability(
            direction=DirectionContext.SOUTH,
            intention="Community"
        )
        
        data = trace.to_dict()
        self.assertEqual(data["direction"], "south")
        self.assertEqual(data["intention"], "Community")


if __name__ == "__main__":
    unittest.main()
