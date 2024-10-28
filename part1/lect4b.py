from collections import Counter
jordan_info = """Jordan is a young state that occupies an ancient land, 
one that bears the traces of many civilizations. 
Separated from ancient Palestine by the Jordan River, 
the region played a prominent role in biblical history. 
The ancient biblical kingdoms of Moab, Gilead, 
and Edom lie within its borders as does the famed red stone city of Petra,
the capital of the Nabatean kingdom and of the Roman province of Arabia Petraea. """

print(Counter(jordan_info.replace("\n","").split(" ")))