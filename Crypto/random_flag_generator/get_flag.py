import random 
import time 
import hashlib

# Gets the current time
seed = round(time.time())

# Seed Seen before
seen_before = [0.33567959567961436,0.8913897703358419,0.3032054069265432,0.6860829464688437,0.2658087107328536,0.8903005048882441,0.914630909612433,0.9688578899818961,0.7925090397955323,0.10136501216336935,0.568451491382639,0.16898065821921437,0.5541712073794856,0.02992636121679015,40.18218590474521223,0.49713845657579536,0.7631162105077507,0.7386939443532723,0.5815609491717452,0.5905894610211082,0.09018146469820387]

# Seed provide flag
seed = 1646437241

while True:
    # print(f"{seed=}")
    # creating a random no. with help of seed
    random.seed(seed, version=2)
    
    found_matches = True
    for i in range(len(seen_before)):
        rand = random.random()
        if rand == seen_before[i] :
            print("Seen before hash")
            print(seed)
            continue
        else:
            found_matches = False
            print("d")
            break
    if not found_matches:
        seed-=1
        # print('not found')
        continue
    else:
        print("Found match !")
        print(seed)
        break

    # creating flag hash
    # has = hashlib.sha256(str(rand).encode()).hexdigest()
    # flag = f"CTF{{{has}}}"
    # if "7a2" in has:
    #     with open("./flag", "w") as f:
    #         f.write(flag)
    #         break
    # else:
    #     print(f"Bad random value: {rand}")

