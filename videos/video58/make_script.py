import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

EXTRA = {
1: ("""If you're starting at zero, be gentle with yourself. Many people are. The point of this step isn't to feel bad about the number. It's
to know exactly where the starting line is, so every dollar you add feels like progress.""",
  "Starting line on track", "ZERO IS A STARTING LINE"),
2: ("""For most people, essential expenses are somewhere between sixty and seventy five percent of their normal spending. If you normally
spend four thousand a month, your essentials might be around twenty eight hundred. That's the number your emergency fund is built
around.""",
  "Essentials list", "USUALLY 60 TO 75%"),
3: ("""Look for an account with no monthly fees, no minimum balance, and FDIC or NCUA insurance. Check the current interest rate, but don't
chase every small rate change. The most important features are safety and easy access within a day or two.""",
  "Bank comparison chart", "SAFE, FREE, ACCESSIBLE"),
4: ("""If you can't name an amount yet, start with ten dollars per paycheck. The habit matters more than the amount at first. You can raise
it every month as you find more money.""",
  "Ten dollar bill", "EVEN $10 COUNTS"),
5: ("""A good trick is to round up your goal. If your quick win target is five hundred dollars, set up the account so you see a progress bar,
or write the number on a sticky note and update it every week. Visible progress keeps people going.""",
  "Progress bar app", "MAKE PROGRESS VISIBLE"),
6: ("""Once the thousand dollars is in place, many people notice a real change. A flat tire or a vet bill no longer means panic. That first
thousand dollars often does more for peace of mind than any later milestone.""",
  "Calm person changing tire", "PEACE OF MIND"),
7: ("""Sell things you don't use. Many homes have a few hundred dollars of unused electronics, furniture, sports gear or clothing. Online
marketplaces and local groups make it easy. Every sale goes straight to the fund.""",
  "Selling items online", "SELL WHAT YOU DON'T USE"),
8: ("""Watch for these moments throughout the year: tax refunds, bonuses, cash gifts, rebates, and the extra paychecks in months with three
paydays. Decide in advance that a set share of each one goes to the emergency fund until it's full.""",
  "Tax refund check", "DECIDE IN ADVANCE"),
9: ("""This step is what keeps the emergency fund from being drained by non emergencies. Without sinking funds, a holiday or an annual bill
looks like an emergency. With them, the emergency fund stays protected for the truly unexpected.""",
  "Holiday gifts and savings", "PROTECT THE FUND"),
10: ("""If you have high interest debt, a common approach is to build the fund to about one thousand dollars, then focus on paying down the
debt, then come back and build the full fund. That way you're protected from new debt while you clear the old.""",
  "Debt and savings balance", "BALANCE IT WITH DEBT"),
11: ("""Write down your own rules before you need them. For example: job loss, medical bills, urgent car or home repairs, emergency travel
for family. Not: sales, vacations, or things you could have planned. Clear rules make hard moments easier.""",
  "Written rules list", "WRITE YOUR RULES"),
12: ("""Once your fund is full, the money you were sending to it can go somewhere new: investing, a down payment, or paying off a loan faster.
The emergency fund isn't the end of the plan. It's the foundation that makes the rest possible.""",
  "Foundation and house", "THEN BUILD ON IT"),
}


