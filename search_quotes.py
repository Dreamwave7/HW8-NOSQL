from models import *
import pprint
from colorit import *


def main():
    while True:
        command = input(color("Enter your command: ",Colors.green))
        if command in ["exit", "."]:
            print(color("Goodbye",Colors.red))
            break

        elif command.startswith("tag:"):
            search = command.split(":")[1]
            res = Quotes.objects(tags = search)
            for quot in res:
                author_id = quot.author.id
                author = Authors.objects(id= author_id)[0]
                print(color(f'''
                \n
                Author = {author.fullname}.
                Quotes = {quot.quote}\n
                ''',Colors.blue
                ))


        else:
            print(color("Wrong command",Colors.red))


if __name__ == "__main__":
    main()
    # id = Authors.objects(fullname="Albert Einstein").first()
    # print(id.id)