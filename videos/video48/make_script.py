import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

def item(n, title, sub, card_text, paras):
    """paras: list of (text, query, caption)"""
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"LEAK {n}")
    for t, q, c in paras:
        sc(t, q, c)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. You got the raise. Congratulations. Five thousand dollars more a year, maybe ten. And
then something strange happens. A year later, your savings look exactly the same. Your stress looks
exactly the same. The raise just vanished. Today, twenty ways your raise disappears, and how to keep the
next one.""")
short("Where did your raise go? Probably here.")
card("""Lifestyle inflation, sometimes called lifestyle creep, is when your spending rises every time your
income does, so a higher salary never turns into more savings.""",
     {"type": "stat", "label": "lifestyle inflation", "big": "+$ IN = +$ OUT", "size": 160, "sub": "when spending rises with every raise"})
sc("""Lifestyle inflation is sneaky because none of it feels like overspending. It feels like finally living
at the level you've earned. A slightly nicer apartment. A newer car. Better groceries. More dinners out. Each
upgrade is small and reasonable. Together, they can swallow an entire raise, and then some.""",
   "Upscale apartment living room", "IT FEELS EARNED")
sc("""We'll look at it from three angles. Angle one, the numbers: the first seven leaks, where the money from a
raise actually goes. Angle two, the psychology: why upgrades feel necessary and become permanent. And
angle three, the playbook: the leaks that hurt your long term wealth, and a simple rule that lets you enjoy
a raise and still get richer from it.""",
   "Three paths forest", "THREE ANGLES")
pr("""And if you've ever wondered why people earning twice as much as you still say they're broke, this video
answers that too. Let's start with the numbers.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Every number here comes from a named source. Spending patterns come from the Bureau of Labor Statistics
Consumer Expenditure Survey, which tracks how American households spend at different income levels. Tax
rules come from the IRS. Retirement plan rules come from the IRS and the Department of Labor. Examples use
stated, simple math, like a seven percent average yearly return. That's an illustration, not a promise.
This is education, not financial advice.""",
   "Bureau of Labor Statistics building", "OUR SOURCES")
card("""The Bureau of Labor Statistics Consumer Expenditure Survey shows a clear pattern. Households with higher
incomes spend more in almost every category, from housing to food away from home to entertainment.""",
     {"type": "stat", "label": "more income", "big": "MORE SPENDING", "size": 150, "sub": "in almost every category (BLS Consumer Expenditure Survey)"})

# ---------------- Joneses ----------------
ch("Keeping up with the Joneses")
sc("""The phrase keeping up with the Joneses comes from a comic strip that started in nineteen thirteen. It
followed a family desperately trying to match the lifestyle of their neighbors, the Joneses, who were never
actually shown. That's the joke. The people we compete with are often people we barely know, and whose
real finances we never see.""",
   "Vintage newspaper comic strip", "THE JONESES, 1913")
sc("""A century later, the Joneses aren't just next door. They're on every screen. Friends, influencers,
celebrities and strangers, all showing their best moments. Economists have found that people's
satisfaction with their income often depends on how it compares with others around them, not just on the
amount itself. That's why a raise can feel great until you see what someone else got.""",
   "Phone social media feed", "THE JONESES ARE EVERYWHERE")
sc("""The good news is that you can choose your comparison. Instead of comparing your lifestyle with other
people's, compare your savings rate this year with your savings rate last year. That's a race you can
actually win, and it's the only one that changes your future.""",
   "Progress chart notebook", "COMPARE WITH LAST YEAR'S YOU")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Where does the money from a raise actually go? Let's follow a five thousand
dollar raise.""")

item(1, "Taxes take the first bite", "the raise is smaller than it looks",
"""Leak number one. Taxes take the first bite.""",
[("""A five thousand dollar raise is not five thousand dollars in your pocket. Federal income tax, Social
Security and Medicare, and in many places state income tax all come out first. Depending on your situation,
the take home part of a five thousand dollar raise might be closer to thirty five hundred or four thousand
dollars. That's around three hundred dollars a month.""",
  "Paycheck stub deductions", "$5,000 BECOMES ~$300 A MONTH"),
 ("""This matters because people mentally spend the full raise. They think, I make five thousand more, so I can
afford a four hundred dollar car payment. But the real extra money might be three hundred a month. The
upgrade is already bigger than the raise before it starts.""",
  "Car loan paperwork", "SPENT BEFORE IT ARRIVES"),
 ("""And by the way, a common myth is that a raise can push you into a higher bracket and make you take home
less. That's not how it works. In the United States, only the dollars above a bracket threshold are taxed
at the higher rate. A raise almost always means more take home pay, just less than the headline number. Try
this: after your next raise, look at your actual paycheck before planning anything.""",
  "IRS tax brackets document", "ONLY THE EXTRA IS TAXED MORE")])
