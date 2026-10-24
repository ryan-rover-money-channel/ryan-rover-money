import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

body_hook = None  # set right before item() to start a Short at its first explained scene

def item(n, title, sub, card_text, scenes):
    """scenes: list of (text, query, caption) shown after the list card."""
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"LESSON {n}")
    global body_hook
    if body_hook:
        short(body_hook); body_hook = None
    for text, q, c in scenes:
        sc(text, q, c)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. How much money do you need to never work again? Most people have no idea. They guess a number like
one million or five million and hope it's enough. But there's a simple rule of thumb that gives you a real starting point in
about five seconds. It's called the four percent rule. Today I'll show you how it works, where it came from, where it breaks,
and how to use it to build your own freedom number.""")
short("Multiply your yearly spending by twenty five. That's your freedom number.")
card("""Here's the rule. Take what you spend in a year and multiply it by twenty five. If you spend forty thousand dollars a year,
your target is one million dollars. Why twenty five? Because four percent of one million is forty thousand. The idea is that you
could withdraw about four percent in your first year of retirement, adjust for inflation after that, and have a good chance of
your money lasting around thirty years.""",
     {"type": "compare", "left": {"label": "You spend each year", "big": "$40K", "sub": "living costs"},
      "right": {"label": "Your freedom number", "big": "$1M", "sub": "25 times spending"},
      "note": "a rule of thumb from historical U.S. data, not a guarantee"})
sc("""That simple multiplication changes how people think about retirement. Suddenly, freedom isn't a vague dream. It's a number
tied directly to your lifestyle. And it reveals something powerful. Lowering your spending doesn't just help you save more. It also
lowers the number you need. Every one thousand dollars you cut from yearly spending reduces your target by about twenty five
thousand dollars.""",
   "Person calculating on notepad", "SPEND LESS, NEED LESS")
sc("""We'll look at the four percent rule from three angles. First, the numbers. Where the rule came from, what it assumes and how
risky it really is. Second, the psychology. Why spending your savings is so hard, and why so many people get the number wrong.
And third, the playbook. How to calculate your own number, reach it and make it last. Reminder, this is education, not financial
advice, and nothing about the future is guaranteed.""",
   "Three paths in a park", "THREE ANGLES")
pr("""Let's start with the numbers. And first, where did this rule actually come from?""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our numbers. The four percent rule comes from William Bengen's 1994 study in the Journal of Financial Planning, and was
supported by the 1998 Trinity study by Philip Cooley, Carl Hubbard and Daniel Walz. Recent safe withdrawal research comes from
Morningstar. Social Security figures come from the Social Security Administration. Growth examples use stated average returns, as
illustrations, not promises.""",
   "Research papers on desk", "OUR NUMBERS")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Seven lessons about what the four percent rule really says, and what it doesn't.""")

item(1, "Where the rule came from", "Bengen's 1994 study",
"""Lesson number one. Where the four percent rule came from.""", [
("""In 1994, a financial planner named William Bengen asked a simple question. How much can a retiree withdraw from savings each
year without running out of money? He tested historical U.S. market data going back to 1926, imagining retirees starting in every
possible year.""", "Financial planner at old computer", "BENGEN, 1994"),
("""He assumed a portfolio split between stocks and intermediate term government bonds. The retiree withdrew a set percentage in
year one, then increased the dollar amount each year with inflation, no matter what markets did.""", "Pie chart stocks and bonds", "STOCKS AND BONDS"),
("""His finding was that a first year withdrawal of about four percent, adjusted for inflation afterward, lasted at least thirty
years in every historical period he tested, including retirements that began just before the Great Depression and the high
inflation of the 1970s.""", "Historical timeline of crises", "LASTED 30 YEARS IN EVERY PERIOD"),
("""Four years later, three professors at Trinity University published a similar study, often called the Trinity study. It also
found that withdrawal rates around four percent had high historical success rates over thirty years for portfolios with a large
share of stocks.""", "University building", "THE TRINITY STUDY"),
("""Bengen himself later suggested that with more asset classes, slightly higher starting rates might have worked historically.
But four percent stuck, because it's simple and memorable. It became one of the most famous rules in personal finance.""", "Number four on sign", "SIMPLE AND MEMORABLE"),
])