EXTRA2 = {
1: ("""Also list any debts and their minimum payments, and any money that's coming soon, like a tax refund or a final paycheck. This gives you
a complete, honest snapshot. It only takes about twenty minutes, and it turns a vague worry into specific numbers.""",
  "Notebook with numbers", "A COMPLETE SNAPSHOT"),
2: ("""If you're not sure what you spend, look at the last three months of bank statements and average them. Don't include things you'd
cut immediately in a crisis, like dining out or streaming services. Those aren't essentials when times are hard.""",
  "Bank statements highlighted", "WHAT YOU'D KEEP IN A CRISIS"),
3: ("""Give the account a clear name, like Emergency Fund, or something personal, like Peace of Mind. A named account with a purpose is
psychologically harder to spend from. It's a small trick, but it works for many people.""",
  "Named savings account", "NAME IT"),
4: ("""If your income arrives on different days, set the transfer for the day each paycheck lands. And if your bank allows it, set up
automatic round ups, which move spare change from each purchase into savings. Small amounts, many times a week, add up.""",
  "Round up savings app", "ROUND UPS HELP TOO"),
5: ("""At twenty five dollars a week, five hundred dollars takes about twenty weeks. At fifty dollars a week, about ten. Add one weekend of
selling unused things, and it can happen in a month or two.""",
  "Calendar weeks counting", "10 TO 20 WEEKS"),
6: ("""To get from five hundred to one thousand faster, look for one recurring cost to cut temporarily, like a streaming service, a gym you
don't use, or food delivery. Send that amount to the fund until you hit one thousand.""",
  "Canceling subscription", "CUT ONE THING TEMPORARILY"),
7: ("""Check your home for old phones, game consoles, furniture, baby gear, tools, bikes and clothes. And check for money you're owed: unclaimed
property databases run by states, forgotten gift cards, or refunds you never requested.""",
  "Unclaimed property website", "MONEY YOU'RE OWED"),
8: ("""A common split is to send at least half of every windfall to the emergency fund until it's full, and enjoy the rest. That way you make
real progress without feeling like every bit of good luck disappears.""",
  "Split money half", "HALF TO THE FUND"),
9: ("""Common sinking funds include car maintenance and registration, holidays and birthdays, school costs, medical copays, pet care, and home
or renters insurance if it's paid yearly. Start with the two or three that most often surprise you.""",
  "Sinking fund list", "COMMON SINKING FUNDS"),
10: ("""Every time you pay off a debt, redirect that payment straight to the emergency fund until it reaches your target. You're already used
to living without that money, so you won't feel the difference.""",
  "Debt paid off stamp", "REDIRECT OLD PAYMENTS"),
11: ("""If you share finances with a partner, agree on these rules together. And consider a simple threshold: any withdrawal above a certain
amount gets discussed first, unless it's a true urgent emergency.""",
  "Couple agreeing", "AGREE TOGETHER"),
12: ("""Some people keep a simple log of every time they used the fund and why. Over the years, it becomes a powerful reminder of how many
crises the fund turned into simple inconveniences.""",
  "Notebook log", "KEEP A LOG"),
}

def step(n, title, sub, card_text, paras):
    ch(f"Step {n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"STEP {n}")
    for t, q, c in paras:
        sc(t, q, c)
    sc(*EXTRA2[n])
    sc(*EXTRA[n])

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. If a four hundred dollar emergency hit you tomorrow, could you pay it in cash? According to the Federal Reserve,
millions of American adults couldn't. If that's you, this video is for you. Today, I'll show you how to build an emergency fund from
absolutely zero, step by step, even on a tight budget.""")
short("Could you cover a $400 emergency tomorrow? Millions can't.")
sc("""An emergency fund is money set aside only for real emergencies: a job loss, a medical bill, an urgent car repair. It's not exciting.
It doesn't grow fast. But it might be the most important money you'll ever save, because it protects everything else.""",
   "Savings jar on table", "THE MOST IMPORTANT MONEY")
sc("""Without one, every surprise becomes debt. A car repair goes on a credit card. A medical bill becomes a payment plan. A lost job means
falling behind on rent. And once that cycle starts, it's very hard to escape.""",
   "Stressed person bills", "EVERY SURPRISE BECOMES DEBT")
sc("""We'll look at this from three angles. First, the numbers: how many people have an emergency fund, how much you need, and what not
having one costs. Second, the psychology: why saving for emergencies is so hard, and how to make it easier. And third, the playbook: twelve
steps from zero to a full emergency fund.""",
   "Three paths map", "THREE ANGLES")
pr("""Stay for step seven. It's a way to raise your first few hundred dollars in a single weekend. Let's start with the numbers.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Emergency savings data comes from the Federal Reserve's annual Survey of Household Economics and Decisionmaking, known as SHED.
Credit card interest information comes from the Federal Reserve's consumer credit data. Deposit insurance information comes from the FDIC
and NCUA. Behavioral research is named as we go. Interest examples are stated math. This is education, not financial advice.""",
   "Federal Reserve building", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. How many people are prepared, how much you need, and what it costs not to have it.""")
sc("""Every year, the Federal Reserve asks American adults a simple question: if you faced an unexpected expense of four hundred dollars,
how would you pay for it? In recent surveys, about sixty three percent said they would cover it with cash or its equivalent. That means
more than a third would not.""",
   "Survey results chart", "~63% COULD PAY $400 IN CASH")
card("""In recent Federal Reserve surveys, about sixty three percent of adults said they would cover a four hundred dollar emergency with cash
or its equivalent. More than a third would not.""",
     {"type": "stat", "label": "adults who would cover $400 with cash", "big": "~63%", "sub": "Federal Reserve SHED, recent years"})
sc("""Those who couldn't said they'd use a credit card and pay over time, borrow from friends or family, take a payday loan, sell something,
or simply wouldn't be able to pay. Each of those options costs money, relationships or stress.""",
   "Borrowing money from friend", "THE ALTERNATIVES COST")
