import ast
import click
import os

categories = {
    'carne': {},
    'peixe': {},
    'vegan': {},
}

@click.group()
def main():
    pass

@main.command()
@click.argument('category')
@click.argument('name')
@click.argument('quantidade')
def add(category, name, quantidade):
    categories = readFile()

    if category in categories:
        if name in categories[category]:
            categories[category][name] = int(categories[category][name]) + int(quantidade)
            saveFile(categories)
            print("adicionou - True - p1")
            print(categories)
        else:
            categories[category][name] = int(quantidade)
            saveFile(categories)
            print("adicionou - True - p2")
            print(categories)
    else:
        categories[category] = {name: quantidade}
        saveFile(categories)
        print("adicionou - True - p3")
        print(categories)

@main.command()
@click.argument('category')
@click.argument('name')
@click.argument('quantidade')
def remove(category, name, quantidade):
    categories = readFile()

    if category in categories:
        if  name in categories[category]:
            if  categories[category][name] - int(quantidade) > 0:
                categories[category][name] = int(categories[category][name]) - int(quantidade)
                saveFile(categories)
                print("removeu - True - p1")
                print(categories)

            elif  categories[category][name] - int(quantidade) == 0:
                del categories[category][name]
                saveFile(categories)
                print("removeu - True - p2")
                print(categories)

            else:
                print(f"O produto {name} na categoria {category} tem menos do que {quantidade} em stock, por favor verifique a quantidade que deseja remover.")
        else:
            print(f"O produto {name} na categoria {category} não existe.")
    else:
        print(f"A categoria {category} não existe.")



@main.command()
def read():
    print("reading...")
    print(readFile())


@main.command()
def reset():
    if os.path.exists("items.txt"):
        os.remove("items.txt")
        readFile()


def saveFile(categories):
    file = open('items.txt','w')
    file.write(str(categories))
    file.close()


def readFile():
    try:
        if not os.path.exists('items.txt'):
            with open('items.txt', 'w') as fp:
                pass

        with open('items.txt', 'r') as file:
            result = file.read().strip()
        
        if result:
            result_dict = ast.literal_eval(result)
            return result_dict
        
        return categories
        
    except FileNotFoundError:
        print("File not found.")
    

if __name__ == "__main__":
    main()
