import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

body_hook = None  # set right before item() to start a Short at its first explained scene

def item(n, title, sub, card_text, body, example, q1, c1, q2, c2):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"HABIT {n}")
    global body_hook
    if body_hook:
        short(body_hook); body_hook = None
    sc(body, q1, c1)
    sc(example, q2, c2)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Most people who stay broke aren't lazy, and they aren't bad with money in some
obvious way. They work hard. They pay their bills. And still, every month, the money just disappears. The
reason is usually not one big mistake. It's a handful of small habits that run quietly in the background,
like apps draining your phone battery. Today, twenty five of them.""")
short("More than a third of Americans can't do this.")
card("""Here's why this matters. In the Federal Reserve's survey of household well being for twenty twenty
four, about sixty three percent of adults said they would cover a four hundred dollar emergency expense
using cash or its equivalent. That means more than a third would not.""",
     {"type": "stat", "label": "could cover a $400 emergency with cash", "big": "63%", "sub": "Federal Reserve, SHED 2024"})
sc("""Think about that. Tens of millions of working adults, many with decent jobs, would have to borrow,
sell something, or simply not pay if a four hundred dollar bill showed up tomorrow. That's not usually a
salary problem. Plenty of people with good incomes are in that group. It's a habits problem, and habits can
be changed.""",
   "Worried person looking at bills", "MORE THAN A THIRD")
sc("""We'll look at these twenty five habits from three angles. First, the numbers. Habits with a cost you
can actually measure. Second, the psychology. The mental shortcuts that keep you spending without noticing.
And third, the playbook. The missing systems that keep people stuck, and what to replace them with. Stay to
the end, because the last angle is where things start to turn around.""",
   "Three doors in hallway", "THREE ANGLES")
pr("""Let's start with the numbers. And habit number one is something almost everyone does, every single
day.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our numbers come from named sources. Household emergency data comes from the Federal Reserve's Survey
of Household Economics and Decisionmaking. Credit card rates come from the Federal Reserve's consumer credit
reports. Banking fee data comes from the Consumer Financial Protection Bureau. Growth examples use simple
stated math, like a seven percent average yearly return. That's an illustration, not a promise. This is
education, not financial advice.""",
   "Federal Reserve building Washington", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Nine habits where the cost is right there in black and white, if you look.""")

item(1, "Not knowing where the money goes", "the invisible budget",
"""Habit number one. Not knowing where your money actually goes.""",
"""Ask most people what they spend in a month on food, and they'll give you a number. Ask them to check
their statements, and the real number is often much higher. It's not dishonesty. Small purchases are easy
to forget. A coffee here, a snack there, a quick online order. None of them feel like spending.""",
"""You can't fix what you can't see. People who build wealth almost always know their numbers, at least
roughly. Try this: for the next thirty days, track every single purchase, even the one dollar ones. Use an
app or a note on your phone. At the end, sort them into five or six categories. The biggest surprise on
that list is where you start.""",
"Receipts pile on table", "WHERE DID IT GO?",
"Phone budgeting app", "TRACK 30 DAYS")

item(2, "Carrying a credit card balance", "the 20% habit",
"""Habit number two. Carrying a balance on your credit card.""",
"""According to the Federal Reserve, the average rate on credit card accounts that pay interest has been
above twenty percent in recent years. On a five thousand dollar balance, that's roughly a thousand dollars a
year in interest alone. And if you only make the minimum payment, it can take many years to pay off.""",
"""This habit keeps people broke because it works in reverse compounding. Instead of your money growing for
you, your debt grows against you. Try this: list every card with its balance and rate. Pay the minimum on
all of them, and put every extra dollar on the one with the highest rate. When it's gone, roll that payment
to the next one. It's called the avalanche method.""",
"Credit card in wallet", "$1,000 A YEAR IN INTEREST",
"Avalanche snow mountain", "THE AVALANCHE METHOD")

item(3, "Paying bank fees", "overdrafts and maintenance",
"""Habit number three. Paying bank fees as if they were normal.""",
"""The Consumer Financial Protection Bureau has reported that banks collected billions of dollars a year
in overdraft and non sufficient funds fees, and that a small share of customers pay most of them. An
overdraft fee has often been around thirty dollars or more, sometimes on a purchase of just a few
dollars.""",
"""Many banks and credit unions now offer accounts with no monthly fee and no overdraft fees. Switching takes
an afternoon. Try this: look at your last six months of statements and add up every fee. Then call your
bank and ask them to waive the most recent one. Many will, once. And if your bank won't stop charging you,
consider moving to one that doesn't.""",
"Bank branch exterior", "$30 FOR A $5 COFFEE",
"Person on phone with bank", "ASK THEM TO WAIVE IT")

