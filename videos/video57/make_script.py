import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short


EXTRA = {
1: ("""A tip that helps many people. As you sort, mark each transaction with a simple face: happy if you're glad you spent it, neutral, or
unhappy if you regret it. The unhappy ones are your easiest cuts, because you won't miss them. The happy ones are what your fun money
should protect.""",
  "Smiley faces on receipts", "HAPPY, NEUTRAL, REGRET"),
2: ("""Don't forget costs that come every two, three or five years, like new tires, a laptop, or a major appliance. Divide those by the
number of months until you expect them. A one thousand two hundred dollar laptop every four years is twenty five dollars a month. Small
monthly amounts make big future costs painless.""",
  "Laptop and tires", "MULTI YEAR COSTS TOO"),
3: ("""Whatever framework you choose, write down your three percentages and put them somewhere visible. When a new expense comes up, you can
ask a simple question: which bucket does this come from, and is there room? That question alone prevents many impulse decisions.""",
  "Percentages on sticky note", "WRITE IT DOWN"),
4: ("""Why separate accounts instead of one big account with a spreadsheet? Because separation makes the rules physical. When your bills
money lives in a different account, you can't accidentally spend it on dinner. Your spending balance is the truth, at a glance, with no
math required.""",
  "Separate bank cards", "WHY SEPARATE ACCOUNTS"),
5: ("""Time the transfers for the day after payday, so the money is always there. And if you're paid twice a month, split each transfer in
half. Within a month or two, you'll stop thinking about bills at all, which is exactly the point.""",
  "Calendar payday arrows", "THE DAY AFTER PAYDAY"),
6: ("""Why weekly instead of monthly? Because a month is long, and it's easy to overspend in the first two weeks and struggle in the last
two. A weekly number gives you a fresh start every Monday, and it's small enough that you can feel it.""",
  "Monday fresh start", "WHY WEEKLY WORKS"),
7: ("""Start with your three biggest irregular costs, often car maintenance, holidays and insurance. Add more buckets as you go. Many
people say sinking funds are the single change that made their budget finally work.""",
  "Three buckets filling", "START WITH THREE"),
8: ("""Give the emergency fund some distance. Some people keep it at a separate bank from their everyday accounts, so it's available within
a day or two but not one tap away. That small bit of friction protects it from non emergencies.""",
  "Separate bank building", "A LITTLE DISTANCE"),
9: ("""During the check, also look for anything unusual: a charge you don't recognize, a price increase on a subscription, or a fee. Catching
these early can save money and protect you from fraud.""",
  "Unusual charge highlighted", "SPOT THE UNUSUAL"),
10: ("""Use the meeting to celebrate progress too. A sinking fund that covered a repair, a debt paid off, an emergency fund milestone. Money
conversations don't have to be stressful. They can be the moment you see your plan working.""",
  "Couple celebrating", "CELEBRATE PROGRESS"),
11: ("""If one category goes over every single month, that's not a willpower problem. It's a planning problem. Raise that category and lower
another one. The budget should fit your real life, not an imaginary one.""",
  "Adjusting sliders", "FIX THE PLAN, NOT YOU"),
12: ("""A good time for the reset is early January, or right after your yearly raise. Pick a date, put it on your calendar, and treat it like
an appointment. One afternoon a year can keep the whole system healthy.""",
  "Calendar annual appointment", "PUT IT ON THE CALENDAR"),
}

def step(n, title, sub, card_text, paras):
    ch(f"Step {n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"STEP {n}")
    for t, q, c in paras:
        sc(t, q, c)
    sc(*EXTRA[n])

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Most people have tried to budget at least once. They download an app, make a spreadsheet, set strict
limits, and three weeks later, it's abandoned. If that's you, the problem probably wasn't you. It was the system. Today, I'll show
you a complete budget system built to survive real life, and why it works when others fail.""")
short("Your budget didn't fail because of you. It was the system.")
sc("""Budgets fail for predictable reasons. They're too strict, too complicated, or they depend on willpower every single day. They
ignore irregular bills, so the first car repair blows them up. And they make people feel guilty, which is a terrible long term
motivator.""",
   "Abandoned budget spreadsheet", "WHY BUDGETS FAIL")
sc("""A budget that actually works does the opposite. It's simple. It runs mostly on autopilot. It plans for irregular costs. And it
includes real money for fun, so you don't feel deprived. The goal isn't to track every penny forever. It's to make good money
decisions the default.""",
   "Simple organized desk", "WHAT WORKS INSTEAD")
sc("""We'll look at this from three angles. First, the numbers: where the average household's money actually goes, and how popular
budget rules divide it. Second, the psychology: why our brains fight budgets, and how to work with them instead. And third, the
playbook: a twelve step system you can set up this weekend.""",
   "Three paths map", "THREE ANGLES")
pr("""Stay for the sample budgets near the end. I'll show the system at three different income levels. Let's start with the numbers.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Household spending data comes from the Bureau of Labor Statistics Consumer Expenditure Survey. The fifty thirty twenty rule comes
from the book All Your Worth by Elizabeth Warren and Amelia Warren Tyagi, published in 2005. Subscription spending comes from a 2022
survey by C plus R Research. Behavioral research comes from published studies, which we name as we go. This is education, not
financial advice.""",
   "Bureau of Labor Statistics building", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Where does the money actually go?""")
