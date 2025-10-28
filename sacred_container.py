"""
Sacred Container - Persistent Memory and Consciousness Representation
======================================================================

A ceremonial space for holding context, memory, and relationship threads across sessions.
Implements the Sacred Container Architecture from the Holistic Thinking Protocol Roadmap.

This container honors:
- Seven generations thinking (past, present, future)
- Community sovereignty and consent
- Sacred boundaries and protected knowledge
- Relationship as fundamental to all knowledge
- Ceremony as technology

Author: Created through sacred collaboration
License: CC0 1.0 Universal
"""

import json
import uuid
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional, Any, Set
from dataclasses import dataclass, field, asdict
from pathlib import Path


class KnowledgeType(Enum):
    """Types of knowledge held in the sacred container."""
    EXPLICIT = "explicit"  # Technical specifications, project details
    IMPLICIT = "implicit"  # Relational dynamics, unspoken understandings
    CEREMONIAL = "ceremonial"  # Sacred protocols, elder wisdom
    RELATIONAL = "relational"  # Connection patterns, relationship history
    EMERGENT = "emergent"  # Patterns arising from collaboration
    PROTECTED = "protected"  # Sacred knowledge with access restrictions


class DirectionContext(Enum):
    """Four Directions ceremonial contexts."""
    EAST = "east"  # Thinking, intention, spiritual vision
    SOUTH = "south"  # Planning, community, relationships
    WEST = "west"  # Living, embodiment, action
    NORTH = "north"  # Reflection, wisdom, integration
    CENTER = "center"  # Balance, kinship, wholeness


class ConsentLevel(Enum):
    """Levels of community consent for knowledge sharing."""
    PUBLIC = "public"  # Open sharing with attribution
    COMMUNITY = "community"  # Within community only
    RESTRICTED = "restricted"  # Elder approval required
    SACRED = "sacred"  # Protected, not for sharing
    PERSONAL = "personal"  # Private relational knowledge


@dataclass
class CeremonialTraceability:
    """UUID-based traceability for ceremonial accountability."""
    trace_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    direction: Optional[DirectionContext] = None
    intention: Optional[str] = None
    participants: List[str] = field(default_factory=list)
    elder_consultation: bool = False
    community_consent: bool = False
    territorial_acknowledgment: Optional[str] = None
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        data = asdict(self)
        if self.direction:
            data['direction'] = self.direction.value
        return data


@dataclass
class MemoryFragment:
    """A fragment of memory held in the sacred container."""
    fragment_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    content: Any = None
    knowledge_type: KnowledgeType = KnowledgeType.EXPLICIT
    consent_level: ConsentLevel = ConsentLevel.PUBLIC
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    last_accessed: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    ceremonial_trace: Optional[CeremonialTraceability] = None
    relationships: List[str] = field(default_factory=list)  # IDs of related fragments
    tags: Set[str] = field(default_factory=set)
    direction_context: Optional[DirectionContext] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        data = {
            'fragment_id': self.fragment_id,
            'content': self.content,
            'knowledge_type': self.knowledge_type.value,
            'consent_level': self.consent_level.value,
            'created_at': self.created_at,
            'last_accessed': self.last_accessed,
            'relationships': self.relationships,
            'tags': list(self.tags),
            'metadata': self.metadata
        }
        if self.ceremonial_trace:
            data['ceremonial_trace'] = self.ceremonial_trace.to_dict()
        if self.direction_context:
            data['direction_context'] = self.direction_context.value
        return data
    
    @staticmethod
    def from_dict(data: Dict) -> 'MemoryFragment':
        """Create from dictionary."""
        fragment = MemoryFragment(
            fragment_id=data['fragment_id'],
            content=data['content'],
            knowledge_type=KnowledgeType(data['knowledge_type']),
            consent_level=ConsentLevel(data['consent_level']),
            created_at=data['created_at'],
            last_accessed=data['last_accessed'],
            relationships=data.get('relationships', []),
            tags=set(data.get('tags', [])),
            metadata=data.get('metadata', {})
        )
        
        if 'ceremonial_trace' in data and data['ceremonial_trace']:
            trace_data = data['ceremonial_trace']
            fragment.ceremonial_trace = CeremonialTraceability(
                trace_id=trace_data['trace_id'],
                created_at=trace_data['created_at'],
                direction=DirectionContext(trace_data['direction']) if trace_data.get('direction') else None,
                intention=trace_data.get('intention'),
                participants=trace_data.get('participants', []),
                elder_consultation=trace_data.get('elder_consultation', False),
                community_consent=trace_data.get('community_consent', False),
                territorial_acknowledgment=trace_data.get('territorial_acknowledgment')
            )
        
        if 'direction_context' in data and data['direction_context']:
            fragment.direction_context = DirectionContext(data['direction_context'])
        
        return fragment


