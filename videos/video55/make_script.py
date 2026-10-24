import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

def move(n, title, sub, card_text, paras):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"MOVE {n}")
    for t, q, c in paras:
        sc(t, q, c)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. If you're in your thirties and you feel behind with money, I want you to hear this first. You are not
too late. Not even close. Your thirties might be the most important catch up decade you'll ever have. And today, I'll show
you how to catch up without panic, without extreme frugality, and without gambling on risky bets.""")
short("Behind on money in your 30s? You're not too late.")
sc("""Feeling behind in your thirties is incredibly common. Many people spent their twenties paying off student loans, changing
careers, moving cities, or simply figuring out life. Then they turn thirty, or thirty five, look at their bank account, and feel
a wave of panic. Everyone else seems further ahead.""",
   "Thirty something looking worried at laptop", "FEELING BEHIND")
sc("""But here's the truth. Someone who starts investing seriously at thirty five still has around thirty years before a
traditional retirement age. Thirty years is a long time for compounding to work. And most people earn more in their thirties
than in their twenties, which means they can save faster.""",
   "Long road ahead", "30 YEARS IS A LONG TIME")
sc("""We'll look at this from three angles. First, the numbers: what catching up from your thirties actually looks like. Second,
the psychology: why panic leads to bad decisions, and what to do instead. And third, the playbook: fifteen moves for your
thirties, including how to handle kids, a home and a partner's finances.""",
   "Three paths map", "THREE ANGLES")
pr("""Stay for the catch up table near the end. It shows exactly how much to save each month, depending on when you start. Let's
start with the numbers.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Growth examples use stated math at a seven percent average yearly return, which is an illustration, not a promise. Savings
guidelines by age come from Fidelity. Household finance data comes from the Federal Reserve's Survey of Consumer Finances.
Childcare and family cost data come from the U.S. Department of Labor and other public sources. Retirement account rules come
from the IRS. This is education, not financial advice.""",
   "Federal Reserve building", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. What does catching up from your thirties really look like?""")
sc("""Let's start from zero. Say you're thirty five with nothing invested. If you invest five hundred dollars a month until sixty
five, at a seven percent average yearly return, it could grow to roughly six hundred ten thousand dollars. You'd have contributed
one hundred eighty thousand dollars. Compounding does the rest.""",
   "Growth chart from zero", "$500 A MONTH FROM 35")
card("""Five hundred dollars a month, invested at seven percent a year from age thirty five to sixty five.""",
     {"type": "growth", "monthly": 500, "rate": 0.07, "years": 30})
sc("""Now raise that to seven hundred fifty dollars a month. Over the same thirty years, it could grow to about nine hundred
fifteen thousand dollars. And at one thousand dollars a month, about one point two million dollars. From a standing start at
thirty five.""",
   "Stacks of coins growing", "$1,000 A MONTH = ~$1.2M")
card("""Starting at thirty five with nothing saved, investing for thirty years at seven percent a year.""",
     {"type": "compare", "left": {"label": "$500 a month", "big": "~$610K", "sub": "from age 35 to 65"},
      "right": {"label": "$1,000 a month", "big": "~$1.22M", "sub": "from age 35 to 65"},
      "note": "Illustration. Returns are not guaranteed."})
sc("""And most people in their thirties aren't starting from zero. Say you have twenty thousand dollars in an old 401k from a
previous job. Left alone for thirty years at seven percent, that alone could grow to about one hundred sixty thousand dollars.
Add five hundred a month, and the total could reach roughly seven hundred seventy thousand.""",
   "Old 401k statement", "$20K + $500 A MONTH = ~$770K")
sc("""What about a five year delay? If you wait until forty and then invest five hundred a month for twenty five years, the total
could be about four hundred five thousand dollars. That five year delay costs around two hundred thousand dollars. To make it up,
you'd need to invest closer to seven hundred fifty a month from forty.""",
   "Calendar pages flipping", "WAITING 5 YEARS COSTS ~$200K")
sc("""So the math in your thirties is clear. Starting now matters more than starting perfectly. And the amount you save each month
matters a lot, because you have less time than a twenty two year old. That's why the playbook focuses heavily on raising your
savings rate.""",
   "Calculator and plan", "NOW BEATS PERFECT")
sc("""Where do people in their thirties actually stand? According to the Federal Reserve's Survey of Consumer Finances, median
net worth for families headed by someone under thirty five was about thirty nine thousand dollars in 2022, and for ages thirty
five to forty four, about one hundred thirty five thousand. Medians hide huge variation, but they show that many people are still
building in this decade.""",
   "Survey data chart", "WHERE PEOPLE STAND")
