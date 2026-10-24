import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

def step(n, title, sub, card_text, paras):
    ch(f"Step {n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"STEP {n}")
    for t, q, c in paras:
        sc(t, q, c)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Most money advice online seems written for people who already have money. Invest your
bonus. Max out every account. Buy a rental property. But what if you earn an ordinary salary? Sixty thousand dollars
a year, a regular job, regular bills. Can you still build real wealth? The answer is yes. And today, I'll show you the
full plan, step by step.""")
short("You can build real wealth on an average salary. Here's how.")
card("""The typical full time worker in America earns around sixty thousand dollars a year, according to Bureau of Labor
Statistics data on median weekly earnings.""",
     {"type": "stat", "label": "a typical full time salary", "big": "~$60,000", "sub": "a year, based on BLS median weekly earnings"})
sc("""Here's the most encouraging fact in personal finance. Many of the people who end up with significant wealth didn't
have extraordinary salaries. They had ordinary salaries, and extraordinary consistency. Teachers, nurses, mechanics,
office managers, electricians. People who spent a little less than they earned, invested the difference, and gave it
decades.""",
   "Teacher nurse electrician workers", "ORDINARY SALARIES")
sc("""We'll look at this from three angles. First, the numbers: what an average salary can realistically build, with
simple math. Second, the psychology: the mindset shifts that matter more than income. And third, the playbook: a
twelve step plan, in order, with a sample budget you can copy.""",
   "Blueprint plan on desk", "THREE ANGLES")
pr("""Stay for the sample budget near the end. It shows exactly where every dollar of a sixty thousand dollar salary can go.
Let's start with the numbers.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Every number here is either from a named source or simple stated math. Earnings data comes from the Bureau of Labor
Statistics. Spending data comes from the BLS Consumer Expenditure Survey. Retirement account rules come from the IRS.
Growth examples use a seven percent average yearly return, which is an illustration, not a promise. Taxes vary by state
and situation. This is education, not financial advice.""",
   "Bureau of Labor Statistics building", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. What can an average salary actually build?""")
sc("""Let's start with take home pay. On a sixty thousand dollar salary, after federal income tax, Social Security, Medicare
and typical state taxes, take home pay might be roughly four thousand dollars a month, depending on where you live and your
deductions. That's the money you actually have to work with.""",
   "Paycheck stub", "~$4,000 A MONTH TAKE HOME")
sc("""Now, a common recommendation from retirement planners is to save around fifteen percent of your gross income for
retirement, including any employer match. On sixty thousand dollars, that's nine thousand dollars a year, or seven hundred
fifty dollars a month.""",
   "Fifteen percent sign", "15% = $750 A MONTH")
sc("""If your employer matches, say, four percent of your pay, that's two hundred dollars a month of the seven hundred fifty
coming from your employer. Your own share would be five hundred fifty dollars a month. And because 401k contributions are
often made before taxes, your take home pay drops by less than the full amount.""",
   "Employer match illustration", "THE MATCH HELPS")
sc("""So what can seven hundred fifty dollars a month become? At a seven percent average yearly return, over thirty five
years, it could grow to roughly one point three five million dollars. That's from a total of about three hundred fifteen
thousand dollars contributed. On an ordinary salary.""",
   "Growth chart rising", "~$1.35 MILLION IN 35 YEARS")
card("""Seven hundred fifty dollars a month, about fifteen percent of a sixty thousand dollar salary, invested at seven percent a
year for thirty five years.""",
     {"type": "growth", "monthly": 750, "rate": 0.07, "years": 35})
sc("""And that assumes your salary never grows. In reality, most people's pay rises over a career. If your salary grows by three
percent a year and you keep saving fifteen percent, the same math could lead to around one point nine million dollars after
thirty five years, in future dollars. Inflation means that money will buy less than it would today, but it's still a
very strong position.""",
   "Career progression stairs", "WITH RAISES: ~$1.9 MILLION")
sc("""Now compare that with saving a smaller amount. Three hundred dollars a month, five to six percent of the salary, for thirty
five years at seven percent, could grow to about five hundred forty thousand dollars. Still meaningful. But the gap between
six percent and fifteen percent is close to a million dollars.""",
   "Two stacks of coins", "6% VS 15%")
card("""Thirty five years at seven percent. Saving about six percent versus fifteen percent of a sixty thousand dollar salary.""",
     {"type": "compare", "left": {"label": "$300 a month", "big": "~$540K", "sub": "about 6% saved"},
      "right": {"label": "$750 a month", "big": "~$1.35M", "sub": "about 15% saved"},
      "note": "Illustration. Returns are not guaranteed."})
