import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

def step(n, title, sub, card_text, paras):
    ch(f"Step {n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"STEP {n}")
    for t, q, c in paras:
        sc(t, q, c)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. When people hear retire early, they usually picture tech millionaires or lottery winners. But some
people with ordinary incomes, teachers, nurses, engineers, government workers, reach financial independence in their forties or
early fifties. They don't win anything. They use one number most people never calculate. Today I'll show you that number, and the
full plan.""")
short("You can retire early on a normal income. Here's the math.")
sc("""Retiring early doesn't have to mean never working again. For most people, it means reaching financial independence: having
enough invested that work becomes optional. You can keep working at something you love, work part time, start a business, or stop
completely. The choice is yours.""",
   "Person relaxing hammock", "WORK BECOMES OPTIONAL")
sc("""This idea has a name: FIRE, which stands for Financial Independence, Retire Early. It became popular through books like Your
Money or Your Life by Vicki Robin and Joe Dominguez, first published in 1992, and later through online communities and blogs. And
its core math is surprisingly simple.""",
   "Your Money or Your Life book", "FIRE")
sc("""We'll look at this from three angles. First, the numbers: how much you need and how long it takes, based mostly on one thing.
Second, the psychology: what makes this path work, and what makes people quit. And third, the playbook: twelve steps, plus how to
handle healthcare and access your money before traditional retirement age.""",
   "Three paths mountain", "THREE ANGLES")
pr("""Stay for the savings rate table. It might be the most important chart in personal finance. Let's start with the numbers.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""The four percent rule comes from financial planner William Bengen's 1994 research and the later Trinity study by professors at
Trinity University. Growth examples use stated math at a five percent return after inflation, an illustration, not a promise.
Retirement account and early withdrawal rules come from the IRS. Health insurance information comes from healthcare dot gov. This is
education, not financial advice.""",
   "Research papers on desk", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. How much do you need, and how long will it take?""")
sc("""Let's start with how much. In 1994, a financial planner named William Bengen studied historical U.S. market returns and asked:
how much could a retiree withdraw each year, adjusted for inflation, without running out of money over thirty years? His answer was
about four percent of the starting portfolio. That became known as the four percent rule.""",
   "William Bengen research chart", "THE 4% RULE")
sc("""Flip the four percent rule around, and you get the rule of twenty five. Multiply your yearly spending by twenty five, and that's
a rough estimate of the portfolio you need. Spend forty thousand dollars a year? Twenty five times that is one million dollars. Spend
thirty thousand? Seven hundred fifty thousand.""",
   "Calculator multiply 25", "THE RULE OF 25")
card("""Multiply yearly spending by twenty five to estimate a financial independence number. Forty thousand a year means about one
million dollars.""",
     {"type": "stat", "label": "your FI number = yearly spending × 25", "big": "$40K → $1M", "sub": "based on the 4% rule (Bengen 1994, Trinity study)"})
sc("""An important caveat. The four percent rule was built around thirty year retirements. If you retire at forty five, your money may
need to last fifty years. Many early retirees use a more cautious withdrawal rate, like three and a half percent, which means a
portfolio closer to twenty eight or thirty times spending. We'll keep that in mind.""",
   "Long timeline", "EARLY RETIREES: BE MORE CAREFUL")
sc("""Now the big insight. Notice that your FI number depends on your spending, not your income. And the time it takes to get there
depends mostly on your savings rate: the share of your take home pay you save. Not your salary. Your savings rate.""",
   "Savings rate gauge", "IT'S YOUR SAVINGS RATE")
short("The most important chart in personal finance")
sc("""Here's why. When you save more, two things happen at once. You invest more each year. And you train yourself to live on less,
which lowers the amount you need. Both sides of the equation move in your favor at the same time.""",
   "Two arrows meeting", "BOTH SIDES MOVE")
sc("""So here's the table. Assuming you start from zero, earn five percent a year after inflation, and need twenty five times your
spending. Save ten percent of your take home pay, and it takes about fifty two years to reach financial independence. Save twenty
percent, about thirty seven years. Save thirty percent, about twenty eight years.""",
   "Savings rate table", "10% = 52 YEARS")
sc("""Save forty percent, and it takes about twenty two years. Save fifty percent, about seventeen years. Save sixty percent, about
thirteen years. Your salary doesn't appear anywhere in that table. Someone earning fifty thousand and someone earning two hundred
thousand, with the same savings rate, need about the same number of years.""",
   "Savings rate table high", "50% = 17 YEARS")
