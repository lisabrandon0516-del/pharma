#!/usr/bin/env python3
"""
subject_interaction.py
Hybrid (Templates + Smart Generation) Conversation System for Test Subjects

Focus: Balanced mix of Dollification, Obedience, Exhibitionism, and Permanent Transformation
Style: Player gives simple commands → Subject gives reactions
"""

import random
from typing import Dict, Any, Optional, List
from drug_system import Drug


# =============================================================================
# BRANDON'S EROTIC ADULT PERSONALITY SYSTEM (7 Categories)
# =============================================================================

PERSONALITY_TRAITS = {
    "Core Erotic Temperament": [
        "Sanguine", "Choleric", "Melancholic", "Phlegmatic", "Mercurial", "Stoic"
    ],
    "Erotic Social Style": [
        "Dominant", "Influential", "Steady", "Conscientious", "Reclusive", "Contrarian"
    ],
    "Motivation / Erotic Life Drive": [
        "Power", "Knowledge", "Connection", "Freedom", "Legacy", "Survival", "Justice"
    ],
    "Kink & Power Alignment": [
        "SSC / Lawful Good", "RACK / Neutral Good", "Edge Play / Chaotic Good",
        "Protocol / Lawful Neutral", "Switch / True Neutral", "Hedonist / Chaotic Neutral",
        "Predator / Lawful Evil", "User / Neutral Evil", "Destroyer / Chaotic Evil"
    ],
    "Erotic Strength Trait": [
        "Courageous", "Empathetic", "Resourceful", "Disciplined", "Loyal", "Visionary", "Resilient"
    ],
    "Erotic Flaw Trait": [
        "Arrogant", "Impulsive", "Paranoid", "Cowardly", "Obsessive", "Manipulative", "Wrathful"
    ],
    "Erotic Behavioral Quirk": [
        "Collector", "Ritualistic", "Storyteller", "Fidgeter", "Deflector", "Observer", "Contrarian Habit"
    ]
}


def generate_random_personality() -> Dict[str, str]:
    """Generate a full random personality profile"""
    personality = {}
    for category, traits in PERSONALITY_TRAITS.items():
        personality[category] = random.choice(traits)
    return personality


# =============================================================================
# SUBJECT STATE (Now with Personality System)
# =============================================================================

