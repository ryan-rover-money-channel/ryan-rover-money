import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short


EXTRA = {
1: ("""Then sort your spending into three groups: needs, like rent and groceries; wants, like eating out and streaming; and future,
like savings and debt payments. Seeing those three totals side by side is often the moment people decide to change something.""",
  "Three spending categories chart", "NEEDS, WANTS, FUTURE"),
2: ("""Give it a name, like Emergency Fund or Freedom Fund. It sounds silly, but research in behavioral economics suggests people
are less likely to raid money that has a clear purpose. Keep it at a different bank from your checking account if that helps you
leave it alone.""",
  "Named savings account", "NAME YOUR ACCOUNT"),
3: ("""If one thousand dollars feels far away, break it into pieces. Twenty dollars a week gets you there in about a year. Add a
side gig weekend or sell a few things you don't use, and you could be there in a few months.""",
  "Selling items online", "BREAK IT INTO PIECES"),
4: ("""Then automate your bills too, at least the minimum payments. Late fees and missed payments are some of the most expensive
mistakes in your twenties, and they're almost always caused by forgetting, not by a lack of money.""",
  "Autopay bills screen", "AUTOMATE BILLS TOO"),
5: ("""Also check the vesting schedule. Some employers require you to stay a certain number of years before their contributions are
fully yours. And when you change jobs, roll your old account into an IRA or your new plan instead of cashing out, which can trigger
taxes and penalties.""",
  "Rollover paperwork", "NEVER CASH OUT"),
6: ("""The IRS sets a yearly contribution limit and income limits, which change over time, so check the current numbers. Even if you
can't contribute the maximum, regular contributions of fifty or one hundred dollars a month can grow into a meaningful tax free
balance over forty years.""",
  "IRS website limits", "CHECK THE LIMITS"),
7: ("""And once you've chosen, leave it alone. One of the most common mistakes young investors make is switching funds after a bad
month or chasing whatever went up last year. A simple fund held for decades usually beats constant tinkering.""",
  "Calm person ignoring phone", "THEN LEAVE IT ALONE"),
8: ("""While you pay down debt, stop adding to it. That might mean removing saved cards from shopping apps or leaving the card at
home for a while. And call your card company to ask for a lower rate. It doesn't always work, but it costs nothing to ask.""",
  "Scissors cutting credit card", "STOP ADDING TO IT"),
9: ("""Also make sure your contact information is up to date with your servicer, so you never miss an important notice. Missed
student loan payments can hurt your credit score and add fees. If you're struggling, contact your servicer before you fall behind,
not after.""",
  "Phone call customer service", "CALL BEFORE YOU FALL BEHIND"),
10: ("""Check your credit reports for free at the official annualcreditreport dot com website, and dispute any errors. Keep your
balances low compared to your limits. And avoid opening lots of new accounts at once, which can temporarily lower your score.""",
  "Credit report document", "CHECK YOUR REPORTS"),
11: ("""Remember that the payment isn't the full cost. Insurance for a new car, especially for a young driver, can be much higher.
Add gas, maintenance and registration, and the true monthly cost can be far above the loan payment. Run all the numbers before you
sign.""",
  "Car insurance bill", "THE FULL COST"),
12: ("""A common guideline is to keep rent under about thirty percent of your gross income, and lower is better while you're building.
On a forty five thousand dollar salary, thirty percent is about eleven hundred dollars a month. If rent in your area is higher,
roommates or a longer commute may be the trade off.""",
  "Rent calculator", "THE 30% GUIDELINE"),
13: ("""Start with meals you already like eating out. Burrito bowls, pasta, stir fry. Cook in batches on Sunday, so weeknight dinner is
already done. You don't need to give up restaurants. Just make them a choice instead of a default.""",
  "Meal prep containers", "BATCH COOK ON SUNDAY"),
14: ("""If you're under twenty six, you may be able to stay on a parent's health plan, under rules from the Affordable Care Act. If you
buy your own, the official healthcare dot gov marketplace may offer subsidies depending on your income. Check before you go
without.""",
  "Healthcare marketplace website", "CHECK YOUR OPTIONS"),
15: ("""Look for skills your industry clearly pays more for. Ask people a few years ahead of you what made the biggest difference in their
pay. Many employers offer tuition assistance or training budgets that go unused. Use them.""",
  "Mentor talking to young worker", "ASK WHAT PAYS"),
16: ("""Keep a simple file of your wins: projects finished, money saved, problems solved. When review time comes, you'll have evidence
instead of feelings. And practice the conversation out loud. It feels awkward at first, but it gets easier every time.""",
  "Notebook list of achievements", "KEEP A WINS FILE"),
17: ("""Here's what that looks like. You get a three thousand dollar raise. Fifteen hundred dollars a year goes to your retirement plan,
about one hundred twenty five a month. The other fifteen hundred makes your life better. Repeat that with every raise, and in ten
years your savings rate can be dramatically higher.""",
  "Raise letter", "$3,000 RAISE EXAMPLE"),
18: ("""To set one up, list your irregular expenses for the year, add them up, and divide by twelve. If they total twenty four hundred
dollars, you need two hundred a month. Many banks let you create several savings buckets inside one account for free.""",
  "Calculator annual expenses", "ADD, THEN DIVIDE BY 12"),
19: ("""And if your family never talked about money, you're not alone. Many people learn as adults. Books, podcasts and free resources
from the Consumer Financial Protection Bureau can fill the gaps. Curiosity about money is one of the best habits you can build.""",
  "Person reading finance book", "KEEP LEARNING"),
20: ("""Once a year, do a bigger review. Check your insurance, your beneficiaries, your credit reports and your overall goals. Write down
your net worth and compare it to last year. Watching that number grow, even slowly, is one of the best motivators there is.""",
  "Net worth chart yearly", "ONCE A YEAR, GO DEEPER"),
}

