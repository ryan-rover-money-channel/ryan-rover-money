import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save

def item(n, title, sub, card_text, body, example, fix, q1, c1, q2, c2, q3, c3):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"SIGN {n}")
    sc(body, q1, c1)
    sc(example, q2, c2)
    sc(fix, q3, c3)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Here's an uncomfortable idea. A lot of people who feel comfortable with money are
actually much closer to trouble than they realize. They have a nice car, a decent salary, a phone that
costs more than their first car. And underneath, there's almost nothing holding it all up. Today, twenty one
signs you might be poorer than you think. And don't worry. Every sign comes with a fix.""")
card("""Here's a number that surprises people. According to the Bureau of Economic Analysis, the personal
saving rate in the United States has been running at only around four to five percent of disposable income
in recent years.""",
     {"type": "stat", "label": "US personal saving rate", "big": "~4-5%", "sub": "Bureau of Economic Analysis, recent years"})
sc("""That means the typical American household spends roughly ninety five cents of every dollar it takes
home. With that little margin, a single job loss, illness or big repair can knock a family off balance. And
because so many people live this way, it feels normal. When everybody around you is stretched, being
stretched doesn't feel like a warning sign. That's exactly why these signs are so easy to miss.""",
   "Busy city street people walking", "95 CENTS OF EVERY DOLLAR")
sc("""We'll go through these signs from three angles. First, the numbers. Hard measurements you can check
in ten minutes. Second, the psychology. The feelings and beliefs that hide the problem. And third, the
playbook. The weak spots in your safety net, and how to fix each one. If you recognize yourself in a few of
these, that's not bad news. It's information. And information is where every turnaround starts.""",
   "Magnifying glass on documents", "THREE ANGLES")
pr("""Let's start with the numbers. Grab a pen, because you'll want to check a few of these as we go.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our numbers come from named sources. Saving data comes from the Bureau of Economic Analysis. Household
wealth comes from the Federal Reserve's Survey of Consumer Finances, and emergency savings from the Federal
Reserve's Survey of Household Economics and Decisionmaking. Housing cost burden comes from the Department
of Housing and Urban Development and Harvard's Joint Center for Housing Studies. Retirement guidelines come
from Fidelity. This is education, not financial advice.""",
   "Government building columns", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Seven measurements that tell the truth, no matter how things look from the
outside.""")

item(1, "You don't know your net worth", "the one number that matters",
"""Sign number one. You don't know your net worth, or it's lower than you'd guess.""",
"""Net worth is simple. Everything you own, minus everything you owe. Savings, investments, retirement
accounts, the value of your home and car, minus your mortgage, car loans, student loans and credit cards.
Many people have never done this calculation. And many who do are shocked, because the car they think of as
an asset is worth less than the loan on it.""",
"""The Federal Reserve's Survey of Consumer Finances found that the median net worth for families headed by
someone under thirty five was about thirty nine thousand dollars in twenty twenty two. Lots of young adults
are below zero because of student loans, and that's not a disaster on its own. The danger is not knowing
the number, because you can't tell whether you're moving forward or sliding back.""",
"""The fix. Tonight, make a simple list with two columns. What you own, and what you owe. Use realistic
values, like what your car would actually sell for today. Subtract. Write the date next to the answer. Do it
again in three months. The direction of that number matters much more than where it starts.""",
"Balance scale concept", "OWN MINUS OWE",
"Young adults with student loans", "UNDER 35: ABOUT $39,000",
"Notebook with two columns", "CHECK IT EVERY 3 MONTHS")

item(2, "You couldn't cover $400 in cash", "the emergency test",
"""Sign number two. A four hundred dollar surprise would mean borrowing.""",
"""The Federal Reserve asks Americans every year how they would pay for an unexpected four hundred dollar
expense. In its report for twenty twenty four, about sixty three percent said they would cover it with cash
or its equivalent. The rest would need to use a credit card they couldn't pay off right away, borrow from
someone, sell something, or simply couldn't pay.""",
"""Four hundred dollars is a dentist visit, a car repair, a vet bill or a broken phone. These things are not
rare. They're guaranteed to happen eventually, we just don't know when. If one of them sends you into debt,
your budget has no room for normal life. And the interest on that debt makes the next surprise even
harder.""",
"""The fix. Build a starter emergency fund of one thousand dollars in a separate savings account. Set an
automatic transfer, even twenty dollars a week. Sell one thing you don't use. Put any refund or bonus there
first. Once you reach one thousand dollars, aim for one month of expenses, then three.""",
"Car repair mechanic garage", "THE $400 TEST",
"Dentist office chair", "SURPRISES ARE GUARANTEED",
"Savings jar labeled emergency", "START WITH $1,000")