sc("""Fidelity suggests a rough guideline of having about one times your salary saved for retirement by thirty, and about three
times by forty. If you're below that, you're in good company. These are targets to aim for, not grades on your life.""",
   "Milestone markers", "1X BY 30, 3X BY 40")
sc("""Now, the cost side. The thirties are often the most expensive decade. The Department of Labor's national childcare price data
shows full time childcare can cost many thousands of dollars per child per year, in some areas more than rent. Add a mortgage,
a larger car and family health insurance, and it's easy to see why saving feels so hard.""",
   "Family with young children", "THE EXPENSIVE DECADE")
pr("""So the numbers are encouraging, but the decade is expensive. That's exactly why psychology matters so much. Angle two.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
pr("""Angle two. The psychology. Why panic is the enemy, and five mindset shifts for your thirties.""")
short("Why panic is the most expensive feeling in your 30s")
sc("""When people feel behind, they often panic. And panic leads to three expensive mistakes. The first is freezing: feeling so
overwhelmed that you do nothing. The second is gambling: trying to catch up fast with risky bets, hot stocks, or schemes that
promise quick returns. The third is extreme restriction: a budget so strict it collapses after a few weeks.""",
   "Panicked person with charts", "THREE PANIC MISTAKES")
sc("""Shift one. From behind, to on my own timeline. Comparison is especially intense in your thirties. Friends buy houses, get
promotions, post vacations. But you don't know their debt, their family help, or their stress. The only comparison that helps is
you versus you a year ago.""",
   "Person running own race", "SHIFT 1: YOUR TIMELINE")
sc("""Shift two. From guilt, to data. Many people avoid looking at their accounts because they feel ashamed. But shame doesn't build
wealth. Looking at your numbers without judgment, like a doctor reading test results, turns a scary feeling into a plan.""",
   "Doctor reading chart calmly", "SHIFT 2: GUILT TO DATA")
sc("""Shift three. From fast, to steady and strong. Catching up doesn't require high risk. It requires a higher savings rate and
consistency. A boring plan that you follow for twenty five years will usually beat an exciting one you abandon after a bad year.""",
   "Strong steady bridge", "SHIFT 3: STEADY")
sc("""Shift four. From either or, to both. In your thirties, money questions often feel like either or. Kids or retirement. House or
investing. Fun or saving. But most of the time, the answer is a balance. A good plan funds several goals at once, in the right
proportions.""",
   "Balanced scale", "SHIFT 4: BOTH")
sc("""And shift five. From someday, to systems. Busy lives in your thirties make willpower unreliable. Systems, like automatic
contributions, automatic increases and automatic bill pay, keep working when you're tired, busy or distracted. Set them up once,
and let them carry you.""",
   "Automated system gears", "SHIFT 5: SYSTEMS")

ch("The hidden advantages of your thirties")
sc("""Here's what people often forget. Your thirties come with real advantages over your twenties. You usually earn more. You
know yourself better, including your spending triggers. You may have a partner to share costs and goals with. And you've seen
enough market ups and downs to stay calmer when the next drop comes.""",
   "Confident thirty something", "REAL ADVANTAGES")
sc("""You also have more information about what you actually value. In your twenties, people often spend on things they think
they should want. In your thirties, many people find it easier to cut the things they don't care about, and spend more on what
truly matters. That kind of clarity makes saving much easier.""",
   "Person choosing what matters", "CLARITY ABOUT VALUES")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
pr("""Angle three. The playbook. Fifteen moves for your thirties, in a sensible order.""")
short("15 money moves to catch up in your 30s")

move(1, "Get your full picture", "one honest hour",
"""Move one. Get your full picture.""",
[("""Gather every account in one place: checking, savings, retirement accounts from old jobs, debts, and their interest rates.
Write down your net worth: what you own minus what you owe. It might be negative. That's okay. It's your starting line.""",
  "Spreadsheet net worth", "ONE HONEST HOUR"),
 ("""Many people in their thirties discover old 401k accounts they'd half forgotten. Consolidating them into one IRA or your current
plan can make your money easier to manage and help you see the whole picture clearly.""",
  "Old 401k statements", "FIND THE OLD ACCOUNTS")])

move(2, "Build a real emergency fund", "three to six months",
"""Move two. Build a real emergency fund.""",
[("""With more responsibilities, your emergency fund matters more than ever. Aim for three to six months of essential expenses in a
high yield savings account. If you have kids, a mortgage or a single income, lean toward six.""",
  "Emergency fund jar", "3 TO 6 MONTHS"),
 ("""Build it in stages. First one month, then three, then six. Keep contributing at least enough to get your employer match while
you build it, so you don't miss free money.""",
  "Stages progress", "BUILD IN STAGES")])