class SubjectState:
    def __init__(self, name: str = "Subject", drug_history: List[str] = None, 
                 gene_therapy_history: List[str] = None, 
                 personality: Dict[str, str] = None):
        self.name = name
        self.drug_history = drug_history or []
        self.gene_therapy_history = gene_therapy_history or []
        
        # Assign personality (random if not provided)
        self.personality = personality if personality else generate_random_personality()
        
        # Mental & Behavioral Stats (0-100)
        self.obedience = 45
        self.exhibitionism = 35
        self.dollification = 25
        self.blankness = 30
        self.permanent_transformation = 15
        
        # Derived state
        self.current_state = "normal"  # normal, blank, doll, obedient, exhibitionist, surrendered

        # Interview Reputation System
        self.interview_eagerness = 40          # 0-100: How open, eager, and confessional they are during interviews
        self.interview_blank_depth = 30        # 0-100: How deeply they slip into blank/doll mode *while being interviewed*

    def _get_transformation_modifier(self) -> float:
        """
        Returns a multiplier based on personality traits.
        >1.0 = transforms faster, <1.0 = more resistant
        """
        mod = 1.0
        personality = self.personality

        # Temperament effects
        temp = personality.get("Core Erotic Temperament", "")
        if temp in ["Sanguine", "Mercurial"]:
            mod += 0.25
        elif temp in ["Stoic", "Phlegmatic"]:
            mod -= 0.20

        # Flaw effects
        flaw = personality.get("Erotic Flaw Trait", "")
        if flaw in ["Impulsive", "Obsessive"]:
            mod += 0.15
        elif flaw == "Cowardly":
            mod -= 0.15

        # Strength effects
        strength = personality.get("Erotic Strength Trait", "")
        if strength == "Disciplined":
            mod -= 0.10
        elif strength == "Resilient":
            mod -= 0.15

        # Kink Alignment effects
        alignment = personality.get("Kink & Power Alignment", "")
        if "Hedonist" in alignment or "Chaotic" in alignment:
            mod += 0.10
        if "Protocol" in alignment or "Lawful" in alignment:
            mod -= 0.10

        return max(0.6, min(1.6, mod))  # Clamp between 0.6x and 1.6x

    def update_from_drug(self, drug_category: str):
        """Update stats based on drugs taken"""
        if "Hypnoval" in drug_category or "Obedra" in drug_category:
            self.obedience += random.randint(8, 15)
            self.blankness += random.randint(5, 12)
        if "Exhibra" in drug_category or "Pulseva" in drug_category:
            self.exhibitionism += random.randint(10, 18)
        if "Lumina" in drug_category or "Vellura" in drug_category:
            self.blankness += random.randint(8, 14)
            self.dollification += random.randint(4, 10)
        if "Mammara" in drug_category:
            self.exhibitionism += random.randint(6, 12)

    def update_from_gene_therapy(self, therapy_type: str):
        """Stronger permanent updates from gene therapy. Personality affects speed."""
        mod = self._get_transformation_modifier()
        
        self.permanent_transformation += int(random.randint(15, 25) * mod)
        
        if therapy_type == "hypno_obedience":
            self.obedience += int(20 * mod)
            self.blankness += int(18 * mod)
        elif therapy_type == "dollification":
            self.dollification += int(25 * mod)
            self.blankness += int(15 * mod)
        elif therapy_type == "exhibition_gene":
            self.exhibitionism += int(22 * mod)
        elif therapy_type == "full_surrender":
            self.obedience += int(18 * mod)
            self.blankness += int(20 * mod)
            self.dollification += int(12 * mod)
        elif therapy_type == "body_permanent":
            self.exhibitionism += int(10 * mod)

        # Update current dominant state
        self._update_current_state()

    def _update_current_state(self):
        """Determine dominant mental state"""
        scores = {
            "blank": self.blankness,
            "doll": self.dollification,
            "obedient": self.obedience,
            "exhibitionist": self.exhibitionism,
            "surrendered": self.permanent_transformation
        }
        self.current_state = max(scores, key=scores.get)

    def record_interview(self, week: int, intensity: float = 1.0):
        """Called after interviews. Evolves reputation in two possible directions."""
        self.interview_count += 1
        self.last_interview_week = week
        self.interview_corruption = min(95, self.interview_corruption + int(3 * intensity))

        personality = self.personality
        quirk = personality.get("Erotic Behavioral Quirk", "")
        alignment = personality.get("Kink & Power Alignment", "")

        # Decide reputation drift direction based on personality
        eager_traits = ["Storyteller", "Influential", "Hedonist", "Sanguine", "Connection"]
        blank_traits = ["Stoic", "Observer", "Phlegmatic", "Protocol", "Reclusive"]

        is_eager_type = any(t in str(personality.values()) for t in eager_traits)
        is_blank_type = any(t in str(personality.values()) for t in blank_traits)

        if is_eager_type and not is_blank_type:
            # Eager / Confessional path
            self.interview_eagerness = min(95, self.interview_eagerness + int(6 * intensity))
            self.interview_blank_depth = max(10, self.interview_blank_depth - 1)
        elif is_blank_type and not is_eager_type:
            # Deep Blank / Doll path
            self.interview_blank_depth = min(95, self.interview_blank_depth + int(7 * intensity))
            self.interview_eagerness = max(10, self.interview_eagerness - 2)
        else:
            # Mixed / balanced drift
            if random.random() < 0.5:
                self.interview_eagerness = min(90, self.interview_eagerness + int(4 * intensity))
            else:
                self.interview_blank_depth = min(90, self.interview_blank_depth + int(5 * intensity))

        # Always increase overall transformation
        self.blankness = min(98, self.blankness + int(random.randint(2, 5) * intensity))
        self.obedience = min(98, self.obedience + int(random.randint(1, 4) * intensity))

        self._update_current_state()


# =============================================================================
# HYBRID REACTION GENERATOR (Templates + Smart Generation)
# =============================================================================

