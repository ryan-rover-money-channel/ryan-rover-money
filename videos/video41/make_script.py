import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

def item(n, title, sub, card_text, body, example, q1, c1, q2, c2):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"REASON {n}")
    sc(body, q1, c1)
    sc(example, q2, c2)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Here's something strange. Americans earn more today than almost any generation in
history, and yet millions of people with good jobs still feel broke at the end of every month. Not poor.
Broke. The paycheck comes in, and a few days later it's gone. So today, the big question. Why do most
people stay broke? And more importantly, how do you escape?""")
short("Why do people with good jobs still feel broke every month?")
card("""The most common money pattern in America isn't poverty. It's the paycheck to paycheck loop. Money
comes in, money goes out, and almost nothing sticks.""",
     {"type": "stat", "label": "the real problem", "big": "IN → OUT", "sub": "the paycheck to paycheck loop"})
sc("""Here's the uncomfortable truth. Staying broke is rarely about one big mistake. It's about a system.
Small leaks, habits you never chose on purpose, and a few traps that are designed by very smart people to
keep your money moving out of your account. Once you see that system, you can't unsee it. And that's
where the escape starts.""",
   "Empty wallet on table", "IT'S A SYSTEM")
sc("""We're going to look at this from three angles. First, the numbers. What the data actually says about
how Americans earn, spend, save and borrow. Second, the psychology. The ten mental traps that keep smart
people broke. And third, the playbook. A step by step escape plan you can start this week, even on an
ordinary income.""",
   "Three paths in forest", "THREE ANGLES")
pr("""Stay to the end, because the escape plan is the part most videos skip. Let's start with the numbers.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Every number in this video comes from a named source. Household finances come from the Federal
Reserve, including its yearly survey on the economic well being of American households, and the Survey of
Consumer Finances. Debt totals come from the Federal Reserve Bank of New York. Saving rates come from the
Bureau of Economic Analysis. Where I use an example, it's simple stated math, not a promise. This is
education, not financial advice.""",
   "Federal Reserve building Washington", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Before we talk about why, let's look at what's actually happening.""")
card("""Start with the most famous test in personal finance. The Federal Reserve asks adults how they would
pay for a surprise four hundred dollar expense. In recent years, only about six in ten said they would
cover it with cash or its equivalent. That means roughly four in ten would need to borrow, sell
something, or simply couldn't pay.""",
     {"type": "stat", "label": "a $400 surprise expense", "big": "~4 in 10", "sub": "could not cover it with cash (Federal Reserve)"})
sc("""Think about how small four hundred dollars is. A car repair. A vet bill. A dental visit. For millions of
households, an expense like that doesn't just hurt. It goes straight onto a credit card, and that's where
the loop begins. The emergency becomes debt, the debt becomes interest, and the interest becomes a
monthly bill that eats into the next paycheck.""",
   "Car repair mechanic garage", "A $400 PROBLEM")
card("""Now the debt side. According to the Federal Reserve Bank of New York, Americans owe more than one
trillion dollars on credit cards. That's more than one thousand billion dollars, much of it charged
interest at rates above twenty percent a year.""",
     {"type": "stat", "label": "u.s. credit card balances", "big": "$1 TRILLION+", "size": 170, "sub": "Federal Reserve Bank of New York"})
sc("""Here's what that rate means in real life. If you carry a five thousand dollar balance at twenty two
percent, you pay roughly eleven hundred dollars a year in interest alone. That's eleven hundred dollars
that buys nothing. No groceries, no fun, no progress. It's the price of having spent money before you had
it. And because the minimum payment is so small, many people carry that balance for years.""",
   "Credit cards pile", "$1,100 A YEAR FOR NOTHING")
card("""Let's look at one of those minimum payments. Five thousand dollars at twenty two percent, paying only
a small minimum each month, can take well over a decade to clear, and the total interest can end up
larger than the original balance. Paying a fixed two hundred dollars a month instead clears it in about
three years.""",
     {"type": "compare", "left": {"label": "Minimum only", "big": "10+ years", "sub": "interest can top the balance"},
      "right": {"label": "$200 a month", "big": "~3 years", "sub": "under $2,000 interest"},
      "note": "Illustration at 22% APR. Your card's terms will differ."})
sc("""Now the savings side. The Bureau of Economic Analysis tracks something called the personal saving rate,
the share of after tax income that households don't spend. In recent years it has often sat somewhere
around four to five percent. In other words, out of every hundred dollars that reaches the average
household, roughly ninety five gets spent.""",
   "Piggy bank coins", "95 OF EVERY 100 SPENT")