card("""A five thousand dollar raise, after federal income tax, Social Security, Medicare and state taxes, might
add only about three hundred dollars a month to take home pay, depending on your situation.""",
     {"type": "compare", "left": {"label": "The headline", "big": "$5,000", "sub": "a year raise"},
      "right": {"label": "Take home", "big": "~$300", "sub": "a month, roughly"},
      "note": "Illustration. Your taxes will differ."})

item(2, "The housing upgrade", "a bigger place, a bigger everything",
"""Leak number two. The housing upgrade.""",
[("""Housing is the biggest line in most budgets, and the most common place a raise goes. A nicer
neighborhood, one more bedroom, a building with a gym. Moving up two hundred or three hundred dollars a
month in rent can feel like a reasonable reward. And just like that, most of the raise is spent, every
month, for as long as you live there.""",
  "Modern apartment building", "RENT GOES UP"),
 ("""And it's never just rent. A bigger place means more furniture, higher utilities, higher renter's insurance,
maybe a parking spot. A house means higher property taxes and maintenance. The housing upgrade is usually
the leak that pulls several other leaks along with it.""",
  "Furniture store showroom", "AND EVERYTHING WITH IT"),
 ("""Try this: when your lease comes up after a raise, ask a different question. Not can I afford a nicer place?
But would a nicer place make me happier than having an extra three thousand dollars a year in
savings? Sometimes the answer is yes. Often, it isn't.""",
  "Lease renewal document", "ASK A DIFFERENT QUESTION")])

item(3, "The car upgrade", "the payment that never ends",
"""Leak number three. The car upgrade.""",
[("""A raise often comes with a new car. The old one works, but it's getting older, and now you can afford the
payment. Remember from my car payment video, the average new car payment has been around seven hundred
fifty dollars a month in recent years. Even a modest upgrade can eat two or three hundred dollars of your
monthly raise.""",
  "New car dealership", "THE NEW CAR"),
 ("""Add higher insurance for a newer, more expensive car, and the upgrade can easily cost more than the raise
itself. The raise lasts as long as your job. The car payment lasts five to seven years, even if your job
changes.""",
  "Insurance bill", "LONGER THAN THE RAISE"),
 ("""Try this: keep your current car until it truly needs replacing, and start paying yourself a car payment now
into a savings account. When the time comes, you'll buy the next car with a big down payment, or cash, and
your raise will have built savings instead of a loan.""",
  "Savings jar car fund", "PAY YOURSELF FIRST")])

item(4, "Subscriptions stack", "small monthly charges",
"""Leak number four. Subscriptions.""",
[("""Streaming services, music, cloud storage, apps, meal kits, fitness classes, premium memberships. Each one
is ten, fifteen, or twenty dollars a month. With a raise, adding one more feels like nothing. But eight or
ten subscriptions can easily reach one hundred fifty to two hundred dollars a month, which is over two
thousand dollars a year.""",
  "Streaming apps on television", "TEN DOLLARS AT A TIME"),
 ("""Subscriptions are designed to be easy to start and easy to forget. Free trials that convert automatically.
Annual renewals that arrive when you're not paying attention. Price increases that happen quietly. Many
people pay for services they haven't used in months.""",
  "Credit card subscription charges", "EASY TO FORGET"),
 ("""Try this: list every subscription from your bank and card statements. Cancel anything you haven't used in
the last month. Rotate streaming services instead of keeping them all. One month for one service, then
switch. You'll still have plenty to watch.""",
  "Cancel subscription button", "LIST, CANCEL, ROTATE")])

item(5, "Eating out more", "convenience on a plate",
"""Leak number five. Eating out and delivery.""",
[("""When money is tight, people cook. When money loosens, takeout and restaurants become a habit. The BLS data
shows food away from home rising with income. And delivery adds fees, tips and menu markups, so the same
meal can cost much more than eating at the restaurant, and far more than cooking.""",
  "Food delivery bag", "FOOD AWAY FROM HOME"),
 ("""Eating out isn't bad. It's one of the best ways to spend time with people you love. The problem is when it
replaces home cooking out of habit, not choice. A few extra delivery orders a week can add up to several
hundred dollars a month.""",
  "Couple at restaurant table", "HABIT VS CHOICE"),
 ("""Try this: decide how many meals out per week fit your goals, then enjoy them fully, without guilt. For
everything else, keep a few easy, fast meals at home for tired nights, which is when most delivery orders
happen.""",
  "Simple home cooked meal", "PLAN THE EASY NIGHTS")])

