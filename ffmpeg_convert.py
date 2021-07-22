command =["ffmpeg", "-i", "Beauty_1920x1080_120fps_420_8bit_YUV.y4m", "-c:v", "h264", "-preset", "medium", "-bf", "0", "medium_h264.mp4"] 
times = 5

import subprocess
import time

start_time = (int(time.time()))

for i in range(times):
	current_command = command[:-1]+[str(i)+"_"+command[-1],]
	print(current_command)
	subprocess.run(current_command)

end_time = (int(time.time()))

print("start",start_time)
print("end",end_time)
