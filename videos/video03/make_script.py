import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save


def level(n, name, sub, card_text, what, numbers, trap, move, q1, c1, q2, c2, q3, c3, q4, c4):
    ch(f"Level {n}. {name}")
    card(card_text, {"type": "list", "n": n, "title": name, "sub": sub}, f"LEVEL {n}")
    sc(what, q1, c1)
    sc(numbers, q2, c2)
    sc(trap, q3, c3)
    sc(move, q4, c4)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Every person watching this video is on one of seven money levels. Not because of
how much they earn, but because of what their money is doing right now. Some people are fighting debt every
month. Some people never have to work again. And most people are stuck somewhere in the middle without
knowing which level they're on, or what it takes to move up.""")
card("""Seven levels. From owing more than you own, all the way to money that pays for your whole life.
By the end of this video you'll know exactly where you are, and the one move that gets you to the next level.""",
     {"type": "stat", "label": "money levels", "big": "7", "sub": "from debt to financial independence"})
sc("""Here's the surprising part. Your level has very little to do with your salary. There are doctors on
level one, buried in debt, and there are mechanics and teachers on level six. Income helps, of course. But
the level you're on is decided by what happens to your money after it arrives.""",
   "Doctor in hospital corridor", "IT'S NOT YOUR SALARY")
sc("""And each level has its own trap. A mistake that feels completely normal at that level, but keeps people
stuck there for years. We'll look at all seven traps, with real numbers from the Federal Reserve and other
named sources, so you can skip the mistakes most people make.""",
   "Maze hedge garden", "EVERY LEVEL HAS A TRAP")
pr("""So let's find out where you are. Grab a piece of paper, or just keep count in your head. Let's start
at the bottom.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Quick note on the data. Net worth numbers come from the Federal Reserve's Survey of Consumer Finances,
the most detailed study of American household wealth, published every three years. The latest full survey
covers twenty twenty two. We also use the Federal Reserve's survey on household well being, Bankrate's savings
research, and the New York Fed's report on household debt.""",
   "Federal Reserve Bank of New York building", "OUR SOURCES")
sc("""When we show growth over time, we use a seven percent average yearly return as an illustration. That
is not a promise. Real markets go up and down, sometimes a lot. This video is education, not financial
advice. Use it to understand the map, then make decisions that fit your own life.""",
   "Calculator and pen on financial papers", "EDUCATION, NOT ADVICE")

# ---------------- Big picture ----------------
ch("The big picture")
card("""First, the big picture. According to the Federal Reserve, the median American family had a net worth
of about one hundred ninety two thousand dollars in twenty twenty two. Median means half had more, half had
less. But the average was over one million dollars, pulled up by the very top.""",
     {"type": "compare", "left": {"label": "Median family", "big": "$192,700", "sub": "half have more, half less"},
      "right": {"label": "Average family", "big": "$1.06M", "sub": "pulled up by the top"},
      "note": "Federal Reserve, Survey of Consumer Finances 2022"})
sc("""That gap tells you something important. The average is misleading. Most families are much closer to the
median, and a big share of that median is home equity, money you can't easily spend. So if your number feels
small, you are probably more normal than you think.""",
   "Suburban houses street United States", "THE AVERAGE LIES")
card("""Age matters a lot too. The same survey found the median net worth for families under thirty five was
about thirty nine thousand dollars. For thirty five to forty four, about one hundred thirty five thousand.
For forty five to fifty four, about two hundred forty seven thousand.""",
     {"type": "compare", "left": {"label": "Under 35", "big": "$39,040", "sub": "median net worth"},
      "right": {"label": "Age 45 to 54", "big": "$246,700", "sub": "median net worth"},
      "note": "Federal Reserve, Survey of Consumer Finances 2022"})
pr("""Keep those numbers in mind, because they'll help you see where you really stand. Now, level one.""")