item(2, "The times twenty five rule", "turning spending into a target",
"""Lesson number two. Turn your spending into a target.""", [
("""The flip side of a four percent withdrawal is the times twenty five rule. If four percent of your portfolio covers one year of
spending, then you need twenty five years of spending saved. Spend thirty thousand a year, you need about seven hundred fifty
thousand. Spend sixty thousand, you need about one point five million.""", "Table of spending and targets", "$30K NEEDS $750K, $60K NEEDS $1.5M"),
("""Notice that this uses spending, not income. Someone earning two hundred thousand dollars but spending one hundred eighty
thousand needs four and a half million dollars. Someone earning sixty thousand but spending thirty thousand needs only seven
hundred fifty thousand. Your lifestyle sets your target.""", "Two households compared", "SPENDING SETS THE TARGET"),
("""It's also about spending in retirement, which may differ from today. Some costs disappear, like commuting or a mortgage that's
paid off. Others may rise, like health care and travel.""", "Retiree budget sheet", "RETIREMENT SPENDING CHANGES"),
("""And the money that counts is the money coming from your portfolio. Income from Social Security, a pension or part time work
reduces how much you need to withdraw, and therefore how much you need saved.""", "Social Security card", "OTHER INCOME LOWERS THE TARGET"),
("""Try this. Add up your yearly spending, subtract any guaranteed retirement income you expect, and multiply what's left by twenty
five. That's your first draft freedom number.""", "Person with calculator", "YOUR FIRST DRAFT NUMBER"),
])

body_hook = "Two retirees. Same returns. One ends up with far less. Here's why."
item(3, "Sequence of returns risk", "bad timing can sink a plan",
"""Lesson number three. The order of returns matters.""", [
("""When you're saving, the order of good and bad years doesn't change your final result much if you just hold. But when you're
withdrawing, it matters enormously. This is called sequence of returns risk.""", "Two lines diverging", "SEQUENCE RISK"),
("""Here's an illustration. Two retirees each start with one million dollars and withdraw forty thousand a year. Both experience
exactly the same twelve yearly returns, just in a different order. For one, the two bad years come first. For the other, they come
last.""", "Two retirees side by side", "SAME RETURNS, DIFFERENT ORDER"),
("""After twelve years, the retiree who faced the bad years first has roughly seven hundred forty thousand dollars left. The one who
faced them last has roughly one million. Same average, very different result, because selling investments to fund withdrawals after
a crash locks in losses.""", "Two account balances", "$740K VS $1M"),
("""This is why the first five to ten years of retirement are often called the danger zone. A big crash early on can do lasting
damage to a portfolio that's also funding withdrawals.""", "Warning zone on timeline", "THE DANGER ZONE"),
("""Many retirees manage this risk by holding a few years of spending in bonds or cash, so they don't have to sell stocks during a
downturn, and by being willing to cut spending a little in bad years.""", "Cash reserve bucket", "A CASH BUFFER HELPS"),
])

item(4, "What success really means", "the rule isn't a guarantee",
"""Lesson number four. Four percent isn't a guarantee.""", [
("""The four percent rule is based on U.S. history. It worked in every historical thirty year period Bengen tested, but there's no
promise the future will look like the past. Future returns could be higher or lower.""", "Crystal ball", "HISTORY ISN'T A PROMISE"),
("""Some researchers have argued that future returns may be lower than historical averages, which would make four percent riskier.
Morningstar's recent research, for example, has estimated a safe starting withdrawal rate for new retirees in the high three percent
range, depending on assumptions.""", "Research report page", "SOME SUGGEST LOWER RATES"),
("""Others point out that in most historical periods, a four percent withdrawal left retirees with much more money than they started
with. The rule was designed around the worst cases, so in typical cases it may be conservative.""", "Growing balance in retirement", "OFTEN CONSERVATIVE"),
("""The truth is that four percent is a reasonable starting point, not a precise answer. Think of it as a guide for planning, not a
law of physics.""", "Compass on map", "A GUIDE, NOT A LAW"),
("""Try this. Run your numbers at both three and a half and four percent. If you'd be comfortable at either, you have a margin of
safety.""", "Two calculations side by side", "TEST 3.5% AND 4%"),
])

item(5, "Time horizon", "thirty years isn't forever",
"""Lesson number five. The rule assumes about thirty years.""", [
("""Bengen's research focused on retirements lasting around thirty years, which fits someone retiring around sixty five. But
someone retiring at forty might need their money to last fifty years or more.""", "Timeline thirty versus fifty years", "30 YEARS VS 50 YEARS"),
("""Longer retirements generally require lower withdrawal rates. Many early retirement planners use three to three and a half
percent for very long horizons, which means saving roughly twenty nine to thirty three times yearly spending instead of twenty five.""", "Larger savings target", "EARLY RETIREES OFTEN USE 3 TO 3.5%"),
("""Life expectancy matters too. Many people live into their nineties, especially couples, where at least one partner often lives a
long time. Planning only to age eighty five could leave you short.""", "Elderly couple smiling", "PLAN FOR A LONG LIFE"),
("""On the other hand, someone retiring at seventy may be able to withdraw a bit more, because their money doesn't need to last as
long.""", "Retiree at seventy", "LATER RETIREMENT, HIGHER RATE"),
("""Try this. Decide how many years your money needs to last, from your planned retirement age to at least ninety five, and adjust your
withdrawal rate to match.""", "Calendar to age 95", "PLAN TO 95"),
])

