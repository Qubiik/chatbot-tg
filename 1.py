import g4f


g4f.debug.logging = True

proga = True


def gpt():
  zapros = input("Введите запрос: ")
  response = g4f.ChatCompletion.create(
      model="gpt-4-0613",
      provider=g4f.Provider.GeekGpt,
      messages=[{"role": "user", "content": zapros}],
  )
  print(response)
while proga == True:
  gpt()