sc("""Now, how much do you need? The most common guideline is three to six months of essential expenses. Essentials mean rent or mortgage,
utilities, groceries, insurance, transportation and minimum debt payments. Not your full lifestyle. Just what you'd need to keep the lights
on.""",
   "Essentials checklist", "3 TO 6 MONTHS OF ESSENTIALS")
sc("""If your essentials are twenty five hundred dollars a month, three months is seventy five hundred dollars and six months is fifteen
thousand. That can sound overwhelming from zero. But you don't build it all at once. You build it in stages, and every stage protects you
more.""",
   "Staircase stages", "$7,500 TO $15,000")
sc("""Who needs closer to six months, or more? People with irregular income, single income households, people in industries with frequent
layoffs, homeowners, and people with health conditions or dependents. Who might be okay with three? Dual income households with stable
jobs and few dependents.""",
   "Different households", "3 OR 6?")
sc("""Now, what does it cost not to have an emergency fund? Say a two thousand dollar car repair goes on a credit card at twenty two percent
interest, and you pay one hundred dollars a month. It would take about twenty six months to pay off, and you'd pay around twenty five
hundred dollars in total. The emergency cost five hundred dollars more because you didn't have savings.""",
   "Credit card bill interest", "$2,000 REPAIR = ~$2,500 ON CREDIT")
card("""A two thousand dollar emergency, paid with a credit card at twenty two percent interest with one hundred dollar monthly payments,
versus paid from savings.""",
     {"type": "compare", "left": {"label": "on a credit card", "big": "~$2,500", "sub": "about 26 months of payments"},
      "right": {"label": "from savings", "big": "$2,000", "sub": "paid once, then refill"},
      "note": "Illustration at 22% APR."})
sc("""And payday loans can be far more expensive. The Consumer Financial Protection Bureau has reported that a typical two week payday loan
can carry fees that work out to an annual percentage rate of almost four hundred percent. One emergency can turn into months of fees.""",
   "Payday loan storefront", "PAYDAY LOANS: ~400% APR")
sc("""Now the good news. Small, regular savings add up faster than people expect. Twenty five dollars a week is thirteen hundred dollars a
year. Fifty dollars a week is twenty six hundred. One hundred dollars a week is fifty two hundred. And in a high yield savings account,
that money can earn interest while it waits.""",
   "Coins stacking weekly", "$50 A WEEK = $2,600 A YEAR")
sc("""What kinds of emergencies actually happen? For most households, the common ones are car repairs, medical and dental bills, home or
appliance repairs, pet emergencies, and income disruptions like reduced hours or job loss. Most of these aren't rare. Over a few years,
almost every household faces several of them.""",
   "Broken car on roadside", "THE COMMON EMERGENCIES")
sc("""Job loss is the big one. The Bureau of Labor Statistics reports that in recent years, the median length of unemployment has often been
around two to three months, and many people take longer to find work. That's one reason three to six months of essentials is the standard
guideline. It covers a typical job search with room to spare.""",
   "Job search laptop", "JOB SEARCHES TAKE TIME")
sc("""And here's a bonus. In a high yield savings account, your emergency fund earns interest while it waits. Some high yield accounts have
paid around four percent a year recently, though rates change. On a ten thousand dollar fund, four percent is about four hundred dollars a
year, money that works for you instead of against you.""",
   "Interest earned statement", "IT EARNS WHILE IT WAITS")
card("""Saving one hundred fifty dollars a week, about six hundred fifty a month, for two years in an account earning four percent a year.""",
     {"type": "growth", "monthly": 650, "rate": 0.04, "years": 2})
pr("""So the math is clear: an emergency fund saves money and protects you. Then why is it so hard to build? Angle two.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
pr("""Angle two. The psychology. Five reasons emergency funds are hard to build, and how to beat each one.""")
short("Why saving for emergencies feels impossible, and how to fix it")
sc("""Reason one. It feels like nothing is happening. Investing has growth charts. Paying off debt has shrinking balances. An emergency fund
just sits there. Our brains like visible rewards, and this money's reward is invisible: the crisis that never happens.""",
   "Empty quiet room", "REASON 1: INVISIBLE REWARD")
sc("""The fix: make progress visible. Name the account, set a goal, and watch a progress bar fill. Celebrate milestones like five hundred,
one thousand, and one month of expenses. Small celebrations keep you going.""",
   "Progress bar milestones", "THE FIX: VISIBLE PROGRESS")
sc("""Reason two. Present bias. Behavioral economists describe a tendency to value rewards today much more than rewards later. Spending
fifty dollars now feels great. Being protected from a future emergency feels abstract. So the present wins, again and again.""",
   "Present versus future scale", "REASON 2: PRESENT BIAS")
