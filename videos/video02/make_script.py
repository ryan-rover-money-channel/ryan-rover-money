import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save

def item(n, title, sub, card_text, body, example, q1, c1, q2, c2):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"CHANGE {n}")
    sc(body, q1, c1)
    sc(example, q2, c2)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Charlie Munger, Warren Buffett's longtime partner, used to say the first one
hundred thousand dollars is the hardest. He didn't say it that politely, but you get the idea. So today,
the real question. What actually changes when your net worth hits one hundred thousand dollars? Because
something does change. And it's not what most people expect.""")
card("""One hundred thousand dollars of net worth. That's everything you own, your savings, your investments,
the equity in your home, minus everything you owe. It's the line where money starts behaving differently.""",
     {"type": "stat", "label": "net worth", "big": "$100,000", "sub": "what you own minus what you owe"})
sc("""Here's why that line matters. Below it, almost all of your progress comes from what you save out of
your paycheck. Above it, your money starts doing a real share of the work. The growth on your money
starts to rival the money you put in. That's the moment the game changes, and most people never notice
it happening.""",
   "New York Stock Exchange trading floor", "THE GAME CHANGES")
sc("""In this video, we'll go through fifteen things that change at one hundred thousand dollars. Some are
exciting. Some are dangerous. And number fifteen is the mistake that keeps a lot of people stuck right at
this level for years. We'll also look at exactly how long it takes to get there, with real math.""",
   "Calculator with financial charts", "15 CHANGES")
pr("""Let's get into it. First, where does one hundred thousand dollars put you compared with everyone else?""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Every number here comes from a named source. Net worth data comes from the Federal Reserve's Survey
of Consumer Finances, the most detailed look at American household wealth, last published for the year
twenty twenty two. Growth examples use simple, stated math, like a seven percent average yearly return.
That's an illustration, not a promise. Markets go down as well as up. This is education, not financial
advice.""",
   "Federal Reserve Bank building columns", "OUR SOURCES")

# ---------------- Big picture ----------------
ch("The big picture")
card("""According to the Federal Reserve's Survey of Consumer Finances, the median net worth of all American
families in twenty twenty two was about one hundred ninety two thousand seven hundred dollars. Median
means half of families had more, and half had less.""",
     {"type": "stat", "label": "median family net worth", "big": "$192,700", "sub": "Federal Reserve, SCF 2022"})
card("""But age changes everything. For families headed by someone under thirty five, the median was about
thirty nine thousand dollars. For thirty five to forty four, about one hundred thirty five thousand. So if
you hit one hundred thousand in your twenties or early thirties, you're well ahead of the typical family
your age.""",
     {"type": "compare", "left": {"label": "Under 35", "big": "$39,040", "sub": "median net worth"},
      "right": {"label": "Age 35 to 44", "big": "$135,300", "sub": "median net worth"},
      "note": "Federal Reserve, Survey of Consumer Finances 2022"})
sc("""And look at the averages. The average net worth for all families was over one million dollars. That's
far above the median, because a small number of very wealthy families pull the average up. That gap is a
reminder. When people talk about what the average American has, ask whether they mean the average or the
median. The median is the better picture of a typical household.""",
   "Suburban houses street aerial", "AVERAGE VS MEDIAN")
sc("""There's another reason this line matters, and it's psychological. Before one hundred thousand,
many people feel like they're not really investors yet. Just people saving a bit. After it, they start
thinking like owners. Owners of businesses, through funds. Owners of a growing machine. That shift in
identity changes behavior. People who see themselves as investors tend to stay invested longer, panic less,
and keep adding money. In many ways, the six figure mark is as much a mindset milestone as a money one.""",
   "Business owner in office", "FROM SAVER TO OWNER")
pr("""Alright. Now the fifteen changes. Number one is the reason Munger said the first hundred thousand is
the hardest.""")

