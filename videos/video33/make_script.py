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
        if text == "CARD":
            card("""Here's that journey on one chart. Five hundred dollars a month, for eleven years, at a seven percent average
yearly return. Watch how the green line pulls away from the dotted line, which is the money you put in yourself.""",
                 {"type": "growth", "monthly": 500, "rate": 0.07, "years": 11})
            continue
        sc(text, q, c)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. There's a number in personal finance that quietly changes everything. It's not a million
dollars. It's not even one hundred thousand. It's ten thousand dollars. When people finally get their first ten thousand
dollars saved and invested, something shifts. The math changes, the psychology changes, and the next ten thousand starts
coming faster. Today I'm going to show you why, and exactly how to get there.""")
short("Your first ten thousand dollars is the hardest money you'll ever make.")
card("""Here's the rule in one sentence. Your first ten thousand dollars is the hardest, and every ten thousand after it
comes faster. Investing five hundred dollars a month at a seven percent average yearly return, the first ten thousand takes
about nineteen months. The tenth ten thousand takes about nine.""",
     {"type": "compare", "left": {"label": "First $10,000", "big": "19 mo", "sub": "$500 a month"},
      "right": {"label": "Tenth $10,000", "big": "9 mo", "sub": "same $500 a month"},
      "note": "assuming 7% average yearly return, compounded monthly"})
sc("""Why does that happen? Because at first, you're doing all the work yourself. Every dollar in the account is a dollar
you earned, saved and moved. But once the balance gets bigger, the money itself starts helping. Growth that was a few
dollars a month becomes dozens, then hundreds. Ten thousand dollars is roughly where most people first start to notice
that help, and that's why it feels like a turning point.""",
   "Snowball rolling downhill", "THE MONEY STARTS HELPING")
sc("""We'll look at this from three angles. First, the numbers. What ten thousand dollars really does, how fast the next
milestones come, and what happens when it sits in the wrong place. Second, the psychology. Why the first ten thousand feels
impossible, and what changes in your head once you have it. And third, the playbook. A step by step plan to reach your first
ten thousand, protect it, and repeat it. Quick reminder, all growth examples here are illustrations, not promises.""",
   "Three paths in a forest", "THREE ANGLES")
pr("""Let's start with the numbers. And the first lesson is what ten thousand dollars actually does for you.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our numbers. All growth examples use monthly compounding with a stated average yearly return, usually seven percent.
These are illustrations, not predictions, because real markets go up and down. Emergency savings data comes from the Federal
Reserve's Survey of Household Economics and Decisionmaking. Credit card rates come from the Federal Reserve. Account rules
come from the IRS. This is education, not financial advice.""",
   "Financial data on screen", "OUR NUMBERS")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Seven lessons about what ten thousand dollars really does.""")

item(1, "Your money gets a job", "the first small paycheck",
"""Lesson number one. At ten thousand dollars, your money gets a job.""", [
("""At a seven percent average yearly return, ten thousand dollars earns roughly seven hundred dollars in a year. That's
about fifty eight dollars a month that you didn't work for. It won't change your life by itself. But it's a real, small
paycheck coming from your money instead of from your time. And for most people, it's the first time that has ever
happened.""", "Small paycheck envelope", "ABOUT $700 A YEAR"),
("""Compare that to one thousand dollars, which earns roughly seventy dollars a year at the same rate. Seventy dollars is
easy to ignore. Seven hundred is not. It's a car payment, a utility bill, a weekend trip. Ten thousand is roughly where
investment growth goes from invisible to noticeable, and noticing it changes how you feel about saving.""", "Comparing two amounts of coins", "$70 VS $700"),
("""And remember, that seven hundred dollars doesn't have to be spent. If you leave it invested, it earns its own growth
next year. Your money's job is to hire more workers, and those workers hire more workers. That's compounding, and ten
thousand dollars is when the hiring really starts to show.""", "Small team of workers", "MONEY HIRES MONEY"),
("""Try this. Calculate seven percent of whatever you have invested today. That's roughly what your money might earn for
you in a typical year. Write it down. Watching that number grow can become one of the most motivating numbers in your
financial life.""", "Person writing in notebook", "WHAT DOES YOURS EARN?"),
])

item(2, "Each $10,000 comes faster", "the milestone curve",
"""Lesson number two. Each ten thousand comes faster than the last.""", [
("""Let's follow one person investing five hundred dollars a month at a seven percent average yearly return. The first ten
thousand takes about nineteen months. The second ten thousand takes about eighteen. The third, about fifteen. By the fifth
ten thousand, it's about fourteen months, and the timing keeps shrinking.""", "Timeline with milestones", "19, 18, 15, 14 MONTHS"),
("CARD", None, None),
("""By the time this person goes from ninety thousand to one hundred thousand dollars, that ten thousand takes only about
nine months. Same five hundred dollars a month. Same effort. But the money already in the account is doing more and more of
the lifting. The whole journey to one hundred thousand takes roughly eleven years.""", "Runner speeding up", "THE TENTH TAKES 9 MONTHS"),
("""This is why Charlie Munger, Warren Buffett's longtime partner, reportedly said the first one hundred thousand is a
pain in the neck, but you have to do it. The early stretch feels slow because compounding hasn't had time to help yet. The
first ten thousand is the first sign that help is coming.""", "Older businessman portrait illustration", "THE FIRST ONE IS THE HARDEST"),
("""Try this. Make a simple milestone chart, ten thousand, twenty thousand, thirty thousand and so on. Put the date you hit
each one next to it. Over time, you'll see the gaps between dates shrink, and that visual proof is powerful.""", "Milestone chart on wall", "TRACK YOUR MILESTONES"),
])

