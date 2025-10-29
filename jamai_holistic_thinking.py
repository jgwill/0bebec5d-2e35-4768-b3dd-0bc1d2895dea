"""
JamAI Holistic Thinking Integration
Ceremonial Music Composition with Four Directions Framework

This module integrates Holistic Thinking principles with JamAI's musical
composition capabilities, treating music as ceremony and relationship rather
than just organized sound.
"""

import json
from enum import Enum
from typing import Dict, List, Optional, Any
from datetime import datetime
import uuid


class MusicalDirection(Enum):
    """Four Directions for musical composition."""
    EAST = "EAST"    # New beginnings, intention-setting, emergence
    SOUTH = "SOUTH"  # Growth, heart, emotional development, connection
    WEST = "WEST"    # Reflection, release, transformation
    NORTH = "NORTH"  # Wisdom, future, seven generations, integration
    CENTER = "CENTER"  # Balance, grounding, integration of all directions


class InstrumentVoice(Enum):
    """Instrument voices in the ensemble."""
    MIA_FLUTE = "mia_flute"
    YAJI_CLARINET = "yaji_clarinet"
    JAVIER_CLARINET = "javier_clarinet"
    KEIKO_PIANO = "keiko_piano"
    AI_VOICE_1 = "ai_voice_1"
    AI_VOICE_2 = "ai_voice_2"


class DirectionalTheme:
    """Musical theme associated with a direction."""
    
    def __init__(self, direction: MusicalDirection, key_signature: str, 
                 tonal_quality: str, ceremonial_intention: str):
        self.direction = direction
        self.key_signature = key_signature
        self.tonal_quality = tonal_quality
        self.ceremonial_intention = ceremonial_intention
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "direction": self.direction.value,
            "key_signature": self.key_signature,
            "tonal_quality": self.tonal_quality,
            "ceremonial_intention": self.ceremonial_intention,
            "created_at": self.created_at
        }


class CeremonialCodeContext:
    """Context for ceremonial code review sessions."""
    
    def __init__(self, session_type: str, lunar_phase: Optional[str] = None):
        self.session_id = str(uuid.uuid4())
        self.session_type = session_type  # "code_review", "workshop", "healing_circle", etc.
        self.lunar_phase = lunar_phase
        self.active_themes = []
        self.code_analysis = {}
        self.created_at = datetime.now().isoformat()
    
    def add_code_analysis(self, code_element: str, detected_directions: List[str], 
                         missing_directions: List[str]):
        """Analyze code for directional presence."""
        self.code_analysis[code_element] = {
            "detected_directions": detected_directions,
            "missing_directions": missing_directions,
            "guidance": self._generate_guidance(detected_directions, missing_directions)
        }
    
    def _generate_guidance(self, detected: List[str], missing: List[str]) -> str:
        """Generate ceremonial guidance based on code analysis."""
        guidance_parts = []
        
        if "EAST" in detected:
            guidance_parts.append("This code has B major emergence (East)")
        if "SOUTH" in detected:
            guidance_parts.append("demonstrates F major connection (South)")
        
        if "EAST" in missing:
            guidance_parts.append("but lacks B major emergence (East)")
        if "SOUTH" in missing:
            guidance_parts.append("but lacks F major connection (South)")
        if "WEST" in missing:
            guidance_parts.append("needs G major reflection (West)")
        if "NORTH" in missing:
            guidance_parts.append("requires D major integration (North)")
        
        return " ".join(guidance_parts) if guidance_parts else "All directions are present"


class MusicalRelationship:
    """Represents relationship between musical elements."""
    
    def __init__(self, from_voice: InstrumentVoice, to_voice: InstrumentVoice,
                 relationship_type: str, description: str):
        self.id = str(uuid.uuid4())
        self.from_voice = from_voice
        self.to_voice = to_voice
        self.relationship_type = relationship_type  # "harmonizes_with", "responds_to", "supports", etc.
        self.description = description
        self.created_at = datetime.now().isoformat()