item(3, "You save less than 5%", "below the national average",
"""Sign number three. You save less than five percent of what you earn.""",
"""Remember, the national personal saving rate has been around four to five percent in recent years. Many
financial planners suggest aiming for fifteen percent or more toward retirement alone, including any
employer match. If you're saving less than five percent in total, you may be falling behind without
feeling it.""",
"""Here's why this matters so much. Your savings rate decides how fast you build a cushion and how much
freedom you'll eventually have. Someone saving twenty percent of their pay builds options far faster than
someone saving two percent, even if they earn the same salary. The savings rate is the engine. Income is
just the fuel.""",
"""The fix. Calculate your savings rate. Add up everything you saved and invested last month, including
retirement contributions, and divide by your take home pay. Then raise it by one percentage point. Next
month, another point. Small increases are much easier to stick to than one big jump.""",
"Calculator and savings book", "LESS THAN 5%",
"Car engine close up", "THE SAVINGS RATE IS THE ENGINE",
"Graph going up steps", "ONE POINT AT A TIME")

item(4, "Housing eats more than 30%", "house poor",
"""Sign number four. Your housing costs more than thirty percent of your income.""",
"""The Department of Housing and Urban Development considers households that spend more than thirty
percent of their income on housing to be cost burdened. Harvard's Joint Center for Housing Studies has
reported that about half of American renter households were cost burdened in recent years, a record high.
Homeowners can be stretched too, especially with rising insurance and property taxes.""",
"""When housing takes too much, everything else gets squeezed. Saving becomes impossible, small surprises
become crises, and people start using credit cards to cover groceries. The term house poor describes people
who own a beautiful home but can't afford to do anything else.""",
"""The fix. Add up your full housing cost, including rent or mortgage, insurance, property taxes, HOA fees
and utilities. Divide by your gross monthly income. If it's well above thirty percent, look at options over
the next year. A roommate, a cheaper place when the lease ends, refinancing if rates allow, or appealing a
property tax assessment.""",
"Apartment building exterior", "MORE THAN 30%",
"Beautiful house empty rooms", "HOUSE POOR",
"Rent and bills paperwork", "ADD IT ALL UP")

item(5, "Your car loan is six years or longer", "the stretched payment",
"""Sign number five. Your car loan stretches six years or more.""",
"""Car prices have climbed, and to keep monthly payments manageable, lenders have stretched loans longer
and longer. Edmunds has reported that a large share of new car loans now run seventy two months or more,
and some run eighty four months. That's seven years of payments on something that loses value every
year.""",
"""The longer the loan, the more interest you pay, and the more likely you'll owe more than the car is
worth for years. That's called being underwater, or upside down. If you need to sell or trade the car, the
negative equity can get rolled into the next loan, and the hole gets deeper.""",
"""The fix. Look up what your car would sell for today and compare it with your loan balance. If you're
underwater, the best move is usually to keep the car, pay a little extra each month, and drive it for years
after it's paid off. Next time, aim for a loan of four years or less, or buy a cheaper car with cash.""",
"New cars on dealership lot", "72 TO 84 MONTHS",
"Car sinking in water concept", "UNDERWATER",
"Car keys and paid stamp", "DRIVE IT AFTER IT'S PAID")

item(6, "You pay only the minimum", "the slow trap",
"""Sign number six. You pay only the minimum on your credit cards.""",
"""Credit card statements are required to show how long it would take to pay off your balance if you only
make minimum payments. For many balances, the answer is many years, and the total interest can be a big
share of what you originally spent. With average card rates above twenty percent, according to the Federal
Reserve, the minimum payment keeps you paying for a long time.""",
"""Paying the minimum feels responsible, because you're never late. But it's often a sign that the card is
quietly funding your lifestyle. If your balance stays the same or keeps rising month after month, your
spending is larger than your income, and the card is covering the gap.""",
"""The fix. Stop adding new charges to cards with a balance. Then list them by interest rate and attack the
highest one with every extra dollar while paying the minimum on the rest. If your rate is very high, ask the
issuer for a lower rate, or look into a nonprofit credit counseling agency.""",
"Credit card statement minimum payment", "MINIMUM PAYMENT WARNING",
"Credit cards cut with scissors", "STOP ADDING",
"Person on phone with bank", "ASK FOR A LOWER RATE")