body_hook = "There's a point where your money earns more than you put in."
item(3, "The crossover point", "when growth beats effort",
"""Lesson number three. The crossover point.""", [
("""There's a moment in every investing journey that feels like magic. It's the year when your investment growth is bigger
than the money you put in. For our five hundred dollars a month investor, that's six thousand dollars a year in
contributions. At seven percent, growth reaches six thousand dollars a year when the balance is in the low eighty
thousands.""", "Two lines crossing on graph", "GROWTH BEATS CONTRIBUTIONS"),
("""In this example, that takes roughly ten years. After the crossover, your money is earning more each year than you're
saving. If you kept going, the gap would widen every year. Eventually, contributions become a small part of the story, and
growth becomes the main character.""", "Graph line curving upward", "ABOUT 10 YEARS IN"),
("""Of course, real markets don't deliver seven percent every year. Some years are up a lot, some are down. But over long
periods, the pattern is the same. The balance has to grow before the growth can grow. And ten thousand dollars is the first
real step on that road to the crossover.""", "Stock chart with ups and downs", "MARKETS VARY"),
("""Try this. Divide your yearly contributions by seven percent. That's roughly the balance where your crossover begins. If
you invest six thousand a year, it's around eighty five thousand. Now you have a clear long term target.""", "Calculator on desk", "FIND YOUR CROSSOVER"),
])

item(4, "Where $10,000 sits matters", "same money, different results",
"""Lesson number four. Where your ten thousand sits matters enormously.""", [
("""Imagine you leave ten thousand dollars alone for thirty years. At two percent, roughly what some savings accounts have
paid, it grows to about eighteen thousand. At four percent, about thirty three thousand. At seven percent, about eighty one
thousand. At ten percent, almost two hundred thousand.""", "Four piles of different sizes", "$18K, $33K, $81K, $198K"),
("""Same ten thousand dollars. Same thirty years. The only difference is the average return. That's a gap of more than one
hundred sixty thousand dollars between the lowest and highest examples. Of course, higher returns usually come with more ups
and downs, so this isn't about chasing the highest number. It's about matching the money to its job.""", "Scales balancing risk and return", "SAME MONEY, DIFFERENT HOMES"),
("""Money you'll need in the next year or two belongs somewhere safe and available, like a high yield savings account.
Money you won't touch for decades usually belongs in diversified long term investments. The mistake is leaving decades long
money in places designed for short term safety.""", "Two labeled jars", "MATCH MONEY TO ITS JOB"),
("""Try this. Split your savings into two labels. Need it within three years, and won't need it for ten plus years. Then
check whether each pile is sitting in the right kind of account.""", "Labels on folders", "TWO LABELS"),
])

item(5, "Inflation shrinks idle money", "cash slowly melts",
"""Lesson number five. Idle cash slowly loses value.""", [
("""If inflation averages three percent a year, ten thousand dollars kept in cash for twenty years will buy only what about
fifty five hundred dollars buys today. The number on the screen still says ten thousand. But what it can buy has nearly been
cut in half.""", "Melting ice cube", "$10,000 BUYS LIKE $5,500"),
("""This is the hidden cost of playing it too safe for too long. Cash feels safe because the number never goes down. But
inflation is a slow leak. You don't notice it month to month, only when you look back years later and realize everything
costs more.""", "Grocery receipt prices", "A SLOW LEAK"),
("""That doesn't mean cash is bad. You need cash for emergencies and near term goals. It just means long term money needs to
grow faster than inflation to keep its buying power. Otherwise, you're getting poorer slowly while feeling safe.""", "Emergency fund jar", "CASH HAS A ROLE"),
("""Try this. Look up the current yield on your savings account. If it's well below the recent inflation rate, consider
whether some of that money belongs somewhere else.""", "Bank app interest rate", "CHECK YOUR RATE"),
])