card("""Years to financial independence from zero, by savings rate, at a five percent return after inflation and a target of twenty
five times spending.""",
     {"type": "compare", "left": {"label": "save 20%", "big": "~37 years", "sub": "start at 25, done at ~62"},
      "right": {"label": "save 50%", "big": "~17 years", "sub": "start at 25, done at ~42"},
      "note": "Illustration. Returns are not guaranteed."})
sc("""Let's apply it. A household brings home fifty five hundred dollars a month after taxes. They spend thirty six hundred and save
nineteen hundred, about thirty five percent. Their yearly spending is about forty three thousand dollars, so their FI number is
around one point oh eight million.""",
   "Couple budget meeting", "A NORMAL HOUSEHOLD")
sc("""Investing nineteen hundred dollars a month at five percent after inflation, they could reach that number in about twenty four
years. Start at thirty, and they could be financially independent around fifty four. Start at twenty five, around forty nine. On a
normal income. With no inheritance and no lottery.""",
   "Calendar fifty four", "FI AROUND 49 TO 54")
card("""Nineteen hundred dollars a month invested at five percent a year after inflation, for twenty four years.""",
     {"type": "growth", "monthly": 1900, "rate": 0.05, "years": 24})
sc("""And there are middle paths. Coast FI means saving enough early that, even if you stop contributing, your investments could grow
to a full retirement by a traditional age. After that, you only need to cover current expenses, which lets you work less or take a
lower stress job. Barista FI means covering part of your expenses from investments and the rest from part time work.""",
   "Coffee shop part time work", "COAST FI AND BARISTA FI")
pr("""So the math works on a normal income. But it requires a high savings rate. And that's where psychology comes in. Angle two.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
pr("""Angle two. The psychology. Six mindset shifts behind early retirement.""")
sc("""Shift one. From money as stuff, to money as time. Your Money or Your Life suggested a powerful exercise: calculate your real hourly
wage, after taxes, commuting and work costs. Then think of every purchase in hours of your life. A two thousand dollar upgrade might
be eighty hours of work. Is it worth it?""",
   "Clock and money", "SHIFT 1: MONEY IS TIME")
sc("""Shift two. From deprivation, to optimization. Successful early retirees usually don't feel deprived. They cut ruthlessly on things
they don't care about and spend happily on things they do. One might drive an old car but travel every year. Another might cook at
home but never skip a concert.""",
   "Happy frugal person", "SHIFT 2: OPTIMIZE")
sc("""Shift three. From normal, to intentional. Normal spending in America often includes a large car payment, a big house, and
constant upgrades. Early retirement requires stepping away from normal. That can feel uncomfortable, especially when friends and family
don't understand. Knowing your why makes it easier.""",
   "Person walking different direction", "SHIFT 3: NOT NORMAL")
sc("""Shift four. From retire from, to retire to. People who plan only to escape a job often struggle after leaving. Purpose, community
and routine matter. Many early retirees end up doing meaningful work they choose, volunteering, or building something. Plan what you're
retiring to.""",
   "Volunteer helping community", "SHIFT 4: RETIRE TO")
sc("""Shift five. From all or nothing, to progress. You don't need to save sixty percent to benefit. Going from ten to twenty five percent
cuts roughly twenty years off the table. Every step up in savings rate buys you freedom, even if you never fully retire early.""",
   "Progress steps", "SHIFT 5: EVERY STEP COUNTS")
sc("""And shift six. From someday, to F you money. Even before full independence, having a year or two of expenses saved changes your
life. You can leave a toxic job, negotiate harder, or take a risk on a better opportunity. Freedom starts long before the finish line.""",
   "Confident person leaving office", "SHIFT 6: FREEDOM EARLY")

sc("""There's another psychological benefit people rarely mention. Once you know your FI number and your timeline, money stops feeling
endless and vague. You know what enough looks like. Many people say that simply having a finish line reduced their anxiety and made
everyday spending decisions much easier, because every choice connected to a clear goal.""",
   "Finish line ribbon", "KNOWING WHAT ENOUGH IS")
sc("""And it changes how you see your job. Instead of feeling trapped, you can see each paycheck as buying a piece of your future freedom.
Some people say their work became more enjoyable once they knew it had an end date they had chosen themselves.""",
   "Person at work smiling", "A CHOSEN END DATE")

ch("Why it's harder than it looks")
sc("""Let's be honest about why many people who try this quit. High savings rates require trade offs, and social pressure is real. Life
events, like children, health problems or caring for parents, can slow progress. And market crashes can make the goal feel further away
for a while.""",
   "Obstacles on path", "WHY PEOPLE QUIT")
