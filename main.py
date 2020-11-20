#Alex Lim
#MatterCombination
#The program simulates calorimetry through calculations to predict the resultant mass and temperature when mixing a substance.  Water is preprogrammed, but it can also combine any other substance after being given the necessary information which it asks for.  The program creates a GUI which allows the user to give and see information.
#12/16/19 (16 December 2019)

from tkinter import *
import tkinter

matterKelvinTemperatures = []
matterMasses = []
sortedMatterKelvinTemperatures = []
sortedMasses = []
#default values are for water
#for specific heat capacity of phases of water:
#https://chem.libretexts.org/Bookshelves/Introductory_Chemistry/Book%3A_Introductory_Chemistry_(CK-12)/17%3A_Thermochemistry/17.04%3A_Heat_Capacity_and_Specific_Heat
SpecificHeatCapacity_Solid = 2.06 #in J/g/K
SpecificHeatCapacity_Liquid = 4.18 #in J/g/K
SpecificHeatCapacity_Gas = 1.87 #in J/g/K
#for enthalpy of fusion and vaporization of water:
#https://gchem.cm.utexas.edu/data/section2.php?target=heat-transition.php
enthalpyOfFusion = 334 #in J/g
enthalpyOfVaporization = 2260 #in J/g
freezingPoint = 273.15 #in K
boilingPoint = 373.15 #in K
userMatter = "water"
temperatureUnits = "Kelvin"
matterTemperatureFinalKelvin = 0 #in K
matterMassTotal = 0


def main():
  global matterKelvinTemperatures
  global matterMasses
  global userMatter
  global temperatureUnits
  global matterTemperatureFinalKelvin
  """
  temperatureUnits = welcome()
  numBodiesErrors = True
  while numBodiesErrors:
    numBodies = int(input("Please enter how many bodies of " + userMatter + " you would like to combine: "))
    #checking for errors with the numBodies input
    if numBodies == 0:
      print("I apologize.\nI am unable to comprehend how to combine 0 bodies of " + userMatter + ".")
      print("Please re-enter the correct number of bodies of " + userMatter + ".\n\n")
    elif numBodies < 0:
      print("I apologize.\nI am unable to comprehend how to combine negative bodies of " + userMatter + ".")
      print("Please re-enter the correct number of bodies of " + userMatter + ".\n\n")
    else:
      numBodiesErrors = False
  #body of matter inputs
  i = 1
  while i <= numBodies:
    bodyMatterErrors = True
    while bodyMatterErrors:
      #getting input for temperature of the matter
      temperatureValue = float(input("\nPlease enter the temperature of " + userMatter + " #" + str(i) + ": "))
      #getting input for the mass of the matter
      matterMass = float(input("Please enter the mass in grams of " + userMatter + " #" + str(i) + ": "))
      #converting temperature from the user stated temperature to Celsius
      temperatureValueCelsius = temperatureConversionToCelsius(temperatureUnits, temperatureValue)
      #converting temperature from Celsius to Kelvin
      temperatureValueKelvin = convertCelsiusToKelvin(temperatureValueCelsius)
      #checking for errors with the inputs
      if temperatureValueKelvin < 0:
        print("I apologize.\nI am unable to comprehend temperatures below absolute zero.")
      elif matterMass < 0:
        print("I apologize.\nI am unable to comprehend how to use negative masses of " + userMatter + ".")
      elif matterMass == 0:
        print("I apologize.\nI am unable to comprehend how to use 0 grams of " + userMatter + ".")
      else:
        #there are no errors found for this body of matter, clear to proceed
        bodyMatterErrors = False
      if bodyMatterErrors:
        #there are errors found for this body of matter, need to re-enter the information
        print("Please re-enter the correct information for " + userMatter + " #" + str(i) + ".\n\n")
    #adding the temperature of the matter to the global matrix
    matterKelvinTemperatures.append(temperatureValueKelvin)
    #adding the mass of the matter to the global matrix
    matterMasses.append(matterMass)
    #checking what phase the matter is in
    matterState = matterPhase(temperatureValueKelvin)
    #telling user what the phase that the matter is in
    print("" + userMatter + " #" + str(i) + " is " + str(matterState) + ".")
    i = i + 1
  #combining matrices of Kelvin temperatures and masses into a tuple
  listSorting()
  matterTemperatureFinalKelvin = matterCombination()
  """
  #starts GUI
  welcomeButton()


def programEnding():
  global matterKelvinTemperatures
  global matterMasses
  global userMatter
  global temperatureUnits
  global matterTemperatureFinalKelvin
  global matterMassTotal
  numBodies = len(matterKelvinTemperatures)
  master = Tk()
  resultsBox = Listbox(master, width = 100)
  #displaying the total mass of the matter
  print("\n\nThe total mass of " + userMatter + " is " + str(round(matterMassTotal, 2)) + " grams.")
  resultsBox.insert(1, "The total mass of " + userMatter + " is " + str(round(matterMassTotal, 2)) + " grams.")
  #checking if matterTemperatureFinalKelvin is not an exception
  if matterTemperatureFinalKelvin != "isSolidAtFreezingPoint" and matterTemperatureFinalKelvin != "isLiquidAtBoilingPoint":
    #converting the final temperature to Kelvin
    matterTemperatureFinalCelsius = convertKelvinToCelsius(matterTemperatureFinalKelvin)
    #checking phase of the matter
    finalMatterPhase = checkPhase(matterTemperatureFinalKelvin)
    #displaying the final phase of the matter
    print("The combined " + str(numBodies) + " bodies of " + userMatter + " will be a " + finalMatterPhase + ".")
    resultsBox.insert(2, "The combined " + str(numBodies) + " bodies of " + userMatter + " will be a " + finalMatterPhase + ".")
  #confirmed that matterTemperatureFinalKelvin is an exception
  #checking if matterTemperatureFinalKelvin is "isSolidAtFreezingPoint" exception
  elif matterTemperatureFinalKelvin == "isSolidAtFreezingPoint":
    #confirmed that matterTemperatureFinalKelvin is "isSolidAtFreezingPoint" exception
    matterTemperatureFinalCelsius = convertKelvinToCelsius(freezingPoint)
    #confirmed that finalMatterPhase is a "solid"
    finalMatterPhase = "solid"
    #displaying the final phase of the matter
    print("The combined " + str(numBodies) + " bodies of " + userMatter + " will be a solid.")
    resultsBox.insert(2, "The combined " + str(numBodies) + " bodies of " + userMatter + " will be a " + finalMatterPhase + ".")
  #confirmed that matterTemperatureFinalKelvin is not "isSolidAtFreezingPoint" exception
  #checking if matterTemperatureFinalKelvin is "isLiquidAtBoilingPoint" exception
  elif matterTemperatureFinalKelvin == "isLiquidAtBoilingPoint":
    #confirmed that matterTemperatureFinalKelvin is "isLiquidAtBoilingPoint" exception
    matterTemperatureFinalCelsius = convertKelvinToCelsius(boilingPoint)
    #confirmed that finalMatterPhase is a "liquid"
    finalMatterPhase = "liquid"
    #displaying the final phase of the matter
    print("The combined " + str(numBodies) + " bodies of " + userMatter + " will be a solid.")
    resultsBox.insert(2, "The combined " + str(numBodies) + " bodies of " + userMatter + " will be a " + finalMatterPhase + ".")
  else:
    print("Error determining final phase of matter")
  temperatureValueUser = temperatureUnconversion(temperatureUnits, matterTemperatureFinalCelsius)
  #displaying final temperature of the matter
  print("The combined " + str(numBodies) + " bodies of " + userMatter + " will have a final temperature of " + temperatureValueUser + ".")
  resultsBox.insert(3, "The combined " + str(numBodies) + " bodies of " + userMatter + " will have a final temperature of " + temperatureValueUser + ".")
  resultsBox.pack()
  master.mainloop()


