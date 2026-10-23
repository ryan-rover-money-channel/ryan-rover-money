import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Here's a question most people never ask out loud. What actually changes
when you have twenty thousand dollars sitting in the bank? Not in a retirement account you can't touch.
Not in crypto. Just cash, ready, yours. The answer surprised me, because the biggest changes have almost
nothing to do with the money itself.""")
card("""Twenty thousand dollars. For some people that sounds like a fortune. For others it sounds like
one bad year. But this number sits right at a turning point, and by the end of this video you'll see why.""",
     {"type": "stat", "label": "in the bank", "big": "$20,000", "sub": "the turning point most people never reach"})
sc("""Here's the hook. According to the Federal Reserve, sixty three percent of American adults say they
would cover a surprise four hundred dollar expense with cash or its equivalent. That means more than a
third would not. They would borrow, sell something, or simply not be able to pay.""",
   "Marriner S. Eccles Federal Reserve Board Building", "THE $400 QUESTION")
sc("""And the money doesn't have to be huge to change your life. The jump from zero to twenty thousand
dollars changes how you sleep, how you work, how you argue, and how you make decisions. Some of these
changes are obvious. A few of them are almost invisible, and the last one on this list is the one that
can quietly undo everything if you are not careful.""",
   "United States one hundred dollar bill", "WHAT REALLY CHANGES")
pr("""So we'll go through fifteen real changes, one by one, with the numbers behind them. Then I'll show you
exactly where to keep that money and how people actually get there. Let's start.""")

# ---------------- How we got the numbers ----------------
ch("How we got the numbers")
sc("""Quick note on the data. Every number in this video comes from a named source. We used the Federal
Reserve's survey on the economic well being of U.S. households, published in May twenty twenty six.
We used the Federal Reserve's Survey of Consumer Finances. We used Bankrate's emergency savings
research, and guidance from the Consumer Financial Protection Bureau and the FDIC.""",
   "Federal Reserve Bank of New York building", "OUR SOURCES")
sc("""When we show growth over time, we show the math and the assumption behind it, like a seven percent
average yearly return. That's an illustration, not a promise. Markets go up and down, and nobody can
guarantee a return. If you remember one thing from this section, remember that. This is education,
not financial advice.""",
   "Calculator and pen on financial papers", "EDUCATION, NOT ADVICE")

# ---------------- The big picture ----------------
ch("The big picture")
card("""Let's start with where most people are. Bankrate surveyed Americans in December twenty twenty five.
Only forty seven percent said they had enough money or access to funds to cover a one thousand dollar
emergency. Fewer than half. For a one thousand dollar problem.""",
     {"type": "stat", "label": "can cover a $1,000 emergency", "big": "47%", "sub": "Bankrate, December 2025"})
card("""It gets sharper. In another Bankrate survey from May twenty twenty five, twenty four percent of
Americans said they had no emergency savings at all. Nearly one in four people is one flat tire away from
debt.""",
     {"type": "stat", "label": "have no emergency savings", "big": "24%", "sub": "Bankrate, May 2025"})
card("""And at the other end, only twenty seven percent said they had six months or more of expenses saved.
That's the group this video is really about. The people who crossed the line.""",
     {"type": "stat", "label": "have 6+ months saved", "big": "27%", "sub": "Bankrate, May 2025"})
sc("""Now look at what a typical family keeps in the bank. The Federal Reserve's Survey of Consumer
Finances found that the median American family had about eight thousand dollars in transaction accounts
in twenty twenty two. That's checking, savings and similar accounts combined. Median means half of
families had less than that.""",
   "Bank branch interior with teller counter", "THE TYPICAL BALANCE")
card("""So twenty thousand dollars is about two and a half times what the typical family keeps in the bank.
It is not rich. But it puts you in a very different position from most of the people around you. And
that position changes behavior in ways you can measure.""",
     {"type": "compare", "left": {"label": "Typical family", "big": "$8,000", "sub": "median, 2022"},
      "right": {"label": "This video", "big": "$20,000", "sub": "about 2.5x more"},
      "note": "Federal Reserve, Survey of Consumer Finances 2022"})

# ---------------- 1 ----------------
ch("1. Emergencies become inconveniences")
pr("""Number one is the one everybody feels first.""")
card("""Change number one. Emergencies stop being emergencies. When your car needs a new transmission, or a
tooth cracks, or the water heater dies, the problem is still annoying. But it's no longer a crisis. It's
a bill. You pay it, you move on, and you rebuild the cushion.""",
     {"type": "list", "n": 1, "title": "Emergencies become bills", "sub": "the problem stays, the panic goes"}, "CHANGE 1")