item(6, "Premium everything", "the quiet upgrade",
"""Leak number six. Premium versions of everyday things.""",
[("""This is the quietest leak. After a raise, the grocery cart changes. Organic versions, name brands, fancier
coffee, nicer shampoo, better wine. None of these choices is big. But a ten to twenty percent increase on
groceries and household items can add up to over one hundred dollars a month for a family.""",
  "Premium grocery products shelf", "THE QUIET UPGRADE"),
 ("""Some upgrades are worth it to you, and that's fine. The leak happens when you upgrade everything
automatically, without asking which ones actually matter. Many store brands are made to similar standards
as name brands, at a lower price.""",
  "Store brand vs name brand", "UPGRADE WHAT MATTERS"),
 ("""Try this: pick three things where premium truly makes you happier, maybe coffee, a good mattress, quality
shoes. Spend well on those. For everything else, buy the good enough version. That's how you upgrade your
life without upgrading your whole budget.""",
  "Good coffee morning", "PICK THREE")])

item(7, "Tech upgrades", "the new phone every year",
"""Leak number seven. Constant tech upgrades.""",
[("""New phones, laptops, watches, headphones and gaming gear arrive every year, and carriers make upgrading easy
with monthly payment plans. A thousand dollar phone spread over two or three years looks like a small
monthly charge, and the next upgrade is always being advertised.""",
  "New smartphone launch", "THE ANNUAL UPGRADE"),
 ("""Modern devices often last many years with a new battery and good care. Upgrading every year or two instead
of every four or five can cost hundreds of dollars a year, often for features you barely notice after the
first week.""",
  "Old phone still working", "IT STILL WORKS"),
 ("""Try this: keep your devices until they stop doing what you need, not until a new one comes out. When you do
upgrade, consider the previous year's model, which often costs much less and does almost everything the
newest one does.""",
  "Previous model phone discount", "LAST YEAR'S MODEL")])
sc("""Let's add up the first seven leaks with very modest numbers. Higher rent, two hundred. Car upgrade, two
hundred. Subscriptions, fifty. More eating out, one hundred. Premium groceries, fifty. Tech, thirty. That's
six hundred thirty dollars a month. Remember, the raise only added about three hundred dollars of take home
pay. The lifestyle grew twice as fast as the income.""",
   "Calculator adding numbers", "$630 OF NEW SPENDING")
card("""A five thousand dollar raise can add about three hundred dollars a month to take home pay. Seven small
upgrades can add over six hundred dollars a month in new spending.""",
     {"type": "compare", "left": {"label": "Raise, take home", "big": "~$300", "sub": "a month"},
      "right": {"label": "New spending", "big": "~$630", "sub": "a month, seven upgrades"},
      "note": "Illustration with modest numbers."})
