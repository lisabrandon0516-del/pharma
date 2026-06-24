#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HYPNODOSE PHARMACEUTICALS — Erotic Transformation Executive Simulator (Tkinter GUI)
Built directly on PULSE GUI architecture (tv_station_gui.py patterns + theme)
Dark cyberpunk executive dashboard: deep navy + electric cyan / hot magenta neon
"""

import json
import os
import random
import sys
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext, simpledialog
from dataclasses import asdict
from typing import Any, Dict, List, Optional

# Import the engine
import pharma_sim as engine
from pharma_sim import (
    GameState, new_game, advance_week, start_rd_project, advance_rd_phase,
    recruit_testers, launch_drug, save_game, load_game, generate_erotic_testimonial,
    start_hybrid_project, start_gene_therapy_project,
    DRUG_CATEGORIES, EROTIC_TALENT_POOL
)
from subject_interaction import SubjectState, generate_subject_reaction

# =============================================================================
# THEME - Exact PULSE Professional Dark Neon (deep navy + cyan/magenta)
# =============================================================================
BG = "#0a0b12"
PANEL = "#12131c"
CARD_BG = "#1a1b26"
CARD_BORDER = "#25263a"

ACCENT = "#3b82f6"
PRIMARY = "#6366f1"
CYAN = "#22d3ee"
MAGENTA = "#c026ff"
PURPLE = "#a855f7"
GOLD = "#f59e0b"
CREAM = "#e2e8f0"
TEXT = "#f1f5f9"
MUTED = "#64748b"
GREEN_OK = "#22c55e"
RED_ALERT = "#ef4444"

DESKTOP_BG = "#0a1425"
ICON_BG = "#162a40"
ICON_SELECTED = "#1e3a5f"
TASKBAR_BG = "#08101f"
WINDOW_BG = "#0f1a2e"
BEZEL = "#1a2535"

def style_root(root: tk.Tk, scale: float = 1.0):
    root.configure(bg=BG)
    style = ttk.Style(root)
    try:
        style.theme_use("clam")
    except:
        pass

    def sf(size):
        return max(8, int(size * scale))

    label_font = ("Segoe UI", sf(11))
    gold_font = ("Segoe UI", sf(12), "bold")
    title_font = ("Segoe UI", sf(18), "bold")
    big_font = ("Segoe UI", sf(13), "bold")
    small_font = ("Segoe UI", sf(10))
    btn_font = ("Segoe UI", sf(11))
    btn_pad = (sf(8), sf(5))
    list_font = ("Consolas", sf(10))
    entry_font = ("Consolas", sf(10))
    pill_font = ("Segoe UI", sf(10), "bold")

    style.configure("TFrame", background=BG)
    style.configure("Panel.TFrame", background=PANEL, relief="flat")
    style.configure("Card.TFrame", background=CARD_BG, relief="flat")

    style.configure("TLabel", background=BG, foreground=TEXT, font=label_font, padding=sf(2))
    style.configure("Gold.TLabel", background=BG, foreground=GOLD, font=gold_font, padding=sf(2))
    style.configure("Title.TLabel", background=BG, foreground=ACCENT, font=title_font, padding=sf(3))
    style.configure("Big.TLabel", background=BG, foreground=CREAM, font=big_font, padding=sf(2))
    style.configure("Small.TLabel", background=BG, foreground=MUTED, font=small_font, padding=sf(1))

    style.configure("TButton", background=PANEL, foreground=TEXT, font=btn_font,
                    padding=btn_pad, relief="flat")
    style.map("TButton",
              background=[("active", "#25263a"), ("pressed", "#1f2937")],
              foreground=[("active", CYAN), ("pressed", TEXT)])

    style.configure("Accent.TButton", background="#161b2e", foreground=CYAN, font=btn_font,
                    padding=(btn_pad[0]+2, btn_pad[1]+1), relief="flat")
    style.map("Accent.TButton",
              background=[("active", "#1f2937"), ("pressed", "#25263a")],
              foreground=[("active", "#67e8f9"), ("pressed", CYAN)])

    style.configure("Gold.TButton", background="#161b2e", foreground=GOLD, font=btn_font,
                    padding=(btn_pad[0]+2, btn_pad[1]+1), relief="flat")
    style.map("Gold.TButton",
              background=[("active", "#1f2937"), ("pressed", "#25263a")],
              foreground=[("active", "#fcd34d"), ("pressed", GOLD)])

    style.configure("TListbox", background=CARD_BG, foreground=TEXT, selectbackground=ACCENT,
                    selectforeground=BG, font=list_font, relief="flat")

    style.configure("TEntry", fieldbackground=PANEL, foreground=TEXT, insertcolor=CYAN, font=entry_font)

    style.configure("Warning.TLabel", background=BG, foreground=RED_ALERT, font=small_font)
    style.configure("Success.TLabel", background=BG, foreground=GREEN_OK, font=small_font)
    style.configure("Section.TLabel", background=BG, foreground=ACCENT, font=gold_font, padding=sf(2))

def make_label(parent, text, style="TLabel", **kw):
    return ttk.Label(parent, text=text, style=style, **kw)

def make_button(parent, text, command, accent=CYAN, bold=False, width=None, scale=1.0, **kw):
    fs = max(9, int(10 * scale))
    font = ("Segoe UI", fs, "bold") if bold else ("Segoe UI", fs)
    pxy = (max(6, int(10*scale)), max(3, int(4*scale)))
    bg = "#161b2e"
    btn = tk.Button(
        parent, text=text, bg=bg, fg=accent,
        font=font, relief="flat", bd=1,
        padx=pxy[0], pady=pxy[1], command=command,
        activebackground="#25263a", activeforeground=accent,
        **kw
    )
    if width:
        btn.config(width=width)

    def on_enter(e, b=btn, a=accent):
        b.config(bg="#1f2937", fg=a, highlightbackground=a, highlightthickness=1)
    def on_leave(e, b=btn, a=accent):
        b.config(bg="#161b2e", fg=a, highlightbackground=CARD_BORDER, highlightthickness=0)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

# =============================================================================
# MAIN GUI CLASS
# =============================================================================

class HypnoDoseGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("HYPNODOSE PHARMACEUTICALS — Executive Simulator")

        try:
            sw = root.winfo_screenwidth()
            sh = root.winfo_screenheight()
            w = int(min(sw * 0.92, 1680))
            h = int(min(sh * 0.88, 980))
            self.root.geometry(f"{w}x{h}+{max(10, (sw-w)//2)}+{max(10, (sh-h)//2)}")
            self.root.minsize(int(sw * 0.55), int(sh * 0.5))
            self.root.resizable(True, True)
            base_h = 850.0
            self.ui_scale = max(0.9, min(1.45, sh / base_h))
        except Exception:
            self.root.geometry("1280x820")
            self.root.minsize(900, 620)
            self.ui_scale = 1.0

        style_root(root, scale=getattr(self, 'ui_scale', 1.0))

        self.state: GameState = new_game()
        self._build_main_ui()

    def _build_main_ui(self):
        for w in self.root.winfo_children():
            w.destroy()

        self.root.configure(bg=BG)

        # Top title bar
        titlebar = tk.Frame(self.root, bg="#001122", height=26)
        titlebar.pack(fill="x")
        titlebar.pack_propagate(False)
        tk.Label(titlebar, text="  HYPNODOSE OS 2026  •  Executive Mode  •  Pleasure Division", 
                 bg="#001122", fg=CYAN, font=("Consolas", 9)).pack(side="left", padx=8)
        tk.Label(titlebar, text="X", bg="#001122", fg=RED_ALERT, font=("Segoe UI", 10, "bold")).pack(side="right", padx=8)

        # Header with glowing logo
        header = tk.Frame(self.root, bg=PANEL, height=68)
        header.pack(fill="x")
        header.pack_propagate(False)

        logo_f = tk.Frame(header, bg=PANEL)
        logo_f.pack(side="left", padx=14, pady=6)

        # Glowing H logo
        icon_c = tk.Canvas(logo_f, width=28, height=28, bg=PANEL, highlightthickness=0, bd=0)
        for i in range(5, 0, -1):
            icon_c.create_oval(2,2,26,26, outline=MAGENTA, width=i, fill="")
        icon_c.create_oval(5,5,23,23, fill=MAGENTA, outline=MAGENTA)
        icon_c.create_oval(8,8,20,20, fill="#05070f", outline="#05070f")
        icon_c.create_text(14, 14, text="H", fill=MAGENTA, font=("Segoe UI", 15, "bold"), anchor="center")
        icon_c.pack(side="left", padx=(0,8))

        glow_frame = tk.Frame(logo_f, bg=PANEL)
        glow_frame.pack(side="left")
        main_font = ("Segoe UI", int(20 * self.ui_scale), "bold")
        glow_c = "#ff66cc"
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
            sh = tk.Label(glow_frame, text="HYPNODOSE", bg=PANEL, fg=glow_c, font=main_font)
            sh.place(x=dx, y=dy)
        tk.Label(glow_frame, text="HYPNODOSE", bg=PANEL, fg=TEXT, font=main_font).place(x=0, y=0)

        make_label(header, "PHARMACEUTICALS  •  Erotic Transformation Division", "Gold.TLabel").pack(side="left", padx=12, pady=8)

        # Quick stats bar
        stats = tk.Frame(header, bg=PANEL)
        stats.pack(side="right", padx=16)
        self.cash_var = tk.StringVar(value="$42,000,000")
        self.users_var = tk.StringVar(value="142,000 users")
        self.trans_var = tk.StringVar(value="Trans Index: 19.8")
        make_label(stats, "CASH", "Small.TLabel").pack(side="left", padx=(0,4))
        make_label(stats, "", "Big.TLabel").pack(side="left")
        tk.Label(stats, textvariable=self.cash_var, bg=PANEL, fg=CYAN, font=("Consolas", 13, "bold")).pack(side="left", padx=8)
        make_label(stats, "  |  ", "Small.TLabel").pack(side="left")
        tk.Label(stats, textvariable=self.users_var, bg=PANEL, fg=TEXT, font=("Consolas", 11)).pack(side="left", padx=4)
        make_label(stats, "  |  ", "Small.TLabel").pack(side="left")
        tk.Label(stats, textvariable=self.trans_var, bg=PANEL, fg=MAGENTA, font=("Consolas", 11, "bold")).pack(side="left", padx=4)

        # Main content area with tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=8, pady=6)

        # Create tabs
        self._create_dashboard_tab()
        self._create_rd_tab()
        self._create_vault_tab()
        self._create_trials_tab()
        self._create_marketing_tab()
        self._create_talent_tab()
        self._create_intel_tab()

        # Bottom quick bar
        bottom = tk.Frame(self.root, bg=PANEL, height=42)
        bottom.pack(fill="x", side="bottom")
        bottom.pack_propagate(False)

        make_button(bottom, "ADVANCE WEEK", self._advance_week, accent=CYAN, bold=True).pack(side="left", padx=6, pady=6)
        make_button(bottom, "START NEW R&D PROJECT", lambda: self._start_rd_dialog(), accent=MAGENTA).pack(side="left", padx=4, pady=6)
        make_button(bottom, "RECRUIT TESTERS", lambda: self._recruit_dialog(), accent=GOLD).pack(side="left", padx=4, pady=6)
        make_button(bottom, "VIEW EROTIC LOGS", self._show_erotic_logs, accent="#ff66cc").pack(side="left", padx=4, pady=6)
        make_button(bottom, "SAVE GAME", self._save, accent=GREEN_OK).pack(side="right", padx=6, pady=6)
        make_button(bottom, "LOAD GAME", self._load, accent=ACCENT).pack(side="right", padx=4, pady=6)

        self._refresh_all()

    def _refresh_all(self):
        s = self.state
        self.cash_var.set(f"${s.cash:,.0f}")
        self.users_var.set(f"{s.active_users:,.0f} users")
        self.trans_var.set(f"Trans Index: {s.transformation_index:.1f}")

        # Refresh each tab if they have refresh methods
        if hasattr(self, '_refresh_dashboard'):
            self._refresh_dashboard()
        if hasattr(self, '_refresh_vault'):
            self._refresh_vault()
        if hasattr(self, '_refresh_rd'):
            self._refresh_rd()

    def _create_dashboard_tab(self):
        tab = tk.Frame(self.notebook, bg=BG)
        self.notebook.add(tab, text="  DASHBOARD  ")

        # Top metrics row
        metrics = tk.Frame(tab, bg=BG)
        metrics.pack(fill="x", padx=10, pady=8)

        # Cash card
        card1 = tk.Frame(metrics, bg=CARD_BG, bd=1, highlightbackground=CYAN, highlightthickness=2, relief="flat")
        card1.pack(side="left", padx=6, fill="both", expand=True)
        make_label(card1, "CASH ON HAND", "Small.TLabel").pack(anchor="w", padx=8, pady=4)
        self.dash_cash = tk.Label(card1, text="$42,000,000", bg=CARD_BG, fg=CYAN, font=("Consolas", 22, "bold"))
        self.dash_cash.pack(anchor="w", padx=8, pady=2)

        # Users card
        card2 = tk.Frame(metrics, bg=CARD_BG, bd=1, highlightbackground=MAGENTA, highlightthickness=2, relief="flat")
        card2.pack(side="left", padx=6, fill="both", expand=True)
        make_label(card2, "ACTIVE USERS", "Small.TLabel").pack(anchor="w", padx=8, pady=4)
        self.dash_users = tk.Label(card2, text="142,000", bg=CARD_BG, fg=MAGENTA, font=("Consolas", 22, "bold"))
        self.dash_users.pack(anchor="w", padx=8, pady=2)

        # Transformation card
        card3 = tk.Frame(metrics, bg=CARD_BG, bd=1, highlightbackground="#ff66cc", highlightthickness=2, relief="flat")
        card3.pack(side="left", padx=6, fill="both", expand=True)
        make_label(card3, "TRANSFORMATION INDEX", "Small.TLabel").pack(anchor="w", padx=8, pady=4)
        self.dash_trans = tk.Label(card3, text="19.8", bg=CARD_BG, fg="#ff66cc", font=("Consolas", 22, "bold"))
        self.dash_trans.pack(anchor="w", padx=8, pady=2)

        # Scandal risk
        card4 = tk.Frame(metrics, bg=CARD_BG, bd=1, highlightbackground=GOLD, highlightthickness=2, relief="flat")
        card4.pack(side="left", padx=6, fill="both", expand=True)
        make_label(card4, "SCANDAL RISK", "Small.TLabel").pack(anchor="w", padx=8, pady=4)
        self.dash_scandal = tk.Label(card4, text="24.5%", bg=CARD_BG, fg=GOLD, font=("Consolas", 22, "bold"))
        self.dash_scandal.pack(anchor="w", padx=8, pady=2)

        # Quick actions + latest log
        bottom = tk.Frame(tab, bg=BG)
        bottom.pack(fill="both", expand=True, padx=10, pady=6)

        make_label(bottom, "QUICK ACTIONS", "Gold.TLabel").pack(anchor="w", padx=4)
        actions = tk.Frame(bottom, bg=BG)
        actions.pack(fill="x", pady=4)
        make_button(actions, "ADVANCE 1 WEEK", self._advance_week, accent=CYAN, bold=True, width=18).pack(side="left", padx=4)
        make_button(actions, "START R&D PROJECT", lambda: self._start_rd_dialog(), accent=MAGENTA, width=18).pack(side="left", padx=4)
        make_button(actions, "RECRUIT TEST SUBJECTS", lambda: self._recruit_dialog(), accent=GOLD, width=20).pack(side="left", padx=4)
        make_button(actions, "INTERVIEW SUBJECTS", self._go_to_interviews_tab, accent="#ff66cc", width=20).pack(side="left", padx=4)

        make_label(bottom, "LATEST EROTIC LOG / CASE STUDY", "Gold.TLabel").pack(anchor="w", padx=4, pady=(12,4))
        self.log_text = scrolledtext.ScrolledText(bottom, height=12, bg="#0f1629", fg=TEXT, 
                                                   font=("Consolas", 10), wrap="word", relief="flat")
        self.log_text.pack(fill="both", expand=True, padx=4, pady=4)
        self.log_text.insert("1.0", "Welcome to HypnoDose Pharmaceuticals.\n\nAll operations are strictly confidential.\n\nUse the bottom bar or tabs to manage R&D, clinical trials, marketing, and talent.")

        self._refresh_dashboard = self._refresh_dashboard_impl

    def _go_to_interviews_tab(self):
        """Switch to the Subject Interviews tab"""
        for i in range(self.notebook.index("end")):
            if "INTERVIEW" in self.notebook.tab(i, "text").upper():
                self.notebook.select(i)
                return
        # Fallback
        try:
            self.notebook.select(4)
        except:
            pass

    def _refresh_dashboard_impl(self):
        s = self.state
        self.dash_cash.config(text=f"${s.cash:,.0f}")
        self.dash_users.config(text=f"{s.active_users:,.0f}")
        self.dash_trans.config(text=f"{s.transformation_index:.1f}")
        self.dash_scandal.config(text=f"{s.scandal_risk:.1f}%")

        if s.erotic_logs:
            self.log_text.delete("1.0", "end")
            self.log_text.insert("1.0", s.erotic_logs[-1])

    def _create_rd_tab(self):
        tab = tk.Frame(self.notebook, bg=BG)
        self.notebook.add(tab, text="  R&D LAB  ")

        make_label(tab, "RESEARCH & DEVELOPMENT PIPELINE", "Gold.TLabel").pack(anchor="w", padx=12, pady=8)

        self.rd_list = tk.Listbox(tab, height=14, bg=CARD_BG, fg=TEXT, selectbackground=CYAN,
                                  font=("Consolas", 10), relief="flat")
        self.rd_list.pack(fill="both", expand=True, padx=12, pady=4)

        btns = tk.Frame(tab, bg=BG)
        btns.pack(fill="x", padx=12, pady=6)
        make_button(btns, "START NEW PROJECT", lambda: self._start_rd_dialog(), accent=MAGENTA).pack(side="left", padx=4)
        make_button(btns, "ADVANCE SELECTED PHASE", self._advance_selected_rd, accent=CYAN).pack(side="left", padx=4)
        make_button(btns, "ASSIGN RESEARCHER", self._assign_researcher_dialog, accent=GOLD).pack(side="left", padx=4)
        make_button(btns, "RESEARCH HYBRID DRUG", self._start_hybrid_dialog, accent="#ff66cc").pack(side="left", padx=4)
        make_button(btns, "GENE THERAPY", self._start_gene_dialog, accent="#c026ff").pack(side="left", padx=4)

        self._refresh_rd = self._refresh_rd_impl

    def _refresh_rd_impl(self):
        self.rd_list.delete(0, "end")
        for proj in self.state.pipeline:
            prefix = "🧬 " if hasattr(proj, "hybrid_parents") else ""
            txt = f"{prefix}{proj.drug_name} | {proj.category} | Phase: {proj.phase} | {proj.progress:.1f}% | Researcher: {proj.assigned_researcher or 'None'}"
            self.rd_list.insert("end", txt)

    def _start_rd_dialog(self):
        dlg = tk.Toplevel(self.root)
        dlg.title("START NEW R&D PROJECT")
        dlg.configure(bg=BG)
        dlg.geometry("520x420")

        make_label(dlg, "Select Drug Category", "Gold.TLabel").pack(padx=12, pady=8)
        cat_var = tk.StringVar(value=list(DRUG_CATEGORIES.keys())[0])
        for cat in DRUG_CATEGORIES.keys():
            ttk.Radiobutton(dlg, text=cat, variable=cat_var, value=cat).pack(anchor="w", padx=20)

        make_label(dlg, "Project Name (optional)", "Small.TLabel").pack(padx=12, pady=(12,4))
        name_e = tk.Entry(dlg, width=40, bg=PANEL, fg=TEXT, insertbackground=CYAN)
        name_e.pack(padx=12)
        name_e.insert(0, "")

        def do_start():
            cat = cat_var.get()
            name = name_e.get().strip() or None
            ok, msg = start_rd_project(self.state, cat, name)
            if ok:
                self._log(msg)
                self._refresh_all()
                dlg.destroy()
            else:
                messagebox.showerror("Error", msg)

        make_button(dlg, "START PROJECT", do_start, accent=MAGENTA, bold=True).pack(pady=16)

    def _start_hybrid_dialog(self):
        if len(self.state.catalog) < 2:
            messagebox.showinfo("Hybrid Research", "You need at least 2 launched drugs to create a hybrid.")
            return

        dlg = tk.Toplevel(self.root)
        dlg.title("RESEARCH HYBRID DRUG")
        dlg.configure(bg=BG)
        dlg.geometry("620x520")

        make_label(dlg, "Combine Two Launched Drugs into a New Hybrid Compound", "Gold.TLabel").pack(padx=12, pady=8)

        # Drug 1 selection
        make_label(dlg, "Select First Drug:", "TLabel").pack(anchor="w", padx=20)
        drug1_var = tk.StringVar()
        drug1_cb = ttk.Combobox(dlg, textvariable=drug1_var, width=50, state="readonly")
        drug1_cb['values'] = [f"{d.name} ({d.category})" for d in self.state.catalog]
        drug1_cb.pack(padx=20, pady=4)

        # Drug 2 selection
        make_label(dlg, "Select Second Drug:", "TLabel").pack(anchor="w", padx=20, pady=(10,0))
        drug2_var = tk.StringVar()
        drug2_cb = ttk.Combobox(dlg, textvariable=drug2_var, width=50, state="readonly")
        drug2_cb['values'] = [f"{d.name} ({d.category})" for d in self.state.catalog]
        drug2_cb.pack(padx=20, pady=4)

        make_label(dlg, "Custom Hybrid Name (optional)", "Small.TLabel").pack(anchor="w", padx=20, pady=(12,4))
        name_e = tk.Entry(dlg, width=45, bg=PANEL, fg=TEXT, insertbackground=CYAN)
        name_e.pack(padx=20)

        def do_hybrid():
            try:
                idx1 = drug1_cb.current()
                idx2 = drug2_cb.current()
                if idx1 < 0 or idx2 < 0 or idx1 == idx2:
                    messagebox.showerror("Error", "Please select two different drugs.")
                    return

                drug1 = self.state.catalog[idx1]
                drug2 = self.state.catalog[idx2]
                custom_name = name_e.get().strip() or None

                ok, msg = start_hybrid_project(self.state, drug1.id, drug2.id, custom_name)
                if ok:
                    self._log(msg)
                    self._refresh_all()
                    dlg.destroy()
                else:
                    messagebox.showerror("Error", msg)
            except Exception as e:
                messagebox.showerror("Error", str(e))

        make_button(dlg, "START HYBRID RESEARCH", do_hybrid, accent="#ff66cc", bold=True).pack(pady=20)
        make_label(dlg, "Hybrids have higher research costs but can produce unique high-intensity erotic effects.", "Small.TLabel").pack(padx=12)

    def _start_gene_dialog(self):
        if self.state.active_gene_projects >= self.state.gene_therapy_slots:
            messagebox.showinfo("Gene Therapy", f"Gene therapy capacity full ({self.state.gene_therapy_slots} slots).")
            return

        dlg = tk.Toplevel(self.root)
        dlg.title("START GENE THERAPY PROJECT")
        dlg.configure(bg=BG)
        dlg.geometry("580x480")

        make_label(dlg, "GENE THERAPY — Permanent Transformation Research", "Gold.TLabel").pack(padx=12, pady=8)
        make_label(dlg, "Extremely expensive but creates powerful, permanent changes.", "Small.TLabel").pack(padx=12)

        therapy_options = [
            ("hypno_obedience", "Hypno-Obedience Gene Protocol"),
            ("body_permanent", "Permanent Body Remodeling"),
            ("exhibition_gene", "Exhibition Susceptibility Gene Edit"),
            ("dollification", "Dollification Gene Sequence"),
            ("full_surrender", "Total Surrender Gene Reprogramming")
        ]

        therapy_var = tk.StringVar(value=therapy_options[0][0])
        for code, label in therapy_options:
            ttk.Radiobutton(dlg, text=label, variable=therapy_var, value=code).pack(anchor="w", padx=30)

        make_label(dlg, "Base on existing drug? (optional)", "Small.TLabel").pack(anchor="w", padx=20, pady=(12,4))
        base_var = tk.StringVar(value="None")
        base_values = ["None"] + [f"{d.name} ({d.category})" for d in self.state.catalog]
        base_cb = ttk.Combobox(dlg, textvariable=base_var, width=45, values=base_values, state="readonly")
        base_cb.pack(padx=20)

        make_label(dlg, "Custom Name (optional)", "Small.TLabel").pack(anchor="w", padx=20, pady=(8,4))
        name_e = tk.Entry(dlg, width=40, bg=PANEL, fg=TEXT)
        name_e.pack(padx=20)

        def do_gene():
            therapy_type = therapy_var.get()
            custom_name = name_e.get().strip() or None
            base_id = None

            if base_var.get() != "None":
                try:
                    idx = base_values.index(base_var.get()) - 1
                    base_id = self.state.catalog[idx].id
                except:
                    pass

            ok, msg = start_gene_therapy_project(self.state, base_id, therapy_type, custom_name)
            if ok:
                self._log(msg)
                self._refresh_all()
                dlg.destroy()
            else:
                messagebox.showerror("Error", msg)

        make_button(dlg, "START GENE THERAPY PROJECT", do_gene, accent="#c026ff", bold=True).pack(pady=16)

    
    def _refresh_subjects(self):
        self.subject_list.delete(0, "end")
        if not hasattr(self.state, 'demo_subjects') or not self.state.demo_subjects:
            self.state.demo_subjects = [
                SubjectState("Subject #47", drug_history=["Hypnoval XR"]),
                SubjectState("Subject #89", drug_history=["Exhibra", "Lumina-9"]),
                SubjectState("Subject #112", gene_therapy_history=["dollification"]),
                SubjectState("Subject #203", drug_history=["Vellura"], gene_therapy_history=["exhibition_gene"])
            ]
            for subj in self.state.demo_subjects:
                for drug in subj.drug_history:
                    subj.update_from_drug(drug)
                for therapy in subj.gene_therapy_history:
                    subj.update_from_gene_therapy(therapy)

        for subj in self.state.demo_subjects:
            txt = f"{subj.name} | {subj.current_state} | Obed:{subj.obedience}"
            self.subject_list.insert("end", txt)

    def _on_subject_select(self, event):
        sel = self.subject_list.curselection()
        if not sel:
            return
        idx = sel[0]
        self.current_subject = self.state.demo_subjects[idx]
        self.selected_subject_label.config(text=f"{self.current_subject.name} ({self.current_subject.current_state})")
        stats = f"Obedience: {self.current_subject.obedience} | Exhibitionism: {self.current_subject.exhibitionism} | Dollification: {self.current_subject.dollification}"
        self.subject_stats.config(text=stats)

        # Personality display
        pers = self.current_subject.personality
        pers_text = (f"Core: {pers.get('Core Erotic Temperament', 'N/A')} | "
                     f"Style: {pers.get('Erotic Social Style', 'N/A')} | "
                     f"Drive: {pers.get('Motivation / Erotic Life Drive', 'N/A')}")
        if hasattr(self, 'personality_label'):
            self.personality_label.config(text=pers_text)
        else:
            # Fallback: append to stats if label doesn't exist
            self.subject_stats.config(text=stats + "\n" + pers_text)

        self.reaction_box.delete("1.0", "end")

    def _send_command(self, event=None):
        if not self.current_subject:
            messagebox.showinfo("Subjects", "Please select a subject first.")
            return
        cmd = self.command_entry.get().strip()
        if not cmd:
            return
        reaction = generate_subject_reaction(self.current_subject, cmd)
        self.reaction_box.delete("1.0", "end")
        self.reaction_box.insert("1.0", reaction)
        self.command_entry.delete(0, "end")

    def _quick_command(self, cmd):
        if not self.current_subject:
            messagebox.showinfo("Subjects", "Please select a subject first.")
            return
        reaction = generate_subject_reaction(self.current_subject, cmd)
        self.reaction_box.delete("1.0", "end")
        self.reaction_box.insert("1.0", reaction)

    def _advance_selected_rd(self):
        sel = self.rd_list.curselection()
        if not sel:
            messagebox.showinfo("R&D", "Select a project first.")
            return
        idx = sel[0]
        if idx >= len(self.state.pipeline):
            return
        proj = self.state.pipeline[idx]
        ok, msg, erotic = advance_rd_phase(self.state, proj.id)
        self._log(msg)
        if erotic:
            self._log("New erotic case study generated from trial.")
        self._refresh_all()

    def _assign_researcher_dialog(self):
        sel = self.rd_list.curselection()
        if not sel:
            messagebox.showinfo("R&D", "Select a project first.")
            return
        idx = sel[0]
        if idx >= len(self.state.pipeline):
            return
        proj = self.state.pipeline[idx]

        dlg = tk.Toplevel(self.root)
        dlg.title("ASSIGN RESEARCHER")
        dlg.configure(bg=BG)
        dlg.geometry("420x320")

        make_label(dlg, f"Assign to: {proj.drug_name}", "Gold.TLabel").pack(padx=12, pady=8)

        names = [t["name"] for t in EROTIC_TALENT_POOL]
        var = tk.StringVar(value=names[0])
        for n in names:
            ttk.Radiobutton(dlg, text=n, variable=var, value=n).pack(anchor="w", padx=20)

        def do_assign():
            proj.assigned_researcher = var.get()
            self._log(f"Assigned {var.get()} to {proj.drug_name}")
            self._refresh_all()
            dlg.destroy()

        make_button(dlg, "ASSIGN", do_assign, accent=CYAN).pack(pady=12)

    def _create_vault_tab(self):
        tab = tk.Frame(self.notebook, bg=BG)
        self.notebook.add(tab, text="  PRODUCT VAULT  ")

        make_label(tab, "LAUNCHED DRUG CATALOG", "Gold.TLabel").pack(anchor="w", padx=12, pady=6)

        self.vault_list = tk.Listbox(tab, height=12, bg=CARD_BG, fg=TEXT, selectbackground=MAGENTA,
                                     font=("Consolas", 10), relief="flat")
        self.vault_list.pack(fill="both", expand=True, padx=12, pady=4)

        # Selection handler to show description
        self.vault_list.bind("<<ListboxSelect>>", self._on_vault_select)

        # Description panel
        make_label(tab, "DRUG PROFILE & MECHANISM", "Gold.TLabel").pack(anchor="w", padx=12, pady=(8,4))
        self.vault_desc = scrolledtext.ScrolledText(tab, height=7, bg="#0f1629", fg=TEXT,
                                                    font=("Consolas", 10), wrap="word", relief="flat")
        self.vault_desc.pack(fill="x", padx=12, pady=4)

        btns = tk.Frame(tab, bg=BG)
        btns.pack(fill="x", padx=12, pady=6)
        make_button(btns, "LAUNCH / ADJUST SELECTED", self._launch_dialog, accent=CYAN).pack(side="left", padx=4)
        make_button(btns, "VIEW FULL EROTIC PROFILE", self._view_drug_erotic, accent="#ff66cc").pack(side="left", padx=4)
        make_button(btns, "COPY DESCRIPTION TO CLIPBOARD", self._copy_vault_desc, accent=GOLD).pack(side="left", padx=4)

        self._refresh_vault = self._refresh_vault_impl

    def _refresh_vault_impl(self):
        self.vault_list.delete(0, "end")
        for drug in self.state.catalog:
            sub = "SUB" if drug.subscription_model else ""
            txt = f"{drug.name} | {drug.category} | Potency {drug.potency:.0f} | Erotic {drug.erotic_intensity:.0f} | ${drug.price_per_dose:.2f} {sub}"
            self.vault_list.insert("end", txt)
        # Clear description when refreshing
        if hasattr(self, 'vault_desc'):
            self.vault_desc.delete("1.0", "end")

    def _launch_dialog(self):
        sel = self.vault_list.curselection()
        if not sel:
            messagebox.showinfo("Vault", "Select a drug first.")
            return
        drug = self.state.catalog[sel[0]]

        dlg = tk.Toplevel(self.root)
        dlg.title(f"LAUNCH / ADJUST — {drug.name}")
        dlg.configure(bg=BG)
        dlg.geometry("480x380")

        make_label(dlg, f"Current Price: ${drug.price_per_dose:.2f}", "TLabel").pack(padx=12, pady=6)
        make_label(dlg, "New Price per Dose", "Small.TLabel").pack(padx=12)
        price_e = tk.Entry(dlg, width=15, bg=PANEL, fg=TEXT)
        price_e.pack(padx=12)
        price_e.insert(0, str(drug.price_per_dose))

        sub_var = tk.BooleanVar(value=drug.subscription_model)
        ttk.Checkbutton(dlg, text="Enable Subscription Model (recurring revenue)", variable=sub_var).pack(padx=12, pady=8)

        def do_launch():
            try:
                new_price = float(price_e.get())
            except:
                new_price = drug.price_per_dose
            ok, msg = launch_drug(self.state, drug.id, new_price, sub_var.get())
            self._log(msg)
            self._refresh_all()
            dlg.destroy()

        make_button(dlg, "UPDATE & LAUNCH", do_launch, accent=CYAN, bold=True).pack(pady=12)

    def _view_drug_erotic(self):
        sel = self.vault_list.curselection()
        if not sel:
            return
        drug = self.state.catalog[sel[0]]
        story = generate_erotic_testimonial(drug, "market")

        # Build full profile text
        desc = DRUG_CATEGORIES.get(drug.category, {}).get("description", "No detailed mechanism available.")
        side_effects = "\n• ".join(drug.side_effects) if drug.side_effects else "No side effect data recorded."

        full_text = f"""DRUG: {drug.name} ({drug.category})