# ---------------- Levels ----------------
level(1, "Underwater", "you owe more than you own",
      """Level one. Underwater. You owe more than you own. Your net worth is below zero. If you sold everything
you have today, you still couldn't pay off what you owe.""",
      """Level one usually looks like this. Credit card balances that never really go down. A car loan bigger
than what the car is worth. Student loans. Maybe a buy now pay later plan or two. Every month, a big part of
the paycheck is already spoken for before it even arrives.""",
      """And it's more common than people admit. The New York Fed reports that Americans owe more than eighteen
trillion dollars in household debt, including well over one trillion on credit cards alone. Credit card
interest rates have been above twenty percent, which means a balance can grow faster than most people can pay
it down.""",
      """The trap at level one is paying the minimum and feeling like you're making progress. On a card charging
over twenty percent, the minimum payment mostly covers interest. You can pay for years and still owe almost the
same amount. It feels responsible. It's actually treading water.""",
      """The move to level two is simple, not easy. List every debt with its interest rate. Stop adding new debt.
Then throw every extra dollar at the highest rate first, while paying the minimum on the rest. When one is gone,
roll that payment into the next one. That's the fastest way up.""",
      "Credit card bills on table", "DEBT EVERYWHERE",
      "Federal Reserve Bank of New York building", "$18 TRILLION OWED",
      "Hamster wheel", "THE MINIMUM PAYMENT TRAP",
      "Person writing list notebook", "HIGHEST RATE FIRST")

level(2, "Paycheck to paycheck", "zero at the end of every month",
      """Level two. Paycheck to paycheck. You're not sinking anymore, but you're not moving either. Your net
worth is around zero, and your bank account hits nearly zero right before every payday.""",
      """Level two is where a huge number of Americans live, including people with good incomes. The money comes
in, and somehow it all goes out. Rent, car, groceries, subscriptions, a dinner out. Nothing crazy. But nothing
left over, either.""",
      """The Federal Reserve found that sixty three percent of adults would cover a surprise four hundred dollar
expense with cash. That means more than a third would not. And Bankrate found that about one in four Americans
has no emergency savings at all. At level two, one flat tire can push you right back to level one.""",
      """The trap at level two is lifestyle creep. Every raise disappears. A bigger apartment, a nicer car, more
eating out. Each upgrade feels earned, and it is. But if your spending rises as fast as your income, you stay on
level two forever, just with nicer things.""",
      """The move to level three is to pay yourself first. Set up an automatic transfer of even fifty dollars on
payday, into a separate savings account, before you can spend it. Then, the next time you get a raise, send at
least half of it to that account. Your lifestyle still improves, and your savings finally start.""",
      "Empty wallet", "NOTHING LEFT OVER",
      "Car with flat tire on road", "ONE FLAT TIRE",
      "Luxury car dealership", "LIFESTYLE CREEP",
      "Piggy bank coins", "PAY YOURSELF FIRST")

level(3, "The starter cushion", "one surprise won't break you",
      """Level three. The starter cushion. You have somewhere between one thousand and ten thousand dollars saved.
A surprise bill is annoying, but it's not a crisis anymore.""",
      """Level three feels different. The car repair, the vet bill, the urgent flight home, you can pay them. You
don't have to borrow, and you don't have to ask anyone for help. That alone takes a weight off your shoulders
that most people don't even realize they're carrying.""",
      """Here's how close this level really is. Saving five hundred dollars a month gets you to ten thousand dollars
in twenty months. Two hundred fifty a month gets you there in under three and a half years. It isn't magic. It's
just a transfer that happens every single month without you thinking about it.""",
      """The trap at level three is raiding the cushion for things that aren't emergencies. A sale, a vacation, a
new phone. Then the real emergency arrives and the money's gone. The fix is to keep it in a separate account,
ideally at a different bank, so spending it takes a deliberate decision.""",
      """The move to level four is to grow the cushion to three to six months of essential costs, and keep it in a
high yield savings account. Then, once it's full, start investing a regular amount every month, even a small one.
That's the moment your money starts working, not just sitting.""",
      "Car repair garage mechanic", "NOT A CRISIS ANYMORE",
      "Calendar planning", "20 MONTHS TO $10,000",
      "Shopping bags mall", "DON'T RAID THE CUSHION",
      "Bank building United States", "SEPARATE ACCOUNT")

