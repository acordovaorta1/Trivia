import requests

def trivia_fetch(num):
    url = "https://opentdb.com/api.php?amount=" + str(num)
    response = requests.get(url)
    trivia = response.json()
    return trivia


def main():

    print("Hello learners!")


    cantidad = int(input("¿Cuántas preguntas quieres? "))
    trivia = trivia_fetch(cantidad)
    print(trivia)
    

if __name__=="__main__":
  main()