sc("""And that's the average. Averages hide a lot. Some households save a big share of what they earn.
Many save nothing at all, and some spend more than they make, filling the gap with credit. When you hear
that Americans save five percent, picture a crowd where a few people save a lot, and a lot of people are
running on empty.""",
   "Crowd of people walking city street", "AVERAGES HIDE A LOT")
sc("""So where does the money actually go? The Bureau of Labor Statistics runs a Consumer Expenditure
Survey that tracks household spending. Year after year, the same three categories dominate. Housing takes
roughly a third of the typical household budget. Transportation, mostly cars, takes around one sixth. And
food, at home and eating out, takes around one eighth.""",
   "Suburban street houses cars", "THE BIG THREE")
card("""Housing, transportation and food. Together, they make up around six of every ten dollars a typical
household spends. That's where the big wins are hiding, not in skipping a coffee.""",
     {"type": "stat", "label": "housing + cars + food", "big": "~60%", "sub": "of household spending (BLS Consumer Expenditure Survey)"})
sc("""This matters because most money advice focuses on tiny things. Skip the latte. Bring lunch. Those
habits help, but they're small. One decision on rent, one decision on a car, can be worth more than a
thousand skipped coffees. A car payment of six hundred dollars versus three hundred dollars is a gap of
three thousand six hundred dollars a year, every year, for the whole loan. If you want to escape faster,
look at the big three first.""",
   "Car keys and loan papers", "BIG DECISIONS FIRST")
card("""Here's another number that surprises people. The Federal Reserve's Survey of Consumer Finances found
the median net worth for families headed by someone under thirty five was about thirty nine thousand
dollars in twenty twenty two. Half had more, half had less, and that includes things like cars and home
equity.""",
     {"type": "stat", "label": "median net worth, under 35", "big": "$39,040", "sub": "Federal Reserve, SCF 2022"})
sc("""So what does the data tell us? It tells us that being broke is not rare, and it's not a personal
failing that only happens to careless people. It's the normal outcome of a normal system. Income goes up,
spending follows it, and easy credit fills every gap. If you do what everyone else does, you'll get what
everyone else gets.""",
   "Highway traffic rush hour", "NORMAL IS BROKE")
sc("""But there's a second message in the data, and it's the hopeful one. The difference between the
households who build wealth and the households who don't is often not their income. Plenty of high
earners are broke. Plenty of ordinary earners quietly build a cushion and then investments. The gap is
mostly in what happens after the money arrives. And that's something you can change.""",
   "Small house with garden", "IT'S NOT JUST INCOME")
card("""Look at what that gap can become. Suppose you redirect just three hundred dollars a month that used
to leak out, and invest it at a seven percent average yearly return. After twenty years, you'd have put in
seventy two thousand dollars. Here's roughly what it could grow to.""",
     {"type": "growth", "monthly": 300, "rate": 0.07, "years": 20})
sc("""That's an illustration, not a promise. Markets go up and down, and some years are negative. But the
point is clear. Three hundred dollars a month is not a lottery win. It's a car payment. A few
subscriptions and takeout nights. The money that keeps people broke is often the same money that could
make them comfortable.""",
   "Takeout food delivery bag", "THE SAME $300")
# ---------------- Hidden costs ----------------
ch("The hidden costs of being broke")
sc("""There's one more set of numbers that rarely makes the news. Being broke is expensive. Not in a
poetic way. In actual dollars. When you have no cushion, you pay fees and prices that people with savings
simply avoid. Let me show you a few.""",
   "Receipts and coins scattered", "BROKE IS EXPENSIVE")
sc("""Overdraft and late fees are the obvious ones. One overdraft can cost around thirty dollars at many
banks, even if the purchase was a five dollar coffee. A late card payment can add a fee and sometimes a
higher penalty rate. People with a cushion rarely pay these. People without one can pay them every few
months.""",
   "Bank fee notice letter", "FEES ON TOP OF FEES")
sc("""Then there's credit. A lower credit score usually means higher interest on car loans, higher
deposits on apartments and utilities, and in many states, higher car insurance premiums. Two people can
buy the same car at the same price and pay very different amounts over the life of the loan, just because
of their credit history.""",
   "Car dealership lot", "THE CREDIT TAX")