item(7, "Retirement savings are behind", "the milestones",
"""Sign number seven. Your retirement savings are far behind common milestones.""",
"""Fidelity offers a widely quoted guideline. Aim to have about one times your salary saved for retirement
by thirty, three times by forty, six times by fifty, eight times by sixty, and ten times by sixty seven.
These are rough targets, not rules, and they assume you start saving in your twenties. But they're a useful
reality check.""",
"""Social Security was designed to replace only part of your pre retirement income, and the Social Security
Administration says that for the average worker it replaces roughly forty percent. If you're counting on it
to cover everything, the gap can be painful. Being behind isn't a crisis at thirty five. Being behind and not
knowing it can become one at sixty.""",
"""The fix. Find your total retirement savings and divide by your salary. Compare it with the milestone for
your age. If you're behind, make sure you get the full employer match first, then raise your contribution
by one percent a year. After fifty, catch up contributions can help, so check the current IRS limits.""",
"Retired couple walking", "1X BY 30, 3X BY 40",
"Social Security card", "ABOUT 40% REPLACED",
"Retirement account online", "RAISE IT 1% A YEAR")

ch("The ten minute money checkup")
sc("""Let's turn those seven numbers into a quick checkup you can do tonight. Grab your phone and a piece of
paper. First, write your net worth, even a rough one. Second, write how much cash you could reach today
without borrowing. Third, write what percentage of last month's take home pay you saved or invested. That's
three numbers in about five minutes.""",
   "Phone and notepad on table", "THE CHECKUP: 1 TO 3")
sc("""Fourth, divide your total housing cost by your gross monthly income. Fifth, write the number of months
left on your car loan. Sixth, write whether you paid your credit cards in full last month, yes or no. And
seventh, divide your retirement savings by your yearly salary. Seven numbers, ten minutes, and you'll know
more about your real financial health than most people ever do.""",
   "Calculator and pen close up", "THE CHECKUP: 4 TO 7")
sc("""Keep that piece of paper. Put a date on it. In six months, do the checkup again. You're not looking for
perfection. You're looking for direction. If four of those seven numbers moved the right way, you're winning,
no matter where you started. And that sense of progress is one of the best motivators there is.""",
   "Calendar six months ahead", "CHECK THE DIRECTION")

card("""Here's why the earlier you fix these numbers the better. Two hundred fifty dollars a month, invested
for thirty years at a seven percent average yearly return, grows to roughly three hundred five thousand
dollars. You'd put in ninety thousand.""",
     {"type": "growth", "monthly": 250, "rate": 0.07, "years": 30})

pr("""That's angle one. Seven numbers. If several of them made you uncomfortable, good. That discomfort is
useful. Now angle two, the psychology. Because the numbers are often hidden behind feelings that tell us
everything's fine.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
sc("""Here's the strange thing about being poorer than you think. It often doesn't feel like being poor.
Your card still works. Your paycheck still arrives. You can still go out to dinner. The feeling of being
okay comes from cash flow, not from wealth. And cash flow can disappear in a single phone call from your
boss.""",
   "Person relaxed on couch with phone", "FEELING OKAY")

item(8, "You feel rich on payday", "the payday high",
"""Sign number eight. You feel rich for a few days after payday, and broke the week before.""",
"""This boom and bust cycle is one of the clearest signs of living paycheck to paycheck. Right after payday
the account looks full, and spending feels easy. By the end of the month, you're checking your balance
before buying groceries.""",
"""The problem isn't how much you earn. It's that your spending follows your balance instead of a plan.
When money is there, it gets spent. People on very different incomes report this same feeling, which shows
that it's a pattern, not a salary level.""",
"""The fix. Make your account look emptier on payday. Move savings out first, automatically. Put money for
fixed bills into a separate bills account. What's left in your checking account is what you can actually
spend, and it can last the whole month.""",
"Person celebrating with money", "THE PAYDAY HIGH",
"Empty wallet end of month", "THE BROKE WEEK",
"Two bank accounts on screen", "MOVE IT OUT FIRST")