item(6, "Stocks and bonds mix", "too safe can be risky",
"""Lesson number six. Your investment mix matters.""", [
("""The four percent rule assumed a meaningful share of stocks, often fifty to seventy five percent. Stocks provide growth that helps
your money keep up with inflation over decades.""", "Pie chart with stocks", "STOCKS PROVIDE GROWTH"),
("""Many people assume retirement money should be entirely in safe investments. But a portfolio that's too conservative may not grow
fast enough to support inflation adjusted withdrawals for thirty years. In Bengen's research, very low stock allocations had lower
safe withdrawal rates.""", "Cash only jar", "TOO SAFE CAN BE RISKY"),
("""Bonds and cash still play an important role. They reduce volatility and provide money to spend during stock market downturns,
helping with sequence risk.""", "Balanced scale", "BONDS REDUCE SWINGS"),
("""The right mix depends on your age, other income and comfort with ups and downs. Target date funds and balanced funds offer simple
ready made mixes.""", "Target date fund brochure", "SIMPLE READY MADE MIXES"),
("""Try this. Look at your current mix of stocks and bonds and ask whether it fits your timeline. If you're decades from retirement, a
very conservative mix may be holding you back.""", "Person reviewing portfolio", "CHECK YOUR MIX"),
])

item(7, "Inflation and taxes", "the hidden costs",
"""Lesson number seven. Don't forget inflation and taxes.""", [
("""The four percent rule raises your withdrawals with inflation each year, which is crucial. At three percent inflation, prices
roughly double in about twenty four years. Forty thousand dollars of spending today could mean around eighty thousand later in
retirement.""", "Rising price tags", "PRICES CAN DOUBLE"),
("""Taxes are another factor. The rule is typically calculated before taxes. Withdrawals from traditional four oh one ks and IRAs are
usually taxed as income, while qualified Roth withdrawals are tax free and taxable accounts may face capital gains taxes.""", "Tax forms", "WITHDRAWALS MAY BE TAXED"),
("""So if you need forty thousand dollars a year to spend, you may need to withdraw more than that from pre tax accounts to cover
taxes. Your freedom number should account for this.""", "Gross versus net income", "PLAN FOR TAXES"),
("""Having money in different types of accounts, pre tax, Roth and taxable, can give you flexibility to manage taxes in retirement.""", "Three account buckets", "TAX FLEXIBILITY"),
("""Try this. Estimate how much of your retirement savings is in pre tax accounts, and add a cushion to your freedom number for
taxes.""", "Person adding cushion", "ADD A TAX CUSHION"),
])

pr("""That's angle one. Where the rule came from, the times twenty five rule, sequence risk, no guarantees, time horizon, investment
mix, and inflation and taxes. Now angle two. The psychology.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
sc("""The math of retirement is only half the challenge. The other half is emotional. Saving for decades and then spending your savings
feels very different from what most people expect. Here are seven psychological lessons about the four percent rule.""",
   "Brain illustration", "THE EMOTIONAL HALF")

item(8, "The number makes it real", "a vague goal becomes a target",
"""Lesson number eight. A number turns a dream into a plan.""", [
("""Most people approach retirement with vague hopes. Someday, enough, comfortable. Without a number, it's hard to know whether you're
on track, so many people either worry constantly or ignore it entirely.""", "Foggy road", "VAGUE GOALS CREATE ANXIETY"),
("""The four percent rule gives you a concrete target. Once you know you need, say, one point two million dollars, you can calculate
how much to save each month and track your progress.""", "Progress bar toward goal", "A CONCRETE TARGET"),
("""Research on goal setting, including work by psychologists Edwin Locke and Gary Latham, has found that specific, challenging goals
tend to lead to better performance than vague goals like do your best.""", "Target with arrow", "SPECIFIC GOALS WORK BETTER"),
("""Tracking progress toward your number can be motivating. Watching yourself move from ten percent to twenty five percent to fifty
percent of the way there makes the journey feel real.""", "Milestone chart", "TRACK YOUR PERCENTAGE"),
("""Try this. Calculate what percentage of your freedom number you have today. Write it down and check it once a year.""", "Notebook with percentage", "WHAT PERCENT ARE YOU?"),
])

body_hook = "Many retirees are scared to spend money they spent decades saving."
item(9, "Fear of spending", "the saver's dilemma",
"""Lesson number nine. Spending savings is surprisingly hard.""", [
("""After decades of saving, many retirees find it emotionally difficult to start spending. Watching a balance go down can feel like
failure, even when it's exactly the plan.""", "Retiree hesitating at checkout", "SPENDING FEELS LIKE FAILURE"),
("""Research by the Employee Benefit Research Institute and others has found that many retirees spend down their savings slowly, and
some keep much of their savings intact well into retirement, often out of caution and uncertainty.""", "Untouched savings account", "MANY UNDERSPEND"),
("""Caution can be wise, but underspending has a cost too. Money saved for decades might never be used for the experiences and
security it was meant to provide.""", "Unused travel brochure", "UNDERSPENDING HAS A COST"),
("""A clear withdrawal plan, like the four percent rule, can actually make spending easier. It gives you permission to spend a set
amount with confidence.""", "Retiree enjoying trip", "A PLAN GIVES PERMISSION"),
("""Try this. If you're retired or close, write down what a safe yearly spending amount looks like for you, and give yourself
permission to use it.""", "Written spending plan", "GIVE YOURSELF PERMISSION"),
])