sc("""Here's what these numbers tell us. On an average salary, wealth is mostly a function of three things: the share you save,
how early you start, and how long you keep going without interruption. Income helps. But the savings rate and time do the
heavy lifting.""",
   "Three gears turning", "RATE, START, TIME")
sc("""Where does the money usually go instead? According to the BLS Consumer Expenditure Survey, housing, transportation and
food make up the biggest share of most budgets, together around six of every ten dollars spent. That's where an average
earner has the most room to create a savings gap, not in skipping coffee.""",
   "House car groceries", "THE BIG THREE")
pr("""So the math says it's possible. Why doesn't it happen more often? That's angle two.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
pr("""Angle two. The psychology. Six mindset shifts that matter more than salary.""")
short("The mindset that lets ordinary earners become millionaires")
sc("""Shift one. From I don't earn enough, to I can start with what I earn. The belief that wealth requires a big salary is one
of the most expensive beliefs there is, because it delays everything. Many people with average incomes build wealth. Many
people with high incomes don't. The difference is behavior.""",
   "Person changing mindset", "SHIFT 1: START NOW")
sc("""The proof is everywhere once you look. Thomas Stanley's research on millionaires found many were teachers, small business
owners, engineers and other ordinary professionals who lived below their means. And retirement plan providers like Fidelity
report hundreds of thousands of 401k millionaires, many of them regular workers who contributed steadily for decades.""",
   "Ordinary workers group", "THE PROOF")
sc("""Shift two. From budget as restriction, to budget as permission. A budget isn't about saying no to everything. It's about
saying yes to what matters, on purpose. When you know your future is funded first, you can spend the rest without guilt.
Many people find they enjoy money more with a plan than without one.""",
   "Happy person shopping planned", "SHIFT 2: PERMISSION")
sc("""Shift three. From comparison, to your own scoreboard. On an average salary, you will see people around you with bigger
houses, newer cars and fancier trips. Some of them earn more. Many of them owe more. If you measure yourself against their
lifestyle, you'll always feel behind. Measure your savings rate instead.""",
   "Scoreboard personal", "SHIFT 3: YOUR SCOREBOARD")
sc("""Shift four. From perfect, to consistent. You don't need the perfect fund, the perfect budget, or the perfect moment.
You need a decent plan you'll follow for thirty years. A simple index fund you hold for decades beats a brilliant
strategy you abandon after two bad years.""",
   "Steady walking path", "SHIFT 4: CONSISTENT")
sc("""Shift five. From big wins, to big leaks. Average earners often look for a big win to change their situation, like a
hot stock or a side hustle that explodes. But the bigger opportunity is usually plugging big leaks: an oversized car
payment, a too expensive apartment, high interest debt. One fixed leak can be worth more than a lucky win, and it's far
more reliable.""",
   "Plugging a leak pipe", "SHIFT 5: FIX LEAKS")
sc("""And shift six. From someday, to automatic. Someday I'll start investing. Someday I'll fix my budget. Someday never
arrives. Automation turns someday into every payday. Once it's set up, you don't need motivation. The system does it for
you.""",
   "Calendar someday crossed out", "SHIFT 6: AUTOMATIC")

ch("Why average earners have an advantage")
sc("""Here's something surprising. In some ways, average earners have an advantage. High earners often face intense lifestyle
pressure from their peer groups. Doctors, lawyers and executives are expected to live in certain neighborhoods and drive
certain cars. Many start their careers late, with large student loans. Their high income can come with high fixed costs.""",
   "Doctor in expensive car", "HIGH EARNER PRESSURE")
sc("""An average earner who starts investing at twenty three, with modest fixed costs and no pressure to look rich, can quietly
build a large portfolio while higher earners are still paying off loans and upgrades. Time in the market is one of the few
things money can't buy back, and average earners often have more of it.""",
   "Young worker starting early", "TIME IS THE ADVANTAGE")

sc("""There's one more quiet advantage. When your lifestyle is built on an average salary, it's cheaper to maintain in
retirement. Someone used to spending one hundred fifty thousand dollars a year needs a huge portfolio to keep that up. Someone
comfortable on fifty thousand a year needs far less. A modest lifestyle isn't just cheaper today. It makes financial
independence reachable sooner.""",
   "Cozy modest home porch", "A CHEAPER FINISH LINE")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