sc("""The people who succeed usually build flexibility into the plan. They don't need a perfect straight line. They accept slower years
and faster years. They keep the big picture: a steadily rising savings rate and steady investing, over many years.""",
   "Winding mountain road", "FLEXIBILITY WINS")

# ---------------- History ----------------
ch("Where the FIRE idea came from")
sc("""The idea of retiring early by living below your means isn't new. But it took a clear form in 1992, when Vicki Robin and Joe
Dominguez published Your Money or Your Life. Dominguez had left Wall Street in his early thirties and lived on the income from
conservative investments. The book asked a simple question: is the money you earn worth the life energy you trade for it?""",
   "1990s book cover desk", "1992: YOUR MONEY OR YOUR LIFE")
sc("""In 1994, William Bengen published his withdrawal rate research. In 1998, three professors at Trinity University tested similar
ideas with different portfolios. Together, these studies gave people a practical way to estimate how much was enough.""",
   "Academic research library", "1994 AND 1998: THE MATH")
sc("""Then in the 2000s and 2010s, blogs and online forums spread the idea to a new generation. Many bloggers showed their real budgets
and savings rates. Some had high incomes. Many had ordinary ones. The common thread was always the same: a high savings rate, low cost
investing, and time.""",
   "Blog on laptop screen", "THE INTERNET ERA")
sc("""Today, FIRE has many flavors. Lean FIRE, for people who want a minimal budget. Fat FIRE, for those who want a larger cushion.
Coast FI and barista FI, for people who want a gentler path. The math is the same. Only the spending number changes.""",
   "Different paths signpost", "MANY FLAVORS")

ch("Your real hourly wage")
sc("""Let's try the most famous exercise from Your Money or Your Life. Start with your take home pay. Then subtract the costs of working:
commuting, work clothes, lunches out, the extra takeout on tired nights. Then add up all the hours your job really takes, including the
commute and recovery time.""",
   "Commuter traffic", "THE REAL COST OF WORK")
sc("""Say you take home four thousand dollars a month and work forty five hours a week, plus five hours of commuting. That's about two
hundred sixteen hours a month. Subtract four hundred dollars of work related costs, and your real wage is about sixteen dollars and
seventy cents an hour.""",
   "Calculator hourly wage", "~$16.70 AN HOUR")
sc("""Now look at a purchase. A one thousand dollar phone upgrade costs about sixty hours of your life. A forty dollar dinner, about two
and a half hours. Sometimes that's absolutely worth it. Sometimes it's not. Seeing price in hours makes the choice clearer.""",
   "Phone price tag hours", "PRICES IN HOURS")

# ---------------- Mid ----------------
ch("A quick favor")
pr("""Quick pause. If the idea of work becoming optional sounds good to you, subscribe to the channel. It's free, and it helps me keep
making videos like this. Now, the twelve step plan.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
pr("""Angle three. The playbook. Twelve steps to retire early on a normal income.""")
short("12 steps to retire early on a normal income")

step(1, "Calculate your real spending", "the number that matters",
"""Step one. Calculate your real spending.""",
[("""Look at the last twelve months of spending, including irregular costs like car repairs, gifts and travel. That yearly total is the
foundation of your FI number. Many people underestimate it by twenty percent or more.""",
  "Annual spending spreadsheet", "TWELVE MONTHS OF REALITY"),
 ("""Then multiply by twenty five, or by twenty eight to thirty if you plan to retire very early. That's your first estimate. It will
change as your life changes, and that's okay.""",
  "Target number written", "YOUR FI NUMBER")])

step(2, "Find your savings rate", "where you are now",
"""Step two. Find your savings rate.""",
[("""Add up everything you save and invest in a year, including retirement contributions and your employer match. Divide by your take
home pay plus those contributions. That's your savings rate. Many Americans save in the single digits.""",
  "Savings rate calculation", "YOUR STARTING RATE"),
 ("""Now pick a target. If you're at five percent, aim for fifteen this year. If you're at fifteen, aim for twenty five. Each step
cuts years off your timeline.""",
  "Target rising chart", "PICK THE NEXT TARGET")])

step(3, "Cut the big three first", "housing, transport, food",
"""Step three. Cut the big three first.""",
[("""Early retirees almost always have modest housing and transportation costs. A smaller home or a cheaper area, one reliable used
car instead of two new ones, and cooking at home can raise your savings rate by ten to twenty percentage points.""",
  "Small home old car", "BIG LEVERS"),
 ("""Small cuts help too, but they can't do the job alone. Cutting a few subscriptions might save a few hundred dollars a year. A
cheaper apartment might save several thousand. Focus where the big money is.""",
  "Scale small versus big", "FOCUS ON BIG MONEY")])

