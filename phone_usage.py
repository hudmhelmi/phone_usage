import csv
import statistics

# Initialize lists to store time spent and pickups data
time_spent_data = []
pickup_data = []

# Initialize an empty list to store dictionaries
user_data_list = []

# Open the CSV file and read data
with open("app_data.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    # Iterate through each row in the CSV file
    for user in reader:
        # Create a dictionary to store app data for the current user
        user_data = {
            user["Most Used App"] + " (time)": user["Time Spent (hrs)"],
            user["2nd Most Used App"] + " (time)": user["2nd Time Spent (hrs)"],
            user["3rd Most Used App"] + " (time)": user["3rd Time Spent (hrs)"],
            user["App with Highest Usage"] + " (pickups)": user["Pickups"],
            user["App with 2nd Highest Usage"] + " (pickups)": user["2nd Pickups"],
            user["App with 3rd Highest Usage"] + " (pickups)": user["3rd Pickups"],
        }

        # Append the dictionary to the app_data_list
        user_data_list.append(user_data)

        # Append time spent and pickups data to the respective lists
        time_spent_data.append(float(user["Time Spent (hrs)"]))
        try:
            pickup_data.append(int(user["Pickups"]))
        except ValueError:
            pickup_data.append(1)

# Calculate median time spent and median pickups
median_time_spent = statistics.median(time_spent_data)
median_pickups = statistics.median(pickup_data)

# Dictionary to store aggregated data
app_aggregate_data = {}

# Iterate through the data
for user_data in user_data_list:
    for key, value in user_data.items():
        app_name, data_type = key.split(" (")
        data_type = data_type[:-1]  # Remove the closing parenthesis from data_type

        if app_name.lower() not in app_aggregate_data:
            app_aggregate_data[app_name.lower()] = {"time": [], "pickups": [], "users": 0}

        try:
            if data_type == "time":
                app_aggregate_data[app_name.lower()]["time"].append(float(value))
            elif data_type == "pickups":
                app_aggregate_data[app_name.lower()]["pickups"].append(int(value))

        except ValueError:
            pass

        app_aggregate_data[app_name.lower()]["users"] += 1  # Count users for this app

# Create a list of dictionaries for aggregated data
aggregated_list = []
for app_name, app_data in app_aggregate_data.items():
    # Calculate the median time spent and median pickups for this app
    try:
        median_time_spent_app = statistics.median(app_data["time"])
    except statistics.StatisticsError:
        pass
    try:
        median_pickups_app = statistics.median(app_data["pickups"])
    except statistics.StatisticsError:
        median_pickups_app = 1

    # Calculate the time/pickup ratio using medians
    try:
        time_pickup_ratio = median_time_spent_app / median_pickups_app
    except ZeroDivisionError:
        time_pickup_ratio = median_time_spent_app / 1

    aggregated_list.append(
        {
            "app_name": app_name,
            "median_time_spent": median_time_spent_app,
            "median_pickups": median_pickups_app,
            "num_users": app_data["users"],
            "time/pickup ratio": time_pickup_ratio,
        }
    )

# Sort the aggregated_list by time/pickup ratio in descending order
aggregated_list.sort(key=lambda x: x["time/pickup ratio"], reverse=True)

# Print the aggregated data for apps with more than 5 users
for app_data in aggregated_list:
    if app_data["num_users"] > 1:
        print(f"App Name: {app_data['app_name']}")
        # print(f"Median Time Spent (hrs): {app_data['median_time_spent']:.2f}")
        # print(f"Median Pickups: {app_data['median_pickups']:.2f}")
        print(f"Number of Users: {app_data['num_users']}")
        print(f"Time/Pickup Ratio: {app_data['time/pickup ratio']:.2f}")
        print("-" * 20)