sc("""The fix: automate it, so the decision is made once. When savings happen automatically on payday, the present version of you doesn't
get a vote every week. Researchers Richard Thaler and Shlomo Benartzi showed with their Save More Tomorrow program that automatic,
pre committed savings can dramatically raise how much people save.""",
   "Automatic transfer setup", "THE FIX: AUTOMATE")
sc("""Reason three. It feels impossible from zero. When the goal is fifteen thousand dollars and you have zero, the gap is so big that
starting feels pointless. So people don't start.""",
   "Mountain looking huge", "REASON 3: TOO BIG")
sc("""The fix: break it into stages. Your first goal isn't fifteen thousand. It's five hundred. Then one thousand. Then one month. Each stage
is reachable, and each one makes you safer than before.""",
   "Small steps up mountain", "THE FIX: STAGES")
sc("""Reason four. Easy access, easy spending. If your emergency fund sits in your checking account, it slowly disappears into everyday
spending. Money that's always visible and one tap away rarely survives.""",
   "Money disappearing from wallet", "REASON 4: TOO EASY TO SPEND")
sc("""The fix: separation. Keep the fund in a separate high yield savings account, maybe even at a different bank. Close enough to reach in a
day or two. Far enough that you don't spend it by accident.""",
   "Separate bank account", "THE FIX: SEPARATION")
sc("""And reason five. Every month feels like an emergency. When money is tight, there's always something urgent. Kids need shoes. A bill is
higher than expected. It can feel like there's never extra.""",
   "Overwhelmed parent", "REASON 5: ALWAYS SOMETHING")
sc("""The fix: separate expected costs from true emergencies. Shoes, birthdays and annual bills are expected, even if irregular. Plan for them
with small sinking funds. Then the emergency fund is only touched for real surprises.""",
   "Sinking fund envelopes", "THE FIX: SINKING FUNDS")

ch("The mindset that works")
sc("""Here's a mindset shift that helps many people. Think of your emergency fund as insurance you pay to yourself. Instead of paying
interest to a credit card company after an emergency, you pay into your own account before it. And unlike most insurance, if you never
need it, you keep every dollar.""",
   "Insurance paid to yourself", "INSURANCE YOU OWN")
sc("""And think of it as buying calm. Many people say the first thousand dollars in savings did more for their stress level than any raise.
You're not just saving money. You're buying the ability to handle bad news without panic.""",
   "Calm person reading news", "BUYING CALM")

# ---------------- History ----------------
ch("Saving for a rainy day")
sc("""The idea of saving for hard times is ancient. Many cultures have a version of the advice. In the Bible, Joseph advises Pharaoh to store
grain during seven good years to prepare for seven years of famine. The phrase saving for a rainy day has been used in English for
centuries.""",
   "Ancient grain storage", "AN ANCIENT IDEA")
sc("""During the Great Depression in the 1930s, many American families lost their savings when thousands of banks failed. That's one reason
Congress created the Federal Deposit Insurance Corporation in 1933, to protect bank deposits. Today, FDIC insurance covers deposits up to
legal limits, currently two hundred fifty thousand dollars per depositor, per insured bank, for each account ownership category.""",
   "1930s bank run", "1933: THE FDIC")
sc("""For many decades, people kept emergency savings in passbook savings accounts at local banks. Then, in the 2000s, online banks began
offering higher interest rates because they didn't have branch costs. Today, anyone can open a high yield savings account in minutes.""",
   "Old passbook savings book", "FROM PASSBOOKS TO APPS")

# ---------------- Mid ----------------
ch("A quick favor")
pr("""Quick pause. If you're building your emergency fund, or about to start, subscribe to the channel. It's free, and it helps me keep
making these videos. Now, the twelve steps from zero.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
pr("""Angle three. The playbook. Twelve steps from zero to a full emergency fund.""")
short("12 steps to build an emergency fund from zero")

step(1, "Face the starting line", "know your numbers",
"""Step one. Face the starting line.""",
[("""Write down how much cash you have available right now, outside of what's needed for this month's bills. For many people starting this
journey, the honest answer is close to zero.""",
  "Bank balance low", "WHERE YOU ARE NOW")])

step(2, "Calculate your essential expenses", "your target",
"""Step two. Calculate your essential expenses.""",
[("""Add up rent or mortgage, utilities, groceries, insurance, transportation, childcare and minimum debt payments. That's your monthly
essentials. Multiply by three and by six. Those are your long term targets.""",
  "Calculator essentials", "MULTIPLY BY 3 AND 6")])

step(3, "Open a separate high yield savings account", "a home for the fund",
"""Step three. Open a separate high yield savings account.""",
[("""Online banks and many credit unions offer high yield savings accounts that often pay much more interest than a typical big bank
savings account. Deposits are insured by the FDIC or NCUA up to legal limits.""",
  "High yield savings online", "A SEPARATE HOME")])

step(4, "Automate a small transfer", "pay your future first",
"""Step four. Automate a small transfer.""",
[("""Set up an automatic transfer from checking to your emergency fund the day after payday. Choose an amount you won't notice too much,
even if it's twenty five dollars.""",
  "Automatic transfer", "THE DAY AFTER PAYDAY")])