pr("""Quick pause. If you've already found your level, I'd love to know which one. Tell me in the comments. And if
this is helping you, subscribe to the channel. It's free, and it helps me keep making these videos for you.""")

level(4, "Stable", "a real safety net and money invested",
      """Level four. Stable. Your emergency fund is full, your high interest debt is gone, and you're investing
every month. Your net worth is somewhere between ten thousand and one hundred thousand dollars.""",
      """This is where life gets calmer. A layoff would hurt, but you'd have months to recover. You're not checking
your balance before every purchase. And for the first time, you're putting money into investments like broad
index funds or a retirement account, on purpose, every single month.""",
      """At level four, your own contributions do almost all the work. If you invest three hundred dollars a month
for ten years, at a seven percent average yearly return, you'd have roughly fifty two thousand dollars. You put
in thirty six thousand. The rest is growth, and it's only getting started.""",
      """The trap at level four is getting impatient. The growth feels slow, so people chase faster money. Hot
stocks, crypto tips, a friend's business idea. Some of it might work. Most of it costs people years. At this
level, boring and consistent beats exciting almost every time.""",
      """The move to level five is to raise your savings rate. Not just your income, your rate. Try going from ten
percent of your income to fifteen, then twenty. Use every raise, every bonus, and every paid off loan to push it
higher. That's what gets you to one hundred thousand.""",
      "Family relaxing at home", "LIFE GETS CALMER",
      "Stock market chart on screen", "YOUR MONEY STARTS WORKING",
      "Slot machines casino", "DON'T CHASE FAST MONEY",
      "Graph trending upward", "RAISE YOUR SAVINGS RATE")

level(5, "Momentum", "your money starts doing real work",
      """Level five. Momentum. Your net worth is between one hundred thousand and about five hundred thousand
dollars. This is where your money starts to pull its own weight.""",
      """Charlie Munger, Warren Buffett's longtime partner, famously said the first one hundred thousand dollars is
the hardest. Here's why. At seven percent, one hundred thousand dollars can grow by around seven thousand dollars in
a single year, without you adding anything. That's a real raise you didn't have to ask for.""",
      """And it compounds. One hundred thousand dollars plus one thousand dollars a month, at a seven percent average
yearly return, reaches one million dollars in about twenty one years. That isn't a promise, markets vary, but it
shows how level five turns into level six with patience.""",
      """The trap at level five is fees and lifestyle. A one percent yearly fee doesn't sound like much, but on a
growing portfolio it can cost hundreds of thousands of dollars over a lifetime. And this is the level where people
upgrade their house and car, and lock in costs that slow everything down.""",
      """The move to level six is to protect the machine. Keep your fees low, keep investing through market drops,
and keep your big fixed costs under control. Most people who reach level six didn't do anything brilliant. They just
didn't interrupt the process.""",
      "Charlie Munger", "THE HARDEST $100,000",
      "New York Stock Exchange trading floor", "COMPOUNDING KICKS IN",
      "Mansion house exterior", "FEES AND BIG UPGRADES",
      "Bank vault door", "PROTECT THE MACHINE")