body_hook = 'The one question that keeps people broke.'
item(4, "Financing everything", "the monthly payment mindset",
"""Habit number four. Thinking in monthly payments.""",
"""Car dealers, phone carriers and even furniture stores love to ask one question. What monthly payment are
you comfortable with? Once you think in payments instead of total price, almost anything feels affordable.
Edmunds has reported average new car payments well above seven hundred dollars a month in recent years.""",
"""The problem is that payments stack. A car, a phone, a couch, a laptop, a buy now pay later order. Each
one feels small. Together they can eat a huge share of your income before you've bought a single grocery.
Try this: add up every monthly payment you have, excluding rent or mortgage. Write the total on a sticky
note and put it somewhere you'll see it.""",
"Car dealership showroom", "WHAT PAYMENT IS COMFORTABLE?",
"Sticky notes on wall", "ADD UP THE PAYMENTS")

item(5, "Ignoring small subscriptions", "death by a thousand charges",
"""Habit number five. Ignoring small recurring charges.""",
"""Streaming, music, cloud storage, apps, delivery memberships, gym, meal kits. Each one is a few dollars a
month. Surveys regularly find that people underestimate what they spend on subscriptions, sometimes by
quite a lot. Companies count on auto renewal and on you forgetting.""",
"""Ten dollars a month doesn't sound like much. But ten subscriptions at ten dollars is one hundred dollars
a month, twelve hundred a year. Try this: search your statements for every charge that repeats. Next to
each one, write the last date you used it. Cancel anything older than a month. If you really miss it, you
can sign up again later.""",
"Streaming services logos on TV", "$10 X 10 = $1,200 A YEAR",
"Laptop canceling account", "CANCEL THE OLD ONES")

item(6, "Eating out by default", "the most common budget leak",
"""Habit number six. Eating out because there's no plan.""",
"""Food away from home is one of the biggest budget categories for American households, according to the
Bureau of Labor Statistics consumer expenditure data. Much of it isn't special dinners. It's the default
choice at the end of a long day, when there's nothing ready at home.""",
"""The fix isn't to never eat out. It's to make eating at home the easy option. Try this: on Sunday, plan
four simple dinners for the week and buy only what you need for them. Cook double portions so you have
lunches. If you replace even three takeout meals a week, the yearly savings can be well over a thousand
dollars for many families.""",
"Fast food drive through", "THE DEFAULT DINNER",
"Meal prep containers kitchen", "PLAN FOUR DINNERS")

item(7, "Keeping cash in a zero interest account", "letting inflation win",
"""Habit number seven. Leaving savings in an account that pays almost nothing.""",
"""Many traditional savings accounts pay a tiny interest rate, while online high yield savings accounts
have offered rates several times higher in recent years. When inflation runs at a few percent and your
savings earn close to zero, your money is losing buying power every year, even though the balance looks the
same.""",
"""Your emergency fund should be safe and easy to reach, so a high yield savings account insured by the
FDIC is a common choice. Try this: check the rate on your savings account today. Then compare it with a few
FDIC insured high yield accounts. If the gap is big, moving the money takes about fifteen minutes and costs
nothing.""",
"Piggy bank on table", "EARNING ALMOST NOTHING",
"Online banking on laptop", "FDIC INSURED, HIGHER RATE")

item(8, "Paying late", "fees and a damaged score",
"""Habit number eight. Paying bills late.""",
"""Late payments cost twice. First, the late fee itself, which can be thirty dollars or more on a credit
card. Second, if a payment is reported as thirty days late or more, it can hurt your credit score for
years. A lower score means higher rates on car loans, mortgages and sometimes even insurance.""",
"""Most late payments aren't because people can't pay. They just forget. Try this: set every bill you can
to automatic payment of at least the minimum, timed a few days after payday. Then set a monthly reminder to
review them. Automation removes the forgetting, and the review keeps you in control.""",
"Calendar with due date circled", "LATE FEES + LOWER SCORE",
"Automatic payment setup screen", "AUTOMATE THE MINIMUM")

