email_count = 0

with open("mbox.txt", "r") as file:

    for line in file:

        if line.startswith("From "):
            parts = line.split()
            
            if len(parts) >= 2:
                sender_email = parts[1]
                print(sender_email)
                email_count = email_count+1

print(f"Total {email_count} email addresses were printed")