def move(n, title, sub, card_text, paras):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"MOVE {n}")
    for t, q, c in paras:
        sc(t, q, c)
    sc(*EXTRA[n])

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Your twenties are the most powerful money decade of your life, and almost nobody tells you
that while you're in them. Your income is probably at its lowest. Your bank account might be close to empty. But you
have something that people in their fifties would pay almost anything for. Time. Today, I'll show you twenty moves
that make the most of it.""")
short("Your 20s are the most powerful money decade of your life.")
sc("""Here's why your twenties matter so much. Money invested early has decades to compound. At a seven percent average
yearly return, a single dollar invested at twenty five could grow to roughly fifteen dollars by sixty five. The same dollar
invested at forty five might grow to about four. Same dollar, same market. Very different result.""",
   "Young adult looking at city", "ONE DOLLAR, FIFTEEN DOLLARS")
sc("""And the habits you build now tend to stick. How you handle your first paychecks, your first credit card and your
first raise often shapes how you handle money for the rest of your life. Get the patterns right now, and the next forty years
get much easier.""",
   "Habit tracker calendar", "HABITS STICK")
sc("""We'll look at this from three angles. First, the numbers: what starting in your twenties is really worth. Second, the
psychology: the traps that catch people in this decade. And third, the playbook: twenty specific moves, from your first
paycheck to your first investment account.""",
   "Three paths diverging", "THREE ANGLES")
pr("""Stick around for move fourteen. It's one most people in their twenties skip, and it can quietly protect everything else.
Let's start with the numbers.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Growth examples use stated math at a seven percent average yearly return, which is an illustration, not a promise. Debt
and credit information comes from the Federal Reserve and the Consumer Financial Protection Bureau. Retirement account rules
come from the IRS. Credit score information comes from FICO. This is education, not financial advice.""",
   "Federal Reserve building", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. What is starting in your twenties actually worth?""")
sc("""Let's meet two people. Ava starts investing two hundred dollars a month at twenty two. Ben waits until thirty two, when he
feels more settled, and then invests the same two hundred dollars a month. Both stop at sixty five. Both earn a seven percent
average yearly return.""",
   "Two young friends talking", "AVA AND BEN")
sc("""By sixty five, Ava could have roughly six hundred fifty five thousand dollars. Ben could have about three hundred nine
thousand. Ava invested only twenty four thousand dollars more than Ben over her lifetime, but she could end up with more than
double. Those ten extra years in her twenties are worth over three hundred thousand dollars.""",
   "Two different sized piles of money", "10 YEARS = $346K")
card("""Two hundred dollars a month at seven percent. Starting at twenty two versus starting at thirty two, both stopping at sixty
five.""",
     {"type": "compare", "left": {"label": "start at 22", "big": "~$655K", "sub": "$200 a month"},
      "right": {"label": "start at 32", "big": "~$309K", "sub": "$200 a month"},
      "note": "Illustration at 7% a year. Returns are not guaranteed."})
sc("""To catch up, Ben would need to invest about four hundred twenty five dollars a month from thirty two, more than twice as
much, to reach roughly the same place. That's the real cost of waiting. It doesn't just delay your wealth. It makes every
future dollar work less.""",
   "Person running to catch bus", "CATCHING UP COSTS 2X")
