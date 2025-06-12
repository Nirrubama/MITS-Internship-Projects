# ------------------------------------------------------------------------------------------------
# 📌 Smart Electricity Usage Tracker

# 🔍 Project Description:
# This project helps users track their daily electricity usage and estimate their monthly bill.
# It's a real-world use case built with Python and offers hands-on exposure to file handling,
# basic data analysis, and plotting graphs using matplotlib. Ideal for internships, portfolios,
# and beginner-level machine learning/data visualization projects.
# ------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

# Reads usage data from file or creates it if missing
def load_usage_data(filename="usage_data.txt"):
    usage = []
    try:
        with open(filename, "r") as f:
            for line in f:
                usage.append(float(line.strip()))
    except FileNotFoundError:
        open(filename, "w").close()  # Create an empty file if not found
    return usage

# Saves today’s electricity usage to file
def save_daily_usage(units, filename="usage_data.txt"):
    with open(filename, "a") as f:
        f.write(f"{units}\n")

# Predicts the monthly electricity bill based on average usage
def predict_bill(usage_list, rate_per_unit=7.5):
    if not usage_list:
        return 0.0
    daily_avg = sum(usage_list) / len(usage_list)
    monthly_estimate = daily_avg * 30
    return round(monthly_estimate * rate_per_unit, 2)

# Plots a graph of the user's daily usage data
def plot_usage(usage_list):
    if not usage_list:
        print("No usage data available to plot.")
        return
    days = list(range(1, len(usage_list) + 1))
    plt.figure(figsize=(8, 4))
    plt.plot(days, usage_list, marker='o', linestyle='-', color='blue')
    plt.title("Electricity Usage Over Days")
    plt.xlabel("Day")
    plt.ylabel("Units Consumed")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# User-facing interaction (console-based)
def main():
    print("\n📊 Smart Electricity Usage Tracker 📊")
    print("====================================")

    usage_data = load_usage_data()

    while True:
        print("\nMenu:")
        print("1. Add today’s electricity usage")
        print("2. View estimated monthly bill")
        print("3. Show usage graph")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            try:
                units = float(input("Enter electricity used today (in units): "))
                save_daily_usage(units)
                usage_data.append(units)
                print("✅ Usage saved successfully.")
            except ValueError:
                print("⚠️ Please enter a valid number.")
        elif choice == "2":
            bill = predict_bill(usage_data)
            print(f"💰 Estimated Monthly Bill: ₹{bill}")
        elif choice == "3":
            plot_usage(usage_data)
        elif choice == "4":
            print("👋 Exiting. Thank you for using the tracker.")
            break
        else:
            print("❌ Invalid choice. Please select between 1 and 4.")

# Start the program
if __name__ == "__main__":
    main()