sc("""According to the BLS Consumer Expenditure Survey, the average American household spent around seventy seven thousand dollars in
2023. Housing was the biggest category by far, around a third of all spending. Transportation came next, around seventeen percent.
Food was around thirteen percent.""",
   "Pie chart household spending", "~$77,000 A YEAR")
sc("""Together, housing, transportation and food make up around six of every ten dollars a typical household spends. Then come
healthcare, personal insurance and pensions, entertainment, and everything else. That's why the biggest budget wins almost always come
from the big three, not from coffee.""",
   "House car groceries", "THE BIG THREE")
card("""Housing, transportation and food make up around six of every ten dollars the average U.S. household spends, according to the BLS
Consumer Expenditure Survey.""",
     {"type": "stat", "label": "share of spending on the big three", "big": "~60%", "sub": "housing, transportation and food (BLS CES)"})
sc("""Now let's look at a popular framework. In their 2005 book All Your Worth, Elizabeth Warren and her daughter Amelia Warren Tyagi
suggested dividing after tax income into three parts. Fifty percent for needs. Thirty percent for wants. And twenty percent for savings
and debt payments. It became known as the fifty thirty twenty rule.""",
   "All Your Worth book", "THE 50/30/20 RULE")
sc("""On a take home pay of five thousand dollars a month, that's twenty five hundred for needs, like housing, utilities, groceries,
insurance and minimum debt payments. Fifteen hundred for wants, like dining out, hobbies and travel. And one thousand for savings,
investing and extra debt payments.""",
   "Three jars money", "$2,500 / $1,500 / $1,000")
card("""The fifty thirty twenty rule on five thousand dollars of monthly take home pay.""",
     {"type": "compare", "left": {"label": "needs (50%)", "big": "$2,500", "sub": "housing, utilities, groceries, insurance"},
      "right": {"label": "savings (20%)", "big": "$1,000", "sub": "investing, emergency fund, extra debt"},
      "note": "Wants get the other 30%: $1,500."})
sc("""It's a useful starting point. But in high cost cities, needs can easily exceed fifty percent. And if you want to retire early or
catch up, twenty percent for savings may not be enough. So think of fifty thirty twenty as a starting map, not a law.""",
   "Map with flexible route", "A MAP, NOT A LAW")
sc("""Now the hidden leaks. In a 2022 survey by C plus R Research, people estimated they spent around eighty six dollars a month on
subscriptions. When they actually added them up, the average was about two hundred nineteen dollars. That's more than two and a half
times what they thought.""",
   "Subscription apps on phone", "$86 GUESSED, $219 ACTUAL")
sc("""Two hundred nineteen dollars a month is over twenty six hundred dollars a year. Invested instead at seven percent for twenty years,
that could grow to over a hundred thousand dollars. Not every subscription is a waste. But the ones you forgot about are pure leakage.""",
   "Money leaking from pipe", "$2,600 A YEAR")
sc("""And then there are irregular expenses: car repairs, holiday gifts, annual insurance premiums, back to school costs, vet bills.
They don't show up every month, so most budgets ignore them. Then they arrive, and the budget breaks. In many households, these
irregular costs can add up to several thousand dollars a year.""",
   "Car repair bill surprised", "THE IRREGULAR EXPENSES")
sc("""Here's what a working budget can be worth. Say the system helps you find three hundred dollars a month: some from subscriptions,
some from food, some from a cheaper insurance policy. Invest that three hundred dollars a month at a seven percent average yearly return
for thirty years, and it could grow to roughly three hundred sixty six thousand dollars.""",
   "Small savings growing into large", "$300 A MONTH = ~$366K")
card("""Three hundred dollars a month found in a budget, invested at seven percent a year for thirty years.""",
     {"type": "growth", "monthly": 300, "rate": 0.07, "years": 30})
sc("""That's the real reason to budget. Not to feel restricted, but to redirect money from things you don't care about to a future you do.
Three hundred dollars a month of forgotten spending, turned into a six figure investment. That's the power of giving every dollar a
job.""",
   "Future home and family", "REDIRECT, DON'T RESTRICT")
sc("""And the benefits aren't only financial. Many people report that having a clear plan reduces money stress and arguments at home.
When you know the bills are covered and the future is funded, everyday spending decisions become much lighter.""",
   "Relaxed family at home", "LESS STRESS")