MECHANISM:
{desc}

CURRENT STATS:
• Potency: {drug.potency:.1f}
• Erotic Intensity: {drug.erotic_intensity:.1f}
• Price per Dose: ${drug.price_per_dose:.2f}
• Subscription Model: {"Enabled" if drug.subscription_model else "Disabled"}
• Weeks on Market: {drug.weeks_in_market}
• Total Sold: {drug.total_sold:,}
• Revenue Generated: ${drug.revenue_generated:,.0f}

OBSERVED SIDE EFFECTS:
• {side_effects}

LATEST EROTIC CASE STUDY:
{story}"""

        messagebox.showinfo(f"{drug.name} — Full Profile", full_text[:1800] + "\n\n[Truncated for dialog]")

    def _on_vault_select(self, event):
        """Show description when user selects a drug in the vault list."""
        sel = self.vault_list.curselection()
        if not sel or not hasattr(self, 'vault_desc'):
            return
        drug = self.state.catalog[sel[0]]

        desc = DRUG_CATEGORIES.get(drug.category, {}).get("description", "No detailed mechanism available for this compound.")

        self.vault_desc.delete("1.0", "end")
        self.vault_desc.insert("1.0", f"{drug.name} ({drug.category})\n\n{desc}\n\n")
        self.vault_desc.insert("end", f"Potency: {drug.potency:.0f}  |  Erotic Intensity: {drug.erotic_intensity:.0f}  |  Price: ${drug.price_per_dose:.2f}")
        if drug.subscription_model:
            self.vault_desc.insert("end", "  |  SUBSCRIPTION ENABLED")

    def _copy_vault_desc(self):
        """Copy current description text to clipboard."""
        if not hasattr(self, 'vault_desc'):
            return
        text = self.vault_desc.get("1.0", "end").strip()
        if text:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            self._log("Drug description copied to clipboard.")

    def _create_trials_tab(self):
        tab = tk.Frame(self.notebook, bg=BG)
        self.notebook.add(tab, text="  CLINICAL TRIALS  ")

        make_label(tab, "CLINICAL TRIAL OPERATIONS", "Gold.TLabel").pack(anchor="w", padx=12, pady=8)
        make_label(tab, "Recruit high-suggestibility test subjects to improve R&D speed and erotic data quality.", "Small.TLabel").pack(anchor="w", padx=12)

        btns = tk.Frame(tab, bg=BG)
        btns.pack(pady=20)
        make_button(btns, "RECRUIT HIGH-QUALITY TESTERS ($185k)", lambda: self._recruit_dialog(185000, "high"), accent=MAGENTA, width=32).pack(pady=6)
        make_button(btns, "RECRUIT EXTREME SUBJECTS ($320k)", lambda: self._recruit_dialog(320000, "extreme"), accent="#ff66cc", width=32).pack(pady=6)

        make_label(tab, "Higher quality testers = faster progress + stronger erotic transformation data", "Small.TLabel").pack(padx=12, pady=8)

    def _recruit_dialog(self, budget=185000, quality="high"):
        ok, msg = recruit_testers(self.state, budget, quality)
        self._log(msg)
        self._refresh_all()

    def _create_marketing_tab(self):
        tab = tk.Frame(self.notebook, bg=BG)
        self.notebook.add(tab, text="  SALES & MARKETING  ")

        make_label(tab, "EROTIC MARKETING & DISTRIBUTION", "Gold.TLabel").pack(anchor="w", padx=12, pady=8)
        make_label(tab, "Design campaigns that generate both revenue and usable content for your social channels.", "Small.TLabel").pack(anchor="w", padx=12)

        btns = tk.Frame(tab, bg=BG)
        btns.pack(pady=16)
        make_button(btns, "RUN SOCIAL SEEDING CAMPAIGN", self._run_marketing_campaign, accent=CYAN, width=28).pack(pady=6)
        make_button(btns, "INFLUENCER SAMPLE DROP", self._influencer_drop, accent=MAGENTA, width=28).pack(pady=6)

        make_label(tab, "Successful campaigns generate new erotic testimonials you can use directly in content.", "Small.TLabel").pack(padx=12, pady=12)

    def _run_marketing_campaign(self):
        if not self.state.catalog:
            messagebox.showinfo("Marketing", "Launch at least one drug first.")
            return
        drug = random.choice(self.state.catalog)
        story = generate_erotic_testimonial(drug, "campaign")
        self.state.erotic_logs.append(story)
        self.state.content_fuel += 2
        self._log(f"Marketing campaign launched for {drug.name}. New erotic content generated.")
        self._refresh_all()

    def _influencer_drop(self):
        self.state.cash -= 45000
        story = "Influencer drop: Three mid-tier OnlyFans creators received free samples. Within 48 hours their content shifted heavily toward blank stares, heavy cleavage focus, and 'good girl' roleplay. Engagement exploded."
        self.state.erotic_logs.append(story)
        self.state.content_fuel += 3
        self._log("Influencer sample drop executed. Significant erotic content generated.")
        self._refresh_all()

    def _create_talent_tab(self):
        tab = tk.Frame(self.notebook, bg=BG)
        self.notebook.add(tab, text="  TALENT ROSTER  ")

        make_label(tab, "EROTIC RESEARCH & CLINICAL TALENT", "Gold.TLabel").pack(anchor="w", padx=12, pady=8)

        self.talent_list = tk.Listbox(tab, height=14, bg=CARD_BG, fg=TEXT, selectbackground=CYAN,
                                      font=("Consolas", 10), relief="flat")
        self.talent_list.pack(fill="both", expand=True, padx=12, pady=4)

        for t in EROTIC_TALENT_POOL:
            txt = f"{t['name']} | {t['role']} | Skill {t['skill']} | Suggestibility {t['suggestibility']}"
            self.talent_list.insert("end", txt)

        make_label(tab, "Hire these specialists via R&D assignment dialogs. Higher suggestibility = better trial data.", "Small.TLabel").pack(padx=12, pady=6)

    def _create_intel_tab(self):
        tab = tk.Frame(self.notebook, bg=BG)
        self.notebook.add(tab, text="  MARKET INTEL  ")

        make_label(tab, "COMPETITOR & FETISH TREND INTELLIGENCE", "Gold.TLabel").pack(anchor="w", padx=12, pady=8)
        make_label(tab, "Current Hot Categories: " + ", ".join(self.state.hot_categories), "TLabel").pack(anchor="w", padx=12)

        make_label(tab, "\nTrending in the underground: Hypnotic eye effects, heavy natural cleavage, public obedience triggers, thick thigh exhibitionism.", "Small.TLabel").pack(anchor="w", padx=12, pady=8)
        make_label(tab, "Tip: Focus R&D on high erotic_intensity categories for maximum transformation and content generation.", "Small.TLabel").pack(anchor="w", padx=12)

    def _advance_week(self):
        logs = advance_week(self.state)
        for line in logs:
            self._log(line)
        self._refresh_all()

    def _log(self, text: str):
        print(text)  # Also print to console
        if hasattr(self, 'log_text'):
            self.log_text.insert("end", "\n" + text)
            self.log_text.see("end")

    def _show_erotic_logs(self):
        dlg = tk.Toplevel(self.root)
        dlg.title("EROTIC LOG ARCHIVE — Content Fuel")
        dlg.configure(bg=BG)
        dlg.geometry("780x520")

        txt = scrolledtext.ScrolledText(dlg, bg="#0f1629", fg=TEXT, font=("Consolas", 10), wrap="word")
        txt.pack(fill="both", expand=True, padx=10, pady=10)

        for log in self.state.erotic_logs[-25:]:
            txt.insert("end", log + "\n\n" + "—"*60 + "\n\n")

        make_button(dlg, "CLOSE", dlg.destroy, accent=CYAN).pack(pady=6)

    def _save(self):
        path = filedialog.asksaveasfilename(
            title="Save HypnoDose Game",
            defaultextension=".json",
            initialfile="hypnodose_save.json",
            filetypes=[("JSON", "*.json")]
        )
        if not path:
            return
        saved = save_game(self.state, path)
        self._log(f"Game saved to {os.path.basename(saved)}")

    def _load(self):
        path = filedialog.askopenfilename(
            title="Load HypnoDose Game",
            filetypes=[("JSON", "*.json")]
        )
        if not path:
            return
        try:
            self.state = load_game(path)
            self._refresh_all()
            self._log(f"Game loaded from {os.path.basename(path)}")
        except Exception as e:
            messagebox.showerror("Load Error", str(e))


def main():
    root = tk.Tk()
    app = HypnoDoseGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