sc("""And there's the cost of buying small. When money is tight, you buy the small pack instead of the
bulk pack, the cheap shoes that wear out in a year instead of the good pair that lasts five. Each choice
makes sense in the moment. Over a year, they add up. This is why the first cushion matters so much. It's
not just safety. It's the ticket out of the expensive way of living.""",
   "Grocery store shelves", "BUYING SMALL COSTS MORE")
sc("""Add it all up, and many households without savings lose hundreds or even thousands of dollars a year
to fees, interest and higher prices. That money is the hidden tax on being broke. And the good news is,
it's also one of the first things you get back when you escape.""",
   "Calculator and bills", "THE HIDDEN TAX")
pr("""So the numbers show the what. Now let's get to the why. Because if the math were all it took, nobody
would be broke.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
pr("""Angle two. The psychology. These are the ten mental traps that keep smart, hard working people broke.
See how many you recognize.""")
short("The mental trap that keeps smart people broke")

item(1, "Scarcity tunnels your vision", "stress shrinks your focus",
"""Reason number one. Scarcity tunnels your vision.""",
"""Researchers Sendhil Mullainathan and Eldar Shafir wrote a book called Scarcity. Their core idea is
simple. When you're short on money, your mind focuses hard on the urgent problem in front of you, like
this week's rent. That focus helps in the moment, but it pushes everything else out. Long term planning,
saving, comparing prices. They called it tunneling.""",
"""Here's what that looks like. You're short this month, so you put the electric bill on a card to get
through. It solves today's problem perfectly. But it creates next month's problem, with interest. When
you're inside the tunnel, that trade looks reasonable. From outside, it's a trap. Try this: make your
money decisions on a calm day, once a month, not in the middle of a crisis.""",
"Tunnel with light at the end", "THE TUNNEL",
"Calendar with circled date", "DECIDE ON A CALM DAY")

item(2, "Present bias", "today always wins",
"""Reason number two. Present bias. Today always wins.""",
"""Economists use the term present bias for a simple human habit. We value a reward today much more than
a bigger reward later. Fifty dollars now feels better than seventy dollars next year, even though the
second is the better deal. Saving asks you to give up something real today for something abstract in the
future. Your brain is wired to resist that.""",
"""This is why willpower alone fails. Every single day, the present makes a better argument than the
future. The fix isn't to try harder. It's to remove the daily decision. When saving happens
automatically on payday, the present never gets a vote. Try this: set an automatic transfer to savings
for the day after your paycheck lands. Start with any amount.""",
"Hourglass on desk", "NOW BEATS LATER",
"Online banking on smartphone", "AUTOMATE IT")

item(3, "Comparison spending", "keeping up with the feed",
"""Reason number three. Comparison spending.""",
"""People have always compared themselves with their neighbors. The difference now is that your neighbors
are everyone on your phone. You see vacations, new cars, renovated kitchens and designer bags all day
long. You don't see the loans behind them. And because what's normal keeps shifting upward, ordinary
spending starts to feel like falling behind.""",
"""A useful reminder: you're comparing your full financial picture with someone else's highlight reel.
The car is visible. The car payment isn't. The trip is visible. The credit card balance isn't. Try this:
for one week, before any purchase over fifty dollars, ask yourself one question. Would I still buy this if
nobody could ever see it?""",
"Person scrolling phone social media", "THE HIGHLIGHT REEL",
"Luxury car parked street", "YOU SEE THE CAR, NOT THE LOAN")

item(4, "Lifestyle creep", "the raise disappears",
"""Reason number four. Lifestyle creep.""",
"""Lifestyle creep is what happens when your spending rises every time your income does. A raise arrives,
and soon the apartment is nicer, the car is newer, and dinners out become a habit. None of these choices
feels big. But together they absorb the whole raise, and you end up with the same savings at a higher
income.""",
"""Here's the sneaky part. Upgrades are easy to make and painful to undo. Once you're used to a better
phone, a bigger place or a premium subscription, going back feels like a loss. Psychologists call this
the hedonic treadmill. The fix is to decide in advance. Try this: next time you get a raise, send at least
half of the increase to savings or investing before you ever get used to spending it.""",
"Moving boxes new apartment", "THE RAISE DISAPPEARS",
"Treadmill in gym", "THE HEDONIC TREADMILL")

item(5, "Mental accounting", "not all dollars feel equal",
"""Reason number five. Mental accounting.""",
"""Economist Richard Thaler, who later won a Nobel prize, described how people sort money into mental
buckets. Tax refunds feel like bonus money. Cash feels more real than a card. A twenty dollar bill found
in a coat feels free. But a dollar is a dollar. Treating some money as play money is one of the easiest
ways for it to disappear.""",
"""Think about the tax refund. Many people treat it like a gift and spend it on something fun, while
carrying a credit card balance at twenty percent. Paying down the card would be worth far more. Try
this: give every windfall a plan before it arrives. A simple split works. For example, most of it to debt
or savings, and a small, guilt free slice for fun.""",
"Coins sorted in jars", "A DOLLAR IS A DOLLAR",
"Tax refund check", "PLAN THE WINDFALL")

pr("""We're halfway through the traps. The next one is the one I see most often, and it's hiding in plain
sight.""")

item(6, "The ostrich effect", "not looking feels safer",
"""Reason number six. The ostrich effect.""",
"""Researchers have found that people check their accounts more often when markets are up, and avoid
looking when things are bad. It's called the ostrich effect, after the myth that ostriches bury their
heads in the sand. When money is tight, opening the banking app feels painful, so people stop opening it.
And what you don't look at, you can't fix.""",
"""Not looking has real costs. Missed due dates lead to late fees. Forgotten subscriptions keep renewing.
Interest quietly grows. The irony is that the anxiety of not knowing is usually worse than the number
itself. Try this: schedule a fifteen minute money check every Sunday. Same time, same coffee. Just look.
No judgment.""",
"Ostrich bird", "THE OSTRICH EFFECT",
"Coffee cup next to laptop morning", "15 MINUTES EVERY SUNDAY")

item(7, "Easy credit", "spending before earning",
"""Reason number seven. Credit makes spending painless.""",
"""Researchers have long observed that paying with a card often feels less painful than paying with cash,
and people tend to spend more when the pain is lower. Tap to pay, one click checkout, saved cards, and
buy now pay later all remove the tiny moment of friction that used to make us think twice.""",
"""Credit isn't evil. Used well, it's a tool. But when spending becomes painless, it also becomes
invisible. And the bill arrives later, when the excitement is gone. Try this: remove saved cards from your
shopping apps and browsers. That extra minute of typing your card number back in is one of the cheapest
money tools there is.""",
"Contactless payment card terminal", "PAINLESS SPENDING",
"Online shopping cart laptop", "ADD FRICTION BACK")

item(8, "Optimism bias", "next month will be different",
"""Reason number eight. Optimism bias.""",
"""Most people believe next month will be cheaper than this month. This month had a birthday, a car
repair, a trip. Next month will be normal. But every month has something. Psychologists call the habit of
expecting things to go better than average optimism bias, and in money it shows up as budgets that never
include the irregular stuff.""",
"""The fix is to plan for the irregular as if it were regular. Car maintenance, gifts, annual
subscriptions, medical copays. Add up what you spent on these over the last year and divide by twelve.
That's a real monthly expense, even if it doesn't show up monthly. Try this: open a separate savings
bucket called irregular, and put that monthly amount into it.""",
"Birthday party gifts", "EVERY MONTH HAS SOMETHING",
"Glass jar labeled savings", "THE IRREGULAR BUCKET")

item(9, "Identity", "people like me aren't savers",
"""Reason number nine. Identity.""",
"""Many people carry an unspoken belief about money. People like me aren't good with money. Rich people
are different. Investing is for experts. Those beliefs often come from childhood, from how money was
talked about at home. And they quietly decide what you even try.""",
"""Here's the thing. Being good with money isn't a personality. It's a short list of habits. Spend less
than you earn. Keep a cushion. Avoid high interest debt. Invest the difference for a long time. Anyone
can learn those. Try this: replace the sentence I'm bad with money with I'm learning to manage money.
It sounds small. It changes what you're willing to try.""",
"Family photo album old", "WHERE BELIEFS COME FROM",
"Person reading book in library", "A SKILL, NOT A TRAIT")

