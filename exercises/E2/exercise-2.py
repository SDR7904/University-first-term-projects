time = int(input())
# hours, minutes, seconds = 0
days = time // 86400
time %= 86400
hours = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print(f"{hours}:{minutes}:{seconds}")