full_name = "Bruce William Wayne"
name_parts = full_name.+split()
initials = ""

for part in name_parts:
    initials += part[0].upper() + ". "

print("Initials:", initials.strip())