item(6, "The emergency shield", "most people don't have it",
"""Lesson number six. Ten thousand dollars is a powerful shield.""", [
("""The Federal Reserve's Survey of Household Economics and Decisionmaking regularly asks Americans how they'd cover a four
hundred dollar emergency expense. In recent years, only around six in ten adults said they'd cover it with cash or its
equivalent. Many others said they'd borrow, sell something or couldn't cover it at all.""", "Survey report pages", "THE $400 QUESTION"),
("""Now imagine having ten thousand dollars set aside. A car repair, a medical bill, a sudden job loss. Instead of
reaching for a credit card at twenty percent interest, you handle it calmly. Ten thousand dollars turns emergencies into
inconveniences.""", "Person fixing car calmly", "EMERGENCIES BECOME INCONVENIENCES"),
("""It also protects your investments. People without cash reserves often have to sell investments at the worst time, like
during a market crash, to pay unexpected bills. A cash cushion lets your long term money stay invested and keep compounding.""", "Shield protecting coins", "IT PROTECTS YOUR INVESTMENTS"),
("""Try this. Figure out your essential monthly expenses, housing, food, utilities, insurance, transportation. Multiply by
three. That's a solid starting emergency fund target.""", "Budget spreadsheet", "THREE MONTHS OF ESSENTIALS"),
])

item(7, "The reverse rule", "$10,000 of debt",
"""Lesson number seven. The rule works in reverse too.""", [
("""Ten thousand dollars invested at seven percent can earn about seven hundred dollars a year. But ten thousand dollars of
credit card debt at twenty two percent can cost about two thousand two hundred dollars a year in interest. Same number, very
different direction.""", "Credit card statement", "$700 EARNED VS $2,200 PAID"),
("""Credit card rates in the United States have been above twenty percent on average in recent years, according to Federal
Reserve data. At that rate, a balance grows much faster than most investments. And if you only pay the minimum, the balance
can take many years to clear.""", "Credit card on table", "RATES ABOVE 20%"),
("""So for many people, the real ten thousand dollar rule starts with debt. Getting from minus ten thousand to zero is just
as powerful as getting from zero to ten thousand, and often more urgent. Every dollar of high interest debt you pay off is a
guaranteed return equal to its rate.""", "Debt payoff tracker", "MINUS 10K TO ZERO COUNTS"),
("""Try this. Add up every high interest balance you have. If it's large, your first milestone isn't ten thousand saved.
It's zero owed.""", "List of debts", "YOUR FIRST MILESTONE MIGHT BE ZERO"),
])

