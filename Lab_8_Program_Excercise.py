def main():
    name=input("Enter your full name: ")
    parts=name.split()
    initials=""
    for part in parts:
        initials+=part[0].upper()+". "
    print(initials.strip())

if __name__ == "__main__":
    main()