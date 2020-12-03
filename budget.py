class Category:
  def __init__(self, budget_category):
    self.ledger = list()
    self.balance = 0
    self.budget_category = budget_category

  def __str__(self): #✓
    title = f"{self.budget_category:*^30}\n"
    items = ""
    total = 0
    for i in self.ledger:
      items += f"{str(i['description']).strip('*()')[0:23]:23}" + f"{i['amount']:>7.2f}" + '\n'
      total += i['amount']
      print(i['description'])
    print(title + str(items) + "Total: " + str(total))
    return title + str(items) + "Total: " + str(total)

  def deposit(self, amount, description=''): #✓
    self.ledger.append({'amount': amount, 'description': description})
    self.balance = self.balance + amount

  def check_funds(self, amount):  #✓
    if amount > self.balance: # not enough money
      return False
    else:
      return True

  def withdraw(self, amount, description=''): #✓
    if self.check_funds(amount) == True: # there's enough money in balance
      self.ledger.append({'amount': - amount, 'description': description})
      self.balance = self.balance - amount
      return True
    else:
      return False

  def transfer(self, amount, budget_category): #✓
    if self.check_funds(amount) == True: # there's enough money in balance
      self.withdraw(amount, "Transfer to " + str(budget_category).strip('*').replace('*********\nTotal: 0','')) ###
      print("HERE")
      print(str(budget_category))
      return True
    else:
      return False

  def get_balance(self):
    return self.balance

def round_to_nearest_ten(n):
  if n<10:
    return 0
  return round(n/10.0)*10
  
def create_spend_chart(categories):
  # categories is an array of strs. 
  withdrawals = []

  max_len_category = 0
  bar_chart = 0

  for i in categories:
    # i = deposit
    # each category has a withdraw amount running total, starting at 0
    withdraw_amount = 0

    for j in i.ledger:
      # j = {'amount': 900, 'description': 'deposit'}

      # if the amount for that category is a negative number, meaning it's a withdrawal, not a deposit, then add it to the running total
      if j["amount"]<0:
        withdraw_amount+=-j["amount"]
        bar_chart+=(-j["amount"])

      # i.budget_category = 'auto'
      # for push list containing budget_category and withdrawal amount into withdrawals
    if len(i.budget_category)>max_len_category:
      max_len_category=len(i.budget_category)
    withdrawals.append([i.budget_category,withdraw_amount])

  # now use the withdrawals list, a 2d list containing [buget_category,withdrawal_amount] to create the bar chart
  # round to nearest 10

  for i in withdrawals:
      i.append(round_to_nearest_ten((i[1]/bar_chart)*100))
  bar_chart=""
  bar_chart+="Percentage spent by category\n"
  t=100
  while t>=0:
      
      #print s number and | symbol
      bar_chart+=str(t).rjust(3)+"|"+" "

      #loop for printing 'o' if the percentage>=t

      for i in range(len(withdrawals)):
        if withdrawals[i][2]>=t:
          bar_chart+="o"+"  "
        else:
          bar_chart+="   "
      t-=10
      bar_chart+="\n"

    #add '-' to last lines
  bar_chart+="    "+("-"*10)+"\n"

  loop_var=0

  for i in range(max_len_category):
    bar_chart+="     "
    for j in range(len(withdrawals)):
      #checks if char exists at a length
      if len(withdrawals[j][0])-1<loop_var:
        #if no char exists add empty string and 2 spaces
        bar_chart+="   "
      else:
        #add char 
        bar_chart+=withdrawals[j][0][loop_var]+"  "
    loop_var+=1
    if i!=max_len_category-1:
      bar_chart+="\n"

  print(bar_chart)
  return bar_chart