pr("""That's how people earn more and end up with less. Now, why do these upgrades feel so necessary? Angle
two.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
pr("""Angle two. The psychology. Eight reasons upgrades feel necessary, and then become permanent.""")
short("Why every upgrade becomes your new normal")

item(8, "The hedonic treadmill", "new becomes normal",
"""Leak number eight. The hedonic treadmill.""",
[("""Psychologists use the term hedonic treadmill to describe how people adapt to changes in their lives. A
new apartment, a new car or a pay raise feels great at first. But within months, it becomes normal. The
happiness boost fades, and we start looking for the next upgrade.""",
  "Treadmill running", "NEW BECOMES NORMAL"),
 ("""This is why lifestyle inflation never feels like enough. You run faster, earn more, spend more, and your
happiness stays roughly in the same place. Meanwhile, the costs stay locked in. You're running on a
treadmill that keeps getting more expensive.""",
  "Running in place", "RUNNING IN PLACE"),
 ("""Try this: before any permanent upgrade, ask, how will I feel about this in six months, when it's normal?
If the honest answer is that you won't notice it much, keep the money. Spend instead on things that keep
giving, like experiences, health, and time with people you love.""",
  "Friends laughing outdoors", "WHAT KEEPS GIVING")])

item(9, "A new peer group", "new job, new normal",
"""Leak number nine. A new peer group.""",
[("""Raises often come with a new role, a new company or a new circle. And new peers bring new norms. Different
restaurants for lunch, more expensive hobbies, nicer vacations, bigger houses. What was a luxury in your
old circle is ordinary in the new one.""",
  "Business colleagues lunch", "NEW CIRCLE, NEW NORMS"),
 ("""It's natural to want to fit in. But your new peers might have different finances. Some earn more. Some have
family money. Some carry a lot of debt. Matching their lifestyle with your income is one of the fastest
ways to lose a raise.""",
  "Golf course business", "THEIR NORMAL ISN'T YOUR PLAN"),
 ("""Try this: join in on your terms. Say yes to the events that matter, suggest cheaper options sometimes, and
don't apologize for having goals. You'll find that many people respect someone who's clear about their
priorities.""",
  "Confident person at work", "JOIN ON YOUR TERMS")])

item(10, "Treat yourself, every week", "rewards become routine",
"""Leak number ten. Treat yourself becomes every week.""",
[("""Treats are great. The problem is frequency. When a treat is rare, it's special. When it becomes weekly, it's
just spending. After a raise, treats tend to multiply. The Friday dinner, the weekend shopping trip, the
random online order because it was a long day.""",
  "Shopping bags weekend", "TREATS MULTIPLY"),
 ("""And the more often you treat yourself, the less each treat feels like a treat. That's the hedonic treadmill
again. You need more to feel the same. Rare treats are both cheaper and more enjoyable.""",
  "Gift box opening", "RARE IS BETTER"),
 ("""Try this: give yourself a set amount of fun money each month, and spend it any way you like, guilt free. When
it's gone, it's gone until next month. Limits make treats feel special again.""",
  "Envelope labeled fun money", "A FUN MONEY BUDGET")])

item(11, "Paying for convenience", "buying back time",
"""Leak number eleven. Paying for convenience.""",
[("""With more income, it's tempting to pay for time. Cleaning services, delivery, rideshares, dry cleaning,
grocery pickup. Some of these can genuinely be worth it, especially if they free time for family, rest or
higher paying work. Research on time and happiness suggests that buying time can improve well being.""",
  "House cleaning service", "BUYING TIME"),
 ("""The leak happens when convenience spending isn't a choice, it's a default. Rideshares when a short walk or
bus works fine. Delivery for things you'll pass on the way home. Convenience is easy to justify one
purchase at a time, and hard to see in total.""",
  "Rideshare app car", "CONVENIENCE BY DEFAULT"),
 ("""Try this: choose one or two convenience services that genuinely give you meaningful time, and keep them.
Drop the rest. That way you're buying time on purpose, instead of leaking money out of habit.""",
  "Family time at home", "BUY TIME ON PURPOSE")])

item(12, "Vacations escalate", "every trip must top the last",
"""Leak number twelve. Escalating vacations.""",
[("""With a raise, vacations often level up. A longer trip, a nicer hotel, a flight upgrade, a more distant
destination. Travel can be one of the most rewarding things to spend money on. But many people put trips on
credit cards and spend the next months paying them off.""",
  "Luxury resort pool", "LEVEL UP TRAVEL"),
 ("""There's also a comparison trap. Each trip has to beat the last one, and the one you saw online. That
escalation can turn a joyful habit into a big yearly expense, financed with debt.""",
  "Airplane window view", "BEAT THE LAST TRIP"),
 ("""Try this: set up a travel sinking fund and pay for trips with cash you've already saved. Decide the budget
before you plan, not after. You'll enjoy the trip more when there's no bill waiting at home.""",
  "Travel savings jar", "A TRAVEL FUND")])

item(13, "Kids' lifestyle creep", "activities, gear, expectations",
"""Leak number thirteen. Kids' lifestyle creep.""",
[("""Parents want the best for their kids, and a raise can make it feel possible. More activities, private
lessons, travel sports, newer gear, bigger birthday parties. Each choice comes from love. But the costs
can rise fast, and kids quickly adapt to the new normal, just like adults.""",
  "Kids sports team", "OUT OF LOVE"),
 ("""The hard truth is that kids often value time and attention more than the most expensive version of every
activity. And one of the biggest gifts you can give them is parents who aren't stressed about money, and a
retirement that won't depend on them later.""",
  "Parent reading with child", "TIME OVER STUFF"),
 ("""Try this: let each child pick one or two activities they love, and set a yearly budget for them. Involve
older kids in the decisions. It teaches them about trade offs, which might be one of the most valuable
lessons of all.""",
  "Family planning together", "TEACH THE TRADE OFFS")])