item(10, "Lifestyle creep", "the moving target",
"""Lesson number ten. Lifestyle creep moves the finish line.""", [
("""As income grows, spending often grows with it. Bigger house, nicer car, more expensive vacations. Each upgrade feels small, but
together they raise your yearly spending.""", "Upgraded car and house", "SPENDING GROWS WITH INCOME"),
("""Because of the times twenty five rule, every permanent ten thousand dollar increase in yearly spending raises your freedom number
by about two hundred fifty thousand dollars. Lifestyle creep doesn't just reduce what you save. It moves the finish line further away.""", "Finish line moving away", "$10K MORE SPENDING, $250K MORE NEEDED"),
("""The opposite is also true. Reducing yearly spending by ten thousand dollars lowers the target by about two hundred fifty thousand,
and frees up money to save. It's a double benefit.""", "Finish line moving closer", "THE DOUBLE BENEFIT"),
("""This doesn't mean never upgrading your life. It means making upgrades deliberately, knowing what each one costs in years of work.""", "Person thinking about purchase", "UPGRADE DELIBERATELY"),
("""Try this. Before any big recurring expense, multiply its yearly cost by twenty five. That's what it adds to your freedom number.""", "Calculator multiplying", "MULTIPLY BY 25"),
])

pr("""Quick pause. If knowing your freedom number sounds useful, please subscribe to Ryan Rover Money. It's free, and it helps us keep
making these. Now, lesson eleven.""")

item(11, "One more year syndrome", "never feeling ready",
"""Lesson number eleven. One more year syndrome.""", [
("""Many people reach their number and still don't stop working. They think, just one more year, to be safe. Then another. And
another. The finish line keeps moving because fear keeps moving it.""", "Calendar pages flipping", "JUST ONE MORE YEAR"),
("""Some extra cushion can be smart, especially with uncertain markets. But years are the one resource you can't get back. Working
years longer than necessary trades healthy, active years for money you may never need.""", "Hourglass", "YEARS ARE PRICELESS"),
("""A plan with flexibility, like being willing to cut spending in bad years or earn some part time income, can give you the
confidence to stop when you've reached a reasonable target.""", "Flexible plan diagram", "FLEXIBILITY BUILDS CONFIDENCE"),
("""It also helps to think about what you're retiring to, not just from. People with clear plans for their time often feel more ready
to make the leap.""", "Person gardening happily", "RETIRE TO SOMETHING"),
("""Try this. Write down what would make you feel ready to stop full time work. A number, a buffer, a plan for your days. Then hold
yourself to it.""", "Written checklist", "DEFINE READY"),
])

item(12, "Freedom without full retirement", "the power of options",
"""Lesson number twelve. Financial freedom doesn't have to mean stopping work.""", [
("""Many people who reach financial independence keep working, but on their own terms. Part time, a passion project, a lower stress job
or starting a business. The freedom is in the choice.""", "Person working on passion project", "FREEDOM IS CHOICE"),
("""Even partial financial independence is powerful. If your savings could cover half your spending, you could take a lower paying
job you love, or work fewer hours.""", "Half filled progress bar", "PARTIAL FREEDOM COUNTS"),
("""Some people use the idea of coast FIRE, where they've saved enough that their investments could grow to their full number by
traditional retirement age, even without more contributions. From there, they only need to cover current expenses.""", "Car coasting downhill", "COAST FIRE"),
("""Earning even a small income in early retirement can dramatically reduce how much you need to withdraw, making your money last much
longer.""", "Part time work income", "A LITTLE INCOME GOES FAR"),
("""Try this. Calculate what percentage of your spending your savings could cover today using four percent. That's your current level
of freedom.""", "Percentage on screen", "YOUR FREEDOM LEVEL"),
])

item(13, "Comparison and enough", "defining your own number",
"""Lesson number thirteen. Define enough for yourself.""", [
("""Some people chase five or ten million because that's what wealthy people seem to have. But your freedom number depends only on
your own spending, not anyone else's.""", "Mountain of money versus modest home", "YOUR NUMBER, NOT THEIRS"),
("""Morgan Housel writes that one of the hardest financial skills is getting the goalpost to stop moving. Without a sense of enough,
no amount ever feels sufficient.""", "Goalpost on field", "STOP MOVING THE GOALPOST"),
("""A clear number tied to a lifestyle you actually want can bring peace. You know what you're working toward, and you know when
you've arrived.""", "Peaceful person at sunset", "ENOUGH BRINGS PEACE"),
("""That doesn't mean you can't want more. It means the more is a choice, not a requirement for feeling secure.""", "Person smiling with options", "MORE IS A CHOICE"),
("""Try this. Describe your ideal ordinary week in retirement, then estimate what it costs. That's the foundation of your enough.""", "Week planner", "DESCRIBE YOUR IDEAL WEEK"),
])