step(4, "Kill high interest debt", "no FI with 20% debt",
"""Step four. Kill high interest debt.""",
[("""You can't build wealth quickly while paying twenty percent interest. Pay off credit cards and other high rate debt first, while
still getting your employer match. Then roll those payments straight into investing.""",
  "Credit card payoff", "HIGH RATE DEBT FIRST"),
 ("""Lower rate debts, like some mortgages or student loans, are a judgment call. Many early retirees keep paying them on schedule and
invest the difference. Others prefer to be debt free before they leave work. Both can work.""",
  "Mortgage document", "LOW RATE: YOUR CHOICE")])

step(5, "Build a strong emergency fund", "freedom's foundation",
"""Step five. Build a strong emergency fund.""",
[("""Keep three to six months of expenses in high yield savings. With a high savings rate, a lower monthly spending number makes this
easier to reach. It protects your investments from being sold at a bad time.""",
  "Emergency fund jar", "3 TO 6 MONTHS"),
 ("""As you approach early retirement, many people build a larger cash buffer, sometimes one to two years of expenses, to avoid selling
investments during a market downturn early in retirement.""",
  "Cash buffer", "BIGGER BUFFER LATER")])

step(6, "Max your tax advantages", "keep more of every dollar",
"""Step six. Max your tax advantages.""",
[("""Use your 401k, an IRA, and a health savings account if you qualify. Tax advantaged accounts let more of your money compound. For
early retirees, a mix of traditional, Roth and taxable accounts gives flexibility later.""",
  "Tax advantaged accounts", "401K, IRA, HSA"),
 ("""An HSA can be especially powerful. Contributions can be tax deductible, growth can be tax free, and withdrawals for qualified
medical costs can be tax free too. Some early retirees pay medical costs out of pocket and let the HSA grow for decades.""",
  "Health savings account card", "THE HSA")])

step(7, "Invest in low cost index funds", "simple, diversified, cheap",
"""Step seven. Invest in low cost index funds.""",
[("""Most early retirees use broad index funds with very low fees. A total U.S. stock market fund, an international fund, and maybe a
bond fund. Or a single target date fund. Low fees matter even more over a long horizon.""",
  "Index fund screen", "LOW COST INDEX FUNDS"),
 ("""And then stay the course. Don't sell in crashes. Don't chase hot trends. The plan works because of time and consistency, not
clever trading.""",
  "Calm investor", "STAY THE COURSE")])

step(8, "Grow your income", "the accelerator",
"""Step eight. Grow your income.""",
[("""Raising income while keeping spending steady is the fastest way to increase your savings rate. A ten thousand dollar raise with no
lifestyle change can add several percentage points to your savings rate in a single year.""",
  "Promotion raise", "RAISES, NOT UPGRADES"),
 ("""Side income helps too, especially if it builds skills you can use after early retirement. Many early retirees keep a small
business or freelance work for both income and purpose.""",
  "Freelancer laptop", "SIDE INCOME")])

step(9, "Plan for healthcare", "the big early retirement cost",
"""Step nine. Plan for healthcare.""",
[("""Medicare generally starts at sixty five. Retire before that, and you need another plan. Options include the Affordable Care Act
marketplace at healthcare dot gov, a spouse's employer plan, or COBRA for a limited time after leaving a job.""",
  "Healthcare marketplace website", "BEFORE MEDICARE"),
 ("""Marketplace premium subsidies are based on income, so early retirees with modest taxable income may qualify for help. Rules change,
so check current details. Include healthcare clearly in your FI number. Underestimating it is one of the most common mistakes.""",
  "Healthcare costs calculator", "INCLUDE IT IN YOUR NUMBER")])

step(10, "Plan access before 59 and a half", "getting to your money",
"""Step ten. Plan how to access your money before fifty nine and a half.""",
[("""Retirement accounts generally have a ten percent penalty on early withdrawals before fifty nine and a half, with exceptions. Early
retirees use several strategies. A taxable brokerage account has no age limits. Roth IRA contributions, not earnings, can generally be
withdrawn anytime.""",
  "Retirement account rules", "TAXABLE AND ROTH"),
 ("""Other strategies include a Roth conversion ladder, which converts traditional funds to Roth over time, the rule of fifty five for
some 401k plans if you leave your job in or after the year you turn fifty five, and substantially equal periodic payments under IRS
rules. These can be complex, so consider professional tax advice.""",
  "Tax advisor meeting", "CONVERSION LADDER AND MORE")])