item(9, "You measure wealth by stuff", "things are not wealth",
"""Sign number nine. You measure how you're doing by what you own.""",
"""A big TV, a new SUV, nice clothes, the latest phone. These things can make you feel successful. But most
of them lose value fast, and many were bought with credit. Thomas Stanley's research on millionaires found
that many people who look rich have very little real wealth, while many quiet millionaires look completely
ordinary.""",
"""Stanley called the first group income statement affluent. They earn and spend a lot. He called the
second group balance sheet affluent. They own assets that grow. If your sense of success comes from what
other people can see, you might be building the wrong kind of wealth.""",
"""The fix. Change your scoreboard. Instead of counting things, track three numbers every month. Net worth,
savings rate, and months of expenses you could cover. Celebrate when those go up, not when you buy something
new.""",
"Luxury SUV in driveway", "LOOKING SUCCESSFUL",
"Modest house with garden", "THE QUIET MILLIONAIRE",
"Scoreboard numbers", "CHANGE YOUR SCOREBOARD")

item(10, "You count on future money", "spending raises you don't have yet",
"""Sign number ten. You're spending money you expect to earn later.""",
"""A raise you're hoping for, a bonus that isn't guaranteed, a tax refund, a promotion next year. Many
people make today's purchases based on tomorrow's income. When that money arrives, it's already spent. And
if it doesn't arrive, the debt stays.""",
"""This is how buy now pay later and credit cards hook people. They let you live in the future, today. The
trouble is, the future has its own expenses. Jobs change, companies cut bonuses, and life throws surprises.
Spending money you don't have yet turns optimism into risk.""",
"""The fix. Only spend money that has already arrived. Treat any raise, bonus or refund as zero until it's
actually in your account. And when it does arrive, decide its job before spending any of it.""",
"Person dreaming of future", "SPENDING TOMORROW'S MONEY",
"Buy now pay later on phone", "LIVING IN THE FUTURE",
"Paycheck deposit notification", "ONLY SPEND WHAT ARRIVED")

item(11, "You think everyone lives this way", "normal isn't safe",
"""Sign number eleven. You tell yourself everyone lives like this.""",
"""It's true that many Americans are stretched. But normal isn't the same as safe. If most of your friends
have car payments, credit card balances and no savings, that becomes your baseline. You compare yourself
with them and feel fine.""",
"""Researchers who study social comparison have found that people judge their situation largely by the
people around them. That's useful when the people around you are doing well. It's dangerous when they're
all quietly struggling. The comfort of being average can keep you from noticing real risk.""",
"""The fix. Compare yourself with a standard, not a crowd. Can you cover three months of expenses? Are you
saving at least ten to fifteen percent? Do you have a plan for retirement? Those questions don't care what
your neighbors are doing.""",
"Group of friends at restaurant", "EVERYONE DOES IT",
"Crowd of people walking", "NORMAL ISN'T SAFE",
"Checklist standard measurements", "USE A STANDARD")

pr("""Quick pause. If any of these signs hit close to home, I want you to know there's no judgment here. I
make these videos so people can see the problem early. If that's useful to you, subscribe to Ryan Rover
Money. It's free and it helps the channel more than you'd think. Now, sign twelve.""")

item(12, "You avoid checking your balance", "money anxiety",
"""Sign number twelve. You feel anxious checking your bank balance, so you don't.""",
"""Money anxiety is very common. Surveys from organizations like the American Psychological Association
have consistently found money to be one of the top sources of stress for Americans. When checking your
account brings dread, it's natural to avoid it.""",
"""But avoidance makes things worse. Unchecked accounts lead to overdrafts, missed fraud, and spending that
quietly runs ahead of your income. The anxiety is often a signal that, deep down, you already know
something isn't right.""",
"""The fix. Make checking small and routine. Five minutes, the same time each week. Look at the balance,
scan for anything strange, and close it. Over time, familiarity replaces fear. And as your cushion grows,
the anxiety usually shrinks with it.""",
"Person stressed looking at phone", "MONEY ANXIETY",
"Overdraft notice letter", "AVOIDANCE MAKES IT WORSE",
"Weekly calendar reminder", "5 MINUTES A WEEK")