item(14, "Uncertainty and flexibility", "plans that bend",
"""Lesson number fourteen. Flexible plans beat rigid ones.""", [
("""The original four percent rule assumes you raise withdrawals with inflation every year, no matter what. Real people don't usually
behave that rigidly. They cut back in bad years and spend more in good ones.""", "Flexible bridge", "REAL PEOPLE ADJUST"),
("""Research on flexible withdrawal strategies, such as guardrail approaches developed by planners Jonathan Guyton and William
Klinger, suggests that being willing to trim spending after poor markets can support higher starting withdrawal rates.""", "Guardrails on road", "GUARDRAILS"),
("""Flexibility reduces anxiety. If you know you'd cut travel for a year or two during a crash, a bad market feels less like a threat
to your entire retirement.""", "Calm retiree reading news", "FLEXIBILITY REDUCES FEAR"),
("""Separating spending into needs and wants helps. Cover essential needs with stable income and safer assets, and fund wants from
the riskier portfolio.""", "Needs and wants lists", "NEEDS VERSUS WANTS"),
("""Try this. List which retirement expenses you could reduce for a year if markets fell sharply. That list is your safety valve.""", "Safety valve illustration", "YOUR SAFETY VALVE"),
])

pr("""That's angle two. The number makes it real, fear of spending, lifestyle creep, one more year, freedom without full retirement,
defining enough and flexibility. Now angle three. The playbook.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
sc("""Let's turn the four percent rule into a practical plan. Six moves to calculate your number, reach it and make it last.""",
   "Toolbox on table", "SIX MOVES")

item(15, "Track your real spending", "the foundation of the number",
"""Move number fifteen. Track your real spending.""", [
("""Your freedom number is only as good as your spending estimate. Many people underestimate what they spend by a lot, because small
purchases and irregular expenses add up.""", "Receipts pile", "MOST PEOPLE UNDERESTIMATE"),
("""Look at at least three to six months of bank and credit card statements, plus yearly expenses like insurance, gifts, car repairs
and holidays.""", "Bank statements on table", "USE REAL STATEMENTS"),
("""Then estimate how spending will change in retirement. Remove work costs and add things like health insurance before Medicare, which
generally starts at sixty five.""", "Health insurance card", "ADJUST FOR RETIREMENT"),
("""Budgeting apps or a simple spreadsheet can help. The goal isn't perfection, just a realistic number. Many people find it helpful to
sort spending into three groups, essentials like housing and food, regular extras like dining out, and one time costs like a new roof.
Each group behaves differently in retirement.""", "Budgeting app", "REALISTIC, NOT PERFECT"),
("""Try this. Add up last year's total spending from your statements. It might surprise you.""", "Person shocked at total", "ADD UP LAST YEAR"),
])

item(16, "Calculate your freedom number", "spending times twenty five",
"""Move number sixteen. Calculate your freedom number.""", [
("""Start with expected yearly retirement spending. Subtract guaranteed income, like Social Security or a pension. Multiply what's left
by twenty five, or by twenty nine to thirty three for very long early retirements.""", "Formula on whiteboard", "THE FORMULA"),
("""Example. Spending of sixty thousand dollars, minus twenty four thousand from Social Security, leaves thirty six thousand to come from
investments. Times twenty five equals nine hundred thousand dollars.""", "Example calculation", "$36K TIMES 25 = $900K"),
("""Add a cushion for taxes if much of your money is in pre tax accounts, and consider a buffer for big future costs like home repairs
or helping family.""", "Cushion illustration", "ADD CUSHIONS"),
("""Revisit your number every few years. Your life, spending and the economy will change.""", "Calendar with review dates", "REVISIT IT"),
("""Try this. Do the calculation today and write your freedom number somewhere you'll see it.""", "Number written on sticky note", "WRITE YOUR NUMBER"),
])

body_hook = "Social Security can cut the amount you need to save by hundreds of thousands."
item(17, "Factor in Social Security", "the built in pension",
"""Move number seventeen. Factor in Social Security.""", [
("""Social Security is an inflation adjusted income stream for life, something very valuable. In 2025, the average retired worker
benefit was around two thousand dollars a month, according to the Social Security Administration.""", "Social Security statement", "AROUND $2,000 A MONTH ON AVERAGE"),
("""Twenty four thousand dollars a year of Social Security would otherwise require about six hundred thousand dollars of savings under
the four percent rule. That's a big reduction in what you need to save.""", "Savings reduced", "WORTH ABOUT $600K OF SAVINGS"),
("""When you claim matters. Claiming before full retirement age reduces benefits, while waiting past it, up to age seventy, increases
them. For many people, delaying can significantly boost lifetime income.""", "Age timeline 62 to 70", "WHEN YOU CLAIM MATTERS"),
("""You can see your estimated benefits by creating an account on the Social Security Administration's website. Your statement shows
estimates at different claiming ages, so you can see exactly how much waiting could add to your monthly check, and how that changes the
amount you need to save.""", "SSA website on laptop", "CHECK YOUR ESTIMATE"),
("""Try this. Log in to your Social Security account, check your estimated benefit and subtract it from your retirement spending before
calculating your number.""", "Person logging in", "SUBTRACT IT"),
])