move(3, "Clear high interest debt", "the catch up accelerator",
"""Move three. Clear high interest debt.""",
[("""Credit card debt at twenty percent or more makes catching up almost impossible. List your debts by rate, pay minimums on all,
and attack the highest rate first. Every card you clear frees up money you can invest.""",
  "Credit card debt payoff", "HIGHEST RATE FIRST"),
 ("""If your credit is good, a balance transfer card or a lower rate personal loan can help, but only if you stop adding new debt.
Read the fees and the promotional period carefully.""",
  "Balance transfer offer", "USE TOOLS CAREFULLY")])

move(4, "Raise your savings rate to 15% or more", "the main catch up lever",
"""Move four. Raise your savings rate to fifteen percent or more.""",
[("""If you're starting in your thirties, a common recommendation is to save fifteen percent or more of your gross income for
retirement, including any match. If you're well behind, twenty percent can make a big difference over thirty years.""",
  "Percentage rising", "15 TO 20 PERCENT"),
 ("""If you can't get there right away, increase by one or two percent every six months. Many workplace plans let you set automatic
increases. In two or three years, you can reach your target without ever feeling a sudden drop in your take home pay.""",
  "Automatic increase setting", "ONE PERCENT AT A TIME")])

move(5, "Use tax advantaged accounts fully", "keep more of the growth",
"""Move five. Use tax advantaged accounts fully.""",
[("""Use your workplace plan, an IRA, and a health savings account if you have a qualifying high deductible health plan. The IRS sets
yearly limits for each. Using them fully can lower your taxes and help your money grow faster.""",
  "Tax advantaged accounts", "401K, IRA, HSA"),
 ("""Roth or traditional? In general, traditional contributions lower your taxes now, and Roth contributions can make future
withdrawals tax free. Many people use a mix. A tax professional can help you decide based on your current and expected tax
rates.""",
  "Roth versus traditional chart", "A MIX CAN WORK")])

move(6, "Grow your income", "your thirties are prime earning years",
"""Move six. Grow your income.""",
[("""Your thirties are often when income can rise fastest. Ask for raises with evidence, pursue promotions, build specialized skills,
and consider changing employers if your pay has stalled. A ten thousand dollar raise, saved in part, can transform your catch up
plan.""",
  "Promotion handshake", "PRIME EARNING YEARS"),
 ("""And use the raise rule. Send at least half of every raise straight to savings and investing. Your life still gets better, but
your savings rate climbs every year.""",
  "Split raise jar", "HALF OF EVERY RAISE")])

move(7, "Control the big three", "housing, cars, food",
"""Move seven. Control the big three.""",
[("""Housing, transportation and food usually make up most of a household budget. In your thirties, the risk is upgrading all three
at once: a bigger house, a second new car, more eating out. Each one feels reasonable. Together they can block your catch up plan.""",
  "Big house two new cars", "THE UPGRADE TRAP"),
 ("""Make one big decision well rather than a hundred small ones. Buy a home you can comfortably afford, not the maximum the bank
approves. Drive cars for longer. Plan meals. These choices can free up hundreds of dollars a month.""",
  "Modest home and older car", "ONE BIG DECISION WELL")])

move(8, "Buy a home only when ready", "not when pressured",
"""Move eight. Buy a home only when you're ready.""",
[("""Many people feel pressure to buy in their thirties. But buying before you're ready can drain your emergency fund and stall your
investing. Signs you may be ready: stable income, an emergency fund that stays intact after the down payment, good credit, and plans
to stay for many years.""",
  "House keys handoff", "READY, NOT PRESSURED"),
 ("""Remember the full cost of owning: property taxes, insurance, maintenance, and repairs. A common guideline is to budget around one
to two percent of the home's value per year for maintenance. Renting while you invest is a perfectly good choice too.""",
  "Home repair tools", "THE FULL COST OF OWNING")])

move(9, "Protect your family", "insurance and paperwork",
"""Move nine. Protect your family.""",
[("""If anyone depends on your income, consider term life insurance. For many healthy people in their thirties, term life coverage
can be relatively affordable. Disability insurance matters too, because your ability to earn is likely your largest asset.""",
  "Family insurance documents", "LIFE AND DISABILITY"),
 ("""Write a will, especially if you have children, and name guardians. Update beneficiaries on every account. These steps take a
few hours and can prevent enormous stress for the people you love.""",
  "Signing will", "A WILL AND BENEFICIARIES")])