sc("""This matters more than it sounds, because unexpected expenses are normal. In the Federal Reserve's
latest survey, fifty nine percent of adults said they had at least one major unexpected expense in the
past year. So the question is not whether something will break. It's whether you'll have to borrow when
it does.""",
   "Car repair garage mechanic", "59% HAD A SURPRISE BILL")
sc("""Without savings, a two thousand dollar repair goes on a credit card. With interest, that repair can
cost you far more than two thousand dollars by the time it's paid off. With twenty thousand in the bank,
the same repair costs exactly what it costs. Nothing more. That difference, repeated over a lifetime,
is enormous.""",
   "Credit cards close up", "THE REPAIR COSTS WHAT IT COSTS")

sc("""Here's a real way to picture it. Imagine two neighbors, both earning the same salary. Their cars break
down the same week, and both repairs cost two thousand dollars. The first neighbor has savings and pays
the shop. Done. The second puts it on a card at over twenty percent interest and pays the minimum. Months
later he's still paying for that repair, and the next surprise is already on its way. Same income. Same
bad luck. Completely different outcome. Try this today: write down the three most likely surprise bills
in your life, a car repair, a medical bill, a trip home, and put a real number next to each one. That's
your first savings target.""", "Car breakdown on road with hazard lights", "SAME LUCK, DIFFERENT OUTCOME")

# ---------------- 2 ----------------
ch("2. You stop paying the broke tax")
card("""Change number two. You stop paying what people call the broke tax. These are the costs that only
exist because you don't have a cushion. Overdraft fees. Late fees. Interest on small balances. Short
term loans with brutal rates.""",
     {"type": "list", "n": 2, "title": "No more broke tax", "sub": "fees that only exist without a cushion"}, "CHANGE 2")
sc("""Here's the worst example. The Consumer Financial Protection Bureau explains that a typical two week
payday loan, with a fee of fifteen dollars for every hundred dollars borrowed, works out to an annual
percentage rate of almost four hundred percent. Four hundred. People don't take those loans because
they are careless. They take them because they have no other option.""",
   "Payday loan store sign", "ALMOST 400% APR")
sc("""Credit cards are less extreme, but they add up. The Federal Reserve publishes average credit card
rates, and in recent years the rate on accounts that pay interest has been above twenty percent. When
you have twenty thousand dollars in cash, you can pay every card in full, every month. That one habit
alone can save you thousands of dollars over a decade.""",
   "Credit card payment terminal", "OVER 20% INTEREST")
pr("""And here's the part people miss. The broke tax doesn't just cost money. It costs time and attention.
Once it's gone, you get both back.""")

sc("""How much does the broke tax really cost? Add it up for a year. A few overdraft fees, a late fee or
two, interest on a balance you couldn't pay off, maybe a rush fee because a bill was late. For many
households that easily reaches hundreds of dollars a year, money that buys absolutely nothing. Try this:
open your last three bank and card statements and highlight every fee and every interest charge. Most
people are surprised by the total. That total is what your cushion will save you, every single year,
from now on.""", "Bank statement with highlighter", "ADD UP YOUR FEES")

# ---------------- 3 ----------------
ch("3. You can say no")
card("""Change number three. You get the power to say no. No to a toxic boss. No to a job that's slowly
wrecking your health. No to a deal that feels wrong. Some people call this walk away money.""",
     {"type": "list", "n": 3, "title": "You can say no", "sub": "walk away money"}, "CHANGE 3")
sc("""Think about it in months instead of dollars. If your basic monthly costs are around four thousand
dollars, twenty thousand dollars is about five months of runway. That is enough time to look for a better
job without panic. And people who search without panic tend to negotiate better, because they can wait
for the right offer.""",
   "Office worker at desk with computer", "FIVE MONTHS OF RUNWAY")
card("""Here's that math on screen. Four thousand dollars a month in essential costs. Twenty thousand
dollars saved. Five months where your decisions belong to you, not to your next paycheck.""",
     {"type": "compare", "left": {"label": "Monthly costs", "big": "$4,000", "sub": "rent, food, bills"},
      "right": {"label": "Runway", "big": "5 months", "sub": "with $20,000 saved"},
      "note": "Example budget. Use your own monthly costs."})