sc("""And even small amounts matter. One hundred dollars a month from twenty two to sixty five, at seven percent, could grow to
about three hundred twenty seven thousand dollars. That's from around fifty two thousand dollars contributed. If a hundred
dollars is all you can do now, it's still one of the best investments of your life.""",
   "Hundred dollar bill", "$100 A MONTH COUNTS")
card("""One hundred dollars a month, invested at seven percent a year from age twenty two to sixty five.""",
     {"type": "growth", "monthly": 100, "rate": 0.07, "years": 43})
sc("""Now the other side of the numbers: debt. Debt in your twenties compounds too, just in the wrong direction. According to
the Federal Reserve, credit card interest rates have often averaged above twenty percent in recent years. A two thousand
dollar balance paid at minimums can take many years and cost more than the original purchase in interest.""",
   "Credit card statement interest", "DEBT COMPOUNDS TOO")
sc("""Student loans are another big number for many people in their twenties. A thirty thousand dollar loan at six percent over
ten years means a payment of about three hundred thirty dollars a month. That's real money, and it's why your twenties plan
has to balance paying down debt with starting to invest.""",
   "Student loan statement", "$30K LOAN = ~$333 A MONTH")
sc("""The good news is that your twenties also often bring the fastest income growth of your career. Many people see their pay
rise significantly in their first ten years of work as they gain skills and change jobs. If you capture part of that growth
for saving, your savings rate can climb quickly.""",
   "Young professional promotion", "FASTEST INCOME GROWTH")
pr("""So the numbers say start early, avoid expensive debt, and capture your raises. Why is that so hard in practice? Angle
two.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
pr("""Angle two. The psychology. Five traps that catch people in their twenties.""")
short("5 money traps that catch almost everyone in their 20s")
sc("""Trap one. I'll start when I earn more. It feels logical. Why invest fifty dollars when you could wait and invest five
hundred later? But as we just saw, those early dollars have the most time to grow. And people who wait for the perfect income
often find their spending rises with their pay, so the right time never seems to come.""",
   "Person waiting at clock", "TRAP 1: LATER")
sc("""Trap two. Keeping up with your friends. Your twenties are full of weddings, trips, dinners and concerts. Social media
shows you everyone's highlights. It's easy to spend to stay included. But you only see their spending, never their credit card
statements. Many of them are just as stressed as you.""",
   "Friends on expensive trip", "TRAP 2: KEEPING UP")
sc("""Trap three. The first real paycheck upgrade. After years as a student, your first salary feels enormous. The temptation is
to upgrade everything at once: a new car, a nicer apartment, new furniture, new clothes. Each upgrade feels deserved. Together,
they can lock in high fixed costs before you've built any cushion.""",
   "New apartment furniture shopping", "TRAP 3: UPGRADE EVERYTHING")
sc("""Trap four. Thinking investing is gambling. Many people in their twenties grew up watching crashes, scams and crypto booms
and busts. So they keep everything in a checking account, which feels safe. But over decades, cash loses buying power to
inflation. Diversified, long term investing in low cost funds is very different from betting on a single hot stock.""",
   "Casino versus index chart", "TRAP 4: INVESTING IS GAMBLING")
sc("""And trap five. Thinking it's too late, or too early. Some twenty somethings feel they're already behind because they see
people their age with big portfolios online. Others feel retirement is so far away that it doesn't matter yet. Both feelings
lead to the same place: doing nothing. And doing nothing is the most expensive choice.""",
   "Confused young person", "TRAP 5: TOO LATE OR TOO EARLY")

ch("The mindset that works")
sc("""So what mindset works? Think of your twenties as building the machine. You're not trying to get rich in this decade. You're
building the systems that will make you wealthy later: automatic savings, low fixed costs, a growing income, good credit, and
the habit of investing every month.""",
   "Machine gears building", "BUILD THE MACHINE")
sc("""Another helpful idea is to give your future self a seat at the table. Before a big purchase, ask: would forty year old me
be glad I did this? Sometimes the answer is yes. A trip with friends, a course that boosts your career. Sometimes it's no. That
simple question can save you thousands.""",
   "Older and younger self", "ASK YOUR FUTURE SELF")
sc("""And finally, give yourself room to make small mistakes. Your twenties are when mistakes are cheapest. Overspending on one
trip, picking a slightly wrong fund, or paying a late fee once won't ruin you. What matters is the overall direction, and
learning fast.""",
   "Young person learning", "SMALL MISTAKES ARE CHEAP")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