move(10, "Put retirement before college", "the oxygen mask rule",
"""Move ten. Put retirement before college savings.""",
[("""If you have kids, it's natural to want to save for their college first. But many planners suggest putting your retirement first,
like putting on your own oxygen mask before helping others. Your kids can borrow for college, apply for aid and scholarships. You
can't borrow for retirement.""",
  "Parent and child airplane mask", "OXYGEN MASK RULE"),
 ("""Once your retirement savings are on track, a 529 plan can be a tax advantaged way to save for education. Even small monthly
amounts add up over eighteen years.""",
  "529 plan document", "THEN A 529")])

move(11, "Get on the same page with your partner", "one plan, two people",
"""Move eleven. Get on the same page with your partner.""",
[("""If you share your life with someone, share your money plan too. Talk about goals, debts, spending styles and what retirement
looks like. Many couples find a monthly money date, just thirty minutes, keeps them aligned.""",
  "Couple money date", "ONE PLAN, TWO PEOPLE"),
 ("""Decide how you'll handle accounts: joint, separate, or a mix. There's no single right answer. What matters is that both people
understand the plan and feel respected in it.""",
  "Joint and separate accounts", "JOINT, SEPARATE OR BOTH")])

move(12, "Invest simply and stay invested", "no catch up gambling",
"""Move twelve. Invest simply and stay invested.""",
[("""Broad, low cost index funds or target date funds work well for most people catching up. Avoid trying to time the market or
chase last year's winners. And keep fees low, because a one percent fee difference can cost a large share of your gains over
decades.""",
  "Index fund simple portfolio", "SIMPLE AND LOW COST"),
 ("""When the market drops, and it will, keep contributing. For someone with decades to go, falling prices mean buying more shares
for the same money. Write that rule down now, before the next drop.""",
  "Market dip and buying", "KEEP BUYING IN DROPS")])

move(13, "Use windfalls on purpose", "bonuses, refunds, gifts",
"""Move thirteen. Use windfalls on purpose.""",
[("""Bonuses, tax refunds, inheritances and gifts are powerful catch up tools. Decide in advance how you'll split them. For example,
seventy percent to your plan and thirty percent to enjoy.""",
  "Bonus check", "DECIDE THE SPLIT IN ADVANCE"),
 ("""A five thousand dollar bonus invested at thirty five, at seven percent, could grow to about thirty eight thousand dollars by
sixty five. Use windfalls well a few times in your thirties, and they can add six figures to your future.""",
  "Small seed big tree", "$5K AT 35 = ~$38K AT 65")])

move(14, "Avoid lifestyle creep", "the silent thief",
"""Move fourteen. Avoid lifestyle creep.""",
[("""As income rises, spending tends to rise with it. A nicer car, more subscriptions, bigger vacations, more takeout. None of it
feels like a big decision. That's what makes lifestyle creep so powerful.""",
  "Spending creeping up", "THE SILENT THIEF"),
 ("""Pick the upgrades you truly value and say no to the rest. Review subscriptions twice a year. Keep your fixed costs low enough
that a job loss or a new baby doesn't turn into a crisis.""",
  "Subscription list", "CHOOSE YOUR UPGRADES")])

move(15, "Review once a quarter", "small corrections",
"""Move fifteen. Review once a quarter.""",
[("""Every three months, check your net worth, savings rate, debt balances and progress toward your emergency fund. Raise your
contributions if you can. Once a year, review insurance, beneficiaries and your overall plan.""",
  "Quarterly calendar review", "15 MINUTES A QUARTER"),
 ("""Track your net worth over time. Watching it rise, even slowly, is one of the best ways to replace panic with confidence.""",
  "Net worth chart rising", "WATCH IT RISE")])

# ---------------- Mid placement ----------------
ch("A quick favor")
pr("""Quick pause. If this is helping you feel less behind, subscribe to the channel. It's free, and it helps me keep making these
videos. Now, the catch up table I promised.""")

# ---------------- Catch up table ----------------
ch("The catch up table")
short("How much to save each month if you start at 30, 35 or 40")
sc("""Here's a simple way to think about catching up. Say your goal is around one million dollars by sixty five, before inflation.
At a seven percent average yearly return, starting from zero, roughly how much would you need to invest each month?""",
   "Goal one million target", "THE GOAL: $1 MILLION")
