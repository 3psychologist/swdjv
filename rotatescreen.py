import time, rotatescreen as rs

pd= rs.get_primary_display()
angle=[90,180,270,0]
for i in range(12):
    for x in angle:
        pd.rotate_to(x)
        time.sleep(0.5)