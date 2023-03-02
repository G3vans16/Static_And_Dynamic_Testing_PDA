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


  def check_for_ace(self, card):
    if card.value = 1:  #Syntax Error: Should use '==' to compare, rather than '='
      return True
    else  #Syntax Error: Else should be preceded by a ':'
      return False
   

  dif highest_card(self, card1 card2):  #'def' has been misspelled as as 'dif', and there is no comma between card1 and card2
  if card1.value > card2.value: #code needs to be indented
    return card   #'card' doesn't exist, 'card1' should be returned
  else:
    return card2
  


def cards_total(self, cards):
  total   #Should be initialised as 'total = 0'
  for card in cards:
    total += card.value
    return "You have a total of" + total  #This line should be outside the for loop, otherwise the loop will never move passed the first iteration. There should also be a space at the end of the string for better string concatenation
  
```