sc("""Starting at thirty: about five hundred fifty five dollars a month. Starting at thirty five: roughly eight hundred
twenty dollars a month. Starting at forty: about one thousand two hundred thirty five dollars a month. Every five years of waiting
raises the monthly amount by around forty to fifty percent.""",
   "Table of monthly amounts", "30, 35, 40")
card("""Approximate monthly investment to reach about one million dollars by sixty five at seven percent a year, starting from zero.""",
     {"type": "stat", "label": "monthly to reach ~$1M by 65", "big": "$555 / $820 / $1,235", "size": 110, "sub": "start at 30 / 35 / 40 (7% a year, illustration)"})
sc("""Those amounts include any employer match. If your employer adds two or three hundred dollars a month, your own share is much
smaller. And if you already have savings, the required amount drops further. Your number may also be lower if you'll have a
pension or expect a healthy Social Security benefit.""",
   "Employer match illustration", "THE MATCH COUNTS")
sc("""Does everyone need a million dollars? No. Your number depends on the life you want. A common rough rule is that a portfolio
of about twenty five times your yearly spending, combined with Social Security, may support a long retirement. But planning is
personal, and it's worth running your own numbers.""",
   "Retirement planning worksheet", "YOUR OWN NUMBER")

# ---------------- Stories ----------------
ch("Two people catching up")
short("She started at 35 with nothing. Here's what happened.")
sc("""Let's look at two examples. Elena is thirty five, earns seventy thousand dollars, and has almost nothing saved after years of
paying off student loans. She feels behind. She builds a three month emergency fund in a year, then raises her retirement
contribution to fifteen percent, with a four percent match. That's about one thousand ninety dollars a month going in.""",
   "Woman professional planning", "ELENA: STARTS AT 35")
sc("""She uses the raise rule every year and keeps her car for ten years. By forty five, her retirement accounts might be worth around
two hundred thousand dollars. By sixty five, if she keeps going and her income rises, she could be well past one million dollars.
She didn't do anything extreme. She just started, and kept going.""",
   "Woman calm retirement", "ELENA: STEADY WINS")
sc("""Now Chris. He's thirty eight, feels behind, and wants to catch up fast. He puts his savings into a single hot stock that a
friend recommends, and later into a speculative coin. Some years he's up. Some years he's down a lot. After five years, he's roughly
where he started, and stressed.""",
   "Man stressed trading phone", "CHRIS: CATCH UP GAMBLING")
sc("""At forty three, Chris resets. He moves to diversified funds, sets up automatic contributions of twenty percent, and stops
checking prices daily. He still has more than twenty years to go. His story shows that it's never too late to switch from panic to
a plan. But those five years of gambling cost him real time.""",
   "Man calm with plan", "CHRIS: THE RESET")

sc("""What do Elena and Chris have in common? Both felt behind, and both could still build a secure future. The difference was how
they responded to the feeling. Elena turned it into a system. Chris turned it into a bet. In your thirties, a system almost always
wins, because it keeps working long after the panic fades.""",
   "System versus gamble", "SYSTEM BEATS A BET")

# ---------------- Kids and money ----------------
ch("Money with young kids")
sc("""For many people, the thirties are the decade of young children, and kids change the budget dramatically. Childcare, diapers,
bigger housing, health insurance and food all add up. It's normal for your savings rate to dip for a few years.""",
   "Young parents with baby", "THE BABY YEARS")
sc("""The key is to protect the essentials during those years. Keep at least your employer match going. Protect your emergency fund.
Avoid adding new debt. And make a plan to raise your savings again when childcare costs fall, for example when kids start school.""",
   "Kid starting school", "PROTECT THE ESSENTIALS")
sc("""Look into tax benefits too. Depending on your situation, the Child Tax Credit, a dependent care flexible spending account
through your employer, or the Child and Dependent Care Credit may reduce your costs. Check the IRS website or ask a tax professional
for current rules.""",
   "Tax form family credits", "CHECK TAX BENEFITS")
sc("""And teach your kids about money early, even in small ways. Letting them see you save, compare prices, and make choices helps
them build the habits you're building now. That might be one of the best long term investments you ever make.""",
   "Parent teaching child coins", "TEACH THEM EARLY")

# ---------------- History ----------------
ch("Why so many people feel behind")
sc("""It's worth understanding why so many people in their thirties feel behind today. Over the past several decades, many employers
replaced traditional pensions with 401k style plans. That shifted the responsibility for retirement saving from companies to
individuals.""",
   "Old pension document", "FROM PENSIONS TO 401K")
sc("""Meanwhile, the cost of education and housing has grown faster than wages for many people. And many people in their thirties
entered the job market during or after major economic shocks, like the 2008 financial crisis or the 2020 pandemic, which delayed
careers and savings.""",
   "Recession news headlines", "REAL HEADWINDS")