sc("""Walk away money also changes how you're treated at work, even if you never use it. People who
don't need the job can speak up in meetings, push back on bad ideas, and turn down extra unpaid work.
They are often the ones who get noticed, because they act like professionals with options. The cushion
doesn't make you braver. It makes bravery cheaper. Try this: calculate your own runway. Add up rent, food,
utilities, insurance, transport and minimum debt payments. Divide your savings by that number. That's
how many months of freedom you have today.""", "Team meeting in conference room", "BRAVERY GETS CHEAPER")

# ---------------- 4 ----------------
ch("4. Your credit gets stronger")
card("""Change number four. Your credit gets stronger, almost automatically. Not because savings show up on
your credit report. They don't. But because cash in the bank changes how you use credit.""",
     {"type": "list", "n": 4, "title": "Your credit gets stronger", "sub": "because you use credit differently"}, "CHANGE 4")
sc("""Two things matter a lot in a credit score. Paying on time, and how much of your available credit
you're using. When you have a cushion, you never miss a payment because money is tight, and you stop
carrying big balances. Both of those push your score up over time.""",
   "Credit report document", "ON TIME, LOW BALANCES")
sc("""A better score is not a trophy. It means lower rates on a car loan, a mortgage, and sometimes even
insurance in some states. Over a lifetime, a few percentage points of interest on big loans can add up
to tens of thousands of dollars. So the cushion pays you twice. Once when you avoid debt, and again when
you borrow on better terms.""",
   "House keys and mortgage contract", "THE CUSHION PAYS TWICE")

sc("""Here's an example of how it works in real life. Someone carries a three thousand dollar balance on a
card with a ten thousand dollar limit. They're using thirty percent of their available credit. Once they
have savings, they pay it off and keep it at zero, using the card only for things they pay in full. Their
utilization drops close to zero, and over the following months their score usually climbs. Try this:
set every card to autopay the full statement balance. With a cushion behind you, that's safe, and it's the
single easiest way to never miss a payment again.""", "Credit card on laptop keyboard", "SET AUTOPAY IN FULL")

# ---------------- 5 ----------------
ch("5. Your money starts working")
pr("""Now here's where it gets fun. Number five.""")
card("""Change number five. Your money starts earning money. Even sitting in a savings account, twenty
thousand dollars produces something. If an account pays four percent a year, that's about eight hundred
dollars a year, for doing nothing.""",
     {"type": "stat", "label": "at a 4% yearly yield", "big": "$800 a year", "sub": "on $20,000, before taxes"}, "CHANGE 5")
sc("""Eight hundred dollars won't change your life by itself. But it changes how you see money. For the
first time, money is not only something you trade your hours for. It is something that grows while you
sleep. Rates change over time, so always check what your bank actually pays today.""",
   "Piggy bank with coins", "MONEY THAT GROWS")
card("""And when you keep going, time does the heavy lifting. One hundred dollars a month, invested for
twenty years, at a seven percent average yearly return, grows to about fifty two thousand dollars. You
put in twenty four thousand. The rest is growth. Again, that's an illustration, not a promise.""",
     {"type": "growth", "monthly": 100, "rate": 0.07, "years": 20})

sc("""Something else happens at this level. You start comparing where your money sits. A big bank checking
account might pay close to nothing. An online high yield savings account might pay much more. On twenty
thousand dollars, the difference between almost zero and a few percent is hundreds of dollars a year,
just for moving the money to a better insured account. Try this: look up what your current savings
account pays. If it's close to zero, you are leaving free money on the table every month.""", "Online banking on laptop screen", "COMPARE YOUR RATE")

# ---------------- 6 ----------------
ch("6. You make better decisions")
card("""Change number six. You make better decisions. This one is backed by research on what scarcity
does to the mind.""",
     {"type": "list", "n": 6, "title": "You think more clearly", "sub": "scarcity takes up mental space"}, "CHANGE 6")
sc("""Economist Sendhil Mullainathan and psychologist Eldar Shafir wrote a book called Scarcity. Their
argument is simple. When you are short on money, your mind gets pulled toward the shortage. Rent, the
next bill, the overdraft. That pull uses up attention, and it leaves less room for planning and long term
thinking.""",
   "Person thinking at window", "SCARCITY USES ATTENTION")
sc("""It's not that people without money are worse at decisions. It's that anyone, put under constant
money pressure, starts deciding worse. A cushion removes some of that pressure. And with the pressure
gone, people tend to plan further ahead, compare prices, and avoid the quick fix that costs more later.""",
   "Notebook and planner on desk", "LESS PRESSURE, BETTER CHOICES")