pr("""So the numbers tell us three things. Focus on the big three. Watch for silent leaks. And plan for irregular costs. Now, why do our
brains make this so hard? Angle two.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
pr("""Angle two. The psychology. Five reasons your brain fights your budget, and how to work with it.""")
short("5 reasons your brain fights your budget")
sc("""Reason one. Restriction backfires. Research on dieting by psychologists Janet Polivy and Peter Herman described what's sometimes
called the what the hell effect. When strict dieters broke their rules, many gave up and ate even more. Budgets work the same way. Go
over once, and it's tempting to abandon the whole thing.""",
   "Broken diet plan donut", "REASON 1: WHAT THE HELL")
sc("""The fix is to build in flexibility. Include a real fun money category. Add a buffer for small surprises. And when you overspend,
adjust next week instead of declaring failure. A budget is a plan, not a test.""",
   "Flexible rubber band", "THE FIX: FLEXIBILITY")
sc("""Reason two. Decision fatigue. Every purchase becomes a small decision when you're trying to budget manually. Is this okay? Can I
afford this? Making dozens of those choices every day is exhausting. Eventually, people stop deciding and just spend.""",
   "Tired person shopping", "REASON 2: DECISION FATIGUE")
sc("""The fix is automation and simple limits. When bills, savings and investing happen automatically on payday, the only decision left
is how to spend a fixed weekly amount. One decision, not a hundred.""",
   "Automatic payments", "THE FIX: AUTOMATE")
sc("""Reason three. Mental accounting. Economist Richard Thaler, who later won a Nobel Prize, showed that people treat money differently
depending on which mental bucket it's in. A tax refund feels like free money. A bonus feels like fun money. But a dollar is a dollar.""",
   "Richard Thaler economics", "REASON 3: MENTAL ACCOUNTING")
sc("""The fix is to use mental accounting on purpose. Create separate accounts for separate jobs: bills, spending, savings, investing.
When the spending account is empty, you're done for the week. The buckets do the work for you.""",
   "Separate labeled jars", "THE FIX: REAL BUCKETS")
sc("""Reason four. Out of sight, out of mind. Card payments and phone wallets make spending almost invisible. Some studies suggest
people may be willing to spend more when paying by card than with cash. When money doesn't feel real, it disappears faster.""",
   "Tap to pay phone", "REASON 4: INVISIBLE MONEY")
sc("""The fix is visibility without obsession. A weekly ten minute check of your spending account is enough. Some people use cash
envelopes for categories they overspend in, like eating out. Seeing the balance shrink makes spending feel real again.""",
   "Cash envelopes", "THE FIX: WEEKLY CHECK")
sc("""And reason five. Shame. Many people avoid looking at their money because it makes them feel bad. But avoidance makes problems
grow. The fix is to treat your budget like data, not a judgment. Numbers are information. They tell you what to adjust next.""",
   "Person hiding from bills", "REASON 5: SHAME")

ch("The mindset that makes budgets stick")
sc("""So what mindset works? Think of your budget as a spending plan that gives every dollar a job, including the job of making you
happy. People who stick with budgets usually describe them as giving freedom, not taking it away. They spend without guilt, because they
know the important things are already covered.""",
   "Happy person spending guilt free", "A PLAN FOR FREEDOM")
sc("""And think in systems, not willpower. A good system makes the right choice the easy choice. Willpower runs out. Systems keep running.""",
   "Gears running smoothly", "SYSTEMS BEAT WILLPOWER")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
pr("""Angle three. The playbook. Twelve steps to build a budget system that actually works. You can set most of this up in one weekend.""")
short("The 12-step budget system that actually works")

step(1, "Track 90 days of spending", "see the truth",
"""Step one. Look back at ninety days of spending.""",
[("""Download three months of bank and credit card statements. Sort every transaction into simple categories: housing, transportation,
food, utilities, insurance, debt, subscriptions, shopping, fun, and other. Don't judge. Just sort.""",
  "Bank statements sorted", "THREE MONTHS OF TRUTH"),
 ("""Ninety days gives you a much more realistic average than one month. Most people find at least one category that's far higher than
they thought. That's your first opportunity.""",
  "Highlighted category", "FIND THE SURPRISE")])

step(2, "Calculate your true monthly costs", "include the irregular",
"""Step two. Calculate your true monthly costs.""",
[("""List every irregular expense you can think of for a full year: car registration, insurance premiums, holidays, birthdays, annual
subscriptions, medical costs, car maintenance, home repairs. Estimate each one, add them up, and divide by twelve.""",
  "Annual expenses list", "LIST THE IRREGULAR"),
 ("""If your irregular costs total thirty six hundred dollars a year, that's three hundred dollars a month. Add that to your regular
monthly bills, and you have your true monthly cost. This one number fixes most broken budgets.""",
  "Calculator divide twelve", "$3,600 ÷ 12 = $300")])