step(11, "Test drive your retirement", "before you quit",
"""Step eleven. Test drive your retirement.""",
[("""Before leaving your job, live on your planned retirement budget for a year. Include healthcare costs. If it works comfortably,
you've proven your number. If it doesn't, adjust before it's too late.""",
  "Person living on budget", "LIVE ON THE BUDGET FIRST"),
 ("""Also test the time. Take a long vacation or a sabbatical if you can. Many people discover what they want to do with their free
time, and what they miss about work.""",
  "Sabbatical travel", "TEST THE TIME TOO")])

step(12, "Stay flexible after you retire", "the safety valve",
"""Step twelve. Stay flexible after you retire.""",
[("""The early years of retirement carry the most risk. If markets fall sharply right after you retire, withdrawing too much can do lasting
damage. This is called sequence of returns risk. Flexibility is your best defense.""",
  "Market drop early retirement", "SEQUENCE RISK"),
 ("""Cut spending a little in bad years. Earn some part time income. Use your cash buffer instead of selling investments at low prices.
Small adjustments can dramatically improve the odds that your money lasts.""",
  "Part time work", "SMALL ADJUSTMENTS")])

# ---------------- Sample plan ----------------
ch("A sample plan on $70,000")
short("How a $70,000 household could retire at 50")
sc("""Let's walk through a sample plan. Sam and Jess are both thirty, with a combined income of seventy thousand dollars. After taxes
and retirement contributions, they bring home about forty six hundred a month. They contribute ten percent to their 401k plans, with a
four percent match, so about eight hundred dollars a month is invested before the paycheck arrives.""",
   "Young couple planning", "SAM AND JESS")
sc("""They rent a modest two bedroom, share one paid off car, and cook most meals. Their spending is about thirty four hundred a month.
That leaves twelve hundred a month to invest in IRAs and a taxable account. Total investing: about two thousand a month, roughly
thirty seven percent of their take home pay plus contributions.""",
   "Modest apartment couple", "~37% SAVINGS RATE")
sc("""Their yearly spending is about forty one thousand dollars, so twenty five times that is about one million dollars. Investing
two thousand a month at five percent after inflation, and using raises to keep their savings growing, they could reach financial
independence in their early fifties. Maybe sooner, if their income grows faster than their spending.""",
   "Growth chart reaching target", "FI IN EARLY 50S")
sc("""Is that a sacrifice? In some ways. They don't have two new cars or a big house. But they travel once a year, eat out on weekends,
and they're debt free. And they'll likely be free to choose what to do with their time ten or fifteen years before most of their
friends.""",
   "Couple traveling happy", "WHAT THEY GET")

# ---------------- Stories ----------------
ch("Three paths to early retirement")
sc("""Early retirement looks different for everyone. Take a teacher who earns sixty thousand dollars. Through a state pension, a 403b
and a Roth IRA, and by living modestly, she may be able to retire in her mid fifties with a pension covering part of her expenses.
Pensions can be a powerful early retirement tool, depending on the plan's rules.""",
   "Teacher in classroom", "THE TEACHER")
sc("""Or a nurse who saves forty percent of a seventy five thousand dollar salary while working night shifts and living with a roommate
for a few years. By her mid forties, she may reach coast FI, cut to part time work she enjoys, and let her portfolio grow until
traditional retirement age.""",
   "Nurse hospital hallway", "THE NURSE: COAST FI")
sc("""Or an electrician who builds a small side business. Between his union pension, his savings and part time contracting work, he
might stop full time work around fifty, and keep doing the jobs he enjoys a few days a month. That's barista FI in action.""",
   "Electrician working", "THE ELECTRICIAN: BARISTA FI")
sc("""None of these paths requires a six figure salary. All of them require a high savings rate, patience, and a plan for healthcare
and income. These are illustrations, not promises. But the principles behind them are available to almost anyone.""",
   "Three people different careers", "NO SIX FIGURE SALARY NEEDED")

sc("""What these stories share is a combination of tools. A pension or part time work covers some expenses. Investments cover the rest.
Social Security arrives later. Early retirement on a normal income usually isn't one big portfolio. It's several income sources fitted
together, with a plan for the gaps.""",
   "Puzzle pieces fitting", "SEVERAL SOURCES TOGETHER")

# ---------------- Risks ----------------
ch("The risks to plan for")
sc("""Let's be clear about the risks. Market risk: a major crash right after you retire can hurt. Inflation risk: prices can rise faster
than expected. Healthcare risk: costs before Medicare can be high and unpredictable. And longevity risk: your money may need to last
fifty years or more.""",
   "Risk warning signs", "THE FOUR RISKS")