item(9, "Buying new when used works", "paying for the first scratch",
"""Habit number nine. Always buying new.""",
"""Cars, furniture, tools, baby gear, sports equipment, textbooks. Many of these lose a big part of their
value right after the first purchase. Buying lightly used lets someone else pay for that first drop. For
cars, the first few years usually bring the biggest loss in value.""",
"""This doesn't mean buying junk. It means checking the used market first, especially for things that last.
Try this: next time you need something over one hundred dollars, spend ten minutes checking used options
locally or online before you buy new. Over a lifetime, that one habit can add up to tens of thousands of
dollars.""",
"Garage sale furniture", "LET SOMEONE ELSE PAY THE DROP",
"Used bicycle shop", "CHECK USED FIRST")

ch("Why small leaks sink big ships")
sc("""Before we move on, let's do the math on why these quiet habits matter so much. Benjamin Franklin
supposedly warned to beware of little expenses, because a small leak will sink a great ship. Whether he
said it exactly that way or not, the math agrees. A six dollar daily habit is over two thousand dollars a
year. A forty dollar monthly fee is almost five hundred. A credit card balance at twenty percent quietly
takes a thousand dollars a year on five thousand owed.""",
   "Old sailing ship at sea", "SMALL LEAKS, BIG SHIPS")
sc("""Now stack a few of those together. A forgotten subscription or two, a bank fee here and there, some
interest, takeout three extra nights a week, and a car payment bigger than it needs to be. For many
households that easily adds up to several hundred dollars a month. That's money that isn't going into an
emergency fund, isn't paying down debt and isn't being invested. Month after month, year after year.""",
   "Water dripping from faucet", "IT ALL STACKS UP")
sc("""And here's the part most people miss. Those leaks don't only cost what you spend. They cost what that
money could have become. Every dollar that leaks out today is a dollar that never gets the chance to
compound for the next twenty or thirty years. That's why fixing these habits in your twenties or thirties is
so powerful, and why fixing them at any age is still worth it.""",
   "Clock and coins concept", "THE COST OF WHAT COULD HAVE BEEN")

card("""Here's what fixing these first nine habits can add up to. Say they free up four hundred dollars a
month, and you invest it at a seven percent average yearly return. After twenty five years, that's roughly
three hundred twenty four thousand dollars.""",
     {"type": "growth", "monthly": 400, "rate": 0.07, "years": 25})

pr("""That's angle one. Notice that none of these are dramatic. They're quiet. That's exactly why they're
dangerous. Now angle two, the psychology. These are the mental habits that make the money habits possible.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
sc("""Spending decisions happen fast, often in seconds, and usually without much thinking. Behavioral
economists, like Nobel Prize winners Daniel Kahneman and Richard Thaler, spent decades showing that humans
aren't perfectly rational with money. We use shortcuts. Those shortcuts are useful in daily life, but some
of them quietly keep us broke.""",
   "Brain illustration concept", "MENTAL SHORTCUTS")

body_hook = 'Why your tax refund vanishes in weeks.'
item(10, "Treating windfalls as fun money", "the bonus that vanishes",
"""Habit number ten. Treating extra money as free money.""",
"""A tax refund, a bonus, a birthday check, a side gig payment. Thaler called this mental accounting. We put
money into different mental buckets, and money that feels unexpected goes into the fun bucket. But a
dollar is a dollar, whether it came from your paycheck or a refund.""",
"""The IRS has reported average federal tax refunds of roughly three thousand dollars in recent years. For
many households, that's the single biggest chunk of money they get all year, and it often disappears
within weeks. Try this: before your next windfall arrives, decide in writing where it goes. For example,
half to savings or debt, half to enjoy. Decide before you see the money.""",
"Envelope with cash bonus", "A DOLLAR IS A DOLLAR",
"Tax refund check", "DECIDE BEFORE IT ARRIVES")

item(11, "Rewarding yourself constantly", "I deserve this",
"""Habit number eleven. Rewarding yourself for everything.""",
"""Hard day, buy something. Good day, buy something. Finished a project, buy something. Treats are fine,
but when every feeling becomes a reason to spend, rewards stop being special and start being a budget line.
Many people don't notice how often they use the words I deserve this.""",
"""The trick is to find rewards that don't cost much. A walk, a long call with a friend, a favorite meal
cooked at home, an hour with a book. Save the bigger rewards for real milestones. Try this: for one week,
notice every time you think I deserve this before buying. Just count them. The number alone can change
your behavior.""",
"Shopping bags celebration", "I DESERVE THIS",
"Person reading in park", "CHEAPER REWARDS")