item(18, "Close the gap", "how fast you can get there",
"""Move number eighteen. Build a plan to reach your number.""", [
("""Once you know your number, you can estimate how long it'll take. At a seven percent average yearly return, investing one thousand
dollars a month could reach one million dollars in roughly twenty seven to twenty eight years, starting from zero.""", "Timeline to one million", "$1,000 A MONTH: ABOUT 28 YEARS"),
("""Two thousand dollars a month could get there in roughly twenty years. Three thousand a month, in roughly fifteen and a half years.
Your savings rate is one of the biggest levers you control.""", "Faster timelines chart", "$2,000: 20 YEARS, $3,000: 15.5"),
("""Raising income, cutting big expenses and investing raises are the most powerful ways to speed things up. The big three expenses for
most households are housing, transportation and food. Small wins there can shave years off your timeline, far more than skipping the
occasional coffee.""", "Three levers", "THREE BIG LEVERS"),
("""Use tax advantaged accounts first, like four oh one ks, IRAs and HSAs, so more of your money compounds.""", "Retirement accounts", "TAX ADVANTAGED FIRST"),
("""Try this. Use an online compound interest calculator with your current savings, monthly amount and seven percent to see your estimated
timeline.""", "Online calculator", "SEE YOUR TIMELINE"),
])

item(19, "Protect the early years", "manage sequence risk",
"""Move number nineteen. Protect the first years of retirement.""", [
("""Because sequence risk is greatest early on, many retirees hold one to three years of spending in cash or short term bonds when they
retire. If markets crash, they spend from that buffer instead of selling stocks low.""", "Cash buffer bucket", "A 1 TO 3 YEAR BUFFER"),
("""Some people use a bucket strategy. Near term money in cash, medium term money in bonds and long term money in stocks.""", "Three buckets", "THE BUCKET STRATEGY"),
("""Others reduce their stock allocation around retirement and gradually increase it again later, an approach some researchers have
studied as a way to manage sequence risk.""", "Changing allocation chart", "ADJUST YOUR MIX"),
("""Having part time income or flexibility in the first few years can also protect your portfolio enormously. Even ten or fifteen thousand
dollars a year from consulting or a part time job means you withdraw less during the years when a crash would hurt the most.""", "Part time worker", "EARLY FLEXIBILITY"),
("""Try this. If you're within five years of retirement, plan how you'd cover two years of spending without selling stocks.""", "Planning worksheet", "PLAN TWO YEARS"),
])

item(20, "Review and adjust", "the rule is a starting point",
"""Move number twenty. Review and adjust every year.""", [
("""The four percent rule is a starting point, not autopilot. Each year in retirement, review your portfolio, spending and the market.""", "Annual review meeting", "REVIEW EVERY YEAR"),
("""If your portfolio has grown a lot, you may be able to spend more. If it has fallen sharply, a small temporary cut can help protect
your plan.""", "Adjusting dial", "ADJUST AS NEEDED"),
("""Many retirees work with a fee only fiduciary financial planner for these decisions, especially around taxes, Social Security and
withdrawals.""", "Advisor meeting", "GET HELP IF NEEDED"),
("""The goal isn't to follow a rule perfectly. It's to spend confidently while making sure your money lasts. A plan that you review,
understand and adjust will serve you far better than any single number followed blindly for thirty years.""", "Confident retiree", "SPEND WITH CONFIDENCE"),
("""Try this. Pick an annual review date and write down the questions you'll ask yourself each year.""", "Calendar reminder", "PICK A REVIEW DATE"),
])

# ---------------- Examples ----------------
ch("Three freedom numbers")
pr("""Let's run the four percent rule for three different households, so you can see how much the number depends on lifestyle and other
income. These are simplified illustrations, before taxes, just to show how the math works.""")
sc("""Household one is a single person who spends thirty thousand dollars a year, owns a modest paid off condo and expects about twenty
thousand dollars a year from Social Security. That leaves ten thousand dollars a year to come from savings. Times twenty five, their
freedom number is about two hundred fifty thousand dollars. Far less than the million most people imagine.""",
   "Single person in small condo", "HOUSEHOLD 1: ABOUT $250K")