sc("""Policy risk matters too. Tax laws, healthcare rules and retirement account rules can change. That's why many early retirees build
in margins: a lower withdrawal rate, a cash buffer, some flexibility to earn income, and a mix of account types.""",
   "Government building policy", "RULES CAN CHANGE")
sc("""None of these risks means early retirement is impossible. It means plan carefully, keep options open, and don't cut your safety
margins too thin. A plan that reaches FI two years later but with a stronger cushion is often the better plan.""",
   "Safety net", "BUILD IN MARGINS")

sc("""Of course, real life won't follow a spreadsheet exactly. Raises will come at different times, markets will rise and fall, and
expenses will surprise them. But the structure, a high savings rate, low fixed costs and steady investing, gives them a strong chance of
reaching freedom years ahead of the traditional schedule.""",
   "Spreadsheet and real life", "REAL LIFE VERSUS THE SPREADSHEET")

# ---------------- Withdrawals ----------------
ch("How the money actually comes out")
sc("""Reaching your number is only half the plan. The other half is withdrawing it wisely. A common approach is to hold a cash buffer of
one to two years of spending, and refill it from investments when markets are doing well. In bad years, you spend from the buffer and
give your investments time to recover.""",
   "Bucket system diagram", "THE BUCKET APPROACH")
sc("""Another approach is a flexible withdrawal rule. Start around three and a half percent, and adjust. In strong years, take a small
raise. In weak years, cut back slightly. Research on flexible withdrawal strategies suggests even modest adjustments can greatly improve
the odds of the money lasting.""",
   "Thermostat adjusting", "FLEXIBLE WITHDRAWALS")
sc("""And taxes matter. Withdrawals from traditional accounts are usually taxed as income. Roth withdrawals can be tax free if the rules
are met. Long term gains in taxable accounts are often taxed at lower rates. With low income in early retirement, some people pay very
little tax by drawing carefully from each type of account.""",
   "Tax buckets chart", "TAX SMART WITHDRAWALS")
sc("""This is one area where a few hours with a tax professional can pay for itself many times over, especially when combining
withdrawals, Roth conversions and healthcare subsidies, which all interact.""",
   "Tax professional meeting", "WORTH A PROFESSIONAL")

ch("Where you live matters")
sc("""Your FI number depends on your spending, and where you live has a huge effect on spending. Housing costs can vary enormously
between cities and states. A home that costs five hundred thousand dollars in one area might cost two hundred fifty thousand in
another.""",
   "Map housing prices", "LOCATION CHANGES THE NUMBER")
sc("""Some early retirees move to lower cost areas when they stop working, a strategy sometimes called geographic arbitrage. If your
spending falls from fifty thousand to forty thousand a year, your FI number falls by about two hundred fifty thousand dollars. That
could mean retiring years earlier.""",
   "Moving truck small town", "GEOGRAPHIC ARBITRAGE")
sc("""It's not for everyone. Family, friends and community matter a lot. But even a smaller move, like a cheaper neighborhood or a
smaller home, can make a real difference.""",
   "Community neighborhood", "IT'S NOT FOR EVERYONE")

ch("Early retirement as a couple")
sc("""For couples, early retirement is a shared project. Both people need to agree on the goal, the trade offs and the timeline.
Disagreements about spending are common. Talking early and often about what you each value helps avoid resentment.""",
   "Couple talking at kitchen table", "A SHARED PROJECT")
sc("""Some couples choose a staggered path. One partner leaves full time work first, maybe to care for children or start a business,
while the other keeps working and provides health insurance. That can reduce risk and make the transition smoother.""",
   "Couple different schedules", "A STAGGERED PATH")

ch("Already close?")
sc("""If you're within five years of your number, focus shifts from accumulation to preparation. Build your cash buffer. Plan healthcare.
Map out which accounts you'll draw from first. And test drive your retirement budget, if you haven't yet.""",
   "Countdown calendar", "WITHIN FIVE YEARS")
sc("""Also think about your investment mix. Some people reduce risk slightly as they approach early retirement, because a big drop just
before or after they stop working can hurt the most. A balanced mix and a cash buffer can soften that risk.""",
   "Balanced portfolio pie", "REDUCE RISK A LITTLE")

ch("Your first week checklist")
sc("""Here's what to do this week. Day one: add up your last twelve months of spending. Day two: multiply by twenty five, and write that
number down. Day three: calculate your current savings rate.""",
   "Checklist days", "DAYS 1 TO 3")
sc("""Day four: look at the savings rate table and find your current timeline. Day five: pick one big three change that would raise your
savings rate by five percentage points. Day six: increase your retirement contribution by at least one percent. Day seven: write down
what you'd do with your time if work were optional. That's your why.""",
   "Person writing in journal", "DAYS 4 TO 7")