item(12, "Keeping up with friends", "social spending pressure",
"""Habit number twelve. Spending to keep up with friends.""",
"""Group dinners, weekend trips, bachelor parties, concerts, birthday gifts. Saying no feels awkward, so
many people say yes and put it on a card. Surveys from places like Bankrate and Credit Karma have found
that many adults admit to overspending to keep up with friends.""",
"""Real friends usually understand. Most people are relieved when someone else suggests a cheaper plan. Try
this: be the one who suggests the potluck, the hike, the game night at home. And when you can't afford
something, say it simply. That's not in my budget this month, but let's do something next week. You'll be
surprised how many people feel the same.""",
"Friends at expensive restaurant", "THE AWKWARD YES",
"Friends having picnic in park", "SUGGEST THE CHEAPER PLAN")

item(13, "Living for today only", "present bias",
"""Habit number thirteen. Always choosing today over tomorrow.""",
"""Economists call it present bias. We value a reward today much more than a bigger reward later. That's
why saving for retirement feels so hard. Retirement is far away, and the new jacket is right here. Your
future self feels almost like a stranger.""",
"""Researchers have found that helping people picture their future selves can make them save more. Try
this: write a short letter from yourself at age seventy, thanking you for what you start today. It sounds
silly, but it makes the future feel real. Then set up one small automatic transfer to a retirement
account.""",
"Older person looking at old photos", "PRESENT BIAS",
"Handwritten letter on desk", "A LETTER FROM FUTURE YOU")

item(14, "Avoiding money completely", "the ostrich effect",
"""Habit number fourteen. Not looking at your accounts.""",
"""Researchers have documented what they call the ostrich effect. People check their accounts less often
when they expect bad news. It feels better in the moment, but problems grow in the dark. Fees pile up,
fraud goes unnoticed, and debt keeps compounding.""",
"""Avoiding money is usually about feelings, like shame or anxiety, not about laziness. The fix is to make
looking small and regular. Try this: set a ten minute money date once a week. Same day, same time, with a
coffee or tea. Open every account, look at the balance, check for anything strange, and close it. That's
it.""",
"Ostrich in grassland", "THE OSTRICH EFFECT",
"Coffee and laptop on table", "A 10 MINUTE MONEY DATE")

pr("""Quick break. If these habits sound familiar, you're not alone, and that's exactly why I make these
videos. If you want more breakdowns like this, subscribe to Ryan Rover Money. It's free and it really helps
the channel. Okay, back to the psychology, and habit fifteen.""")

item(15, "Believing it's too late", "the fresh start you skip",
"""Habit number fifteen. Believing it's too late to start.""",
"""People in their thirties think they missed their twenties. People in their fifties think they missed
everything. So they don't start at all. But time works forward. The best day to start was years ago. The
second best day is today.""",
"""Here's encouraging math. Someone who starts at forty five and invests five hundred dollars a month at a
seven percent average yearly return could have roughly four hundred thousand dollars by sixty five. Not
the same as starting at twenty five, but far better than zero. Try this: replace the thought it's too late
with the question what can I do in the next ten years?""",
"Middle aged man planning", "IT'S NOT TOO LATE",
"Sunrise over mountains", "THE NEXT TEN YEARS")

item(16, "Believing more income will fix it", "the raise that disappears",
"""Habit number sixteen. Believing a bigger paycheck will fix everything.""",
"""More income helps, absolutely. But if the habits don't change, spending tends to rise to match the new
income. Economists call this lifestyle inflation. Plenty of high earners live paycheck to paycheck, and
plenty of average earners build real wealth.""",
"""The test is simple. If you can't save anything at your current income, a raise alone probably won't
change that. The habit has to come first. Try this: practice saving even five percent of what you earn
now. When the raise comes, keep your lifestyle the same for six months and save the difference.""",
"Office worker with paycheck", "SPENDING RISES TOO",
"Savings jar with coins", "HABIT FIRST, RAISE SECOND")