item(14, "Gifts and obligations", "the social cost of success",
"""Leak number fourteen. Gifts and social obligations.""",
[("""When you earn more, people may expect more. Bigger wedding gifts, more expensive birthday presents, picking
up the check more often, helping family members. Some of this is generous and beautiful. Some of it
happens because you feel you should, not because you want to.""",
  "Wrapped gifts table", "EXPECTED GENEROSITY"),
 ("""Try this: decide your giving on purpose. Set a yearly budget for gifts and help, and plan for it in your
sinking funds. Generosity is one of the best uses of money. Just make it a choice, not a pressure, so it
doesn't quietly replace your own savings.""",
  "Budget notebook gifts", "GIVE ON PURPOSE"),
 ("""And remember, the most meaningful gifts are rarely the most expensive. A handwritten note, time together, a
shared experience. People remember how you made them feel much more than what you spent.""",
  "Handwritten card", "MEANING OVER PRICE")])

item(15, "Status brands", "paying for the logo",
"""Leak number fifteen. Status brands.""",
[("""With more income, it's tempting to signal success. Designer clothes, a luxury watch, a premium car badge.
Economists have studied conspicuous consumption, spending meant to be seen, for over a century. Thorstein
Veblen coined the term back in eighteen ninety nine.""",
  "Designer store window", "CONSPICUOUS CONSUMPTION"),
 ("""The trouble is that status spending is a race with no finish line. There's always a more expensive brand,
and the people you're signaling to are usually too busy with their own lives to notice. Meanwhile, quiet
wealth, the kind in investment accounts, is invisible but much more powerful.""",
  "Luxury watch close up", "A RACE WITH NO FINISH"),
 ("""Try this: before buying a status item, ask who it's for. If it's genuinely for you, because you love the
quality and will use it for years, fine. If it's for an audience, consider whether that audience is worth the
money.""",
  "Person thinking mirror", "WHO IS IT FOR?")])

# ---------------- Signs ----------------
ch("Signs you're on the treadmill")
sc("""Before the playbook, five signs you're on the lifestyle treadmill. One. You earn more than you did three
years ago, but your savings balance is about the same. Two. You can't name where your last raise went.
Three. Your fixed monthly costs have grown faster than your take home pay.""",
   "Treadmill gym", "SIGNS 1 TO 3")
sc("""Four. You often think, I'd be fine if I just earned a little more. And five. Most of your upgrades in the
last year were things you'd now struggle to undo, like a lease, a loan or a contract. If three or more of
these feel familiar, you're not bad with money. You're normal. But normal is exactly what the playbook is
designed to fix.""",
   "Person reflecting window", "SIGNS 4 AND 5")

# ---------------- Mid ----------------
ch("A quick favor")
pr("""Quick pause. If you're counting your own leaks right now, you're not alone. Subscribe to the channel if
this is helping. It's free, and it helps me keep making these videos for you. Now, the last five leaks, the
ones that hurt your future most.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
pr("""Angle three. The five leaks that hurt your long term wealth, and then the rule that stops them all.""")
short("The raise rule that makes you rich instead of busy")

item(16, "Not raising your contributions", "the raise skips your future",
"""Leak number sixteen. Not raising your retirement contributions.""",
[("""Here's a quiet one. Many people set their retirement contribution once, as a percent of pay, and never
touch it again. If it's a percent, it grows a little with a raise. But if it's a flat dollar amount, a raise
does nothing for your future at all. All of the raise goes to today.""",
  "401k enrollment form", "SET ONCE, NEVER CHANGED"),
 ("""Many workplace plans offer an automatic increase feature, sometimes called auto escalation, that raises your
contribution by one percent each year. It's one of the easiest ways to grow your savings without feeling
it, because the increase usually comes with a raise.""",
  "Benefits portal on laptop", "AUTO ESCALATION"),
 ("""Try this: log into your retirement plan today and check two things. Are you getting the full employer
match? And is automatic increase turned on? If not, turn it on. It takes five minutes and could be worth
tens of thousands of dollars over your career.""",
  "Person clicking settings laptop", "FIVE MINUTES TODAY")])

item(17, "Higher limits, higher balances", "credit grows with income",
"""Leak number seventeen. Higher credit limits.""",
[("""When your income rises, card companies often raise your limits, and offer new cards. More available credit
can make bigger purchases feel affordable, even if you don't have the cash. For people who pay in full,
this doesn't matter much. For people who carry a balance, it can mean the debt grows with the income.""",
  "Credit limit increase notice", "MORE ROOM TO BORROW"),
 ("""Try this: treat your income, not your credit limit, as your spending ceiling. If you ever carry a balance,
put the first part of every raise toward paying it off. Clearing high interest debt is like giving yourself a
second raise.""",
  "Paying off credit card", "A SECOND RAISE"),
 ("""It's also worth checking how many cards you actually need. Every new card offer after a raise is
designed to capture some of your new income. One or two cards, paid in full every month, cover almost
everything most people need. More cards mostly mean more temptation and more due dates.""",
  "Wallet few cards", "ONE OR TWO IS ENOUGH")])