sc("""In practice, it looks like this. Without savings, a fridge breaks and you buy the first one that
fits, on a store card, the same day. With savings, you wait two days, compare three models, check the
energy costs, buy the one that's actually cheaper over ten years, and pay cash. Same problem. Better
decision. Lower total cost. Try this: for any purchase over two hundred dollars, give yourself a forty
eight hour rule. If you still want it after two days, buy it. Most of the time, you won't.""", "Appliance store refrigerators", "THE 48 HOUR RULE")

# ---------------- 7 ----------------
ch("7. You stop financing small things")
card("""Change number seven. You stop financing small things. Phones on monthly plans. Furniture in four
payments. Sneakers on buy now pay later.""",
     {"type": "list", "n": 7, "title": "No more small loans", "sub": "if you can't buy it twice, you can't afford it"}, "CHANGE 7")
sc("""Splitting a purchase into payments feels harmless. But every small payment is a claim on your future
paycheck. Stack a few of them and a big part of your income is spoken for before it arrives. With cash
in the bank, you just pay, or you decide you don't need it. Both options are better than a slow drip
of monthly payments.""",
   "Shopping bags retail store", "PAYMENTS ADD UP")
pr("""Quick rule I like. If you can't buy it twice in cash, you probably can't afford it yet. Now, number
eight is one most people never think about.""")

sc("""The trick is that each small payment looks affordable on its own. Thirty dollars here, forty dollars
there. But add up every installment plan, every financing deal and every subscription, and many people
discover hundreds of dollars a month already committed. That's money that can't go to the cushion or to
investing. Try this: list every recurring payment you have, every single one, and total it. Then cancel
or pay off the smallest ones first. Each one you clear frees up cash for good.""", "Subscription services on phone screen", "LIST EVERY PAYMENT")

# ---------------- 8 ----------------
ch("8. You pay less for insurance")
card("""Change number eight. You can pay less for insurance. When you have savings, you can choose a
higher deductible, and a higher deductible usually means a lower premium.""",
     {"type": "list", "n": 8, "title": "Cheaper insurance", "sub": "higher deductible, lower premium"}, "CHANGE 8")
sc("""The deductible is the part you pay yourself before insurance kicks in. If a five hundred dollar
deductible feels scary, you pay a higher premium every single month to avoid it. With twenty thousand
dollars saved, a one thousand dollar deductible is not scary anymore. You can take on that small risk
and keep the monthly savings.""",
   "Car insurance accident damaged car", "YOU CARRY THE SMALL RISK")
sc("""Done carefully, this is one of the quiet ways people with money pay less for the same thing. They
can afford to self insure the small stuff, so they only buy insurance for the big disasters. That's
exactly what insurance is for.""",
   "Family house suburban street", "INSURE THE BIG DISASTERS")

sc("""Here's how the math can work. Say raising a deductible from five hundred to one thousand dollars
lowers a premium by a certain amount each year. If you go several years without a claim, you keep all of
those savings. If you do have a claim, you pay five hundred dollars more that year, which your cushion
covers easily. Over many years, people with savings often come out ahead. Try this: ask your insurer for a
quote with a higher deductible, and compare. It's a five minute phone call that can pay for itself every
year.""", "Insurance policy documents", "ASK FOR THE QUOTE")

# ---------------- 9 ----------------
ch("9. You can negotiate")
card("""Change number nine. You can negotiate. Cash on hand gives you options, and options give you
leverage.""",
     {"type": "list", "n": 9, "title": "You get leverage", "sub": "options are bargaining power"}, "CHANGE 9")
sc("""Some sellers will lower a price for payment in full. Some service providers offer a discount if you
pay a year up front instead of monthly. A used car bought with cash, at the right price, can cost far less
than a new one bought with a loan. None of these deals are available to someone who can only pay a little
at a time.""",
   "Used car dealership lot", "PAYING IN FULL")
sc("""And maybe the biggest negotiation is your salary. When you're not desperate, you can ask for more,
and you can hold out for the right offer. That's not arrogance. It's the calm that comes from not needing
the next paycheck to survive.""",
   "Business meeting handshake office", "ASK FOR MORE")

sc("""Negotiating with cash is not about being aggressive. It's about being ready. When you can say, I can
pay today, in full, what's your best price, you change the conversation. Many sellers would rather take a
little less now than wait for maybe later. Try this: next time you buy something big, a used car,
furniture, a contractor job, ask that exact question. The worst answer you'll get is no.""", "Furniture store showroom", "WHAT'S YOUR BEST PRICE?")