# ---------------- Items ----------------
item(1, "Compounding becomes visible", "growth you can actually see",
"""Change number one. Compounding stops being a theory and becomes something you can see on your
statement.""",
"""At small balances, growth is almost invisible. Seven percent of five thousand dollars is three hundred
fifty dollars a year. Nice, but it doesn't move the needle. Seven percent of one hundred thousand dollars
is seven thousand dollars a year. Same percentage. Twenty times the result. That's why the early years
feel so slow, and why it suddenly feels like things are speeding up.""",
"""Picture it like a snowball. At the top of the hill, it's small and you're doing all the pushing. Around
one hundred thousand dollars, it's heavy enough to start rolling on its own. You still push, but now the
hill helps. Try this: look at your last year of investment statements and separate the money you added from
the growth. Watching that growth line catch up with your contributions is one of the most motivating
things in personal finance.""",
"Snowball rolling in snow", "SAME %, 20X THE RESULT",
"Snow covered hill", "THE SNOWBALL")

card("""Here's the math on screen. One hundred thousand dollars, with nothing added, at a seven percent
average yearly return compounded monthly, becomes roughly two hundred thousand in about ten years. That's
the rule of seventy two in action, which we'll get to in a moment.""",
     {"type": "compare", "left": {"label": "Today", "big": "$100,000", "sub": "nothing added"},
      "right": {"label": "About 10 years", "big": "~$200,000", "sub": "at 7% a year"},
      "note": "Illustration. Returns are not guaranteed."})

item(2, "Your money out-earns your savings", "growth rivals contributions",
"""Change number two. Your money can start earning about as much as you save.""",
"""Say you save five hundred dollars a month. That's six thousand dollars a year. At a seven percent return,
one hundred thousand dollars would earn about seven thousand dollars in a year. In a good year, your money
puts in more than you do. That's a strange and wonderful feeling the first time it happens.""",
"""This is exactly why the first one hundred thousand is so hard. Before it, you are the engine. After it,
you have a second engine. In a bad year, of course, the market can take money away instead, and that's
part of the deal. But over long periods, the second engine tends to get stronger. Try this: write two
numbers at the top of a page. What you saved last year, and what your investments earned. Track both every
year.""",
"Two engines airplane wing", "A SECOND ENGINE",
"Notebook with financial notes", "TRACK BOTH NUMBERS")

item(3, "The rule of 72 gets real", "how fast money doubles",
"""Change number three. The rule of seventy two starts to matter.""",
"""The rule of seventy two is a shortcut. Divide seventy two by your yearly return, and you get roughly how
many years it takes for money to double. At seven percent, that's about ten years. At ten percent, about
seven years. At two percent, thirty six years. It's an estimate, not an exact formula, but it's
surprisingly close.""",
"""When you have five thousand dollars, doubling to ten thousand doesn't feel life changing. When you have
one hundred thousand, doubling to two hundred thousand absolutely does. And the next double after that is
four hundred thousand. That's why patience is the most powerful financial skill. Try this: use the rule of
seventy two on your own savings account rate today. If the answer is a very big number, your money is
probably sitting in the wrong place.""",
"Hourglass sand timer", "72 ÷ RETURN = YEARS",
"Wall clock office", "PATIENCE PAYS")

item(4, "You think in net worth", "not just income",
"""Change number four. You start tracking net worth, not just income.""",
"""Income is what comes in. Net worth is what you keep. Lots of people with big salaries have a small net
worth, because everything that comes in goes right back out. Lots of people with ordinary salaries build
real wealth, because they keep the gap between earning and spending, and invest it. At one hundred
thousand, net worth becomes the number that tells the truth.""",
"""Here's a simple example. Two people each earn eighty thousand dollars a year. One spends seventy eight
thousand. The other spends sixty five thousand and invests the rest. After ten years, their incomes look
the same on paper. Their net worth looks completely different. Try this: once a month, write down what you
own and what you owe. One number. It takes ten minutes, and it changes how you see every purchase.""",
"Office building at dusk", "INCOME VS NET WORTH",
"Spreadsheet on laptop", "ONE NUMBER A MONTH")