item(17, "Believing money is for other people", "the identity trap",
"""Habit number seventeen. Believing wealth is for other people.""",
"""Some people grow up hearing that rich people are greedy, that money is the root of all evil, or that
people like us don't invest. Those beliefs can quietly stop you from opening an investment account, asking
for a raise, or learning how money works.""",
"""Stanley's research found that many American millionaires were first generation wealthy. They didn't
inherit it. They were teachers, engineers, small business owners. Try this: write down three beliefs about
money you grew up with. Next to each one, ask: is this actually true, or is it just familiar?""",
"Family dinner conversation", "THE STORIES WE GREW UP WITH",
"Notebook with handwritten list", "TRUE OR JUST FAMILIAR?")

ch("Why your brain fights saving")
sc("""Let's go one level deeper on the psychology, because understanding this takes away a lot of the
guilt. Spending gives your brain a reward right now. Saving gives you a reward years from now, in a future
you can't see or feel. Studies of decision making show that people tend to discount future rewards steeply,
which is a fancy way of saying a dollar today feels much bigger than a dollar later.""",
   "Brain scan illustration", "NOW FEELS BIGGER")
sc("""On top of that, modern shopping is designed to remove every bit of friction. One click checkout,
saved cards, tap to pay, buy now pay later. Researchers have found that people tend to spend more when
paying feels less painful, for example with cards instead of cash. When paying doesn't hurt, spending
grows without you noticing.""",
   "Tap to pay contactless card", "PAYING DOESN'T HURT")
sc("""So the solution isn't to feel more guilty. It's to flip the friction. Make spending a little harder
and saving completely automatic. Delete saved cards from shopping sites. Turn off one click buying. Take
shopping apps off your home screen. And move savings automatically, so the good choice happens without
needing willpower at all.""",
   "Smartphone home screen apps", "FLIP THE FRICTION")

pr("""That's angle two. Mental accounting, rewards, peer pressure, present bias, avoidance, and the stories
we tell ourselves. Now angle three. The playbook. These are the systems that are missing in most broke
households, and the good news is they're easy to install.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
sc("""Willpower runs out. Systems don't. The people who stay on track with money usually aren't more
disciplined than everyone else. They've just built a few simple systems so the right thing happens
automatically. The last eight habits on our list are missing systems.""",
   "Gears machine working", "SYSTEMS BEAT WILLPOWER")

item(18, "No emergency fund", "every surprise becomes debt",
"""Habit number eighteen. Living without an emergency fund.""",
"""Without a cash cushion, every flat tire, dentist visit or broken phone goes on a credit card. Then the
interest makes the surprise even more expensive. It's one of the main ways people get stuck in a cycle of
debt that never quite ends.""",
"""A common starting goal is one thousand dollars, then one month of expenses, then three to six months.
Try this: open a separate savings account just for emergencies, with a name like do not touch. Set an
automatic transfer of even twenty five dollars every payday. Small and automatic beats big and someday.""",
"Flat tire on car", "EVERY SURPRISE BECOMES DEBT",
"Savings account app", "START WITH $1,000")

body_hook = "Stop saving what's left over. Do this instead."
item(19, "Saving what's left over", "there is never anything left",
"""Habit number nineteen. Saving whatever is left at the end of the month.""",
"""For most people, there's nothing left at the end of the month. Spending expands to fill whatever is
available. That's why saving last almost never works.""",
"""The fix is to pay yourself first. On payday, before you spend anything, a set amount moves automatically
into savings or investments. You then live on what remains. Try this: set up an automatic transfer for the
day after payday. Start with five percent of your take home pay. Raise it by one percent every few months.
You'll barely notice.""",
"Empty wallet", "NOTHING LEFT",
"Paycheck direct deposit", "PAY YOURSELF FIRST")

item(20, "Skipping the employer match", "free money left behind",
"""Habit number twenty. Not taking the full employer match.""",
"""Many employers match part of what you put into a four oh one k, for example fifty cents for every dollar
up to a certain percent of your salary. If you don't contribute enough to get the full match, you're
leaving part of your pay on the table.""",
"""It's one of the few places in personal finance where you get an instant return just for participating.
Try this: log into your benefits portal this week, or ask HR, and find out exactly what the match is. Then
make sure your contribution is at least high enough to get all of it.""",
"Office workers in meeting", "FREE MONEY ON THE TABLE",
"Retirement plan paperwork", "GET THE FULL MATCH")