pr("""That's angle one. Your money gets a job, milestones speed up, the crossover point, where money sits, inflation, the
emergency shield, and the reverse rule. Now angle two. The psychology.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
sc("""Getting to ten thousand dollars isn't mainly a math problem. It's a behavior problem. Plenty of people earn enough to
save it but never do. And plenty of people who save it end up spending it. In this angle, we'll look at seven mental forces
that decide whether you reach your first ten thousand, and whether you keep it.""",
   "Brain and coins illustration", "A BEHAVIOR PROBLEM")

item(8, "Invisible progress", "why the start feels pointless",
"""Lesson number eight. Early progress feels invisible.""", [
("""When you're saving your first ten thousand, growth is tiny. In the first year, you might earn a couple hundred dollars
in returns. Almost everything in the account is money you put there yourself. It can feel like you're just moving money from
one pocket to another.""", "Small plant sprouting", "PROGRESS FEELS INVISIBLE"),
("""That's why so many people give up early. They don't see results quickly, so they assume it isn't working. But slow
early progress isn't failure. It's simply how compounding works. Results stay quiet for a while, then get loud.""", "Person giving up", "QUIET BEFORE LOUD"),
("""The trick is to measure what you can control. Your savings rate. Your consistency. The number of months in a row you
invested. Those numbers move right away, even when the balance seems slow.""", "Habit tracker with checkmarks", "MEASURE YOUR HABITS"),
("""Try this. Track your months in a row of saving, like a streak. Many people find that not wanting to break a streak is a
stronger motivator than watching a slow balance.""", "Calendar streak", "KEEP THE STREAK"),
])

item(9, "The goal gradient", "speeding up near the finish",
"""Lesson number nine. We speed up as goals get close.""", [
("""Psychologists call it the goal gradient effect. In a well known study, researchers Ran Kivetz, Oleg Urminsky and Yuhuang
Zheng found that coffee shop customers with reward cards bought coffee more often as they got closer to a free drink. The
closer the finish line, the harder people push.""", "Coffee loyalty card", "THE GOAL GRADIENT"),
("""The same study found something clever. Cards that started with two stamps already filled in got completed faster than
cards with fewer total stamps but no head start. Feeling like you've already made progress makes you more motivated to
finish.""", "Stamped reward card", "A HEAD START HELPS"),
("""That's why ten thousand dollars works so well as a goal. It's big enough to matter but close enough to feel reachable.
One million dollars feels like a fantasy. Ten thousand feels like a project.""", "Finish line ribbon", "CLOSE ENOUGH TO CHASE"),
("""Try this. Break your ten thousand into ten blocks of one thousand. Color in a block each time you hit one. You'll start
at block one, not zero, the moment you have a thousand saved.""", "Progress bar with blocks", "TEN BLOCKS OF $1,000"),
])

body_hook = "The moment people hit ten thousand dollars, many make this mistake."
item(10, "The spending trap", "having money makes you spend",
"""Lesson number ten. Reaching ten thousand creates a temptation.""", [
("""Here's a strange thing. Many people work hard to save ten thousand dollars, and then, almost as soon as they reach it,
they spend a big chunk. A newer car, a vacation, a big upgrade. Having the money makes it feel like they can afford things
they couldn't before.""", "Person at car dealership", "THE TEMPTATION"),
("""Researchers sometimes call this a wealth effect. When people feel richer, they tend to spend more. And ten thousand
dollars, sitting in a single account, can feel like a lot of money, even though it's really just the start of a foundation.""", "Shopping bags", "FEELING RICH"),
("""The fix is to decide in advance what the ten thousand is for, before you reach it. If it's your emergency fund, it's not
a car fund. If it's your investing base, it's not a vacation fund. Rules made in advance are much easier to keep.""", "Written plan on paper", "DECIDE IN ADVANCE"),
("""Try this. Give your ten thousand a name. Freedom fund, foundation fund, never broke again fund. It's surprisingly harder
to spend money you've named.""", "Label on savings jar", "NAME YOUR MONEY"),
])

pr("""Quick pause. If this is changing how you think about your first ten thousand, please subscribe to Ryan Rover Money.
It's free, and it helps us keep making these. Now, lesson eleven.""")

item(11, "Mental accounting", "money with labels",
"""Lesson number eleven. Use mental accounting on purpose.""", [
("""Nobel prize winning economist Richard Thaler described something called mental accounting. People treat money
differently depending on where it came from or what label it has. A tax refund feels like bonus money. A salary feels like
serious money. Logically, a dollar is a dollar, but our brains don't work that way.""", "Different labeled envelopes", "MENTAL ACCOUNTING"),
("""Usually mental accounting causes mistakes, like blowing a refund on things you'd never buy with your paycheck. But you
can flip it into an advantage. Separate accounts with clear labels make money harder to spend and easier to grow.""", "Multiple bank accounts on app", "FLIP IT TO YOUR SIDE"),
("""Many banks let you open several savings accounts or buckets, each with its own name. One for emergencies, one for a
down payment, one for travel. When each dollar has a job, you're much less likely to raid the important ones.""", "Savings buckets illustration", "BUCKETS WITH JOBS"),
("""Try this. Open a separate savings account for your ten thousand dollar goal, ideally at a different bank from your
checking account. Out of sight really does help keep it out of mind.""", "Two different bank cards", "A SEPARATE ACCOUNT"),
])

item(12, "Loss aversion", "the first drop hurts",
"""Lesson number twelve. Losses hurt more than gains feel good.""", [
("""Psychologists Daniel Kahneman and Amos Tversky showed that losses tend to feel roughly twice as painful as equal gains
feel good. Losing one thousand dollars hurts much more than gaining one thousand dollars feels nice.""", "Sad face and happy face", "LOSSES HURT MORE"),
("""This matters when you first invest your ten thousand. Markets fall sometimes, and a ten percent drop means watching
one thousand dollars disappear on paper. For a new investor, that can feel terrible, and some people sell in a panic,
locking in the loss.""", "Red stock chart", "THE FIRST DROP"),
("""Expect it before it happens. Market drops are a normal part of long term investing. Historically, broad markets have
recovered from past declines over time, though there's no guarantee and recovery can take years. Knowing that in advance
makes panic less likely.""", "Calm person reading", "EXPECT IT"),
("""Try this. Write a note to your future self now. When my investments drop, I will not sell. I invested for the long term.
Read it the next time the market falls.""", "Handwritten note", "A NOTE TO FUTURE YOU"),
])