item(5, "Fees start to hurt", "1% is not small anymore",
"""Change number five. Fees start to hurt.""",
"""A one percent yearly fee sounds tiny. On one hundred thousand dollars, it's one thousand dollars a year.
Every year. And that thousand dollars would otherwise have kept compounding. Over decades, a one percent
difference in fees can add up to a very large amount of money, because you lose both the fee and all the
growth it would have produced.""",
"""Funds charge something called an expense ratio, a yearly percentage of what you invest. Some broad index
funds charge a small fraction of a percent. Some actively managed funds and some advice arrangements charge
much more. Higher fees aren't always wrong, but you should know exactly what you're paying and what you get
for it. Try this: find the expense ratio of every fund you own. It's listed on the fund's page. Add them up
in dollars, not percent.""",
"Receipt and coins on table", "1% = $1,000 A YEAR",
"Investment fund prospectus document", "KNOW YOUR FEES")

sc("""Let's put a number on that. Imagine one hundred thousand dollars growing for twenty years at seven
percent a year before fees. If the total yearly cost is a small fraction of a percent, you keep almost all of
that growth. If the cost is around one percent, your return effectively drops to around six percent, and the
ending balance can be tens of thousands of dollars lower. Same market. Same years. The only difference is
what you paid along the way. That's why low cost investing became so popular.""",
   "Graph comparing two lines on screen", "SAME MARKET, LESS MONEY")

pr("""Okay, quick check. If you're finding this useful, the next few get more practical, especially number
nine. Let's keep going.""")

item(6, "Allocation beats stock picking", "the mix matters most",
"""Change number six. Your mix of investments matters more than any single pick.""",
"""At this level, the big decision isn't which hot stock to buy. It's how your money is split between broad
categories, like stocks, bonds and cash. That mix, called asset allocation, drives most of how your
portfolio behaves, how much it can grow, and how far it can fall in a bad year.""",
"""Someone in their twenties with a stable job might hold mostly stocks, because they have decades to wait
out the bad years. Someone close to retirement usually holds more bonds and cash, because they can't wait
as long. There's no single right answer, but there is a wrong one: not choosing at all. Try this: open your
accounts and write down your actual mix. Many people are surprised by what they find.""",
"Pie chart financial report", "THE MIX MATTERS",
"Person reviewing investment portfolio", "CHECK YOUR MIX")

item(7, "Drops feel real", "a 20% fall is $20,000",
"""Change number seven. Market drops start to feel real.""",
"""When you had five thousand dollars invested, a twenty percent drop cost you a thousand dollars on paper.
Painful, but survivable. With one hundred thousand dollars, the same drop is twenty thousand dollars. That
can be more than you saved in a whole year. And that's when many people make their worst decision: they
sell after the drop and lock in the loss.""",
"""Markets have always had bad years, and some very bad ones. Historically, broad markets have recovered
over long periods, but there are no guarantees, and recovery can take years. The best protection is
deciding your plan before the drop happens. Try this: write a short note to your future self today. When my
portfolio falls twenty percent, I will. Then finish the sentence. Read it when it happens.""",
"Stock market crash red screen", "-20% = -$20,000",
"Handwritten letter and pen", "A NOTE TO YOUR FUTURE SELF")

sc("""Another way to handle drops is to keep investing through them. When you invest the same amount every
month, you automatically buy more shares when prices are low and fewer when prices are high. It's called
dollar cost averaging. It doesn't guarantee a profit or protect against losses, but it removes the
impossible job of guessing the perfect moment, and it turns a scary drop into a sale on what you were
already buying.""",
   "Shopping sale price tag", "BUYING ON SALE")

item(8, "Taxes matter more", "where you hold it counts",
"""Change number eight. Taxes start to matter a lot more.""",
"""Retirement accounts like a four oh one k or an IRA give you tax advantages, either now or later, in
exchange for keeping the money invested for the long term. At one hundred thousand dollars, the difference
between investing inside those accounts and outside them can be thousands of dollars a year in taxes over
time. The rules and limits change, so always check the current numbers with the IRS.""",
"""A common order many people follow: first, get any employer match on a four oh one k, because that's
extra money for saving. Next, consider an IRA. Then, if you still have money to invest, add more to tax
advantaged accounts or a regular brokerage account. Try this: check whether your employer offers a match,
and whether you're getting all of it. Leaving a match on the table is leaving part of your pay behind.""",
"Tax forms and calculator", "TAXES ADD UP",
"Retirement savings jar", "GET THE FULL MATCH")