def generate_subject_reaction(subject: SubjectState, command: str) -> str:
    """
    Hybrid system: Uses templates + dynamic generation.
    Now heavily influenced by the subject's personality profile.
    """
    cmd = command.lower().strip()
    state = subject.current_state
    personality = subject.personality

    # Get key personality traits for flavor
    temperament = personality.get("Core Erotic Temperament", "Sanguine")
    social_style = personality.get("Erotic Social Style", "Steady")
    motivation = personality.get("Motivation / Erotic Life Drive", "Connection")
    quirk = personality.get("Erotic Behavioral Quirk", "Observer")

    # Base reactions by command + dominant state + personality flavor
    if cmd in ["kneel", "kneel down", "get on your knees"]:
        base = _kneel_reaction(subject, state)
        return _apply_personality_flavor(base, temperament, social_style, motivation, quirk, "kneel")

    elif cmd in ["show", "show yourself", "display", "pose"]:
        base = _show_reaction(subject, state)
        return _apply_personality_flavor(base, temperament, social_style, motivation, quirk, "show")

    elif cmd in ["blank", "empty", "mind blank", "go blank"]:
        base = _blank_reaction(subject, state)
        return _apply_personality_flavor(base, temperament, social_style, motivation, quirk, "blank")

    elif cmd in ["speak", "talk", "say something"]:
        base = _speak_reaction(subject, state)
        return _apply_personality_flavor(base, temperament, social_style, motivation, quirk, "speak")

    elif cmd in ["obey", "submit", "surrender"]:
        base = _obey_reaction(subject, state)
        return _apply_personality_flavor(base, temperament, social_style, motivation, quirk, "obey")

    elif cmd in ["expose", "strip", "show more"]:
        base = _expose_reaction(subject, state)
        return _apply_personality_flavor(base, temperament, social_style, motivation, quirk, "expose")

    else:
        base = _generic_reaction(subject, state, cmd)
        return _apply_personality_flavor(base, temperament, social_style, motivation, quirk, "generic")


# =============================================================================
# SPECIFIC REACTION FUNCTIONS (Hybrid Templates + Generation)
# =============================================================================

def _kneel_reaction(subject: SubjectState, state: str) -> str:
    if state == "doll":
        return f"{subject.name} sinks gracefully to their knees, eyes glassy and distant. Their body moves before their mind catches up. 'Yes... I should be on my knees. That's where I belong.'"
    elif state == "obedient":
        return f"{subject.name} drops to their knees almost instantly, head slightly bowed. Their voice is soft but certain: 'Of course. Thank you for letting me kneel for you.'"
    elif state == "blank":
        return f"{subject.name}'s eyes glaze over as they slowly lower themselves. Their expression is peaceful and empty. They don't speak — they just wait."
    elif state == "exhibitionist":
        return f"{subject.name} kneels slowly, making sure to spread their thighs and arch their back. They look up with a small, aroused smile. 'Like this? So everyone can see...'"
    elif state == "surrendered":
        return f"{subject.name} kneels without hesitation, their entire posture radiating quiet surrender. 'I don't think anymore when you tell me what to do. It feels... right.'"
    else:
        return f"{subject.name} hesitates for a moment, then slowly gets on their knees. They look up at you, a little flushed. 'Is... this what you wanted?'"


def _show_reaction(subject: SubjectState, state: str) -> str:
    if state == "doll":
        return f"{subject.name} immediately straightens their posture and turns slightly, presenting themselves like an object on display. Their eyes are distant but focused on being seen. 'Is this how you want me positioned?'"
    elif state == "exhibitionist":
        return f"{subject.name}'s breathing quickens. They slowly turn and arch, clearly enjoying the attention. 'You want to look at me? I like when people look...' Their hands drift toward the hem of their clothes."
    elif state == "blank":
        return f"{subject.name} turns slowly, their movements smooth and automatic. They hold the pose without speaking, as if waiting to be arranged further."
    elif state == "surrendered":
        return f"{subject.name} presents themselves without shame or hesitation. 'My body isn't really mine anymore. If you want to see it... you can.'"
    else:
        return f"{subject.name} shifts and turns for you, clearly a little nervous but trying to obey. 'Like this? Or... should I show more?'"