item(13, "The identity shift", "from spender to investor",
"""Lesson number thirteen. Ten thousand changes who you are.""", [
("""Something deeper happens when you reach ten thousand dollars. You stop seeing yourself as someone who's bad with money.
You become someone who saves. Someone who invests. That change in identity often matters more than the money.""", "Person looking in mirror confidently", "A NEW IDENTITY"),
("""Habit writer James Clear argues that lasting change often comes from identity, not just goals. Instead of I want to save
money, the thought becomes I'm the kind of person who saves. Every deposit is a small vote for that new identity.""", "Ballot box votes", "EVERY DEPOSIT IS A VOTE"),
("""And once you believe you're a saver, decisions get easier. You don't agonize over every purchase, because the choice
already fits who you are. That's why the first ten thousand is so powerful. It's proof.""", "Person confidently declining purchase", "PROOF YOU CAN DO IT"),
("""Try this. Finish this sentence and say it out loud. I am someone who... Make it about the money habits you want. Then act
like that person this week.""", "Person speaking to camera", "I AM SOMEONE WHO"),
])

item(14, "The comparison trap", "other people's money",
"""Lesson number fourteen. Don't compare your chapter one to someone's chapter twenty.""", [
("""Social media makes it look like everyone has more money than you. New cars, big houses, fancy trips. Ten thousand dollars
can feel small next to that. But what you see online is spending, not saving, and spending is often funded by debt.""", "Person scrolling social media", "SPENDING IS VISIBLE"),
("""Thomas Stanley and William Danko, in The Millionaire Next Door, found that many millionaires they studied lived well below
their means, and that many high earners with flashy lifestyles had surprisingly little wealth. Looking rich and being rich are
often different things.""", "Modest house and luxury car", "LOOKING RICH VS BEING RICH"),
("""The person with ten thousand dollars invested and no debt may be in a much better position than a neighbor with a new
truck and a big loan. Your progress only needs to beat your own past, not someone else's highlight reel.""", "Person climbing stairs", "BEAT YOUR PAST SELF"),
("""Try this. Compare your net worth today with your net worth one year ago. That's the only comparison that really matters.""", "Net worth chart", "YOU VS LAST YEAR"),
])

pr("""That's angle two. Invisible progress, the goal gradient, the spending trap, mental accounting, loss aversion, the
identity shift and the comparison trap. Now angle three. The playbook.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
sc("""Here's a practical plan to reach your first ten thousand dollars, keep it, and repeat it. Six moves. You can start most
of them this week, and none of them require a high income, just a plan and some patience.""",
   "Toolbox on table", "SIX MOVES")

item(15, "Pick your number and date", "a real deadline",
"""Move number fifteen. Pick a monthly number and a date.""", [
("""A goal without a deadline is a wish. So pick your monthly amount and calculate your finish date. At a seven percent
average yearly return, three hundred dollars a month reaches ten thousand in about thirty one months. Five hundred dollars
a month, about nineteen months. Eight hundred dollars, about thirteen months.""", "Calendar with circled date", "300, 500 OR 800 A MONTH"),
("""If those numbers feel too high, start smaller and grow. Even one hundred dollars a month is a beginning. The important
thing is that the money moves automatically, every month, before you have a chance to spend it.""", "Automatic transfer screen", "START WHERE YOU ARE"),
("""Many people find money by reviewing subscriptions, insurance, phone plans and food spending. Cutting a few hundred
dollars a month from expenses you barely notice can cut a year or more off your timeline.""", "Subscription list being cut", "FIND THE MONEY"),
("""Try this. Write your ten thousand dollar date on a sticky note and put it somewhere you'll see daily, like your bathroom
mirror or your laptop.""", "Sticky note on mirror", "WRITE THE DATE"),
])

item(16, "Capture windfalls", "shortcut the timeline",
"""Move number sixteen. Capture windfalls.""", [
("""Tax refunds, bonuses, raises, cash gifts, money from selling things you don't use. These windfalls can shortcut your
path to ten thousand dollars dramatically. A single tax refund can be worth several months of regular saving.""", "Tax refund check", "WINDFALLS ARE SHORTCUTS"),
("""A simple rule many people use is to save at least half of any windfall before spending the rest. That way, you still get
to enjoy some of it, but your future self gets a big boost too.""", "Splitting money in half", "SAVE HALF"),
("""Raises are the most powerful windfall, because they repeat. If you raise your automatic savings each time your pay goes
up, your lifestyle grows a little and your savings grow a lot, without ever feeling like a sacrifice.""", "Pay raise letter", "SAVE YOUR RAISES"),
("""Try this. Decide right now what percentage of your next windfall goes to your ten thousand dollar goal. Deciding before
the money arrives is the key.""", "Person planning budget", "DECIDE BEFORE IT ARRIVES"),
])

item(17, "Build in the right order", "a simple sequence",
"""Move number seventeen. Build your ten thousand in the right order.""", [
("""Here's a common sequence. First, a starter emergency fund of about one thousand dollars. Second, if your employer offers
a retirement match, contribute enough to get the full match, because it's an immediate return on your money.""", "Steps on a staircase", "STARTER FUND, THEN THE MATCH"),
("""Third, pay off high interest debt like credit cards. Fourth, build your emergency fund up to three to six months of
essential expenses. Fifth, invest more for the long term, for example in an IRA and low cost broad index funds.""", "Checklist of steps", "DEBT, FUND, THEN INVEST"),
("""Your exact order may differ depending on your situation. But the principle holds. Protect yourself first, grab free
money, eliminate expensive debt, then let long term investing do the heavy lifting.""", "Person climbing steps", "PROTECT, GRAB, ELIMINATE, GROW"),
("""Try this. Figure out which step you're on today. Then focus only on that step until it's done.""", "Pointing at step", "WHICH STEP ARE YOU ON?"),
])

