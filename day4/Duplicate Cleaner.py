raw_logs=["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
print(raw_logs)
unique_users=set(raw_logs)
check_id = input("Enter User ID to check: ")
print(f"Is {check_id} in unique_users? ", check_id in unique_users)
print("Original list count:", len(raw_logs))
print("Unique users count:", len(unique_users))
print("Unique User IDs:", unique_users)
