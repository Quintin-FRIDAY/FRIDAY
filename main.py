from core.assistant import Friday
from core.commands import process


def main():
    friday = Friday()
    friday.boot()
    friday.introduce()

    while True:
        command = input("You > ")

        if command.lower() in ["exit", "quit", "shutdown"]:
            friday.shutdown()
            break

        response = process(command)
        print(f"F.R.I.D.A.Y. > {response}")


if __name__ == "__main__":
    main()