item(10, "Waiting for more income", "I'll save when I earn more",
"""Reason number ten. Waiting until you earn more.""",
"""This is maybe the most common trap of all. I'll start saving when I get the promotion. When the loan is
paid. When things calm down. But as we saw, when income rises, spending usually rises too. People who
can't save on fifty thousand dollars a year often can't save on eighty thousand either, because the
habit, not the income, was missing.""",
"""The habit has to come first, even if the number is tiny. Saving twenty five dollars a week doesn't
change your net worth much. It changes you. It proves you can do it, and it builds the system that will
handle bigger amounts later. Try this: start with one percent of your income. Next month, two. Raise it
until you feel it, then stop for a while.""",
"Office worker at desk", "WAITING FOR MORE",
"Small plant growing in soil", "THE HABIT FIRST")

# ---------------- Self test ----------------
ch("Are you in the loop? A quick test")
pr("""Before the escape plan, a quick self test. Answer honestly, just for yourself. Count how many are a
yes.""")
sc("""One. Is your checking account close to zero the day before payday? Two. Do you carry a credit card
balance from month to month? Three. If a five hundred dollar bill arrived tomorrow, would it go on a
card? Four. Do you avoid opening your banking app when money is tight?""",
   "Questionnaire checklist pen", "THE TEST: 1 TO 4")
