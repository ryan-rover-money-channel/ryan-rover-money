import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

ch("Intro")
short("Most people never get here. Do you?")
pr("Hi, I'm Ryan Rover. What really changes when you have twenty thousand dollars in the bank? More than you think.")
short("This one number changes how you think about money.")
card("Twenty thousand dollars is the point where money stops being a daily worry.",
     {"type": "stat", "label": "in the bank", "big": "$20,000", "sub": "the number that changes how you think"})
short("It starts with one simple rule.")
sc("And it starts with something simple: cash you don't touch.", "United States one hundred dollar bill", "CASH YOU DON'T TOUCH", cuts=2)
short("One hundred dollars a month can become fifty two thousand.")
card("One hundred dollars a month, invested for twenty years at seven percent, grows to about fifty two thousand dollars.",
     {"type": "growth", "monthly": 100, "rate": 0.07, "years": 20})
short("Time is the secret nobody explains.")
pr("That's the power of time. Stay with me, and I'll show you the whole plan.")
save("test30", "Ryan Rover Money: 30 second test", ["Growth math: monthly compounding at 7% (illustration, not a promise)"], "pipeline test")