item(18, "Protect it", "make it hard to touch",
"""Move number eighteen. Protect your ten thousand.""", [
("""Once you have it, the goal is to keep it. That means making it a little harder to spend. A separate bank, no debit card
attached, and no link on your main banking app. Small barriers stop impulse spending surprisingly well.""", "Lock on piggy bank", "ADD FRICTION"),
("""Protecting it also means insurance. Health, auto, renters or home insurance, and for people with dependents, often life
and disability coverage. Insurance stops one bad event from wiping out years of saving.""", "Insurance documents", "INSURANCE IS PROTECTION"),
("""And it means avoiding scams and get rich quick offers. People with savings are exactly who scammers target. If someone
promises guaranteed high returns with no risk, that's a major warning sign.""", "Warning sign on phone", "AVOID SCAMS"),
("""Try this. Check that your savings account is FDIC insured, or NCUA insured at a credit union, and set up two factor
authentication on your financial accounts.""", "Security settings on phone", "INSURED AND SECURED"),
])

body_hook = "Once you have ten thousand dollars, do this immediately."
item(19, "Start the next $10,000", "momentum is everything",
"""Move number nineteen. Start the next ten thousand immediately.""", [
("""The biggest mistake after reaching ten thousand dollars is stopping. People hit the goal, celebrate, and then the
automatic transfers quietly end. But this is exactly when momentum matters most, because the next ten thousand comes faster
than the first.""", "Runner continuing past finish line", "DON'T STOP NOW"),
("""Keep your automatic contributions running, and point the new money at the next goal. If your emergency fund is full,
send it to long term investing. The habit you built for your first ten thousand is now your biggest financial asset.""", "Automatic investment confirmation", "KEEP IT RUNNING"),
("""Celebrate, but celebrate small. A nice dinner or a small treat is great. Just make sure the celebration doesn't cost a big
chunk of what you worked so hard to build.""", "Small celebration dinner", "CELEBRATE SMALL"),
("""Try this. The day you hit ten thousand, set your next milestone. Twenty five thousand. Fifty thousand. One hundred
thousand. Write the new date down right away.""", "New goal written down", "SET THE NEXT GOAL"),
])

item(20, "Raise the bar slowly", "the escalator",
"""Move number twenty. Raise your savings rate a little every year.""", [
("""Economists Richard Thaler and Shlomo Benartzi designed a program called Save More Tomorrow. Employees agreed in advance to
raise their retirement savings rate each time they got a raise. In their study, average savings rates for participants rose
dramatically over a few years.""", "Escalator going up", "SAVE MORE TOMORROW"),
("""The beauty of this approach is that you never feel a pay cut. Your take home pay still rises, just a little less than it
would have. Meanwhile, your savings rate climbs steadily, and so does your speed to each new milestone.""", "Paycheck growing", "NO PAY CUT FEELING"),
("""Many retirement plans offer an automatic increase feature, often called auto escalation. If yours does, turning it on is
one of the simplest wealth building moves you can make.""", "Retirement plan settings", "TURN ON AUTO ESCALATION"),
("""Try this. Raise your savings by one percent of your income today, and set a reminder to do it again in a year.""", "Reminder on phone", "ONE PERCENT MORE"),
])

