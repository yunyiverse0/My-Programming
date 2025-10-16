# A cinema charges different ticket prices based on a person's age:
# • Children under 5 years old can enter for free.
# • People aged 5 to 17 pay $8.
# • Adults aged 18 to 59 pay $12.
# • Seniors aged 60 and above pay $10

n = int(input())

if n < 5:
  print('Ticket price: Free')
elif 5 <= n <= 17:
  print('Ticket price: $8')
elif 18 <= n <= 59:
  print('Ticket price: $12')
else:
  print('Ticket price: $10')