item(13, "You use credit to feel normal", "keeping up",
"""Sign number thirteen. You use credit cards to keep up a normal life.""",
"""Groceries on the card. Gas on the card. A friend's wedding on the card. When credit pays for everyday
life, not just emergencies, it means your income isn't covering your lifestyle. The card is filling the
gap, and charging you over twenty percent for it.""",
"""This sign is especially hard to see because nothing feels extravagant. You're not buying yachts. You're
buying normal things. But normal things paid with expensive debt slowly turn into a heavy monthly payment
that takes away even more of your income.""",
"""The fix. For one month, use only debit or cash for everyday spending. It will feel tight, and that's the
point. The tightness shows you the real size of the gap. Then close the gap from both sides, cutting where
you can and looking for ways to earn more.""",
"Grocery checkout paying with card", "GROCERIES ON CREDIT",
"Wedding celebration", "NORMAL THINGS, EXPENSIVE DEBT",
"Cash and debit card", "ONE MONTH ON DEBIT")

item(14, "You think about money constantly", "scarcity mindset",
"""Sign number fourteen. Money is always on your mind.""",
"""Researchers Sendhil Mullainathan and Eldar Shafir wrote a book called Scarcity. They found that when
people are short on money, the worry takes up mental bandwidth. It's harder to focus, harder to plan, and
easier to make short term decisions that cost more later.""",
"""That means being financially stretched doesn't just cost money. It costs attention. People who are
always worried about the next bill have less energy for the long term moves, like learning a new skill or
negotiating a raise, that could actually change their situation.""",
"""The fix. Create a small buffer, even a few hundred dollars, and protect it. Many people find that even a
small cushion reduces the constant worry and frees up mental space. Then use that space to make one long
term move at a time.""",
"Person thinking hard at desk", "SCARCITY",
"Book on desk with glasses", "MENTAL BANDWIDTH",
"Small savings jar with coins", "A SMALL BUFFER HELPS")

ch("Why the brain hides the problem")
sc("""Why are these psychological signs so hard to see in ourselves? Part of it is optimism bias. Research
shows that most people tend to believe bad things are more likely to happen to others than to themselves.
Job losses, illnesses, accidents. We know they happen. We just don't expect them to happen to us. That's why
emergency funds feel optional until the day they're not.""",
   "Sunny day optimistic person", "OPTIMISM BIAS")
sc("""Another part is that wealth is invisible and spending is visible. You can see a new car in the
driveway. You can't see an emergency fund or a retirement account. So the signals around us constantly
reward spending and almost never reward saving. Nobody compliments your index fund at a dinner party.""",
   "Shiny new car in driveway", "SPENDING IS VISIBLE")
sc("""The answer is to make your progress visible, at least to yourself. Some people use a chart on the
fridge. Some rename savings accounts after their goals, like freedom fund or new roof. Some celebrate every
thousand dollars saved. When progress is visible, saving starts to feel as rewarding as spending once did.""",
   "Progress chart on fridge", "MAKE PROGRESS VISIBLE")

pr("""That's angle two. Payday highs, stuff as a scoreboard, spending future money, comparing with the crowd,
avoidance, credit for normal life and constant worry. Now angle three, the playbook. These are the weak spots
in your safety net. And this is where we fix things.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
sc("""Think of your finances like a house. Income is the roof. Savings are the walls. Insurance is the
foundation. Most people focus on the roof and forget the rest. These last seven signs are cracks in the
foundation, and each one has a straightforward repair.""",
   "House construction frame", "FIX THE FOUNDATION")

item(15, "One job loss from crisis", "how long could you last?",
"""Sign number fifteen. Losing your job would be a crisis within weeks.""",
"""Ask yourself a simple question. If your income stopped tomorrow, how many months could you cover your
essential expenses? Rent, food, utilities, insurance, minimum payments. For many households, the honest
answer is less than one month.""",
"""Job losses happen even to good workers. Companies restructure, industries change, and recessions come.
The Bureau of Labor Statistics reports millions of layoffs and discharges every year, even in good economies.
Your job security depends partly on things you can't control. Your cushion depends on you.""",
"""The fix. Calculate your essential monthly expenses. Multiply by three. That's your medium term goal.
Six months is even better if your income is irregular or you're the only earner. Build it step by step, and
keep it in an FDIC insured high yield savings account.""",
"Office worker carrying box", "IF YOUR INCOME STOPPED",
"Layoff news headline", "LAYOFFS HAPPEN",
"High yield savings on phone", "3 TO 6 MONTHS")