pr("""Angle three. The playbook. Twenty moves for your twenties. You don't need to do them all at once. Pick a few each year.""")
short("20 money moves to make in your 20s")

move(1, "Know where your money goes", "track one month",
"""Move one. Know where your money goes.""",
[("""Track every dollar for one month. Use your bank app, a spreadsheet, or a notebook. Don't change anything yet. Just watch.
Most people are surprised by at least one category, often food delivery, subscriptions or rideshares.""",
  "Phone banking app", "TRACK ONE MONTH")])

move(2, "Open a high yield savings account", "your money's home base",
"""Move two. Open a high yield savings account.""",
[("""Many traditional banks pay very little interest on savings. Online banks and credit unions often pay much more, and FDIC or
NCUA insured accounts protect deposits up to legal limits. It takes about ten minutes and gives your savings a better home.""",
  "Savings account online", "A BETTER HOME FOR SAVINGS")])

move(3, "Build a starter emergency fund", "$1,000 first",
"""Move three. Build a starter emergency fund.""",
[("""Save one thousand dollars as fast as you can. A car repair, a vet bill or a lost shift won't become credit card debt. This
small cushion changes how you feel about money almost immediately.""",
  "Emergency fund jar", "$1,000 FIRST")])

move(4, "Automate your savings", "pay yourself first",
"""Move four. Automate your savings.""",
[("""Set up an automatic transfer from checking to savings on payday. Start with whatever you can, even twenty five dollars. When
saving happens before you see the money, you don't have to rely on willpower.""",
  "Automatic transfer setup", "PAY YOURSELF FIRST")])

move(5, "Take the full employer match", "free money",
"""Move five. Take the full employer match.""",
[("""If your job offers a retirement plan with a match, contribute at least enough to get all of it. Many plans now enroll new
employees automatically, but often at a low rate. Check yours. A match is an instant return you won't find anywhere else.""",
  "401k enrollment form", "DON'T LEAVE IT ON THE TABLE")])

move(6, "Open a Roth IRA", "tax free growth",
"""Move six. Open a Roth IRA.""",
[("""If you qualify under IRS income limits, a Roth IRA lets your investments grow tax free, and qualified withdrawals in
retirement are tax free too. For many people in their twenties, whose tax rates are relatively low, this is a powerful account.
You can also withdraw your contributions, though not the earnings, without penalty, which adds flexibility.""",
  "Roth IRA account", "TAX FREE GROWTH")])

move(7, "Pick simple, low cost funds", "boring is good",
"""Move seven. Pick simple, low cost funds.""",
[("""Broad index funds or a single target date fund are a simple way to start. Look at the expense ratio, the yearly fee. A fund
charging point one percent instead of one percent can leave you with tens of thousands of dollars more over a lifetime. Boring
and cheap is often best.""",
  "Index fund fees comparison", "BORING AND CHEAP")])

move(8, "Attack high interest debt", "highest rate first",
"""Move eight. Attack high interest debt.""",
[("""List your debts by interest rate. Pay minimums on all of them and send extra money to the highest rate first. Credit cards
usually come first. Every card you pay off is a guaranteed return equal to its interest rate.""",
  "Debt list highest rate", "HIGHEST RATE FIRST")])

move(9, "Make a student loan plan", "know your options",
"""Move nine. Make a student loan plan.""",
[("""Know every loan, its rate and its servicer. Federal loans may offer income driven repayment plans and, for some public
service workers, forgiveness programs. Check the official studentaid dot gov site for current rules. Pay higher rate loans
faster, and be careful about refinancing federal loans into private ones, because you can lose federal protections.""",
  "Student loan paperwork", "KNOW YOUR OPTIONS")])

move(10, "Build your credit on purpose", "it's a long game",
"""Move ten. Build your credit on purpose.""",
[("""According to FICO, payment history and the amount you owe are the biggest parts of your credit score. Use one card for
small regular purchases, pay it in full every month, and keep your oldest account open. Good credit can save you thousands on
car loans, mortgages and even insurance in some states.""",
  "Credit score dial", "PAY IN FULL, ON TIME")])

# ---------------- Mid ----------------
ch("A quick favor")
pr("""Quick pause. If you're in your twenties, or you know someone who is, subscribe to the channel. It's free, it helps the
channel grow, and every week I'll help you build the machine. Now, moves eleven to twenty.""")

