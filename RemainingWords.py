alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def GetRemainingGuesses(letters):
  guesses = []
  for i in range(0, len(letters[0])):
    for j in range(0, len(letters[1])):
      for k in range(0, len(letters[2])):
        for l in range(0, len(letters[3])):
          for m in range(0, len(letters[4])):
            newGuess = letters[0][i]+letters[1][j]+letters[2][k]+letters[3][l]+letters[4][m]
            guesses.append(newGuess)
  return guesses

def GetGuessesWithNecessaryCharacters(allGuesses, letters):
  allGuessesList = [x for x in allGuesses]
  
  flatLetterList = [x for sublist in letters for x in sublist]
  allUniqueLetters = GetDuplicateFreeList(flatLetterList)
  
  excludedCharacterListAtEachPosition = []
  for i in range(0, len(letters)):
    excludedCharacterListAtEachPosition.append(GetListWithoutSelectedLetters(allUniqueLetters, letters[i]))
  
  print(f"Excluded characters at each position: \n{excludedCharacterListAtEachPosition}")
  
  guessesMissingYellowLetters = []
  for i in range(0, len(excludedCharacterListAtEachPosition)):
    availableCharactersAtPosition = len(allUniqueLetters) - len(excludedCharacterListAtEachPosition[i])
    if (excludedCharacterListAtEachPosition[i] == [] or availableCharactersAtPosition == 1):
      continue
    else:
      for j in range(0, len(allGuessesList)):
        for k in range(0, len(excludedCharacterListAtEachPosition[i])):
          if (excludedCharacterListAtEachPosition[i][k] not in allGuessesList[j]):
            guessesMissingYellowLetters.append(allGuessesList[j])
  
  print(f"Guesses without regard to yellow letters: \n{guessesMissingYellowLetters}")
  guessesIncludingAllYellowLetters = [x for x in allGuessesList if x not in guessesMissingYellowLetters]
  return guessesIncludingAllYellowLetters

def GetTestLetters():
  remainingLetters = ["q","w","e","y","u","i","a","f","g","h","j","k","z","x","c","v","m"]
  firstLetterOptions = remainingLetters + ["t"]
  secondLetterOptions = ["a"]
  thirdLetterOptions = remainingLetters
  fourthLetterOptions = ["i"]
  fifthLetterOptions = remainingLetters + ["t"]
  return [firstLetterOptions,secondLetterOptions,thirdLetterOptions,fourthLetterOptions,fifthLetterOptions]

def GetInputs():
  inputMode = input("Input mode? 1 (manual), 2 (Brady test): ")
  
  if inputMode == "1":
    print("Input can be prefixed by \"-\" as a shortcut to use the full alphabet minus the letters following the \"-\". For example, an input of -abcdefg will indicate the letters hijklm...z.\n")
    remainingLetters = GetAllRemainingLetters("If using this to get the set of answers before your last guess, ignore your last guess. \nIf using this to solve for your next guess, look at your latest guess. \nPlease enter all remaining letters (green, yellow, and unused (OR use \"-\" before eliminated (gray) letters)): ")
    firstLetterOptions = GetPositionLetters("In the first letter spot, enter remaining options (if green, enter that letter only, otherwise, enter other greens, yellows, and unused the next guess could have (OR use \"-\" before eliminated (gray) letters)): ", remainingLetters)
    secondLetterOptions = GetPositionLetters("In the second letter spot, enter remaining options (if green, enter that letter only, otherwise, enter other greens, yellows, and unused the next guess could have (OR use \"-\" before eliminated (gray) letters)): ", remainingLetters)
    thirdLetterOptions = GetPositionLetters("In the third letter spot, enter remaining options (if green, enter that letter only, otherwise, enter other greens, yellows, and unused the next guess could have (OR use \"-\" before eliminated (gray) letters)): ", remainingLetters)
    fourthLetterOptions = GetPositionLetters("In the fourth letter spot, enter remaining options (if green, enter that letter only, otherwise, enter other greens, yellows, and unused the next guess could have (OR use \"-\" before eliminated (gray) letters)): ", remainingLetters)
    fifthLetterOptions = GetPositionLetters("In the fifth letter spot, enter remaining options (if green, enter that letter only, otherwise, enter other greens, yellows, and unused the next guess could have (OR use \"-\" before eliminated (gray) letters)): ", remainingLetters)
    return [firstLetterOptions,secondLetterOptions,thirdLetterOptions,fourthLetterOptions,fifthLetterOptions]
  elif inputMode == "2":
    return GetTestLetters()
  else:
    print("Invalid mode selected. Please try again.")
    GetInputs()

def IsInTheAlphabet(inputLetters):
  for i in inputLetters:
    if (i not in alphabet):
      return False
  return True

def GetAllRemainingLetters(message):
  lettersReceived = input(f"{message} ")
  if (HasSubtraction(lettersReceived)):
    excludedLettersOnly = GetLettersWithoutSubtractionCharacter(GetDuplicateFreeList(lettersReceived))
    listWithoutExcludedLetters = GetListWithoutSelectedLetters(alphabet, excludedLettersOnly)
    return listWithoutExcludedLetters
  elif (IsInTheAlphabet(lettersReceived)):
    return lettersReceived
  else:
    print("Input invalid. Please try again.")
    GetAllRemainingLetters(message)

def GetPositionLetters(message, remainingLetters):
  lettersReceived = input(f"{message} ")
  
  if (IsValidInput(lettersReceived)):
    isSubtraction = HasSubtraction(lettersReceived)
    lettersReceived = GetLettersWithoutSubtractionCharacter(GetDuplicateFreeList(lettersReceived))
    if (isSubtraction):
      return GetListWithoutSelectedLetters(remainingLetters, lettersReceived)
    else:
      return lettersReceived
  else:
    print("Input invalid. Please try again.")
    GetPositionLetters(message)

def IsValidInput(letters):
  letters = GetDuplicateFreeList(letters)
  if HasSubtraction(letters):
    letters = GetLettersWithoutSubtractionCharacter(letters)
  return IsInTheAlphabet(letters)

def GetLettersWithoutSubtractionCharacter(letters):
  letters = "".join(letters)
  return [x for x in letters if x not in "-"]

def GetDuplicateFreeList(letters):
  duplicateFreeSet = set(letters)
  duplicateFreeList = [x for x in duplicateFreeSet]
  return duplicateFreeList

def HasSubtraction(letters):
  return "-" in letters

def GetListWithoutSelectedLetters(letterList, lettersToRemove):
  return [x for x in letterList if x not in lettersToRemove]

def GetGuessesIntersectionWithRealWords(guesses, realWords):
  remainingGuessesSet = set()
  for item in guesses:
      remainingGuessesSet.add(item)

  realWordsSet = set()
  for item in realWords:
      realWordsSet.add(item)
  
  return remainingGuessesSet.intersection(realWordsSet)
  
def main():
  file = open("words.txt")
  inputData = file.readlines()
  dictionary = [x.strip() for x in inputData]

  letters = GetInputs()
  remainingGuesses = GetRemainingGuesses(letters)
  print(f"{len(remainingGuesses)} remaining combinations, word or otherwise: \n{remainingGuesses}")

  realWordsRemainingSet = GetGuessesIntersectionWithRealWords(remainingGuesses, dictionary)
  print(realWordsRemainingSet)

  smartGuesses = GetGuessesWithNecessaryCharacters(realWordsRemainingSet, letters)
  print(f"Guesses with yellow letters: \n{sorted(smartGuesses)}")
  input("Press enter key to rerun.")
  main()

main()