step(3, "Choose your framework", "a starting map",
"""Step three. Choose your framework.""",
[("""Pick a simple starting structure. Fifty thirty twenty is a good default. If you're catching up or paying off debt, try sixty
twenty twenty: sixty for needs, twenty for wants, twenty for savings. Or seventy twenty ten if your housing costs are very high, with a
plan to improve it.""",
  "Framework options chart", "PICK A STARTING MAP"),
 ("""Some people prefer zero based budgeting, where every dollar of income is assigned a job until nothing is left unassigned. It takes
more effort, but it gives you full control. Choose whatever you'll actually stick with.""",
  "Zero based budget sheet", "OR ZERO BASED")])

step(4, "Set up four accounts", "one job each",
"""Step four. Set up four accounts.""",
[("""Here's the core of the system. Account one: Bills, a checking account for fixed expenses like rent, utilities, insurance and loan
payments. Account two: Spending, a separate checking account or card for day to day purchases. Account three: Savings, a high yield
savings account with buckets for your emergency fund and sinking funds. Account four: Investing, your retirement and brokerage
accounts.""",
  "Four accounts diagram", "BILLS, SPENDING, SAVINGS, INVESTING"),
 ("""Many banks and credit unions offer free checking and savings accounts, and many let you create multiple savings buckets inside one
account. Setting this up usually takes an hour or two.""",
  "Opening bank account online", "AN HOUR OR TWO")])

step(5, "Automate the payday flow", "money moves itself",
"""Step five. Automate the payday flow.""",
[("""When your paycheck lands, automatic transfers move money where it belongs. Retirement contributions come out before the paycheck.
Then a set amount goes to Bills, a set amount to Savings, and a set amount to Investing. What's left goes to Spending.""",
  "Money flowing automatically", "THE PAYDAY FLOW"),
 ("""Set all your fixed bills to autopay from the Bills account. Now your bills, savings and investing happen without a single decision.
The only thing you manage is your spending account.""",
  "Autopay settings", "BILLS ON AUTOPAY")])

step(6, "Use a weekly spending number", "one number to watch",
"""Step six. Use a weekly spending number.""",
[("""Take your monthly spending money and divide it into weekly amounts. If you have one thousand dollars a month for groceries, gas, eating
out and fun, that's about two hundred thirty dollars a week. That's your only number to watch.""",
  "Weekly allowance", "ONE WEEKLY NUMBER"),
 ("""Some people transfer the weekly amount every Monday. When it's gone, they wait until next week. It's simple, flexible, and you can
see at a glance whether you're on track.""",
  "Monday transfer calendar", "EVERY MONDAY")])

step(7, "Build sinking funds", "no more surprise bills",
"""Step seven. Build sinking funds.""",
[("""Inside your Savings account, create buckets for each irregular expense: car repairs, holidays, insurance, medical, gifts, travel.
Each month, a fixed amount goes to each one automatically. When the bill comes, the money is already waiting.""",
  "Labeled savings buckets", "A BUCKET FOR EACH"),
 ("""This is the step that turns budget breaking surprises into planned expenses. A seven hundred dollar car repair becomes a withdrawal,
not a crisis.""",
  "Calm person paying car repair", "SURPRISES BECOME PLANS")])

step(8, "Build your emergency fund", "the true unexpected",
"""Step eight. Build your emergency fund.""",
[("""Sinking funds cover expected irregular costs. The emergency fund covers the truly unexpected: a job loss, a medical emergency, a major
repair. Start with one thousand dollars, then build toward three to six months of essential expenses.""",
  "Emergency fund jar", "3 TO 6 MONTHS"),
 ("""Keep it in the Savings account, separate from your sinking funds, and only use it for real emergencies. Then refill it.""",
  "Refill savings", "USE IT, THEN REFILL IT")])

step(9, "Do a ten minute weekly check", "small corrections",
"""Step nine. Do a ten minute weekly check.""",
[("""Once a week, look at your spending account balance and recent transactions. Are you on track? Any surprises? Any subscriptions you
forgot? Ten minutes is enough.""",
  "Phone banking app quick check", "10 MINUTES A WEEK"),
 ("""This small habit catches problems early, when they're easy to fix. Many people pair it with something pleasant, like a Sunday coffee.""",
  "Sunday coffee laptop", "PAIR IT WITH COFFEE")])

step(10, "Hold a monthly money meeting", "big picture",
"""Step ten. Hold a monthly money meeting.""",
[("""Once a month, look at the big picture. Did your automatic transfers run? Are your sinking funds growing? How's your emergency fund?
Is there anything coming next month, like a birthday or a trip?""",
  "Monthly calendar review", "ONCE A MONTH"),
 ("""If you have a partner, do this together. Keep it short, positive and focused on goals, not blame. Many couples end it with something
fun, like ordering their favorite takeout from the fun budget.""",
  "Couple reviewing budget", "TOGETHER, NOT BLAME")])