move(11, "Keep your car cheap", "the biggest twenties trap",
"""Move eleven. Keep your car cheap.""",
[("""A car is often the biggest financial mistake people make in their twenties. A large monthly payment on a new car can eat
the money that could have started your investments. A reliable used car, bought with cash or a short loan, keeps your options
open.""",
  "Reliable used car", "BUY RELIABLE, NOT FLASHY")])

move(12, "Keep housing reasonable", "roommates are a superpower",
"""Move twelve. Keep housing reasonable.""",
[("""Housing is usually your biggest expense. A roommate, a smaller place or living a bit farther from the center can free up
hundreds of dollars a month. In your twenties, that money invested has decades to grow. Many people look back on their
roommate years as some of their best.""",
  "Roommates apartment", "ROOMMATES ARE A SUPERPOWER")])

move(13, "Learn to cook ten meals", "a skill that pays forever",
"""Move thirteen. Learn to cook ten meals.""",
[("""Food is one of the easiest places to overspend in your twenties, especially with delivery apps. Learning ten simple meals you
enjoy can cut your food bill significantly, improve your health, and save money for the rest of your life.""",
  "Cooking simple meal", "TEN MEALS")])

move(14, "Get the right insurance", "protect the machine",
"""Move fourteen. Get the right insurance.""",
[("""Here's the one most people skip. Have health insurance, even a basic plan, because a single hospital visit can create huge
debt. If you rent, renters insurance is often inexpensive and protects your belongings. And if your employer offers disability
insurance, consider it, because your ability to earn is your biggest asset in your twenties.""",
  "Insurance card", "PROTECT YOUR EARNING POWER")])

move(15, "Invest in your skills", "the highest return",
"""Move fifteen. Invest in your skills.""",
[("""In your twenties, the highest return investment is often you. A certification, a new skill, a course, or a mentor can raise
your income for decades. A raise of five thousand dollars a year, kept for forty years, is worth far more than almost any stock
pick.""",
  "Studying certification course", "INVEST IN YOU")])

move(16, "Negotiate your pay", "every job, every time",
"""Move sixteen. Negotiate your pay.""",
[("""Research typical pay for your role using sources like the BLS and salary sites. When you get an offer, ask politely for more,
with evidence. Every raise compounds into future raises and retirement contributions. Changing jobs every few years early in
your career can also bring larger increases.""",
  "Job offer negotiation", "ASK FOR MORE")])

move(17, "Use the raise rule", "half to future you",
"""Move seventeen. Use the raise rule.""",
[("""Every time you get a raise, send at least half of it to savings and investing, automatically. The other half improves your
life. This way, your lifestyle grows, but your savings rate grows faster.""",
  "Split jar raise", "HALF OF EVERY RAISE")])

move(18, "Start a sinking fund system", "no more surprise bills",
"""Move eighteen. Start a sinking fund system.""",
[("""Car repairs, holidays, weddings, annual subscriptions. These aren't surprises, they're just irregular. Set aside a small amount
each month for each one in separate savings buckets. When the bill arrives, the money is waiting.""",
  "Labeled savings buckets", "NO MORE SURPRISES")])

move(19, "Talk about money", "with partners and friends",
"""Move nineteen. Talk about money.""",
[("""If you're in a serious relationship, talk about money early: debts, goals, spending styles. Money conflicts are a common source
of stress for couples. And find at least one friend who's also working on their finances. Good habits spread.""",
  "Couple talking over coffee", "TALK ABOUT IT")])

move(20, "Review once a quarter", "fifteen minutes",
"""Move twenty. Review once a quarter.""",
[("""Every three months, spend fifteen minutes checking your savings, debts, net worth and contributions. Raise your retirement
contribution by one percent if you can. These small check ins keep you on course without obsessing over daily market moves.""",
  "Calendar quarterly review", "15 MINUTES A QUARTER")])

# ---------------- Order ----------------
ch("What order to do it in")
sc("""Twenty moves can feel like a lot, so here's a simple order. First year: moves one through five. Track your money, open a
high yield account, build one thousand dollars, automate it, and take the full match. These are the foundations.""",
   "Foundation of house", "YEAR ONE: FOUNDATIONS")
sc("""Years two and three: moves six through ten. Open a Roth IRA, choose simple funds, attack high interest debt, make a student
loan plan, and build your credit. This is when you go from not losing ground to actually building.""",
   "Building frame house", "YEARS 2 AND 3: BUILDING")
sc("""And throughout your twenties: moves eleven to twenty. Keep your car and housing reasonable, learn to cook, protect yourself
with insurance, invest in skills, negotiate pay, use the raise rule, set up sinking funds, talk about money, and review every
quarter. These are the habits that carry the plan.""",
   "Completed house", "ALWAYS: THE HABITS")