sc("""So if you feel behind, it's not just you. The system changed. But the tools available today, like automatic enrollment, low cost
index funds, Roth accounts and high yield savings, are better than ever. You can use them to build your own pension, one paycheck at
a time.""",
   "Modern tools smartphone", "BUILD YOUR OWN PENSION")

# ---------------- Sample budget ----------------
ch("A sample 30s budget")
pr("""Let's make this real with a sample budget. A couple in their thirties, one young child, combined income of one hundred ten
thousand dollars a year.""")
sc("""After taxes, health insurance and retirement contributions of twelve percent of pay, plus a four percent employer match, their
take home pay might be around six thousand two hundred dollars a month, depending on their state. The retirement contributions,
including the match, total about fourteen hundred sixty dollars a month, going in before the paycheck arrives.""",
   "Family budget paycheck", "~$6,200 TAKE HOME")
sc("""Housing, including mortgage or rent, insurance and utilities, about twenty one hundred dollars. Childcare, about twelve hundred.
Transportation for two adults, about six hundred. Groceries and some eating out, about eight hundred fifty.""",
   "Monthly bills sheet", "HOUSING, CHILDCARE, CARS, FOOD")
sc("""Sinking funds for car repairs, holidays and annual bills, about three hundred. Emergency fund and other savings, about four
hundred. A small 529 contribution, one hundred. Phone, internet and subscriptions, about two hundred. Fun and personal spending, about
three hundred. That leaves a small buffer for clothes, health costs and the unexpected.""",
   "Labeled envelopes", "SAVINGS, FUN, BUFFER")
sc("""Notice what this budget does. Retirement is funded first. The emergency fund keeps growing. There's a small college fund. And
there's still money for fun. It's tight, because childcare is expensive. But when childcare ends, that twelve hundred dollars a month
can go straight to savings, and their catch up accelerates.""",
   "Family relaxed at home", "WHEN CHILDCARE ENDS")
card("""Retirement first, emergency fund growing, a small 529, real fun money. When childcare ends, redirect it to savings.""",
     {"type": "stat", "label": "sample 30s family budget", "big": "FUTURE FIRST", "size": 120, "sub": "illustration; adjust to your city and family"})

# ---------------- Career ----------------
ch("Career moves that pay in your 30s")
sc("""In your thirties, career decisions can have a bigger impact on wealth than almost any budget tweak. Research from labor
economists has found that much of lifetime wage growth happens in the first ten to fifteen years of a career, often through job
changes and promotions.""",
   "Career ladder climbing", "CAREER MATTERS MOST")
sc("""Practical moves include asking for a clear path to promotion, learning skills that are in demand in your field, building
relationships with people a level or two above you, and checking market pay every year or two. If your employer won't pay market
rates, it may be time to look elsewhere.""",
   "Professional networking", "PRACTICAL MOVES")
sc("""And think about your income resilience. Could you find a new job quickly if you lost yours? Keeping your skills current, your
network active and your resume updated is a kind of insurance. Combined with a strong emergency fund, it lets you handle
layoffs without derailing your plan.""",
   "Resume updated laptop", "INCOME RESILIENCE")

# ---------------- Already on track ----------------
ch("Already on track?")
sc("""If you're in your thirties and already saving fifteen percent, with an emergency fund and no high interest debt, you're in a
strong position. Your job now is to protect it. Avoid big lifestyle jumps, keep fees low, and don't let a market drop scare you out.""",
   "Confident person reviewing", "PROTECT YOUR LEAD")
sc("""Consider raising your savings rate toward twenty or twenty five percent, which could open the door to retiring earlier or
working by choice in your fifties. And look at your taxes: making the most of tax advantaged accounts can add up significantly over
decades.""",
   "Early retirement beach", "AIM HIGHER")

# ---------------- The 40s ----------------
ch("A look ahead to your forties")
sc("""What you do in your thirties shapes your forties. People who build an emergency fund, clear high interest debt and save fifteen
percent in their thirties often find their forties feel very different. Their investments start to grow by more each year than they
contribute. Money starts working as hard as they do.""",
   "Middle aged couple relaxed", "THE CURVE BENDS")
sc("""Your forties may also bring peak earning years, which is the perfect time to push your savings rate even higher. And by fifty,
catch up contributions allow you to put even more into retirement accounts. The thirties are the foundation. The forties and fifties
are where it can really take off.""",
   "Rocket taking off", "THEN IT TAKES OFF")

