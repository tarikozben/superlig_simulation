# Super Lig 2025-26 Championship Simulator ⚽

A realistic Turkish Super League championship simulation for the 2025-2026 season.

## Features
- **18 Teams** - All current 2025-26 Super Lig teams
- **34-Week Season** - Complete double round-robin tournament
- **Realistic Results** - Home advantage and team strength factors
- **Detailed League Table** - Points, wins, draws, losses, goals, goal difference
- **Championship Winner** - Final season champion announcement

## How to Run
```bash
python super_lig_simulation.py
```

## Sample Output
```
🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
  2025-2026 SUPER LIG SAMPIYONLUK YARISI
🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥

📋 18 takım:
 1. Galatasaray
 2. Fenerbahce
 3. Besiktas
 4. Trabzonspor
 ...

🏆 2025-2026 SUPER LIG FINAL PUAN TABLOSU
================================================================================
Sira Takim              O   G   B   M   A   Y   AV  P  
--------------------------------------------------------------------------------
 1. 🏆 Galatasaray        34  26   5   3  78  32 +45  83
 2. 🥈 Fenerbahce         34  24   7   3  71  28 +43  79
 3. 🥉 Besiktas           34  22   8   4  65  35 +30  74
 ...

🏆 SAMPIYON: GALATASARAY
```

## Teams (2025-26 Season)
- **Big 3:** Galatasaray, Fenerbahce, Besiktas
- **Strong Contenders:** Trabzonspor, Basaksehir
- **Mid-Table:** Goztepe, Rizespor, Kasimpasa, Samsunspor
- **Newly Promoted:** Kocaelispor, Genclerbirligi, Fatih Karagumruk

## Technical Details
- **Python 3.x** required
- **Random simulation** - Different results each run
- **34 matches per team** (17 opponents × 2)
- **3 points for win, 1 for draw, 0 for loss**
- **Ranking:** Points → Goal Difference → Goals Scored

## Simulation Logic
- Teams have strength ratings (60-95)
- Home advantage (+3 strength bonus)
- Random factors for realistic upsets
- Goal calculation based on team strength

---
*Note: This is a simulation for entertainment. Results are randomly generated and do not predict real outcomes.*