# ---------------- Mistakes ----------------
ch("Mistakes early retirees make")
sc("""Let's look at the most common mistakes, so you can avoid them. Mistake one: underestimating spending. People often forget
irregular costs like roof repairs, new cars every ten or fifteen years, dental work, or helping family. Build these into your yearly
number.""",
   "Roof repair house", "MISTAKE 1: FORGETTING COSTS")
sc("""Mistake two: forgetting healthcare. Before Medicare, premiums and deductibles can be thousands of dollars a year. Price your real
options before you quit, not after.""",
   "Medical bills", "MISTAKE 2: HEALTHCARE")
sc("""Mistake three: retiring right at the edge. If your plan only works with perfect returns and no surprises, it's too tight. A
margin of safety, a little extra saved or a little flexibility in spending, protects you from bad luck.""",
   "Person on cliff edge", "MISTAKE 3: NO MARGIN")
sc("""Mistake four: losing identity and community. Work gives many people structure, friends and a sense of purpose. Early retirees who
thrive usually replace those things deliberately, with projects, groups, volunteering or part time work.""",
   "Community group activity", "MISTAKE 4: LOSING PURPOSE")
sc("""And mistake five: going too extreme. Some people cut spending so hard they burn out and abandon the plan. A sustainable savings
rate you can keep for fifteen years beats an extreme one you quit after two.""",
   "Burned out person", "MISTAKE 5: TOO EXTREME")

ch("What early retirement really looks like")
sc("""So what do early retirees actually do all day? Surveys and interviews with people who've reached financial independence show a
wide range. Many travel slowly, spend more time with family, exercise, cook, read, and learn new skills. Many also keep earning some
money, often from work they find meaningful.""",
   "Person gardening morning", "A NORMAL DAY")
sc("""What changes most, they often say, isn't the activities. It's the feeling. Not needing a paycheck changes how you approach work,
relationships and time. You say yes to the things you value and no to the things you don't. That freedom is the real goal.""",
   "Person smiling calm sunrise", "THE FEELING OF FREEDOM")

# ---------------- Objections ----------------
ch("But Ryan, what about...")
sc("""Objection one. I'd be bored. Some early retirees are, at first. But many find more purpose, not less, once they choose their
work. The key is planning what you're retiring to. Volunteering, learning, creating, caring for family, or meaningful part time work.""",
   "Person painting hobby", "I'D BE BORED")
sc("""Objection two. It's only for people without kids. Many families pursue FI, though children add costs and usually slow the timeline.
Families often focus on housing and transportation savings, use tax advantaged accounts fully, and aim for a slightly later but still
early finish line.""",
   "Family with kids", "WHAT ABOUT KIDS?")
sc("""Objection three. It sounds miserable. It doesn't have to be. Saving thirty or forty percent while living well is possible when
the big three are controlled. And even if you never retire early, a high savings rate gives you security, freedom and lower stress
for the rest of your life.""",
   "Happy friends dinner at home", "SOUNDS MISERABLE")

sc("""Objection four. What if the market crashes right after I retire? That's the sequence of returns risk we discussed. A cash buffer,
a conservative withdrawal rate, and willingness to earn a little or spend a little less in bad years are the main defenses. Historical
studies suggest plans with these safeguards have held up through severe downturns.""",
   "Market crash chart", "WHAT IF IT CRASHES?")
sc("""And objection five. I love my job. Wonderful. Financial independence doesn't require leaving it. It means you stay because you
want to, not because you have to. Many people find they enjoy their work more once the pressure of needing the paycheck disappears.""",
   "Happy person at work", "I LOVE MY JOB")

# ---------------- FAQ ----------------
ch("Raising your savings rate in practice")
sc("""How do people actually go from ten percent to thirty or forty percent? Usually not all at once. A common path looks like this.
Year one: track spending and get the full match, reaching about fifteen percent. Year two: pay off a car loan and keep driving the car,
redirecting the payment, reaching twenty percent.""",
   "Progress chart step by step", "YEAR 1 AND 2")
sc("""Year three: move to a cheaper apartment or take in a roommate, and send the savings to investments, reaching twenty eight percent.
Year four: get a raise and send most of it to savings, reaching thirty three percent. Year five: cut a few recurring costs and add side
income, reaching forty percent.""",
   "Rising staircase", "YEARS 3 TO 5")
sc("""Notice that none of those steps is extreme on its own. Each is one decision. But together, over five years, they can cut decades
off the path to financial independence. That's how ordinary incomes become early retirements.""",
   "Small decisions big result", "ONE DECISION AT A TIME")
