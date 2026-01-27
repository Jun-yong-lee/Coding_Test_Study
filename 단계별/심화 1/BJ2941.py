import sys
input = sys.stdin.readline

cri_alpha = input().rstrip()

presets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for each_preset in presets:
    cri_alpha = cri_alpha.replace(each_preset, "a")     

print(len(cri_alpha))