item(9, "You need a real emergency fund", "protect the investments",
"""Change number nine. Your emergency fund becomes the guard dog of your investments.""",
"""Here's why. If you have investments but no cash cushion, any emergency forces you to sell, maybe at the
worst possible time, maybe with taxes and penalties. A cash cushion of a few months of expenses means your
investments never have to be touched for a broken car or a lost job. The cushion protects the compounding.""",
"""Think of it as two walls. The outer wall is cash for emergencies. The inner wall is your long term
investments. As long as the outer wall holds, the inner one keeps growing. If you haven't watched my video
on what changes at twenty thousand dollars, that's the outer wall. Try this: check how many months of
expenses you hold in cash right now. If it's less than three, building that up may come before investing
more.""",
"Castle stone walls", "TWO WALLS",
"Savings account on phone", "MONTHS OF CASH")

sc("""Many people use a simple target. Three months of essential expenses if their income is stable, six
months or more if their income is irregular, or if they're the only earner in the house. At one hundred
thousand of net worth, that might mean keeping ten or twenty thousand in cash while the rest is invested.
It can feel like money doing nothing. It isn't. It's insurance for the compounding machine.""",
   "Piggy bank and calculator", "3 TO 6 MONTHS")

item(10, "Home equity isn't cash", "rich on paper, tight in reality",
"""Change number ten. If part of your net worth is your home, you realize equity is not cash.""",
"""Net worth includes home equity, the value of your home minus what you owe on it. That's real wealth.
But you can't buy groceries with it. To use it, you have to sell, borrow against it, or wait. So two people
with the same one hundred thousand dollar net worth can live very different financial lives, depending on
how much is locked in a house.""",
"""Someone with one hundred thousand in home equity and nothing else is house rich and cash poor. Someone
with fifty thousand in equity, thirty thousand invested and twenty thousand in cash has far more options.
Neither is wrong, but the second is more flexible. Try this: split your net worth into three buckets. Cash,
investments, and home. Look at how balanced it really is.""",
"House for sale sign", "EQUITY IS NOT CASH",
"Three glass jars with coins", "THREE BUCKETS")

pr("""We're past the halfway point. The last five are about protecting what you built, and number fifteen
is the trap. Stay with me.""")

item(11, "High-interest debt is an emergency", "no investment beats 20%",
"""Change number eleven. High interest debt becomes an emergency, not a footnote.""",
"""It's hard to find an investment that reliably beats twenty percent a year. But credit card interest
regularly costs that much. So if you have one hundred thousand dollars of net worth and ten thousand dollars
on credit cards, paying off the cards is often one of the best returns available to you. Guaranteed, and
tax free.""",
"""Low interest debt is different. A mortgage at a low fixed rate might not need to be paid off early,
because your money could earn more elsewhere over time. The rule of thumb: the higher the rate, the more
urgent the payoff. Try this: list every debt with its interest rate, from highest to lowest. Attack the top
one first, while making minimum payments on the rest.""",
"Credit cards and bills on table", "20% IS AN EMERGENCY",
"List written on notepad", "HIGHEST RATE FIRST")

item(12, "You become a sales target", "products follow money",
"""Change number twelve. You become a target for salespeople.""",
"""At one hundred thousand dollars, you start getting offers. Complex insurance products. Expensive managed
accounts. Exclusive opportunities. Some are fine. Many come with high fees and long lock ups that mainly
benefit the person selling them. And scammers know this level too. The Federal Reserve's latest survey found
twenty percent of adults experienced financial fraud or a scam in the past year.""",
"""One simple rule protects you from most of it. If you can't explain how a product makes money, and how
the seller makes money, in two sentences, don't buy it. Ask about every fee, ask whether the advisor is a
fiduciary, meaning legally required to act in your interest, and never decide on the same day. Try this:
next time someone pitches you, ask, how do you get paid on this? Their answer tells you a lot.""",
"Business handshake in suit", "HOW DO YOU GET PAID?",
"Phone with scam call warning", "20% HIT BY FRAUD")