# ---------------- Finding the money ----------------
ch("Where the ten thousand comes from")
pr("""Now, a lot of you are thinking, that's great, Ryan, but where do I find the money? Let's get practical. Here are five
common places people find money for their first ten thousand.""")
sc("""Place one. Recurring bills. Phone plans, insurance, internet and subscriptions are often set once and forgotten. Many
people save fifty to two hundred dollars a month just by calling providers, comparing quotes and canceling services they
rarely use. That money can go straight into an automatic transfer, and you won't miss it, because you weren't really using
it anyway.""",
   "Person reviewing bills at desk", "PLACE 1: RECURRING BILLS")
sc("""Place two. Food. For many households, food is one of the biggest flexible expenses. Cooking a few more meals at home,
planning a weekly grocery list and cutting food waste can free up a surprising amount of money without making life feel
smaller. Even redirecting one or two takeout orders a week adds up over a year.""",
   "Home cooked meal prep", "PLACE 2: FOOD")
sc("""Place three. Transportation. Cars are expensive to buy, insure, fuel and maintain. Keeping a reliable car a few years
longer instead of upgrading, or avoiding a large car payment, can free up hundreds of dollars a month. For some people, that
single decision is the fastest road to ten thousand dollars.""",
   "Older reliable car in driveway", "PLACE 3: TRANSPORTATION")
sc("""Place four. Extra income. Overtime, freelancing, a weekend side job, or selling things you no longer use. The key is
to send extra income straight to your goal instead of letting it blend into your everyday spending. Extra income that's
saved can cut your timeline in half.""",
   "Person working on laptop at night", "PLACE 4: EXTRA INCOME")
sc("""Place five. Your raise. The next time your pay goes up, send at least half of the increase to savings before you ever
get used to spending it. Your lifestyle still improves a little, and your ten thousand dollar date moves a lot closer.""",
   "Pay raise celebration", "PLACE 5: YOUR NEXT RAISE")

# ---------------- Story ----------------
ch("Two people, one number")
pr("""Let's put this all together with a simple example of two people.""")
short("Same income. Same ten thousand dollars. Completely different futures.")
sc("""Meet Alex and Jordan. Both are twenty eight. Both earn the same salary. Both spend two years saving their first ten
thousand dollars. On the day they hit it, they make different choices. Alex buys a newer car with the ten thousand as a down
payment and stops saving. Jordan leaves the money invested and keeps saving four hundred dollars a month.""",
   "Two friends side by side", "ALEX AND JORDAN")
sc("""Ten years later, Alex has a car that's worth much less than it cost, and probably a car payment too. Jordan, at a
seven percent average yearly return, would have roughly eighty nine thousand dollars. Same income. Same starting point. One
decision on the day they reached ten thousand dollars made all the difference.""",
   "Person reviewing growing account", "ONE DECISION")
sc("""And Jordan didn't do anything extraordinary. No stock picking. No side hustle empire. Just kept the first ten thousand
invested and kept the habit going. That's the ten thousand dollar rule in real life. It's not about the number. It's about
what you do once you reach it.""",
   "Calm person walking in park", "IT'S WHAT YOU DO NEXT")

# ---------------- By age ----------------
ch("The rule at every age")
sc("""In your twenties, ten thousand dollars invested has decades to grow. Left alone for forty years at seven percent, it
could become roughly one hundred sixty thousand dollars, without adding another cent. It's the most powerful ten thousand
you'll ever save.""",
   "Young adult with laptop", "IN YOUR 20s")
sc("""In your thirties and forties, ten thousand is often your emergency fund, your safety net while juggling a mortgage,
kids and a career. Building it protects everything else you're working toward, and lets your retirement savings keep
compounding uninterrupted.""",
   "Family at kitchen table", "IN YOUR 30s AND 40s")
sc("""In your fifties and sixties, ten thousand might be one of many milestones, or it might be your first. Either way, it's
not too late. Higher incomes later in life can make milestones come faster, and retirement accounts allow extra catch up
contributions for people fifty and older. Check the current limits with the IRS.""",
   "Mature couple planning", "IN YOUR 50s AND 60s")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. Should my first ten thousand be cash or investments? For many people, the first several thousand works