card("""Year one: foundations. Years two and three: start building. All decade: the habits that carry the plan.""",
     {"type": "stat", "label": "your twenties plan", "big": "BUILD THE MACHINE", "size": 120, "sub": "foundations, then building, then habits"})

ch("What a good twenties looks like")
sc("""So what does a good financial twenties look like by the end? Here's a realistic target many people can work toward by
thirty. Three to six months of expenses in an emergency fund. No credit card debt. A plan for student loans. A good credit score.
And retirement savings equal to about one year of your salary, a rough benchmark used by firms like Fidelity.""",
   "Thirtieth birthday cake", "A TARGET FOR 30")
sc("""If you don't hit all of those by thirty, that's okay. They're guidelines, not a test. Someone who starts at twenty seven with
student loans may be behind on savings but making great progress. What matters most is that the machine is built and running.""",
   "Progress bar partially filled", "PROGRESS, NOT PERFECTION")

# ---------------- Stories ----------------
ch("Three twenty somethings")
short("Three people in their 20s. Three very different results.")
sc("""Let's meet three people. Jordan earns forty two thousand dollars at twenty three. He lives with two roommates, drives a
ten year old car, takes the full match, and opens a Roth IRA with one hundred dollars a month. It doesn't feel like much. He
sometimes wonders if it's worth it.""",
   "Young man roommates", "JORDAN: SMALL START")
sc("""Priya earns fifty five thousand dollars at twenty four. She buys a new car with a six hundred dollar payment, moves into a
nice apartment alone, and puts trips on credit cards. She's having fun. She plans to get serious at thirty.""",
   "Young woman new car", "PRIYA: LATER")
sc("""And Marcus earns thirty eight thousand dollars at twenty five with twenty five thousand dollars in student loans. He builds a
starter fund, signs up for the match, and takes a weekend certification that bumps his pay. He uses the raise rule every year.""",
   "Young man studying", "MARCUS: SKILLS")
sc("""By thirty, Jordan has a growing portfolio and no debt beyond a small car loan he paid off early. Marcus has cleared his
highest rate loans, earns noticeably more, and has a real emergency fund. Priya has a higher salary than both of them, but
she has credit card debt, a car worth less than she owes, and almost no savings.""",
   "Three paths outcome", "AT THIRTY")
sc("""Priya isn't a bad person. She did what felt normal. And she can absolutely turn things around in her thirties. But she'll be
starting from behind, while Jordan and Marcus have a machine that's already running. That's the quiet power of your twenties.""",
   "Determined woman planning", "SHE CAN STILL TURN IT AROUND")

# ---------------- History ----------------
ch("Why it's different for this generation")
sc("""It's worth acknowledging that people in their twenties today face real challenges. Housing costs in many cities have risen
faster than wages. Student debt is much higher than it was for earlier generations. And many jobs no longer offer traditional
pensions, which once provided retirement income automatically.""",
   "Expensive city apartments", "REAL CHALLENGES")
sc("""But there are real advantages too. Earlier generations often paid high commissions to buy stocks. Today, many brokers offer
commission free trades, and broad index funds can cost a tiny fraction of a percent a year. You can open an account from your
phone in minutes. Automatic enrollment in workplace plans has become more common.""",
   "Smartphone investing app", "REAL ADVANTAGES")
sc("""So the playing field has changed in both directions. Housing and education cost more. Investing costs much less. That's why
the moves in this video focus on keeping big fixed costs low and getting your money invested early and cheaply. You can't
control rent prices. You can control your savings rate and your fees.""",
   "Balance scale", "CONTROL WHAT YOU CAN")

# ---------------- First paycheck ----------------
ch("Your first paycheck, step by step")
pr("""Let's make this concrete. Here's what to do with your very first full time paycheck, step by step.""")
sc("""Say you earn forty five thousand dollars a year and you're paid every two weeks. Your gross pay is about seventeen hundred
thirty dollars per paycheck. After federal and state taxes, Social Security, Medicare, health insurance and a five percent 401k
contribution, your take home pay might be around thirteen hundred dollars. Your exact number will depend on your state and
benefits.""",
   "First paycheck stub", "~$1,300 TAKE HOME")
sc("""Before that money hits your account, the five percent is already invested, and if your employer matches it, you're
investing even more. That's the best part of the paycheck, and you didn't have to do anything after the first setup.""",
   "Retirement contribution line", "ALREADY INVESTED")