step(5, "Hit your first quick win", "$500",
"""Step five. Hit your first quick win: five hundred dollars.""",
[("""Five hundred dollars can cover many common emergencies, like a minor car repair, a doctor visit or a broken phone. It's the first
milestone, and it's reachable within a few months for most people.""",
  "Five hundred dollars", "THE FIRST $500")])

step(6, "Reach $1,000", "the starter fund",
"""Step six. Reach one thousand dollars.""",
[("""One thousand dollars is a classic starter emergency fund. It covers many of the surprises that would otherwise go on a credit card.""",
  "One thousand dollars", "$1,000 STARTER FUND")])

step(7, "Raise money in a weekend", "the jump start",
"""Step seven. Raise money in a weekend.""",
[("""Here's the jump start. Spend one weekend raising cash: sell unused items, pick up an extra shift, do a few hours of gig work, or offer
a service like babysitting, yard work or tutoring. Many people raise a few hundred dollars in a single weekend.""",
  "Garage sale weekend", "ONE WEEKEND, A FEW HUNDRED")])

step(8, "Capture windfalls", "refunds, bonuses, gifts",
"""Step eight. Capture windfalls.""",
[("""According to the IRS, the average tax refund in recent years has been around three thousand dollars. For many households, that single
refund could build most of a starter emergency fund in one day.""",
  "Tax refund", "~$3,000 AVERAGE REFUND")])

step(9, "Build sinking funds alongside", "for the expected",
"""Step nine. Build sinking funds alongside.""",
[("""Once you have a starter fund, add small sinking funds for predictable irregular costs: car maintenance, holidays, gifts, annual bills.
Even ten or twenty dollars a month for each makes a difference.""",
  "Labeled sinking funds", "FOR THE EXPECTED")])

step(10, "Grow to one month, then three", "the next stages",
"""Step ten. Grow to one month, then three months.""",
[("""After the starter fund, aim for one full month of essentials, then three months. Raise your automatic transfer every time you can,
especially after a raise or after paying off a debt.""",
  "Stages chart", "ONE MONTH, THEN THREE")])

step(11, "Define what counts as an emergency", "rules in advance",
"""Step eleven. Define what counts as an emergency.""",
[("""A simple test: is it unexpected, is it necessary, and is it urgent? If all three are yes, it's probably an emergency. If not, it
belongs in a sinking fund or your regular spending.""",
  "Three question checklist", "UNEXPECTED, NECESSARY, URGENT")])

step(12, "Use it, then refill it", "the cycle",
"""Step twelve. Use it, then refill it.""",
[("""When a real emergency happens, use the fund without guilt. That's exactly what it's for. Then restart your automatic transfers, or raise
them for a while, until the fund is back to full.""",
  "Refill savings jar", "USE IT, THEN REFILL")])

# ---------------- Stages ----------------
ch("The five stages, at a glance")
short("The 5 stages of an emergency fund")
sc("""Let's put it all together. Stage one: five hundred dollars. The quick win. Stage two: one thousand dollars. The starter fund. Stage
three: one month of essential expenses. Stage four: three months. Stage five: six months, or more if your situation calls for it.""",
   "Five stage staircase", "THE FIVE STAGES")
card("""Five hundred dollars, then one thousand, then one month of essentials, then three months, then six.""",
     {"type": "stat", "label": "the five stages", "big": "$500 → $1K → 1 → 3 → 6", "size": 100, "sub": "months of essential expenses"})
sc("""How long does it take? With essentials of twenty five hundred a month and one hundred fifty dollars a week saved, plus a tax refund
each year, many people could reach one thousand dollars in a few months, one month of essentials in under a year, and three months in about
two years. Faster with side income or windfalls.""",
   "Timeline calendar", "A REALISTIC TIMELINE")