sc("""Five. Has your income gone up in the last few years without your savings going up? Six. Do you have
subscriptions you haven't used in a month? Seven. Do you say you'll start saving when something changes?
And eight. Do you not know, roughly, what you spent last month?""",
   "Person looking at receipts", "THE TEST: 5 TO 8")
sc("""If you said yes to zero or one, you're probably already out of the loop. Two to four, you're on the
edge, and a few changes will make a big difference. Five or more, you're in it, like millions of other
people. That's not a judgment. It's a starting point. And every one of those questions maps to a step in
the playbook coming up next.""",
   "Road sign starting point", "YOUR STARTING POINT")

# ---------------- Mid ----------------
ch("A quick favor")
pr("""Quick pause. If this is helping you see your money differently, subscribe to the channel. It's free,
and it helps me keep making these long, detailed videos for you. Now, the part that actually changes
things. The escape plan.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
pr("""Angle three. The playbook. Ten steps to escape the broke loop, in order. You don't need to do them
all this week. You need to do the next one.""")
short("10 steps to escape the paycheck to paycheck loop")
sc("""Step one. Find your real number. Look at the last three months of bank and card statements and
add up everything that went out. Not what you think you spend. What you actually spent. Divide by three.
That's your real monthly cost of living. Most people are surprised, and that surprise is useful.""",
   "Bank statements highlighter", "STEP 1: YOUR REAL NUMBER")
sc("""Step two. Build a starter cushion. Before anything fancy, get one thousand dollars, or one month of
essential expenses, into a separate savings account. This is the wall between you and the next credit
card emergency. It won't solve everything, but it breaks the cycle where every surprise becomes debt.""",
   "Savings account passbook", "STEP 2: THE STARTER CUSHION")
card("""How fast can you build it? At fifty dollars a week, you reach about one thousand dollars in five
months. At one hundred dollars a week, about ten weeks. Pick a pace you can actually keep.""",
     {"type": "compare", "left": {"label": "$50 a week", "big": "~5 months", "sub": "to $1,000"},
      "right": {"label": "$100 a week", "big": "~10 weeks", "sub": "to $1,000"},
      "note": "Simple math, before any interest."})
sc("""Step three. Stop the bleeding. Cancel what you don't use. Most people have at least a few
subscriptions they forgot about. Call your phone and internet providers and ask for a better rate. Shop
your car insurance once a year. These are one time actions that save money every single month after,
without any willpower.""",
   "Phone call customer service", "STEP 3: STOP THE BLEEDING")
sc("""Step four. List every debt. Write down each balance, its interest rate and its minimum payment.
Then choose a method. The avalanche method pays the highest rate first, which saves the most money. The
snowball method pays the smallest balance first, which gives you quick wins. Both work if you stick with
them. The best method is the one you'll actually follow.""",
   "Notepad list with pen", "STEP 4: LIST EVERY DEBT")
card("""Here's the core difference. Avalanche: highest interest first, the least total interest. Snowball:
smallest balance first, the fastest early wins. Pick one and keep going.""",
     {"type": "compare", "left": {"label": "Avalanche", "big": "Highest %", "sub": "least interest paid"},
      "right": {"label": "Snowball", "big": "Smallest $", "sub": "fastest early wins"},
      "note": "Both work. Consistency matters most."})
sc("""Step five. Automate the good stuff. On payday, money should leave automatically for your cushion,
your extra debt payment and eventually your investments. What's left is yours to spend without guilt.
This flips the usual order. Instead of saving what's left after spending, you spend what's left after
saving. That one switch is the heart of the whole escape.""",
   "Automatic payment bank app", "STEP 5: PAY YOURSELF FIRST")