item(21, "Never investing", "cash alone can't keep up",
"""Habit number twenty one. Never investing at all.""",
"""Saving keeps money safe. Investing helps it grow. Over long periods, broad stock market investments have
historically grown faster than savings accounts and inflation, though with ups and downs along the way and
no guarantees. People who never invest miss out on compounding completely.""",
"""You don't need to pick stocks. Many people use broad, low cost index funds through a retirement account.
Try this: once your emergency fund is started and high interest debt is under control, open a retirement
account and make one small automatic investment each month. Learning by doing beats waiting until you know
everything.""",
"Stock market screen green", "LET IT GROW",
"Person using investing app", "START SMALL")

item(22, "No written goals", "aiming at nothing",
"""Habit number twenty two. Having no written money goals.""",
"""Without a goal, every purchase competes only with the moment. With a goal, every purchase competes with
something you really want, like a house, freedom from debt, or an early retirement. Goals give saving a
reason.""",
"""Make goals specific. Not save more, but save six thousand dollars for an emergency fund by December. Try
this: write down three money goals, one for this year, one for five years, and one for twenty years. Put a
number and a date on each one. Keep the list where you'll see it.""",
"Dartboard with arrow", "AIMING AT NOTHING",
"Written goals on paper", "A NUMBER AND A DATE")

item(23, "Never asking for more", "income left on the table",
"""Habit number twenty three. Never negotiating.""",
"""Salary, rent, insurance, phone plans, car prices, medical bills. Many of these are more flexible than
people think. But most people accept the first number they're given. Over a career, not negotiating salary
can cost a lot, because every future raise is built on top of your starting pay.""",
"""Negotiating doesn't have to be aggressive. It's research plus a polite question. Try this: once a year,
call your insurance and phone providers and ask if there's a better rate. And before your next review,
look up salary data for your role so you can ask for a raise with numbers, not hope.""",
"Handshake business meeting", "THE FIRST NUMBER ISN'T FINAL",
"Person on phone negotiating", "ASK ONCE A YEAR")

item(24, "Not protecting what you have", "one disaster away",
"""Habit number twenty four. Skipping basic protection.""",
"""Health insurance, renters or homeowners insurance, enough car insurance, and life insurance if people
depend on your income. One uninsured accident or illness can wipe out years of progress. Medical bills are
a common reason families fall into debt.""",
"""Insurance is boring until the day you need it. The goal isn't to insure everything, but to protect
against the disasters you could never pay for. Try this: make a one page list of every policy you have,
what it covers and what it costs. Look for gaps, and look for overlap you can cut.""",
"Insurance documents on desk", "ONE DISASTER AWAY",
"Family home exterior", "PROTECT THE BASICS")

item(25, "Doing it all alone", "money is a team sport",
"""And habit number twenty five. Trying to do it all alone.""",
"""Money is still a taboo topic in many families. People don't talk about salaries, debt or mistakes. So
everyone struggles in private, repeating the same mistakes their parents made. Couples who never talk about
money often fight about it later.""",
"""Find your money team. That could be your partner, a friend working on the same goals, a free nonprofit
credit counselor, or a fee only financial planner. Try this: schedule one honest money conversation this
month with someone you trust. Share one goal and one struggle. Saying it out loud makes it real.""",
"Couple talking at kitchen table", "THE TABOO TOPIC",
"Friends talking over coffee", "FIND YOUR MONEY TEAM")

# ---------------- Story ----------------
ch("Two paychecks, two stories")
pr("""Let me show you how these habits play out with two people earning exactly the same.""")
short('Same paycheck. Completely different life.')
sc("""Jordan and Taylor both earn sixty thousand dollars a year. Jordan has most of the habits on this list.
A car payment, a credit card balance, a pile of subscriptions, takeout most nights, and no automatic
savings. Every month, Jordan's account hits nearly zero right before payday. Jordan isn't reckless. Jordan
is just running on default settings.""",
   "Young professional tired at desk", "JORDAN: DEFAULT SETTINGS")
sc("""Taylor earns the same, but set up a few systems early. Automatic transfer to savings the day after
payday. Full employer match. A used car paid in cash. Credit card paid in full. Groceries planned on
Sundays. Taylor still eats out and travels, just on purpose.""",
   "Young woman planning with notebook", "TAYLOR: A FEW SYSTEMS")
sc("""Ten years later, Taylor has a full emergency fund and retirement savings growing steadily. Jordan has
the same income, the same job title, and still no cushion, plus a credit card balance that never seems to
shrink. Same paycheck. Completely different life. The difference was never income. It was habits.""",
   "Two paths diverging road", "SAME PAYCHECK, DIFFERENT LIFE")

