import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short


def step(n, title, sub, card_text, why, how, example, q1, c1, q2, c2, q3, c3):
    ch(f"Step {n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"STEP {n}")
    sc(why, q1, c1)
    sc(how, q2, c2)
    sc(example, q3, c3)

# ---------------- Intro ----------------
ch("Intro")
short("Getting from zero to one hundred thousand dollars has an order. Most people do it backwards.")
pr("""Hi, I'm Ryan Rover. Getting from zero to one hundred thousand dollars is the hardest climb in personal
finance. Charlie Munger famously said the first hundred thousand is the hardest. But here's what almost nobody
tells you. There's an order to it. Do the steps in the right order, and every step makes the next one easier.
Do them in the wrong order, and you can work hard for years and barely move.""")
card("""From zero to one hundred thousand dollars. Twelve steps, in order. Each one builds the floor for the
next.""",
     {"type": "stat", "label": "the first milestone", "big": "$0 → $100K", "sub": "12 steps, in the right order"})
sc("""Most people do it backwards. They start investing before they have any cash for emergencies, so the first
surprise bill sends them to a credit card. Or they pay off a low interest loan early while their high interest card
grows. Or they skip free money from their employer because they think they can't afford to save. Each mistake
alone costs a little. Together, they cost years.""",
   "Maze hedge garden", "MOST PEOPLE DO IT BACKWARDS")
sc("""Today we'll go step by step, in order, from the very first dollar to one hundred thousand. And we'll look at
the whole journey from three angles. First the numbers: how long it really takes. Then the psychology: why most
people quit around the same point. And then the playbook: three real paths for three different incomes.""",
   "Staircase steps", "12 STEPS, 3 ANGLES")
pr("""If you're starting from zero, or even below zero, this video is for you. Let's go.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our numbers come from named sources. Household savings data comes from the Federal Reserve's survey on the
economic well being of U.S. households. Net worth data comes from the Federal Reserve's Survey of Consumer
Finances. Credit card rates come from the Federal Reserve's consumer credit report. Retirement account rules come
from the IRS, and the limits change every year, so always check the current numbers.""",
   "Federal Reserve Bank building columns", "OUR SOURCES")
sc("""Growth examples use a seven percent average yearly return, compounded monthly, as an illustration. That's not
a promise. Markets go up and down, sometimes a lot. This is education, not financial advice. Use it as a map, and
adjust it to your own life.""",
   "Calculator and pen on financial papers", "EDUCATION, NOT ADVICE")

# ---------------- Angle 1: numbers ----------------
ch("Angle 1: The numbers")
pr("""Angle one. The numbers. Before the steps, let's see exactly how long the climb takes, because once you see
the math, it stops feeling impossible.""")
card("""At a seven percent illustration, investing five hundred dollars a month gets you to one hundred thousand
dollars in about eleven years. One thousand a month gets you there in under seven.""",
     {"type": "compare", "left": {"label": "$500 a month", "big": "~11 years", "sub": "to $100,000"},
      "right": {"label": "$1,000 a month", "big": "~6.7 years", "sub": "to $100,000"},
      "note": "Illustration at 7% a year, compounded monthly. Not guaranteed."})
sc("""Notice something. Doubling your monthly amount doesn't cut the time in half. It cuts it from about eleven years
to under seven. That's because at the start, almost all of the balance is your own money. Growth only becomes big
later. At five hundred a month, you'd put in about sixty six thousand of your own money, and growth adds the rest.""",
   "Calculator with financial charts", "YOUR MONEY DOES MOST OF IT")
card("""Flip it around. If you want one hundred thousand dollars in ten years, you'd need to invest about five
hundred eighty dollars a month. In seven years, about nine hundred twenty five. In five years, about fourteen
hundred.""",
     {"type": "compare", "left": {"label": "In 10 years", "big": "~$580/mo", "sub": "to reach $100,000"},
      "right": {"label": "In 5 years", "big": "~$1,400/mo", "sub": "to reach $100,000"},
      "note": "Illustration at 7% a year, compounded monthly. Not guaranteed."})
sc("""Those numbers might look big. But remember, they don't have to come only from cutting costs. Employer
matches count. Raises count. A paid off car loan that you redirect counts. Most people who reach one hundred
thousand do it with a mix of all of those, not with one heroic budget.""",
   "Office workers meeting", "EVERYTHING COUNTS")
sc("""Now here's where most people actually start. The Federal Reserve found that sixty three percent of adults
would cover a surprise four hundred dollar expense with cash or its equivalent. That means more than a third
couldn't. And credit card interest rates, according to the Federal Reserve, have been above twenty percent. So for
many people, step zero is simply stopping the bleeding.""",
   "Credit card bills on table", "WHERE MOST PEOPLE START")
sc("""One more number before the steps: the cost of waiting. If you put off starting for just three years, you don't
arrive three years later at the same place. You lose the three years of growth at the very end, when the balance is
largest. That's why the best time to start this road is always now, even with a small amount. Twenty five dollars a
month started today often beats two hundred dollars a month started someday.""",
   "Wall clock office", "THE COST OF WAITING")
sc("""And the last number is the one that makes all the others work: consistency. A plan you follow for ten years at five
hundred dollars a month beats a plan for one thousand a month that you abandon after eighteen months. When you choose
your monthly amount, choose one you can keep through a bad month, not just a good one. You can always raise it later.""",
   "Calendar planning", "CONSISTENCY BEATS SIZE")
pr("""Okay. Now the twelve steps, in order. Step one takes about one evening, and it changes everything after it.""")

# ---------------- Steps ----------------
step(1, "Know your numbers", "net worth and cash flow",
"""Step one. Know your numbers. You can't plan a trip without knowing where you're starting.""",
"""Two numbers matter. Your net worth, which is everything you own minus everything you owe. And your monthly cash
flow, which is what comes in minus what goes out. Most people have never written either of them down. They have a
feeling about their money, and feelings are usually wrong, in both directions.""",
"""Here's how. Open every account: checking, savings, retirement, credit cards, loans. Write down each balance.
Add up what you own, subtract what you owe. Then look at the last three months of bank statements and calculate
your average income and spending. It takes one evening. It's not fun. But it's the foundation of everything else.""",
"""Say you discover your net worth is minus eight thousand dollars, and you have two hundred dollars left at the end
of a typical month. That's not bad news. That's a starting line. You now know exactly how much fuel you have, two
hundred dollars a month, and exactly how far you have to go. People who track their numbers tend to make better
decisions, simply because they can see them.""",
"Spreadsheet on laptop", "TWO NUMBERS",
"Person writing list notebook", "ONE EVENING",
"Starting line track", "A STARTING LINE")

step(2, "A starter emergency fund", "one thousand to two thousand dollars",
"""Step two. Build a small emergency fund, around one thousand to two thousand dollars, before anything else.""",
"""Why first? Because without it, every surprise becomes new debt. The flat tire, the dentist, the broken phone. If
you put that on a card at over twenty percent, you're going backwards. A small cushion breaks that cycle. It's not
meant to cover a job loss yet. It's meant to cover the normal chaos of life.""",
"""Open a separate savings account, ideally at a different bank, so it's not sitting next to your spending money.
Set an automatic transfer on payday. Sell a few things you don't use. Pick up a few extra shifts. The goal is speed.
Most people can build this in one to four months if they focus.""",
"""Here's what changes. The next time the car needs a three hundred dollar repair, you pay it from the cushion, and
then refill it. No new debt. No panic. It sounds small, but for many people this is the first time money feels like
it's working for them instead of against them.""",
"Car with flat tire on road", "LIFE IS CHAOS",
"Piggy bank coins", "SPEED MATTERS",
"Car repair garage mechanic", "NO NEW DEBT")

step(3, "Get the full employer match", "free money comes before debt payoff",
"""Step three. If your employer matches retirement contributions, contribute enough to get the full match.""",
"""Why this comes before paying off debt: a match is often a fifty or one hundred percent instant return on your
money. A common formula is fifty cents for every dollar you put in, up to six percent of your salary. No investment
and no debt payoff beats an instant fifty percent return. Skipping it is turning down part of your pay.""",
"""Look up your plan's matching rule in your benefits portal, or ask HR. Then set your contribution to at least the
level that gets every matching dollar. If money is tight, start at whatever you can, and raise it by one percent
every few months until you reach the full match.""",
"""Say you earn fifty thousand dollars and your employer matches fifty percent up to six percent. You put in three
thousand a year. Your employer adds fifteen hundred. That's fifteen hundred dollars a year you'd lose by not
participating, and over thirty years, with growth, that alone could add up to far more than you'd expect.""",
"Office building at dusk", "FREE MONEY",
"Office workers meeting", "ASK HR TODAY",
"Graph trending upward", "$1,500 A YEAR FREE")

short("Paying the minimum on a credit card is treading water. Here's how to escape.")
step(4, "Kill high interest debt", "anything above about eight percent",
"""Step four. Pay off high interest debt, especially credit cards.""",
"""Credit card balances often charge over twenty percent a year. Paying off a card at twenty two percent is like
earning a guaranteed twenty two percent return. Nothing in the investing world reliably beats that. So until high
interest debt is gone, it's the best investment you have.""",
"""There are two popular methods. The avalanche: pay minimums on everything, and throw every extra dollar at the
highest interest rate first. It saves the most money. The snowball: pay off the smallest balance first for quick
wins. It can keep you motivated. Either works far better than paying minimums on everything. Pick the one you'll
actually stick to.""",
"""Say you have three cards, with balances of two thousand, four thousand and six thousand dollars. With the avalanche
method, you'd target whichever card has the highest rate, while paying minimums on the others. When it's gone, that
whole payment rolls into the next one. Each payoff speeds up the next. People often describe the last card as the
fastest one, because by then they're throwing everything at it.""",
"Credit card close up", "OVER 20% A YEAR",
"Snowball rolling in snow", "AVALANCHE OR SNOWBALL",
"Scissors cutting credit card", "ROLL IT FORWARD")

step(5, "A full emergency fund", "three to six months of essentials",
"""Step five. Grow your emergency fund to three to six months of essential expenses.""",
"""Your starter fund protects you from small surprises. This one protects you from big ones: a job loss, a medical
problem, a family emergency. With three to six months of essentials saved, a layoff becomes a hard time instead of a
financial disaster. And it means you'll never have to sell investments at a bad time to pay rent.""",
"""Add up your essential monthly costs: housing, food, utilities, insurance, transport, minimum payments. Multiply by
three to six. If your income is very stable, three might be enough. If you're self employed or your industry is
unpredictable, aim closer to six. Keep it in a high yield savings account that's FDIC insured.""",
"""Say your essentials are three thousand dollars a month. Your target is somewhere between nine and eighteen
thousand dollars. That sounds like a lot. But if you just finished paying off debt, you already have a monthly
payment habit. Keep making the same payment, just to yourself. Many people fill this fund faster than they paid off
their debt.""",
"Family relaxing at home", "BIG SURPRISES",
"Bank building United States", "3 TO 6 MONTHS",
"Online banking smartphone app", "PAY YOURSELF")

step(6, "Automate and raise your rate", "aim for 15 to 20 percent",
"""Step six. Automate your saving and push your savings rate toward fifteen to twenty percent.""",
"""Willpower runs out. Automation doesn't. When money moves to savings and investments automatically on payday,
before you see it, you adjust your spending to what's left. That's the single most reliable way people build wealth
on ordinary incomes. And your savings rate, the share of your income you keep, decides how fast you climb.""",
"""Set up automatic contributions to your retirement account through payroll, and automatic transfers to your other
accounts on payday. Then use a simple rule: every time you get a raise, send at least half of it to savings. Your
lifestyle still improves, but your rate climbs every year without it ever feeling like a sacrifice.""",
"""Say you earn sixty thousand dollars and save five percent. That's three thousand a year. Each year you get a three
percent raise and send half of it to savings. After about seven years, without ever cutting your spending, you're
saving well over ten percent. That's the quiet power of automating your raises.""",
"Clock gears mechanism", "AUTOMATION WINS",
"Calendar planning", "HALF OF EVERY RAISE",
"Graph trending upward", "THE RATE CLIMBS")

pr("""Quick pause. If you're finding this step by step useful, subscribe to the channel. I'm making a full series on
every stage, from zero to one million, and subscribing is the best way not to miss the next step. Now, step seven.""")

step(7, "Open an IRA", "a retirement account of your own",
"""Step seven. Open an individual retirement account, an IRA, alongside your workplace plan.""",
"""An IRA is a retirement account you open yourself, at a brokerage. There are two main types. A traditional IRA may
give you a tax deduction now, and you pay tax later. A Roth IRA uses money you've already paid tax on, and qualified
withdrawals in retirement are tax free. Both let your investments grow without yearly taxes on gains.""",
"""Which one? Many people early in their careers, in lower tax brackets, prefer the Roth, because they pay tax now at a
lower rate. Income limits apply to Roth contributions, and the yearly limits change, so check the current IRS rules.
Open the account, set up an automatic monthly contribution, and, this is important, actually choose an investment
inside it. Money sitting as cash in an IRA doesn't grow much.""",
"""That last point catches a lot of people. They open an IRA, transfer money in, and never pick an investment. Years
later, they discover it's been sitting in cash, earning almost nothing. Try this: if you already have an IRA, log in
today and check what it's actually invested in.""",
"Paperwork documents desk", "TRADITIONAL OR ROTH",
"Investment fund prospectus document", "CHOOSE AN INVESTMENT",
"Laptop online banking", "CHECK IT TODAY")

step(8, "Invest simply and cheaply", "broad, low cost index funds",
"""Step eight. Invest simply. Broad, low cost index funds.""",
"""An index fund buys a whole market, like the five hundred largest U.S. companies, or the entire U.S. stock market,
instead of trying to pick winners. Research, like S and P's long running SPIVA reports, has repeatedly found that most
actively managed funds trail their benchmark index over long periods, especially after fees.""",
"""A simple approach many investors use is one or two broad stock index funds, plus a bond fund that grows as you get
closer to needing the money. Or a single target date fund that does that mix for you. Look for low expense ratios. The
less you pay, the more you keep. And keep it boring. Boring is the point.""",
"""Here's why cost matters so much on the way to one hundred thousand. A fund charging one percent a year versus one
charging a small fraction of a percent might not look different in year one. But over decades, that fee difference
compounds into a very large amount of money. Same market, same years, less money for you.""",
"New York Stock Exchange trading floor", "BUY THE WHOLE MARKET",
"Pie chart on paper", "KEEP IT BORING",
"Receipt and coins on table", "LOW COST WINS")

step(9, "Control the big three", "housing, transport, food",
"""Step nine. Control the big three: housing, transportation and food.""",
"""According to the Bureau of Labor Statistics, housing, transportation and food together make up the largest share of
what American households spend. That means a ten percent cut in one of these is worth more than cancelling dozens of
small subscriptions. Small savings help. The big three move the needle.""",
"""On housing, think about a roommate, a smaller place, or a slightly longer commute. On transportation, keep cars
longer, buy reliable used ones, and avoid long loans. On food, cook more and plan meals. You don't need to do all of
it. One meaningful change in one of the big three can free hundreds of dollars a month.""",
"""Say you keep your current car for four more years instead of trading it in for a new one with a six hundred dollar
payment. That's over twenty eight thousand dollars you don't spend. Invested instead, that money alone could cover a
big chunk of the road to one hundred thousand.""",
"Apartment building", "THE BIG THREE",
"Old car parked on street", "KEEP THE CAR",
"Cooking at home kitchen", "COOK MORE")

step(10, "Grow your income", "the step with no ceiling",
"""Step ten. Grow your income. Cutting has a floor. Earning has no ceiling.""",
"""There's only so much you can cut. But there's no limit to how much your income can grow. A raise, a promotion, a
new job, a certification, or a side income can change your timeline more than any budget. Studies of wage growth have
found that people who switch jobs often see bigger raises than people who stay.""",
"""Start with your current job. Ask what it takes to get to the next level, and get it in writing. Look at job listings
for your role to see what you're worth. Learn one skill that's in demand in your field. And if you have time, a side
income, even a few hundred dollars a month, can go straight to savings.""",
"""Say a new certification bumps your salary by six thousand dollars a year. If you invest all of it, that's five
hundred dollars a month. At a seven percent illustration, that alone gets to one hundred thousand in about eleven
years. One skill, one raise, one decision.""",
"Person studying laptop at night", "NO CEILING",
"Job interview handshake", "KNOW YOUR WORTH",
"Graduation cap diploma", "ONE SKILL, ONE RAISE")

step(11, "Beat lifestyle creep", "the silent killer of progress",
"""Step eleven. Beat lifestyle creep.""",
"""Lifestyle creep is when your spending rises as fast as your income. A bigger apartment, a nicer car, more eating
out. None of it feels crazy. Each upgrade feels earned. But if everything you gain gets spent, your net worth stands
still, no matter how much you earn. It's why some high earners never get anywhere.""",
"""The fix isn't to never upgrade. It's to upgrade on purpose. Pick the one or two things that genuinely make you
happier, and spend on those without guilt. Then keep everything else the same. And keep the half of every raise rule
from step six. Your life gets better, and your savings rate keeps climbing.""",
"""Picture two coworkers who each get a ten thousand dollar raise. One upgrades their car and apartment and ends the
year with the same savings as before. The other upgrades their apartment a little and invests five thousand. Ten years
later, the second coworker could have roughly seventy thousand dollars more, at a seven percent illustration, from that
single decision repeated each year.""",
"Luxury car dealership", "LIFESTYLE CREEP",
"Shopping bags mall", "UPGRADE ON PURPOSE",
"Two people office", "SAME RAISE, NEW RESULT")

step(12, "Stay the course", "don't interrupt the process",
"""Step twelve. Stay the course. This is the step that decides whether you actually reach one hundred thousand.""",
"""Somewhere on the way, the market will drop. Maybe ten percent, maybe thirty. Broad markets have fallen like that many
times in history and, so far, recovered, though the past doesn't guarantee the future. The people who reach their
goals usually keep investing through the drops. The people who don't often sell at the bottom and lock in their
losses.""",
"""Make a simple rule now, while things are calm. I keep investing every month, no matter what the news says. Check your
accounts once a month, not once a day. And once a year, rebalance: if your stocks have grown much bigger than your plan,
move a bit back to bonds, and vice versa. That's it. Discipline beats intelligence.""",
"""Think of it this way. When prices fall, your monthly investment buys more shares. If you're still years away from
needing the money, a drop is actually a sale. It doesn't feel like one. It feels terrible. But the investors who treat
drops as sales, instead of emergencies, are usually the ones who get to one hundred thousand first.""",
"Stock market chart falling on screen", "THE MARKET WILL DROP",
"Calendar planning", "ONE RULE",
"Store sale sign", "A DROP IS A SALE")

# ---------------- Finding the money ----------------
ch("Finding your first $300 a month")
pr("""Every path starts with finding some money each month. So here's where people usually find their first three
hundred dollars a month, without a second job.""")
sc("""Start with subscriptions and memberships. Streaming services, apps, a gym you don't go to, software you forgot
about. Go through your bank statement line by line. Many people find thirty to eighty dollars a month here in under an
hour, and they don't miss any of it.""",
   "Online banking smartphone app", "SUBSCRIPTIONS")
sc("""Next, the bills you never question. Call your phone company, your internet provider and your insurance company,
and ask for a better rate, or compare quotes from competitors. Prices for the same service can vary a lot, and loyal
customers are often paying the most. An hour of phone calls can save another fifty to one hundred fifty dollars a
month.""",
   "Phone call customer service", "CALL AND ASK")
sc("""Then food. Delivery apps add fees, tips and higher menu prices on top of the meal. Cutting delivery from twice a
week to twice a month, and bringing lunch to work a few days a week, can easily free up one hundred dollars or more.
You're not giving up good food. You're giving up the markup.""",
   "Cooking at home kitchen", "THE FOOD MARKUP")
sc("""And finally, the money you already have but don't see. A tax refund. A bonus. Cash back rewards. Money from
selling things you don't use. Instead of letting these disappear into everyday spending, send them straight to your
current step. A single tax refund can fill a starter emergency fund in one day.""",
   "Garage sale items", "MONEY YOU DON'T SEE")
sc("""Add those up, and three hundred dollars a month is realistic for a lot of households, with no change in where
you live or what you drive. At a seven percent illustration, three hundred dollars a month for thirty years grows to
over three hundred sixty thousand dollars. That's what's hiding in your bank statement right now.""",
   "Calculator with financial charts", "$300 A MONTH = A LOT")

# ---------------- Angle 2: psychology ----------------
short("Most people quit saving at almost exactly the same point. Here's why.")
ch("Angle 2: The psychology")
pr("""Angle two. The psychology. Because most people who start this journey don't fail at step one. They quit somewhere
in the middle. And it happens at surprisingly predictable points.""")
sc("""The first danger zone is around ten to twenty thousand dollars. The debt is gone, there's a cushion, and the urgency
disappears. People feel safe, and safe feels like done. This is where many people stop pushing. The fix is to set the
next goal before you reach the current one. When you hit twenty thousand, you should already be aiming at fifty.""",
   "Person relaxing on couch", "DANGER ZONE 1: SAFE FEELS DONE")
sc("""The second danger zone is the slow middle, around thirty to sixty thousand. Growth is still small compared with your
contributions, and every month feels the same. It's boring. Behavioral researchers have shown that people value rewards
now much more than rewards later. When the reward is years away, motivation fades. The fix is to celebrate milestones:
every ten thousand dollars, mark it. Make progress visible.""",
   "Long road desert", "DANGER ZONE 2: THE SLOW MIDDLE")
sc("""The third danger zone is comparison. Around the time you're making real progress, you'll notice what other people
are spending. New cars, big trips, bigger houses. It's easy to feel like you're missing out. But remember, you're seeing
their spending, not their balance sheet. Many of them are on level two, with nicer things.""",
   "Social media smartphone", "DANGER ZONE 3: COMPARISON")
sc("""The fourth is the first big market drop. Watching ten thousand dollars disappear from your account in a few weeks
is genuinely painful. Psychologists Daniel Kahneman and Amos Tversky showed that losses hurt roughly twice as much as
equal gains feel good. That's why people panic. Knowing this in advance won't remove the pain, but it can stop you from
acting on it.""",
   "Stock market crash newspaper", "DANGER ZONE 4: THE FIRST CRASH")
sc("""And here's the good news. People who reach one hundred thousand often say the second hundred thousand came much
faster. Partly because of compounding. But partly because by then, saving had become a habit, not a decision. The
first hundred thousand builds the person. After that, the person builds the money.""",
   "Mountain climber reaching summit", "THE HABIT BUILDS THE MONEY")

# ---------------- Angle 3: playbook ----------------
short("Three incomes, three paths to one hundred thousand dollars. Which one is yours?")
ch("Angle 3: The playbook")
pr("""Angle three. The playbook. Here are three example paths to one hundred thousand dollars, for three different
incomes. They're made up examples, but the math is simple and real.""")
sc("""Path one. Forty thousand dollars a year. Alex starts with three thousand dollars of credit card debt. Six months to
build a starter cushion and clear the card. Then Alex invests three hundred dollars a month, plus a small employer match
of about one hundred dollars. Every raise, half goes to savings. At a seven percent illustration, Alex reaches one
hundred thousand in roughly thirteen years. Not fast. But steady, and completely realistic.""",
   "Young man working warehouse", "PATH 1: $40,000 A YEAR")
sc("""Path two. Seventy thousand dollars a year. Jordan has no debt except a car loan. Jordan builds a full emergency fund
in a year, then invests fifteen percent of income, about eight hundred seventy five dollars a month, plus a match of about
one hundred seventy five. That's roughly one thousand fifty dollars a month. At the same illustration, Jordan reaches one
hundred thousand in a little over six years.""",
   "Young woman working on laptop", "PATH 2: $70,000 A YEAR")
sc("""Path three. A couple earning one hundred twenty thousand together. Sam and Riley keep one modest car, cook most
meals, and invest twenty percent of their income, about two thousand dollars a month, including matches. At a seven
percent illustration, they reach one hundred thousand dollars in a little under four years. Then they keep
going, and the second hundred thousand comes even faster.""",
   "Couple cooking together kitchen", "PATH 3: $120,000 TOGETHER")
sc("""Notice what's the same in all three paths. The order. Starter cushion, match, high interest debt, full cushion,
automate, invest cheaply, control the big three, grow income, beat lifestyle creep, stay the course. The income changes
the speed. The order is the same for everyone.""",
   "Staircase steps", "THE ORDER IS THE SAME")
sc("""And here's your one page plan. At the top, write your net worth today. Under it, write which step you're on. Under
that, the one action for this month. And at the bottom, the date you'll check again. Tape it somewhere you'll see it.
That page is worth more than any budgeting app, because it tells you exactly what to do next.""",
   "Notebook with financial notes", "YOUR ONE PAGE PLAN")

# ---------------- Milestones ----------------
short("Here's what one thousand, ten thousand and fifty thousand dollars really feel like.")
ch("What every milestone feels like")
pr("""Let's walk the whole road from zero to one hundred thousand, milestone by milestone, and talk about what
actually changes at each one. Because knowing what's coming makes it much easier to keep going.""")
sc("""One thousand dollars. This is the first milestone, and it's mostly emotional. For many people, it's the first time
they've ever had money that wasn't already spoken for. A surprise bill no longer means a credit card. People often
describe a strange, quiet feeling of control. It's small money. It's a big moment.""",
   "Piggy bank coins", "$1,000: CONTROL")
sc("""Ten thousand dollars. Now you have real options. You could survive a few months of reduced income. You could move
for a better job. You could say no to something that's bad for you. Ten thousand dollars is often the point where people
stop feeling poor, even if their income hasn't changed at all. And at a seven percent illustration, ten thousand dollars
can grow by about seven hundred dollars in a year, without you adding a cent.""",
   "Person standing at crossroads", "$10,000: OPTIONS")
sc("""Twenty five thousand dollars. This is where many people's emergency fund is full and their investing is truly under
way. You can absorb most of life's surprises. And it's often where people first notice their investments moving by more
in a single day than they used to save in a week. That can be exciting, and a little scary. It's a good time to remind
yourself that daily swings don't matter. Years matter.""",
   "Stock market chart on screen", "$25,000: REAL INVESTOR")
sc("""Fifty thousand dollars. Halfway. But here's the surprise: in time, you're usually more than halfway, because the
second fifty thousand comes faster than the first. Growth starts to carry real weight. At a seven percent illustration,
fifty thousand dollars can earn around three thousand five hundred in a year. For many people that's like an extra
month or two of saving, delivered by the market instead of their paycheck.""",
   "Halfway sign road", "$50,000: HALFWAY")
sc("""Seventy five thousand dollars. This is where the finish line becomes visible, and where a lot of people get
impatient. They start looking for ways to speed up, and that's when risky bets look tempting. Don't. You're close
precisely because you did boring things consistently. Keep doing them. The last stretch rewards patience more than any
other.""",
   "Long road desert", "$75,000: STAY PATIENT")
sc("""And one hundred thousand dollars. Most people say it doesn't feel like fireworks. It feels like confidence. You've
proven to yourself that you can do it. You know the steps. And the next milestones, two hundred and fifty thousand, five
hundred thousand, one million, suddenly stop sounding like fantasy and start sounding like math.""",
   "Mountain climber reaching summit", "$100,000: CONFIDENCE")

# ---------------- Mistakes ----------------
ch("Five mistakes on the way")
pr("""Before the recap, five mistakes that slow people down on the way to one hundred thousand.""")
sc("""Mistake one. Investing before having any emergency cash. The first surprise turns into credit card debt, and the
whole plan stalls. Mistake two. Paying off low interest debt early while ignoring high interest debt. Always attack the
highest rate first. Mistake three. Leaving money in cash inside a retirement account, never actually invested.""",
   "Credit card bills on table", "MISTAKES 1 TO 3")
sc("""Mistake four. Chasing fast money. Hot stock tips, crypto hype, a friend's sure thing. Some people get lucky. Many
lose years of progress. And mistake five. Stopping contributions when the market drops, which means buying less when
prices are lowest. Keep the automation running. The plan works because you don't interrupt it.""",
   "Slot machines casino", "MISTAKES 4 AND 5")

# ---------------- Questions ----------------
ch("Questions people ask")
pr("""Let me answer a few questions I get all the time about the first one hundred thousand.""")
sc("""Question one. Does home equity count toward the hundred thousand? For net worth, yes. But for this plan, I'd focus
on savings and investments, because that's money that can grow and support you. Question two. Should I invest or pay
off student loans first? It depends on the rate. Low rate federal loans can often sit alongside investing. High rate
private loans usually come first.""",
   "House with for sale sign", "HOME EQUITY? STUDENT LOANS?")
sc("""Question three. What if I'm starting at forty five? The steps are the same. You'll probably invest larger amounts,
and you can use catch up contributions once you turn fifty, which the IRS allows in retirement accounts. Question four.
What if my income is unpredictable? Build a bigger emergency fund, closer to six months, and invest a percentage of each
payment instead of a fixed amount.""",
   "Older man reading financial newspaper", "STARTING LATE? IRREGULAR INCOME?")
sc("""Question five. Do I need a financial advisor to do this? Most people can do these twelve steps on their own. If you
want help, a fee only planner who charges by the hour or by the project can review your plan without selling you
products. Just make sure you know exactly how anyone you work with gets paid.""",
   "Business meeting handshake", "DO I NEED AN ADVISOR?")
sc("""Question six. Where should I keep my emergency fund? Somewhere safe, separate and easy to reach. For most people that
means a high yield savings account at an FDIC insured bank, or a credit union insured by the NCUA. Not in stocks, because
the emergency always seems to arrive when the market is down. Question seven. Is it okay to use a budgeting app? Absolutely,
if you'll use it. The best budget is the one you actually look at.""",
   "Bank building United States", "WHERE DOES THE CUSHION GO?")
sc("""Question eight. What if I fall back a step? You will, probably more than once. A car dies, you change jobs, a family
emergency eats your cushion. That's not failure. That's exactly what the cushion was for. Go back to the step you're on,
rebuild, and keep going. The people who reach one hundred thousand aren't the ones who never fall back. They're the ones
who never quit.""",
   "Person running on road", "WHAT IF I FALL BACK?")

# ---------------- Recap ----------------
ch("Recap: 12 steps in order")
sc("""Let's recap the twelve steps, in order. One, know your numbers. Two, a starter emergency fund. Three, get the full
employer match. Four, kill high interest debt. Five, a full emergency fund. Six, automate and raise your savings rate.""",
   "Staircase steps", "STEPS 1 TO 6")
sc("""Seven, open an IRA. Eight, invest simply and cheaply. Nine, control the big three. Ten, grow your income. Eleven,
beat lifestyle creep. And twelve, stay the course. Do them in this order, and each step makes the next one easier.""",
   "Mountain climber reaching summit", "STEPS 7 TO 12")
sc("""And the three angles. The numbers: five hundred a month gets there in about eleven years, one thousand in under
seven. The psychology: watch out for the danger zones, especially safe feels done and the first crash. And the playbook:
the income changes the speed, but the order stays the same for everyone.""",
   "Map and compass", "NUMBERS, PSYCHOLOGY, PLAYBOOK")
sc("""And remember why the order matters so much. Each step protects the one after it. The starter cushion protects your
debt payoff from new debt. The full cushion protects your investments from forced selling. Automation protects your plan
from bad days and busy months. And staying the course protects all of it from fear. Skip a step, and the steps above it
become fragile. Follow the order, and every step you climb stays climbed.""",
   "Brick wall construction", "EACH STEP PROTECTS THE NEXT")

# ---------------- Close ----------------
ch("What to do next")
pr("""So here's your homework. Find your step. Just one. And do the action for that step this week. Not all twelve. One. Then next month, check where you are,
and if that step is done, move to the next one. Twelve steps sounds like a lot, but you only ever have to do one at a
time.
If you want the full plan with worksheets, it's in my playbook, link in the description. And when you get close to one
hundred thousand, watch my video on what changes at that level. I'm Ryan Rover. See you in the next one.""")

save("video05", "From $0 to $100K: Every Step, In Order", [
    "Federal Reserve, Economic Well-Being of U.S. Households in 2025 (63% would cover a $400 expense with cash or its equivalent)",
    "Federal Reserve G.19 Consumer Credit (credit card interest rates above 20%)",
    "IRS, 401(k) and IRA contribution limits and catch-up contributions (check current-year limits)",
    "S&P Dow Jones Indices, SPIVA U.S. Scorecard (most active funds trail their benchmark over long periods)",
    "Bureau of Labor Statistics, Consumer Expenditure Survey (housing, transportation and food are the largest spending categories)",
    "Kahneman and Tversky, Prospect Theory, Econometrica (1979) (losses loom larger than gains)",
    "Compound growth: stated illustrative math at 7% average yearly return, compounded monthly",
], "from $0 to $100k, every step in order")
