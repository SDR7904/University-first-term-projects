time = int(input())
# hours, minutes, seconds = 0
hours = time // 3600
time = time % 3600
minutes = time // 60
time = time % 60
seconds = time
print(f"{hours}:{minutes}:{seconds}")