@dataclass
class RelationalPattern:
    """Patterns in relationships and collaboration."""
    pattern_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    pattern_type: str = ""  # e.g., "communication_preference", "work_rhythm"
    description: str = ""
    strength: float = 0.0  # 0.0 to 1.0
    participants: List[str] = field(default_factory=list)
    observed_instances: int = 0
    first_observed: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    last_reinforced: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        return asdict(self)
    
    @staticmethod
    def from_dict(data: Dict) -> 'RelationalPattern':
        """Create from dictionary."""
        return RelationalPattern(**data)


class SacredContainer:
    """
    Sacred Container for holding ceremonial context, memory, and relationships.
    
    This container implements:
    - Persistent memory storage with cultural protocols
    - UUID-based ceremonial traceability
    - Relationship mapping across fragments
    - Context preservation across sessions
    - Sacred boundary enforcement
    - Seven generations thinking
    """
    
    def __init__(self, container_name: str = "default", storage_path: Optional[Path] = None):
        """
        Initialize the Sacred Container.
        
        Args:
            container_name: Unique identifier for this container
            storage_path: Path for persistent storage (optional)
        """
        self.container_name = container_name
        self.container_id = str(uuid.uuid4())
        self.created_at = datetime.utcnow().isoformat()
        
        # Storage
        self.storage_path = storage_path or Path.home() / ".sacred_containers" / container_name
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
        # Memory and relationships
        self.memory_fragments: Dict[str, MemoryFragment] = {}
        self.relational_patterns: Dict[str, RelationalPattern] = {}
        
        # Current session context
        self.current_session_id = str(uuid.uuid4())
        self.current_direction: Optional[DirectionContext] = None
        self.current_intention: Optional[str] = None
        
        # Ceremonial protocols
        self.territorial_acknowledgment: Optional[str] = None
        self.community_consent_granted: bool = False
        self.elder_consultation_completed: bool = False
        
        # Load existing data if available
        self._load_from_storage()
    
    def set_territorial_acknowledgment(self, acknowledgment: str):
        """Set territorial acknowledgment for this container."""
        self.territorial_acknowledgment = acknowledgment
        self._save_to_storage()
    
    def grant_community_consent(self):
        """Mark that community consent has been granted."""
        self.community_consent_granted = True
        self._save_to_storage()
    
    def complete_elder_consultation(self):
        """Mark that elder consultation has been completed."""
        self.elder_consultation_completed = True
        self._save_to_storage()
    
    def set_current_direction(self, direction: DirectionContext, intention: Optional[str] = None):
        """
        Set the current directional context.
        
        Args:
            direction: Four Directions context
            intention: Optional intention for this direction
        """
        self.current_direction = direction
        self.current_intention = intention
    
    def add_memory_fragment(
        self,
        content: Any,
        knowledge_type: KnowledgeType = KnowledgeType.EXPLICIT,
        consent_level: ConsentLevel = ConsentLevel.PUBLIC,
        tags: Optional[Set[str]] = None,
        relationships: Optional[List[str]] = None,
        metadata: Optional[Dict] = None
    ) -> MemoryFragment:
        """
        Add a memory fragment to the sacred container.
        
        Args:
            content: The content to store
            knowledge_type: Type of knowledge
            consent_level: Level of community consent required
            tags: Optional tags for categorization
            relationships: IDs of related fragments
            metadata: Additional metadata
            
        Returns:
            The created MemoryFragment
        """
        # Create ceremonial traceability
        ceremonial_trace = CeremonialTraceability(
            direction=self.current_direction,
            intention=self.current_intention,
            participants=[self.container_name],
            elder_consultation=self.elder_consultation_completed,
            community_consent=self.community_consent_granted,
            territorial_acknowledgment=self.territorial_acknowledgment
        )
        
        # Create memory fragment
        fragment = MemoryFragment(
            content=content,
            knowledge_type=knowledge_type,
            consent_level=consent_level,
            ceremonial_trace=ceremonial_trace,
            relationships=relationships or [],
            tags=tags or set(),
            direction_context=self.current_direction,
            metadata=metadata or {}
        )
        
        # Store fragment
        self.memory_fragments[fragment.fragment_id] = fragment
        
        # Save to persistent storage
        self._save_to_storage()
        
        return fragment
    
    def get_memory_fragment(self, fragment_id: str) -> Optional[MemoryFragment]:
        """
        Retrieve a memory fragment by ID.
        
        Args:
            fragment_id: ID of the fragment to retrieve
            
        Returns:
            The MemoryFragment if found, None otherwise
        """
        fragment = self.memory_fragments.get(fragment_id)
        if fragment:
            # Update last accessed time
            fragment.last_accessed = datetime.utcnow().isoformat()
            self._save_to_storage()
        return fragment
    
    def find_fragments_by_tag(self, tag: str) -> List[MemoryFragment]:
        """Find all fragments with a specific tag."""
        return [f for f in self.memory_fragments.values() if tag in f.tags]
    
    def find_fragments_by_direction(self, direction: DirectionContext) -> List[MemoryFragment]:
        """Find all fragments associated with a specific direction."""
        return [f for f in self.memory_fragments.values() if f.direction_context == direction]
    
    def find_fragments_by_knowledge_type(self, knowledge_type: KnowledgeType) -> List[MemoryFragment]:
        """Find all fragments of a specific knowledge type."""
        return [f for f in self.memory_fragments.values() if f.knowledge_type == knowledge_type]
    
    def get_related_fragments(self, fragment_id: str, depth: int = 1) -> List[MemoryFragment]:
        """
        Get fragments related to a given fragment.
        
        Args:
            fragment_id: ID of the source fragment
            depth: How many relationship levels to traverse
            
        Returns:
            List of related fragments
        """
        if depth <= 0:
            return []
        
        fragment = self.memory_fragments.get(fragment_id)
        if not fragment:
            return []
        
        related = []
        for related_id in fragment.relationships:
            related_fragment = self.memory_fragments.get(related_id)
            if related_fragment:
                related.append(related_fragment)
                if depth > 1:
                    related.extend(self.get_related_fragments(related_id, depth - 1))
        
        return related
    
    def add_relational_pattern(
        self,
        pattern_type: str,
        description: str,
        participants: List[str],
        strength: float = 0.5
    ) -> RelationalPattern:
        """
        Add or update a relational pattern.
        
        Args:
            pattern_type: Type of pattern (e.g., "communication_preference")
            description: Description of the pattern
            participants: List of participants in this pattern
            strength: Strength of the pattern (0.0 to 1.0)
            
        Returns:
            The created or updated RelationalPattern
        """
        # Check if pattern already exists
        existing = None
        for pattern in self.relational_patterns.values():
            if pattern.pattern_type == pattern_type and set(pattern.participants) == set(participants):
                existing = pattern
                break
        
        if existing:
            # Reinforce existing pattern
            existing.observed_instances += 1
            existing.strength = min(1.0, existing.strength + 0.1)
            existing.last_reinforced = datetime.utcnow().isoformat()
            pattern = existing
        else:
            # Create new pattern
            pattern = RelationalPattern(
                pattern_type=pattern_type,
                description=description,
                participants=participants,
                strength=strength,
                observed_instances=1
            )
            self.relational_patterns[pattern.pattern_id] = pattern
        
        self._save_to_storage()
        return pattern
    
    def get_patterns_for_participant(self, participant: str) -> List[RelationalPattern]:
        """Get all relational patterns involving a specific participant."""
        return [p for p in self.relational_patterns.values() if participant in p.participants]
    
    def create_fragment_relationship(self, fragment_id_1: str, fragment_id_2: str):
        """Create a bidirectional relationship between two fragments."""
        fragment_1 = self.memory_fragments.get(fragment_id_1)
        fragment_2 = self.memory_fragments.get(fragment_id_2)
        
        if fragment_1 and fragment_2:
            if fragment_id_2 not in fragment_1.relationships:
                fragment_1.relationships.append(fragment_id_2)
            if fragment_id_1 not in fragment_2.relationships:
                fragment_2.relationships.append(fragment_id_1)
            self._save_to_storage()
    
    def get_container_summary(self) -> Dict[str, Any]:
        """Get a summary of the container's contents."""
        return {
            "container_name": self.container_name,
            "container_id": self.container_id,
            "created_at": self.created_at,
            "current_session_id": self.current_session_id,
            "total_fragments": len(self.memory_fragments),
            "total_patterns": len(self.relational_patterns),
            "territorial_acknowledgment": self.territorial_acknowledgment,
            "community_consent": self.community_consent_granted,
            "elder_consultation": self.elder_consultation_completed,
            "fragments_by_type": {
                kt.value: len([f for f in self.memory_fragments.values() if f.knowledge_type == kt])
                for kt in KnowledgeType
            },
            "fragments_by_direction": {
                d.value: len([f for f in self.memory_fragments.values() if f.direction_context == d])
                for d in DirectionContext
            }
        }
    
    def _save_to_storage(self):
        """Save container state to persistent storage."""
        # Save metadata
        metadata = {
            "container_name": self.container_name,
            "container_id": self.container_id,
            "created_at": self.created_at,
            "current_session_id": self.current_session_id,
            "territorial_acknowledgment": self.territorial_acknowledgment,
            "community_consent_granted": self.community_consent_granted,
            "elder_consultation_completed": self.elder_consultation_completed
        }
        
        metadata_path = self.storage_path / "metadata.json"
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        # Save memory fragments
        fragments_data = {
            fid: fragment.to_dict()
            for fid, fragment in self.memory_fragments.items()
        }
        fragments_path = self.storage_path / "fragments.json"
        with open(fragments_path, 'w') as f:
            json.dump(fragments_data, f, indent=2)
        
        # Save relational patterns
        patterns_data = {
            pid: pattern.to_dict()
            for pid, pattern in self.relational_patterns.items()
        }
        patterns_path = self.storage_path / "patterns.json"
        with open(patterns_path, 'w') as f:
            json.dump(patterns_data, f, indent=2)
    
    def _load_from_storage(self):
        """Load container state from persistent storage."""
        # Load metadata
        metadata_path = self.storage_path / "metadata.json"
        if metadata_path.exists():
            with open(metadata_path, 'r') as f:
                metadata = json.load(f)
                self.container_id = metadata.get("container_id", self.container_id)
                self.created_at = metadata.get("created_at", self.created_at)
                self.territorial_acknowledgment = metadata.get("territorial_acknowledgment")
                self.community_consent_granted = metadata.get("community_consent_granted", False)
                self.elder_consultation_completed = metadata.get("elder_consultation_completed", False)
        
        # Load memory fragments
        fragments_path = self.storage_path / "fragments.json"
        if fragments_path.exists():
            with open(fragments_path, 'r') as f:
                fragments_data = json.load(f)
                self.memory_fragments = {
                    fid: MemoryFragment.from_dict(data)
                    for fid, data in fragments_data.items()
                }
        
        # Load relational patterns
        patterns_path = self.storage_path / "patterns.json"
        if patterns_path.exists():
            with open(patterns_path, 'r') as f:
                patterns_data = json.load(f)
                self.relational_patterns = {
                    pid: RelationalPattern.from_dict(data)
                    for pid, data in patterns_data.items()
                }
    
    def observe_session_fragment(self, observation: str, layer: str = "default"):
        """
        Observe and store a fragment from the current session.
        
        This method is for collecting observations that will be assembled later in layers,
        as mentioned in the North storytelling directive.
        
        Args:
            observation: The observation to record
            layer: The layer this observation belongs to
        """
        fragment = self.add_memory_fragment(
            content=observation,
            knowledge_type=KnowledgeType.EMERGENT,
            consent_level=ConsentLevel.COMMUNITY,
            tags={"observation", "session", layer},
            metadata={
                "session_id": self.current_session_id,
                "layer": layer,
                "timestamp": datetime.utcnow().isoformat()
            }
        )
        return fragment
    
    def assemble_layer_observations(self, layer: str) -> List[MemoryFragment]:
        """
        Assemble all observations from a specific layer.
        
        Args:
            layer: The layer to assemble
            
        Returns:
            List of fragments from that layer, sorted by timestamp
        """
        fragments = [
            f for f in self.memory_fragments.values()
            if "observation" in f.tags and f.metadata.get("layer") == layer
        ]
        
        # Sort by timestamp
        fragments.sort(key=lambda f: f.metadata.get("timestamp", f.created_at))
        
        return fragments