sc("""Household two is a couple spending sixty thousand dollars a year, with combined Social Security of about thirty six thousand. They
need twenty four thousand a year from savings, so their freedom number is about six hundred thousand dollars. If they downsize their home
and cut yearly spending to fifty thousand, the number falls to about three hundred fifty thousand.""",
   "Couple in suburban home", "HOUSEHOLD 2: ABOUT $600K")
sc("""Household three is a family that spends one hundred twenty thousand dollars a year and wants to retire at fifty, long before Social
Security begins. For a long retirement they use three and a half percent, so they divide by point zero three five. Their freedom number is
roughly three point four million dollars. Lifestyle and timing changed the target enormously.""",
   "Family with large house", "HOUSEHOLD 3: ABOUT $3.4M")
sc("""Same rule, three completely different answers, from a quarter of a million to more than three million dollars. That's why copying
someone else's retirement number makes little sense. The only number that matters is the one built from your spending, your income and
your timeline.""",
   "Three different numbers on board", "YOUR NUMBER IS PERSONAL")

# ---------------- By age ----------------
ch("Using the rule at every age")
sc("""In your twenties and thirties, the four percent rule is mostly a motivation tool. Your future spending is uncertain, but knowing that
roughly twenty five times spending is the goal helps you see why saving early matters, and why keeping your lifestyle in check gives you
options later.""",
   "Young professional planning", "20s AND 30s: MOTIVATION")
sc("""In your forties and fifties, the rule becomes a progress check. You have a clearer picture of your spending, your Social Security
estimate and your savings. This is the time to compare where you are with where you need to be, and to adjust contributions, catch up
savings and your retirement age.""",
   "Middle aged person reviewing accounts", "40s AND 50s: PROGRESS CHECK")
sc("""In your sixties and beyond, the rule turns into a spending guide. It helps you decide how much to withdraw each year, when to claim
Social Security and how much to keep in safer assets. Many retirees use it as a starting point, then adjust each year with flexibility.""",
   "Retired couple at kitchen table", "60s AND BEYOND: SPENDING GUIDE")

# ---------------- Worksheet ----------------
ch("Your freedom number in five steps")
pr("""Let's put the whole video into a simple five step worksheet you can do tonight with a pen and paper.""")
sc("""Step one. Write down what you spend in a typical year, using real bank and credit card statements, not a guess. Include the irregular
costs people forget, like car repairs, gifts, annual subscriptions, insurance and holidays. If you're unsure, add ten percent. This number is
the foundation for everything else, so it's worth getting right.""",
   "Pen and paper worksheet", "STEP 1: REAL SPENDING")
sc("""Step two. Adjust that number for retirement. Cross out costs that will likely disappear, like commuting, work clothes, retirement
contributions or a mortgage you'll have paid off. Add costs that may appear, like health insurance before Medicare, more travel or helping
family. What's left is your estimated retirement spending.""",
   "Crossing out expenses", "STEP 2: RETIREMENT SPENDING")
sc("""Step three. Subtract guaranteed income. Look up your estimated Social Security benefit, and add any pension or reliable rental income.
Subtract the yearly total from your retirement spending. The result is the amount your investments need to provide each year.""",
   "Subtracting income on paper", "STEP 3: SUBTRACT GUARANTEED INCOME")
sc("""Step four. Multiply. Use twenty five for a traditional thirty year retirement, or around twenty nine to thirty three for a very long
early retirement. Then add a cushion if most of your savings are in pre tax accounts, since withdrawals there are usually taxed. That's your
freedom number.""",
   "Multiplication on worksheet", "STEP 4: MULTIPLY AND CUSHION")
sc("""Step five. Compare your freedom number with what you have today, and work out the gap. Then decide how you'll close it, by saving
more, earning more, spending less, working a little longer or combining all four. Write the plan next to the number, and revisit both once a
year.""",
   "Plan written next to number", "STEP 5: CLOSE THE GAP")

# ---------------- Story ----------------
ch("Two retirees")
short("Two retirees saved the same amount. Only one panicked.")
sc("""Imagine two retirees, each with one million dollars, each planning to withdraw forty thousand dollars a year. In their second year
of retirement, the market drops thirty percent. Both portfolios fall sharply, and both feel scared.""",
   "Two retirees watching news", "SAME START, SAME CRASH")
sc("""The first retiree panics, sells all their stocks and moves everything to cash. When markets recover over the next few years, their
money doesn't. They keep withdrawing forty thousand a year from a shrinking pile, and their plan is now at real risk.""",
   "Worried retiree", "RETIREE ONE PANICS")
sc("""The second retiree had a two year cash buffer. They spend from it, trim travel for a year and leave their stocks alone. When
markets recover, their portfolio recovers too. Same crash, very different outcomes, because one had a plan for bad years.""",
   "Calm retiree gardening", "RETIREE TWO HAD A PLAN")
sc("""The four percent rule didn't save the second retiree by itself. What saved them was the system around it. A realistic number, a cash
buffer for bad years, a willingness to adjust spending a little and the discipline to stay invested. The rule tells you where to aim. The
system is what gets you through the storms.""",
   "Lighthouse in storm", "THE SYSTEM MATTERS")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. Is four percent too high now? Some researchers suggest slightly lower starting rates for long retirements or lower