item(16, "One income source", "all eggs in one basket",
"""Sign number sixteen. All your income comes from one place.""",
"""Most people depend on a single paycheck. That's normal, and it's not wrong. But it means one decision by
one employer can change your whole life. People who build wealth often add a second stream over time, like
a side business, freelance work, rental income or investment income.""",
"""A second income stream doesn't have to be big. Even a few hundred dollars a month adds resilience, and
if you invest it, it grows. It also builds skills and contacts that make you more valuable in your main
job.""",
"""The fix. List three skills people might pay you for. Pick one and test it with a single small project
this month. Keep your expectations modest and your costs low. If it works, put most of what you earn into
savings or investments, not into a bigger lifestyle.""",
"Basket of eggs", "ONE BASKET",
"Freelancer working on laptop", "A SECOND STREAM",
"Notebook brainstorming list", "TEST ONE SKILL")

item(17, "No insurance safety net", "one accident away",
"""Sign number seventeen. You're missing basic insurance.""",
"""No health insurance, no renters insurance, the minimum car insurance, no disability coverage, and no
life insurance even though people depend on you. Insurance feels like money thrown away until something goes
wrong. Medical bills are one of the most common reasons Americans fall into debt.""",
"""Disability insurance is the one people forget most. Your ability to earn an income over your career is
probably your biggest financial asset, and an illness or injury can stop it. Many employers offer disability
coverage, sometimes very cheaply.""",
"""The fix. List every type of insurance you have and what it covers. Check for the big gaps first. Health,
disability if you work, life if anyone depends on your income, and liability. Renters insurance is often
quite inexpensive and covers more than people expect.""",
"Hospital hallway", "ONE ACCIDENT AWAY",
"Person with cast on arm", "PROTECT YOUR INCOME",
"Insurance documents checklist", "FIND THE GAPS")

item(18, "No investments outside your home", "house rich, cash poor",
"""Sign number eighteen. Almost all your wealth is in your home.""",
"""Home equity counts toward net worth. But it's hard to use. You can't spend a bedroom at the grocery
store. To turn home equity into cash, you usually need to sell or borrow against it. Many people reach their
fifties or sixties with a valuable house and very little else.""",
"""A home is a place to live first. It's also concentrated in one property, one neighborhood and one local
market. Investments like broad index funds spread risk across thousands of companies, and they can provide
income in retirement without needing to sell your home.""",
"""The fix. Make sure you're investing outside your home, ideally through tax advantaged retirement
accounts. Even if your house is your biggest asset, aim to build a second pile of wealth that you can
actually access.""",
"House with for sale sign", "YOU CAN'T SPEND A BEDROOM",
"Diverse investment portfolio chart", "SPREAD THE RISK",
"Retirement account dashboard", "BUILD A SECOND PILE")

item(19, "Paying for convenience you can't afford", "the premium lifestyle",
"""Sign number nineteen. You pay for convenience you can't really afford.""",
"""Delivery fees, ride shares, premium subscriptions, pre cut vegetables, expensive coffees. Convenience is
wonderful when you have room in your budget. When you don't, it becomes a quiet premium on almost
everything you buy.""",
"""The tricky part is that convenience often feels like a necessity when you're busy and tired. And many
people who are stretched financially are also stretched for time. That makes convenience spending one of the
hardest habits to change, and one of the most expensive.""",
"""The fix. Pick the single most expensive convenience in your budget and cut it in half for one month. For
example, delivery twice a week instead of four times. Put the difference into savings automatically, so you
can see what the change is worth.""",
"Delivery driver with bag", "THE CONVENIENCE PREMIUM",
"Tired person after work", "BUSY AND TIRED",
"Cooking simple meal at home", "CUT IT IN HALF")

item(20, "Your debt keeps growing", "the direction matters",
"""Sign number twenty. Your total debt is higher than it was a year ago.""",
"""Debt isn't automatically bad. A reasonable mortgage or student loan can make sense. But if your total
debt, not counting a new mortgage, keeps rising year after year, it usually means spending is outrunning
income. And rising debt means rising interest payments, which take even more income next year.""",
"""The New York Fed's household debt reports show total American household debt at record levels in recent
years, including credit cards and auto loans. That doesn't mean your debt has to follow the national trend.
The direction of your own debt is one of the clearest signals of where you're headed.""",
"""The fix. Write down every debt, its balance and its rate. Next year, you want that total to be smaller.
Choose a payoff method, like paying the highest rate first, and automate an extra payment, however small.""",
"Stack of bills and calculator", "DEBT GOING UP",
"Federal Reserve Bank of New York building", "RECORD HOUSEHOLD DEBT",
"Debt payoff chart going down", "MAKE IT SMALLER")

