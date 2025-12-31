def main():
    amount=int(input("How many people do you want to enter: "))
    with open("golf.txt", "w") as f:
        for i in range(1,amount+1):
            print(f"The player number {i}")
            name=input("Enter player's name: ")
            score=input("Enter player's score: ")
            f.write(f"{name}\n")
            f.write(f"{score}\n")
            f.write("\n")
            print()
    print("All player's information have been copied to golf.txt")
if __name__=="__main__":
    main()