# ---------------- 10 ----------------
ch("10. Money fights get quieter")
card("""Change number ten. Money fights get quieter. Money is one of the most common sources of stress in
relationships, and a cushion takes a lot of that tension out of the room.""",
     {"type": "list", "n": 10, "title": "Fewer money fights", "sub": "less stress at home"}, "CHANGE 10")
sc("""When every surprise bill is a crisis, every surprise bill becomes an argument. Who spent what. Why
there's nothing left. With savings, a surprise bill is just a bill. You can talk about goals instead of
blame. Plans instead of panic.""",
   "Couple at kitchen table", "GOALS, NOT BLAME")
pr("""We're past the halfway point, and the next five changes are where it gets really interesting.
Especially number fifteen. Stay with me.""")

sc("""A cushion also lets couples plan together. Instead of arguing about the last surprise, you can sit
down once a month and talk about the next goal. A vacation paid in cash. A down payment. Paying off the
car. Shared goals turn money from a fight into a project. Try this: pick one evening a month for a short
money meeting. Fifteen minutes. One number to check, the cushion, and one goal to move forward.""", "Couple planning with laptop at home", "A MONTHLY MONEY MEETING")

# ---------------- 11 ----------------
ch("11. You start seeing opportunities")
card("""Change number eleven. You start seeing opportunities. A course that would raise your income. A
small side business. A chance to move to a city with better jobs.""",
     {"type": "list", "n": 11, "title": "You see opportunities", "sub": "you can afford to take a shot"}, "CHANGE 11")
sc("""When you have nothing saved, every opportunity looks like a risk you can't take. With twenty thousand
dollars, you can afford a smart bet. Not your whole cushion. A small part of it, on something that could
pay off for years. That's how many small businesses actually start. Not with a big loan, but with savings.""",
   "Small business storefront open sign", "A SMART BET")

sc("""The rule many people use is to never risk the whole cushion. Keep the core untouched for emergencies,
and only use a small slice, maybe ten or twenty percent, for an opportunity with real upside. A
certification. Tools for a side business. A move for a better job. If it works, your income grows. If it
doesn't, your emergency fund is still there. Try this: write down one opportunity you've been putting off
because of money, and what it would really cost.""", "Laptop with online course", "RISK A SLICE, NOT THE CAKE")

# ---------------- 12 ----------------
ch("12. You think in percentages")
card("""Change number twelve. You start thinking in percentages instead of prices. Not "is this cheap?"
but "what share of my money is this?" """,
     {"type": "list", "n": 12, "title": "Percent, not price", "sub": "how big is this, compared to what I have?"}, "CHANGE 12")
sc("""A two hundred dollar purchase is one percent of twenty thousand. That framing helps you spend without
guilt on what matters, and say no faster to what doesn't. It's also the mindset that makes investing
click, because investing is all about percentages over time.""",
   "Stock market numbers display", "1% OF $20,000")

sc("""Percentages also protect you from small leaks. A coffee subscription, a streaming service, an app
you forgot about. Each one is a tiny percentage. But a dozen of them can add up to a meaningful share of
your monthly savings. When you think in percentages, you see the total, not just the price tag. Try this:
take your monthly savings goal and ask what percent of it each recurring expense eats. It's a sharper way
to decide what stays.""", "Coffee cup and receipt", "SMALL LEAKS ADD UP")

# ---------------- 13 ----------------
ch("13. You become a target")
card("""Change number thirteen. You become a target. As your balance grows, so does the number of people
who want a piece of it.""",
     {"type": "list", "n": 13, "title": "You become a target", "sub": "scams follow money"}, "CHANGE 13")
sc("""The Federal Reserve's latest survey found that twenty percent of adults experienced financial fraud or
a scam in the past year. Fake investment offers, fake bank calls, fake emergencies from fake relatives.
A real cushion deserves real protection. Turn on account alerts, never move money because a caller tells
you to, and be suspicious of anything that promises guaranteed returns.""",
   "Smartphone with phone call screen", "20% HIT BY FRAUD")

sc("""Scammers know that people with savings feel safe, and that's exactly what they exploit. A common
pattern is urgency. Your account is compromised, move your money now. A real bank will never ask you to
move money to a new account to protect it. Try this: agree on a simple rule with your family. Any request
to move money, from anyone, waits twenty four hours and gets verified by calling a number you already
know. That one rule stops most scams cold.""", "Laptop security padlock", "THE 24 HOUR RULE")