sc("""Step six. Add friction to impulse spending. Remove saved cards. Unsubscribe from store emails. Use
a twenty four hour rule for anything that isn't a need. If you still want it tomorrow, fine. Very often,
you won't. Small barriers beat big intentions.""",
   "Unsubscribe email inbox", "STEP 6: ADD FRICTION")
sc("""Step seven. Plan the irregular. Remember the optimism trap. Create a sinking fund, which is just a
savings bucket for a known future cost. Car repairs. Holidays. Annual fees. Medical. Put a little in each
month, so when the bill comes, it's already paid. This is how you stop getting surprised by things that
weren't really surprises.""",
   "Christmas gifts wrapped", "STEP 7: SINKING FUNDS")
sc("""Step eight. Grow your income. Cutting has a limit. Earning doesn't. Ask for a raise with evidence of
what you've delivered. Learn a skill that pays more. Take on a side job for a set period with a specific
goal, like clearing a card. And here's the key: send every extra dollar to your plan, not your lifestyle.""",
   "Job interview handshake", "STEP 8: EARN MORE")
sc("""Step nine. Build the full emergency fund. Once high interest debt is gone, grow the cushion to
three to six months of essential expenses. More if your income is irregular. This is the moment the loop
truly breaks. A job loss or a big repair becomes a problem, not a crisis.""",
   "Stack of dollar bills", "STEP 9: THREE TO SIX MONTHS")
sc("""Step ten. Start investing for the long term. Take the same automatic payments that used to go to
debt, and point them at a retirement account and low cost diversified funds. Get any employer match
first, because that's part of your pay. Then let time do the heavy lifting.""",
   "Stock market chart on laptop", "STEP 10: INVEST")
card("""Here's why step ten matters so much. Say you were paying four hundred dollars a month toward a card.
Once it's gone, you invest that same four hundred dollars a month at a seven percent average yearly
return. Over twenty five years, here's roughly where that habit could lead.""",
     {"type": "growth", "monthly": 400, "rate": 0.07, "years": 25})
sc("""That's an illustration, not a promise. But look at the shape of it. The payment you were already
used to making becomes the engine of your future. You don't need to feel richer to start. You just need
to keep making the same payment to a better place.""",
   "Sunrise over city skyline", "SAME PAYMENT, NEW DESTINATION")
pr("""Ten steps. Find your number, build a cushion, stop the leaks, list your debts, automate, add friction,
plan the irregular, earn more, finish the emergency fund, and invest. That's the whole escape.""")

# ---------------- Real people ----------------
ch("Three ways out")
pr("""Let me make this real with three people. They're examples, but you'll probably recognize at least one.""")
short("Three people, three ways out of being broke")
sc("""Jasmine, twenty nine, earns a decent salary in a big city. She's never missed rent, but she's never
had more than a few hundred dollars saved either. Her problem is lifestyle creep and comparison. When she
tracked three months of spending, she found about six hundred dollars a month in takeout, rideshares and
subscriptions she barely noticed.""",
   "Young woman in city apartment", "JASMINE: THE LEAKS")
sc("""She didn't cut everything. She cut half. Three hundred dollars a month moved automatically into
savings on payday. In a little over three months she had her starter cushion. A year later, she had a
real emergency fund. Same job, same city. The difference was the order. Save first, then spend.""",
   "Woman smiling with coffee cup", "SAVE FIRST, THEN SPEND")
sc("""Marcus, thirty eight, has two kids and about fourteen thousand dollars across three credit cards.
Every month he pays the minimums and wonders where the money goes. His problem is the debt loop. Every
surprise expense lands on a card, and the interest keeps the balance stuck.""",
   "Father with children at home", "MARCUS: THE DEBT LOOP")
sc("""Marcus built a one thousand dollar cushion first, so new emergencies stopped going on the cards.
Then he listed his debts and used the avalanche, highest rate first. He picked up weekend shifts for a
year and sent all of it to the debt. It took about two and a half years. Then he pointed the same monthly
payment at investing.""",
   "Man working weekend shift warehouse", "CUSHION, THEN AVALANCHE")