def welcomeButton():
  master = tkinter.Tk()
  startButton = tkinter.Button(master, text ="\n\nWelcome to the Matter Combination Program!\nPress Here to Start\n\n", command=lambda:[master.withdraw(), startButton.pack_forget(), chooseSubstance()])
  startButton.pack()
  master.mainloop()


def chooseSubstance():
  master = Tk()
  #instructions to press whether the user wants to use water or a custom substance
  enterTemperatureUnitInstructions = Label(master, text="Please select whether you want to use water or a custom substance")
  enterTemperatureUnitInstructions.pack(anchor = W)
  #button selection for "water"
  waterChosen = Radiobutton(master, text="water", command=lambda:[master.withdraw(), waterChosen.pack_forget(), customSubstanceChosen.pack_forget(), chooseTemperatureUnits()])
  waterChosen.pack(anchor = W)
  #button selection for "other"
  customSubstanceChosen = Radiobutton(master, text="other", command=lambda:[master.withdraw(), customSubstanceChosen.pack_forget(), waterChosen.pack_forget(), customSubstance()])
  customSubstanceChosen.pack(anchor = W)

  label = Label(master)
  label.pack()
  master.mainloop()


def customSubstance():
  master = Tk()

  def unknownMatter():
    global userMatter
    print("Printing matterChoice.get()" + matterChoice.get())
    userMatter = str(matterChoice.get())
    #checking if user selected "water" or "H2O" regardless of letter case
    if userMatter.casefold() == str("water").casefold() or userMatter.casefold() == str("H2O").casefold():
      #the user chose "water" or "H2O" regardless of letter case so skipping past inputting the unknown information
      chooseTemperatureUnits()
    else:
      #the user did not choose "water" or "H2O" regardless of letter case so asking to input the unknown information
      inputFreezingAndBoilingPoint()
    
  #instructions asking to "Please enter what substance you would like to combine"
  enterSubstanceInstructions = Label(master, text="Please enter what substance you would like to combine")
  enterSubstanceInstructions.pack()

  #text entry field for what substance the user wants to combine
  matterChoice = Entry(master)
  matterChoice.pack()
  matterChoice.focus_set()

  #submission button asking to "Press Here to Submit Choice"
  submissionButton = Button(master, text="Press Here to Submit Choice", command=lambda:[master.withdraw(), submissionButton.pack_forget(), unknownMatter()])
  submissionButton.pack()

  mainloop()
  matterChoice = Entry(master)
  matterChoice.pack()
  text = matterChoice.get()
  text = content.get()
  content.set(text)