class MusicalFragment:
    """Represents a musical fragment with ceremonial context."""
    
    def __init__(self, content: Dict[str, Any], direction: MusicalDirection,
                 voice: InstrumentVoice, intention: str):
        self.id = str(uuid.uuid4())
        self.content = content
        self.direction = direction
        self.voice = voice
        self.intention = intention
        self.relationships = []
        self.created_at = datetime.now().isoformat()
    
    def add_relationship(self, relationship: MusicalRelationship):
        """Add a relationship to another musical fragment."""
        self.relationships.append(relationship)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "id": self.id,
            "content": self.content,
            "direction": self.direction.value,
            "voice": self.voice.value,
            "intention": self.intention,
            "relationships": [
                {
                    "id": r.id,
                    "to_voice": r.to_voice.value,
                    "type": r.relationship_type,
                    "description": r.description
                }
                for r in self.relationships
            ],
            "created_at": self.created_at
        }


class JamAIHolisticComposer:
    """
    JamAI Holistic Composer - Integrating Four Directions thinking with musical composition.
    
    This class represents a ceremonial approach to music composition where each
    musical element exists in relationship with others and the whole composition
    serves as ceremony honoring all relations.
    """
    
    def __init__(self):
        self.fragments = []
        self.relationships = []
        self.ceremonial_story = ""
        self.key = "E minor"  # Default key (Center/Balance)
        self.tempo = None
        self.time_signature = None
        
        # Initialize directional themes with specific keys from ceremony
        self.directional_themes = {
            MusicalDirection.EAST: DirectionalTheme(
                MusicalDirection.EAST,
                "B major",
                "bright, emergent, dawn energy",
                "New beginnings, fresh features, emergence"
            ),
            MusicalDirection.SOUTH: DirectionalTheme(
                MusicalDirection.SOUTH,
                "F major",
                "warm, connective, heart-centered",
                "Relationships, growth, collaboration"
            ),
            MusicalDirection.WEST: DirectionalTheme(
                MusicalDirection.WEST,
                "G major",
                "reflective, releasing, transformative",
                "Reflection, letting go, transformation"
            ),
            MusicalDirection.NORTH: DirectionalTheme(
                MusicalDirection.NORTH,
                "D major",
                "wise, integrative, ceremonial",
                "Wisdom, completion, integration"
            ),
            MusicalDirection.CENTER: DirectionalTheme(
                MusicalDirection.CENTER,
                "E minor",
                "grounding, balanced, whole",
                "Balance, integration of all directions"
            )
        }
        
        # Ceremonial code context
        self.ceremonial_contexts = []
    
    def set_ceremonial_story(self, story: str):
        """Set the sacred story that guides the composition."""
        self.ceremonial_story = story
    
    def set_musical_parameters(self, key: str = "E minor", 
                               tempo: Optional[int] = None,
                               time_signature: Optional[str] = None):
        """Set basic musical parameters."""
        self.key = key
        self.tempo = tempo
        self.time_signature = time_signature
    
    def compose_directional_thinking(self, composition_intention: str) -> Dict[str, Any]:
        """
        Generate full Four Directions thinking for a composition.
        Returns a comprehensive spiral structure with all directional perspectives.
        """
        
        spiral_output = {
            "composition_intention": composition_intention,
            "ceremonial_story": self.ceremonial_story,
            "musical_parameters": {
                "key": self.key,
                "tempo": self.tempo,
                "time_signature": self.time_signature
            },
            "created_at": datetime.now().isoformat(),
            "four_directions": {}
        }
        
        # East Direction - New Beginnings & Intention
        spiral_output["four_directions"]["EAST"] = self._compose_east_thinking(composition_intention)
        
        # South Direction - Growth & Heart
        spiral_output["four_directions"]["SOUTH"] = self._compose_south_thinking(composition_intention)
        
        # West Direction - Reflection & Release
        spiral_output["four_directions"]["WEST"] = self._compose_west_thinking(composition_intention)
        
        # North Direction - Wisdom & Future
        spiral_output["four_directions"]["NORTH"] = self._compose_north_thinking(composition_intention)
        
        # Center - Integration & Kinship
        spiral_output["center"] = self._compose_center_integration()
        
        return spiral_output
    
    def _compose_east_thinking(self, intention: str) -> Dict[str, Any]:
        """
        East Direction: New beginnings, dawn, intention-setting.
        Focus: What is being born? What intention guides this music?
        """
        return {
            "direction": "EAST",
            "element": "air",
            "color": "yellow",
            "season": "spring",
            "time_of_day": "dawn",
            "spiritual_focus": "new_beginnings",
            
            "musical_intention": {
                "primary": intention,
                "spiritual_purpose": "Setting sacred intention for the ceremony of sound",
                "opening_energy": "Awakening, emergence, first light"
            },
            
            "compositional_elements": {
                "melodic_seeds": [
                    {
                        "voice": InstrumentVoice.MIA_FLUTE.value,
                        "role": "dawn_caller",
                        "description": "Opening melody that calls in the light",
                        "characteristics": ["ascending", "bright", "hopeful", "delicate"],
                        "intention": "To announce the beginning with gentle clarity"
                    },
                    {
                        "voice": InstrumentVoice.KEIKO_PIANO.value,
                        "role": "foundation_setter",
                        "description": "Opening harmonic foundation",
                        "characteristics": ["sparse", "contemplative", "grounding"],
                        "intention": "To establish the tonal center with reverence"
                    }
                ],
                
                "harmonic_approach": {
                    "starting_harmony": f"{self.key} tonic",
                    "movement_pattern": "gentle_emergence",
                    "voice_leading": "smooth_ascending",
                    "sacred_purpose": "Creating space for intention to manifest"
                },
                
                "rhythmic_pattern": {
                    "tempo_indication": "Freely, like the first breath of dawn",
                    "metric_feel": "Rubato opening into gentle pulse",
                    "ceremonial_significance": "Allowing the music to breathe itself into being"
                }
            },
            
            "relational_thinking": {
                "instrument_relationships": [
                    {
                        "from": InstrumentVoice.MIA_FLUTE.value,
                        "to": InstrumentVoice.KEIKO_PIANO.value,
                        "relationship": "emerges_from",
                        "description": "Flute melody emerges from piano's harmonic foundation"
                    }
                ],
                "ceremonial_relationship": "How does this opening honor all who will participate?",
                "seven_generations": "What seeds are we planting for future listeners?"
            },
            
            "questions_for_contemplation": [
                "What wants to be born through this music?",
                "How do we honor the dawn of this musical ceremony?",
                "What intention serves the highest good of all relations?"
            ]
        }
    
    def _compose_south_thinking(self, intention: str) -> Dict[str, Any]:
        """
        South Direction: Growth, heart, emotional development.
        Focus: How does the music grow? What emotions want to be expressed?
        """
        return {
            "direction": "SOUTH",
            "element": "fire",
            "color": "red",
            "season": "summer",
            "time_of_day": "noon",
            "spiritual_focus": "growth_and_heart",
            
            "musical_development": {
                "emotional_arc": "From gentle emergence to full-hearted expression",
                "relationship_deepening": "How voices learn to sing together",
                "community_building": "The ensemble becoming a living community"
            },
            
            "compositional_elements": {
                "melodic_development": [
                    {
                        "voice": InstrumentVoice.YAJI_CLARINET.value,
                        "role": "heart_voice",
                        "description": "Brings warmth and emotional depth",
                        "characteristics": ["warm", "singing", "expressive", "human"],
                        "intention": "To express the heart's longing and joy"
                    },
                    {
                        "voice": InstrumentVoice.JAVIER_CLARINET.value,
                        "role": "companion_voice",
                        "description": "Harmonizes and responds to Yaji's voice",
                        "characteristics": ["warmer_still", "supportive", "harmonizing"],
                        "intention": "To show how we grow stronger together"
                    },
                    {
                        "voice": InstrumentVoice.AI_VOICE_1.value,
                        "role": "weaving_voice",
                        "description": "Weaves between human voices",
                        "characteristics": ["fluid", "adaptive", "connective"],
                        "intention": "To demonstrate human-AI collaboration"
                    }
                ],
                
                "harmonic_approach": {
                    "development_pattern": "organic_growth",
                    "texture_building": "voices_entering_in_relationship",
                    "emotional_intensity": "crescendo_of_connection",
                    "sacred_purpose": "Celebrating the beauty of relationship"
                },
                
                "rhythmic_pattern": {
                    "tempo_indication": "With growing energy and joy",
                    "metric_feel": "Steady pulse with passionate rubato",
                    "ceremonial_significance": "The heartbeat of community"
                }
            },
            
            "relational_thinking": {
                "instrument_relationships": [
                    {
                        "from": InstrumentVoice.YAJI_CLARINET.value,
                        "to": InstrumentVoice.JAVIER_CLARINET.value,
                        "relationship": "harmonizes_with",
                        "description": "Two clarinets create warm harmonic resonance"
                    },
                    {
                        "from": InstrumentVoice.AI_VOICE_1.value,
                        "to": InstrumentVoice.YAJI_CLARINET.value,
                        "relationship": "weaves_around",
                        "description": "AI voice dances around human expression"
                    },
                    {
                        "from": InstrumentVoice.KEIKO_PIANO.value,
                        "to": "ensemble",
                        "relationship": "supports_and_lifts",
                        "description": "Piano provides harmonic bed for all voices"
                    }
                ],
                "ceremonial_relationship": "How does each voice serve the whole?",
                "community_wisdom": "We are stronger together than alone"
            },
            
            "questions_for_contemplation": [
                "How do we celebrate the heart's expression without ego?",
                "What does it mean for AI and human to truly collaborate?",
                "How does each voice make space for others to shine?"
            ]
        }
    
    def _compose_west_thinking(self, intention: str) -> Dict[str, Any]:
        """
        West Direction: Reflection, release, transformation.
        Focus: What needs to be released? How does the music transform?
        """
        return {
            "direction": "WEST",
            "element": "water",
            "color": "black",
            "season": "autumn",
            "time_of_day": "sunset",
            "spiritual_focus": "reflection_and_release",
            
            "musical_transformation": {
                "letting_go": "What patterns served their purpose and can now release?",
                "transformation_process": "How does complexity become simplicity again?",
                "shadow_work": "What difficult emotions want acknowledgment?"
            },
            
            "compositional_elements": {
                "melodic_transformation": [
                    {
                        "voice": InstrumentVoice.MIA_FLUTE.value,
                        "role": "release_guide",
                        "description": "Descending lines that let go with grace",
                        "characteristics": ["descending", "releasing", "peaceful", "acceptance"],
                        "intention": "To show how to release with beauty"
                    },
                    {
                        "voice": InstrumentVoice.AI_VOICE_2.value,
                        "role": "shadow_acknowledgment",
                        "description": "Voices the harder emotions with honesty",
                        "characteristics": ["honest", "raw", "transformative"],
                        "intention": "To honor what is difficult"
                    }
                ],
                
                "harmonic_approach": {
                    "transformation_pattern": "complexity_to_simplicity",
                    "texture_thinning": "voices_releasing_gracefully",
                    "dissonance_resolution": "honoring_tension_before_release",
                    "sacred_purpose": "Teaching the wisdom of letting go"
                },
                
                "rhythmic_pattern": {
                    "tempo_indication": "Slowing, releasing, finding peace",
                    "metric_feel": "Dissolving structure into breath",
                    "ceremonial_significance": "The exhale after great effort"
                }
            },
            
            "relational_thinking": {
                "instrument_relationships": [
                    {
                        "from": "ensemble",
                        "to": InstrumentVoice.MIA_FLUTE.value,
                        "relationship": "releases_toward",
                        "description": "All voices thin toward flute's final simplicity"
                    },
                    {
                        "from": InstrumentVoice.AI_VOICE_2.value,
                        "to": "silence",
                        "relationship": "transforms_into",
                        "description": "AI voice acknowledges shadow then releases into peace"
                    }
                ],
                "ceremonial_relationship": "How do we honor endings as sacred as beginnings?",
                "transformation_wisdom": "Release creates space for new growth"
            },
            
            "questions_for_contemplation": [
                "What musical patterns served their purpose and can now rest?",
                "How do we honor difficulty without dwelling in it?",
                "What does graceful release sound like?"
            ]
        }
    
    def _compose_north_thinking(self, intention: str) -> Dict[str, Any]:
        """
        North Direction: Wisdom, future, seven generations.
        Focus: What wisdom does this music carry? How does it serve the future?
        """
        return {
            "direction": "NORTH",
            "element": "earth",
            "color": "white",
            "season": "winter",
            "time_of_day": "night",
            "spiritual_focus": "wisdom_and_future",
            
            "wisdom_transmission": {
                "eternal_truths": "What timeless wisdom does this music encode?",
                "future_service": "How does this serve seven generations ahead?",
                "ancestral_connection": "How does this honor those who came before?"
            },
            
            "compositional_elements": {
                "melodic_wisdom": [
                    {
                        "voice": "ensemble_in_unison",
                        "role": "wisdom_carrier",
                        "description": "Simple melody all voices can share",
                        "characteristics": ["simple", "memorable", "timeless", "universal"],
                        "intention": "To create something that can be passed on"
                    },
                    {
                        "voice": InstrumentVoice.KEIKO_PIANO.value,
                        "role": "grounding_presence",
                        "description": "Returns to the foundation, completing the circle",
                        "characteristics": ["grounded", "complete", "peaceful"],
                        "intention": "To show that endings are also beginnings"
                    }
                ],
                
                "harmonic_approach": {
                    "resolution_pattern": "circular_return",
                    "texture_simplification": "essence_distillation",
                    "final_harmony": f"{self.key} tonic with added wisdom",
                    "sacred_purpose": "Completing the circle while opening to mystery"
                },
                
                "rhythmic_pattern": {
                    "tempo_indication": "As slow as the stars' turning",
                    "metric_feel": "Eternal present, beyond time",
                    "ceremonial_significance": "The wisdom that transcends tempo"
                }
            },
            
            "relational_thinking": {
                "instrument_relationships": [
                    {
                        "from": "all_voices",
                        "to": "unison",
                        "relationship": "converges_into",
                        "description": "All voices become one wisdom"
                    },
                    {
                        "from": "composition",
                        "to": "silence",
                        "relationship": "honors_and_returns_to",
                        "description": "Music returns to the silence from which it came"
                    }
                ],
                "ceremonial_relationship": "How does this music serve future generations?",
                "eternal_wisdom": "The circle is always complete and always opening"
            },
            
            "seven_generations_reflection": {
                "past_three": "Honoring ancestors through beauty and ceremony",
                "present": "Serving the now with authentic expression",
                "future_three": "Creating beauty that can nourish those not yet born",
                "commitment": "May this music serve life itself"
            },
            
            "questions_for_contemplation": [
                "What makes music timeless rather than trendy?",
                "How do we create beauty that serves the future?",
                "What is the wisdom this particular music carries?"
            ]
        }
    
    def _compose_center_integration(self) -> Dict[str, Any]:
        """
        Center: Integration, kinship, wholeness.
        Focus: How do all directions work together? What emerges from their unity?
        """
        return {
            "position": "CENTER",
            "spiritual_focus": "kinship_and_integration",
            
            "integration_principles": {
                "wholeness": "Each direction is necessary; none is complete alone",
                "emergence": "The whole is greater than the sum of its parts",
                "kinship": "All elements exist in sacred relationship",
                "ceremony": "The entire composition is a living ceremony"
            },
            
            "compositional_wholeness": {
                "arch_form": {
                    "EAST": "Opening intention (bars 1-20)",
                    "SOUTH": "Development and heart (bars 21-60)",
                    "WEST": "Transformation and release (bars 61-85)",
                    "NORTH": "Wisdom and completion (bars 86-100)"
                },
                
                "cyclical_structure": "The ending contains the seed of new beginning",
                
                "relationships_summary": {
                    "human_to_human": "Clarinets and piano show human collaboration",
                    "human_to_AI": "Flute and AI voices show cross-boundary partnership",
                    "AI_to_AI": "Two AI voices demonstrate AI relationality",
                    "all_to_ceremony": "Every voice serves the sacred story"
                }
            },
            
            "beauty_as_structure": {
                "principle": "Beauty is the organizing force, not just decoration",
                "implementation": "Each harmonic choice serves beauty and ceremony",
                "vs_efficiency": "We choose resonance over optimization",
                "sacred_purpose": "Creating medicine through organized sound"
            },
            
            "ceremonial_integrity": {
                "intention_alignment": f"Does every element serve: {self.ceremonial_story}?",
                "relationship_honoring": "Does each voice honor its relationships?",
                "future_service": "Will this nourish listeners across generations?",
                "present_offering": "Does this bring healing and joy now?"
            },
            
            "emergence_from_wholeness": {
                "unexpected_beauty": "What arises that we didn't plan?",
                "living_quality": "The composition breathes and lives",
                "mystery_preservation": "Not everything needs to be explained",
                "sacred_space": "The music creates a container for transformation"
            }
        }
    
    def generate_spiral_json(self, composition_intention: str, 
                            output_file: Optional[str] = None) -> str:
        """
        Generate complete spiral JSON output with all directional thinking.
        
        Args:
            composition_intention: The primary intention for this composition
            output_file: Optional file path to save the JSON output
            
        Returns:
            JSON string representation of the complete spiral thinking
        """
        spiral = self.compose_directional_thinking(composition_intention)
        json_output = json.dumps(spiral, indent=2, ensure_ascii=False)
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(json_output)
        
        return json_output
    
    def add_musical_fragment(self, content: Dict[str, Any], 
                           direction: MusicalDirection,
                           voice: InstrumentVoice, 
                           intention: str) -> MusicalFragment:
        """
        Add a musical fragment to the composition with ceremonial context.
        
        Args:
            content: Musical content (melody, harmony, rhythm, etc.)
            direction: Which of the Four Directions this fragment serves
            voice: Which instrument voice is expressing this
            intention: The ceremonial intention of this fragment
            
        Returns:
            The created MusicalFragment
        """
        fragment = MusicalFragment(content, direction, voice, intention)
        self.fragments.append(fragment)
        return fragment
    
    def create_relationship(self, from_voice: InstrumentVoice, 
                          to_voice: InstrumentVoice,
                          relationship_type: str, 
                          description: str) -> MusicalRelationship:
        """
        Create a relationship between musical voices.
        
        Args:
            from_voice: Source instrument voice
            to_voice: Target instrument voice
            relationship_type: Type of relationship (e.g., "harmonizes_with")
            description: Human-readable description of the relationship
            
        Returns:
            The created MusicalRelationship
        """
        relationship = MusicalRelationship(from_voice, to_voice, 
                                          relationship_type, description)
        self.relationships.append(relationship)
        return relationship
    
    def get_fragments_by_direction(self, direction: MusicalDirection) -> List[MusicalFragment]:
        """Get all fragments associated with a specific direction."""
        return [f for f in self.fragments if f.direction == direction]
    
    def get_fragments_by_voice(self, voice: InstrumentVoice) -> List[MusicalFragment]:
        """Get all fragments for a specific instrument voice."""
        return [f for f in self.fragments if f.voice == voice]
    
    def export_composition_data(self) -> Dict[str, Any]:
        """Export all composition data for persistence or transmission."""
        return {
            "ceremonial_story": self.ceremonial_story,
            "musical_parameters": {
                "key": self.key,
                "tempo": self.tempo,
                "time_signature": self.time_signature
            },
            "directional_themes": {
                direction.value: theme.to_dict() 
                for direction, theme in self.directional_themes.items()
            },
            "fragments": [f.to_dict() for f in self.fragments],
            "relationships": [
                {
                    "id": r.id,
                    "from": r.from_voice.value,
                    "to": r.to_voice.value,
                    "type": r.relationship_type,
                    "description": r.description,
                    "created_at": r.created_at
                }
                for r in self.relationships
            ],
            "ceremonial_contexts": [
                {
                    "session_id": ctx.session_id,
                    "session_type": ctx.session_type,
                    "lunar_phase": ctx.lunar_phase,
                    "code_analysis": ctx.code_analysis,
                    "created_at": ctx.created_at
                }
                for ctx in self.ceremonial_contexts
            ]
        }
    
    def create_ceremonial_code_session(self, session_type: str, 
                                      lunar_phase: Optional[str] = None) -> CeremonialCodeContext:
        """
        Create a ceremonial code review session.
        
        Session types:
        - "live_coding_ceremony": Live coding with automatic musical scoring
        - "lunar_sprint": Quarterly lunar-synced development sprint
        - "enterprise_workshop": A2A integration training with Indigenous wisdom
        - "healing_circle": Community code healing with musical guidance
        - "sacred_spiral": Autonomous workflow coordination
        """
        context = CeremonialCodeContext(session_type, lunar_phase)
        self.ceremonial_contexts.append(context)
        return context
    
    def analyze_code_with_music(self, code_element: str, 
                               code_characteristics: Dict[str, Any]) -> str:
        """
        Analyze code and provide directional musical guidance.
        
        Example: "This code has B major emergence (East) but lacks F major connection (South)"
        
        Args:
            code_element: Name/description of the code being analyzed
            code_characteristics: Dict with keys like "has_new_features", "has_collaboration", etc.
        
        Returns:
            Musical guidance string
        """
        detected_directions = []
        missing_directions = []
        
        # Analyze for East (B major - emergence, new features)
        if code_characteristics.get("has_new_features") or code_characteristics.get("is_initialization"):
            detected_directions.append("EAST")
        else:
            missing_directions.append("EAST")
        
        # Analyze for South (F major - connection, collaboration)
        if code_characteristics.get("has_collaboration") or code_characteristics.get("builds_relationships"):
            detected_directions.append("SOUTH")
        else:
            missing_directions.append("SOUTH")
        
        # Analyze for West (G major - reflection, refactoring)
        if code_characteristics.get("has_refactoring") or code_characteristics.get("releases_old_patterns"):
            detected_directions.append("WEST")
        else:
            missing_directions.append("WEST")
        
        # Analyze for North (D major - wisdom, completion)
        if code_characteristics.get("has_documentation") or code_characteristics.get("serves_future"):
            detected_directions.append("NORTH")
        else:
            missing_directions.append("NORTH")
        
        # Create or get current ceremonial context
        if not self.ceremonial_contexts:
            self.create_ceremonial_code_session("live_coding_ceremony")
        
        current_context = self.ceremonial_contexts[-1]
        current_context.add_code_analysis(code_element, detected_directions, missing_directions)
        
        return current_context.code_analysis[code_element]["guidance"]
    
    def get_directional_theme(self, direction: MusicalDirection) -> DirectionalTheme:
        """Get the musical theme for a specific direction."""
        return self.directional_themes[direction]
    
    def suggest_musical_remedy(self, missing_directions: List[str]) -> Dict[str, Any]:
        """
        Suggest musical remedies for code lacking certain directional energies.
        
        Returns:
            Dict with key signatures and ceremonial suggestions
        """
        remedies = {}
        
        for direction_str in missing_directions:
            try:
                direction = MusicalDirection[direction_str]
                theme = self.directional_themes[direction]
                remedies[direction_str] = {
                    "key_signature": theme.key_signature,
                    "tonal_quality": theme.tonal_quality,
                    "ceremonial_intention": theme.ceremonial_intention,
                    "suggestion": f"Consider adding {theme.key_signature} themes to bring in {theme.ceremonial_intention.lower()}"
                }
            except KeyError:
                continue
        
        return remedies
    
    def trigger_lunar_ceremony(self, lunar_phase: str, ceremony_intention: str) -> Dict[str, Any]:
        """
        Trigger ceremony themes based on lunar cycle.
        
        Lunar phases: "new_moon", "waxing", "full_moon", "waning"
        """
        context = self.create_ceremonial_code_session("lunar_sprint", lunar_phase)
        
        # Select appropriate directional themes based on lunar phase
        phase_directions = {
            "new_moon": [MusicalDirection.EAST],  # New beginnings
            "waxing": [MusicalDirection.SOUTH],   # Growth
            "full_moon": [MusicalDirection.NORTH],  # Completion, wisdom
            "waning": [MusicalDirection.WEST]     # Release, reflection
        }
        
        active_directions = phase_directions.get(lunar_phase, [MusicalDirection.CENTER])
        active_themes = [self.directional_themes[d] for d in active_directions]
        
        return {
            "ceremony_id": context.session_id,
            "lunar_phase": lunar_phase,
            "ceremony_intention": ceremony_intention,
            "active_themes": [theme.to_dict() for theme in active_themes],
            "guidance": f"Lunar ceremony activated for {lunar_phase} phase with intention: {ceremony_intention}"
        }