# ---------------- 14 ----------------
ch("14. Where to keep it")
card("""Change number fourteen. You have to decide where the money lives. And this is where a lot of people
make a mistake.""",
     {"type": "list", "n": 14, "title": "Where it lives matters", "sub": "safe, separate, and easy to reach"}, "CHANGE 14")
sc("""Emergency money should be safe and easy to reach. The FDIC insures deposits up to two hundred fifty
thousand dollars per depositor, per insured bank, for each account ownership category. So a savings account
at an insured bank is protected even if the bank fails. Keep it in a separate account from your
checking, so you don't spend it by accident.""",
   "FDIC sign bank", "INSURED UP TO $250,000")
sc("""What about the stock market? Long term investing is how wealth grows, but stocks can drop a lot in a
short time. Money you might need next month should not be in something that could be down twenty percent
next month. So the cushion stays in cash. Money beyond the cushion is what you invest.""",
   "Wall Street New York Stock Exchange", "CUSHION IN CASH")

sc("""A simple setup many people use has three layers. Checking for monthly bills. A separate high yield
savings account for the cushion, three to six months of expenses. And investment accounts, like a
retirement account, for everything beyond that. Each layer has a job, and money flows down from one to
the next. Try this: open a separate savings account just for the cushion, and give it a name, like
freedom fund. People who name their savings accounts tend to protect them.""", "Three glass jars with coins", "THREE LAYERS")

# ---------------- 15 ----------------
ch("15. The trap")
pr("""And now, number fifteen. The one I warned you about at the start.""")
card("""Change number fifteen. Twenty thousand dollars makes you feel richer than you are. And that feeling
is the trap.""",
     {"type": "list", "n": 15, "title": "The trap: feeling rich", "sub": "lifestyle creep"}, "CHANGE 15")
sc("""It's called lifestyle creep. The balance looks big, so the car gets nicer, the apartment gets
bigger, and the monthly costs quietly go up. Then one day the cushion is gone, but the higher monthly bills
are still there. You end up with a more expensive life and less protection than before.""",
   "Luxury car showroom", "LIFESTYLE CREEP")
sc("""The fix is simple. Decide in advance what the cushion is for. It's for emergencies, for freedom, and
for opportunities. It's not a shopping budget. When it's spent on an emergency, refilling it becomes the
first priority, before any upgrade.""",
   "Savings account passbook", "DECIDE IN ADVANCE")

sc("""Lifestyle creep is sneaky because every single upgrade feels reasonable. You deserve a nicer car. You
work hard. And maybe you do deserve it. The question is timing. A rule that works: when your income goes
up, send at least half of the raise to savings or investing, and enjoy the other half. You still get a
better life, but your cushion and your future grow faster than your bills. Try this: next time you get a
raise, set up the extra transfer before the first bigger paycheck even arrives.""", "Paycheck and calculator on desk", "HALF THE RAISE")

# ---------------- Three people ----------------
pr("""Quick pause. If these changes are already making you think about your own money, do me a favor and
subscribe to the channel. It's free, it takes one second, and it helps me keep making these videos.""")

ch("Three people, one number")
pr("""Numbers are easier to feel when there's a person behind them. So let me walk you through three
people. They're made up, but every one of them is built from situations that happen to real people every
single day. Watch what twenty thousand dollars does in each story.""")
sc("""Meet Maya. She's thirty one, works in marketing, and spends about four thousand dollars a month on
rent, food, her car and everything else. On a Tuesday morning, her company announces layoffs, and her
whole team is cut. No warning. Two weeks of severance, and that's it.""",
   "Office worker carrying box of belongings", "MAYA: THE LAYOFF")
card("""Here's the difference twenty thousand dollars makes for Maya. With four thousand a month in costs,
her savings cover about five months. That's five months to find the right job, not the first job. People
who can wait for a better offer often come back at the same pay or higher. People who panic tend to accept
less, and that lower salary follows them for years.""",
     {"type": "compare", "left": {"label": "Without savings", "big": "2 weeks", "sub": "take the first offer"},
      "right": {"label": "With $20,000", "big": "5 months", "sub": "wait for the right offer"},
      "note": "Example: $4,000 monthly costs. Use your own numbers."})
sc("""Maya doesn't touch a credit card. She files for unemployment benefits, cuts a few subscriptions,
and spends her mornings applying and her afternoons learning a new skill. Eleven weeks later she accepts a
job that pays a little more than the old one. The layoff still hurt. But it was a bad season, not a
disaster.""",
   "Woman working on laptop at home", "A BAD SEASON, NOT A DISASTER")
