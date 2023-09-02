# phone_usage
Python script to analyze app usage data, calculate median time spent and pickups, and determine time/pickup ratios for different apps.

# Details
This Python code reads data from a CSV file named "app_data.csv," processes it, and then prints aggregated information about various mobile apps. It begins by initializing lists to store time spent and pickups data, along with an empty list for dictionaries to store user data. It then opens the CSV file, reads the data, and creates dictionaries for each user's app usage information, storing it in the user_data_list. Additionally, it calculates the median time spent and pickups.

Next, the code aggregates data for each app by calculating the median time spent, median pickups, and the time/pickup ratio for users of each app. It stores this aggregated data in a list of dictionaries called aggregated_list.

Finally, the code sorts the aggregated_list by the time/pickup ratio in descending order and prints information for apps with more than one user, including the app name, the number of users, and the time/pickup ratio.

Interpreting the output:
- The output will display app names, the number of users for each app, and the time/pickup ratio for apps with more than one user.
- The time/pickup ratio indicates the relationship between the median time spent on the app and the median number of pickups. A higher ratio suggests that users spend more time on the app per pickup.