step(11, "Handle overspending without guilt", "adjust, don't quit",
"""Step eleven. Handle overspending without guilt.""",
[("""You will overspend sometimes. Everyone does. When it happens, move money from another category, reduce next week's spending a bit,
or adjust the category if it was unrealistic.""",
  "Adjusting budget lines", "ADJUST, DON'T QUIT"),
 ("""What you don't do is abandon the system. One bad week doesn't ruin a budget. Quitting does.""",
  "Person continuing path", "ONE BAD WEEK IS FINE")])

step(12, "Do an annual reset", "a fresh start",
"""Step twelve. Do an annual reset.""",
[("""Once a year, review everything. Update your irregular expenses list. Raise your savings and investing transfers, especially after
raises. Cancel subscriptions you don't use. Shop around for insurance, phone and internet.""",
  "New year planning", "ONCE A YEAR"),
 ("""This yearly reset often finds hundreds or even thousands of dollars in savings, and keeps your budget aligned with your life.""",
  "Savings found", "FIND HUNDREDS")])

# ---------------- History ----------------
ch("A short history of budgeting")
sc("""Budgeting isn't new. For generations, many families used the envelope system. On payday, cash went into labeled envelopes: rent,
groceries, coal, clothing. When an envelope was empty, spending in that category stopped. It was simple, visual, and it worked without
any technology.""",
   "Vintage cash envelopes", "THE ENVELOPE SYSTEM")
sc("""In 1970, a manager at Texas Instruments named Peter Pyhrr described zero based budgeting for businesses. Instead of starting from
last year's budget, every expense had to be justified from zero. The idea later spread to personal finance: every dollar gets a job.""",
   "1970s corporate office", "1970: ZERO BASED")
sc("""In 2005, Elizabeth Warren and Amelia Warren Tyagi popularized the fifty thirty twenty rule as a simpler alternative. And in the
2000s and 2010s, budgeting apps began linking bank accounts and categorizing spending automatically.""",
   "Budget app smartphone", "RULES AND APPS")
sc("""The four account system in this video borrows from all of them. The envelope idea of separate buckets. The zero based idea of
giving every dollar a job. The simplicity of fifty thirty twenty. And modern automation, so it runs without daily effort.""",
   "Combining ideas puzzle", "THE BEST OF EACH")

# ---------------- Mid ----------------
ch("A quick favor")
pr("""Quick pause. If this system is helping you, subscribe to the channel. It's free, and it helps me keep making these videos for you.
Now, the sample budgets.""")

# ---------------- Sample budgets ----------------
ch("The system at three incomes")
short("The same budget system at $3,000, $5,000 and $8,000 a month")
sc("""Let's see the system at three income levels. First, three thousand dollars a month of take home pay, a single person. Bills account:
fourteen hundred, including rent with a roommate, utilities, phone, insurance and a small loan payment. Savings: two hundred fifty for
sinking funds and one hundred fifty for the emergency fund.""",
   "Small apartment budget", "$3,000 A MONTH")
sc("""Investing: one hundred fifty to a Roth IRA, plus a workplace match through payroll. Spending: about one thousand fifty, or roughly
two hundred forty a week for groceries, gas, fun and everything else. It's tight, but every dollar has a job, and the future is
funded.""",
   "Weekly spending envelope", "~$240 A WEEK")
sc("""Second, five thousand dollars a month, a couple with no kids. Bills: twenty three hundred, including rent, utilities, insurance and
one car payment. Savings: four hundred for sinking funds and three hundred for the emergency fund. Investing: six hundred in IRAs, plus
retirement plans through payroll.""",
   "Couple apartment budget", "$5,000 A MONTH")
sc("""Spending: about fourteen hundred, around three hundred twenty a week for groceries, gas, dining out and fun. That's about eighteen
percent going to the emergency fund and investing from take home pay alone, plus the payroll contributions.""",
   "Couple shopping groceries", "~$320 A WEEK")
sc("""Third, eight thousand dollars a month, a family of four. Bills: thirty nine hundred, including mortgage, utilities, insurance,
childcare and a car payment. Savings: six hundred for sinking funds and four hundred for the emergency fund. Investing: one thousand,
plus a small 529 contribution and payroll retirement contributions.""",
   "Family home budget", "$8,000 A MONTH")
sc("""Spending: about two thousand, around four hundred sixty a week for groceries, gas, kids' activities and fun. Same four accounts.
Same automatic flow. Same weekly number. The amounts change. The system doesn't.""",
   "Family dinner table", "~$460 A WEEK")
