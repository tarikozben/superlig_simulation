import random
import time as time_module
from datetime import datetime

# 2025-26 Süper Lig Takımları (18 takım)
super_lig_teams_2025 = {
    "Galatasaray": {"city": "Istanbul", "strength": 95, "star_player": "Victor Osimhen"},
    "Fenerbahce": {"city": "Istanbul", "strength": 92, "star_player": "Jhon Duran"},
    "Besiktas": {"city": "Istanbul", "strength": 88, "star_player": "Ciro Immobile"},
    "Trabzonspor": {"city": "Trabzon", "strength": 85, "star_player": "Simon Banza"},
    "Basaksehir": {"city": "Istanbul", "strength": 82, "star_player": "Krzysztof Piatek"},
    "Goztepe": {"city": "Izmir", "strength": 78, "star_player": "Romulo"},
    "Rizespor": {"city": "Rize", "strength": 76, "star_player": "Adolfo Gaich"},
    "Kasimpasa": {"city": "Istanbul", "strength": 75, "star_player": "Haris Hajradinovic"},
    "Samsunspor": {"city": "Samsun", "strength": 74, "star_player": "Moussa Djenepo"},
    "Eyupspor": {"city": "Istanbul", "strength": 72, "star_player": "Emre Akbaba"},
    "Antalyaspor": {"city": "Antalya", "strength": 73, "star_player": "Sam Larsson"},
    "Alanyaspor": {"city": "Antalya", "strength": 71, "star_player": "Sergio Cordova"},
    "Kayserispor": {"city": "Kayseri", "strength": 70, "star_player": "Stephane Bahoken"},
    "Gaziantep FK": {"city": "Gaziantep", "strength": 69, "star_player": "Deian Sorescu"},
    "Konyaspor": {"city": "Konya", "strength": 68, "star_player": "Sokol Cikalleshi"},
    "Kocaelispor": {"city": "Kocaeli", "strength": 65, "star_player": "Ahmet Calik"},  # Yeni çıkan
    "Genclerbirligi": {"city": "Ankara", "strength": 64, "star_player": "Rahman Bugra Cagiran"},  # Yeni çıkan
    "Fatih Karagumruk": {"city": "Istanbul", "strength": 63, "star_player": "Andrea Bertolacci"}  # Yeni çıkan
}


def simulate_season():
    """Tam sezon simülasyonu - 34 hafta"""
    # Her takım diğer takımlarla 2 kez oynayacak (ev-deplasman)
    matches_per_team = 34  # 17 takımla 2'şer maç

    # Puan tablosu
    league_table = {}
    for team in super_lig_teams_2025.keys():
        league_table[team] = {
            "points": 0,
            "wins": 0,
            "draws": 0,
            "losses": 0,
            "goals_for": 0,
            "goals_against": 0,
            "matches_played": 0
        }

    print("🏟️  2025-2026 SUPER LİG SEZONU BAŞLIYOR!")
    print("=" * 60)
    print("⚽ Sezon simulasyonu calışıyor...")
    time_module.sleep(2)

    # Sezon simülasyonu
    total_matches = 0
    for week in range(1, 35):  # 34 hafta
        # Her hafta rastgele maçlar
        teams_list = list(super_lig_teams_2025.keys())
        random.shuffle(teams_list)

        # Haftalık maçlar (9 maç - 18 takım)
        for i in range(0, len(teams_list) - 1, 2):
            if i + 1 < len(teams_list):
                home_team = teams_list[i]
                away_team = teams_list[i + 1]

                # Maç simülasyonu
                home_strength = super_lig_teams_2025[home_team]["strength"]
                away_strength = super_lig_teams_2025[away_team]["strength"]

                # Ev sahibi avantajı
                home_strength += 3

                # Gol hesaplama
                home_attack = (home_strength + random.randint(-10, 15)) / 25
                away_attack = (away_strength + random.randint(-10, 15)) / 25

                home_goals = max(0, int(home_attack + random.uniform(-0.5, 1.5)))
                away_goals = max(0, int(away_attack + random.uniform(-0.5, 1.5)))

                # Puan hesaplama
                if home_goals > away_goals:  # Ev sahibi kazandı
                    league_table[home_team]["points"] += 3
                    league_table[home_team]["wins"] += 1
                    league_table[away_team]["losses"] += 1
                elif away_goals > home_goals:  # Deplasman kazandı
                    league_table[away_team]["points"] += 3
                    league_table[away_team]["wins"] += 1
                    league_table[home_team]["losses"] += 1
                else:  # Berabere
                    league_table[home_team]["points"] += 1
                    league_table[away_team]["points"] += 1
                    league_table[home_team]["draws"] += 1
                    league_table[away_team]["draws"] += 1

                # İstatistikler
                league_table[home_team]["goals_for"] += home_goals
                league_table[home_team]["goals_against"] += away_goals
                league_table[away_team]["goals_for"] += away_goals
                league_table[away_team]["goals_against"] += home_goals
                league_table[home_team]["matches_played"] += 1
                league_table[away_team]["matches_played"] += 1

                total_matches += 1

    return league_table


def calculate_goal_difference(stats):
    """Gol averajı hesapla"""
    return stats["goals_for"] - stats["goals_against"]


def print_league_table(league_table):
    """Puan tablosunu yazdır"""
    print("\n" + "=" * 80)
    print("🏆 2025-2026 SUPER LIG FINAL PUAN TABLOSU")
    print("=" * 80)

    # Sıralama: Puan -> Gol Averajı -> Atılan Gol
    sorted_teams = sorted(league_table.items(),
                          key=lambda x: (x[1]["points"],
                                         calculate_goal_difference(x[1]),
                                         x[1]["goals_for"]),
                          reverse=True)

    print(f"{'Sira':<4} {'Takim':<18} {'O':<3} {'G':<3} {'B':<3} {'M':<3} {'A':<3} {'Y':<3} {'AV':<4} {'P':<3}")
    print("-" * 80)

    for pos, (team, stats) in enumerate(sorted_teams, 1):
        gd = calculate_goal_difference(stats)

        # Pozisyon emojileri
        if pos == 1:
            emoji = "🏆"
        elif pos == 2:
            emoji = "🥈"
        elif pos == 3:
            emoji = "🥉"
        elif pos <= 4:
            emoji = "🟢"  # Avrupa Ligi
        elif pos >= 16:
            emoji = "🔴"  # Küme düşme
        else:
            emoji = "  "

        print(f"{pos:2d}. {emoji} {team:<18} {stats['matches_played']:2d} "
              f"{stats['wins']:2d} {stats['draws']:2d} {stats['losses']:2d} "
              f"{stats['goals_for']:2d} {stats['goals_against']:2d} "
              f"{gd:+3d} {stats['points']:2d}")

    # Sadece şampiyon
    champion = sorted_teams[0][0]
    print(f"\n🏆 ŞAMPİYON: {champion.upper()}")


def main():
    """Ana simülasyon fonksiyonu"""
    print("🔥" * 25)
    print("  2025-2026 SUPER LIG SAMPIYONLUK YARISI")
    print("🔥" * 25)
    print(f"\n📋 {len(super_lig_teams_2025)} takım:")

    # Sadece takım isimlerini listele
    for i, team in enumerate(super_lig_teams_2025.keys(), 1):
        print(f"{i:2d}. {team}")

    # Sezon simülasyonu
    league_table = simulate_season()

    # Sonuçları yazdır
    print_league_table(league_table)


# Simülasyonu çalıştır
if __name__ == "__main__":
    main()