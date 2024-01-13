
import g4f

zapros = input("Введите запрос: ")

response = g4f.ChatCompletion.create(
  model="gpt-4-0613",
  provider=g4f.Provider.GeekGpt,
  messages=[{"role": "user", "content": zapros}],
)
print(response)