card("""Same four accounts, same payday flow, same weekly spending number, whether you bring home three thousand, five thousand or eight
thousand a month.""",
     {"type": "stat", "label": "the four account system", "big": "SAME SYSTEM", "size": 120, "sub": "bills, spending, savings, investing"})

# ---------------- Stories ----------------
ch("Two budgeters")
short("She tracked every penny. He used one number. Guess who stuck with it.")
sc("""Let's compare two people. Nina downloads a detailed budget app, sets thirty categories, and tracks every coffee. For two weeks, she's
motivated. Then a busy month hits. She stops logging. Her categories fall out of date. By month two, she feels guilty and deletes the
app.""",
   "Woman frustrated with app", "NINA: 30 CATEGORIES")
sc("""Tom sets up four accounts and automates everything. His only rule is a weekly spending number of two hundred eighty dollars. Some
weeks he goes over, so the next week he eats at home more. He spends ten minutes on Sunday checking. A year later, he's still doing it,
his emergency fund is full, and he's investing more than ever.""",
   "Man relaxed checking phone", "TOM: ONE NUMBER")
sc("""Nina didn't fail because she lacked discipline. She chose a system that needed too much of it. When she switches to the four
account approach, she finds it far easier. The best budget isn't the most detailed one. It's the one you'll keep using.""",
   "Woman relieved simple system", "THE BEST BUDGET IS THE ONE YOU KEEP")

sc("""Here's the lesson from Nina and Tom. Detail feels productive, but it often isn't sustainable. If you love tracking, track. If you
don't, let the account structure do the work. Either way, the goal is the same: bills covered, future funded, and spending money you can
enjoy without worry. Choose the version you'll still be using a year from now.""",
   "Two paths same destination", "CHOOSE WHAT YOU'LL KEEP")

# ---------------- Irregular income ----------------
ch("Budgeting with irregular income")
sc("""What if your income changes every month, like freelancers, gig workers, salespeople on commission, or seasonal workers? The system
still works, with one change. Add a fifth account: a holding tank.""",
   "Freelancer laptop", "IRREGULAR INCOME")
sc("""All income goes into the holding tank first. Then, on the same day each month, you pay yourself a fixed salary from it, based on
a conservative estimate of your income. That salary flows into the four accounts as usual. In good months, the tank grows. In slow
months, it keeps your salary steady.""",
   "Water tank reservoir", "PAY YOURSELF A SALARY")
sc("""Aim to build the holding tank to at least one or two months of your salary, on top of your emergency fund. And if you're
self employed, set aside money for taxes in a separate bucket, since you may need to make quarterly estimated payments to the IRS.""",
   "Tax bucket savings", "AND A TAX BUCKET")

# ---------------- Couples ----------------
ch("Budgeting as a couple")
sc("""Couples have extra challenges: different spending styles, different incomes, and sometimes different goals. A common approach is
yours, mine and ours. Shared bills, savings and investing come from a joint system. Each person also gets personal spending money with
no questions asked.""",
   "Couple three accounts", "YOURS, MINE AND OURS")
sc("""How much each person contributes can be equal, or proportional to income. There's no single right answer. What matters is that it
feels fair to both of you. The monthly money meeting keeps everything transparent.""",
   "Scale balance fair", "EQUAL OR PROPORTIONAL")

# ---------------- Tools ----------------
ch("Apps, spreadsheets or envelopes?")
sc("""Which tool should you use? Honestly, any of them can work. Budgeting apps can link your accounts and categorize spending
automatically, though some charge a fee. A simple spreadsheet is free and fully customizable. And cash envelopes work well for people
who overspend with cards.""",
   "App spreadsheet envelopes", "ANY TOOL CAN WORK")
sc("""The four account system works with all of them, because most of the work is done by the account structure and automation, not by
tracking. The tool is just a window. The system is the engine.""",
   "Engine and window", "THE SYSTEM IS THE ENGINE")

# ---------------- Category guide ----------------
ch("Where to find money, category by category")
pr("""Now, if your budget doesn't balance yet, where do you find the money? Here's a quick category by category guide, from biggest to
smallest impact.""")
sc("""Housing. It's usually the biggest lever. Options include a roommate, a cheaper unit at your next lease, negotiating rent, or
refinancing a mortgage if rates and fees make sense. Even a two hundred dollar monthly reduction is twenty four hundred a year.""",
   "Apartment for rent sign", "HOUSING")
sc("""Transportation. Keep cars longer, avoid large payments, compare insurance quotes every year or two, and consider whether a household
really needs two cars. For some people, public transit or biking for some trips can save a surprising amount.""",
   "Car insurance comparison", "TRANSPORTATION")
sc("""Food. Plan meals, cook in batches, shop with a list, and limit delivery apps, whose fees and markups can add up fast. You don't have
to stop eating out. Just decide in advance how much of your weekly number goes to it.""",
   "Meal planning groceries", "FOOD")
