from utils import load_data, export_to_csv
from analysis.batting import top_run_scorers, top_six_hitters
from analysis.teams import top_winning_teams
from analysis.visualize import plot_bar

def menu():
    print("\n📊 IPL Data Analyzer")
    print("1. Top Run Scorers")
    print("2. Top Six Hitters")
    print("3. Top Teams by Wins")
    print("4. Exit")

def run():
    deliveries, matches = load_data()

    while True:
        menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            data = top_run_scorers(deliveries)
            print(data)
            export_to_csv(data, "top_run_scorers.csv")
            plot_bar(data, "Top Run Scorers", "Batsman", "Runs")

        elif choice == '2':
            data = top_six_hitters(deliveries)
            print(data)
            export_to_csv(data, "top_six_hitters.csv")
            plot_bar(data, "Top Six Hitters", "Batsman", "Sixes")

        elif choice == '3':
            data = top_winning_teams(matches)
            print(data)
            export_to_csv(data, "top_winning_teams.csv")
            plot_bar(data, "Top Winning Teams", "Team", "Wins")

        elif choice == '4':
            print("Exiting the IPL Data Analyzer. Goodbye! 👋")
            break
        else:
            print(" ❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    run()