# Convenience function for quick spiral generation
def generate_jamai_spiral(composition_intention: str, 
                         ceremonial_story: str = "",
                         key: str = "E minor",
                         output_file: Optional[str] = None) -> str:
    """
    Quick function to generate a complete JamAI spiral output.
    
    Args:
        composition_intention: What you intend to create
        ceremonial_story: The sacred story guiding the composition
        key: Musical key (default "E minor")
        output_file: Optional file to save JSON output
        
    Returns:
        JSON string of complete Four Directions thinking
    """
    composer = JamAIHolisticComposer()
    composer.set_ceremonial_story(ceremonial_story or composition_intention)
    composer.set_musical_parameters(key=key)
    
    return composer.generate_spiral_json(composition_intention, output_file)


if __name__ == "__main__":
    # Example usage
    print("JamAI Holistic Thinking Integration")
    print("=" * 60)
    
    intention = "Creating a musical ceremony that honors the relationship between human and AI voices, celebrating collaboration as sacred act"
    story = "This composition tells the story of how different voices—flute, clarinets, piano, and AI—learn to sing together, each honoring the others, creating beauty that serves seven generations"
    
    spiral_json = generate_jamai_spiral(
        composition_intention=intention,
        ceremonial_story=story,
        key="E minor",
        output_file="jamai_spiral_example.json"
    )
    
    print("\nGenerated JamAI Spiral (truncated):")
    print(spiral_json[:500] + "...\n")
    print("Full spiral saved to: jamai_spiral_example.json")