item(13, "Paperwork matters", "beneficiaries and a will",
"""Change number thirteen. The boring paperwork starts to matter.""",
"""Retirement accounts and many investment accounts let you name a beneficiary, the person who receives the
money if something happens to you. Those forms often override what's in a will. At one hundred thousand
dollars, getting this wrong can cause real problems for the people you love. It's ten minutes of work that
most people skip.""",
"""Also consider basic protection. If people depend on your income, term life insurance is often a simple
and affordable way to protect them. And a basic will makes your wishes clear. Laws differ by state, so a
local professional can help. Try this: log into every account this week and check the beneficiary. Make
sure it's the right person, and that the information is up to date.""",
"Signing legal documents", "NAME A BENEFICIARY",
"Family walking in park", "PROTECT YOUR PEOPLE")

item(14, "Your options multiply", "career, location, risk",
"""Change number fourteen. Your options multiply.""",
"""With a solid cushion and one hundred thousand dollars of net worth, you can consider moves that were
impossible before. A lower paying job you love, because your money is already working. A career change with
a year of retraining. A move to a cheaper city. A small business. You're not forced to take the first offer
anymore.""",
"""This is the real point of wealth. Not stuff. Choices. The person with options negotiates better, waits for
better deals, and recovers faster from bad luck. Try this: write down one decision you'd make differently if
money weren't the deciding factor. Then ask how far you are from making it possible. Sometimes the answer is
closer than you think.""",
"Open road through countryside", "CHOICES, NOT STUFF",
"Person writing in journal", "WHAT WOULD YOU CHANGE?")

ch("15. The trap")
pr("""And now, number fifteen. The trap that keeps people stuck right here.""")
card("""Change number fifteen. Complacency. Hitting one hundred thousand feels like the finish line. It's not.
It's the starting line.""",
     {"type": "list", "n": 15, "title": "The trap: easing off", "sub": "the starting line, not the finish"}, "CHANGE 15")
sc("""Here's how it happens. You hit the goal, you celebrate, and the automatic contributions quietly get
smaller. A bigger car payment here, a lifestyle upgrade there. The snowball is still rolling, but now
you've stopped pushing. And the years between one hundred thousand and five hundred thousand are exactly the
years where pushing matters most, because every dollar you add has decades to compound.""",
   "Finish line marathon", "THE STARTING LINE")
card("""Look at the difference. One hundred thousand dollars, plus five hundred dollars a month, at a seven
percent average yearly return, for twenty years. That's the kind of path that can turn one hundred thousand
into far more. Compare that with stopping contributions entirely.""",
     {"type": "growth", "monthly": 500, "rate": 0.07, "years": 20})
sc("""On top of that chart, the original one hundred thousand would have grown on its own to roughly four
hundred thousand over twenty years at that same seven percent. Together, that's roughly six hundred sixty
thousand dollars. Again, that's an illustration, not a promise, but it shows why the habit matters more
after one hundred thousand, not less. Try this: when you hit a milestone, raise your automatic contribution
instead of lowering it, even by fifty dollars.""",
   "Mountain summit hiker", "RAISE IT, DON'T STOP")

# ---------------- Same money, different ages ----------------
ch("$100,000 at 25, 40 and 55")
pr("""Here's something most people miss. One hundred thousand dollars is not the same number at every age.
The money is the same. What it can become is completely different. Let me show you three versions of the
same milestone.""")
card("""Let's keep it simple. Imagine you reach one hundred thousand dollars invested, you never add another
dollar, and it earns a seven percent average yearly return until age sixty five. That's an illustration,
not a promise. But look at how much the starting age matters.""",
     {"type": "stat", "label": "$100,000 at 7% until 65", "big": "3 ages", "sub": "same money, very different futures"})
card("""Reach it at twenty five, and you have forty years of growth ahead. At seven percent, one hundred
thousand dollars grows to roughly one point five million dollars by sixty five, without adding a single
dollar. That is the most powerful position on this list, and almost nobody is in it.""",
     {"type": "growth", "start": 100000, "monthly": 0, "rate": 0.07, "years": 40})