# ---------------- Stories ----------------
ch("Three people, three starting points")
sc("""Let's meet three people. Kayla is a single mom earning thirty eight thousand dollars. She starts with twenty dollars a week and puts
most of her tax refund into savings. After one year, she has about thirty five hundred dollars. When her car's transmission fails, she
pays for most of the repair in cash.""",
   "Single mother with child", "KAYLA: $20 A WEEK + REFUND")
sc("""Devon is a delivery driver with irregular income. Some weeks are great, some are slow. He saves fifteen percent of every payout into a
separate account. After eighteen months, he has two months of expenses saved, and slow weeks no longer mean panic.""",
   "Delivery driver car", "DEVON: 15% OF EVERY PAYOUT")
sc("""And Linda and Ray, a couple in their fifties, had always relied on credit cards for emergencies. After Ray's hours were cut, their
card balances grew. They paused extra spending, sold a second car, and built three months of savings over two years. Now, when the
furnace failed last winter, they paid in cash for the first time in their lives.""",
   "Older couple at home", "LINDA AND RAY: STARTING IN THEIR 50s")
sc("""Notice something about all three stories. None of them saved a large amount at the start. Kayla started with twenty dollars a week.
Devon used a percentage. Linda and Ray started in their fifties after years of relying on credit. What they had in common was a decision to
start, and a system that kept going even when motivation faded.""",
   "Small seed growing plant", "THEY ALL STARTED SMALL")
sc("""Three different lives. Three different incomes. The same principles. Start small, automate, use windfalls, separate the money, and
keep going. These are illustrations, but they reflect what many real households do.""",
   "Three households", "THE SAME PRINCIPLES")

ch("Starting from zero while in debt")
sc("""Many people starting from zero also have credit card debt, and they wonder whether saving even makes sense. Here's the problem with
skipping the emergency fund entirely. While you're paying down a card, any surprise expense goes right back on it. You pay down two hundred
dollars, then a car repair adds five hundred. It feels like running on a treadmill.""",
   "Person on treadmill", "THE DEBT TREADMILL")
sc("""That's why a small starter fund comes first, even before aggressive debt payoff. With five hundred to one thousand dollars set aside,
surprises stop undoing your progress. Then every extra dollar can go to the debt with confidence.""",
   "Breaking free from treadmill", "STARTER FUND FIRST")
sc("""Once high interest debt is gone, the payments you were making become your emergency fund engine. If you were paying four hundred
dollars a month toward cards, send that same four hundred to savings. In about a year, you could have close to five thousand dollars. That's
how the cycle reverses.""",
   "Money flowing to savings", "THE CYCLE REVERSES")
sc("""And during this phase, be careful with new credit. Store cards, buy now pay later offers and payday loans can look like easy solutions
when money is tight. But they often make the next emergency worse. The emergency fund is the real solution.""",
   "Buy now pay later warning", "AVOID NEW DEBT TRAPS")

# ---------------- Where to keep it ----------------
ch("Where to keep your emergency fund")
sc("""Where should the money live? The main options are high yield savings accounts, money market accounts at banks or credit unions, and
money market funds at brokerages. All three can be good choices. The key features are safety, easy access, and a reasonable interest
rate.""",
   "Savings options comparison", "THE MAIN OPTIONS")
sc("""High yield savings accounts and bank money market accounts are generally FDIC insured up to legal limits, and credit union accounts are
NCUA insured. Money market funds at brokerages are not FDIC insured, though they invest in short term, high quality securities. Know which
one you have.""",
   "Insurance shield", "KNOW WHAT'S INSURED")
sc("""Avoid keeping your emergency fund in stocks, crypto, or long term CDs with large early withdrawal penalties. You want the money to be
there, at full value, the moment you need it. Earning a little less is the price of safety, and it's worth it.""",
   "Warning stocks crypto", "AVOID RISKY PLACES")
sc("""Once your fund is large, some people split it. One or two months in a high yield savings account for instant access, and the rest in
a slightly higher yielding safe option. That's optional. For most people, one good high yield account is enough.""",
   "Two savings tiers", "SPLITTING IT IS OPTIONAL")

sc("""A practical tip. Make sure you can actually get the money quickly. Test a transfer from your emergency account to your checking account
before you need it, and note how long it takes. Most online transfers arrive within one to three business days. If a real emergency needs
cash the same day, a small amount in checking or a credit card you pay off immediately with the transferred funds can bridge the gap.""",
   "Bank transfer timing", "TEST THE TRANSFER")

# ---------------- Special situations ----------------
ch("Special situations")
sc("""Irregular income. Freelancers, gig workers and commission earners need a bigger cushion, often six months or more. A helpful approach
is to save a fixed percentage of every payment, like ten or fifteen percent, rather than a fixed dollar amount. In good months, you save
more automatically.""",
   "Freelancer laptop", "IRREGULAR INCOME")