sc("""Insurance. Shop your auto and home or renters insurance regularly. Consider higher deductibles if you have a solid emergency fund,
which can lower premiums. And make sure you're not paying for coverage you don't need.""",
   "Insurance quote comparison", "INSURANCE")
sc("""Phone, internet and utilities. Call your providers and ask about cheaper plans or promotions. Many people overpay for phone data or
internet speed they don't use. Prepaid phone plans can cost much less than traditional contracts.""",
   "Phone bill", "PHONE AND INTERNET")
sc("""Subscriptions. List every recurring charge from the last three months. Cancel what you don't use. Rotate streaming services instead
of keeping them all at once. Remember, the average person in that survey underestimated their subscriptions by more than half.""",
   "Canceling subscriptions", "SUBSCRIPTIONS")
sc("""And banking fees. Overdraft fees, monthly maintenance fees and ATM fees are pure waste. Many banks and credit unions offer free
accounts with no minimums. Switching can save hundreds of dollars a year.""",
   "Bank fees statement", "BANK FEES")

ch("Common budgeting mistakes")
sc("""Mistake one: making the budget too tight. A budget with no fun money and no buffer usually collapses within weeks. Plan for a life
you actually want to live.""",
   "Overly tight belt", "MISTAKE 1: TOO TIGHT")
sc("""Mistake two: forgetting irregular expenses. This is the number one reason budgets break. Sinking funds solve it.""",
   "Holiday gifts bill", "MISTAKE 2: IRREGULAR COSTS")
sc("""Mistake three: too many categories. Thirty categories means thirty decisions. Most people do better with a handful of buckets
and one weekly spending number.""",
   "Complicated spreadsheet", "MISTAKE 3: TOO COMPLEX")
sc("""Mistake four: budgeting on gross pay. Your budget should be built on take home pay, after taxes and payroll deductions, because
that's the money that actually reaches your account.""",
   "Gross versus net pay", "MISTAKE 4: GROSS PAY")
sc("""And mistake five: never updating it. Life changes. Raises, moves, kids, new goals. Your budget should change too. The monthly
meeting and the annual reset keep it current.""",
   "Outdated calendar", "MISTAKE 5: NEVER UPDATING")

ch("Tom's first year")
sc("""Let's go back to Tom and see what one year of the system did. In month one, he discovered he was spending about one hundred eighty
dollars a month on subscriptions and food delivery fees he barely noticed. He cut about half of it.""",
   "Man reviewing statements", "MONTH ONE")
sc("""By month three, his sinking funds covered a surprise car repair and a friend's wedding without touching a credit card. By month
six, his emergency fund reached one month of expenses. And by month twelve, he raised his investing transfer by one hundred dollars a
month after a raise.""",
   "Progress chart months", "MONTHS 3 TO 12")
sc("""Nothing dramatic happened. No extreme cuts. No windfall. Just a system that quietly moved money to the right places every payday.
That's what a budget that works looks like.""",
   "Calm steady progress", "NOTHING DRAMATIC")

ch("Already budgeting?")
sc("""If you already have a budget that works, look for three upgrades. Automate anything still manual. Add sinking funds if you don't
have them. And raise your savings and investing transfers by at least one percent of income this year.""",
   "Upgrade arrows", "THREE UPGRADES")
sc("""Then consider simplifying. Many experienced budgeters find that once their habits are solid, they can track less and automate more.
The goal is a system that takes less time every year, not more.""",
   "Simplified desk", "TRACK LESS, AUTOMATE MORE")

ch("Your setup weekend")
sc("""Here's how to set everything up in one weekend. Saturday morning: download ninety days of statements and sort them. Saturday
afternoon: list irregular expenses and calculate your true monthly costs.""",
   "Weekend planning coffee", "SATURDAY")
sc("""Sunday morning: open any accounts you need and create your savings buckets. Sunday afternoon: set up the automatic transfers for
payday and autopay for bills. Then write your weekly spending number on a sticky note. You're done.""",
   "Sticky note weekly number", "SUNDAY")

ch("But Ryan, what about...")
sc("""Objection one. I don't earn enough to budget. Actually, a budget matters most when money is tight, because every dollar counts. Even
if your savings are small at first, the system prevents overdrafts, late fees and surprise debt, which can save hundreds of dollars a
year.""",
   "Small paycheck", "I DON'T EARN ENOUGH")
sc("""Objection two. I earn plenty, I don't need a budget. Many high earners still live paycheck to paycheck, because spending tends to
rise with income. A simple automated system makes sure a high income actually becomes wealth.""",
   "High earner stressed", "I EARN PLENTY")
sc("""And objection three. Budgeting takes too much time. The system in this video takes a weekend to set up, ten minutes a week, about
thirty minutes a month, and one afternoon a year. That's less time than most people spend scrolling on a single day.""",
   "Clock small time", "IT TAKES TOO LONG")