# ---------------- Single ----------------
ch("Single in your thirties")
sc("""Not everyone in their thirties has a partner or kids, and the plan works just as well for singles. In some ways, single people
can save faster, with fewer dependents and more flexibility. In other ways, it's harder, because there's only one income to cover
rent, insurance and emergencies.""",
   "Single professional apartment", "ONE INCOME")
sc("""If you're single, your emergency fund matters even more, because there's no second paycheck to fall back on. Six months of
expenses is a good target. Disability insurance is especially important. And make sure your beneficiaries and a basic will reflect
who you want to inherit what you've built.""",
   "Emergency fund six months", "SIX MONTHS AND PROTECTION")
sc("""Singles also face their own social pressure: weddings, trips, dinners. Choose the ones that truly matter to you. And use your
flexibility as an advantage. A cheaper city, a career move, or a few years of aggressive saving can transform your catch up plan.""",
   "Friends at wedding", "USE YOUR FLEXIBILITY")

ch("Starting over in your thirties")
sc("""Some people reach their thirties after a divorce, a business failure, a health crisis or a layoff that wiped out their savings.
If that's you, the plan still works. Start with the same foundations: a starter emergency fund, the employer match, and a plan for
any debt.""",
   "Person starting over sunrise", "STARTING OVER")
sc("""Be patient with yourself. Recovering financially often takes a few years, and that's normal. But with twenty five to thirty
years ahead, a fresh start in your thirties can still lead to a secure retirement. Many people who rebuilt in their thirties look
back and say it taught them the habits that made them wealthy later.""",
   "Person rebuilding house", "PATIENCE AND REBUILDING")

ch("Your health is a money plan too")
sc("""One more thing that's easy to overlook. Your health is one of your biggest financial assets. Chronic health problems can raise
medical costs and reduce your ability to work. Regular checkups, exercise, sleep and managing stress aren't just good for your body.
They protect your earning power for decades.""",
   "Person jogging park", "HEALTH IS WEALTH")

# ---------------- First week ----------------
ch("Your first week checklist")
sc("""Here's what to do in the next seven days. Day one: list every account and debt. Day two: calculate your net worth. Day three:
log into your retirement plan, confirm you're getting the full match, and turn on automatic increases if available.""",
   "Checklist days", "DAYS 1 TO 3")
sc("""Day four: open or check your high yield savings account and automate a transfer. Day five: list debts by interest rate and pick
your target. Day six: check your beneficiaries and insurance. Day seven: sit down with your partner, or yourself, and write your
three money goals for the next year.""",
   "Couple writing goals", "DAYS 4 TO 7")

# ---------------- Objections ----------------
ch("But Ryan, what about...")
pr("""Whenever I talk about catching up in your thirties, I hear the same objections. Let's go through them honestly.""")
sc("""Objection one. I can't afford to save fifteen percent. For many families in their thirties, that's true right now. So start with
what you can, even three or five percent plus the match. Then use automatic increases, raises and windfalls to climb. The goal is the
direction, not the starting number.""",
   "Small plant growing", "I CAN'T AFFORD 15%")
sc("""Objection two. The market is too high, I'll wait for a crash. Nobody can reliably predict crashes. People who wait often miss
years of growth. Investing every month, in good markets and bad, means you buy some shares at high prices and some at low prices,
without needing to guess.""",
   "Market chart question mark", "I'LL WAIT FOR A CRASH")
sc("""Objection three. Social Security won't be there for me. According to the Social Security Trustees reports, the program's trust
funds are projected to be depleted in the 2030s if nothing changes, but even then, ongoing payroll taxes are projected to cover most
scheduled benefits. Many experts expect changes to the program, not its disappearance. Still, it's wise to plan with a margin of
safety.""",
   "Social Security card", "SOCIAL SECURITY")
sc("""Objection four. I'd rather enjoy life now. Me too. A good plan includes real fun money. The point isn't to sacrifice your thirties.
It's to make sure your fifties and sixties are enjoyable too. With a balanced budget, you don't have to choose.""",
   "Family on vacation beach", "ENJOY LIFE NOW")
sc("""And objection five. I'll just work longer. Working longer can help, but it isn't always a choice. Health problems, caregiving and
layoffs can force earlier retirement than planned. Many surveys of retirees find a large share retired earlier than they expected.
Saving now gives you options if life changes your plans.""",
   "Older worker leaving office", "I'LL WORK LONGER")