pr("""Angle three. The twelve step plan. Follow it roughly in order. Each step makes the next one easier.""")
short("The 12-step plan to build wealth on a normal income")

step(1, "Know your numbers", "income, spending, debt",
"""Step one. Know your numbers.""",
[("""Write down your monthly take home pay, your average spending over the last three months, every debt with its interest
rate, and what you have in savings and investments. This takes about an hour. It's the foundation of everything else.""",
  "Laptop with spreadsheet", "ONE HOUR, ONE PAGE"),
 ("""Then calculate your current savings rate. If it's zero or negative, that's your starting point, not a judgment. Many
people who now have significant wealth started exactly there.""",
  "Starting line track", "YOUR STARTING POINT")])

step(2, "Build a starter cushion", "$1,000 or one month",
"""Step two. Build a starter cushion.""",
[("""Save one thousand dollars, or one month of essential expenses, in a separate high yield savings account. This stops new
emergencies from becoming new debt. Automate a transfer on payday, even if it's small.""",
  "Savings account app", "BREAK THE DEBT LOOP"),
 ("""If it feels slow, speed it up with a one time push. Sell things you don't use, take an extra shift, or put a tax refund
straight into it. Most people can finish this step within a few months.""",
  "Selling items garage sale", "A ONE TIME PUSH")])

step(3, "Get the full match", "never leave pay on the table",
"""Step three. Get the full employer match.""",
[("""If your employer offers a retirement plan match, contribute at least enough to get all of it. A match is part of your
compensation. Not taking it is like turning down a raise. On a sixty thousand dollar salary, a four percent match is two
thousand four hundred dollars a year.""",
  "401k match form", "$2,400 A YEAR IN MATCH"),
 ("""Check your plan's vesting schedule too, which tells you how long you need to stay to keep the employer's contributions.
And if your employer doesn't offer a plan, an IRA is the next best place to start.""",
  "Vesting schedule document", "CHECK VESTING")])

step(4, "Kill high interest debt", "anything above about 8%",
"""Step four. Kill high interest debt.""",
[("""List every debt above roughly eight percent interest, especially credit cards. Pay minimums on all of them, and send
every extra dollar to the highest rate first. Paying off a card at twenty two percent is a guaranteed twenty two percent
return.""",
  "Credit card debt payoff", "HIGHEST RATE FIRST"),
 ("""When one is paid off, roll that payment into the next. You're already used to living without that money, so the
momentum builds. Many people clear thousands of dollars of debt within a year or two this way.""",
  "Snowball rolling downhill", "ROLL THE PAYMENT")])

step(5, "Right size the big three", "housing, car, food",
"""Step five. Right size the big three.""",
[("""Look at housing, transportation and food. Many planners suggest keeping housing around a quarter to under a third of gross
income. On sixty thousand dollars, that's roughly twelve hundred fifty to sixteen hundred dollars a month. Cars, including
insurance and gas, ideally well under fifteen percent.""",
  "Apartment rent sign", "HOUSING AND CARS"),
 ("""You don't have to fix everything at once. At your next lease renewal, consider a cheaper unit or a roommate. When your car
loan ends, keep driving the car. Cook a few more meals at home. One big change in the big three can be worth more than a year
of small cuts.""",
  "Cooking at home family", "ONE BIG CHANGE")])

step(6, "Build the full emergency fund", "three to six months",
"""Step six. Build the full emergency fund.""",
[("""Grow your cushion to three to six months of essential expenses. On an average salary with essential costs of about three
thousand dollars a month, that's nine to eighteen thousand dollars. More if your income is irregular or you're the only
earner.""",
  "Emergency fund jar", "3 TO 6 MONTHS"),
 ("""This is what lets you keep investing through job changes, car repairs and medical bills without touching your
investments or going back into debt. It's the wall that protects everything else.""",
  "Castle wall", "THE WALL")])

step(7, "Invest 15% automatically", "low cost, diversified",
"""Step seven. Invest fifteen percent of your income, automatically.""",
[("""Raise your retirement contributions toward fifteen percent of gross pay, including the match. Use your workplace plan, an
IRA, or both. Choose simple, diversified, low cost funds, like broad index funds or target date funds.""",
  "Index funds on screen", "15%, AUTOMATICALLY"),
 ("""If fifteen percent isn't possible yet, start where you can and add one percent every six months, or turn on automatic
increases if your plan has them. You'll barely notice each step, but in a few years, you'll be there.""",
  "Percentage stairs", "ONE PERCENT AT A TIME")])