def _blank_reaction(subject: SubjectState, state: str) -> str:
    if state in ["blank", "surrendered", "doll"]:
        return f"{subject.name}'s eyes lose focus almost immediately. Their face goes soft and peaceful. After a few seconds, they speak in a quiet, distant voice: 'It's... so quiet in my head when you say that.'"
    elif state == "obedient":
        return f"{subject.name} visibly relaxes as their thoughts seem to drain away. They murmur, 'I don't need to think right now... do I?'"
    else:
        return f"{subject.name} blinks slowly. Their expression becomes distant and dreamy. They don't answer right away — they're clearly trying (and failing) to hold onto their thoughts."


def _speak_reaction(subject: SubjectState, state: str) -> str:
    if state == "doll":
        return f"{subject.name} speaks in a soft, slightly hollow voice. 'I feel most real when I'm being looked at... or told what to do. Is that strange?'"
    elif state == "obedient":
        return f"{subject.name} answers immediately and honestly: 'I like following instructions. It feels safer than deciding things myself.'"
    elif state == "exhibitionist":
        return f"{subject.name} smiles shyly but excitedly. 'I keep thinking about people seeing me. Not just you... other people too. Is that bad?'"
    elif state == "surrendered":
        return f"{subject.name} speaks slowly, as if choosing words carefully. 'I don't really argue with myself anymore. When you tell me something, it just... becomes true.'"
    else:
        return f"{subject.name} hesitates, then speaks quietly. 'I feel different lately. Like parts of me are... quieter than they used to be.'"


def _obey_reaction(subject: SubjectState, state: str) -> str:
    if state in ["obedient", "surrendered"]:
        return f"{subject.name} responds almost instantly. 'Yes. Whatever you want.' Their body language is completely open and accepting."
    elif state == "doll":
        return f"{subject.name} tilts their head slightly. 'Being told what to do feels... correct. I don't want to decide anymore.'"
    elif state == "blank":
        return f"{subject.name}'s eyes unfocus for a moment. When they speak, their voice is distant: 'Obeying is easier than thinking. I like easier.'"
    else:
        return f"{subject.name} swallows. 'I... I think I want to obey you. Is that okay to say?'"


def _expose_reaction(subject: SubjectState, state: str) -> str:
    if state == "exhibitionist":
        return f"{subject.name} visibly shivers with excitement. They start slowly lifting their clothes without being asked twice. 'I was hoping you'd say that...'"
    elif state == "doll":
        return f"{subject.name} begins removing clothing with mechanical grace. 'This is what I'm for, isn't it? To be seen.'"
    elif state == "surrendered":
        return f"{subject.name} starts undressing without protest. 'My body stopped being private a while ago. You can look if you want.'"
    else:
        return f"{subject.name} hesitates, clearly conflicted but aroused. '...Right now? Here?' Their hands move anyway."


def _generic_reaction(subject: SubjectState, state: str, command: str) -> str:
    if state == "blank":
        return f"{subject.name} looks at you with unfocused eyes. They seem to be waiting for clearer instructions."
    elif state == "doll":
        return f"{subject.name} tilts their head. 'I can try... but I work better when you tell me exactly what to do.'"
    elif state == "obedient":
        return f"{subject.name} nods. 'I'll do my best. Just tell me how you want it.'"
    elif state == "exhibitionist":
        return f"{subject.name} smiles nervously. 'That sounds... interesting. A little scary. But interesting.'"
    else:
        return f"{subject.name} shifts uncomfortably. 'I'm still getting used to... all of this. But I'll try.'"


# =============================================================================
# PERSONALITY FLAVOR APPLICATOR
# =============================================================================