sc("""Couples. Decide whether the emergency fund will be joint or separate. Many couples keep one shared fund for household emergencies, and
each person may also keep a small personal cushion. What matters is that both people know where it is and how it can be used.""",
   "Couple reviewing savings", "COUPLES")
sc("""Families with kids. Kids bring their own surprises: urgent care visits, broken glasses, last minute school costs. Families often aim for
the higher end of the range, closer to six months, and add a kids sinking fund for the expected surprises.""",
   "Family with children", "FAMILIES")
sc("""Homeowners. A water heater, a roof leak or a broken furnace can cost thousands. Homeowners often keep a separate home repair sinking
fund, with a common guideline of setting aside around one to two percent of the home's value each year.""",
   "Water heater repair", "HOMEOWNERS")
sc("""And people with health conditions. Medical costs can be unpredictable. If you have a high deductible health plan, a health savings
account can help with medical costs, but your regular emergency fund should still cover your deductible and out of pocket maximum.""",
   "Medical bills HSA", "HEALTH COSTS")

# ---------------- Mistakes ----------------
ch("Common emergency fund mistakes")
sc("""Mistake one: waiting until you can save a lot. Starting small beats waiting. Twenty five dollars this week is better than five hundred
someday.""",
   "Small coin jar", "MISTAKE 1: WAITING")
sc("""Mistake two: keeping it in checking. Money in your everyday account tends to vanish. Separate it.""",
   "Checking account vanishing", "MISTAKE 2: CHECKING")
sc("""Mistake three: using it for non emergencies. Sales, vacations and predictable bills aren't emergencies. Use sinking funds for those.""",
   "Shopping sale sign", "MISTAKE 3: NON EMERGENCIES")
sc("""Mistake four: never refilling it. After using the fund, make refilling it the top priority until it's full again.""",
   "Empty jar", "MISTAKE 4: NOT REFILLING")
sc("""And mistake five: keeping too much forever. Once you have a full six months and a stable life, extra cash beyond that may be better
invested for long term goals. An emergency fund should protect your future, not replace investing for it.""",
   "Too much cash pile", "MISTAKE 5: TOO MUCH CASH")

ch("What changes when you have one")
sc("""People who build a full emergency fund often describe the same change. Money stress drops. They sleep better. They feel more confident
at work, because a layoff wouldn't be a disaster. And they make better decisions, because they're not choosing out of fear.""",
   "Person sleeping peacefully", "LESS STRESS")
sc("""It also changes your options. With three to six months saved, you can negotiate a raise more confidently, leave a bad job, take a short
break between jobs, or say no to a predatory loan. An emergency fund isn't just protection. It's freedom.""",
   "Person walking confidently", "MORE OPTIONS")

ch("Your first week")
sc("""Here's your first week. Day one: write down your current savings and your monthly essentials. Day two: open a separate high yield
savings account. Day three: set up an automatic transfer for payday.""",
   "Checklist days", "DAYS 1 TO 3")
sc("""Day four: list three things you could sell and post them. Day five: cancel one subscription and redirect it to savings. Day six: write
down your emergency rules. Day seven: celebrate your first deposit, however small. You've started.""",
   "Celebrating small win", "DAYS 4 TO 7")

ch("But Ryan, what about...")
sc("""Objection one. I'm living paycheck to paycheck. I can't save anything. Start with the smallest possible amount, even five dollars a
week, and focus on step seven, raising money in a weekend, and step eight, windfalls. A tax refund alone can transform your starting point.""",
   "Tight budget calculator", "PAYCHECK TO PAYCHECK")
sc("""Objection two. Inflation will eat my savings. Inflation does reduce buying power, which is why high yield accounts matter. But the
purpose of an emergency fund isn't growth. It's protection. Avoiding one credit card emergency at over twenty percent interest is worth far
more than a few percent of extra return.""",
   "Inflation chart", "INFLATION")
sc("""And objection three. I'd rather invest everything. Investing is important, but without an emergency fund, you might have to sell
investments at a bad time or take on expensive debt. The emergency fund is what makes long term investing possible.""",
   "Investing and safety net", "I'D RATHER INVEST")

# ---------------- FAQ ----------------
ch("Questions people ask")
pr("""Let me answer the questions people ask me most about emergency funds.""")
sc("""Question one. Should I invest my emergency fund to earn more? Generally, no. An emergency fund needs to be safe and available when
you need it. Stocks can drop sharply, sometimes at the same time as layoffs. A high yield savings account or similar safe option is usually
the right home.""",
   "Stock chart versus savings", "INVEST IT?")