sc("""And the effect compounds in a second way. Every year at a higher savings rate, you get more comfortable living on less. Many people
say they don't miss the spending they cut, and they're surprised how much calmer they feel with a growing cushion.""",
   "Calm person at home", "YOU DON'T MISS IT")

ch("Questions people ask")
pr("""Let me answer the questions I hear most about early retirement.""")
sc("""Question one. Is the four percent rule still safe? It's a historical guideline, not a guarantee. Some researchers suggest lower
starting rates for very long retirements or when valuations are high. Many early retirees use three to three and a half percent, plus
flexibility, to improve their odds.""",
   "Research chart", "IS 4% SAFE?")
sc("""Question two. What about Social Security? If you retire early, your benefits may be lower, because they're based on your highest
thirty five years of earnings. But you'll likely still receive something later. Many early retirees treat Social Security as a bonus
that reduces how much they need to withdraw later in life. You can check your estimate at ssa dot gov.""",
   "Social Security website", "SOCIAL SECURITY?")
sc("""Question three. Should I pay off my house before retiring early? It can lower your spending and your FI number, which many people
like. But it ties up money that could be invested. Many early retirees aim to have their mortgage paid off around the time they retire,
for peace of mind.""",
   "Paid off house", "PAY OFF THE HOUSE?")
sc("""Question four. Do I need a financial advisor? Not necessarily, but a fee only fiduciary or a tax professional can be very helpful
for withdrawal strategies, Roth conversions and healthcare subsidies. Even one or two planning sessions can prevent costly
mistakes.""",
   "Advisor meeting", "AN ADVISOR?")
sc("""And question five. What if I start late? Even at forty or forty five, raising your savings rate to thirty or forty percent can
significantly move your retirement date. You may not retire at forty five, but you could reach financial independence well before a
traditional retirement age.""",
   "Middle aged person planning", "STARTING LATE?")

sc("""Question six. What about the people who say early retirement is a myth? Some critics point out that many FIRE bloggers earn money
from their blogs, so they never really stopped working. That's fair. But many people use the same principles quietly, to switch to
work they love or cut back to part time. Financial independence is about options, not idleness.""",
   "Debate discussion", "IS IT A MYTH?")
sc("""And question seven. What's the single most important number? Your savings rate. It controls how fast you build your portfolio and
how much you need. Raise it, keep it high, and give it time. Everything else is detail.""",
   "Savings rate gauge high", "THE ONE NUMBER")

# ---------------- Recap ----------------
ch("Recap: the 12 steps")
short("Retire early on a normal income: the 60-second version")
sc("""Quick recap. Your FI number is roughly twenty five times your yearly spending, or more if you retire very early. The time it takes
depends mostly on your savings rate. Ten percent takes about fifty years. Fifty percent takes about seventeen.""",
   "Checklist clipboard", "THE NUMBERS")
sc("""The twelve steps. Calculate your real spending. Find your savings rate. Cut the big three. Kill high interest debt. Build a strong
emergency fund. Max your tax advantages. Invest in low cost index funds. Grow your income. Plan for healthcare. Plan access before
fifty nine and a half. Test drive your retirement. And stay flexible after you retire.""",
   "Staircase twelve steps", "THE 12 STEPS")

sc("""One last thought. You don't have to decide today whether you want to retire at forty five, fifty five or never. Raising your
savings rate gives you the option. And options, more than any number, are what financial freedom really feels like.""",
   "Open road horizon", "OPTIONS")

# ---------------- Close ----------------
ch("What to do next")
pr("""This week, calculate two numbers: your yearly spending and your savings rate. Those two numbers tell you more about your future
than your salary ever will. And watch my video on the complete budget system. It's how you raise that savings rate. I'm Ryan Rover.
See you in the next one.""")

save("video56", "How to Retire Early on a Normal Income", [
    "William P. Bengen, Determining Withdrawal Rates Using Historical Data, Journal of Financial Planning (1994)",
    "Cooley, Hubbard and Walz, Retirement Savings: Choosing a Withdrawal Rate That Is Sustainable (Trinity study, 1998)",
    "Vicki Robin and Joe Dominguez, Your Money or Your Life (1992)",
    "IRS, early withdrawal rules, Roth IRA, HSA, rule of 55 and substantially equal periodic payments",
    "HealthCare.gov, marketplace coverage and premium tax credits",
    "Social Security Administration, ssa.gov benefit estimates",
    "Savings rate table and growth figures: stated illustrative math at a 5% return after inflation, target 25x spending",
], "retire early on a normal income: numbers, psychology, playbook")