item(18, "Debt financed upgrades", "borrowing against the raise",
"""Leak number eighteen. Financing upgrades against future raises.""",
[("""Some people spend a raise before they get it. They expect a promotion, so they buy the bigger house or the
nicer car now, assuming the money will be there. But raises can be delayed, jobs can change, and companies
can cut costs. Borrowing against future income turns a hope into an obligation.""",
  "Promotion letter", "SPENDING THE FUTURE"),
 ("""Try this: only upgrade after the raise has actually arrived, and after it's been in your paycheck for at
least a few months. If you can live without the upgrade during that time, you might find you don't need it
at all.""",
  "Waiting calendar months", "WAIT FOR THE MONEY"),
 ("""A useful habit is to live on last year's income for the first few months of a new raise. Bank the
difference. If the raise turns out to be stable and you still want the upgrade, you'll be able to buy it
with savings instead of a loan, which is a much stronger position.""",
  "Savings growing app", "LIVE ON LAST YEAR'S INCOME")])

item(19, "No plan for bonuses", "windfalls without a job",
"""Leak number nineteen. Bonuses and windfalls with no plan.""",
[("""Bonuses, tax refunds, commissions and gifts often arrive without a plan. And money without a plan tends to
disappear into the general spending pool. Many people can't say, a month later, what happened to their last
bonus.""",
  "Bonus check", "WHERE DID IT GO?"),
 ("""Try this: set a simple windfall rule before the money arrives. For example, half to long term goals like
investing or debt, a quarter to a near term goal like a trip or a car fund, and a quarter for pure fun. You
get to enjoy it, and you still make real progress.""",
  "Pie chart split", "A WINDFALL RULE"),
 ("""And if the bonus is large, give yourself a cooling off period. Park it in a high yield savings account for
thirty days before deciding anything. Big money decisions made in the excitement of a windfall are
rarely the best ones. A month of patience costs nothing and often saves a lot.""",
  "Calendar thirty days", "PARK IT FOR 30 DAYS")])

item(20, "Locked in costs", "contracts outlive raises",
"""Leak number twenty. Locking in costs with contracts.""",
[("""The most dangerous upgrades are the ones you can't easily undo. Long leases, car loans, mortgages, annual
memberships, phone contracts, private school commitments. Once signed, they stay, even if your income drops.
Lifestyle inflation becomes lifestyle lock in.""",
  "Signing long contract", "LIFESTYLE LOCK IN"),
 ("""This is why many financial planners suggest keeping your fixed costs well below your income, so that if you
lose a job or take a pay cut, you can still cover them. Flexibility is a form of wealth.""",
  "Flexible bamboo plant", "FLEXIBILITY IS WEALTH"),
 ("""Try this: before signing any contract after a raise, ask, could I still pay this if my income went back to
what it was last year? If the answer is no, you're betting the raise is permanent. Sometimes that's a good
bet. Just make it on purpose.""",
  "Person reviewing contract", "THE LAST YEAR TEST")])

ch("The 50/50 raise rule")
pr("""So how do you enjoy a raise and still build wealth? Here's the simplest rule I know.""")
card("""The fifty fifty raise rule. Every time your income goes up, send at least half of the increase to your
future, and enjoy the other half guilt free.""",
     {"type": "stat", "label": "the raise rule", "big": "50 / 50", "sub": "half to your future, half to enjoy"})
sc("""Here's how it works. Your take home pay goes up three hundred dollars a month. You immediately send one
hundred fifty to investing, debt payoff or savings, ideally on autopay, before you ever see it. The other one
hundred fifty is yours to enjoy. A nicer dinner, a hobby, a small upgrade. No guilt.""",
   "Two jars split coins", "HALF AND HALF")
sc("""Why it works: you still feel the raise, so you don't feel deprived. But your savings rate goes up every
single year. Over a career with many raises, that steady increase can build serious wealth, without ever
feeling like a sacrifice.""",
   "Stairs going up", "THE SAVINGS RATE CLIMBS")
card("""Investing an extra one hundred fifty dollars a month from one raise, at a seven percent average yearly
return, for twenty five years. And that's just one raise.""",
     {"type": "growth", "monthly": 150, "rate": 0.07, "years": 25})
sc("""And here's the magic. You'll probably get several raises over the next decade. If you apply the rule each
time, the amounts stack. One hundred fifty, then three hundred, then four hundred fifty a month going to your
future, while your lifestyle still improves every year. That's what getting richer actually looks like.""",
   "Stacking blocks growing", "THE RAISES STACK")