sc("""When the paycheck arrives, an automatic transfer of one hundred dollars goes to your high yield savings account. Then your
fixed bills come out: half of your rent, your phone, a share of utilities, a student loan payment. What's left covers groceries,
transport and fun until the next payday.""",
   "Money flowing to accounts", "SAVINGS FIRST, THEN BILLS")
sc("""Two paychecks a month cover your regular budget. And here's a bonus. In most years, being paid every two weeks gives you
twenty six paychecks, which means two months have a third paycheck. Many people send those extra paychecks straight to their
emergency fund or debt. That's two bonus paychecks a year, without a raise.""",
   "Calendar with three paydays", "THE THIRD PAYCHECK BONUS")

# ---------------- Side income ----------------
ch("Side income in your twenties")
sc("""Your twenties are often the best time to experiment with side income. You may have more free time and energy, and fewer
responsibilities. Tutoring, freelancing, pet sitting, delivery, selling crafts, or building a small online business can add a
few hundred dollars a month.""",
   "Young person freelancing laptop", "EXPERIMENT NOW")
sc("""The key is where that money goes. If side income disappears into lifestyle, it doesn't change your future. If it goes to
your emergency fund, your debt or a Roth IRA, it can speed up your plan by years. Three hundred dollars a month of side income,
invested for ten years at seven percent, could grow to about fifty two thousand dollars.""",
   "Side income jar", "$300 A MONTH, 10 YEARS = ~$52K")
sc("""And remember taxes. Side income is usually taxable, and if you're self employed, you may owe self employment tax and need to
make estimated quarterly payments. Set aside a portion of what you earn for taxes, and check the IRS guidance for gig workers.""",
   "Tax forms self employed", "SET ASIDE FOR TAXES")

# ---------------- Mental health ----------------
ch("Money stress in your twenties")
sc("""Money stress is common in your twenties. Surveys from the American Psychological Association have found that money is one of
the most frequently reported sources of stress for adults, and younger adults often report it most. If money keeps you up at night,
you're far from alone.""",
   "Stressed young adult at night", "YOU'RE NOT ALONE")
sc("""The good news is that small actions often reduce stress faster than big ones. Building the first five hundred dollars of
savings, setting up autopay so you never miss a bill, or making a written plan for your debts can create a real sense of control,
long before the numbers look impressive.""",
   "Relieved person writing plan", "SMALL ACTIONS, LESS STRESS")
sc("""And be kind to yourself about the past. Maybe you ran up a credit card in college or spent your first bonus on a trip.
That's done. What matters is the next paycheck. Your twenties give you time to recover from almost any money mistake, as long as
you start building now.""",
   "Fresh start sunrise", "THE NEXT PAYCHECK MATTERS")

# ---------------- Late twenties ----------------
ch("Starting at 27, 28 or 29?")
sc("""If you're watching this near the end of your twenties with little saved, don't tune out. You still have more than thirty five
years until a traditional retirement age. Two hundred fifty dollars a month from twenty eight to sixty five, at seven percent,
could still grow to over half a million dollars.""",
   "Person in late twenties determined", "STILL 35+ YEARS")
sc("""Your advantage now is that your income is probably higher than it was at twenty two. That means you can often save a larger
share and catch up faster. Focus on moves three, five, six, eight and seventeen first: the cushion, the match, the Roth IRA, high
interest debt and the raise rule.""",
   "Focused priority list", "FOCUS ON FIVE MOVES")
sc("""And avoid the trap of trying to make up for lost time with risky bets. Catching up is done with a higher savings rate and
consistency, not by gambling on a single stock or coin. Slow and steady still works, and it works better the sooner you begin.""",
   "Tortoise on path", "NO CATCH UP GAMBLING")

ch("A look ahead to your thirties")
sc("""Finally, here's why all of this matters for the next decade. Your thirties often bring bigger decisions: marriage or
partnership, children, buying a home, career changes. Each of those is much easier with an emergency fund, good credit and a
retirement account that's already growing.""",
   "Couple looking at house", "YOUR THIRTIES ARE COMING")
sc("""Good credit can mean a lower mortgage rate. An emergency fund can make a career change possible. Retirement savings already
compounding can give you room to save less for a few years when childcare costs are high. The machine you build in your twenties
gives you options in your thirties. And options are what financial freedom really feels like.""",
   "Open doors choices", "OPTIONS ARE FREEDOM")