sc("""Reach it at forty, and you have twenty five years. The same one hundred thousand grows to roughly five
hundred forty thousand dollars. Still a big number. Not a full retirement on its own for most people, but a
serious foundation, especially if you keep adding to it every month.""",
   "Middle aged man reviewing finances on laptop", "AT 40: ABOUT $540,000")
sc("""Reach it at fifty five, and you have ten years. It grows to roughly one hundred ninety seven
thousand dollars. That's still almost double, and it matters a lot. But at this age, the money you keep
adding, and the years you keep working, matter more than the growth.""",
   "Older couple planning retirement at table", "AT 55: ABOUT $197,000")
pr("""So if you're young, the lesson is urgency. Every year you get there sooner is worth a lot. And if
you're older, the lesson is not regret. It's focus. Let me explain what I mean.""")
sc("""If you're in your twenties or early thirties, your biggest asset isn't your account. It's time.
Cutting costs, raising your income, and automating your investing early all get multiplied for decades.
A raise you invest at twenty eight is worth far more by retirement than the same raise at forty eight.""",
   "Young professional working at desk", "YOUNG: TIME IS THE ASSET")
sc("""If you're in your forties or fifties, your biggest levers are different. Your income is usually
higher, so your savings rate can be much higher. In the United States, people fifty and older can also
make extra catch up contributions to retirement accounts, so check the current limits each year. And
lowering your fees and avoiding big mistakes protects what you've already built.""",
   "Financial advisor meeting with client", "OLDER: SAVINGS RATE AND PROTECTION")
sc("""And whatever your age, compare yourself to the right people. The Federal Reserve's survey found the
median net worth for families under thirty five was about thirty nine thousand dollars, and about one
hundred thirty five thousand for families thirty five to forty four. Hitting one hundred thousand early
puts you well ahead. Hitting it later is still real progress.""",
   "Federal Reserve Board Building Washington", "COMPARE TO YOUR AGE")
pr("""The point isn't to feel good or bad about your age. It's to know which lever is strongest for you
right now, and pull that one first.""")

# ---------------- How long it takes ----------------
ch("How long it takes to reach $100,000")
sc("""So how long does it take to get to one hundred thousand dollars from zero? It depends on two things:
how much you invest each month, and what return you get. Let's look at a few realistic paths, with a seven
percent average yearly return. Remember, real returns go up and down, and some years are negative.""",
   "Calendar on desk", "THE TIMELINE")
card("""At five hundred dollars a month and a seven percent average yearly return, it takes roughly eleven
years to reach one hundred thousand. At one thousand dollars a month, roughly six and a half years. Doubling
your contribution doesn't cut the time in half, but it gets close in the early years.""",
     {"type": "compare", "left": {"label": "$500 a month", "big": "~11 years", "sub": "at 7% a year"},
      "right": {"label": "$1,000 a month", "big": "~6.5 years", "sub": "at 7% a year"},
      "note": "Illustration with monthly compounding. Not a promise."})
sc("""And here's the encouraging part. The last stretch is faster than the first. With five hundred dollars a
month, going from zero to fifty thousand takes about six and a half years. Going from fifty to one hundred
thousand takes less time, because the money you already have is helping. That's compounding again. The
hardest part really is the beginning.""",
   "Running track athletes", "THE LAST STRETCH IS FASTER")
pr("""So if you're early in the journey and it feels slow, that's normal. It's supposed to feel slow at the
start. Keep going.""")

# ---------------- Three paths ----------------
ch("Three paths to $100,000")
pr("""Let's make this concrete with three people. Same goal. Very different paths. See which one sounds like
you.""")
sc("""Path one. Maya, twenty six, earns a modest salary. She can only invest three hundred dollars a month at
first. But she automates it, never stops, and raises it by fifty dollars every time she gets a raise. She
doesn't touch it during bad years. Her early progress feels painfully slow. It takes her years to reach the
first twenty thousand. But because she started young and kept increasing, time does a huge share of her
work. Her advantage isn't income. It's the calendar.""",
   "Young woman working on laptop in cafe", "PATH 1: TIME")