step(8, "Use tax advantages", "keep more of what grows",
"""Step eight. Use tax advantages.""",
[("""Tax advantaged accounts can make a big difference on an average salary. A 401k or traditional IRA can lower your taxes now.
A Roth IRA or Roth 401k can make future withdrawals tax free, under IRS rules. Many people on moderate incomes find a Roth
especially attractive, because their tax rate today may be relatively low.""",
  "Roth IRA document", "TRADITIONAL OR ROTH"),
 ("""If you have a high deductible health plan, a health savings account can offer tax benefits too. And low and moderate income
savers may qualify for the Saver's Credit, a federal tax credit for retirement contributions. Check the IRS website for
current rules and limits.""",
  "Health savings account card", "HSA AND SAVER'S CREDIT")])

step(9, "Grow your income", "the biggest lever",
"""Step nine. Grow your income.""",
[("""On an average salary, income growth is often the most powerful lever. Ask for raises with evidence of your results. Learn
skills your industry pays more for. Get a certification. Consider changing employers, which often brings a larger raise than
staying put.""",
  "Certification course", "THE BIGGEST LEVER"),
 ("""And apply a raise rule. Send at least half of every raise to savings and investing. Your lifestyle still improves, but your
savings rate climbs every year. That's how average salaries become above average wealth.""",
  "Two jars split", "HALF OF EVERY RAISE")])

step(10, "Protect what you build", "insurance and paperwork",
"""Step ten. Protect what you build.""",
[("""Have health insurance. If people depend on your income, consider affordable term life insurance. Consider disability
insurance, which replaces part of your income if you can't work. Many employers offer it cheaply.""",
  "Insurance documents", "INSURANCE"),
 ("""Name beneficiaries on every account and keep them up to date. And consider a basic will. These steps cost little, take a few
hours, and protect years of work.""",
  "Signing will document", "BENEFICIARIES AND A WILL")])

step(11, "Avoid the big mistakes", "the ones that cost years",
"""Step eleven. Avoid the big mistakes.""",
[("""The biggest threats to wealth on an average salary are a handful of big mistakes. Cashing out retirement accounts when
changing jobs. Buying a house or car far above your means. Co signing loans you can't afford to cover. Putting a large share
of savings into a single risky bet.""",
  "Warning signs road", "THE BIG MISTAKES"),
 ("""And panic selling during a market crash. Write your plan now: when the market falls, I keep investing. Then follow it.
Avoiding a few big mistakes matters more than finding the perfect investment.""",
  "Calm investor reading", "DON'T PANIC SELL")])

step(12, "Stay the course for decades", "the step that matters most",
"""Step twelve. Stay the course for decades.""",
[("""This is the step that turns everything else into wealth. Keep the automatic contributions running for twenty, thirty,
forty years. Review once a quarter. Adjust when life changes. But don't stop.""",
  "Long road through seasons", "DECADES"),
 ("""Remember the shape of the curve. Slow for years, then suddenly steep. On an average salary, the steep part usually arrives
in your forties and fifties. The people who get there are the ones who didn't quit in their twenties and thirties.""",
  "Curve steep rising", "SLOWLY, THEN SUDDENLY")])

# ---------------- Mid ----------------
ch("A quick favor")
pr("""Quick pause. If you're on an average salary and this is giving you hope, subscribe to the channel. It's free, and it
helps me keep making these videos for you. Now, the sample budget.""")

# ---------------- Sample budget ----------------
ch("A sample budget on $60,000")
pr("""Here's the sample budget I promised. A single person earning sixty thousand dollars a year, with about four thousand
dollars a month of take home pay after taxes and a pre tax retirement contribution.""")
short("Where every dollar of a $60,000 salary can go")
sc("""Retirement, taken from the paycheck before it arrives: ten percent of gross pay, five hundred dollars a month, plus a
four percent employer match of two hundred dollars. That's fourteen percent going to the future before you see a dime.""",
   "Paycheck retirement deduction", "RETIREMENT: $500 + $200 MATCH")
sc("""From the four thousand of take home pay. Housing, including utilities, about thirteen hundred dollars. Transportation,
including a modest car payment or an older paid off car, insurance and gas, about four hundred fifty. Groceries and some
eating out, about five hundred fifty.""",
   "Monthly budget sheet", "HOUSING, CAR, FOOD")