level(6, "Millionaire", "a seven figure net worth",
      """Level six. Millionaire. Your net worth has passed one million dollars. It sounds like the finish line.
For most people who get here, it isn't.""",
      """UBS's Global Wealth Report estimates there are more than twenty million millionaires in the United States.
Most of them are not celebrities. They're often people in their fifties and sixties who owned a home for decades,
saved in retirement accounts, and never stopped. Many of them drive ordinary cars.""",
      """Here's the reality check. One million dollars sounds rich, but if half of it is your home, the money you
could actually live on is much smaller. Using the four percent rule of thumb, five hundred thousand dollars in
investments supports about twenty thousand dollars a year. Nice, but not freedom yet.""",
      """The trap at level six is feeling rich and acting like it. Bigger house, second home, expensive hobbies. At
this level, a few large decisions can easily erase ten years of progress. The people who stay here keep their
spending tied to what their investments can really support.""",
      """The move to level seven is to stop measuring net worth and start measuring one thing: how many years of
your life your investments can pay for. That changes every decision. Suddenly a cheaper house isn't a sacrifice.
It's years of your freedom bought back.""",
      "Suburban houses street United States", "QUIET MILLIONAIRES",
      "Retired couple on porch", "$1 MILLION IS NOT FREEDOM YET",
      "Yacht marina", "DON'T ACT RICH",
      "Hourglass", "COUNT YEARS, NOT DOLLARS")

level(7, "Financially independent", "work becomes optional",
      """Level seven. Financially independent. Your investments can pay for your life, indefinitely. Work becomes
a choice, not a requirement.""",
      """A common rule of thumb comes from research by financial planner William Bengen in the nineteen nineties:
withdrawing about four percent in the first year, then adjusting for inflation, has historically lasted at least
thirty years in most periods. Flip that around, and you need about twenty five times your yearly spending.""",
      """So the number is personal. If you spend forty thousand dollars a year, you need about one million dollars
invested. If you spend eighty thousand, you need about two million. That's why spending less is so powerful. It
lowers the finish line and gets you there faster at the same time.""",
      """The trap at level seven is assuming the rule is a guarantee. It isn't. A bad market right at the start of
retirement, high inflation, or big health costs can change the math. Most people at this level keep some
flexibility, like spending a little less in bad years, or earning a bit on the side.""",
      """And here's what people at level seven say surprised them most. It wasn't the money. It was the time. Time
with family, time to build something they care about, time to say no. That's what all seven levels are really
about. Not getting rich. Getting free.""",
      "William Bengen", "THE 4% RULE",
      "Calculator with financial charts", "25 TIMES YOUR SPENDING",
      "Stock market crash newspaper", "NOT A GUARANTEE",
      "Family walking on beach", "IT'S ABOUT TIME")

# ---------------- How long ----------------
ch("How long each level takes")
pr("""So how long does it actually take to climb? Let me show you the math, because it's more encouraging than you
think.""")
card("""Here's one path. Five hundred dollars a month, invested for thirty years at a seven percent average yearly
return, grows to roughly six hundred ten thousand dollars. You'd put in one hundred eighty thousand. More than two
thirds of the final number is growth.""",
     {"type": "growth", "monthly": 500, "rate": 0.07, "years": 30})
card("""Now double the effort. One thousand dollars a month for twenty five years, at the same seven percent
illustration, grows to roughly eight hundred ten thousand dollars. You'd put in three hundred thousand. Higher
contributions shorten the climb by years.""",
     {"type": "growth", "monthly": 1000, "rate": 0.07, "years": 25})
sc("""The pattern is always the same. The first levels are about behavior: stopping debt, saving on autopilot,
building a cushion. The middle levels are about consistency: investing every month and not interrupting it. And
the top levels are about protection: low fees, controlled spending, and patience.""",
   "Staircase steps", "BEHAVIOR, CONSISTENCY, PROTECTION")
sc("""And here's the part people forget. You don't have to climb all seven levels to change your life. Going from
level one to level three, from debt to a real cushion, is the biggest jump in peace of mind most people will ever
feel. Start there.""",
   "Sunrise over mountains", "START WITH THE NEXT LEVEL")

# ---------------- Mistakes ----------------
ch("Five mistakes that drop you a level")
pr("""Climbing is one thing. Not falling back down is another. Here are five mistakes that knock people down a
level, sometimes two.""")
sc("""Mistake one. No emergency fund once you start investing. When the surprise comes, people sell investments at
a bad time or go back to credit cards. Mistake two. A car payment that's too big. Cars lose value fast, and a large
loan can drag you from level four back to level two.""",
   "Car dealership lot", "MISTAKES ONE AND TWO")