# ---------------- Three incomes ----------------
ch("The same trap at three incomes")
pr("""Let's see lifestyle inflation at three income levels. Because it doesn't disappear when you earn more. It
just gets more expensive.""")
sc("""At fifty thousand dollars a year, the trap looks like this. A car payment that's a little too high, a few
streaming services, takeout twice a week, and a credit card that's never quite paid off. The person feels
like they'd be fine if they only earned a bit more.""",
   "Small apartment kitchen", "AT $50,000")
sc("""At one hundred thousand, they do earn more. Now there's a bigger apartment or a starter home, two car
payments in the household, a gym membership, more travel, and nicer restaurants. Savings are still small,
because the new lifestyle costs almost exactly what the new income brings. They feel like they'd be fine if
they only earned a bit more.""",
   "Suburban home two cars", "AT $100,000")
sc("""At two hundred thousand, the house is larger, the cars are luxury models, the kids are in expensive
activities, and vacations are international. The numbers are bigger, but the feeling is the same. Tight.
And notice the sentence they repeat. I'd be fine if I only earned a bit more. That sentence is the
treadmill talking.""",
   "Large house luxury car", "AT $200,000")
sc("""Now picture the same three people following the fifty fifty rule. At fifty thousand, they save a little.
At one hundred thousand, they save a meaningful amount. At two hundred thousand, they can save a large share
of their income and still live very comfortably. The income is the same in both versions. The difference is
whether the raises went to the treadmill or to the future.""",
   "Calm person savings growing", "SAME INCOME, DIFFERENT ENDINGS")

# ---------------- Undo in 30 days ----------------
ch("Undo lifestyle creep in 30 days")
pr("""If you're already deep in lifestyle creep, here's a thirty day reset. Four weeks, four steps.""")
sc("""Week one. Look. Download two months of statements and sort every expense into three groups. Needs, wants
you love, and wants you barely notice. That third group is your target. Most people find a few hundred
dollars a month there without cutting anything they truly care about.""",
   "Highlighting bank statements", "WEEK 1: LOOK")
sc("""Week two. Cut the invisible. Cancel the subscriptions you don't use, call your phone, internet and insurance
providers to lower your rates, and remove saved cards from shopping apps. These are one time actions that save
money every month after.""",
   "Phone call to provider", "WEEK 2: CUT THE INVISIBLE")
sc("""Week three. Automate the savings. Take the amount you freed up and set it to transfer automatically to
savings or investing on payday. If the money disappears before you see it, you won't miss it. If it stays in
checking, lifestyle creep will find it.""",
   "Automatic transfer banking app", "WEEK 3: AUTOMATE")
sc("""And week four. Decide the next raise. Write down, today, what you'll do with your next raise. Fifty fifty,
or whatever split you choose. Turn on automatic increases in your retirement plan. That way, when the raise
comes, the decision is already made, and the treadmill doesn't get a vote.""",
   "Writing plan in notebook", "WEEK 4: DECIDE THE NEXT RAISE")

# ---------------- Stories ----------------
ch("Two coworkers, same raises")
short("Two coworkers got the same raises. One got rich.")
sc("""Let's look at two coworkers who got the same raises over ten years, from fifty thousand to eighty five
thousand dollars a year. Ashley upgraded with every raise. A bigger apartment, a new car, more dinners out,
nicer trips. At eighty five thousand, she had the same savings rate she had at fifty, close to zero, and
still felt tight every month.""",
   "Woman in nice apartment worried", "ASHLEY: EVERY UPGRADE")
sc("""Ben followed the fifty fifty rule. With each raise, half went to his 401k and investments, and half to his
life. His apartment got a bit nicer, he upgraded his car once, he traveled more. But his savings rate climbed
from five percent to almost twenty percent of his pay over the decade.""",
   "Man relaxed reading at home", "BEN: FIFTY FIFTY")
sc("""After ten years, Ashley had a few thousand dollars saved. Ben had well over one hundred thousand dollars
invested, depending on the market. Both enjoyed their lives. Both felt their income go up. But only one of
them turned those raises into freedom.""",
   "Two paths in road", "SAME RAISES, DIFFERENT FUTURES")
sc("""And here's the part people miss. Ben didn't feel deprived. He felt every raise. He just felt half of each
one. Ashley felt every raise fully, for a few months, and then it disappeared into her new normal. The
treadmill took it.""",
   "Happy man walking city", "HE FELT EVERY RAISE")