sc("""Phone and internet, about one hundred twenty. Health costs and insurance not covered by payroll, about one hundred fifty.
Subscriptions and memberships, about fifty. Sinking funds for car repairs, gifts and annual bills, about two hundred.""",
   "Labeled envelopes", "BILLS AND SINKING FUNDS")
sc("""Savings for the emergency fund or other goals, about three hundred dollars. And guilt free fun money, for whatever you
enjoy, about four hundred. Plus a buffer of about four hundred eighty dollars for clothes, personal care, household items
and the unexpected. That's four thousand dollars, every dollar with a job.""",
   "Fun money envelope", "SAVINGS, FUN AND BUFFER")
card("""Retirement fourteen percent including match. Housing about thirteen hundred. Transportation about four hundred fifty. Food
about five hundred fifty. Savings about three hundred. Fun about four hundred. The rest for bills, sinking funds and a
buffer.""",
     {"type": "stat", "label": "sample budget, $60,000 salary", "big": "EVERY $ HAS A JOB", "size": 120, "sub": "illustration; adjust to your city and life"})
sc("""Your numbers will be different. Rent in a big city may be much higher, and in a small town much lower. The point isn't the
exact amounts. It's the structure. Future first, big three under control, sinking funds for the irregular, savings, and real
money for fun. That structure works at almost any income.""",
   "Different cities skyline", "THE STRUCTURE WORKS")

# ---------------- Stories ----------------
ch("Two coworkers, same salary")
short("Two coworkers earned the same. One retired a millionaire.")
sc("""Let's look at two coworkers at the same company, both earning around sixty thousand dollars at twenty five. Daniel takes
the full match, invests fifteen percent, keeps an older car, and sends half of every raise to investing. He lives in a modest
apartment with a roommate until he's twenty nine.""",
   "Young man office desk", "DANIEL: THE PLAN")
sc("""His coworker Megan contributes three percent, just enough to get part of the match. She upgrades her car twice and moves to
a nicer apartment with each raise. She's not reckless. She's doing what feels normal. And she enjoys her twenties.""",
   "Young woman new car", "MEGAN: NORMAL")
sc("""By forty, Daniel's investments might be worth several hundred thousand dollars. Megan's might be closer to one hundred
thousand. By sixty, if both keep going the same way, Daniel could be a millionaire on paper, while Megan is worried about
whether she can retire at all. Same company. Same salary. Thirty five years of different defaults.""",
   "Two retirees different moods", "SAME SALARY, DIFFERENT FUTURES")
sc("""And here's the twist. Megan can still change her ending. At forty, with her highest earning years ahead, raising her
contribution to fifteen or twenty percent and avoiding big new fixed costs can dramatically improve her retirement. The plan
works best when started early. But it works whenever you start.""",
   "Woman planning determined", "IT'S NOT TOO LATE")

sc("""Now meet a third person. Rosa is a school bus driver who earns about forty five thousand dollars a year. She doesn't have a
big employer match, so she opens a Roth IRA at twenty eight and sets up an automatic contribution of three hundred dollars a
month. She drives the same car for twelve years and rents a small apartment near her route.""",
   "School bus driver smiling", "ROSA: SMALLER SALARY")
sc("""Every time she gets a raise, she adds twenty five dollars to her monthly contribution. After about ten years, she's
contributing around five hundred fifty a month. If her investments average seven percent a year, by sixty five she could have
close to a million dollars, mostly tax free under Roth rules, because her contributions kept rising and she never stopped.""",
   "Roth IRA growth chart", "SMALL RAISES, BIG RESULT")
sc("""Rosa's story shows something important. She didn't earn a big salary. She didn't pick hot stocks. She didn't get lucky. She
automated, increased her contributions slowly, and avoided the big mistakes. These are illustrations, not guarantees. But the
behavior behind them is available to almost anyone.""",
   "Woman walking confidently", "BEHAVIOR, NOT LUCK")

ch("Already doing this?")
sc("""If you're already saving fifteen percent, have an emergency fund and no high interest debt, congratulations. You're ahead of
most people. Your job now is mostly to protect the plan. Keep costs low, rebalance once a year if your funds don't do it for
you, and resist the urge to tinker.""",
   "Person relaxing reading", "PROTECT THE PLAN")
sc("""Then think about raising your savings rate toward twenty percent, which can shorten your path to financial independence
by years. Look at your investment fees, because a difference of even half a percent a year compounds into a large amount over
decades. And make sure your partner, if you have one, understands the plan too, so it survives whatever life brings.""",
   "Couple reviewing plan together", "RAISE THE RATE, CUT FEES")