item(21, "You have no plan", "hoping isn't a strategy",
"""And sign number twenty one. You don't have a written money plan.""",
"""No budget, no goals, no idea when you could retire. Just hoping things work out. Hope is wonderful for
motivation, but it's a terrible financial strategy. Without a plan, every decision happens in the moment,
and the moment usually wants to spend.""",
"""A plan doesn't have to be complex. It can fit on one page. What comes in, what goes out, what you save,
what you're paying off, and what you're working toward. People who write down their goals tend to take them
more seriously, because a written goal is a promise to yourself.""",
"""The fix. Write a one page plan this week. Income, fixed costs, savings, debts and three goals with
numbers and dates. Review it once a month. Update it once a year. That one page can change the direction of
your whole financial life.""",
"Person looking at map lost", "HOPING ISN'T A PLAN",
"One page plan on desk", "IT FITS ON ONE PAGE",
"Calendar with monthly review", "REVIEW MONTHLY")

# ---------------- Story ----------------
ch("The couple who looked fine")
pr("""Let me tell you a story that shows how these signs hide in plain sight.""")
sc("""Imagine a couple in their late thirties. Let's call them Chris and Dana. Two good jobs, combined income
of about one hundred forty thousand dollars. A nice home in the suburbs, two newer cars, a family vacation
every summer. Their friends think they're doing great. Honestly, so do they.""",
   "Suburban family home", "CHRIS AND DANA")
sc("""Then Chris's company announces layoffs. Suddenly, they run the numbers for the first time. Their housing
takes almost forty percent of their income. Both car loans run seventy two months. They carry eight thousand
dollars on credit cards. They have about two thousand dollars in savings, and their retirement accounts are
far behind the milestones for their age.""",
   "Couple at table with bills worried", "THE NUMBERS FOR THE FIRST TIME")
sc("""Chris keeps the job, this time. But the scare changes everything. They build a one page plan. They stop
adding to the cards and pay them off in about a year. They raise retirement contributions one percent at a
time. When the lease on one car ends, they replace it with an older, paid off model. Within three years,
they have six months of expenses saved.""",
   "Couple high five at home", "THE TURNAROUND")
sc("""Here's the lesson. Nothing about their income changed. Their friends probably didn't notice any
difference. What changed was that they finally looked at the signs. They were poorer than they thought.
Once they knew it, they could fix it. That's exactly what this video is meant to do for you.""",
   "Couple walking in park smiling", "LOOKING IS THE FIRST STEP")

# ---------------- Score ----------------
ch("Score yourself")
pr("""Okay. Let's turn this into a simple score.""")
sc("""Count how many of the twenty one signs applied to you. Zero to three. You're in good shape. Keep
building and check again next year. Four to eight. You're like a lot of people, comfortable on the surface
with a few weak spots. Pick the two most dangerous ones and fix them in the next three months.""",
   "Scorecard with pen", "SCORE YOURSELF")
sc("""Nine to fourteen. You're more exposed than you probably feel. Focus first on the emergency fund and
high interest debt, because those protect you from the next surprise. Fifteen or more. Don't panic. You've
just discovered the truth, and that's the hardest step. Start with one sign from each angle this month.""",
   "Person climbing mountain", "WHERE TO START")
sc("""Whatever your score, remember that these signs aren't a judgment of who you are. They're a snapshot
of where you are. Snapshots change. The person who scores twelve today and works on it for two years can
easily score three. That's the whole point of looking.""",
   "Old photos and new photos", "A SNAPSHOT, NOT A VERDICT")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. I have a high income. Do these signs still apply? Absolutely. Many high earners live