best as an emergency fund in a high yield savings account. Once you have a few months of expenses saved, additional money can
go toward long term investing.""",
   "Savings and investment apps", "CASH OR INVESTMENTS?")
sc("""Question two. Is ten thousand dollars enough to start investing? You can start investing with much less. Many
brokerages have no minimums and offer fractional shares. Ten thousand is a milestone, not an entry fee.""",
   "Investing app with small amount", "YOU CAN START WITH LESS")
sc("""Question three. What if I have debt and no savings? A common approach is to build a small starter emergency fund first,
maybe one thousand dollars, then attack high interest debt aggressively, then build your full emergency fund and invest.""",
   "Debt and savings balance", "DEBT AND NO SAVINGS")
sc("""Question four. How long should it take? It depends on your income and expenses. At three hundred dollars a month, about
two and a half years. At five hundred, about a year and a half. Faster with windfalls. What matters most is that you start.""",
   "Hourglass", "HOW LONG?")

sc("""Question five. What if I reach ten thousand and then need to spend some of it? That's okay. If it's your emergency
fund, that's literally what it's for. Use it, then rebuild it with the same automatic habit. A fund that gets used and refilled
is doing its job. The goal isn't to never touch it. The goal is to never need a credit card for an emergency again.""",
   "Person refilling jar with coins", "USING IT IS OKAY")
sc("""Question six. Should couples aim for ten thousand each or together? It depends on how you share finances. Many couples
start with one shared emergency fund, then build separate or joint investment goals. What matters most is that you agree on
the plan, talk about money regularly, and celebrate the milestones together.""",
   "Couple planning finances together", "COUPLES AND THE RULE")

# ---------------- Mistakes ----------------
ch("Four mistakes to avoid")
sc("""Mistake one. Waiting until you earn more. Most people think they'll save once they get a raise. But spending tends to
rise with income. The habit matters more than the amount, so start saving something now, and increase it later.""",
   "Person waiting at window", "WAITING FOR A RAISE")
sc("""Mistake two. Keeping all ten thousand in a checking account. It's too easy to spend, and it usually earns little or
nothing. Move it to a high yield savings account or invest it according to its job.""",
   "Checking account statement", "TOO EASY TO SPEND")
sc("""Mistake three. Treating the milestone like a finish line. Ten thousand dollars is the beginning. The people who build
real wealth are the ones who keep going after the first milestone, when momentum is finally on their side.""",
   "Runner at starting line", "IT'S A STARTING LINE")

sc("""Mistake four. Chasing a faster ten thousand with risky bets. When the goal feels slow, it's tempting to gamble on a hot
stock or a trendy coin to get there quicker. But big losses can push you right back to zero. Steady saving gets you to ten
thousand reliably. Gambling only gets you there by luck.""",
   "Dice on a trading screen", "MISTAKE 4: GAMBLING TO GET THERE")

# ---------------- Recap ----------------
ch("Recap")
sc("""Quick recap. Angle one, the numbers. Your money gets a job, each ten thousand comes faster, the crossover point, where
money sits, inflation, the emergency shield, and the reverse rule of debt.""",
   "Checklist on clipboard", "THE NUMBERS: 1 TO 7")
sc("""Angle two, the psychology. Invisible progress, the goal gradient, the spending trap, mental accounting, loss aversion,
the identity shift and the comparison trap.""",
   "Person thinking", "THE PSYCHOLOGY: 8 TO 14")
sc("""Angle three, the playbook. Pick your number and date, capture windfalls, build in the right order, protect it, start the
next ten thousand, and raise the bar slowly.""",
   "Notebook with plan", "THE PLAYBOOK: 15 TO 20")

# ---------------- Close ----------------
ch("What to do next")
pr("""Your first ten thousand dollars is the hardest money you'll ever save. But it's also the money that changes everything
after it. If you want my full step by step plan, it's in my playbook, linked in the description. Tell me in the comments,
what's your ten thousand dollar date? I'm Ryan Rover. See you in the next one.""")

save("video33", "The $10,000 Rule That Changes Everything", [
    "Federal Reserve, Economic Well-Being of U.S. Households (SHED): the $400 emergency question",
    "Federal Reserve, G.19 Consumer Credit (credit card interest rates)",
    "Kivetz, Urminsky and Zheng, The Goal-Gradient Hypothesis Resurrected (Journal of Marketing Research, 2006)",
    "Richard Thaler, Mental Accounting Matters (Journal of Behavioral Decision Making, 1999)",
    "Kahneman and Tversky, Prospect Theory (Econometrica, 1979)",
    "Thaler and Benartzi, Save More Tomorrow (Journal of Political Economy, 2004)",
    "Stanley and Danko, The Millionaire Next Door (1996)",
    "James Clear, Atomic Habits (2018): identity-based habits",
    "Charlie Munger's remark on the first $100,000 (widely reported)",
    "IRS, catch-up contribution rules for age 50 and older",
    "Growth examples: monthly compounding at stated average yearly returns (illustrations, not promises)",
], "the $10,000 rule in 20 lessons, from 3 angles: numbers, psychology, playbook")