sc("""And finally, give yourself credit. Building wealth on an average salary takes patience in a world that celebrates fast
money. Every month you stick with the plan is a quiet win. You may never post it on social media, but your future self will
notice.""",
   "Quiet sunrise over town", "A QUIET WIN")

# ---------------- FAQ ----------------
ch("Questions people ask")
pr("""Let me answer the questions people ask me most about building wealth on an average salary.""")
sc("""Question one. What if I earn less than sixty thousand? The same plan works. The percentages matter more than the amounts.
Saving ten percent of forty thousand is still building wealth, and the Saver's Credit and Roth IRAs can be especially valuable
at lower incomes. And income growth, step nine, matters even more.""",
   "Hourly worker store", "EARNING LESS?")
sc("""Question two. Should I buy a house? A home can be a great choice if you plan to stay for many years and the full cost of
owning fits comfortably within your budget, with your emergency fund intact. But don't stretch for one. Renting while investing
consistently is also a perfectly good path to wealth.""",
   "Starter home small", "SHOULD I BUY A HOUSE?")
sc("""Question three. Is it worth having a side hustle? It can be, especially for a specific goal, like clearing debt or building
the emergency fund. But protect your time and health, and send side income to the plan, not to new lifestyle costs. A side
hustle that funds a bigger car payment hasn't helped.""",
   "Side hustle delivery", "SIDE HUSTLE?")
sc("""Question four. What about kids? Kids add real costs, and the plan adapts. Many families lower their savings rate for a few
years, then raise it again. Keep at least the match going, protect the emergency fund, and remember that your retirement comes
before their college fund, because they can borrow for school and you can't borrow for retirement.""",
   "Young family with baby", "WHAT ABOUT KIDS?")
sc("""And question five. How do I know if I'm on track? A rough guideline many planners use is to have about one times your salary
saved by thirty, three times by forty, six times by fifty, and eight to ten times by retirement. These are rough targets, not
rules. If you're behind, the plan still works. You just lean harder on steps seven and nine.""",
   "Checklist milestones", "AM I ON TRACK?")

# ---------------- History ----------------
ch("How ordinary workers got access to wealth")
sc("""It's worth remembering how new this opportunity is. For most of history, investing in the stock market was something only
wealthy people did. Buying shares meant paying a broker large commissions, and building a diversified portfolio required a lot
of money.""",
   "Old stock exchange floor historic", "INVESTING WAS FOR THE RICH")
sc("""That started to change in the second half of the twentieth century. In 1974, Congress passed ERISA, the law that created
the individual retirement account. In 1976, Vanguard, founded by John Bogle, launched one of the first index mutual funds
for ordinary investors, letting people own a slice of hundreds of companies at very low cost.""",
   "John Bogle portrait", "INDEX FUNDS ARRIVE")
sc("""Then in 1978, a provision in the tax code, section 401k, was added. Within a few years, employers began using it to let
workers save for retirement directly from their paychecks, before taxes, often with a matching contribution. In 1997, the
Roth IRA followed, allowing tax free growth for people who qualified.""",
   "Tax code book", "THE 401K AND THE ROTH")
sc("""Today, an average worker with a phone can open an account in minutes, buy a broad index fund with very low fees, and
automate contributions every payday. The tools that once belonged to the wealthy are available to almost everyone. The
question is no longer access. It's whether we use them.""",
   "Smartphone investing app", "ACCESS FOR EVERYONE")

# ---------------- Accounts ----------------
ch("Which account first?")
pr("""People often ask me where each dollar should go first. Here's a common order many planners suggest, for someone on an
average salary.""")
sc("""First, your workplace plan up to the full match. That's an instant return you won't find anywhere else. Second, if you
qualify and have a high deductible health plan, a health savings account can offer tax benefits going in, while growing, and
coming out for qualified medical costs.""",
   "Stacked account folders", "MATCH, THEN HSA")
sc("""Third, a Roth IRA or traditional IRA, up to the annual IRS limit, which gives you more control over your investment choices
and often lower fees than some workplace plans. Fourth, go back to your workplace plan and raise contributions toward fifteen
percent or more.""",
   "IRA account statement", "THEN AN IRA, THEN MORE 401K")
sc("""And fifth, once those are on track, a regular taxable brokerage account for goals that aren't retirement, or for extra
investing. The order can change based on your plan's fees, your tax bracket and your goals. But the principle is simple: take
free money first, then tax advantages, then flexibility.""",
   "Brokerage account screen", "FREE MONEY, TAXES, FLEXIBILITY")