sc("""Question two. Should I build an emergency fund or pay off debt first? A common approach is a starter fund of about one thousand
dollars, then focus on high interest debt, then build the full fund. And always get your employer's retirement match if you can.""",
   "Debt versus savings", "DEBT OR SAVINGS?")
sc("""Question three. Can a credit card be my emergency fund? It can be a backup, but it's an expensive one. If you have to use it, interest
adds up fast, and your credit limit can be reduced when you need it most. Cash is safer.""",
   "Credit card in wallet", "CREDIT CARD AS BACKUP?")
sc("""Question four. Is my Roth IRA an emergency fund? Contributions to a Roth IRA can generally be withdrawn without tax or penalty, but
taking them out means losing years of tax free growth. Some people use it as a last resort backup. It's better to have a separate
emergency fund.""",
   "Roth IRA document", "ROTH AS BACKUP?")
sc("""And question five. What if I keep having to use it? That's a signal. If emergencies are frequent, the problem might be expenses that
are actually predictable, like an unreliable car or irregular bills. Sinking funds and planning can help. Or your budget may need a
bigger change to create more breathing room.""",
   "Repeated car repairs", "ALWAYS USING IT?")

sc("""Question six. How do I stay motivated when it's slow? Track milestones, not just the final goal. Every hundred dollars is progress.
Some people keep a simple chart on the fridge and color in a box for every fifty dollars saved. Small visual wins keep you moving.""",
   "Fridge savings chart", "STAYING MOTIVATED")
sc("""Question seven. Should my kids or teenagers have an emergency fund? A small one, yes. A teen with a part time job can learn the habit by
saving a portion of each paycheck. It's one of the best money lessons you can teach, because it builds a habit that lasts a lifetime.""",
   "Teenager with savings jar", "KIDS AND TEENS")
sc("""And question eight. Once I have six months, what's next? Keep the fund in place and adjust it as your expenses grow. Then redirect the
money you were saving into investing, paying off lower interest debt, or other goals. The emergency fund is the foundation. Now you build
the house.""",
   "House built on foundation", "WHAT'S NEXT")

# ---------------- Recap ----------------
ch("Recap: the 12 steps")
short("Build an emergency fund from zero: the 60-second version")
sc("""Quick recap. In recent Federal Reserve surveys, more than a third of adults couldn't cover a four hundred dollar emergency with cash.
Not having savings turns emergencies into expensive debt. And our brains fight saving, so we use visibility, automation, stages,
separation and sinking funds.""",
   "Checklist clipboard", "THE NUMBERS AND PSYCHOLOGY")
sc("""The twelve steps. Face the starting line. Calculate your essentials. Open a separate high yield account. Automate a small transfer.
Hit five hundred. Reach one thousand. Raise money in a weekend. Capture windfalls. Build sinking funds. Grow to one month, then three. Define
what counts as an emergency. And use it, then refill it.""",
   "Staircase twelve steps", "THE 12 STEPS")

sc("""One last thought. Building an emergency fund from zero can feel slow and boring. But it's one of the most powerful things you'll ever
do with money. It turns emergencies into inconveniences. It stops the cycle of debt. It gives you room to breathe and room to choose. And
it starts with a single small transfer. Today is a great day to make it.""",
   "Sunrise over town", "IT STARTS TODAY")
sc("""And if you're already on your way, keep going. Every dollar you add is a dollar of protection for you and the people who depend on
you. One day soon, a surprise bill will arrive, and you'll simply pay it. That's the moment you'll know it was worth it.""",
   "Person paying bill calmly", "THE MOMENT IT PAYS OFF")

# ---------------- Close ----------------
ch("What to do next")
pr("""Today, do steps three and four. Open the account, and set up an automatic transfer, even for twenty five dollars. That's the moment
your emergency fund begins. And watch my video on thirty money rules to live by. Rule number one is all about this. I'm Ryan Rover. See
you in the next one.""")

save("video58", "How to Build an Emergency Fund From Zero", [
    "Federal Reserve, Economic Well-Being of U.S. Households (SHED), recent reports ($400 emergency question)",
    "Federal Reserve, G.19 Consumer Credit (credit card interest rates)",
    "Consumer Financial Protection Bureau, payday loan research (typical APR near 400%)",
    "FDIC and NCUA, deposit insurance coverage",
    "IRS, filing season statistics (average refund)",
    "Richard H. Thaler and Shlomo Benartzi, Save More Tomorrow, Journal of Political Economy (2004)",
    "Credit card payoff example: stated illustrative math at 22% APR",
], "emergency fund from zero: numbers, psychology, playbook")
