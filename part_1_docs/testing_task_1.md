### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

  # there is a syntax error; 
  # line 24 the else should be followed by a :
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   
  # typing errors;
  # line 32 should read def instead of dif and card1 and card2 should be separated by a comma
  # line 34 card1 should be returned not card
  # indent error; 
  # if and else statements should be indented from the def function line.
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  


# a value needs to be assigned to the total variable (total = 0)
# return needs to be contained in () and total value (which would be a integer) converted to a string i.e.
# i.e. return ("You have a total of" + int(total))
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