sc("""One more tip. Keep it simple. On an average salary, you don't need ten accounts and thirty funds. Two or three accounts,
each with one or two broad low cost funds, is a perfectly strong setup. Simple plans are easier to stick with, and sticking
with it is what builds wealth.""",
   "Minimalist desk one folder", "KEEP IT SIMPLE")

# ---------------- Decades ----------------
ch("The plan, decade by decade")
pr("""Let's put the twelve steps on a timeline. Here's what the plan can look like on an average salary, decade by decade.""")
sc("""Your twenties. This is the decade of foundations. Steps one through four usually happen here: know your numbers, build
the starter cushion, take the full match, and clear high interest debt. Your income is probably at its lowest, but every
dollar you invest now has the most time to grow. A dollar invested at twenty five, at seven percent, could become roughly
fifteen dollars by sixty five.""",
   "Young adult first apartment", "YOUR 20s: FOUNDATIONS")
sc("""The big risks in your twenties are not market crashes. They're lifestyle decisions that lock in high fixed costs. An
expensive car loan, an apartment that takes half your take home pay, or credit card balances that follow you for years. Keep
your fixed costs low, and you keep your options open.""",
   "Young person new car dealership", "AVOID LOCKING IN COSTS")
sc("""Your thirties. This is often the decade of big life changes. Partners, kids, maybe a home. It's also when many people see
their first major raises. The key move here is step nine's raise rule. Send half of every raise to your future, and let the
other half improve your life. Your savings rate rises without you ever feeling poorer.""",
   "Young family moving into home", "YOUR 30s: THE RAISE RULE")
sc("""In your thirties, the emergency fund matters even more, because more people depend on you. And protection, step ten,
becomes essential. Term life insurance and disability insurance are usually cheap at this age, and they protect everything
you're building.""",
   "Parent holding child", "PROTECT THE FAMILY")
sc("""Your forties. This is often when the curve starts to bend upward. If you've been investing steadily, you may notice your
investments growing by more in a good year than you contribute. That's compounding becoming visible. It's also the decade of
peak expenses for many families, so the challenge is to keep contributions steady through it.""",
   "Middle aged couple reviewing finances", "YOUR 40s: THE CURVE BENDS")
sc("""If you started late, your forties are a powerful time to catch up. Your income is often near its peak. Pushing your savings
rate to twenty percent or more for fifteen to twenty years can still build a strong retirement, even from a modest
starting point.""",
   "Determined person at desk", "CATCHING UP WORKS")
sc("""Your fifties and early sixties. Under IRS rules, people aged fifty and older can make extra catch up contributions to
401k plans and IRAs. Many average earners use this decade to make their biggest contributions ever, as kids leave home and
mortgages shrink. This is also when you start planning the transition: when to claim Social Security, how to withdraw, and
how to reduce risk gradually.""",
   "Older worker planning retirement", "YOUR 50s: CATCH UP")
sc("""And at retirement, the average earner who followed the plan often has three sources of income. Social Security, which is
designed to replace a larger share of income for lower and middle earners. Withdrawals from their investments. And, for some,
a pension or part time work they enjoy. Together, these can provide a comfortable, independent retirement.""",
   "Retired couple walking beach", "THREE SOURCES OF INCOME")

# ---------------- Objections ----------------
ch("But Ryan, what about...")
pr("""Now, whenever I share this plan, I hear the same objections. Let's go through them honestly.""")
sc("""Objection one. Prices are too high. Rent, groceries and childcare have risen fast, and for many people, the squeeze is
real. If saving fifteen percent is impossible right now, don't skip the plan. Start with the match and the starter cushion.
Then use steps five and nine, the big three and income growth, to create room over time. Progress beats perfection.""",
   "Grocery prices rising", "PRICES ARE TOO HIGH")
sc("""Objection two. The market could crash. Yes, it will, several times over a thirty five year career. Historically, broad
stock markets have recovered from every major crash, though some recoveries took years. For a long term investor still
contributing every month, a crash means buying at lower prices. That's why emergency funds and automatic contributions
matter so much. They let you keep going.""",
   "Stock market crash chart", "THE MARKET COULD CRASH")
sc("""Objection three. A million dollars won't be worth much in thirty five years. It's true that inflation reduces purchasing
power. At three percent inflation, a million dollars in thirty five years might buy what roughly three hundred fifty thousand
dollars buys today. But that's exactly why investing matters. Cash in a drawer loses value. Investments have historically
been one of the few ways to stay ahead of inflation.""",
   "Inflation shrinking dollar", "INFLATION")