sc("""And Linda, fifty two, earns well and has no debt, but has almost nothing saved for retirement. Her
problem is the waiting trap. She always meant to start. Now she's catching up. People fifty and older can
make extra catch up contributions to retirement accounts, and her income is at its peak, so she can save
a high share. She can't change the past. She can change the next fifteen years.""",
   "Middle aged woman reviewing documents", "LINDA: THE WAITING TRAP")
sc("""Three different people. Three different traps. One shared solution. They stopped relying on
willpower and built a system. A cushion, an automatic transfer, a clear order of priorities. The system
did the work on the days they didn't feel like it.""",
   "Gears machine working", "A SYSTEM, NOT WILLPOWER")

# ---------------- Stages ----------------
ch("What escaping feels like")
pr("""Let me tell you what escaping actually feels like, stage by stage. Because it's not one moment. It's a
series of small ones.""")
sc("""Stage one. The first month. It feels uncomfortable. You're looking at numbers you avoided. You're
saying no to things you used to say yes to. Nothing in your life looks different yet. This is the stage
where most people quit, because the effort is real and the reward is invisible.""",
   "Person thinking at window", "STAGE 1: UNCOMFORTABLE")
sc("""Stage two. Around month three to six. The starter cushion is there. A bill arrives that would have
gone on a card, and you just pay it. That's the first real win. Your stress drops a little. You start
checking your accounts because you want to, not because you're scared to.""",
   "Relieved woman at desk", "STAGE 2: THE FIRST WIN")
sc("""Stage three. Somewhere in the first two years. The last high interest debt is gone. The money that
used to go to interest is suddenly yours. It feels like a raise, because it is one. This is often when
people realize the system works, and they start to get a little ambitious.""",
   "Celebration confetti", "STAGE 3: THE RAISE YOU GAVE YOURSELF")
sc("""Stage four. The full emergency fund and the first investments. You stop thinking of yourself as
someone who's broke. A job change, a car repair or a medical bill becomes a decision, not a disaster. And
quietly, the investments start to grow on their own. That's the moment the loop is officially broken.
You're no longer escaping. You're building.""",
   "Person walking on beach calm", "STAGE 4: BUILDING")

# ---------------- Myths ----------------
ch("Five myths that keep people stuck")
sc("""Before the questions, five myths that keep people stuck. Myth one. You need a high income to build
wealth. Income helps, but the gap between what you earn and what you spend matters more. Myth two.
Budgets are about restriction. A good budget is just a plan that tells your money where to go before it
disappears.""",
   "Myth vs fact sign", "MYTHS 1 AND 2")
sc("""Myth three. Small amounts don't matter. Small amounts, repeated for years and compounded, are how
most ordinary people build wealth. Myth four. Investing is gambling. Picking hot stocks on a hunch can
be. Owning broad, diversified funds for decades is a very different thing, though it still carries risk.
And myth five. It's too late. It's later than it could have been. It's never too late to make the next
ten years better than the last ten.""",
   "Old clock tower", "MYTHS 3, 4 AND 5")

# ---------------- FAQ ----------------
ch("Questions people ask")
pr("""Now the questions people ask me most about escaping the broke loop.""")
sc("""Question one. Should I save or pay off debt first? For most people, a small starter cushion comes
first, so new emergencies don't create new debt. Then attack high interest debt aggressively, because
paying off a card at twenty percent is like earning a guaranteed twenty percent return. Then build the
full emergency fund, then invest. One exception: if your employer matches retirement contributions, many
people grab at least the match early, because that's free money.""",
   "Scale balancing coins", "SAVE OR PAY DEBT?")
sc("""Question two. What if I truly can't cut anything? Sometimes the budget really is tight, and the
problem is income, not spending. If that's you, focus on step eight. Ask for a raise, look at better
paying roles, learn a skill, or add a temporary side income with a clear goal. Also check whether you
qualify for programs that lower essential costs. There's no shame in it.""",
   "Person studying laptop at night", "WHAT IF I CAN'T CUT?")
sc("""Question three. Is a debt consolidation loan a good idea? It can be, if it gives you a lower
interest rate and you stop using the cards. The danger is that people consolidate, feel relief, and then
run the cards back up. Now they have the loan and the card debt. If you consolidate, close the loop
first: build the cushion and remove the cards from your wallet and your apps.""",
   "Loan documents signing", "CONSOLIDATION?")
sc("""Question four. How long does it take to stop feeling broke? Most people feel a real difference
within three to six months of starting, usually when the starter cushion is in place. The first time a
surprise bill arrives and you just pay it from savings, without a card, is a turning point. Many people
say that feeling is worth more than the money itself.""",
   "Relaxed person on couch", "WHEN DOES IT FEEL BETTER?")
