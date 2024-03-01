print("\n")
print("\tGame Start\nNow the task is to move all of them to the right side of the river")
print("rules:\n1. The boat can carry at most two people\n2. If cannibals num greater than missionaries then the cannibals would eat the missionaries\n3. The boat cannot cross the river by itself with no people on board")

lM = 3  # Left side Missionaries number
lC = 3  # Left side Cannibals number
rM = 0  # Right side Missionaries number
rC = 0  # Right side Cannibals number

k = 0

print("\nM M M C C C | --- | \n")

try:
    while True:
        while True:
            print("Left side -> right side river travel")
            uM = int(input("Enter number of Missionaries to travel => "))
            uC = int(input("Enter number of Cannibals to travel => "))

            if uM == 0 and uC == 0:
                print("Empty travel not possible. Please re-enter.")
            elif (uM + uC) <= 2 and (lM - uM) >= 0 and (lC - uC) >= 0:
                break
            else:
                print("Wrong input. Please re-enter.")

            lM -= uM
            lC -= uC
            rM += uM
            rC += uC

            print("\n")
            for _ in range(lM):
                print("M ", end="")
            for _ in range(lC):
                print("C ", end="")
            print("| --> | ", end="")
            for _ in range(rM):
                print("M ", end="")
            for _ in range(rC):
                print("C ", end="")
            print("\n")

            k += 1

            if lC == 3 and lM == 1 or lC == 3 and lM == 2 or lC == 2 and lM == 1 or rC == 3 and rM == 1 or rC == 3 and rM == 2 or rC == 2 and rM == 1:
                print("Cannibals eat missionaries. You lost the game.")
                break

        if (rM + rC) == 6:
            print("You won the game! Congrats.")
            print("Total attempts:", k)
            break

        while True:
            print("Right side -> Left side river travel")
            userM = int(input("Enter number of Missionaries to travel => "))
            userC = int(input("Enter number of Cannibals to travel => "))

            if userM == 0 and userC == 0:
                print("Empty travel not possible. Please re-enter.")
            elif (userM + userC) <= 2 and (rM - userM) >= 0 and (rC - userC) >= 0:
                break
            else:
                print("Wrong input. Please re-enter.")

            lM += userM
            lC += userC
            rM -= userM
            rC -= userC

            k += 1

            print("\n")
            for _ in range(lM):
                print("M ", end="")
            for _ in range(lC):
                print("C ", end="")
            print("| <-- | ", end="")
            for _ in range(rM):
                print("M ", end="")
            for _ in range(rC):
                print("C ", end="")
            print("\n")

        if lC == 3 and lM == 1 or lC == 3 and lM == 2 or lC == 2 and lM == 1 or rC == 3 and rM == 1 or rC == 3 and rM == 2 or rC == 2 and rM == 1:
            print("Cannibals eat missionaries. You lost the game.")
            break

except ValueError:
    print("\nInvalid input. Please retry.")