sc("""Mistake three. Panic selling in a market drop. Broad markets have fallen twenty percent or more many times,
and recovered, though past results don't guarantee the future. Selling at the bottom turns a temporary drop into a
permanent loss. Mistake four. Co-signing loans for friends or family. If they don't pay, you do.""",
   "Stock market chart falling on screen", "MISTAKES THREE AND FOUR")
sc("""And mistake five. Falling for a scam or a too good to be true investment. The Federal Reserve found that about
one in five adults experienced fraud or a scam in a single year. The higher your level, the more of a target you
become. If someone promises guaranteed high returns, walk away.""",
   "Computer hacker keyboard", "MISTAKE FIVE: SCAMS")

# ---------------- Questions ----------------
ch("Questions people ask")
pr("""Before the recap, let me answer the questions I get the most about these levels.""")
sc("""Question one. Does my home count? For net worth, yes. Your home's value minus your mortgage is part of it.
But for these levels, I'd look mostly at money you can actually use: savings and investments. A big house with no
savings is still level two in daily life.""",
   "House with for sale sign", "DOES MY HOME COUNT?")
sc("""Question two. Can I skip a level? Not really. People try to jump from level two straight to investing big,
without a cushion. Then the first emergency sends them back down. Each level builds the floor for the next one.
Question three. Is it too late at fifty? No. Your monthly savings need to do more of the work, but people in their
fifties often earn the most they ever will.""",
   "Older man reading financial newspaper", "SKIP A LEVEL? TOO LATE?")
sc("""Question four. What if I have a low income? Then the early levels are about protecting what you have. Avoid
high interest debt, build even a small cushion, and look for ways to raise your income, like new skills or a better
paying job. Small amounts still count, because the habit is what moves you up.""",
   "Person studying laptop at night", "LOW INCOME?")

# ---------------- Recap ----------------
ch("Recap: the 7 levels")
sc("""Let's recap. Level one, underwater, you owe more than you own. Level two, paycheck to paycheck. Level three,
the starter cushion. Level four, stable, with a full emergency fund and regular investing.""",
   "Staircase steps", "LEVELS 1 TO 4")
sc("""Level five, momentum, where your money does real work. Level six, millionaire, which isn't the finish line.
And level seven, financially independent, when your investments can pay for your life and work becomes optional.""",
   "Mountain climber reaching summit", "LEVELS 5 TO 7")

# ---------------- Close ----------------
ch("What to do next")
pr("""Now pick your level and do just one thing: the move to the next one. That's it. If you want the full plan, step
by step, it's in my playbook. The link is in the description. And if you're on level three or four, watch my video on
what changes at one hundred thousand dollars. I'm Ryan Rover. See you in the next one.""")

save("video03", "The 7 Money Levels: Where Are You in 2027?", [
    "Federal Reserve, Survey of Consumer Finances 2022 (median net worth $192,700, mean $1,063,700; by age: under 35 $39,040, 35-44 $135,300, 45-54 $246,700)",
    "Federal Reserve, Economic Well-Being of U.S. Households in 2025 (63% would cover a $400 expense with cash; about 1 in 5 experienced fraud or scams)",
    "Bankrate, Emergency Savings Report (about 1 in 4 Americans have no emergency savings)",
    "Federal Reserve Bank of New York, Quarterly Report on Household Debt and Credit (total household debt above $18 trillion)",
    "Federal Reserve G.19 Consumer Credit (credit card interest rates above 20%)",
    "UBS Global Wealth Report 2025 (more than 20 million millionaires in the United States)",
    "William P. Bengen, Determining Withdrawal Rates Using Historical Data, Journal of Financial Planning (1994)",
    "Compound growth: stated illustrative math at 7% average yearly return, compounded monthly",
], "the 7 money levels")