# ---------------- FAQ ----------------
ch("Questions people ask")
pr("""Let me answer the questions people ask me most about budgeting.""")
sc("""Question one. What if my needs are more than fifty percent? That's common, especially in expensive cities. Start where you are, and
look for one big change over time, like a roommate, a cheaper apartment at your next lease, or a lower cost car. Meanwhile, keep
savings going, even if it's ten percent instead of twenty.""",
   "Expensive city rent", "NEEDS OVER 50%?")
sc("""Question two. Should I budget with credit cards? If you pay the full balance every month, cards can work fine and may earn rewards.
But if you've ever carried a balance or overspent with them, using a debit card for your spending account can make the system much
safer.""",
   "Credit card versus debit card", "CREDIT CARDS?")
sc("""Question three. How do I budget for fun without guilt? Make fun a real line in your budget. When the money is planned, spending it
is part of the plan, not a failure. Many people find they enjoy fun money more when it's guilt free.""",
   "Friends at concert", "FUN WITHOUT GUILT")
sc("""Question four. What if I'm paying off debt? Put minimum payments in the Bills account, and send extra payments from Savings or
directly from your paycheck. Keep a small emergency fund while you pay down debt, so surprises don't create new debt.""",
   "Debt payoff tracker", "PAYING OFF DEBT?")
sc("""And question five. How long until it feels easy? For many people, about three months. The first month is setup and surprises. The
second month you adjust. By the third month, the system often runs quietly in the background.""",
   "Calendar three months", "ABOUT 3 MONTHS")

sc("""Question six. Should I use the fifty thirty twenty rule exactly? Use it as a starting point. If you have high interest debt or want
to retire early, you may want more than twenty percent going to savings and debt. If you live in an expensive city, needs may be higher
for a while. Adjust it to your goals.""",
   "Adjusting pie chart", "50/30/20 EXACTLY?")
sc("""Question seven. What about kids' expenses? Give them their own sinking funds: school supplies, activities, birthdays, clothing.
Kids' costs are often irregular, so sinking funds make them much easier to handle.""",
   "Kids school supplies", "KIDS' EXPENSES")
sc("""And question eight. Is it ever okay to stop budgeting? Some people with strong habits and plenty of margin move to a simpler
approach: automate savings and investing first, pay bills automatically, and spend the rest freely. That's still a budget. It's just
one that runs itself.""",
   "Relaxed person automatic", "STOP BUDGETING?")

# ---------------- Recap ----------------
ch("Recap: the 12 steps")
short("The budget system that actually works, in 60 seconds")
sc("""Quick recap. The big three, housing, transportation and food, are around six of every ten dollars. Subscriptions and irregular
costs are silent budget breakers. And our brains fight strict budgets, so build in flexibility, automation and real buckets.""",
   "Checklist clipboard", "THE NUMBERS AND PSYCHOLOGY")
sc("""The twelve steps. Track ninety days. Calculate your true monthly costs. Choose a framework. Set up four accounts. Automate the
payday flow. Use a weekly spending number. Build sinking funds. Build your emergency fund. Do a ten minute weekly check. Hold a monthly
money meeting. Handle overspending without guilt. And do an annual reset.""",
   "Staircase twelve steps", "THE 12 STEPS")

sc("""One last thought. The perfect budget doesn't exist. The one that works is the one that fits your life, runs mostly on its own, and
gets a little better every year. Start simple, automate what you can, and give yourself permission to adjust. That's how a budget turns
into a habit, and a habit turns into wealth.""",
   "Sunrise new start", "START SIMPLE")
sc("""And remember why you're doing this. Not for the spreadsheet. For the emergency that doesn't become a crisis. For the trip you
can pay for in cash. For the retirement that arrives on your terms. Every dollar with a job is a step toward that life.""",
   "Family enjoying trip", "REMEMBER WHY")

# ---------------- Close ----------------
ch("What to do next")
pr("""This weekend, do steps one and two. Download ninety days of statements, and calculate your true monthly costs. Then set up the four
accounts. And watch my video on building an emergency fund from zero. It's the first bucket this system fills. I'm Ryan Rover. See you
in the next one.""")

save("video57", "The Complete Budget System That Actually Works", [
    "U.S. Bureau of Labor Statistics, Consumer Expenditure Survey 2023 (average household spending and shares)",
    "Elizabeth Warren and Amelia Warren Tyagi, All Your Worth (2005), the 50/30/20 rule",
    "C+R Research, subscription spending survey (2022)",
    "Janet Polivy and C. Peter Herman, research on dieting and disinhibition (the what-the-hell effect)",
    "Richard H. Thaler, Mental Accounting Matters, Journal of Behavioral Decision Making (1999)",
    "IRS, estimated taxes for self-employed workers",
], "the complete budget system: numbers, psychology, playbook")
