from core.assistant import Friday

def main():
    friday = Friday()
    friday.boot()

    while True:
        command = input("You > ")

        if command.lower() in ["exit", "quit", "shutdown"]:
            friday.shutdown()
            break

        print(f"F.R.I.D.A.Y. > I heard: {command}")

if __name__ == "__main__":
    main()