sc("""Path two. Daniel, thirty four, earns more but started late. He had a car loan and credit card debt
through his twenties. First he cleared the cards, which was like earning a guaranteed twenty percent return.
Then he directed those same monthly payments, about nine hundred dollars, into investing. Because the habit
of paying nine hundred a month already existed, he never felt the difference. His advantage is the size of
his monthly contribution.""",
   "Man paying bills at home desk", "PATH 2: CONTRIBUTION")
sc("""Path three. Sara and Luis, a couple in their thirties, both work. They live on one income and invest
most of the other. It's a big sacrifice for a few years, but it builds the cushion and the investments
incredibly fast. They reach one hundred thousand in a few years, then relax their savings rate a bit,
knowing the snowball is rolling. Their advantage is the savings rate.""",
   "Couple walking together in city", "PATH 3: SAVINGS RATE")
sc("""Notice what all three have in common. None of them got lucky with a single stock. None of them waited
for a perfect moment. All three automated the habit, avoided high interest debt, and kept going during bad
years. Time, contribution, savings rate. Pick the lever you can pull hardest, and pull it consistently.""",
   "Three runners on track", "PICK YOUR LEVER")

# ---------------- This week ----------------
ch("What to do this week")
sc("""Here's a simple checklist you can do this week, wherever you are on the path. One. Calculate your net
worth. Everything you own minus everything you owe, on one page. Two. Check that you have at least a few
months of expenses in cash before you invest more. Three. List your debts by interest rate and decide which
one to attack first.""",
   "Weekly planner with checklist", "THIS WEEK: 1 TO 3")
sc("""Four. Check your fees. Find the expense ratio of every fund you own and convert it into dollars per
year. Five. Check your employer match and make sure you're getting all of it. Six. Set up, or raise, one
automatic investment, even if it's small. And seven, check every beneficiary on every account.""",
   "Laptop with online banking dashboard", "THIS WEEK: 4 TO 7")
sc("""That's seven tasks. Most of them take less than half an hour. None of them require a big income. But
together they remove most of the leaks that slow people down on the way to one hundred thousand dollars.
Do them once, then check them again once a year.""",
   "Coffee and notebook on table morning", "SEVEN SIMPLE TASKS")

# ---------------- Mistakes ----------------
ch("Five mistakes on the way")
sc("""Five mistakes to avoid on the way to one hundred thousand. Mistake one. Chasing hot tips. Fast money
stories are exciting, but most people build wealth slowly, with boring, diversified investments. Mistake
two. Stopping during a downturn. Contributions made when prices are low are often the ones that help most
later.""",
   "Newspaper financial headlines", "MISTAKES 1 AND 2")
sc("""Mistake three. Ignoring fees, which we covered. Small percentages, big dollars. Mistake four. Skipping
the emergency fund and investing everything, which turns every surprise into a forced sale. And mistake
five. Comparing yourself with people online. You see their car, not their debt. Run your own race, with your
own numbers.""",
   "Smartphone social media scrolling", "MISTAKES 3, 4 AND 5")

# ---------------- FAQ ----------------
ch("Questions people ask")
pr("""Before the recap, let me answer the questions people ask me most about this milestone.""")
sc("""Question one. Does one hundred thousand dollars count if most of it is in a retirement account? Yes.
Net worth counts everything you own, including retirement accounts. The difference is access. Money in a
retirement account usually has rules and possible penalties for early withdrawals. So it counts for your
net worth, but it's not your emergency fund.""",
   "Retirement account statement", "DOES RETIREMENT COUNT?")
sc("""Question two. Should I pay off my mortgage or invest? It depends on your rate and your peace of mind.
At a high rate, paying it down can make sense. At a low fixed rate, many people prefer to invest the
difference, because over long periods investments have often earned more. There's no single right answer,
but there is a clear order: emergency fund and high interest debt first.""",
   "House keys on table", "MORTGAGE OR INVEST?")
sc("""Question three. Is it too late to start at forty, or fifty? No. You'll have fewer years for compounding,
so the monthly contribution needs to do more of the work. But people in their forties and fifties are often
at their highest earning years, which helps. Starting late is far better than not starting. Question four.
Do I need a financial advisor? Not necessarily at this level. Many people do fine with simple low cost
funds. If you do hire someone, know exactly how they're paid, and prefer someone who acts as a fiduciary.""",
   "Older man reading financial newspaper", "TOO LATE? ADVISOR?")