sc("""Fifteen years later, the gap is even wider. Taylor's investments are now growing by thousands of
dollars in a good year, sometimes more than Taylor adds. Taylor could handle a job loss, help a family member,
or change careers without panic. Jordan, meanwhile, feels trapped. Every raise has been swallowed by a new
payment. Jordan works just as hard as Taylor, maybe harder, and has far less to show for it.""",
   "Person looking out window thinking", "15 YEARS LATER")
sc("""The good news is that Jordan can still turn this around, at any point. Not by becoming a different
person, but by copying Taylor's few systems, one at a time. Autopay. Pay yourself first. Get the full match.
Pay off the card. Plan dinners. Each one is small. Together, they rewrite the story.""",
   "Sunrise over city skyline", "IT'S NEVER TOO LATE TO SWITCH")

# ---------------- Swaps ----------------
ch("The habits that replace them")
pr("""Breaking a habit is much easier when you replace it with something. So here are the swaps that people
who build wealth tend to make.""")
sc("""Swap one. Instead of checking social media when you're bored, check your accounts once a week. It
sounds dull, but people who look at their money regularly tend to make better decisions with it. You catch
fraud early, you notice the leaks, and you see your progress, which keeps you motivated.""",
   "Person checking phone on couch", "SCROLL LESS, CHECK MORE")
sc("""Swap two. Instead of the monthly payment question, ask the total cost question. What will this cost
me in total, including interest, insurance, maintenance and everything else? Swap three. Instead of buying
on impulse, use a waiting rule. Twenty four hours for small things, thirty days for big things. Most wants
fade. The ones that remain are probably worth it.""",
   "Calendar pages flipping", "TOTAL COST AND WAITING RULES")
sc("""Swap four. Instead of spending a windfall, split it in advance. Swap five. Instead of saving what's
left, save first and spend what's left. Swap six. Instead of avoiding money talk, have a regular money
meeting with your partner or with yourself. Same day each month, same questions. What came in, what went
out, are we on track, and what's one thing to improve?""",
   "Couple at kitchen table with laptop", "SPLIT, SAVE FIRST, TALK")
sc("""Swap seven. Instead of comparing yourself with people online, compare yourself with your own past. Are
you better off than you were a year ago? Do you have more saved, less debt, a clearer plan? That's the only
comparison that matters, and it's one you can actually win. Swap eight. Instead of waiting for the perfect
moment, start with the smallest possible step today.""",
   "Person climbing stairs", "COMPARE WITH YOUR PAST SELF")

# ---------------- Plan ----------------
ch("Your 4 week reset")
sc("""Here's a simple four week reset. Week one, look. Track every purchase, list every payment and every
subscription, and check your savings rate. Week two, cut. Cancel what you don't use, call to remove fees,
and ask for one lower rate.""",
   "Calendar on wall", "WEEKS 1 AND 2")
sc("""Week three, automate. Set up autopay for bills, an automatic transfer to savings the day after payday,
and make sure you're getting the full employer match. Week four, aim. Write your three goals with numbers
and dates, and share them with one person you trust. Four weeks. That's all it takes to start turning
these habits around.""",
   "Checklist with checkmarks", "WEEKS 3 AND 4")

# ---------------- By age ----------------
ch("Where to start at your age")
sc("""Where you start depends a bit on your stage of life. In your twenties, the most valuable habits are
the systems. Automatic saving, getting the full employer match, and avoiding high interest debt. Time is
your biggest asset, so even small amounts invested early can grow a lot over the decades ahead.""",
   "Young adults graduating", "IN YOUR 20s")
sc("""In your thirties and forties, life gets expensive. Kids, housing, cars, maybe caring for parents. This
is when lifestyle inflation and monthly payments do the most damage. Focus on keeping fixed costs under
control and raising your savings rate every time your income goes up.""",
   "Family with kids at home", "IN YOUR 30s AND 40s")
sc("""In your fifties and beyond, the focus shifts to catching up and protecting what you've built. Many
retirement accounts allow extra catch up contributions after fifty, so check the current IRS limits. And
the psychology habits matter more than ever, especially avoiding panic and not believing it's too late.""",
   "Older couple reviewing documents", "IN YOUR 50s AND BEYOND")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. Which habit should I fix first? Start with the most expensive one. For most people,