sc("""Now meet Daniel. He's forty, a contractor, two kids. His truck's transmission fails, and the
repair quote is three thousand eight hundred dollars. The same week, a client offers him a bigger project,
but he has to buy materials up front, about five thousand dollars, and he gets paid in sixty days.""",
   "Pickup truck in auto repair shop", "DANIEL: TWO BILLS, ONE WEEK")
sc("""Without savings, Daniel has a terrible choice. He can put the repair on a card at over twenty
percent interest and turn down the project. Or he can take a high cost loan and hope the client pays on
time. With twenty thousand dollars, he fixes the truck, buys the materials, and takes the job. The
project pays him far more than the repair cost. Savings didn't just protect Daniel. They let him say yes
to an opportunity.""",
   "Construction worker reviewing plans", "SAVINGS LET YOU SAY YES")
sc("""And finally, meet Priya and Sam. Married, mid thirties, both working. For years, they argued about
money every few weeks. Not about big things. About the dentist bill, the car insurance renewal, the
friend's wedding they had to fly to. Every surprise expense turned into a fight about whose fault it was.""",
   "Couple sitting at kitchen table with bills", "PRIYA AND SAM: THE FIGHTS")
sc("""They didn't fix it with a budgeting app. They fixed it by building a shared cushion, slowly, over
about two and a half years, until it reached twenty thousand dollars. The surprise bills still came. But
now a dentist bill was just a transfer, not an argument. Sam put it simply. We still talk about money. We
just don't fight about it anymore.""",
   "Happy couple walking in park", "A TRANSFER, NOT AN ARGUMENT")
pr("""Three different lives. A layoff, a broken truck, a marriage under pressure. And in every story, the
money did the same thing. It bought time, it bought choices, and it bought peace. That's the pattern you'll
see again and again, and it's why twenty thousand dollars matters more than it looks on paper.""")

# ---------------- Verdict ----------------
ch("The verdict")
pr("""So, what really changes at twenty thousand dollars? Here's my honest verdict.""")
sc("""Not your lifestyle. Your options. Twenty thousand dollars won't make you rich. But it turns
emergencies into bills, stops the broke tax, gives you time to make good decisions, and puts you ahead
of most people around you. It is the foundation that everything else gets built on.""",
   "Construction foundation concrete", "OPTIONS, NOT LIFESTYLE")
card("""And the foundation keeps paying. Once the cushion is full, every extra dollar can go to work. Five
hundred dollars a month, for twenty years, at a seven percent average yearly return, grows to roughly two
hundred sixty thousand dollars. You'd put in one hundred twenty thousand. That's what's on the other side
of the cushion.""",
     {"type": "growth", "monthly": 500, "rate": 0.07, "years": 20})

# ---------------- How to get there ----------------
ch("How to get to $20,000")
sc("""So how do people actually get there? Step one. Automate it. Set up an automatic transfer to a separate
savings account on payday. Money you never see is money you don't spend. Even fifty dollars a paycheck
builds the habit, and the habit matters more than the amount at the start.""",
   "Smartphone banking app", "STEP 1: AUTOMATE")
sc("""Step two. Kill the broke tax first. If you're paying interest on a credit card, a small starter
cushion plus paying down that card often beats everything else, because no savings account pays you
twenty percent. Step three. Send every windfall to the cushion. Tax refunds, bonuses, raises. Before they
become lifestyle.""",
   "Tax refund check", "STEPS 2 AND 3")
card("""Here's what the timeline looks like without any investment growth. Saving five hundred dollars a
month, you reach twenty thousand in forty months, a little over three years. At one thousand a month,
twenty months. Pick a pace you can actually keep.""",
     {"type": "compare", "left": {"label": "$500 a month", "big": "40 months", "sub": "about 3.3 years"},
      "right": {"label": "$1,000 a month", "big": "20 months", "sub": "under 2 years"},
      "note": "Simple savings, no growth assumed"})

# ---------------- Mistakes ----------------
ch("Five mistakes to avoid")
pr("""Before we wrap up, five mistakes I see all the time on the way to twenty thousand. Avoid these and
you'll get there faster.""")
sc("""Mistake one. Waiting for a bigger income to start. The habit comes first, the amount comes later.
People who start with fifty dollars a paycheck usually find that the number grows, because they already
built the system. Mistake two. Keeping the cushion in checking. If it's next to your spending money, it
will get spent. Separate account, different bank if you need it, out of sight.""",
   "Two bank cards on table", "MISTAKES 1 AND 2")