sc("""And one more, because it comes up every time. Is one hundred thousand dollars enough to retire? On its
own, no, not for most people. Using the four percent rule of thumb many planners mention, one hundred
thousand dollars would support roughly four thousand dollars of withdrawals a year. That's a meaningful
supplement, not a full income. Which is exactly why it's the starting line, not the finish line.""",
   "Retired couple on porch", "ENOUGH TO RETIRE?")
sc("""Question six. What if the market crashes right after I hit one hundred thousand? It probably will drop
at some point. Broad stock markets have fallen twenty percent or more many times in history, and they have
always been scary while it was happening. If your money is invested, you might watch one hundred thousand
become eighty thousand for a while. The people who did best historically were usually the ones who kept
investing through the drop instead of selling at the bottom. Past results don't guarantee future ones, but
panic selling locks in the loss.""",
   "Stock market chart falling on screen", "WHAT IF IT CRASHES?")
sc("""Question seven. Should I tell people I've reached it? Honestly, most people are better off keeping it
quiet. Not because it's shameful, but because money changes how people treat you. Friends may start asking
for loans, family may expect help, and scammers love people they know have savings. Celebrate it with your
partner or someone you trust, and let your habits stay the same.""",
   "Two friends having coffee", "KEEP IT QUIET")
sc("""And question eight. What's the next milestone after this? For most people the next big one is two
hundred fifty thousand dollars, and then half a million. Here's the encouraging part. At a seven percent
return, money roughly doubles about every ten years, by the rule of seventy two. So the second one hundred
thousand usually comes faster than the first, because your money is now doing part of the work for you.""",
   "Mountain climber reaching summit", "THE NEXT MILESTONE")
pr("""If you have a question I didn't answer here, leave it in the comments. I read them, and the best ones
become future videos. And if you're still far from one hundred thousand, don't let that number scare you.
Every person who reached it started at zero, with a first deposit that felt too small to matter. It did
matter. It was the start of the habit, and the habit is what gets you there. So set up the transfer today, even if it's small, and let time do
the heavy lifting for you.""")
card("""Here's a quick reminder of how small that first step can be. Two hundred dollars a month, for
twenty years, at a seven percent average yearly return, grows to roughly one hundred four thousand
dollars. You'd put in forty eight thousand. Small, boring, and automatic beats big and occasional.""",
     {"type": "growth", "monthly": 200, "rate": 0.07, "years": 20})

# ---------------- Recap ----------------
ch("Recap: all 15 changes")
sc("""Quick recap. One, compounding becomes visible. Two, your money can out earn your savings. Three, the
rule of seventy two gets real. Four, you think in net worth. Five, fees start to hurt. Six, allocation beats
stock picking. Seven, drops feel real. Eight, taxes matter more.""",
   "Checklist on clipboard", "THE RECAP")
sc("""Nine, your emergency fund guards your investments. Ten, home equity isn't cash. Eleven, high interest
debt becomes an emergency. Twelve, you become a sales target. Thirteen, the paperwork matters. Fourteen, your
options multiply. And fifteen, the trap of easing off right when the snowball starts rolling.""",
   "Notebook with written goals", "15 CHANGES")

# ---------------- Close ----------------
ch("What to do next")
pr("""If you want the full step by step plan, from zero to one hundred thousand and beyond, it's in my
playbook. The link is in the description. And if you missed it, watch my video on what changes at twenty
thousand dollars in the bank. That's the foundation for everything we talked about today. I'm Ryan Rover.
See you in the next one.""")

save("video02", "What Changes When You Hit $100,000 Net Worth", [
    "Federal Reserve, Survey of Consumer Finances 2022 (median net worth $192,700; by age: under 35 $39,040, 35-44 $135,300)",
    "Federal Reserve, Economic Well-Being of U.S. Households in 2025 (20% experienced fraud or scams)",
    "IRS, retirement plan and IRA rules (check current limits)",
    "Rule of 72 and compound growth: stated illustrative math at 7% average yearly return",
], "what changes at $100k net worth")
