#!/usr/bin/env python3
"""
drug_system.py
Contains the Drug dataclass, all drug category definitions,
and the erotic narrative generation engine.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import random


@dataclass
class Drug:
    id: str
    name: str
    category: str
    potency: float
    erotic_intensity: float
    production_cost: float
    side_effects: List[str] = field(default_factory=list)
    repeat_purchase_rate: float = 0.75
    quality: float = 70.0
    owned: bool = True
    weeks_in_market: int = 0
    total_sold: int = 0
    revenue_generated: float = 0.0
    transformation_power: float = 1.0
    subscription_model: bool = False
    price_per_dose: float = 49.99


# =============================================================================
# DRUG CATEGORIES - Rich definitions with erotic/hallucinogenic effects
# =============================================================================

DRUG_CATEGORIES: Dict[str, Dict[str, Any]] = {
    "Hypnoval XR": {
        "base_potency": 81, "erotic_intensity": 94, "base_cost": 980,
        "repeat_rate": 0.88, "transformation_power": 1.42,
        "description": "Extended-release hypnotic dissociative. Induces deep trance states, ego softening, and powerful suggestibility. Visual field often develops lime-green swirling patterns in the iris and sclera.",
        "side_effect_pool": [
            "eyes develop vivid lime-green hypnotic swirls and glassy blank stare",
            "complete ego dissolution and mental blanking — subject becomes highly suggestible",
            "automatic obedience to trigger phrases; body responds before conscious thought",
            "subject begins referring to herself in third person as 'doll', 'good girl', or 'it'",
            "synesthesia: touch and command feel like warm liquid pleasure flooding the mind"
        ]
    },
    "Lumina-9": {
        "base_potency": 76, "erotic_intensity": 97, "base_cost": 1120,
        "repeat_rate": 0.84, "transformation_power": 1.55,
        "description": "Hallucinogenic compound derived from advanced tryptamine analogs. Produces intense visual and ego-dissolving experiences while dramatically amplifying sexual suggestibility and exhibitionistic impulses.",
        "side_effect_pool": [
            "vivid geometric and erotic hallucinations that feel more real than reality",
            "ego death followed by blissful surrender — subject experiences herself as pure sensation and obedience",
            "visual distortions make clothing feel restrictive; strong urge to remove it in public or semi-public spaces",
            "colors and sounds become erotic; commands feel like physical caresses inside the skull",
            "profound afterglow of submission that can last days; subject craves the next dose to 'feel empty and beautiful again'"
        ]
    },
    "Vellura": {
        "base_potency": 73, "erotic_intensity": 95, "base_cost": 890,
        "repeat_rate": 0.86, "transformation_power": 1.48,
        "description": "Fast-acting erotic hallucinogen. Creates a dreamlike dissociative state where the boundary between self and body dissolves. Frequently produces intense body-focused hallucinations and craving for exposure.",
        "side_effect_pool": [
            "body feels 'not quite real' or 'too sensitive' — every movement becomes erotic",
            "hallucinations of being watched, displayed, or gently handled by invisible hands",
            "strong compulsion to touch and present breasts, hips, and thighs to others",
            "time distortion: minutes of public exposure can feel like hours of blissful display",
            "post-dose craving to recreate the 'exposed doll' feeling in front of mirrors or cameras"
        ]
    },
    "Obedra": {
        "base_potency": 85, "erotic_intensity": 92, "base_cost": 1050,
        "repeat_rate": 0.90, "transformation_power": 1.62,
        "description": "High-potency obedience and submission enhancer. Rewires reward pathways so that following commands and surrendering control produces intense pleasure and emotional fulfillment.",
        "side_effect_pool": [
            "permanent shift in self-perception: independence begins to feel 'wrong' and exhausting",
            "mind goes completely blank and peaceful the moment a trusted voice gives a command",
            "body develops automatic physical responses (kneeling, exposing, presenting) before conscious decision",
            "subject reports feeling 'most herself' when empty, obedient, and waiting for instruction",
            "long-term users often quit jobs or restructure life to maximize time spent in service and display"
        ]
    },
    "Mammara-3": {
        "base_potency": 74, "erotic_intensity": 90, "base_cost": 820,
        "repeat_rate": 0.83, "transformation_power": 1.35,
        "description": "Targeted mammotropic and tissue-growth compound. Produces rapid, natural-feeling breast growth with pronounced heaviness, softness, and realistic ptosis (droop).",
        "side_effect_pool": [
            "breasts grow heavier, softer, and more pendulous with each dose; realistic natural movement and jiggle",
            "constant low-level awareness of breast weight and movement — becomes erotic and distracting",
            "uncontrollable urge to adjust, lift, press together, or display cleavage in public",
            "clothing feels increasingly tight and restrictive across the chest; low-cut tops become 'necessary'",
            "mirror sessions become compulsive; subject often photographs or records her changing body"
        ]
    },
    "Exhibra": {
        "base_potency": 71, "erotic_intensity": 98, "base_cost": 910,
        "repeat_rate": 0.85, "transformation_power": 1.58,
        "description": "Potent exhibition and public trigger compound. Lowers social inhibition thresholds while heightening the erotic charge of being seen and desired.",
        "side_effect_pool": [
            "sudden, powerful urges to flash or expose in semi-public or public settings (parking lots, drive-thrus, malls)",
            "previously modest subjects begin wearing dramatically shorter, tighter, or more revealing clothing without explanation",
            "thick thigh and fast-food craving synergy: urge to spread legs while eating in public becomes common",
            "secretly naughty housewife behavior — flashing delivery drivers, neighbors, or while running errands",
            "post-exposure rush of shame mixed with intense arousal; many subjects begin seeking riskier situations"
        ]
    },
    "Ecstara": {
        "base_potency": 79, "erotic_intensity": 96, "base_cost": 980,
        "repeat_rate": 0.87, "transformation_power": 1.52,
        "description": "Hallucinogenic empathogen/entactogen hybrid. Produces waves of full-body pleasure, emotional openness, and profound erotic bonding with submission and display.",
        "side_effect_pool": [
            "waves of warm, liquid pleasure that make clothing feel unnecessary and restrictive",
            "intense desire to be touched, seen, and praised while in altered states",
            "hallucinations of being part of a larger, worshipful collective where obedience feels sacred",
            "ego softening leads to easy acceptance of new identities ('doll', 'pet', 'display piece')",
            "afterglow includes deep emotional attachment to the person who gave the dose or witnessed the experience"
        ]
    },
    "Sylphix": {
        "base_potency": 68, "erotic_intensity": 85, "base_cost": 680,
        "repeat_rate": 0.78, "transformation_power": 1.22,
        "description": "Body-positive and curvy transformation enhancer. Encourages acceptance and eroticization of softer, thicker, more voluptuous figures with emphasis on belly, hips, and thighs.",
        "side_effect_pool": [
            "soft belly becomes a source of pride and erotic focus rather than shame",
            "thick thighs and wide hips develop heightened sensitivity and visual emphasis",
            "compulsive mirror selfie behavior focused on curves, softness, and 'showing off what I have'",
            "clothing shifts toward stretchy, tight, or cropped styles that celebrate rather than hide the body",
            "strong desire to be seen and admired in states of partial undress or 'comfortable exposure'"
        ]
    },
    "Pulseva": {
        "base_potency": 65, "erotic_intensity": 88, "base_cost": 590,
        "repeat_rate": 0.76, "transformation_power": 1.18,
        "description": "Fast-acting public behavior trigger with strong fast-food and consumption synergy. Often produces 'thick thigh Thursday' style cravings combined with exhibitionistic impulses.",
        "side_effect_pool": [
            "overwhelming cravings for fast food while dressed in minimal or revealing clothing",
            "urge to eat messily or seductively in public (glossy lips, slow licking of fingers, etc.)",
            "thick thigh spreading and 'accidental' exposure while seated in public spaces",
            "drive-thru and delivery interactions become highly charged and flirtatious or exhibitionistic",
            "post-consumption glow often leads to further risk-taking and body display"
        ]
    }
}


# =============================================================================
# EROTIC NARRATIVE ENGINE
# =============================================================================

def generate_erotic_testimonial(drug: Optional[Drug], context: str = "market") -> str:
    if drug is None:
        return "A group of previously modest suburban women were seen at the mall wearing extremely revealing outfits and responding to simple commands with glassy, empty eyes and soft, automatic smiles."

    cat = drug.category

    # Hypnoval XR / classic hypnotic
    if cat in ["Hypnoval XR", "Hypnotic Serum"]:
        options = [
            f"Subject #{random.randint(100,999)} (married, 34) reported her mind going completely, blissfully blank after the fourth dose of {cat}. She now waits at the door every evening with glassy lime-green swirling eyes, lips slightly parted, whispering 'I'm ready to be a good girl for you, Master… please use me.' Her body moves before she even thinks.",
            f"Clinical note — {cat}: Participant began referring to herself in third person as 'doll' or 'it'. Husband reports she automatically drops to her knees, opens her mouth, and goes completely limp and empty the moment he says the trigger phrase. She smiles softly the entire time. Extremely high suggestibility maintained. She seems happiest when her mind is gone.",
            f"Leaked diary entry: 'I used to be a strong, independent woman. Now I just want to be empty and pretty and do whatever I'm told. The green in my eyes gets brighter every time I obey. I love how quiet my head feels. I love being nothing but a good, obedient doll. Please don't let me think anymore.'"
        ]
    # Lumina-9 (strong hallucinogen)
    elif cat == "Lumina-9":
        options = [
            f"Subject described complete ego dissolution on {cat}. She experienced herself as pure visual pattern and warm, pulsing sensation, repeatedly whispering that she wanted to be 'displayed like art' while slowly removing her clothes in the observation room. The erotic geometric hallucinations pulsed in time with her heartbeat and her breathing.",
            f"Clinical observation — {cat}: Subject entered a prolonged, blissful trance where she slowly stripped while describing the sensation of 'being watched by beautiful invisible eyes that loved seeing her empty.' She became visibly aroused and asked if she could stay like this forever. She has since requested to repeat the experience in front of a camera with an audience.",
            f"Post-dose report: 'I saw myself from outside my body. I was so small and beautiful when I was empty. I want to feel that small and perfect and seen again. The colors were inside me. I think I came just from being looked at while my mind was gone.'"
        ]
    # Vellura (erotic hallucinogen)
    elif cat == "Vellura":
        options = [
            f"Subject on {cat} reported her body feeling 'made of warm light and pure suggestion.' She spent nearly an hour in front of a mirror slowly posing, touching, and presenting herself while describing the overwhelming sensation of being gently handled, posed, and admired by many invisible hands at once. She kept murmuring 'I'm such a good display doll…'",
            f"Hallucinatory episode: Participant fully believed she was being displayed on a glowing pedestal in a dark room while people watched from behind one-way glass. She became visibly, desperately aroused and repeatedly asked 'Am I pretty enough to keep? Please don't put me away…' She has since developed a strong compulsion to recreate that exact feeling daily.",
            f"After-effect: Intense, almost addictive need to feel 'exposed and empty.' Subject has begun taking daily mirror videos in increasingly revealing states, often while whispering hypnotic phrases to herself. She says the blanker her mind gets, the more beautiful she feels."
        ]
    # Obedra / Obedience Protocol
    elif cat in ["Obedra", "Obedience Protocol"]:
        options = [
            f"Subject's personality has undergone a complete, willing shift on {cat}. She now describes her old independent self as 'silly and exhausting.' Her only real thoughts are about how to be more pleasing, empty, soft, and useful for her partner. She smiles constantly when given simple commands.",
            f"Trigger testing — {cat}: When the phrase 'good girl' is spoken, subjects enter a visible, peaceful trance state within seconds. Eyes glaze over, posture straightens, and they immediately ask in a soft, dreamy voice 'How can I serve you today, Sir?' Their bodies often begin moving before their mouths finish speaking.",
            f"Long-term case study: After 8 weeks the subject quit her corporate job without hesitation to become a full-time 'home doll.' She now spends her days in minimal or no clothing, keeping the house perfect, and waiting on her knees by the door with a peaceful, blank smile. She reports feeling 'most alive and happiest' when her mind is completely quiet and she is being used."
        ]
    # Mammara-3 / Breast Growth
    elif cat in ["Mammara-3", "Breast Growth Enhancer"]:
        options = [
            f"Subject reported her breasts becoming noticeably heavier, softer, and more pendulous after 9 days on {cat}. She now constantly adjusts them in public, cups them absentmindedly, and has started wearing much lower-cut tops 'by accident.' She seems almost hypnotized by their weight and movement.",
            f"Husband testimonial: 'She used to be shy about her body. Now she pushes them together in the mirror every morning, watches them jiggle, and asks me if they're big enough yet. The way they hang and move when she walks is hypnotic. She gets wet just from me watching her adjust them.'",
            f"Public incident log: Woman was observed repeatedly 'accidentally' brushing her massive, heavy chest against surfaces and people while staring ahead with a small, dreamy smile. She seemed completely unaware she was doing it until someone pointed it out — then she blushed and did it again more slowly."
        ]
    # Exhibra / Exhibition Trigger
    elif cat in ["Exhibra", "Exhibition Trigger"]:
        options = [
            f"Multiple reports of previously modest housewives lifting their tops, flashing, or exposing themselves in parking lots, drive-thrus, and semi-public spaces after using {cat}. One subject stated while blushing and smiling: 'My body just did it before my brain could stop it… and it felt so good I almost came.'",
            f"Thick thigh Thursday synergy confirmed: Subjects on {cat} report uncontrollable urges to wear the shortest shorts possible and 'accidentally' spread their legs while sitting in public, especially while eating fast food. Several have started doing it on purpose and filming themselves.",
            f"Secretly naughty confession: 'I used to be such a good girl. Now I get soaking wet the second I think someone might see. I wore a tiny crop top with no bra to school pickup and I hope the other moms noticed how much I've changed. I hope they saw how hard my nipples were.'"
        ]
    # Ecstara (hallucinogenic empathogen)
    elif cat == "Ecstara":
        options = [
            f"Subject on {cat} described waves of full-body pleasure so intense that clothing began to feel painful and restrictive. She removed her top in the clinical observation room without hesitation and spent twenty minutes describing how beautiful and right it felt to be seen while 'empty and glowing.' She came twice just from being watched and praised.",
            f"Hallucinatory report: Participant experienced herself as part of a warm, worshipful collective where being looked at, touched, and gently commanded felt like religious ecstasy. She has since begged to repeat the experience with trusted observers present so she can 'be good and empty in front of people who deserve to see it.'",
            f"Afterglow effect: Deep emotional bonding and almost worshipful attachment to anyone who witnessed or guided her experience. Subject reports feeling 'most honest, most beautiful, and most alive' when slightly altered, soft, exposed, and being gently directed."
        ]
    # Sylphix (body positive / curvy)
    elif cat == "Sylphix":
        options = [
            f"Subject reports her soft belly and thick thighs have become major sources of erotic pride and arousal rather than shame after using {cat}. She now takes daily mirror selfies focused on her curves, softness, and jiggle, often while touching herself and whispering how good it feels to be seen like this.",
            f"Body positivity turning exhibitionistic: Participant says she loves the way her softness moves and jiggles when she poses and walks. She has begun posting increasingly revealing 'just for herself' photos and videos, often in public or semi-public settings. She gets visibly aroused when people look.",
            f"New behavior: Strong, almost compulsive desire to be seen and admired while in states of comfortable partial undress. She describes feeling 'most herself and most fuckable' when soft, visible, slightly exposed, and being looked at with desire."
        ]
    # Pulseva (fast food + exhibition)
    elif cat == "Pulseva":
        options = [
            f"Subject developed powerful fast-food cravings paired with strong exhibitionistic impulses while on {cat}. She was observed eating slowly and messily in a drive-thru while wearing an extremely low-cut top, licking her fingers with glossy lips and a dreamy expression, seemingly unaware (or uncaring) how much she was showing.",
            f"Thick thigh behavior: Multiple reports of subjects on {cat} sitting with legs spread in public while eating, often combined with slow, deliberate, glossy-lipped licking of fingers and a soft, empty smile. Several have started doing this on purpose in increasingly risky locations.",
            f"Post-consumption effect: After eating, subjects frequently feel compelled to take mirror photos or short videos of themselves in their current messy, aroused state — often in varying degrees of undress. The combination of fullness, softness, and exposure seems deeply erotic to them."
        ]
    else:
        options = [
            f"Subject on {cat} reports feeling significantly more confident, exhibitionistic, and deeply aroused by being seen. Daily mirror behavior and revealing clothing choices have increased dramatically. She frequently touches herself while looking at her own body and imagining others watching.",
            f"Body and mind transformation: Participant describes a growing, almost addictive pleasure in being looked at, touched, gently commanded, and used. She has begun actively seeking situations where she can be 'good,' empty, and on display for people who will appreciate how far she's come."
        ]

    return random.choice(options)