paycheck to paycheck because their spending rises with their income. In fact, a high income can hide these
signs for longer, until a job loss suddenly reveals them.""",
   "Business professional in office", "HIGH INCOME TOO?")
sc("""Question two. Which sign is most dangerous? For most people, it's the combination of no emergency fund
and growing credit card debt. Together, they create a cycle where every surprise adds expensive debt, and the
debt makes it harder to save for the next surprise.""",
   "Chain links close up", "THE MOST DANGEROUS COMBO")
sc("""Question three. Should I pay off debt or build savings first? Many planners suggest a small starter
emergency fund first, around one thousand dollars, so new surprises don't become new debt. Then attack high
interest debt aggressively. Then build the full emergency fund.""",
   "Balance scale with coins", "DEBT OR SAVINGS FIRST?")

sc("""Question four. I'm in my fifties and I matched most of these signs. Is it too late? No. Your fifties
are often your highest earning years, and the tax rules give you extra room to save through catch up
contributions. You may need to work a few years longer or adjust your retirement lifestyle, but every year
of strong saving now makes a real difference. Starting late beats never starting.""",
   "Older man working at desk", "IN YOUR FIFTIES?")
sc("""Question five. How often should I check these signs? A full checkup twice a year is plenty for most
people. Your net worth and savings rate are worth a quick look every month. The goal is to stay aware without
becoming obsessed. Money should serve your life, not take it over.""",
   "Calendar with two dates circled", "HOW OFTEN TO CHECK")
sc("""Question six. Can I fix several signs at once? You can, but most people do better fixing one or two at
a time. Each fix frees up money or attention for the next one. Paying off a card frees up cash for the
emergency fund. The emergency fund protects you from new debt. Small wins stack, and momentum is easier
to keep than to start.""",
   "Dominoes falling in a row", "ONE FIX LEADS TO THE NEXT")

# ---------------- Recap ----------------
ch("Recap: all 21 signs")
sc("""Quick recap. Angle one, the numbers. You don't know your net worth, you couldn't cover four hundred
dollars in cash, you save less than five percent, housing eats more than thirty percent, your car loan is six
years or longer, you pay only the minimum, and your retirement savings are behind.""",
   "Checklist on clipboard", "THE NUMBERS: 1 TO 7")
sc("""Angle two, the psychology. You feel rich on payday, you measure wealth by stuff, you count on future
money, you think everyone lives this way, you avoid your balance, you use credit to feel normal, and money
is always on your mind.""",
   "Person thinking at window", "THE PSYCHOLOGY: 8 TO 14")
sc("""Angle three, the playbook. One job loss from crisis, one income source, no insurance net, no
investments outside your home, convenience you can't afford, growing debt, and no plan.""",
   "Notebook with plan", "THE PLAYBOOK: 15 TO 21")

# ---------------- Close ----------------
ch("What to do next")
pr("""Remember, feeling poor and being poor are not the same, and feeling fine and being fine are not the
same either. The numbers tell the truth. Look at them regularly, and they will tell you exactly what to do
next. If you counted more signs than you'd like, that's okay. You now know exactly where to start. My
playbook walks through the whole plan step by step, and the link is in the description. Tell me your score in
the comments, no judgment. I'm Ryan Rover. See you in the next one.""")

save("video23", "21 Signs You're Poorer Than You Think", [
    "US Bureau of Economic Analysis, personal saving rate (around 4-5% in recent years)",
    "Federal Reserve, Survey of Consumer Finances 2022 (median net worth under 35: about $39,040)",
    "Federal Reserve, Economic Well-Being of U.S. Households in 2024 (63% would cover a $400 expense with cash or its equivalent)",
    "HUD, cost-burdened households (over 30% of income on housing); Harvard Joint Center for Housing Studies, State of the Nation's Housing",
    "Edmunds, share of new-car loans of 72 months or longer",
    "Federal Reserve, G.19 Consumer Credit: credit card interest rates",
    "Fidelity, retirement savings guideline (1x salary by 30, 3x by 40, 6x by 50, 8x by 60, 10x by 67)",
    "Social Security Administration (benefits replace about 40% of pre-retirement income for the average worker)",
    "Thomas J. Stanley, income statement vs balance sheet affluent; Mullainathan and Shafir, Scarcity (2013)",
    "American Psychological Association, Stress in America surveys; BLS JOLTS layoffs and discharges; Federal Reserve Bank of New York, Household Debt and Credit Report",
    "Growth example: monthly compounding at 7% average yearly return (illustration, not a promise)",
], "21 signs you're poorer than you think, from 3 angles: numbers, psychology, playbook")