def inputFreezingAndBoilingPoint():
  global userMatter
  global freezingPoint
  global boilingPoint
  master = Tk()

  
  def inputBoilingPoint():
    def checkBoilingPoint():
      global freezingPoint
      global boilingPoint
      #master = Tk()
      print("Printing temp_boilingPoint.get()" + temp_boilingPoint.get())
      #checking if user inputted boiling point as a non-numeric answer
      try:
        float(temp_boilingPoint.get())
      except ValueError:
        master = Tk()
        #if not isinstance(temp_boilingPoint.get(), int) and not isinstance(temp_boilingPoint.get(), float):
        #boilingPointTypeErrorButton that says "TypeError:\nPlease Enter a Real Number\nPress Here to Resubmit Choice"
        boilingPointTypeErrorButton = Button(master, text="TypeError:\nPlease Enter a Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), boilingPointTypeErrorButton.pack_forget(), inputFreezingAndBoilingPoint()])
        boilingPointTypeErrorButton.pack()
      #float(temp_boilingPoint.get())
      #checking if user inputted boiling point below absolute 0 or 0 K
      if float(temp_boilingPoint.get()) < 0:
        master = Tk()
        #user inputted boiling point below absolute 0 or 0 K so says "Boiling Point Below Absolute 0:\nPlease Enter a Positive Real Number\nPress Here to Resubmit Choice"
        boilingPointTypeBelowAbsoluteZeroButton = Button(master, text="Boiling Point Below Absolute 0:\nPlease Enter a Positive Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), boilingPointTypeBelowAbsoluteZeroButton.pack_forget(), inputFreezingAndBoilingPoint()])
        boilingPointTypeBelowAbsoluteZeroButton.pack()
      elif float(temp_boilingPoint.get()) == 0:
        master = Tk()
        #user inputted boiling point at absolute 0 or 0 K so says "Boiling Point at Absolute 0:\nPlease Enter a Positive Real Number\nPress Here to Resubmit Choice"
        boilingPointTypeAtAbsoluteZeroButton = Button(master, text="Boiling Point at Absolute 0:\nPlease Enter a Positive Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), boilingPointTypeAtAbsoluteZeroButton.pack_forget(), inputFreezingAndBoilingPoint()])
        boilingPointTypeAtAbsoluteZeroButton.pack()
      elif float(temp_boilingPoint.get()) < freezingPoint:
        master = Tk()
        #user inputted boiling point below freezing point so says "Boiling Point Below Freezing Point:\nPlease Re-enter the Freezing Point and Boiling Point\nPress Here to Resubmit Choice"
        boilingPointTypeBelowFreezingPointButton = Button(master, text="Boiling Point Below Freezing Point:\nPlease Re-enter the Freezing Point and Boiling Point\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), boilingPointTypeBelowFreezingPointButton.pack_forget(), inputFreezingAndBoilingPoint()])
        boilingPointTypeBelowFreezingPointButton.pack()
      elif float(temp_boilingPoint.get()) == freezingPoint:
        master = Tk()
        #user inputted boiling point at freezing point so says "Boiling Point at Freezing Point:\nPlease Re-enter the Freezing Point and Boiling Point\nPress Here to Resubmit Choice"
        boilingPointTypeAtFreezingPointButton = Button(master, text="Boiling Point at Freezing Point:\nPlease Re-enter the Freezing Point and Boiling Point\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), boilingPointTypeAtFreezingPointButton.pack_forget(), inputFreezingAndBoilingPoint()])
        boilingPointTypeAtFreezingPointButton.pack()
      else:
        boilingPoint = float(temp_boilingPoint.get())
        inputSpecificHeatCapacities()
  
    global userMatter
    global freezingPoint
    global boilingPoint
    master = Tk()
    #instructions asking to "Please enter the boiling point of " + userMatter + " in K as a positive real number"
    enterSubstanceBoilingPointInstructions = Label(master, text="Please enter the boiling point of " + userMatter + " in K as a positive real number")
    enterSubstanceBoilingPointInstructions.pack()

    #text entry field for the userMatter boiling point
    temp_boilingPoint = Entry(master)
    temp_boilingPoint.pack()
    temp_boilingPoint.focus_set()

    #submission button asking to "Press Here to Submit Choice"
    submissionButton = Button(master, text="Press Here to Submit Choice", command=lambda:[master.withdraw(), submissionButton.pack_forget(), checkBoilingPoint()])
    submissionButton.pack()

    mainloop()
    temp_boilingPoint = Entry(master)
    temp_boilingPoint.pack()
    text = temp_boilingPoint.get()
    text = content.get()
    content.set(text)

  def inputFreezingPoint():
    def checkFreezingPoint():
      global freezingPoint
      #master = Tk()
      print("Printing temp_freezingPoint.get()" + temp_freezingPoint.get())
      #checking if user inputted freezing point as a non-numeric answer
      try:
        float(temp_freezingPoint.get())
      except ValueError:
        master = Tk()
        #if not isinstance(temp_freezingPoint.get(), int) and not isinstance(temp_freezingPoint.get(), float):
        #freezingPointTypeErrorButton that says "TypeError:\nPlease Enter a Real Number\nPress Here to Resubmit Choice"
        freezingPointTypeErrorButton = Button(master, text="TypeError:\nPlease Enter a Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), freezingPointTypeErrorButton.pack_forget(), inputFreezingAndBoilingPoint()])
        freezingPointTypeErrorButton.pack()
      #temp_freezingPoint = float(temp_freezingPoint.get())
      #checking if user inputted freezing point below absolute 0 or 0 K
      if float(temp_freezingPoint.get()) < 0:
        master = Tk()
        #user inputted freezing point below absolute 0 or 0 K so says "Freezing Point Below Absolute 0:\nPlease Enter a Positive Real Number\nPress Here to Resubmit Choice"
        freezingPointTypeBelowAbsoluteZeroButton = Button(master, text="Freezing Point Below Absolute 0:\nPlease Enter a Positive Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), freezingPointTypeBelowAbsoluteZeroButton.pack_forget(), inputFreezingAndBoilingPoint()])
        freezingPointTypeBelowAbsoluteZeroButton.pack()
      elif float(temp_freezingPoint.get()) == 0:
        master = Tk()
        #user inputted freezing point at absolute 0 or 0 K so says "Freezing Point at Absolute 0:\nPlease Enter a Positive Real Number\nPress Here to Resubmit Choice"
        freezingPointTypeAtAbsoluteZeroButton = Button(master, text="Freezing Point at Absolute 0:\nPlease Enter a Positive Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), freezingPointTypeAtAbsoluteZeroButton.pack_forget(), inputFreezingAndBoilingPoint()])
        freezingPointTypeAtAbsoluteZeroButton.pack()
      else:
        freezingPoint = float(temp_freezingPoint.get()) 
        inputBoilingPoint()
    #instructions asking to "Please enter the freezing point of " + userMatter + " in K as a positive real number"
    enterSubstanceFreezingPointInstructions = Label(master, text="Please enter the freezing point of " + userMatter + " in K as a positive real number")
    enterSubstanceFreezingPointInstructions.pack()

    #text entry field for the userMatter freezing point
    temp_freezingPoint = Entry(master)
    temp_freezingPoint.pack()
    temp_freezingPoint.focus_set()

    #submission button asking to "Press Here to Submit Choice"
    submissionButton = Button(master, text="Press Here to Submit Choice", command=lambda:[master.withdraw(), submissionButton.pack_forget(), checkFreezingPoint()])
    submissionButton.pack()

    mainloop()
    temp_freezingPoint = Entry(master)
    temp_freezingPoint.pack()
    text = temp_freezingPoint.get()
    text = content.get()
    content.set(text)
  inputFreezingPoint()
  


def inputSpecificHeatCapacities():
  

    

  def inputSpecificHeatCapacity_Gas():
    def checkSpecificHeatCapacity_Gas():
      global userMatter
      global SpecificHeatCapacity_Gas
      #master = Tk()
      print("Printing temp_SpecificHeatCapacity_Gas.get()" + temp_SpecificHeatCapacity_Gas.get())
      #checking if user inputted freezing point as a non-numeric answer
      try:
        float(temp_SpecificHeatCapacity_Gas.get())
      except ValueError:
        master = Tk()
        #if not isinstance(temp_SpecificHeatCapacity_Gas.get(), int) and not isinstance(temp_SpecificHeatCapacity_Gas.get(), float):
        #specificHeatCapacity_GasTypeErrorButton that says "TypeError:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice"
        specificHeatCapacity_GasTypeErrorButton = Button(master, text="TypeError:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), specificHeatCapacity_GasTypeErrorButton.pack_forget(), inputSpecificHeatCapacity_Gas()])
        specificHeatCapacity_GasTypeErrorButton.pack()
      #float(temp_SpecificHeatCapacity_Gas.get())
      #checking if user inputted specificHeatCapacity_Gas below 0 J/g/K
      if float(temp_SpecificHeatCapacity_Gas.get()) < 0:
        #user inputted specificHeatCapacity_Gas below 0 J/g/K so converting to positive number then continuing
        SpecificHeatCapacity_Gas = abs(float(temp_SpecificHeatCapacity_Gas.get()))
        inputSpecificHeatCapacity_Liquid()
      elif float(temp_SpecificHeatCapacity_Gas.get()) == 0:
        master = Tk()
        #user inputted specificHeatCapacity_Gas at 0 J/g/K so says "Freezing Point at Absolute 0:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice"
        specificHeatCapacity_GasTypeBelowAbsoluteZeroButton = Button(master, text="Specific Heat Capacity of Gas at 0 J/g/K:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), specificHeatCapacity_GasTypeBelowAbsoluteZeroButton.pack_forget(), inputSpecificHeatCapacity_Gas()])
        specificHeatCapacity_GasTypeBelowAbsoluteZeroButton.pack()
      else:
        SpecificHeatCapacity_Gas = float(temp_SpecificHeatCapacity_Gas.get())
        inputSpecificHeatCapacity_Liquid()
    global userMatter
    master = Tk()
    #instructions asking to "Please enter the specific heat capacity of " + userMatter + " as a gas in J/g/K"
    enterSubstanceSpecificHeatCapacity_GasInstructions = Label(master, text="Please enter the specific heat capacity of " + userMatter + " as a gas in J/g/K")
    enterSubstanceSpecificHeatCapacity_GasInstructions.pack()

    #text entry field for the userMatter SpecificHeatCapacity_Gas
    temp_SpecificHeatCapacity_Gas = Entry(master)
    temp_SpecificHeatCapacity_Gas.pack()
    temp_SpecificHeatCapacity_Gas.focus_set()

    #submission button asking to "Press Here to Submit Choice"
    submissionButton = Button(master, text="Press Here to Submit Choice", command=lambda:[master.withdraw(), submissionButton.pack_forget(), checkSpecificHeatCapacity_Gas()])
    submissionButton.pack()

    mainloop()
    temp_SpecificHeatCapacity_Gas = Entry(master)
    temp_SpecificHeatCapacity_Gas.pack()
    text = temp_SpecificHeatCapacity_Gas.get()
    text = content.get()
    content.set(text)

  def inputSpecificHeatCapacity_Liquid():
    def checkSpecificHeatCapacity_Liquid():
      global userMatter
      global SpecificHeatCapacity_Liquid
      #master = Tk()
      print("Printing temp_SpecificHeatCapacity_Liquid.get()" + temp_SpecificHeatCapacity_Liquid.get())
      #checking if user inputted freezing point as a non-numeric answer
      try:
        float(temp_SpecificHeatCapacity_Liquid.get())
      except ValueError:
        master = Tk()
        #if not isinstance(temp_SpecificHeatCapacity_Liquid.get(), int) and not isinstance(temp_SpecificHeatCapacity_Liquid.get(), float):
        #specificHeatCapacity_LiquidTypeErrorButton that says "TypeError:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice"
        specificHeatCapacity_LiquidTypeErrorButton = Button(master, text="TypeError:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), specificHeatCapacity_LiquidTypeErrorButton.pack_forget(), inputSpecificHeatCapacity_Liquid()])
        specificHeatCapacity_LiquidTypeErrorButton.pack()
      #float(temp_SpecificHeatCapacity_Liquid.get())
      #checking if user inputted specificHeatCapacity_Liquid below 0 J/g/K
      if float(temp_SpecificHeatCapacity_Liquid.get()) < 0:
        #user inputted specificHeatCapacity_Liquid below 0 J/g/K so converting to positive number then continuing
        SpecificHeatCapacity_Liquid = abs(float(temp_SpecificHeatCapacity_Liquid.get()))
        inputSpecificHeatCapacity_Liquid()
      elif float(temp_SpecificHeatCapacity_Liquid.get()) == 0:
        master = Tk()
        #user inputted specificHeatCapacity_Liquid at 0 J/g/K so says "Freezing Point at Absolute 0:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice"
        specificHeatCapacity_LiquidTypeBelowAbsoluteZeroButton = Button(master, text="Specific Heat Capacity of Liquid at 0 J/g/K:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), specificHeatCapacity_LiquidTypeBelowAbsoluteZeroButton.pack_forget(), inputSpecificHeatCapacity_Liquid()])
        specificHeatCapacity_LiquidTypeBelowAbsoluteZeroButton.pack()
      else:
        SpecificHeatCapacity_Liquid = float(temp_SpecificHeatCapacity_Liquid.get())
        inputSpecificHeatCapacity_Solid()

    global userMatter
    master = Tk()
    #instructions asking to "Please enter the specific heat capacity of " + userMatter + " as a liquid in J/g/K"
    enterSubstanceSpecificHeatCapacity_LiquidInstructions = Label(master, text="Please enter the specific heat capacity of " + userMatter + " as a liquid in J/g/K")
    enterSubstanceSpecificHeatCapacity_LiquidInstructions.pack()

    #text entry field for the userMatter SpecificHeatCapacity_Liquid
    temp_SpecificHeatCapacity_Liquid = Entry(master)
    temp_SpecificHeatCapacity_Liquid.pack()
    temp_SpecificHeatCapacity_Liquid.focus_set()

    #submission button asking to "Press Here to Submit Choice"
    submissionButton = Button(master, text="Press Here to Submit Choice", command=lambda:[master.withdraw(), submissionButton.pack_forget(), checkSpecificHeatCapacity_Liquid()])
    submissionButton.pack()

    mainloop()
    temp_SpecificHeatCapacity_Liquid = Entry(master)
    temp_SpecificHeatCapacity_Liquid.pack()
    text = temp_SpecificHeatCapacity_Liquid.get()
    text = content.get()
    content.set(text)

  def inputSpecificHeatCapacity_Solid():
    def checkSpecificHeatCapacity_Solid():
      global userMatter
      global SpecificHeatCapacity_Solid
      #master = Tk()
      print("Printing temp_SpecificHeatCapacity_Solid.get()" + temp_SpecificHeatCapacity_Solid.get())
      #checking if user inputted freezing point as a non-numeric answer
      try:
        float(temp_SpecificHeatCapacity_Solid.get())
      except ValueError:
        master = Tk()
        #if not isinstance(temp_SpecificHeatCapacity_Solid.get(), int) and not isinstance(temp_SpecificHeatCapacity_Solid.get(), float):
        #specificHeatCapacity_SolidTypeErrorButton that says "TypeError:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice"
        specificHeatCapacity_SolidTypeErrorButton = Button(master, text="TypeError:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), specificHeatCapacity_SolidTypeErrorButton.pack_forget(), inputSpecificHeatCapacity_Solid()])
        specificHeatCapacity_SolidTypeErrorButton.pack()
      #float(temp_SpecificHeatCapacity_Solid)
      #checking if user inputted specificHeatCapacity_Solid below 0 J/g/K
      if float(temp_SpecificHeatCapacity_Solid.get()) < 0:
        #user inputted specificHeatCapacity_Liquid below 0 J/g/K so converting to positive number then continuing
        SpecificHeatCapacity_Solid = abs(float(temp_SpecificHeatCapacity_Solid.get()))
        inputSpecificHeatCapacity_Solid()
      elif float(temp_SpecificHeatCapacity_Solid.get()) == 0:
        master = Tk()
        #user inputted specificHeatCapacity_Solid at 0 J/g/K so says "Freezing Point at Absolute 0:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice"
        specificHeatCapacity_SolidTypeBelowAbsoluteZeroButton = Button(master, text="Specific Heat Capacity of Solid at 0 J/g/K:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), specificHeatCapacity_SolidTypeBelowAbsoluteZeroButton.pack_forget(), inputSpecificHeatCapacity_Solid()])
        specificHeatCapacity_SolidTypeBelowAbsoluteZeroButton.pack()
      else:
        SpecificHeatCapacity_Solid = float(temp_SpecificHeatCapacity_Solid.get())
        inputEnthalpyOfFusionAndVaporization()

    global userMatter
    master = Tk()
    #instructions asking to "Please enter the specific heat capacity of " + userMatter + " as a solid in J/g/K"
    enterSubstanceSpecificHeatCapacity_SolidInstructions = Label(master, text="Please enter the specific heat capacity of " + userMatter + " as a solid in J/g/K")
    enterSubstanceSpecificHeatCapacity_SolidInstructions.pack()

    #text entry field for the userMatter SpecificHeatCapacity_Solid
    temp_SpecificHeatCapacity_Solid = Entry(master)
    temp_SpecificHeatCapacity_Solid.pack()
    temp_SpecificHeatCapacity_Solid.focus_set()

    #submission button asking to "Press Here to Submit Choice"
    submissionButton = Button(master, text="Press Here to Submit Choice", command=lambda:[master.withdraw(), submissionButton.pack_forget(), checkSpecificHeatCapacity_Solid()])
    submissionButton.pack()

    mainloop()
    temp_SpecificHeatCapacity_Solid = Entry(master)
    temp_SpecificHeatCapacity_Solid.pack()
    text = temp_SpecificHeatCapacity_Solid.get()
    text = content.get()
    content.set(text)
  
  inputSpecificHeatCapacity_Gas()


def inputEnthalpyOfFusionAndVaporization():
  def inputEnthalpyOfFusion():
    def checkEnthalpyOfFusion():
      global userMatter
      global enthalpyOfFusion
      #master = Tk()
      print("Printing temp_enthalpyOfFusion.get()" + temp_enthalpyOfFusion.get())
      #checking if user inputted enthalpy of fusion as a non-numeric answer
      try:
        float(temp_enthalpyOfFusion.get())
      except ValueError:
        master = Tk()
        #if not isinstance((temp_enthalpyOfFusion.get()), int) and not isinstance(temp_enthalpyOfFusion.get(), float):
        #enthalpyOfFusionTypeErrorButton that says "TypeError:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice"
        enthalpyOfFusionTypeErrorButton = Button(master, text="TypeError:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), enthalpyOfFusionTypeErrorButton.pack_forget(), inputEnthalpyOfFusion()])
        enthalpyOfFusionTypeErrorButton.pack()
      #float(temp_enthalpyOfFusion)
      #checking if user inputted enthalpyOfFusion below 0 J/g
      if float(temp_enthalpyOfFusion.get()) < 0:
        #user inputted enthalpyOfFusion below 0 J/g so converting to positive number then continuing
        enthalpyOfFusion = abs(float(temp_enthalpyOfFusion.get()))
        inputEnthalpyOfVaporization()
      elif float(temp_enthalpyOfFusion.get()) == 0:
        master = Tk()
        #user inputted enthalpyOfFusion at 0 J/g so says "Enthalpy of Fusion at 0 J/g:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice"
        zeroErrorEnthalpyOfFusion = Button(master, text="Enthalpy of Fusion at 0 J/g:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), zeroErrorEnthalpyOfFusion.pack_forget(), inputEnthalpyOfFusion()])
        zeroErrorEnthalpyOfFusion.pack()
      else:
        enthalpyOfFusion = float(temp_enthalpyOfFusion.get())
        inputEnthalpyOfVaporization()
    global userMatter
    master = Tk()
    #instructions asking to "Please enter the enthalpy of fusion of " + userMatter + " in J/g"
    enterEnthalpyOfFusionInstructions = Label(master, text="Please enter the enthalpy of fusion of " + userMatter + " in J/g")
    enterEnthalpyOfFusionInstructions.pack()

    #text entry field for the userMatter temp_enthalpyOfFusion
    temp_enthalpyOfFusion = Entry(master)
    temp_enthalpyOfFusion.pack()
    temp_enthalpyOfFusion.focus_set()

    #submission button asking to "Press Here to Submit Choice"
    submissionButton = Button(master, text="Press Here to Submit Choice", command=lambda:[master.withdraw(), submissionButton.pack_forget(), checkEnthalpyOfFusion()])
    submissionButton.pack()

    mainloop()
    temp_enthalpyOfFusion = Entry(master)
    temp_enthalpyOfFusion.pack()
    text = temp_enthalpyOfFusion.get()
    text = content.get()
    content.set(text)
  
  def inputEnthalpyOfVaporization():
    def checkEnthalpyOfVaporization():
      global userMatter
      global enthalpyOfVaporization
      #master = Tk()
      print("Printing temp_enthalpyOfVaporization.get()" + temp_enthalpyOfVaporization.get())
      #checking if user inputted enthalpy of Vaporization as a non-numeric answer
      try:
        float(temp_enthalpyOfVaporization.get())
      except ValueError:
        master = Tk()
        #if not isinstance(temp_enthalpyOfVaporization.get(), int) and not isinstance(temp_enthalpyOfVaporization.get(), float):
        #enthalpyOfVaporizationTypeErrorButton that says "TypeError:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice"
        enthalpyOfVaporizationTypeErrorButton = Button(master, text="TypeError:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), enthalpyOfVaporizationTypeErrorButton.pack_forget(), inputEnthalpyOfVaporization()])
        enthalpyOfVaporizationTypeErrorButton.pack()
      float(temp_enthalpyOfVaporization.get())
      #checking if user inputted enthalpyOfVaporization below 0 J/g
      if float(temp_enthalpyOfVaporization.get()) < 0:
        #user inputted enthalpyOfVaporization below 0 J/g so converting to positive number then continuing
        enthalpyOfVaporization = abs(float(temp_enthalpyOfVaporization.get()))
        chooseTemperatureUnits()
      elif float(temp_enthalpyOfVaporization.get()) == 0:
        master = Tk()
        #user inputted enthalpyOfVaporization at 0 J/g so says "Enthalpy of Vaporization at 0 J/g:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice"
        zeroErrorEnthalpyOfVaporization = Button(master, text="Enthalpy of Vaporization at 0 J/g:\nPlease Enter a Nonzero Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), zeroErrorEnthalpyOfVaporization.pack_forget(), inputEnthalpyOfVaporization()])
        zeroErrorEnthalpyOfVaporization.pack()
      else:
        enthalpyOfVaporization = float(temp_enthalpyOfVaporization.get())
        chooseTemperatureUnits()
    global userMatter
    master = Tk()
    #instructions asking to "Please enter the enthalpy of Vaporization of " + userMatter + " in J/g"
    enterEnthalpyOfVaporizationInstructions = Label(master, text="Please enter the enthalpy of Vaporization of " + userMatter + " in J/g")
    enterEnthalpyOfVaporizationInstructions.pack()

    #text entry field for the userMatter temp_enthalpyOfVaporization
    temp_enthalpyOfVaporization = Entry(master)
    temp_enthalpyOfVaporization.pack()
    temp_enthalpyOfVaporization.focus_set()

    #submission button asking to "Press Here to Submit Choice"
    submissionButton = Button(master, text="Press Here to Submit Choice", command=lambda:[master.withdraw(), submissionButton.pack_forget(), checkEnthalpyOfVaporization()])
    submissionButton.pack()

    mainloop()
    temp_enthalpyOfVaporization = Entry(master)
    temp_enthalpyOfVaporization.pack()
    text = temp_enthalpyOfVaporization.get()
    text = content.get()
    content.set(text)
  
  inputEnthalpyOfFusion()


def chooseTemperatureUnits():
  def choseFahrenheit():
    global temperatureUnits
    temperatureUnits = "Fahrenheit"
    inputBodiesOfMatter()

  def choseCelsius():
    global temperatureUnits
    temperatureUnits = "Celsius"
    inputBodiesOfMatter()

  def choseKelvin():
    global temperatureUnits
    temperatureUnits = "Kelvin"
    inputBodiesOfMatter()
  master = Tk()
  #instructions to press the temperature unit that the user wants to use
  enterTemperatureUnitInstructions = Label(master, text="Please select the units you would like to use")
  enterTemperatureUnitInstructions.pack()
  #button selection for "Fahrenheit"
  FahrenheitChosen = Radiobutton(master, text="Fahrenheit", command=lambda:[master.withdraw(), FahrenheitChosen.pack_forget(), CelsiusChosen.pack_forget(), KelvinChosen.pack_forget(), choseFahrenheit()])
  FahrenheitChosen.pack(anchor = W)
  #button selection for "Celsius"
  CelsiusChosen = Radiobutton(master, text="Celsius", command=lambda:[master.withdraw(), FahrenheitChosen.pack_forget(), CelsiusChosen.pack_forget(), KelvinChosen.pack_forget(), choseCelsius()])
  CelsiusChosen.pack(anchor = W)
  #button selection for "Kelvin"
  KelvinChosen = Radiobutton(master, text="Kelvin", command=lambda:[master.withdraw(), FahrenheitChosen.pack_forget(), CelsiusChosen.pack_forget(), KelvinChosen.pack_forget(), choseKelvin()])
  KelvinChosen.pack(anchor = W)

  label = Label(master)
  label.pack()
  master.mainloop()


def inputBodiesOfMatter():
  def inputTemperatureOfMatter():
    global userMatter
    global matterKelvinTemperatures
    global temperatureUnits
    def checkTemperatureOfMatter():
      global userMatter
      global matterKelvinTemperatures
      global temperatureUnits
      #master = Tk()
      print("Printing temp_temperatureOfMatter.get()" + temp_temperatureOfMatter.get())
      #checking if user inputted temperature of matter as a non-numeric answer
      try:
        float(temp_temperatureOfMatter.get())
      except ValueError:
        master = Tk()
        #if not isinstance(float(temp_temperatureOfMatter.get()), int) and not isinstance(float(temp_temperatureOfMatter.get()), float):
        #temperatureOfMatterTypeErrorButton that says "TypeError:\nPlease Enter a Real Number\nPress Here to Resubmit Choice"
        temperatureOfMatterTypeErrorButton = Button(master, text="TypeError:\nPlease Enter a Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), temperatureOfMatterTypeErrorButton.pack_forget(), inputTemperatureOfMatter()])
        temperatureOfMatterTypeErrorButton.pack()
      #converting user temperature to Celsius
      temp_temperatureOfMatterCelsius = temperatureConversionToCelsius(temperatureUnits, temp_temperatureOfMatter.get())
      #converting user temperature to Kelvin
      temp_temperatureOfMatterKelvin = convertCelsiusToKelvin(temp_temperatureOfMatterCelsius)
      #checking if user inputted temperatureOfMatter below absolute 0 or 0 K
      if temp_temperatureOfMatterKelvin < 0:
        master = Tk()
        #user inputted temperatureOfMatter below absolute 0 or 0 K so says "Temperature Below Absolute 0:\nPlease Enter a Positive Real Number\nPress Here to Resubmit Choice"
        temperatureOfMatterTypeBelowAbsoluteZeroButton = Button(master, text="Temperature Below Absolute 0:\nPlease Enter a Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), temperatureOfMatterTypeBelowAbsoluteZeroButton.pack_forget(), inputTemperatureOfMatter()])
        temperatureOfMatterTypeBelowAbsoluteZeroButton.pack()
        """
        #checking if user inputted temperatureOfMatter at absolute 0 or 0 K
        elif temp_temperatureOfMatterKelvin.get() == 0:
        #user inputted temperatureOfMatter at absolute 0 or 0 K so says "Temperature at Absolute 0:\nPlease Enter a Positive Real Number\nPress Here to Resubmit Choice"
        temperatureOfMatterTypeAtAbsoluteZeroButton = Button(master, text="Temperature at Absolute 0:\nPlease Enter a Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), temperatureOfMatterTypeAtAbsoluteZeroButton.pack_forget(), inputTemperatureOfMatter()])
        temperatureOfMatterTypeAtAbsoluteZeroButton.pack()
        """
      else:
        matterKelvinTemperatures.append(temp_temperatureOfMatterKelvin)
        print(userMatter + " #" + str(len(matterKelvinTemperatures)) + " is a " + matterPhase(temp_temperatureOfMatterKelvin))
        master = tkinter.Tk()
        tellUserPhaseButton = tkinter.Button(master, text ="\n" + userMatter + " #" + str(len(matterKelvinTemperatures)) + " is a " + matterPhase(temp_temperatureOfMatterKelvin) + ".\nPress Here when Ready to Move to the Next Step\n", command=lambda:[master.withdraw(), tellUserPhaseButton.pack_forget(), inputMassOfMatter()])
        tellUserPhaseButton.pack()
        master.mainloop()
        inputMassOfMatter()
    master = Tk()
    #getting input for temperature of the matter
    enterTemperatureOfMatterInstructions = Label(master, text="Please enter the temperature of " + userMatter + " #" + str(len(matterKelvinTemperatures) + 1) + " in " + temperatureUnits + ": ")
    enterTemperatureOfMatterInstructions.pack()

    #text entry field for the userMatter temp_temperatureOfMatter
    temp_temperatureOfMatter = Entry(master)
    temp_temperatureOfMatter.pack()
    temp_temperatureOfMatter.focus_set()

    #submission button asking to "Press Here to Submit Choice"
    submissionButton = Button(master, text="Press Here to Submit Choice", command=lambda:[master.withdraw(), submissionButton.pack_forget(), checkTemperatureOfMatter()])
    submissionButton.pack()

    mainloop()
    temp_temperatureOfMatter = Entry(master)
    temp_temperatureOfMatter.pack()
    text = temp_temperatureOfMatter.get()
    text = content.get()
    content.set(text)
  
  def inputMassOfMatter():
    def checkMassOfMatter():
      global userMatter
      global matterMasses
      global massUnits
      #master = Tk()
      print("Printing temp_massOfMatter.get()" + temp_massOfMatter.get())

      #checking if user inputted mass of matter as a non-numeric answer
      try:
        float(temp_massOfMatter.get())
      except ValueError:
        master = Tk()
        #if not isinstance(temp_massOfMatter.get(), int) and not isinstance(temp_massOfMatter.get(), float):
        #massOfMatterTypeErrorButton that says "TypeError:\nPlease Enter a Real Number\nPress Here to Resubmit Choice"
        massOfMatterTypeErrorButton = Button(master, text="TypeError:\nPlease Enter a Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), massOfMatterTypeErrorButton.pack_forget(), inputMassOfMatter()])
        massOfMatterTypeErrorButton.pack()
      #temp_massOfMatter = float(temp_massOfMatter.get())
      #checking if user inputted massOfMatter below 0 grams
      if float(temp_massOfMatter.get()) < 0:
        master = Tk()
        #user inputted massOfMatter below below 0 grams so says "Mass Below 0 Grams:\nPlease Enter a Positive Real Number\nPress Here to Resubmit Choice"
        massOfMatterTypeBelowZeroGramsButton = Button(master, text="Mass Below 0 Grams:\nPlease Enter a Positive Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), massOfMatterTypeBelowZeroGramsButton.pack_forget(), inputMassOfMatter()])
        massOfMatterTypeBelowZeroGramsButton.pack()
      #checking if user inputted massOfMatter at 0 grams
      elif float(temp_massOfMatter.get()) == 0:
        master = Tk()
        #user inputted massOfMatter at 0 grams so says "Mass at Absolute 0:\nPlease Enter a Positive Real Number\nPress Here to Resubmit Choice"
        massOfMatterTypeAtZeroGramsButton = Button(master, text="Mass at 0 Grams:\nPlease Enter a Real Number\nPress Here to Resubmit Choice", command=lambda:[master.withdraw(), massOfMatterTypeAtZeroGramsButton.pack_forget(), inputMassOfMatter()])
        massOfMatterTypeAtZeroGramsButton.pack()
      else:
        matterMasses.append(float(temp_massOfMatter.get()))
        confirmIfWantToContinue()

    global userMatter
    global matterMasses
    master = Tk()
    #getting input for mass of the matter
    enterMassOfMatterInstructions = Label(master, text="Please enter the mass of " + userMatter + " #" + str(len(matterMasses) + 1) + " in grams: ")
    enterMassOfMatterInstructions.pack()

    #text entry field for the userMatter temp_massOfMatter
    temp_massOfMatter = Entry(master)
    temp_massOfMatter.pack()
    temp_massOfMatter.focus_set()

    #submission button asking to "Press Here to Submit Choice"
    submissionButton = Button(master, text="Press Here to Submit Choice", command=lambda:[master.withdraw(), submissionButton.pack_forget(), checkMassOfMatter()])
    submissionButton.pack()

    mainloop()
    temp_massOfMatter = Entry(master)
    temp_massOfMatter.pack()
    text = temp_massOfMatter.get()
    text = content.get()
    content.set(text)

  inputTemperatureOfMatter()


def confirmIfWantToContinue():
  global temperatureUnits
  global matterKelvinTemperatures
  global userMatter
  master = Tk()

  def choseNo():
    temperatureUnits = "Celsius"
    inputBodiesOfMatter()

  #instructions to press a button to ask "Continue?\nWould you like to add " + userMatter + " #" + str(len(matterKelvinTemperatures) + 1) + "?"
  enterTemperatureUnitInstructions = Label(master, text="Continue?\nWould you like to add " + userMatter + " #" + str(len(matterKelvinTemperatures) + 1) + "?")
  enterTemperatureUnitInstructions.pack()
  #button selection for "Yes"
  yesChosen = Radiobutton(master, text="Yes", command=lambda:[master.withdraw(), yesChosen.pack_forget(), inputBodiesOfMatter()])
  yesChosen.pack(anchor = W)
  #button selection for "No"
  noChosen = Radiobutton(master, text="No", command=lambda:[master.withdraw(), noChosen.pack_forget(), listSorting()])
  noChosen.pack(anchor = W)

  label = Label(master)
  label.pack()
  master.mainloop()

  inputTemperatureOfMatter()


def welcome():
  global userMatter
  print("Welcome to the Matter Combination Program!\n\n")
  #asking for what substance will be combined
  userMatter = str(input('Please enter what substance you would like to combine\n(I already know of "water"): '))
  #changing values if the user chooses an unknown substance
  if userMatter != "water":
    changeMatter()
  #asking for what temperature units will be used
  notValidTemperatureUnit = True
  while notValidTemperatureUnit:
    temperatureUnits = input('Please enter the units you would like to use\n("F" for Fahrenheit, "C" for Celsius, or "K" for Kelvin): ')
    #checking for errors with the temperature unit input:
    if temperatureUnits == "F" or temperatureUnits == "f": #checking if using Fahrenheit
      notValidTemperatureUnit = False
    elif temperatureUnits == "C" or temperatureUnits == "c": #checking if using Celsius
      notValidTemperatureUnit = False
    elif temperatureUnits == "K" or temperatureUnits == "k": #checking if using Kelvin
      notValidTemperatureUnit = False
    else:
      print("I apologize.\nI am unable to comprehend how to use " + str(temperatureUnits) + ".")
      print("Please re-enter a unit that I am familiar with.\n\n")
  return temperatureUnits


def changeMatter():
  global userMatter
  global freezingPoint
  global boilingPoint
  global SpecificHeatCapacity_Gas
  global SpecificHeatCapacity_Liquid
  global SpecificHeatCapacity_Solid
  global enthalpyOfFusion
  global enthalpyOfVaporization
  freezingAndBoiling = True
  while freezingAndBoiling:
    freezingPoint = float(input('Please enter the freezing point of ' + userMatter + ' in K\n(water\'s is "' + str(freezingPoint) + '" K): '))
    boilingPoint = float(input('Please enter the boiling point of ' + userMatter + ' in K\n(water\'s is "' + str(boilingPoint) + '" K): '))
    if freezingPoint < boilingPoint:
      freezingAndBoiling = False
    elif freezingPoint == boilingPoint:
      print("The freezing and boiling points are the same.\nPlease re-enter the correct freezing and boiling points.\n\n")
    elif freezingPoint > boilingPoint:
      print("The freezing point is greater than the boiling point.\nPlease re-enter the correct freezing and boiling points.\n\n")
  SpecificHeatCapacity_Gas = float(input('Please enter the specific heat capacity of ' + userMatter + ' as a gas in J/g/K\n(water\'s is "' + str(SpecificHeatCapacity_Gas) + '"): '))
  SpecificHeatCapacity_Liquid = float(input('Please enter the specific heat capacity of ' + userMatter + ' as a liquid in J/g/K\n(water\'s is "' + str(SpecificHeatCapacity_Liquid) + '"): '))
  SpecificHeatCapacity_Solid = float(input('Please enter the specific heat capacity of ' + userMatter + ' as a solid in J/g/K\n(water\'s is "' + str(SpecificHeatCapacity_Solid) + '"): '))
  enthalpyOfFusion = float(input('Please enter the enthalpy of fusion of ' + userMatter + ' in J/g\n(water\'s is "' + str(enthalpyOfFusion) + '" J/g): '))
  enthalpyOfVaporization = float(input('Please enter the enthalpy of fusion of ' + userMatter + ' in J/g\n(water\'s is "' + str(enthalpyOfVaporization) + '" J/g): '))


def matterPhase(temperatureValueKelvin):
  global freezingPoint
  global boilingPoint
  if temperatureValueKelvin < freezingPoint:
    return "a solid"
  elif temperatureValueKelvin < boilingPoint:
    return "a liquid"
  else:
    return "a gas"


def listSorting():
  global matterKelvinTemperatures
  global matterMasses
  global sortedMatterKelvinTemperatures
  global sortedMasses
  global matterTemperatureFinalKelvin
  #combining matrices of Kelvin temperatures and masses into a tuple
  sortedMatterKelvinTemperatures = sorted(matterKelvinTemperatures)
  #for how to combine multiple lists into a tuple:
  #https://docs.python.org/3/library/functions.html#zip
  sortedMasses = [y for x, y in sorted(zip(matterKelvinTemperatures,matterMasses))]
  #combining the matter
  matterTemperatureFinalKelvin = matterCombination()
  programEnding()

def matterCombination():
  global matterKelvinTemperatures
  global matterMasses
  global sortedMatterKelvinTemperatures
  global sortedMasses
  global SpecificHeatCapacity_Solid
  global SpecificHeatCapacity_Liquid
  global SpecificHeatCapacity_Gas
  global enthalpyOfFusion
  global enthalpyOfVaporization
  global freezingPoint
  global boilingPoint
  global userMatter
  global matterMassTotal
  matterTemperatureFinalKelvin = 0
  energyMatterTotal = 0
  i = 0
  while i < len(sortedMatterKelvinTemperatures):
    #for matter at index i
    matterTemperatureCurrent = sortedMatterKelvinTemperatures[i]
    isGas = False
    isLiquid = False
    isSolid = False
    if matterTemperatureCurrent < freezingPoint:
      isSolid = True
    elif matterTemperatureCurrent < boilingPoint:
      isLiquid = True
    else:
      isGas = True
    if isGas:
      energyMatterTotal = energyFromGas(energyMatterTotal, matterTemperatureCurrent, i)
      matterTemperatureCurrent = boilingPoint #temperature at boiling point
      isGas = False
      isLiquid = True
      isSolid = False
    if isLiquid:
      energyMatterTotal = energyFromLiquid(energyMatterTotal, matterTemperatureCurrent, i)
      matterTemperatureCurrent = freezingPoint #temperature at freezing point
      isGas = False
      isLiquid = False
      isSolid = True
    if isSolid:
      energyMatterTotal = energyFromSolid(energyMatterTotal, matterTemperatureCurrent, i)
      matterTemperatureCurrent = 0 #temperature at absolute 0 or 0 K
      isGas = False
      isLiquid = False
      isSolid = False
    matterMassTotal = matterMassTotal + sortedMasses[i]
    i = i + 1
  #displaying the total mass of the matter
  #print("\n\nThe total mass of " + userMatter + " is " + str(round(matterMassTotal, 2)) + " grams.")
  #raising matter temperature as a solid
  matterTemperatureFinalKelvin = matterTemperatureFinalKelvin + energyMatterTotal / (matterMassTotal * SpecificHeatCapacity_Solid)
  if matterTemperatureFinalKelvin > freezingPoint:
    #subtracting energy from total enthalpy to get the total unused energy remaining after raising the temperature to the phase change from solid to liquid
    energyMatterTotal = energyMatterTotal - matterMassTotal * SpecificHeatCapacity_Solid * freezingPoint
    #subtracting energy from the total unused energy remaining after undergoing a phase change from solid to liquid
    energyMatterTotal = energyMatterTotal - matterMassTotal * enthalpyOfFusion
    if energyMatterTotal > 0:
      #temperature of matter after solid to liquid phase change
      matterTemperatureFinalKelvin = freezingPoint
      #raising matter temperature as a liquid
      matterTemperatureFinalKelvin = matterTemperatureFinalKelvin + energyMatterTotal / (matterMassTotal * SpecificHeatCapacity_Liquid)
      if matterTemperatureFinalKelvin >= boilingPoint:
        #subtracting energy from the total unused energy remaining after raising the temperature to the phase change from liquid to gas
        energyMatterTotal = energyMatterTotal - matterMassTotal * SpecificHeatCapacity_Liquid * (boilingPoint - freezingPoint)
        #subtracting energy from the total unused energy remaining after undergoing a phase change from liquid to gas
        energyMatterTotal = energyMatterTotal - matterMassTotal * enthalpyOfVaporization
        if energyMatterTotal >= 0:
          #temperature of matter after liquid to gas phase change
          matterTemperatureFinalKelvin = boilingPoint
          #raising matter temperature as a gas
          matterTemperatureFinalKelvin = matterTemperatureFinalKelvin + energyMatterTotal / (matterMassTotal * SpecificHeatCapacity_Gas)
          return matterTemperatureFinalKelvin
        else:
          return "isLiquidAtBoilingPoint"
      else:
        return matterTemperatureFinalKelvin
    elif energyMatterTotal == 0:
      return matterTemperatureFinalKelvin
    else:
      return "isSolidAtFreezingPoint"
  elif matterTemperatureFinalKelvin == freezingPoint:
    return "isSolidAtFreezingPoint"
  else:
    return matterTemperatureFinalKelvin


def energyFromGas(energyMatterTotal, matterTemperatureCurrent, i):
  global sortedMasses
  global SpecificHeatCapacity_Gas
  global enthalpyOfVaporization
  global boilingPoint
  #lowering temperature to phase change from gas to liquid
  energyMatterTotal = energyMatterTotal + sortedMasses[i] * SpecificHeatCapacity_Gas * (matterTemperatureCurrent - boilingPoint)
  #undergoing phase change from gas to liquid
  energyMatterTotal = energyMatterTotal + sortedMasses[i] * enthalpyOfVaporization
  return energyMatterTotal


def energyFromLiquid(energyMatterTotal, matterTemperatureCurrent, i):
  global sortedMasses
  global SpecificHeatCapacity_Liquid
  global enthalpyOfFusion
  global freezingPoint
  #lowering temperature to phase change from liquid to solid
  energyMatterTotal = energyMatterTotal + sortedMasses[i] * SpecificHeatCapacity_Liquid * (matterTemperatureCurrent - freezingPoint)
  #undergoing phase change from liquid to solid
  energyMatterTotal = energyMatterTotal + sortedMasses[i] * enthalpyOfFusion
  return energyMatterTotal


def energyFromSolid(energyMatterTotal, matterTemperatureCurrent, i):
  global sortedMasses
  global SpecificHeatCapacity_Solid
  #lowering temperature to absolute 0 which is 0 K
  energyMatterTotal = energyMatterTotal + sortedMasses[i] * SpecificHeatCapacity_Solid * matterTemperatureCurrent
  return energyMatterTotal


def temperatureConversionToCelsius(temperatureUnits, temperatureValue):
  if temperatureUnits.casefold() == "Fahrenheit".casefold():
    temperatureValueCelsius = convertFahrenheitToCelsius(temperatureValue)
  elif temperatureUnits.casefold() == "Celsius".casefold():
    temperatureValueCelsius = temperatureValue
  elif temperatureUnits.casefold() == "Kelvin".casefold():
    temperatureValueCelsius = convertKelvinToCelsius(temperatureValue)
  return temperatureValueCelsius


def convertFahrenheitToCelsius(temperatureValue):
  temperatureValueCelsius = (float(temperatureValue) - 32) * 5 / 9
  return temperatureValueCelsius


def convertKelvinToCelsius(temperatureValue):
  temperatureValueCelsius = float(temperatureValue) - 273.15
  return temperatureValueCelsius


def convertCelsiusToFahrenheit(temperatureCelsius):
  temperatureValueFahrenheit = float(temperatureCelsius) * 9 / 5 + 32
  return temperatureValueFahrenheit


def convertCelsiusToKelvin(temperatureCelsius):
  temperatureValueKelvin = float(temperatureCelsius) + 273.15
  return temperatureValueKelvin


def temperatureUnconversion(temperatureUnits, matterTemperatureFinal):
  if temperatureUnits.casefold() == "Fahrenheit".casefold():
    temperatureValueUser = str(round(convertCelsiusToFahrenheit(matterTemperatureFinal), 2)) + " degrees Fahrenheit"
  elif temperatureUnits.casefold() == "Celsius".casefold():
    temperatureValueUser = str(round(matterTemperatureFinal, 2)) + " degrees Celsius"
  elif temperatureUnits.casefold() == "Kelvin".casefold():
    temperatureValueUser = str(round(convertCelsiusToKelvin(matterTemperatureFinal), 2)) + " Kelvin"
  return temperatureValueUser

def checkPhase(matterTemperatureInKelvin):
  global freezingPoint
  global boilingPoint
  #checking if the temperature is below the freezingPoint
  if matterTemperatureInKelvin < freezingPoint:
    #the temperature is below the freezingPoint so is a "solid"
    matterPhase = "solid"
  #checking if the temperature is below the boilingPoint
  elif matterTemperatureInKelvin <= boilingPoint:
    #the temperature is below the freezingPoint so is a "liquid"
    matterPhase = "liquid"
  else:
    #must be above the boilingPoint so is a "gas"
    matterPhase = "gas"
  return matterPhase

main()