sc("""Question five. What about my partner? Money is one of the most common things couples argue about.
The escape works best as a team. Sit down on a calm day, share your real numbers, and agree on the next
single step. Not the whole plan. One step. Then celebrate it together when it's done.""",
   "Couple talking at kitchen table", "WHAT ABOUT MY PARTNER?")
sc("""Question six. Should I use buy now pay later? It's convenient, and some plans charge no interest if
you pay on time. But it makes spending painless again, and several plans at once can add up quickly and
quietly. If you're trying to escape the broke loop, a simple rule is: if you can't afford it today, don't
split it into four.""",
   "Online checkout payment options", "BUY NOW, PAY LATER?")
sc("""Question eight. Does my credit score really matter if I'm not borrowing? Yes, more than people
think. Landlords, insurers in many states, and even some employers may look at credit information. A
better score can mean lower deposits, lower rates and more options. The basics are simple: pay every bill
on time, keep card balances low compared with your limits, and check your credit reports for errors. You
can get your reports for free from the official site, annual credit report dot com.""",
   "Credit score report on screen", "DOES CREDIT MATTER?")
sc("""And question seven. What's the very first thing I should do today? Open your banking app and look.
That's it. Look at your balance, your last thirty days, and your debts. The ostrich effect is the first
trap to break, because every other step depends on knowing where you stand.""",
   "Hand holding phone banking app", "THE FIRST THING TODAY")

# ---------------- This week ----------------
ch("Your first week")
sc("""Here's a simple first week. Day one, look at your accounts. Day two, add up last month's spending.
Day three, cancel two things you don't use. Day four, open a separate savings account if you don't have
one. Day five, set up an automatic transfer, even ten dollars. Day six, list your debts by interest
rate. Day seven, rest. You've already done more than most people do in a year.""",
   "Weekly planner open on desk", "YOUR FIRST WEEK")
sc("""None of these steps need a big income. None of them take more than an hour. But together they flip
the system. You stop being the person things happen to, and start being the person who decides where the
money goes.""",
   "Person writing plan in notebook", "YOU DECIDE")

# ---------------- Recap ----------------
ch("Recap")
short("Why most people stay broke, in 30 seconds")
sc("""Quick recap. The numbers: about four in ten adults couldn't cover a four hundred dollar surprise with
cash, Americans owe over a trillion dollars on credit cards, and the average household saves only a small
slice of its income. Broke is normal, but it's not permanent.""",
   "Checklist clipboard", "THE NUMBERS")
sc("""The psychology: scarcity tunnels your vision, today beats tomorrow, comparison spending, lifestyle
creep, mental accounting, the ostrich effect, painless credit, optimism bias, identity, and waiting for
more income. Ten traps, all human, all fixable.""",
   "Brain illustration thinking", "THE TEN TRAPS")
sc("""And the playbook: find your number, build a cushion, stop the leaks, list your debts, automate,
add friction, plan the irregular, earn more, finish the emergency fund, and invest. One step at a time,
in that order.""",
   "Stairs going up", "THE TEN STEPS")

# ---------------- Close ----------------
ch("What to do next")
pr("""If you want the whole plan in one place, from broke to your first million, it's in my playbook. The
link is in the description. And if you're building your cushion right now, watch my video on what changes
when you have twenty thousand dollars in the bank. That's where this road leads. I'm Ryan Rover. See you
in the next one.""")

save("video41", "Why Most People Stay Broke (And How to Escape)", [
    "Federal Reserve, Economic Well-Being of U.S. Households (SHED): share of adults who would cover a $400 expense with cash or its equivalent",
    "Federal Reserve Bank of New York, Quarterly Report on Household Debt and Credit (credit card balances above $1 trillion)",
    "Federal Reserve, G.19 Consumer Credit (credit card interest rates above 20%)",
    "U.S. Bureau of Economic Analysis, Personal Saving Rate",
    "Federal Reserve, Survey of Consumer Finances 2022 (median net worth under 35: $39,040)",
    "Mullainathan and Shafir, Scarcity: Why Having Too Little Means So Much (2013)",
    "Richard Thaler, mental accounting research; IRS catch-up contribution rules (check current limits)",
    "Debt payoff and growth figures: stated illustrative math",
], "why people stay broke: numbers, psychology, playbook")
