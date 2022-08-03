conflicts = (check_conflicts(["192.168.4.0/23","192.168.1.0/22"], quiet=True))
print(f"\nConflict found : {conflicts}\n")