sc("""Objection four. I want to enjoy my life now. Good. So do I. This plan is not about living like a monk. Fifteen percent
saved means eighty five percent spent. The sample budget includes real fun money. The goal is balance: a good life now and a
secure life later, instead of trading one for the other.""",
   "Friends enjoying dinner", "ENJOY LIFE NOW")
sc("""Objection five. I'm too far behind. Whether you're thirty five with nothing saved or fifty with very little, the best
time to start is still today. Every year you invest is a year that compounds. And remember the catch up contributions and
Social Security. Starting late is harder than starting early, but it's far better than never starting.""",
   "Sunrise new start", "TOO FAR BEHIND")
sc("""And objection six. Investing is too complicated. It doesn't have to be. Many 401k plans offer a single target date fund
that automatically spreads your money across stocks and bonds and becomes more conservative as you age. One fund, chosen once,
contributed to automatically. For many average earners, that's enough.""",
   "Simple single fund choice", "TOO COMPLICATED")

sc("""And objection seven. I don't trust the system. Some people worry about Social Security, Wall Street, or rules changing.
Those are fair concerns. That's part of why the plan uses diversified, low cost funds rather than any single company, keeps an
emergency fund in insured savings accounts, and spreads money across different account types. You don't need to trust any one
institution completely. You build a plan that doesn't depend on a single point of failure. And you keep reviewing it every
year as the rules change.""",
   "Diversified baskets eggs", "I DON'T TRUST THE SYSTEM")

# ---------------- This week ----------------
ch("Your first week checklist")
pr("""Plans are only useful if you start. Here's what to do in the next seven days.""")
sc("""Day one. Log into your bank and credit card accounts and write down your take home pay, your last three months of spending,
and every debt with its interest rate. Day two. Open a high yield savings account if you don't have one, and set up an
automatic transfer for payday, even twenty five dollars.""",
   "Person at laptop checklist", "DAYS 1 AND 2")
sc("""Day three. Log into your workplace retirement plan. Check the match formula and make sure you're contributing enough to
get all of it. If your plan offers automatic increases, turn them on. Day four. Look at your big three and pick one change you
can make in the next six months.""",
   "Retirement plan website", "DAYS 3 AND 4")
sc("""Day five. List your high interest debts from highest rate to lowest, and decide where extra payments will go. Day six. Check
your beneficiaries on every account. Day seven. Write one sentence about why you're doing this. A home, freedom, your kids,
peace of mind. Keep it where you'll see it. That's your fuel for the next thirty years.""",
   "Handwritten note on fridge", "DAYS 5, 6 AND 7")

# ---------------- Recap ----------------
ch("Recap: the 12 steps")
sc("""Quick recap. On an average salary, fifteen percent invested for thirty five years at seven percent could grow to well over a
million dollars. The mindset shifts: start now, budget as permission, your own scoreboard, consistent over perfect, fix leaks,
and make it automatic.""",
   "Checklist clipboard", "THE NUMBERS AND MINDSET")
sc("""And the twelve steps: know your numbers, build a starter cushion, get the full match, kill high interest debt, right size the
big three, build the full emergency fund, invest fifteen percent automatically, use tax advantages, grow your income, protect
what you build, avoid the big mistakes, and stay the course for decades.""",
   "Staircase twelve steps", "THE 12 STEPS")

# ---------------- Close ----------------
ch("What to do next")
pr("""If you want this whole plan with worksheets and the sample budget in a spreadsheet, it's in my playbook. The link is in the
description. And watch my video on the first one hundred thousand dollars. It's the first big milestone on this road. I'm
Ryan Rover. See you in the next one.""")

save("video53", "How to Build Wealth on an Average Salary: The Full Plan", [
    "U.S. Bureau of Labor Statistics, Usual Weekly Earnings of Wage and Salary Workers (median full-time earnings)",
    "U.S. Bureau of Labor Statistics, Consumer Expenditure Survey (housing, transportation and food shares)",
    "IRS, 401(k), IRA, Roth, HSA and Saver's Credit rules (check current limits)",
    "Fidelity, quarterly retirement analysis (number of 401(k) millionaires)",
    "Thomas J. Stanley and William D. Danko, The Millionaire Next Door (1996)",
    "Growth figures: stated illustrative math at a 7% average yearly return; salary growth illustration at 3% a year",
], "wealth on an average salary: numbers, psychology, playbook")