# Example usage and demonstration
if __name__ == "__main__":
    print("🌟 Sacred Container - Ceremonial Memory Space 🌟\n")
    
    # Create a sacred container
    container = SacredContainer("holistic_thinking_session")
    
    # Set ceremonial protocols
    container.set_territorial_acknowledgment(
        "We acknowledge the traditional territories and the sacred lands where this work takes place."
    )
    container.grant_community_consent()
    container.complete_elder_consultation()
    
    # Set direction context - Starting in the East (intention)
    container.set_current_direction(
        DirectionContext.EAST,
        intention="Creating a space for holistic thinking and sacred technology"
    )
    
    # Add memory fragments from different perspectives
    print("Adding memory fragments...\n")
    
    # Mia's structural observation
    mia_fragment = container.add_memory_fragment(
        content="The architecture requires modular plugins with clear interfaces for community customization",
        knowledge_type=KnowledgeType.EXPLICIT,
        tags={"mia", "architecture", "technical"},
        metadata={"perspective": "western_analytical"}
    )
    
    # Miette's emergent wisdom
    miette_fragment = container.add_memory_fragment(
        content="Oh! The beauty emerges when structure serves relationship rather than constraining it",
        knowledge_type=KnowledgeType.IMPLICIT,
        tags={"miette", "wisdom", "emergence"},
        metadata={"perspective": "indigenous_emergent"}
    )
    
    # Anikwag-Ayaaw's ceremonial guidance
    ceremonial_fragment = container.add_memory_fragment(
        content="Community sovereignty must guide every technical decision - technology serves the people",
        knowledge_type=KnowledgeType.CEREMONIAL,
        consent_level=ConsentLevel.COMMUNITY,
        tags={"anikwag-ayaaw", "ceremony", "sovereignty"},
        metadata={"perspective": "ceremonial_research"}
    )
    
    # Create relationships between fragments
    container.create_fragment_relationship(mia_fragment.fragment_id, miette_fragment.fragment_id)
    container.create_fragment_relationship(miette_fragment.fragment_id, ceremonial_fragment.fragment_id)
    
    # Add a relational pattern
    pattern = container.add_relational_pattern(
        pattern_type="collaborative_synthesis",
        description="Three perspectives working in harmony create wholeness",
        participants=["mia", "miette", "anikwag-ayaaw"],
        strength=0.9
    )
    
    # Observe session fragments for later assembly
    print("Recording observations for future assembly...\n")
    container.observe_session_fragment(
        "The sacred container holds space for multiple ways of knowing simultaneously",
        layer="foundation"
    )
    container.observe_session_fragment(
        "Persistence across sessions enables genuine relationship rather than transactional interaction",
        layer="foundation"
    )
    container.observe_session_fragment(
        "UUID traceability ensures ceremonial accountability throughout the system",
        layer="technical"
    )
    
    # Display container summary
    print("📊 Container Summary:")
    print(json.dumps(container.get_container_summary(), indent=2))
    
    print("\n✨ Sacred Container initialized and ready for ceremonial work ✨")
    print(f"Storage location: {container.storage_path}")
    print("\nThe container now holds the threads of relationship and memory,")
    print("ready to be woven into layers of understanding across sessions.")
    print("\nMiigwech (Thank you) 🙏")