# ---------------- FAQ ----------------
ch("Questions people ask")
pr("""Let me answer the questions I hear most from people in their twenties.""")
sc("""Question one. Should I pay off student loans or invest? Many people do both. Take the full match first, because it's free
money. Then compare your loan rates. High rate loans, often above seven or eight percent, usually deserve extra payments. Low rate
loans can be paid on schedule while you invest. And always check your federal loan options first.""",
   "Scale loans versus investing", "LOANS OR INVEST?")
sc("""Question two. Should I buy a house in my twenties? It can make sense if you plan to stay put for many years, have a solid
emergency fund, and the full cost of owning fits your budget. But there's no rush. Renting while you build savings, credit and
career flexibility is often a smart choice in your twenties.""",
   "First home keys", "BUY A HOUSE?")
sc("""Question three. What about crypto and individual stocks? If you're curious, many planners suggest keeping speculative
investments to a small share of your portfolio, money you could lose without hurting your plan. The core should be diversified,
low cost funds. Don't let a speculative bet replace your foundations.""",
   "Crypto coins and charts", "CRYPTO AND STOCKS?")
sc("""Question four. How much should I have saved by thirty? A rough guideline used by some firms is about one times your salary in
retirement savings by thirty. But don't panic if you're not there. Many people start late in their twenties. The moves in this
video can get you on track in your thirties.""",
   "Milestone flag", "HOW MUCH BY 30?")
sc("""And question five. Is it okay to spend money on fun? Absolutely. Your twenties should include experiences, friendships and
adventure. The goal isn't to spend nothing. It's to spend on purpose, with your future self funded first. A budget with real fun
money is one you'll actually stick to.""",
   "Friends hiking adventure", "FUN IS ALLOWED")

sc("""Question six. Should I live with my parents to save money? If it works for your family, it can be one of the most
powerful money moves available. Saving even a few hundred dollars a month in rent, for a year or two, can clear debt or build a
full emergency fund. Agree on clear expectations, contribute something to the household, and have a plan for what you'll do with
the money you save.""",
   "Young adult family home dinner", "LIVING AT HOME?")
sc("""And question seven. What's the single most important move? If I had to pick one, it would be automating your investing
early, even with a small amount. It builds the habit, starts the compounding clock, and keeps going on the days when you're busy,
tired or unmotivated. Everything else can be added over time.""",
   "Automatic investing app", "THE ONE MOVE")

sc("""One last thought before the recap. The people who do best with money in their twenties usually aren't the ones who know
the most. They're the ones who start, keep it simple, and don't stop. You don't need to understand every account or every fund
today. You just need to take the next step.""",
   "Young person taking step forward", "JUST TAKE THE NEXT STEP")

# ---------------- Recap ----------------
ch("Recap: 20 moves")
short("Your 20s money checklist in 60 seconds")
sc("""Quick recap. Starting at twenty two instead of thirty two could more than double what you have at sixty five. The traps: waiting
for more income, keeping up with friends, upgrading everything, fearing investing, and feeling too early or too late.""",
   "Checklist clipboard", "THE NUMBERS AND TRAPS")
sc("""The twenty moves. Track your money. Open a high yield account. Build one thousand dollars. Automate. Take the match. Open a Roth
IRA. Choose low cost funds. Attack high interest debt. Plan your student loans. Build credit.""",
   "First ten moves list", "MOVES 1 TO 10")
sc("""Keep your car cheap. Keep housing reasonable. Learn ten meals. Get the right insurance. Invest in your skills. Negotiate your pay.
Use the raise rule. Start sinking funds. Talk about money. And review once a quarter.""",
   "Second ten moves list", "MOVES 11 TO 20")

# ---------------- Close ----------------
ch("What to do next")
pr("""Pick three moves and do them this week. If you're not sure where to start, start with one, five and six. And if you're in
your thirties, I made a full plan for you too. It's linked right here. I'm Ryan Rover. See you in the next one.""")

save("video54", "Your 20s Money Plan: 20 Moves That Matter", [
    "Growth figures: stated illustrative math at a 7% average yearly return",
    "Federal Reserve, G.19 Consumer Credit (credit card interest rates)",
    "Consumer Financial Protection Bureau, credit card and student loan guides",
    "Federal Student Aid (studentaid.gov), repayment and forgiveness programs",
    "IRS, 401(k) and Roth IRA rules and income limits",
    "FICO, What's in my FICO Scores",
    "Fidelity, retirement savings guidelines by age",
    "U.S. Bureau of Labor Statistics, Occupational Employment and Wage Statistics",
], "your 20s money plan: numbers, psychology, playbook")