that's high interest credit card debt. Second, start an emergency fund so new surprises don't become new
debt. Everything else gets easier after those two.""",
   "Question mark sign", "WHICH FIRST?")
sc("""Question two. What if my income really is too low? Then the focus shifts toward income, like skills,
certifications, a better paying job, or a side income, while keeping the basic systems in place. Even
saving a very small amount builds the habit that will matter when your income grows.""",
   "Person studying at night", "IF INCOME IS TOO LOW")
sc("""Question three. How long does it take to change a habit? Research on habit formation suggests it
varies a lot from person to person and from habit to habit, often taking weeks to months. That's why
automation is so powerful. An automatic transfer doesn't need to become a habit. It just happens.""",
   "Hourglass on table", "HOW LONG IT TAKES")
sc("""Question four. Should I use a budget app? If it helps, yes. But the best budget is the one you'll
actually use. For some people that's an app, for others a spreadsheet, for others a notebook. What matters
is looking at your numbers regularly.""",
   "Notebook and laptop budget", "APP OR NOTEBOOK?")

sc("""Question five. Is it bad to buy coffee every day? Not if it's a choice you've made on purpose and it
fits your plan. The coffee isn't the problem. Not knowing what you spend is the problem. If your bills are
paid, your emergency fund is growing and you're investing, enjoy the coffee. If not, it might be one of many
small leaks worth looking at.""",
   "Coffee cup on cafe table", "WHAT ABOUT COFFEE?")
sc("""Question six. What if my partner has these habits and I don't? Start with shared goals, not blame. Talk
about what you both want, then build systems together, like a joint savings transfer and a personal
allowance for each of you. Blame rarely changes behavior. A shared plan often does.""",
   "Couple holding hands walking", "IF YOUR PARTNER SPENDS")
sc("""Question seven. Do I need to cut all fun spending? No. Cutting everything usually backfires. Plan for
fun, give it a fixed amount, and spend it without guilt. The goal is a life you enjoy that also moves you
forward, not a life of constant denial that you eventually quit.""",
   "Friends laughing at concert", "KEEP SOME FUN")

# ---------------- Recap ----------------
ch("Recap: all 25")
sc("""Quick recap. Angle one, the numbers. Not tracking spending, carrying a balance, paying bank fees,
thinking in monthly payments, ignoring subscriptions, eating out by default, leaving savings at zero
interest, paying late, and always buying new.""",
   "Checklist on clipboard", "THE NUMBERS: 1 TO 9")
sc("""Angle two, the psychology. Treating windfalls as fun money, constant rewards, keeping up with friends,
living only for today, avoiding your accounts, believing it's too late, believing more income will fix it,
and believing wealth is for other people.""",
   "Person thinking at window", "THE PSYCHOLOGY: 10 TO 17")
sc("""Angle three, the playbook. No emergency fund, saving what's left over, skipping the match, never
investing, no written goals, never negotiating, skipping protection, and doing it all alone.""",
   "Notebook with plan", "THE PLAYBOOK: 18 TO 25")

# ---------------- Close ----------------
ch("What to do next")
pr("""Here's what I want you to remember. Being broke is rarely about one big failure. It's usually a
set of quiet habits, and quiet habits can be replaced with quiet systems. You don't need a bigger income
to start, and you don't need to be perfect. You just need to be a little better than last month, every
month. You don't need to fix all twenty five. Pick one from each angle and start this week. If you want the
full step by step plan, it's in my playbook, linked in the description. And tell me in the comments which
habit you're breaking first. I'm Ryan Rover. See you in the next one.""")

save("video22", "25 Habits That Keep People Broke (Without Them Noticing)", [
    "Federal Reserve, Economic Well-Being of U.S. Households in 2024 (SHED): 63% would cover a $400 emergency expense with cash or its equivalent",
    "Federal Reserve, G.19 Consumer Credit: interest rate on credit card accounts assessed interest (above 20%)",
    "Consumer Financial Protection Bureau, research on overdraft and NSF fee revenue",
    "Edmunds, average new-vehicle monthly payment (above $700 in recent years)",
    "US Bureau of Labor Statistics, Consumer Expenditure Survey (food away from home)",
    "IRS filing season statistics (average federal refund around $3,000)",
    "Richard Thaler, mental accounting; Daniel Kahneman, behavioral economics",
    "Thomas J. Stanley and William D. Danko, The Millionaire Next Door (first-generation wealth)",
    "Growth examples: monthly compounding at 7% average yearly return (illustration, not a promise)",
], "25 habits that keep people broke, from 3 angles: numbers, psychology, playbook")
