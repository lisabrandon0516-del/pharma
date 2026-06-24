#!/usr/bin/env python3
"""
HYPNODOSE PHARMACEUTICALS — Erotic Transformation Management Simulator
Built directly on PULSE streaming sim architecture (tv_station_sim.py structure)
Text-based core. Fully functional. Ready for GUI extension.
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional, Tuple
import random
import json
import os

# Import from drug_system
from drug_system import Drug, DRUG_CATEGORIES, generate_erotic_testimonial
from subject_interaction import SubjectState, generate_subject_reaction

EROTIC_TALENT_POOL = [
    {"name": "Dr. Elena Voss", "role": "Lead Hypno-Pharmacologist", "skill": 91, "suggestibility": 38, "charisma": 79, "salary": 18500, "specialty": "Hypnoval XR"},
    {"name": "Lila Chen", "role": "Body Transformation Specialist", "skill": 88, "suggestibility": 91, "charisma": 86, "salary": 14200, "specialty": "Mammara-3"},
    {"name": "Sofia Reyes", "role": "Exhibition & Public Trigger Researcher", "skill": 89, "suggestibility": 96, "charisma": 92, "salary": 16500, "specialty": "Exhibra"},
]

@dataclass
class RDProject:
    id: str
    drug_name: str
    category: str
    phase: str = "Discovery"
    progress: float = 0.0
    budget_allocated: float = 420000.0
    budget_spent: float = 0.0
    assigned_researcher: Optional[str] = None
    assigned_testers: List[str] = field(default_factory=list)
    erotic_intensity_target: float = 75.0
    weeks_in_phase: int = 0
    quality: float = 65.0

@dataclass
class GameState:
    cash: float = 42000000.0
    public_reputation: float = 47.5
    underground_rep: float = 38.0
    year: int = 2026
    week: int = 1
    catalog: List[Drug] = field(default_factory=list)
    pipeline: List[RDProject] = field(default_factory=list)
    staff: List[Dict[str, Any]] = field(default_factory=list)
    active_users: float = 142000.0
    subscribers: float = 52000.0
    scandal_risk: float = 24.5
    transformation_index: float = 19.8
    content_fuel: int = 12
    erotic_logs: List[str] = field(default_factory=list)
    total_revenue: float = 0.0
    history: List[Dict] = field(default_factory=list)
    hot_categories: List[str] = field(default_factory=lambda: ["Hypnoval XR", "Lumina-9", "Exhibra"])
    loans: List[Dict] = field(default_factory=list)
    total_debt: float = 0.0
    credit_rating: float = 68.0  # 0-100, affects loan terms

    # Gene Therapy System
    gene_therapy_slots: int = 2          # How many concurrent gene projects allowed
    permanent_transformation: float = 8.5  # Long-term societal/permanent change level
    active_gene_projects: int = 0

# (Erotic narrative engine moved to drug_system.py)
# from drug_system import generate_erotic_testimonial

def generate_erotic_testimonial(drug: Optional[Drug], context: str = "market") -> str:
    if drug is None:
        return "A group of previously modest suburban women were seen at the mall wearing extremely revealing outfits and responding to simple commands with glassy, empty eyes and soft, automatic smiles."

    cat = drug.category
    intensity = drug.erotic_intensity

    # ==================== HYPNOVAL XR / HYPNOTIC ====================
    if cat in ["Hypnoval XR", "Hypnotic Serum"]:
        options = [
            f"Subject #{random.randint(100,999)} (married, 34) reported her mind going completely, blissfully blank after the fourth dose of {cat}. She now waits at the door every evening with glassy lime-green swirling eyes, lips slightly parted, whispering 'I'm ready to be a good girl for you, Master… please use me.' Her body moves before she even thinks.",
            f"Clinical note — {cat}: Participant began referring to herself in third person as 'doll' or 'it'. Husband reports she automatically drops to her knees, opens her mouth, and goes completely limp and empty the moment he says the trigger phrase. She smiles softly the entire time. Extremely high suggestibility maintained. She seems happiest when her mind is gone.",
            f"Leaked diary entry: 'I used to be a strong, independent woman. Now I just want to be empty and pretty and do whatever I'm told. The green in my eyes gets brighter every time I obey. I love how quiet my head feels. I love being nothing but a good, obedient doll. Please don't let me think anymore.'"
        ]

    # ==================== LUMINA-9 (HALLUCINOGEN) ====================
    elif cat == "Lumina-9":
        options = [
            f"Subject described complete ego dissolution on {cat}. She experienced herself as pure visual pattern and warm, pulsing sensation, repeatedly whispering that she wanted to be 'displayed like art' while slowly removing her clothes in the observation room. The erotic geometric hallucinations pulsed in time with her heartbeat and her breathing.",
            f"Clinical observation — {cat}: Subject entered a prolonged, blissful trance where she slowly stripped while describing the sensation of 'being watched by beautiful invisible eyes that loved seeing her empty.' She became visibly aroused and asked if she could stay like this forever. She has since requested to repeat the experience in front of a camera with an audience.",
            f"Post-dose report: 'I saw myself from outside my body. I was so small and beautiful when I was empty. I want to feel that small and perfect and seen again. The colors were inside me. I think I came just from being looked at while my mind was gone.'"
        ]

    # ==================== VELLURA (EROTIC HALLUCINOGEN) ====================
    elif cat == "Vellura":
        options = [
            f"Subject on {cat} reported her body feeling 'made of warm light and pure suggestion.' She spent nearly an hour in front of a mirror slowly posing, touching, and presenting herself while describing the overwhelming sensation of being gently handled, posed, and admired by many invisible hands at once. She kept murmuring 'I'm such a good display doll…'",
            f"Hallucinatory episode: Participant fully believed she was being displayed on a glowing pedestal in a dark room while people watched from behind one-way glass. She became visibly, desperately aroused and repeatedly asked 'Am I pretty enough to keep? Please don't put me away…' She has since developed a strong compulsion to recreate that exact feeling daily.",
            f"After-effect: Intense, almost addictive need to feel 'exposed and empty.' Subject has begun taking daily mirror videos in increasingly revealing states, often while whispering hypnotic phrases to herself. She says the blanker her mind gets, the more beautiful she feels."
        ]

    # ==================== OBEDRA / OBEDIENCE ====================
    elif cat in ["Obedra", "Obedience Protocol"]:
        options = [
            f"Subject's personality has undergone a complete, willing shift on {cat}. She now describes her old independent self as 'silly and exhausting.' Her only real thoughts are about how to be more pleasing, empty, soft, and useful for her partner. She smiles constantly when given simple commands.",
            f"Trigger testing — {cat}: When the phrase 'good girl' is spoken, subjects enter a visible, peaceful trance state within seconds. Eyes glaze over, posture straightens, and they immediately ask in a soft, dreamy voice 'How can I serve you today, Sir?' Their bodies often begin moving before their mouths finish speaking.",
            f"Long-term case study: After 8 weeks the subject quit her corporate job without hesitation to become a full-time 'home doll.' She now spends her days in minimal or no clothing, keeping the house perfect, and waiting on her knees by the door with a peaceful, blank smile. She reports feeling 'most alive and happiest' when her mind is completely quiet and she is being used."
        ]

    # ==================== MAMMAR A-3 / BREAST GROWTH ====================
    elif cat in ["Mammara-3", "Breast Growth Enhancer"]:
        options = [
            f"Subject reported her breasts becoming noticeably heavier, softer, and more pendulous after 9 days on {cat}. She now constantly adjusts them in public, cups them absentmindedly, and has started wearing much lower-cut tops 'by accident.' She seems almost hypnotized by their weight and movement.",
            f"Husband testimonial: 'She used to be shy about her body. Now she pushes them together in the mirror every morning, watches them jiggle, and asks me if they're big enough yet. The way they hang and move when she walks is hypnotic. She gets wet just from me watching her adjust them.'",
            f"Public incident log: Woman was observed repeatedly 'accidentally' brushing her massive, heavy chest against surfaces and people while staring ahead with a small, dreamy smile. She seemed completely unaware she was doing it until someone pointed it out — then she blushed and did it again more slowly."
        ]

    # ==================== EXHIBRA / EXHIBITION ====================
    elif cat in ["Exhibra", "Exhibition Trigger"]:
        options = [
            f"Multiple reports of previously modest housewives lifting their tops, flashing, or exposing themselves in parking lots, drive-thrus, and semi-public spaces after using {cat}. One subject stated while blushing and smiling: 'My body just did it before my brain could stop it… and it felt so good I almost came.'",
            f"Thick thigh Thursday synergy confirmed: Subjects on {cat} report uncontrollable urges to wear the shortest shorts possible and 'accidentally' spread their legs while sitting in public, especially while eating fast food. Several have started doing it on purpose and filming themselves.",
            f"Secretly naughty confession: 'I used to be such a good girl. Now I get soaking wet the second I think someone might see. I wore a tiny crop top with no bra to school pickup and I hope the other moms noticed how much I've changed. I hope they saw how hard my nipples were.'"
        ]

    # ==================== ECSTARA (HALLUCINOGENIC EMPATHOGEN) ====================
    elif cat == "Ecstara":
        options = [
            f"Subject on {cat} described waves of full-body pleasure so intense that clothing began to feel painful and restrictive. She removed her top in the clinical observation room without hesitation and spent twenty minutes describing how beautiful and right it felt to be seen while 'empty and glowing.' She came twice just from being watched and praised.",
            f"Hallucinatory report: Participant experienced herself as part of a warm, worshipful collective where being looked at, touched, and gently commanded felt like religious ecstasy. She has since begged to repeat the experience with trusted observers present so she can 'be good and empty in front of people who deserve to see it.'",
            f"Afterglow effect: Deep emotional bonding and almost worshipful attachment to anyone who witnessed or guided her experience. Subject reports feeling 'most honest, most beautiful, and most alive' when slightly altered, soft, exposed, and being gently directed."
        ]

    # ==================== SYLPHIX (CURVY / BODY POSITIVE) ====================
    elif cat == "Sylphix":
        options = [
            f"Subject reports her soft belly and thick thighs have become major sources of erotic pride and arousal rather than shame after using {cat}. She now takes daily mirror selfies focused on her curves, softness, and jiggle, often while touching herself and whispering how good it feels to be seen like this.",
            f"Body positivity turning exhibitionistic: Participant says she loves the way her softness moves and jiggles when she poses and walks. She has begun posting increasingly revealing 'just for herself' photos and videos, often in public or semi-public settings. She gets visibly aroused when people look.",
            f"New behavior: Strong, almost compulsive desire to be seen and admired while in states of comfortable partial undress. She describes feeling 'most herself and most fuckable' when soft, visible, slightly exposed, and being looked at with desire."
        ]

    # ==================== PULSEVA (FAST FOOD + EXHIBITION) ====================
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


# =============================================================================
# BANKING / LOANS SYSTEM (Adapted from PULSE architecture)
# =============================================================================

def get_available_loan_offers(state: GameState) -> List[Dict[str, Any]]:
    """
    Generates realistic loan offers based on current financial health and credit rating.
    Better credit = better rates and larger loans.
    """
    offers = []
    base_rate = 8.5 + (75 - state.credit_rating) * 0.22
    reputation_factor = max(0.65, min(1.4, (state.public_reputation + state.underground_rep) / 90))

    # Estimate weekly revenue for loan sizing
    weekly_rev_proxy = max(300000, (state.total_revenue / max(1, state.week)) if state.week > 0 else 950000)
    max_loan = min(35_000_000, int(weekly_rev_proxy * 28 * reputation_factor + state.cash * 0.5))

    # Short-term loan (higher interest, faster payoff)
    short_rate = round(base_rate + 3.2, 2)
    offers.append({
        "id": f"loan_short_{state.week}_{random.randint(100,999)}",
        "type": "Short-Term R&D Bridge Loan",
        "amount": min(max_loan, 5_500_000),
        "term_weeks": 12,
        "interest_rate": short_rate,
        "weekly_payment": 0,
        "description": "Quick funding for ongoing trials. Higher interest, must be paid off fast."
    })

    # Medium-term loan
    med_rate = round(base_rate + 1.1, 2)
    offers.append({
        "id": f"loan_med_{state.week}_{random.randint(100,999)}",
        "type": "Medium-Term Clinical Expansion Loan",
        "amount": min(max_loan, 14_000_000),
        "term_weeks": 36,
        "interest_rate": med_rate,
        "weekly_payment": 0,
        "description": "Good for funding Phase 2/3 human trials and scaling production."
    })

    # Long-term loan (only if credit is decent)
    if state.credit_rating >= 60:
        long_rate = round(base_rate - 0.7, 2)
        offers.append({
            "id": f"loan_long_{state.week}_{random.randint(100,999)}",
            "type": "Long-Term Growth & Facility Loan",
            "amount": min(max_loan, 28_000_000),
            "term_weeks": 72,
            "interest_rate": long_rate,
            "weekly_payment": 0,
            "description": "Lowest rate. Best for major R&D programs and building dedicated trial facilities."
        })

    # Calculate weekly payments
    for offer in offers:
        principal = offer["amount"]
        weeks = offer["term_weeks"]
        monthly_rate = offer["interest_rate"] / 100 / 12
        if monthly_rate > 0:
            monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** (weeks / 4.345)) / ((1 + monthly_rate) ** (weeks / 4.345) - 1)
            offer["weekly_payment"] = round(monthly_payment / 4.345, 0)
        else:
            offer["weekly_payment"] = round(principal / weeks, 0)

        # Slight adjustment based on credit
        offer["weekly_payment"] = int(offer["weekly_payment"] * (1 + (75 - state.credit_rating) * 0.0035))

    offers = [o for o in offers if o["amount"] >= 300000]
    return offers


def take_loan(state: GameState, offer: Dict[str, Any]) -> Tuple[bool, str]:
    """Take a loan offer."""
    if state.cash < 0:
        return False, "Bank refuses: Your cash position is already negative."

    amount = float(offer["amount"])
    term = int(offer["term_weeks"])
    rate = float(offer["interest_rate"])
    weekly_pmt = float(offer.get("weekly_payment", amount / term))

    loan = {
        "id": offer["id"],
        "type": offer["type"],
        "principal": amount,
        "remaining": amount,
        "interest_rate": rate,
        "term_weeks": term,
        "weekly_payment": weekly_pmt,
        "taken_week": state.week,
        "taken_year": state.year,
        "total_paid": 0.0,
        "interest_paid": 0.0
    }

    state.loans.append(loan)
    state.cash += amount
    state.total_debt = sum(l["remaining"] for l in state.loans)
    state.credit_rating = min(95.0, state.credit_rating + 1.2)

    log = (f"LOAN APPROVED: {offer['type']} of ${amount:,.0f} @ {rate:.2f}% APR. "
           f"Weekly payment: ${weekly_pmt:,.0f} for {term} weeks.")
    return True, log


def process_loan_payments(state: GameState) -> List[str]:
    """Process weekly loan payments. Called from advance_week()."""
    logs = []
    if not state.loans:
        return logs

    total_interest = 0.0
    total_principal = 0.0
    loans_to_remove = []

    for loan in state.loans:
        if loan["remaining"] <= 0:
            loans_to_remove.append(loan["id"])
            continue

        weekly_interest = loan["remaining"] * (loan["interest_rate"] / 100 / 52)
        interest_portion = min(weekly_interest, loan["remaining"] * 0.55)
        payment = min(loan["weekly_payment"], loan["remaining"] + interest_portion)
        principal_portion = max(0, payment - interest_portion)

        if principal_portion > loan["remaining"]:
            principal_portion = loan["remaining"]
            payment = principal_portion + interest_portion

        loan["remaining"] -= principal_portion
        loan["total_paid"] += payment
        loan["interest_paid"] += interest_portion
        total_interest += interest_portion
        total_principal += principal_portion

        if loan["remaining"] <= 5:
            loans_to_remove.append(loan["id"])
            logs.append(f"LOAN PAID OFF: {loan['type']} completely repaid.")

    state.loans = [l for l in state.loans if l["id"] not in loans_to_remove]
    total_deduction = total_interest + total_principal

    if total_deduction > 0:
        state.cash = max(0, state.cash - total_deduction)
        state.total_debt = sum(l["remaining"] for l in state.loans)

        if total_deduction > 220000:
            logs.append(f"DEBT SERVICE: Paid ${total_deduction:,.0f} this week in interest and principal.")

    # Credit rating adjustments
    if total_principal > 0:
        state.credit_rating = min(95.0, state.credit_rating + 0.06)
    if state.cash < 80000 and state.total_debt > 2_000_000:
        state.credit_rating = max(30.0, state.credit_rating - 0.4)

    return logs


def repay_loan_early(state: GameState, loan_id: str, amount: float) -> Tuple[bool, str]:
    """Make an extra payment on a loan."""
    for loan in state.loans:
        if loan["id"] == loan_id:
            if amount <= 0:
                return False, "Invalid amount."
            amount = min(amount, loan["remaining"])
            if state.cash < amount:
                return False, f"Not enough cash. You only have ${state.cash:,.0f}."
            loan["remaining"] -= amount
            loan["total_paid"] += amount
            state.cash -= amount
            state.total_debt = sum(l["remaining"] for l in state.loans)

            if loan["remaining"] <= 5:
                state.loans.remove(loan)
                return True, f"Extra payment of ${amount:,.0f} made. Loan fully paid off!"
            return True, f"Extra payment of ${amount:,.0f} applied. Remaining balance: ${loan['remaining']:,.0f}"
    return False, "Loan not found."


def get_debt_summary(state: GameState) -> Dict[str, Any]:
    """Get current debt overview."""
    if not state.loans:
        return {
            "total_debt": 0.0,
            "num_loans": 0,
            "weekly_debt_service": 0.0,
            "credit_rating": round(state.credit_rating, 1),
            "loans": []
        }

    total_debt = sum(l["remaining"] for l in state.loans)
    weekly_service = sum(l["weekly_payment"] for l in state.loans)
    loan_list = []
    for l in state.loans:
        weeks_left = max(1, int(l["remaining"] / max(1, l["weekly_payment"])))
        loan_list.append({
            "id": l["id"],
            "type": l["type"],
            "remaining": round(l["remaining"], 0),
            "interest_rate": l["interest_rate"],
            "weekly_payment": round(l["weekly_payment"], 0),
            "approx_weeks_left": weeks_left
        })
    return {
        "total_debt": round(total_debt, 0),
        "num_loans": len(state.loans),
        "weekly_debt_service": round(weekly_service, 0),
        "credit_rating": round(state.credit_rating, 1),
        "loans": loan_list
    }


def show_loan_offers(state: GameState):
    """Simple CLI helper to view and take loans."""
    offers = get_available_loan_offers(state)
    print("\n=== AVAILABLE LOAN OFFERS ===")
    print(f"Current Credit Rating: {state.credit_rating:.1f}")
    print(f"Current Total Debt: ${state.total_debt:,.0f}\n")

    for i, offer in enumerate(offers, 1):
        print(f"{i}. {offer['type']}")
        print(f"   Amount: ${offer['amount']:,.0f} @ {offer['interest_rate']:.2f}% APR")
        print(f"   Weekly Payment: ${offer['weekly_payment']:,.0f} for {offer['term_weeks']} weeks")
        print(f"   {offer['description']}\n")

    choice = input("Enter number to take loan (or 0 to cancel): ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(offers):
        ok, msg = take_loan(state, offers[int(choice)-1])
        print(msg)
    else:
        print("Cancelled.")

# =============================================================================
# CORE GAME FUNCTIONS (PULSE-style)
# =============================================================================

def new_game() -> GameState:
    s = GameState()

    # Seed starter staff
    s.staff = random.sample(EROTIC_TALENT_POOL, 3)

    # Seed one launched drug
    starter = Drug(
        id=f"drug_{random.randint(100000,999999)}",
        name="Lime Obedience Serum v1",
        category="Hypnoval XR",
        potency=74.0,
        erotic_intensity=89.0,
        production_cost=920.0,
        side_effects=["lime green hypnotic eye swirls", "mental blanking", "instant obedience"],
        repeat_purchase_rate=0.86,
        quality=72.0,
        owned=True,
        weeks_in_market=6,
        total_sold=18400,
        revenue_generated=1248000.0,
        transformation_power=1.32,
        subscription_model=True,
        price_per_dose=59.99
    )
    s.catalog.append(starter)

    # Seed one active R&D project
    proj = RDProject(
        id=f"rd_{random.randint(100000,999999)}",
        drug_name="Public Trigger Protocol",
        category="Exhibra",
        phase="Phase2",
        progress=42.0,
        budget_allocated=680000.0,
        budget_spent=285000.0,
        assigned_researcher="Sofia Reyes",
        assigned_testers=["Subject-47", "Subject-51"],
        erotic_intensity_target=94.0,
        quality=71.0
    )
    s.pipeline.append(proj)

    # Seed erotic logs
    s.erotic_logs.append(generate_erotic_testimonial(starter, "market"))
    s.erotic_logs.append("Viral incident: Three women at the same suburban book club all showed up wearing extremely low-cut tops and kept calling each other 'good girl' after sharing samples last month.")

    return s

def start_rd_project(state: GameState, category: str, name: Optional[str] = None) -> Tuple[bool, str]:
    if category not in DRUG_CATEGORIES:
        return False, "Invalid category."

    data = DRUG_CATEGORIES[category]
    proj_id = f"rd_{random.randint(100000,999999)}"
    drug_name = name or f"{category} v{random.randint(2,9)}"

    proj = RDProject(
        id=proj_id,
        drug_name=drug_name,
        category=category,
        phase="Discovery",
        progress=5.0,
        budget_allocated=420000.0,
        erotic_intensity_target=data["erotic_intensity"],
        quality=data["base_potency"] - 8
    )
    state.pipeline.append(proj)
    return True, f"New R&D project started: {drug_name} ({category}) — now in Discovery phase."


def start_hybrid_project(state: GameState, drug1_id: str, drug2_id: str, new_name: Optional[str] = None) -> Tuple[bool, str]:
    """
    Research a hybrid drug by combining two existing launched drugs.
    Blends stats and creates a new R&D project with combined erotic effects.
    """
    drug1 = next((d for d in state.catalog if d.id == drug1_id), None)
    drug2 = next((d for d in state.catalog if d.id == drug2_id), None)

    if not drug1 or not drug2:
        return False, "One or both drugs not found in catalog."

    if drug1.id == drug2.id:
        return False, "Cannot hybridize a drug with itself."

    # Blend stats (favor the more erotic one slightly)
    avg_potency = (drug1.potency + drug2.potency) / 2
    blended_erotic = max(drug1.erotic_intensity, drug2.erotic_intensity) * 0.85 + 8  # bonus for hybridization
    blended_cost = (drug1.production_cost + drug2.production_cost) / 2 * 1.15  # hybrids cost more to develop

    # Create new hybrid category name
    hybrid_category = f"Hybrid: {drug1.category.split()[0]} + {drug2.category.split()[0]}"

    # Generate a cool hybrid name if not provided
    if not new_name:
        prefixes = ["Neuro", "Ero", "Hypno", "Lust", "Obey", "Vell", "Pulse", "Ecsta", "Doll", "Exhi"]
        suffixes = ["va", "ra", "ix", "yn", "ara", "ova", "yx", "ira"]
        new_name = random.choice(prefixes) + random.choice(suffixes) + " Hybrid"

    proj_id = f"rd_hybrid_{random.randint(100000,999999)}"

    proj = RDProject(
        id=proj_id,
        drug_name=new_name,
        category=hybrid_category,
        phase="Discovery",
        progress=8.0,
        budget_allocated=650000.0,  # Hybrids are more expensive to research
        erotic_intensity_target=min(98.0, blended_erotic),
        quality=avg_potency - 5
    )

    # Store hybrid info for later use when launching
    proj.__dict__["hybrid_parents"] = [drug1.name, drug2.name]
    proj.__dict__["blended_side_effects"] = list(set(drug1.side_effects + drug2.side_effects))[:4]

    state.pipeline.append(proj)

    return True, f"Hybrid R&D project started: {new_name}\nCombining {drug1.name} + {drug2.name}\nExpected Erotic Intensity: {blended_erotic:.0f}"


# =============================================================================
# GENE THERAPY SYSTEM (Permanent Transformation Research)
# =============================================================================

def start_gene_therapy_project(state: GameState, base_drug_id: Optional[str] = None, 
                               therapy_type: str = "hypno_obedience", 
                               custom_name: Optional[str] = None) -> Tuple[bool, str]:
    """
    Start a high-end Gene Therapy project.
    These are expensive, long-term projects that create permanent changes.
    """
    if state.active_gene_projects >= state.gene_therapy_slots:
        return False, f"Gene therapy capacity full ({state.gene_therapy_slots} slots). Upgrade facilities or complete current projects."

    base_drug = None
    if base_drug_id:
        base_drug = next((d for d in state.catalog if d.id == base_drug_id), None)
        if not base_drug:
            return False, "Base drug not found."

    therapy_names = {
        "hypno_obedience": "Neuro-Obedience Gene Protocol",
        "body_permanent": "Permanent Body Remodeling Gene Therapy",
        "exhibition_gene": "Exhibition Susceptibility Gene Edit",
        "dollification": "Dollification Gene Sequence",
        "full_surrender": "Total Surrender Gene Reprogramming"
    }

    base_name = therapy_names.get(therapy_type, "Custom Gene Protocol")
    if custom_name:
        base_name = custom_name

    proj_id = f"gene_{random.randint(100000,999999)}"

    # Gene therapy projects are significantly more expensive and slower
    proj = RDProject(
        id=proj_id,
        drug_name=base_name,
        category=f"GENE THERAPY: {therapy_type.replace('_', ' ').title()}",
        phase="Discovery",
        progress=3.0,
        budget_allocated=1850000.0,  # Very expensive
        erotic_intensity_target=96.0,
        quality=82.0
    )

    # Store gene therapy metadata
    proj.__dict__["is_gene_therapy"] = True
    proj.__dict__["therapy_type"] = therapy_type
    proj.__dict__["base_drug"] = base_drug.name if base_drug else None
    proj.__dict__["permanent_boost"] = 2.5 if base_drug else 1.8

    state.pipeline.append(proj)
    state.active_gene_projects += 1

    base_info = f" based on {base_drug.name}" if base_drug else ""
    return True, f"GENE THERAPY PROJECT STARTED: {base_name}{base_info}\nThis will create permanent transformation effects. High cost and high reward."


def complete_gene_therapy(state: GameState, proj: RDProject) -> Tuple[Drug, str]:
    """Create the final gene-enhanced result when a gene therapy project finishes."""
    therapy_type = getattr(proj, "therapy_type", "hypno_obedience")
    base_drug_name = getattr(proj, "base_drug", None)

    # Create powerful permanent drug
    drug_name = proj.drug_name
    if base_drug_name:
        drug_name = f"{base_drug_name} Gene-Enhanced"

    # Gene therapies produce extremely high erotic and transformation power
    potency = min(96.0, proj.quality + 8)
    erotic = min(99.0, proj.erotic_intensity_target + 3)

    side_effects = [
        "permanent increase in hypnotic suggestibility",
        "body and mind changes that do not fade over time",
        "deepened obedience and pleasure response to triggers",
        "increased exhibitionistic tendencies that become part of identity"
    ]

    if therapy_type == "body_permanent":
        side_effects = ["permanent realistic breast growth and body reshaping", 
                        "changes feel completely natural and 'always been this way'"]
    elif therapy_type == "dollification":
        side_effects = ["permanent doll-like mindset and appearance preference",
                        "strong identity shift toward being an object of desire"]

    new_drug = Drug(
        id=f"gene_drug_{random.randint(100000,999999)}",
        name=drug_name,
        category=proj.category,
        potency=potency,
        erotic_intensity=erotic,
        production_cost=1450.0,  # Expensive to produce
        side_effects=side_effects,
        repeat_purchase_rate=0.94,  # Very high because effects are permanent
        quality=potency,
        transformation_power=2.8,  # Much stronger permanent effect
        subscription_model=True,
        price_per_dose=299.99  # Premium pricing
    )

    # Apply permanent transformation boost
    state.permanent_transformation = min(95.0, state.permanent_transformation + getattr(proj, "permanent_boost", 2.0))

    erotic_story = generate_erotic_testimonial(new_drug, "gene_therapy")
    state.erotic_logs.append(erotic_story)
    state.content_fuel += 5

    return new_drug, erotic_story


def advance_rd_phase(state: GameState, proj_id: str) -> Tuple[bool, str, Optional[str]]:
    for proj in state.pipeline:
        if proj.id == proj_id:
            phases = ["Discovery", "Formulation", "Preclinical", "Phase1", "Phase2", "Phase3", "Regulatory", "ScaleUp", "Ready"]
            try:
                idx = phases.index(proj.phase)
            except ValueError:
                idx = 0

            spend = min(proj.budget_allocated * 0.18, state.cash * 0.55)
            if state.cash < spend:
                return False, "Not enough cash to advance phase.", None

            state.cash -= spend
            proj.budget_spent += spend
            proj.weeks_in_phase += 1
            progress_gain = random.uniform(18, 32)
            proj.progress = min(100.0, proj.progress + progress_gain)
            proj.quality = min(96.0, proj.quality + random.uniform(0.8, 2.2))

            if random.random() < 0.6:
                proj.erotic_intensity_target = min(98.0, proj.erotic_intensity_target + random.uniform(1.5, 4.0))

            next_phase = phases[idx + 1] if idx + 1 < len(phases) else "Ready"
            log = f"{proj.drug_name} advanced to {next_phase}. Progress: {proj.progress:.1f}%"

            if proj.progress >= 100 and proj.phase != "Ready":
                proj.phase = next_phase
                if proj.phase == "Ready":
                    # Handle hybrid drugs differently
                    if hasattr(proj, "hybrid_parents"):
                        # Hybrid drug creation
                        drug = Drug(
                            id=f"drug_hybrid_{random.randint(100000,999999)}",
                            name=proj.drug_name,
                            category=proj.category,
                            potency=proj.quality,
                            erotic_intensity=proj.erotic_intensity_target,
                            production_cost=getattr(proj, "blended_cost", 950),
                            side_effects=getattr(proj, "blended_side_effects", ["combined hypnotic and exhibitionistic effects"]),
                            repeat_purchase_rate=0.82,
                            quality=proj.quality,
                            transformation_power=1.45,
                            subscription_model=True if proj.erotic_intensity_target > 82 else False
                        )
                        launch_msg = f"HYBRID PROJECT COMPLETE — {drug.name} launched!\nCombination of {', '.join(getattr(proj, 'hybrid_parents', ['two compounds']))}"
                    else:
                        # Normal drug
                        data = DRUG_CATEGORIES.get(proj.category, DRUG_CATEGORIES["Hypnoval XR"])
                        drug = Drug(
                            id=f"drug_{random.randint(100000,999999)}",
                            name=proj.drug_name,
                            category=proj.category,
                            potency=proj.quality,
                            erotic_intensity=proj.erotic_intensity_target,
                            production_cost=data.get("base_cost", 850),
                            side_effects=random.sample(data.get("side_effect_pool", ["intense erotic effects"]), min(2, len(data.get("side_effect_pool", ["intense erotic effects"])))),
                            repeat_purchase_rate=data.get("repeat_rate", 0.8),
                            quality=proj.quality,
                            transformation_power=data.get("transformation_power", 1.3),
                            subscription_model=True if proj.erotic_intensity_target > 85 else False
                        )
                        launch_msg = f"PROJECT COMPLETE — {drug.name} launched to market!"

                    state.catalog.append(drug)
                    state.pipeline.remove(proj)

                    # Handle gene therapy completion
                    if getattr(proj, "is_gene_therapy", False):
                        state.active_gene_projects = max(0, state.active_gene_projects - 1)
                        erotic_story = generate_erotic_testimonial(drug, "gene_therapy")
                        state.erotic_logs.append(erotic_story)
                        state.content_fuel += 5
                        launch_msg = f"GENE THERAPY COMPLETE — {drug.name} created!\nPermanent transformation effects unlocked."
                    else:
                        erotic_story = generate_erotic_testimonial(drug, "launch")
                        state.erotic_logs.append(erotic_story)
                        state.content_fuel += 3

                    return True, launch_msg, erotic_story

            return True, log, None

    return False, "Project not found.", None

def recruit_testers(state: GameState, budget: float, quality_target: str = "high") -> Tuple[bool, str]:
    if state.cash < budget:
        return False, "Not enough cash."

    state.cash -= budget
    num = max(2, int(budget / 18000))

    new_testers = [f"Subject-{random.randint(10,99)}" for _ in range(num)]
    if state.pipeline:
        proj = random.choice(state.pipeline)
        proj.assigned_testers.extend(new_testers)

    state.scandal_risk = min(95.0, state.scandal_risk + (budget / 180000))
    return True, f"Recruited {num} test subjects (quality level: {quality_target}). Scandal risk increased slightly."

def launch_drug(state: GameState, drug_id: str, price: Optional[float] = None, subscription: Optional[bool] = None) -> Tuple[bool, str]:
    for drug in state.catalog:
        if drug.id == drug_id:
            if price:
                drug.price_per_dose = price
            if subscription is not None:
                drug.subscription_model = subscription
            drug.weeks_in_market = 0
            story = generate_erotic_testimonial(drug, "launch")
            state.erotic_logs.append(story)
            state.content_fuel += 2
            return True, f"{drug.name} is now actively selling at ${drug.price_per_dose:.2f} per dose. New user story generated."
    return False, "Drug not found in catalog."

def advance_week(state: GameState) -> List[str]:
    logs: List[str] = []
    state.week += 1
    if state.week > 52:
        state.year += 1
        state.week = 1
        logs.append(f"=== NEW YEAR: {state.year} ===")

    weekly_revenue = 0.0

    # Catalog sales + erotic logs
    for drug in state.catalog:
        if not drug.owned:
            continue
        base_demand = state.active_users * 0.09
        potency_factor = drug.potency / 70.0
        repeat = drug.repeat_purchase_rate
        sold = int(base_demand * potency_factor * repeat * random.uniform(0.85, 1.15))

        revenue = sold * drug.price_per_dose
        drug.total_sold += sold
        drug.revenue_generated += revenue
        weekly_revenue += revenue
        drug.weeks_in_market += 1

        if random.random() < 0.28:
            story = generate_erotic_testimonial(drug, "market")
            state.erotic_logs.append(story)
            state.content_fuel += 1
            logs.append(f"New erotic testimonial generated for {drug.name}")

    state.cash += weekly_revenue
    state.total_revenue += weekly_revenue

    # Process loan payments (Banking system)
    loan_logs = process_loan_payments(state)
    logs.extend(loan_logs)

    # Pipeline processing
    for proj in list(state.pipeline):
        if random.random() < 0.65:
            ok, msg, erotic = advance_rd_phase(state, proj.id)
            if ok:
                logs.append(msg)
            if erotic:
                logs.append("Erotic case study unlocked from trial.")

    # User growth & transformation
    growth = 1.009 + (state.transformation_index / 2800)
    state.active_users *= growth
    state.subscribers = int(state.active_users * 0.38)

    state.transformation_index = min(92.0, state.transformation_index + random.uniform(0.6, 1.4))

    if random.random() < 0.18:
        state.scandal_risk = min(96.0, state.scandal_risk + random.uniform(1.5, 4.5))
        logs.append("⚠ Scandal risk increased — someone is talking.")

    # Random viral erotic event
    if random.random() < 0.22:
        event = generate_erotic_testimonial(random.choice(state.catalog) if state.catalog else None, "event")
        state.erotic_logs.append(event)
        state.content_fuel += 2
        state.transformation_index += 1.8
        logs.append("VIRAL TRANSFORMATION EVENT — public incident reported.")

    # History
    state.history.append({
        "year": state.year, "week": state.week,
        "cash": round(state.cash, 0),
        "users": round(state.active_users, 0),
        "transformation": round(state.transformation_index, 1),
        "scandal": round(state.scandal_risk, 1),
        "revenue": round(weekly_revenue, 0)
    })

    logs.append(f"W{state.week} complete | Revenue: ${weekly_revenue:,.0f} | Users: {state.active_users:,.0f} | Transformation Index: {state.transformation_index:.1f}")
    return logs

def save_game(state: GameState, path: str = "hypnodose_save.json") -> str:
    data = asdict(state)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    return path

def load_game(path: str = "hypnodose_save.json") -> GameState:
    with open(path, "r") as f:
        data = json.load(f)
    return GameState(**data)

# =============================================================================
# INTERACTIVE CLI (Highly Interactive Menu-Driven Gameplay)
# =============================================================================

def show_status(state: GameState):
    print(f"\n{'='*70}")
    print(f"WEEK {state.week}  |  YEAR {state.year}")
    print(f"Cash: ${state.cash:,.0f}     |  Users: {state.active_users:,.0f}")
    print(f"Transformation Index: {state.transformation_index:.1f}  |  Scandal Risk: {state.scandal_risk:.1f}%")
    print(f"Credit Rating: {state.credit_rating:.1f}  |  Total Debt: ${state.total_debt:,.0f}")
    print(f"Content Fuel: {state.content_fuel} erotic stories ready")
    print(f"{'='*70}")


def show_pipeline(state: GameState):
    if not state.pipeline:
        print("No active R&D projects.")
        return
    print("\n--- R&D PIPELINE ---")
    for i, proj in enumerate(state.pipeline, 1):
        print(f"{i}. {proj.drug_name} ({proj.category}) | Phase: {proj.phase} | {proj.progress:.1f}% | Researcher: {proj.assigned_researcher or 'Unassigned'}")


def show_catalog(state: GameState):
    if not state.catalog:
        print("No drugs launched yet.")
        return
    print("\n--- PRODUCT VAULT ---")
    for i, drug in enumerate(state.catalog, 1):
        sub = " [SUBSCRIPTION]" if drug.subscription_model else ""
        print(f"{i}. {drug.name} ({drug.category}){sub}")
        print(f"   Potency: {drug.potency:.0f} | Erotic: {drug.erotic_intensity:.0f} | Price: ${drug.price_per_dose:.2f}")


def interactive_menu():
    print("╔════════════════════════════════════════════════════════════╗")
    print("║   HYPNODOSE PHARMACEUTICALS — Erotic Transformation Sim    ║")
    print("║              HIGHLY INTERACTIVE MODE                       ║")
    print("╚════════════════════════════════════════════════════════════╝\n")

    state = new_game()
    show_status(state)

    while True:
        print("\n" + "-"*70)
        print("MAIN MENU")
        print("1. Advance 1 Week")
        print("2. Manage R&D Pipeline")
        print("3. View / Launch Drugs (Product Vault)")
        print("4. Recruit Test Subjects")
        print("5. Loans & Debt Management")
        print("6. View Erotic Logs / Generate Content")
        print("7. Interact with Subjects (Commands & Reactions)")
        print("8. Show Full Status")
        print("9. Save Game")
        print("10. Load Game")
        print("0. Quit")
        print("-"*70)

        choice = input("Select option: ").strip()

        if choice == "1":
            # Advance week
            logs = advance_week(state)
            print("\n--- WEEK RESULTS ---")
            for line in logs:
                print("•", line)
            show_status(state)

            # Chance for random interactive event
            if random.random() < 0.25:
                print("\n>>> A new situation has arisen. Check the logs above.")

        elif choice == "2":
            # R&D Management
            show_pipeline(state)
            print("\nR&D Options:")
            print("a. Start New R&D Project")
            print("b. Advance Selected Project Phase")
            print("c. Assign Researcher to Project")
            print("d. Research Hybrid Drug (Combine two existing drugs)")
            print("e. Start Gene Therapy Project (Permanent Transformation)")
            print("f. Back to Main Menu")
            sub = input("Choose: ").lower().strip()

            if sub == "a":
                print("\nAvailable Categories:")
                for i, cat in enumerate(DRUG_CATEGORIES.keys(), 1):
                    print(f"{i}. {cat}")
                try:
                    idx = int(input("Select category number: ")) - 1
                    cat = list(DRUG_CATEGORIES.keys())[idx]
                    ok, msg = start_rd_project(state, cat)
                    print(msg)
                except:
                    print("Invalid selection.")

            elif sub == "b":
                show_pipeline(state)
                try:
                    idx = int(input("Select project number to advance: ")) - 1
                    proj = state.pipeline[idx]
                    ok, msg, erotic = advance_rd_phase(state, proj.id)
                    print(msg)
                    if erotic:
                        print("\n[New erotic case study generated from trial]")
                except:
                    print("Invalid selection.")

            elif sub == "c":
                show_pipeline(state)
                try:
                    pidx = int(input("Select project number: ")) - 1
                    proj = state.pipeline[pidx]
                    print("\nAvailable Researchers:")
                    for i, t in enumerate(EROTIC_TALENT_POOL, 1):
                        print(f"{i}. {t['name']} ({t['role']}) - Skill {t['skill']}")
                    ridx = int(input("Select researcher: ")) - 1
                    proj.assigned_researcher = EROTIC_TALENT_POOL[ridx]["name"]
                    print(f"Assigned {proj.assigned_researcher} to {proj.drug_name}")
                except:
                    print("Invalid selection.")

            elif sub == "d":
                # Hybrid drug research
                if len(state.catalog) < 2:
                    print("You need at least 2 launched drugs to create a hybrid.")
                else:
                    show_catalog(state)
                    try:
                        print("\nSelect first drug to combine:")
                        d1 = int(input("Drug number: ")) - 1
                        print("Select second drug to combine:")
                        d2 = int(input("Drug number: ")) - 1
                        custom_name = input("Custom hybrid name (leave blank for auto): ").strip() or None

                        ok, msg = start_hybrid_project(state, state.catalog[d1].id, state.catalog[d2].id, custom_name)
                        print(msg)
                    except Exception as e:
                        print(f"Invalid selection: {e}")

            elif sub == "e":
                # Gene Therapy
                print("\n=== GENE THERAPY RESEARCH ===")
                print(f"Available slots: {state.gene_therapy_slots - state.active_gene_projects}/{state.gene_therapy_slots}")
                print("Gene Therapy creates permanent transformation effects (very expensive but extremely powerful).")

                therapy_types = {
                    "1": ("hypno_obedience", "Hypno-Obedience Gene Protocol"),
                    "2": ("body_permanent", "Permanent Body Remodeling"),
                    "3": ("exhibition_gene", "Exhibition Susceptibility Gene Edit"),
                    "4": ("dollification", "Dollification Gene Sequence"),
                    "5": ("full_surrender", "Total Surrender Gene Reprogramming")
                }

                print("\nTherapy Types:")
                for k, v in therapy_types.items():
                    print(f"{k}. {v[1]}")

                tchoice = input("Select therapy type (or 0 to cancel): ").strip()
                if tchoice in therapy_types:
                    therapy_type, _ = therapy_types[tchoice]
                    base_id = None
                    if state.catalog:
                        use_base = input("Base this on an existing drug? (y/n): ").lower().startswith("y")
                        if use_base:
                            show_catalog(state)
                            try:
                                bidx = int(input("Select base drug number: ")) - 1
                                base_id = state.catalog[bidx].id
                            except:
                                pass

                    custom = input("Custom name (optional): ").strip() or None
                    ok, msg = start_gene_therapy_project(state, base_id, therapy_type, custom)
                    print(msg)
                else:
                    print("Cancelled.")

            elif sub == "f":
                pass  # Back to main menu

        elif choice == "3":
            show_catalog(state)
            print("\nVault Options:")
            print("a. View Full Profile of a Drug")
            print("b. Adjust Pricing / Subscription of a Drug")
            print("c. Back")
            sub = input("Choose: ").lower().strip()

            if sub == "a":
                show_catalog(state)
                try:
                    idx = int(input("Select drug number: ")) - 1
                    drug = state.catalog[idx]
                    desc = DRUG_CATEGORIES.get(drug.category, {}).get("description", "")
                    print(f"\n{drug.name} ({drug.category})")
                    print(f"Description: {desc}")
                    story = generate_erotic_testimonial(drug, "market")
                    print(f"\nLatest Erotic Case Study:\n{story}")
                except:
                    print("Invalid selection.")

            elif sub == "b":
                show_catalog(state)
                try:
                    idx = int(input("Select drug number: ")) - 1
                    drug = state.catalog[idx]
                    new_price = float(input(f"New price per dose (current ${drug.price_per_dose:.2f}): "))
                    sub_choice = input("Enable Subscription Model? (y/n): ").lower().startswith("y")
                    ok, msg = launch_drug(state, drug.id, new_price, sub_choice)
                    print(msg)
                except:
                    print("Invalid input.")

        elif choice == "4":
            print("\nRecruit Test Subjects")
            print("1. Standard Quality ($85,000)")
            print("2. High Quality ($185,000) - Recommended")
            print("3. Extreme Suggestibility ($320,000)")
            rchoice = input("Select tier: ").strip()
            budgets = {"1": 85000, "2": 185000, "3": 320000}
            quality = {"1": "medium", "2": "high", "3": "extreme"}
            if rchoice in budgets:
                ok, msg = recruit_testers(state, budgets[rchoice], quality[rchoice])
                print(msg)
            else:
                print("Cancelled.")

        elif choice == "5":
            print("\n--- LOANS & DEBT ---")
            summary = get_debt_summary(state)
            print(f"Total Debt: ${summary['total_debt']:,.0f}")
            print(f"Weekly Debt Service: ${summary['weekly_debt_service']:,.0f}")
            print(f"Credit Rating: {summary['credit_rating']}")
            if summary["loans"]:
                for loan in summary["loans"]:
                    print(f"  - {loan['type']}: ${loan['remaining']:,.0f} remaining @ {loan['interest_rate']:.1f}%")

            print("\nOptions:")
            print("a. View & Take New Loan Offers")
            print("b. Make Extra Payment on a Loan")
            print("c. Back")
            sub = input("Choose: ").lower().strip()

            if sub == "a":
                show_loan_offers(state)
            elif sub == "b":
                if not state.loans:
                    print("No active loans.")
                else:
                    for i, loan in enumerate(state.loans, 1):
                        print(f"{i}. {loan['type']} - ${loan['remaining']:,.0f} remaining")
                    try:
                        lidx = int(input("Select loan: ")) - 1
                        amount = float(input("Extra payment amount: $"))
                        ok, msg = repay_loan_early(state, state.loans[lidx]["id"], amount)
                        print(msg)
                    except:
                        print("Invalid input.")

        elif choice == "6":
            print("\n--- EROTIC LOGS / HIGHLY AROUSING CONTENT ---")
            if state.erotic_logs:
                print(f"You have {len(state.erotic_logs)} erotic case studies logged.")
                print("Latest:")
                print(state.erotic_logs[-1][:450] + "...")
            else:
                print("No erotic logs yet.")

            print("\nOptions:")
            print("a. Generate Highly Arousing Story from a Drug")
            print("b. Generate Custom Intense Hypno / Doll Story")
            print("c. Generate Public Exhibition / Risk Story")
            print("d. View Recent Logs")
            print("e. Back to Main Menu")
            sub = input("Choose: ").lower().strip()

        elif choice == "7":
            # Interact with Subjects (v1)
            print("\n=== INTERACT WITH SUBJECTS ===")
            print("You can give simple commands to test subjects and see their reactions.")

            # Create demo subjects if none exist
            if not hasattr(state, 'demo_subjects') or not state.demo_subjects:
                state.demo_subjects = [
                    SubjectState("Subject #47", drug_history=["Hypnoval XR"]),
                    SubjectState("Subject #89", drug_history=["Exhibra", "Lumina-9"]),
                    SubjectState("Subject #112", gene_therapy_history=["dollification"])
                ]
                # Apply history
                for subj in state.demo_subjects:
                    for drug in subj.drug_history:
                        subj.update_from_drug(drug)
                    for therapy in subj.gene_therapy_history:
                        subj.update_from_gene_therapy(therapy)

            print("\nAvailable Subjects:")
            for i, subj in enumerate(state.demo_subjects, 1):
                print(f"{i}. {subj.name} | State: {subj.current_state} | Obedience: {subj.obedience}")

            try:
                sidx = int(input("\nSelect subject number: ")) - 1
                selected = state.demo_subjects[sidx]
                print(f"\nInteracting with: {selected.name} ({selected.current_state})")

                while True:
                    cmd = input("Enter command (or 'back' to return): ").strip()
                    if cmd.lower() in ["back", "exit", "quit"]:
                        break
                    reaction = generate_subject_reaction(selected, cmd)
                    print(f"\n{reaction}\n")
            except (ValueError, IndexError):
                print("Invalid selection.")

            if sub == "a" and state.catalog:
                show_catalog(state)
                try:
                    idx = int(input("Select drug number: ")) - 1
                    drug = state.catalog[idx]
                    story = generate_erotic_testimonial(drug, "manual")
                    state.erotic_logs.append(story)
                    state.content_fuel += 1
                    print("\n" + "="*70)
                    print("GENERATED HIGHLY AROUSING STORY")
                    print("="*70)
                    print(story)
                except:
                    print("Invalid selection.")

            elif sub == "b":
                # Custom intense hypno / doll story
                story = generate_erotic_testimonial(random.choice(state.catalog) if state.catalog else None, "hypno")
                # Force a very hypno/doll focused version
                story = f"[INTENSE HYPNOTIC / DOLLIFICATION STORY]\n\n" + story.replace("good girl", "empty doll").replace("blank", "completely, blissfully empty")
                state.erotic_logs.append(story)
                state.content_fuel += 1
                print("\n" + "="*70)
                print("INTENSE HYPNOTIC / DOLL STORY GENERATED")
                print("="*70)
                print(story)

            elif sub == "c":
                story = generate_erotic_testimonial(random.choice(state.catalog) if state.catalog else None, "exhibition")
                story = f"[PUBLIC RISK / EXHIBITION STORY]\n\n" + story
                state.erotic_logs.append(story)
                state.content_fuel += 1
                print("\n" + "="*70)
                print("PUBLIC EXHIBITION / RISK STORY GENERATED")
                print("="*70)
                print(story)

            elif sub == "d":
                print("\n--- RECENT EROTIC LOGS ---")
                for log in state.erotic_logs[-5:]:
                    print(log[:500] + "...\n" + "-"*50)

        elif choice == "7":
            show_status(state)
            show_pipeline(state)
            show_catalog(state)

        elif choice == "8":
            path = save_game(state)
            print(f"Game saved to {path}")

        elif choice == "9":
            try:
                path = input("Enter save file name (default: hypnodose_save.json): ").strip() or "hypnodose_save.json"
                state = load_game(path)
                print("Game loaded successfully.")
                show_status(state)
            except Exception as e:
                print(f"Load failed: {e}")

        elif choice == "0":
            print("Thanks for playing HypnoDose Pharmaceuticals.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    interactive_menu()