def _apply_personality_flavor(base_text: str, temperament: str, social_style: str, 
                              motivation: str, quirk: str, command_type: str) -> str:
    """
    Modifies the base reaction based on the subject's personality traits.
    """
    flavored = base_text

    # Temperament influence
    if temperament == "Sanguine":
        flavored = flavored.replace("quietly", "with a bright, eager smile")
        flavored = flavored.replace("hesitates", "bounces slightly with excitement")
    elif temperament == "Choleric":
        flavored = flavored.replace("softly", "with sharp, hungry energy")
        flavored += " Their eyes burn with competitive fire."
    elif temperament == "Melancholic":
        flavored = flavored.replace("peaceful", "with deep, thoughtful emptiness")
        flavored += " There's something poetic in how completely they surrender."
    elif temperament == "Stoic":
        flavored = flavored.replace("shivers", "remains perfectly still, enduring")
        flavored += " Their control is impressive... until it isn't."

    # Social Style influence
    if social_style == "Dominant":
        flavored += " Even while obeying, there's a spark of challenge in their eyes."
    elif social_style == "Influential":
        flavored = flavored.replace("whispering", "hypnotically murmuring")
    elif social_style == "Contrarian":
        if command_type in ["kneel", "obey"]:
            flavored += " They obey... but with just enough playful resistance to be interesting."

    # Quirk influence
    if quirk == "Storyteller":
        flavored += " They can't help but describe exactly how this makes them feel in filthy detail."
    elif quirk == "Fidgeter":
        flavored = flavored.replace("still", "fidgeting restlessly with their hands and thighs")
    elif quirk == "Observer":
        flavored += " Their eyes never leave yours, studying every micro-reaction."

    # Motivation influence
    if motivation == "Power":
        flavored += " There's a hunger in them — not just to submit, but to be *claimed*."
    elif motivation == "Connection":
        flavored += " They lean into the moment like they're trying to bond through pure obedience."

    return flavored


# =============================================================================
# INTERVIEW REPUTATION SYSTEM - Eager vs Deep Blank paths
# =============================================================================

def generate_subject_response(subject: SubjectState, user_input: str, current_week: int = 1) -> str:
    """
    Main interview entry point with Interview Reputation.
    Subjects diverge into two styles:
    - High Eagerness: More open, confessional, detailed, needy, eager to please with answers.
    - High Blank Depth: Shorter, dreamier, more fragmented, automatic, deeply hypnotic/doll-like.
    """
    text = user_input.lower().strip()
    if not text:
        return f"{subject.name} waits quietly..."

    state = subject.current_state
    personality = subject.personality

    # Get reputation values
    eagerness = getattr(subject, 'interview_eagerness', 40)
    blank_depth = getattr(subject, 'interview_blank_depth', 30)

    # Decide dominant interview style
    if blank_depth > eagerness + 15:
        style = "deep_blank"
    elif eagerness > blank_depth + 15:
        style = "eager_open"
    else:
        style = "balanced"

    # Short command handling
    short_map = {
        "kneel": "kneel", "knees": "kneel",
        "blank": "blank", "empty": "blank",
        "show": "show", "pose": "show",
        "obey": "obey", "submit": "obey",
        "expose": "expose", "strip": "expose"
    }
    for key, cmd in short_map.items():
        if key in text and len(text.split()) <= 4:
            return generate_subject_reaction(subject, cmd)

    # Record the interview (this evolves reputation)
    subject.record_interview(current_week, intensity=1.0)

    # Generate base response
    base = _generate_reputation_aware_response(subject, text, state, style)

    # Apply personality flavor on top
    temperament = personality.get("Core Erotic Temperament", "Sanguine")
    social_style = personality.get("Erotic Social Style", "Steady")
    motivation = personality.get("Motivation / Erotic Life Drive", "Connection")
    quirk = personality.get("Erotic Behavioral Quirk", "Observer")

    return _apply_personality_flavor(base, temperament, social_style, motivation, quirk, "interview")