# ---------------- FAQ ----------------
ch("Questions people ask")
pr("""Let me answer the questions I hear most from people in their thirties.""")
sc("""Question one. Is it too late to start at thirty eight or thirty nine? No. You still have more than twenty five years before a
typical retirement age. Saving fifteen to twenty percent and staying consistent can build a solid retirement. And catch up
contributions become available at fifty under IRS rules.""",
   "Person starting at desk", "TOO LATE AT 39?")
sc("""Question two. Should I pay off my mortgage early or invest? It depends on your rate and your goals. Many people with low rate
mortgages choose to invest instead, because long term market returns have historically been higher. Others value the peace of mind
of a paid off home. Either can be reasonable once your retirement savings are on track.""",
   "Mortgage document", "MORTGAGE OR INVEST?")
sc("""Question three. My partner and I have very different money styles. What do we do? That's very common. Start with shared goals
rather than spending details. Agree on savings targets together, then give each person some personal spending money with no
questions asked. That reduces conflict while keeping the plan on track.""",
   "Couple talking calmly", "DIFFERENT STYLES")
sc("""Question four. Should I take money out of my 401k to pay off debt? Usually, it's best to avoid it. Early withdrawals can trigger
taxes and penalties, and you lose years of compounding. Loans from a 401k have their own risks, especially if you leave your job.
Explore other options first.""",
   "401k withdrawal warning", "RAID THE 401K?")
sc("""And question five. How do I stop feeling anxious about money? Action helps more than worry. Make a written plan, automate as
much as you can, and review once a quarter instead of every day. As your emergency fund grows and your net worth rises, many people
find the anxiety fades.""",
   "Calm person journaling", "ANXIETY")

sc("""Question six. Should I hire a financial advisor? It can help, especially for complex situations. If you do, look for a fee
only fiduciary, someone legally required to act in your best interest, and understand exactly how they're paid. For many people with
simple situations, a target date fund and an automated plan work well too.""",
   "Advisor meeting", "HIRE AN ADVISOR?")
sc("""And question seven. What's the single most important move in your thirties? Raising your savings rate and automating it. Everything
else helps, but nothing replaces a steady, automatic share of every paycheck going to your future.""",
   "Automatic savings app", "THE ONE MOVE")

sc("""Question eight. How much should I keep in cash versus investments? A common approach is to keep your emergency fund and any
money you'll need within the next few years, like a down payment, in high yield savings or similar safe accounts. Money for goals
ten or more years away, like retirement, can usually be invested for growth. Matching the account to the timeline reduces the chance
you'll have to sell investments at a bad time.""",
   "Cash and investments split", "CASH OR INVEST?")
sc("""And one last thought before the recap. Feeling behind is a feeling, not a fact. The fact is that you have time, income, and
better tools than any generation before you. What you do with the next five years matters far more than what happened in the last
ten. Start this week.""",
   "Person looking at horizon", "A FEELING, NOT A FACT")

# ---------------- Recap ----------------
ch("Recap: 15 moves")
short("Your 30s money checklist in 60 seconds")
sc("""Quick recap. Starting at thirty five with five hundred dollars a month could build around six hundred ten thousand dollars by
sixty five. Raising that to one thousand a month could build over a million. Don't panic. Don't freeze, gamble or over restrict.""",
   "Checklist clipboard", "THE NUMBERS")
sc("""The fifteen moves. Get your full picture. Build a real emergency fund. Clear high interest debt. Raise your savings rate to
fifteen percent or more. Use tax advantaged accounts. Grow your income. Control the big three. Buy a home only when ready.""",
   "First moves list", "MOVES 1 TO 8")
sc("""Protect your family. Put retirement before college. Get on the same page with your partner. Invest simply and stay invested.
Use windfalls on purpose. Avoid lifestyle creep. And review once a quarter.""",
   "Second moves list", "MOVES 9 TO 15")

# ---------------- Close ----------------
ch("What to do next")
pr("""This week, do move one. One honest hour with your numbers. Then pick the next move and keep going. If you want to go further,
watch my video on retiring early on a normal income. I'm Ryan Rover. See you in the next one.""")

save("video55", "Your 30s Money Plan: Catching Up Without Panic", [
    "Growth figures: stated illustrative math at a 7% average yearly return",
    "Federal Reserve, Survey of Consumer Finances 2022 (median net worth by age)",
    "Fidelity, retirement savings guidelines by age",
    "U.S. Department of Labor, Women's Bureau, National Database of Childcare Prices",
    "IRS, 401(k), IRA, HSA, Child Tax Credit and dependent care rules",
    "Consumer Financial Protection Bureau, guides on debt and homebuying",
], "your 30s money plan: numbers, psychology, playbook")