sc("""Mistake three. Investing the emergency fund. When the market drops, that's often exactly when jobs
get cut too. The worst moment to need cash is the moment your investments are down. Keep the cushion
boring on purpose. Mistake four. Treating every sale as a reason to spend. A discount on something you
didn't need is not savings. It's spending with a better story.""",
   "Sale sign in shop window", "MISTAKES 3 AND 4")
sc("""Mistake five. Stopping at the finish line. Many people reach their goal, relax, and slowly drift back.
The better move is to change the destination. Once the cushion is full, redirect that same automatic
transfer into long term investing. Same habit, new job. That's how twenty thousand becomes one hundred
thousand, and one hundred thousand becomes much more.""",
   "Finish line running race", "MISTAKE 5")

# ---------------- Questions ----------------
ch("Questions people ask")
pr("""Before the recap, let me answer the three questions I get the most about this.""")
sc("""Question one. Should I pay off debt first, or build the twenty thousand first? For most people the
answer is both, in order. Build a small starter cushion, say one thousand dollars, so a surprise doesn't
push you deeper into debt. Then attack any debt above about eight percent interest, especially credit
cards. Once that's gone, build the full cushion. Paying off a card at twenty two percent is a guaranteed
return no savings account can match.""",
   "Credit cards and calculator on table", "DEBT OR SAVINGS FIRST?")
card("""Question two. Isn't cash a bad investment because of inflation? As an investment, yes. But this
money isn't an investment. It's insurance. In a high yield savings account paying around four percent,
twenty thousand dollars earns roughly eight hundred dollars a year. In a regular checking account paying
next to nothing, it earns about two dollars. Same safety, very different result.""",
     {"type": "compare", "left": {"label": "Checking at 0.01%", "big": "$2", "sub": "per year"},
      "right": {"label": "High yield at ~4%", "big": "$800", "sub": "per year"},
      "note": "On $20,000. Rates change; check current rates."})
sc("""Question three. Is twenty thousand the right number for me? Maybe not exactly. The real target is
three to six months of your essential costs. If your costs are low, you may need less. If you're self
employed, have kids, or work in an unstable industry, you may want more. Twenty thousand is simply the
point where, for a typical household, the changes in this video really start to show up. Write your own number down today, then divide it by what you can save each
month. That gives you a date, and a goal with a date is a plan, not a wish.""",
   "Family budget planning at table", "YOUR NUMBER")

# ---------------- Recap ----------------
ch("Recap: all 15 changes")
sc("""Let's recap all fifteen. One, emergencies become bills. Two, the broke tax disappears. Three, you
can say no. Four, your credit gets stronger. Five, your money starts working. Six, you think more clearly,
so you decide better. Seven, small payment plans stop eating your income. Eight, insurance gets cheaper.""",
   "Checklist on clipboard", "THE RECAP")
sc("""Nine, you gain leverage to negotiate. Ten, money fights get quieter. Eleven, you can take a smart
shot at an opportunity. Twelve, you think in percentages. Thirteen, you become a target, so you protect
yourself. Fourteen, you keep the money in the right place. And fifteen, the trap. Feeling richer than you
are. Avoid that one, and the other fourteen keep working for you for the rest of your life.""",
   "Notebook with written goals", "15 CHANGES")

# ---------------- Close ----------------
ch("What to do next")
pr("""If you want the full plan, step by step, from zero all the way to your first million, it's in my
playbook. The link is in the description. And if this video helped, the next one is about what changes at
one hundred thousand dollars. That's where things get really interesting. I'm Ryan Rover. See you there.""")

save("video01", "What Changes When You Have $20,000 in the Bank", [
    "Federal Reserve, Economic Well-Being of U.S. Households in 2025 (May 2026): https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-executive-summary.htm",
    "Federal Reserve, Survey of Consumer Finances 2022 (median transaction accounts $8,000)",
    "Bankrate, Emergency Savings Report 2026: https://www.bankrate.com/banking/savings/emergency-savings-survey",
    "CFPB, What is a payday loan (fee of $15 per $100 equals almost 400% APR)",
    "Federal Reserve G.19 Consumer Credit (credit card interest rates)",
    "FDIC, Deposit Insurance ($250,000 per depositor, per insured bank, per ownership category)",
    "Mullainathan and Shafir, Scarcity: Why Having Too Little Means So Much (2013)",
], "what changes at $20k in the bank")