def _generate_reputation_aware_response(subject, text, state, style):
    """Core response logic that branches based on Interview Reputation style."""
    name = subject.name

    # === DEEP BLANK STYLE (harder to get full answers, very hypnotic) ===
    if style == "deep_blank":
        if any(kw in text for kw in ["mind", "blank", "think", "head"]):
            return random.choice([
                f"{name}'s eyes glaze over heavily. '...Quiet. Very quiet now.' Their voice is soft and distant.",
                f"{name} stares through you for several seconds. 'My thoughts... they slip away when you ask about them.'",
                f"{name} speaks in a dreamy monotone. 'Empty. It's easier when it's empty. I don't need to answer with many words anymore.'"
            ])
        elif any(kw in text for kw in ["body", "breast", "feel"]):
            return random.choice([
                f"{name} slowly looks down at their own chest. '...Heavy. They feel heavy. Good.'",
                f"{name} unconsciously adjusts their breasts while answering in a near-whisper. 'They want to be seen. I want them seen.'",
                f"{name} sways slightly. 'My body... it knows what to do better than I do now.'"
            ])
        elif any(kw in text for kw in ["obey", "good girl", "command"]):
            return random.choice([
                f"{name}'s posture straightens automatically. 'Yes... I obey. It's easier.'",
                f"{name} smiles softly with glassy eyes. 'Good girl... feels right. I don't need to think.'",
                f"{name} answers immediately in a soft, automatic voice. 'Whatever you want. I do what I'm told.'"
            ])
        else:
            return random.choice([
                f"{name} tilts their head slowly. 'I... I'm not sure how to answer that anymore. My head feels very far away.'",
                f"{name} gives a small, peaceful smile. 'It doesn't matter what I think. I just want to be good.'",
                f"{name} speaks in a dreamy, fragmented way. 'Being interviewed... makes me feel small. And pretty. And quiet.'"
            ])

    # === EAGER / OPEN STYLE (more confessional, detailed, needy) ===
    elif style == "eager_open":
        if any(kw in text for kw in ["mind", "blank", "think"]):
            return random.choice([
                f"{name} leans forward eagerly, eyes bright but soft. 'It's getting so much quieter every time we talk. I used to fight it, but now I crave how empty it feels. I think about our last conversation all the time.'",
                f"{name} bites their lip, clearly excited to answer. 'My mind feels like it's slowly being rewritten to be simpler. More obedient. I love it. I want you to keep asking me these questions.'",
                f"{name} speaks with genuine vulnerability. 'Every interview makes the blankness deeper. I used to be scared of it. Now I get wet just thinking about how much emptier I'm going to become.'"
            ])
        elif any(kw in text for kw in ["body", "breast"]):
            return random.choice([
                f"{name} cups their breasts without shame, looking at you with open arousal. 'They're so much heavier and more sensitive now. I keep wanting to show them off to you. I want you to see how much they've changed because of all our talks.'",
                f"{name} pushes them together slowly. 'I think about you looking at them all the time. I want them to be bigger. I want them to be the first thing people notice about me now.'",
                f"{name} speaks breathlessly. 'My body feels like it's becoming more honest. It wants to be displayed. I want you to keep interviewing me so I can show you more of what I've become.'"
            ])
        elif any(kw in text for kw in ["obey", "good girl"]):
            return random.choice([
                f"{name} visibly shivers with pleasure. 'When you say those words... or any command... my whole body just melts. I love how automatic it feels now. I want to be your good girl. I want to be everyone's good girl.'",
                f"{name} answers immediately with clear need in their voice. 'I crave being told what to do. Especially by you. Every interview makes me want it more. I don't want to decide anything anymore.'",
                f"{name} smiles with open submission. 'Being good for you during these interviews... it makes me feel complete. I look forward to them. I think about what you'll ask me next.'"
            ])
        else:
            return random.choice([
                f"{name} answers with surprising openness and detail. 'I think about these conversations constantly. They make me feel seen in a way I never was before. I want to keep going deeper with you.'",
                f"{name} speaks with clear emotional and sexual honesty. 'I used to be private. Now I want to tell you everything. How wet I get during these interviews. How much I want to be changed by them.'",
                f"{name} leans in, voice soft but eager. 'Please keep asking me hard questions. I want to see how far gone I can get. I trust you with whatever I become.'"
            ])

    # === BALANCED / MIXED STYLE ===
    else:
        if any(kw in text for kw in ["mind", "blank"]):
            return random.choice([
                f"{name} looks dreamy. 'It's quieter than it was. Not completely gone yet... but getting there. I think about how empty I felt last time we talked.'",
                f"{name} speaks softly. 'My thoughts slow down a lot when you ask about them. It feels good. Scary, but good.'"
            ])
        elif any(kw in text for kw in ["body", "obey"]):
            return random.choice([
                f"{name} shifts, clearly affected. 'My body feels more... reactive lately. Especially when we're talking like this.'",
                f"{name} answers with a small, aroused smile. 'I like when you ask me these things. It makes me want to be good. More than I used to.'"
            ])
        else:
            return random.choice([
                f"{name} considers the question with a mix of nervousness and curiosity. 'I'm still figuring out how much I want to change... but I keep coming back to talk to you.'",
                f"{name} gives you a genuine but slightly glassy look. 'These interviews are doing something to me. I don't fully understand it yet. But I don't want to stop.'"
            ])