sc("""One more thing about Ben. Because his fixed costs stayed reasonable, he had options. When his company
went through layoffs in year eight, he wasn't panicked. He had savings, a manageable rent and no car
payment. He took his time, found a better job, and kept going. Ashley, with higher fixed costs, felt she had
to stay in a job she didn't like, because she couldn't afford even a short gap in income. Lifestyle
inflation doesn't just cost money. It costs choices.""",
   "Man calm at job interview", "IT COSTS CHOICES")

# ---------------- FAQ ----------------
ch("Questions people ask")
pr("""A few questions people ask me about lifestyle inflation.""")
sc("""Question one. Is all lifestyle inflation bad? No. Some upgrades genuinely improve your life, like a safer
neighborhood, a shorter commute, better health care, or more time with family. The goal isn't to never
upgrade. It's to upgrade on purpose, and make sure your savings grow too.""",
   "Family in safe neighborhood", "IS ALL OF IT BAD?")
sc("""Question two. What if I already inflated my lifestyle? Start with the leak that costs the most and adds the
least joy. Often it's subscriptions, delivery, or a car payment. Undo one, and send that money to savings
automatically. Then apply the fifty fifty rule to your next raise.""",
   "Person reviewing budget", "ALREADY INFLATED?")
sc("""Question three. What percent of income should I save? A common target for retirement is around fifteen
percent of pre tax income, including any employer match, though it depends on your age and goals. If you're
far from that, the raise rule is one of the most painless ways to get there.""",
   "Percentage sign savings", "HOW MUCH TO SAVE?")
sc("""Question four. My partner spends every raise. What do I do? Talk about goals before you talk about
spending. What do you both want in five or ten years? Then agree on a simple rule, like fifty fifty, and
automate it. It's easier to agree on a system than to argue about every purchase.""",
   "Couple talking at table", "MY PARTNER SPENDS IT")
sc("""Question six. What if my raise is small, like two or three percent? Then the rule matters even more, because
small raises are the easiest to lose without noticing. Even half of a small raise, sent to savings every year,
adds up over a career. And small raises often roughly match inflation, so not spending them on upgrades
keeps your budget from slipping backward.""",
   "Small raise letter", "WHAT IF IT'S SMALL?")
sc("""And question five. Does lifestyle inflation happen to rich people too? Absolutely. Many high earners, like
doctors, lawyers and executives, struggle with it because their peer groups spend heavily. Income doesn't
protect you from lifestyle inflation. A plan does.""",
   "Doctor in hospital hallway", "RICH PEOPLE TOO?")

sc("""Before we wrap up, one honest note. Enjoying your money is part of the point. You worked for that raise.
The goal of this video isn't to make you feel guilty about a nice dinner or a better apartment. It's to make
sure that years from now, your raises added up to something you can see, not just a lifestyle you can't
afford to leave.""",
   "Person enjoying dinner happy", "ENJOY IT, AND KEEP SOME")

# ---------------- Recap ----------------
ch("Recap: all 20 leaks")
short("20 ways your raise disappears")
sc("""Quick recap. The money leaks: taxes, housing, cars, subscriptions, eating out, premium everything, and tech
upgrades. The mind leaks: the hedonic treadmill, a new peer group, weekly treats, convenience spending,
escalating vacations, kids' lifestyle creep, gifts and obligations, and status brands.""",
   "Checklist clipboard", "THE FIRST 15")
sc("""And the future leaks: not raising your contributions, higher credit limits, upgrades financed against future
raises, bonuses with no plan, and locked in contracts. One rule stops them all. Half of every raise to your
future. Half to enjoy.""",
   "Two jars coins", "THE LAST 5 AND THE RULE")

# ---------------- Close ----------------
ch("What to do next")
pr("""If you want the full plan for turning every raise into real wealth, it's in my playbook. The link is in
the description. And watch my video on why most people stay broke. Lifestyle inflation is one of the
biggest reasons. I'm Ryan Rover. See you in the next one.""")

save("video48", "Lifestyle Inflation: 20 Ways Your Raise Disappears", [
    "U.S. Bureau of Labor Statistics, Consumer Expenditure Survey (spending by income level)",
    "IRS, federal income tax brackets (marginal rates); Social Security and Medicare payroll taxes",
    "IRS and U.S. Department of Labor, 401(k) plan rules (employer match, automatic increase features)",
    "Thorstein Veblen, The Theory of the Leisure Class (1899): conspicuous consumption",
    "Research on hedonic adaptation and on buying time and well-being",
    "Raise, spending and growth figures: stated illustrative math",
], "lifestyle inflation: numbers, psychology, playbook")