expected returns. Others think four percent remains reasonable. Using three and a half to four percent with flexibility is a common
middle ground.""",
   "Debate illustration", "IS 4% TOO HIGH?")
sc("""Question two. Does the rule work for early retirement? It can be a starting point, but longer retirements usually call for lower
withdrawal rates, often three to three and a half percent, and more flexibility.""",
   "Young retiree", "EARLY RETIREMENT")
sc("""Question three. What if I have a pension? A pension, like Social Security, reduces how much you need from savings. Subtract it
from your spending before multiplying by twenty five.""",
   "Pension statement", "WHAT ABOUT PENSIONS?")
sc("""Question four. Should I include my home's value? Usually not, unless you plan to sell or downsize and use the money for living
expenses. Your home provides shelter, not spending money.""",
   "House", "WHAT ABOUT MY HOME?")

sc("""Question five. What about long term care costs? Long term care can be very expensive, and many retirees will need some help later in
life. Some people plan for it with long term care insurance, others set aside extra savings or plan to use home equity. It's worth
discussing with a planner, because it can be one of the biggest late life expenses.""",
   "Caregiver helping senior", "LONG TERM CARE")
sc("""Question six. Can I retire with less than twenty five times spending? Possibly, with more flexibility. Part time income, delaying Social
Security, a willingness to cut spending in bad years, or moving to a lower cost area can all make a smaller number work. The more flexible
you are, the less you may need.""",
   "Person working part time happily", "LESS THAN 25 TIMES?")

# ---------------- Mistakes ----------------
ch("Four 4% rule mistakes")
sc("""Mistake one. Using income instead of spending. Your freedom number is built from what you spend, not what you earn. Using income can
make your target far too high or, if you spend more than you think, far too low.""",
   "Income versus spending", "MISTAKE 1: INCOME, NOT SPENDING")
sc("""Mistake two. Forgetting health care before Medicare. People who retire before sixty five need health insurance until Medicare starts,
and premiums can be significant. Build that cost into your spending estimate.""",
   "Health insurance bill", "MISTAKE 2: HEALTH CARE GAP")
sc("""Mistake three. Treating four percent as guaranteed. It's a historical rule of thumb. Markets, inflation and your lifespan can differ
from the past. Build in a margin of safety and stay flexible.""",
   "Warning sign", "MISTAKE 3: TREATING IT AS A GUARANTEE")
sc("""Mistake four. Ignoring taxes. Withdrawals from pre tax accounts are usually taxed as income. If you need forty thousand dollars to
spend, you may need to withdraw more. Plan for the tax bill.""",
   "Tax bill", "MISTAKE 4: IGNORING TAXES")

# ---------------- Recap ----------------
ch("Recap")
sc("""Quick recap. Angle one, the numbers. Where the rule came from, the times twenty five rule, sequence risk, no guarantees, time
horizon, investment mix, and inflation and taxes.""",
   "Checklist on clipboard", "THE NUMBERS: 1 TO 7")
sc("""Angle two, the psychology. A number makes it real, fear of spending, lifestyle creep, one more year, freedom without full retirement,
defining enough and flexibility.""",
   "Person thinking", "THE PSYCHOLOGY: 8 TO 14")
sc("""Angle three, the playbook. Track spending, calculate your number, factor in Social Security, close the gap, protect the early years
and review every year.""",
   "Notebook with plan", "THE PLAYBOOK: 15 TO 20")

# ---------------- Close ----------------
ch("What to do next")
pr("""Your freedom number isn't a fantasy. It's your yearly spending times twenty five, adjusted for your life. Once you know it, you can
build a real plan to reach it. If you want my full step by step plan, it's in my playbook, linked in the description. Tell me in the
comments, what's your freedom number? I'm Ryan Rover. See you in the next one.""")

save("video38", "The 4% Rule: How Much You Need to Never Work Again", [
    "William P. Bengen, Determining Withdrawal Rates Using Historical Data (Journal of Financial Planning, 1994)",
    "Cooley, Hubbard and Walz, Retirement Savings: Choosing a Withdrawal Rate That Is Sustainable (AAII Journal, 1998), the Trinity study",
    "Morningstar, The State of Retirement Income (safe withdrawal rate research)",
    "Guyton and Klinger, Decision Rules and Maximum Initial Withdrawal Rates (Journal of Financial Planning, 2006)",
    "Social Security Administration: average retired worker benefit (2025), claiming ages",
    "Employee Benefit Research Institute: retiree spending and asset drawdown research",
    "Locke and Latham, goal-setting theory",
    "Morgan Housel, The Psychology of Money (2020)",
    "Growth and sequence examples: stated average returns, illustrations, not promises",
], "the 4% rule in 20 lessons, from 3 angles: numbers, psychology, playbook")
