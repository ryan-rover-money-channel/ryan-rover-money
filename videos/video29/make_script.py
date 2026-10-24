import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

body_hook = None  # set right before item() to start a Short at its first explained scene

def item(label, n, title, sub, card_text, body, example, fix, q1, c1, q2, c2, q3, c3):
    ch(f"{label} {n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"{label.upper()} {n}")
    global body_hook
    if body_hook:
        short(body_hook); body_hook = None
    sc(body, q1, c1)
    sc(example, q2, c2)
    sc(fix, q3, c3)

def good(*a): item("Habit", *a)
def bad(*a): item("Trap", *a)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Frugal living has a branding problem. Some people hear frugal and picture someone reusing
tea bags, arguing over a two dollar coupon, and never having any fun. Other people treat frugality like a magic
formula for getting rich. The truth is somewhere in the middle. Some frugal habits genuinely build wealth. Others
waste your time, your health, or even your money. Today, twenty frugal habits that actually make you rich, and ten
that don't.""")
short("Some frugal habits make you rich. Others just make you miserable.")
card("""Here's the idea that separates the two. Imagine the same five hundred dollars a month saved. If it comes from
big decisions like housing and cars, it takes almost no daily effort. If it comes from tiny cuts, it can take dozens
of painful decisions every week. Same money, very different life.""",
     {"type": "compare", "left": {"label": "Big wins", "big": "A few decisions", "sub": "car, housing, debt, fees"},
      "right": {"label": "Tiny cuts", "big": "Hundreds of decisions", "sub": "coupons, coffee, small stuff"},
      "note": "Same savings, very different effort"})
sc("""That's the key to smart frugality. It's not about spending as little as possible on everything. It's about
spending less on things that don't matter to you, so you can spend more on things that do, and invest the rest.
Researchers who study wealth, like Thomas Stanley, found that many millionaires were frugal, but in a targeted way.
They cut hard on cars, houses and status items, and still spent on things they valued, like education and family.""",
   "Family enjoying picnic", "TARGETED FRUGALITY")
sc("""We'll go through these thirty habits from three angles. First, the numbers. Ten frugal habits with math so
strong they can change your net worth by hundreds of thousands of dollars. Second, the psychology. Ten frugal habits
that feel smart but backfire, and why our brains love them anyway. And third, the playbook. Ten habits that turn
frugality into an automatic system, so you can stop thinking about money all the time.""",
   "Three paths in forest", "THREE ANGLES")
pr("""Let's start with the numbers. Habit number one is the single biggest frugal move most families can make.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our sources. Car costs come from AAA, Kelley Blue Book and Edmunds. Food spending from the Bureau of Labor
Statistics. Credit card rates from the Federal Reserve. Millionaire habits from Thomas Stanley's research. Health
spending research from the Centers for Disease Control and Prevention. Growth examples use a stated seven percent
average yearly return, an illustration, not a promise. This is education, not financial advice.""",
   "Research documents on desk", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Ten frugal habits that genuinely make people rich, because the math is so big.""")

good(1, "Drive reliable used cars", "the biggest frugal win",
"""Habit number one. Buy reliable used cars and drive them for a long time.""",
"""AAA estimates that owning and operating a new car costs more than twelve thousand dollars a year on average,
including depreciation, insurance, fuel, maintenance and financing. Kelley Blue Book reported average new car prices
above fifty thousand dollars. A reliable used car, kept for ten years, can cut those costs dramatically.""",
"""Stanley found that many millionaires bought used cars and kept them for years. Over a lifetime, the difference
between a new car every few years and a used car kept long can reach hundreds of thousands of dollars, once you count
what that money could have earned invested.""",
"""Make it yours. Next time, buy a car two or three years old with a strong reliability record. Keep it until repairs
are frequent and expensive. When the loan ends, keep paying yourself the payment.""",
"Reliable used sedan", "THE BIGGEST WIN",
"Car dealership new cars", "$12,000+ A YEAR",
"Odometer high mileage", "KEEP IT LONG")

good(2, "Right size your home", "less house, more wealth",
"""Habit number two. Live in a home that fits your needs, not your maximum approval.""",
"""Housing is the biggest expense for most American households, according to Bureau of Labor Statistics data. A
smaller or cheaper home means a lower mortgage, lower property taxes, lower insurance, lower utilities and lower
maintenance. It's savings on five bills at once, every single month, for as long as you live there.""",
"""Buying a home a hundred thousand dollars cheaper than your maximum approval can save hundreds of dollars a month.
Invested over decades, that difference can become a fortune. Many quiet millionaires live in homes far below what they
could afford.""",
"""Make it yours. Decide your housing budget before talking to a lender. Aim to keep total housing costs around thirty
percent of income or less. Think about the life you want, not the house you're approved for.""",
"Modest family home", "LESS HOUSE, MORE WEALTH",
"Mortgage paperwork", "FIVE BILLS AT ONCE",
"Family in cozy living room", "THE LIFE YOU WANT")

good(3, "Cook most meals at home", "the weekly win",
"""Habit number three. Cook most meals at home.""",
"""Food away from home is one of the largest budget categories for American households, according to the Bureau of
Labor Statistics. A home cooked meal often costs a fraction of the same meal from a restaurant or delivery app,
especially once fees and tips are added.""",
"""Replacing even three restaurant or delivery meals a week can save a typical family well over a thousand dollars a
year. And cooking at home is often healthier, which saves money in a second way over time.""",
"""Make it yours. Plan four dinners each weekend and shop with a list. Cook double portions for lunches. Keep a few
fast backup meals in the freezer for tired nights.""",
"Family cooking dinner together", "COOK AT HOME",
"Delivery receipt with fees", "FEES AND TIPS ADD UP",
"Meal prep containers", "DOUBLE PORTIONS")

good(4, "Kill high interest debt", "a guaranteed return",
"""Habit number four. Pay off high interest debt aggressively.""",
"""The Federal Reserve reports average credit card rates above twenty percent for accounts that pay interest. Paying
off a card at twenty two percent is like earning a guaranteed twenty two percent return. No investment reliably offers
that.""",
"""On a ten thousand dollar balance, that's around two thousand two hundred dollars a year in interest. Eliminating it
frees up that money every year, forever. That's frugality with real teeth.""",
"""Make it yours. List debts by interest rate. Pay minimums on all, and every extra dollar to the highest rate. Stop
adding new charges to cards with balances.""",
"Credit card statement", "20%+ INTEREST",
"Calculator with debt numbers", "$2,200 A YEAR",
"Debt payoff list", "HIGHEST RATE FIRST")

good(5, "Pay low investment fees", "the quiet fortune",
"""Habit number five. Keep investment fees low.""",
"""A one percent yearly fee sounds small. But on a growing retirement account, it can cost tens of thousands of
dollars or more over a career, because you lose the fee and all the growth it would have produced. Many broad index
funds charge a small fraction of that.""",
"""This is one of the few frugal habits that takes about an hour once and pays off for decades. You don't have to
think about it every day. You just choose low cost funds and let time work.""",
"""Make it yours. Look up the expense ratio of every fund in your retirement accounts. Compare with low cost
alternatives in the same plan. If you use an advisor, ask exactly what you pay in dollars.""",
"Investment statement fees", "THE QUIET 1%",
"Index fund chart growing", "ONE HOUR, DECADES OF PAYOFF",
"Fund expense ratio on screen", "CHECK THE EXPENSE RATIO")

good(6, "Shop insurance every year", "loyalty costs money",
"""Habit number six. Shop for insurance once a year.""",
"""Car and home insurance premiums have risen sharply in recent years. Many people renew automatically for years
without comparing. Getting a few quotes once a year can often save hundreds of dollars for the same coverage.""",
"""It's an ideal frugal habit. One hour a year, no change in lifestyle, and often a meaningful saving. Raising your
deductible, if you have a solid emergency fund, can lower premiums further.""",
"""Make it yours. Put an annual reminder in your calendar a month before renewal. Get at least three quotes for the
same coverage. Ask about bundling and discounts.""",
"Insurance documents", "PREMIUMS RISING",
"Comparing quotes on laptop", "ONE HOUR A YEAR",
"Calendar reminder renewal", "THREE QUOTES")

good(7, "Cancel what you don't use", "the subscription sweep",
"""Habit number seven. Cancel subscriptions you don't use.""",
"""Streaming, apps, memberships and boxes add up. Surveys regularly find people underestimate what they spend on
subscriptions. Each one renews automatically, so the cost continues long after the interest fades.""",
"""A sweep every few months can easily free up fifty to a hundred dollars a month for many households, with no real
loss. You can always resubscribe when there's something you really want to watch or use.""",
"""Make it yours. Search your statements for every repeating charge. Cancel anything you haven't used in the last
month. Rotate streaming services instead of keeping them all.""",
"Streaming apps on TV", "THE QUIET LEAK",
"Bank statement repeating charges", "SWEEP EVERY FEW MONTHS",
"Canceling subscription on laptop", "ROTATE, DON'T STACK")

good(8, "Take the full employer match", "free money",
"""Habit number eight. Always take the full employer match.""",
"""Many employers match part of what you put into a retirement plan. If your employer matches fifty cents on the
dollar up to six percent of your salary, contributing less than six percent leaves free money on the table.""",
"""It's technically saving, not frugality. But it's the most frugal thing you can do, because it's the highest return
on any dollar you'll ever save. Skipping it is like declining part of your salary.""",
"""Make it yours. Check your benefits portal or ask HR exactly how your match works. Make sure your contribution is at
least high enough to get all of it.""",
"Office workers benefits meeting", "FREE MONEY",
"Retirement plan statement", "DON'T DECLINE YOUR SALARY",
"HR benefits portal", "GET ALL OF IT")

good(9, "Keep cash in a high yield account", "make savings earn",
"""Habit number nine. Keep your emergency fund in a high yield savings account.""",
"""Many traditional savings accounts pay a tiny interest rate. Online high yield savings accounts, insured by the
FDIC, have offered rates many times higher in recent years. On a ten thousand dollar emergency fund, that difference
can be hundreds of dollars a year.""",
"""It's a fifteen minute change that pays you every month, with no extra risk if you stay within FDIC insurance
limits. Frugality isn't only about spending less. It's also about making your money work harder.""",
"""Make it yours. Check your current savings rate. Compare with a few FDIC insured high yield accounts. Move your
emergency fund if the gap is large.""",
"Piggy bank on table", "MAKE SAVINGS EARN",
"Online banking app rates", "HUNDREDS A YEAR",
"FDIC insured sign", "15 MINUTES TO SWITCH")

good(10, "Buy quality for daily use", "buy once, cry once",
"""Habit number ten. Pay for quality on things you use every day.""",
"""Smart frugality isn't always buying the cheapest. For items you use constantly, like a mattress, work shoes, or a
good winter coat, quality can be cheaper over time. Cheap versions that wear out quickly cost more in the long run.""",
"""The writer Terry Pratchett described this as the boots theory of poverty. A cheap pair of boots that falls apart
every year ends up costing more than a well made pair that lasts a decade. The key word is daily.""",
"""Make it yours. List the five things you use most. For those, research quality and durability. For things you use
rarely, cheap is fine.""",
"Quality leather boots", "BUY ONCE, CRY ONCE",
"Worn out cheap shoes", "THE BOOTS THEORY",
"Hardware store quality tools", "QUALITY FOR DAILY USE")

short("Ten frugal habits that could be worth almost half a million dollars.")
card("""Here's what the first ten habits can add up to. If they free up six hundred dollars a month, invested at a seven
percent average yearly return, after twenty five years that's roughly four hundred eighty six thousand dollars.""",
     {"type": "growth", "monthly": 600, "rate": 0.07, "years": 25})

pr("""That's angle one. Ten habits, almost all of them about big decisions you make once or a few times a year. Now
angle two. The psychology. Ten frugal habits that feel smart, but quietly cost you.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
sc("""Why do people fall for bad frugal habits? Because saving money feels good, even when the saving is tiny or the
cost is hidden. Our brains love a visible win, like a coupon or a sale sticker, and ignore invisible costs, like our time,
our health, or the money we lose later. These next ten are frugal traps.""",
   "Coupons and sale stickers", "THE FRUGAL TRAPS")

body_hook = "Driving across town to save two dollars? Do the math."
bad(1, "Driving far to save a little", "your time and gas count",
"""Trap number one. Driving across town to save a few dollars.""",
"""Gas, wear on your car, and your time all cost money. The IRS standard mileage rate, which estimates the full cost of
driving, has been around seventy cents a mile in recent years. A twenty mile round trip to save five dollars can easily
cost more than you save.""",
"""The brain sees the five dollar saving clearly, and the driving cost not at all. That's why this trap is so common,
and why so many people feel frugal while actually losing money.""",
"""Avoid it. Before going out of your way for a deal, multiply the extra miles by roughly the IRS rate, and add the value
of your time. Only go if the saving is clearly bigger.""",
"Car driving on highway", "THE HIDDEN DRIVE COST",
"Gas pump price", "70 CENTS A MILE",
"Map with route", "DO THE MATH FIRST")

bad(2, "Bulk buying you waste", "the warehouse trap",
"""Trap number two. Buying in bulk things you end up throwing away.""",
"""Warehouse clubs can save money on things you use reliably, like paper towels or staples. But the US Department of
Agriculture estimates thirty to forty percent of the food supply is wasted, and bulk produce that spoils is a common
culprit.""",
"""Bulk packs also make people use more. A giant bag of snacks disappears faster than a small one. The unit price
looks lower, but the total spending goes up.""",
"""Avoid it. Buy bulk only for nonperishables you use consistently. For food, buy what you'll realistically eat before
it spoils.""",
"Warehouse store shelves", "THE BULK TRAP",
"Spoiled produce in fridge", "30 TO 40% WASTED",
"Pantry staples organized", "BULK FOR STAPLES ONLY")

bad(3, "Skipping preventive health care", "the most expensive saving",
"""Trap number three. Skipping checkups and dental cleanings to save money.""",
"""Preventive care often costs far less than treating problems later. A dental cleaning is much cheaper than a root
canal. The Centers for Disease Control and Prevention notes that many chronic diseases can be prevented or managed better
when caught early.""",
"""Many insurance plans cover certain preventive services at no extra cost under the Affordable Care Act. Skipping them
saves nothing and can cost thousands later.""",
"""Avoid it. Check which preventive services your insurance covers at no cost, and schedule them. Health is the asset
that protects every other asset.""",
"Dentist office cleaning", "PREVENTION IS CHEAPER",
"Doctor checkup", "CATCH IT EARLY",
"Calendar with appointments", "SCHEDULE THEM")

bad(4, "Cheap tires and brakes", "never cut safety",
"""Trap number four. Saving money on safety equipment.""",
"""Tires, brakes, car seats, smoke detectors, helmets. These are places where the cheapest option, or delaying
replacement, can be dangerous. Worn tires take longer to stop, especially on wet roads, according to safety
organizations.""",
"""An accident costs far more than good tires, in money and in health. Frugality should never put you or your family
at risk.""",
"""Avoid it. Spend appropriately on safety. Replace tires when they're worn, keep brakes maintained, and buy safety
gear that meets current standards.""",
"Car tire tread close up", "NEVER CUT SAFETY",
"Car brakes repair", "STOPPING DISTANCE",
"Child car seat installed", "SAFETY FIRST")

bad(5, "Cheap stuff that breaks", "false economy",
"""Trap number five. Buying the cheapest version every time.""",
"""Remember the boots theory. Cheap items that break quickly have to be replaced, again and again. The total cost over
years can far exceed a better version bought once.""",
"""This trap is common with tools, appliances, furniture and clothing. The low price feels like a win at checkout, but
the replacement costs are spread out and easy to ignore.""",
"""Avoid it. For anything you'll use often or for years, check reviews for durability and compare cost per year of use,
not just the price.""",
"Broken cheap appliance", "FALSE ECONOMY",
"Trash with broken items", "BUY, BREAK, REPEAT",
"Product reviews on laptop", "COST PER YEAR")

pr("""Quick break. If you're enjoying this, please subscribe to Ryan Rover Money. It's free and it helps the channel
grow. Okay, frugal trap number six. This one hurts more than your wallet.""")

bad(6, "Cutting all social spending", "loneliness is expensive too",
"""Trap number six. Cutting all spending on friends and fun.""",
"""Some people get so focused on saving that they stop seeing friends, skip every event, and cut every pleasure.
Research has linked loneliness and social isolation to worse health outcomes. And extreme budgets often snap back into
big spending binges.""",
"""Relationships are also a financial asset. Friends help with jobs, opportunities and support in hard times. Cutting
them off to save money is a bad trade.""",
"""Avoid it. Budget for social life on purpose. Suggest cheaper plans, like potlucks or hikes, but keep showing up.""",
"Friends laughing at dinner", "LONELINESS COSTS TOO",
"Person alone at home", "THE SNAP BACK",
"Friends at potluck", "CHEAPER PLANS, STILL TOGETHER")

bad(7, "Extreme couponing", "time is money",
"""Trap number seven. Spending hours to save a few dollars.""",
"""Extreme couponing can take many hours a week. If those hours save fifty dollars, that might be less than you'd earn
in the same time at work, a side job, or by building a skill that raises your income.""",
"""Coupons also push people to buy things they don't need, just because there's a deal. The saving is real, but so is
the extra spending.""",
"""Avoid it. Use coupons and cash back apps for things you already buy, when it's quick. Spend most of your energy on
the big wins from angle one.""",
"Stack of coupons", "HOURS FOR DOLLARS",
"Overflowing shopping cart", "BUYING BECAUSE OF A DEAL",
"Cash back app on phone", "QUICK WINS ONLY")

bad(8, "Skipping insurance", "one disaster away",
"""Trap number eight. Dropping important insurance to save money.""",
"""Health, renters, homeowners, car liability, disability and, if others depend on you, life insurance. Skipping
these saves money every month, until the one month something goes wrong. Medical bills are a leading cause of debt for
many Americans.""",
"""The frugal move is to insure against disasters you couldn't afford, while self insuring small losses with an
emergency fund. That's very different from having no insurance at all.""",
"""Avoid it. Keep coverage for catastrophes. Save money by raising deductibles and shopping around, not by dropping
coverage completely.""",
"Hospital hallway", "ONE DISASTER AWAY",
"House damaged by storm", "WHEN IT HAPPENS",
"Insurance comparison chart", "INSURE THE DISASTERS")

bad(9, "DIY everything", "some jobs need a pro",
"""Trap number nine. Doing every job yourself, even the risky ones.""",
"""Doing simple repairs yourself can save a lot. But electrical work, gas lines, major plumbing and roof work can be
dangerous, and mistakes can be very expensive to fix. Some work also needs permits.""",
"""A failed DIY project can cost more than hiring a professional in the first place. And your safety is worth more
than any saving.""",
"""Avoid it. Do simple, low risk jobs yourself. For anything dangerous or complex, get several quotes from licensed
professionals.""",
"Person doing electrical work", "SOME JOBS NEED A PRO",
"Water damage from leak", "EXPENSIVE MISTAKES",
"Contractor giving quote", "GET QUOTES")

bad(10, "Buying because it's on sale", "spending isn't saving",
"""Trap number ten. Buying things because they're on sale.""",
"""Saving forty percent on something you didn't need isn't saving. It's spending sixty percent. Retailers know that
sale signs trigger a feeling of winning, and they use it to move inventory.""",
"""Sales, flash deals and limited time offers create urgency. Under that pressure, people buy things they'd never buy at
full price, and many of them go unused.""",
"""Avoid it. Ask: would I buy this at full price? If not, skip it. Keep a list of things you actually need, and only buy
those on sale.""",
"Sale sign in store window", "SPENDING ISN'T SAVING",
"Unused items with tags", "BOUGHT BUT UNUSED",
"Shopping list on phone", "NEEDS LIST ONLY")

ch("Why bad frugality feels so good")
sc("""Why do the bad habits feel so satisfying? Because they give you a visible, immediate win. A coupon, a sale price, a
bigger bulk package. Your brain gets a little reward. Meanwhile, the costs are hidden, delayed or spread out. Your time,
gas, health and future replacement costs.""",
   "Brain reward concept", "VISIBLE WINS")
sc("""Good frugality often feels less exciting. Buying a used car or shopping insurance once a year doesn't give you a
weekly rush. But the savings are huge and permanent. The trick is learning to value the big, boring wins over the small,
exciting ones.""",
   "Boring paperwork on desk", "BIG BORING WINS")
sc("""Here's a simple test. For any frugal habit, ask: how much does this save per year, and how many hours does it
take? If the answer is a lot of money for a little time, keep it. If it's a little money for a lot of time, or any risk
to health or safety, drop it.""",
   "Stopwatch and coins", "THE MONEY PER HOUR TEST")

pr("""That's angle two. Ten frugal traps. Now angle three. The playbook. Ten habits that make good frugality automatic,
so you don't need willpower every day.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
sc("""The best frugal people don't think about money constantly. They built a few systems once, and those systems do the
work. This last group of habits is about building that system.""",
   "Gears working together", "BUILD THE SYSTEM")

good(11, "Automate savings", "pay yourself first",
"""Habit number eleven. Automate your savings.""",
"""Set an automatic transfer to savings and investments for the day after payday. Money you never see is money you
don't spend. Research on retirement plans shows automatic enrollment greatly increases participation, because the default
does the work.""",
"""Automation turns frugality from a daily fight into a background process. You live on what's left, and adjust
naturally. Most people find that after a month or two, they don't even miss the money. Their spending quietly reshapes
itself around what's in checking, without a single painful decision.""",
"""Make it yours. Set up one automatic transfer this week. Start with five percent of take home pay, and increase by one
percent every few months.""",
"Automatic transfer on phone", "PAY YOURSELF FIRST",
"Paycheck splitting", "MONEY YOU NEVER SEE",
"Calendar with increases", "RAISE IT OVER TIME")

good(12, "Use a waiting rule", "24 hours, 30 days",
"""Habit number twelve. Wait before you buy.""",
"""A simple waiting rule stops most impulse purchases. Twenty four hours for small non essentials, thirty days for big
ones. Most wants fade. The ones that last are probably worth buying.""",
"""It works because it gives your careful, slow thinking time to catch up with your fast, emotional thinking. A day
later, you're no longer in the store, the countdown timer is gone, and the excitement has cooled. What's left is a calm
question. Do I actually want this? Surprisingly often, the honest answer is no.""",
"""Make it yours. Keep a wish list on your phone. Add things instead of buying them. Check the list after the waiting
period.""",
"Hourglass timer", "WAIT BEFORE YOU BUY",
"Online cart saved for later", "WANTS FADE",
"Wish list on phone", "ADD, DON'T BUY")

good(13, "Think in cost per use", "value over price",
"""Habit number thirteen. Judge purchases by cost per use.""",
"""Divide the price by how many times you'll realistically use something. A hundred dollar jacket worn two hundred times
is fifty cents a wear. A forty dollar dress worn once is forty dollars.""",
"""This one habit protects you from both cheap junk and expensive things you'll never use. It also helps you spend
with confidence. When you know something will be used hundreds of times, paying more for quality stops feeling
extravagant and starts feeling smart.""",
"""Make it yours. Before any purchase over fifty dollars, estimate the number of uses and do the division.""",
"Jacket on hanger", "COST PER USE",
"Calculator and price tag", "VALUE OVER PRICE",
"Closet organized", "DO THE DIVISION")

good(14, "Spend on what you love", "conscious spending",
"""Habit number fourteen. Spend freely on what you love, cut hard on what you don't.""",
"""Personal finance author Ramit Sethi calls this conscious spending. You decide what you value most and spend on it
without guilt, while cutting ruthlessly on everything else.""",
"""This makes frugality sustainable, because you're not depriving yourself of what matters. You're just removing the
spending that doesn't. One person might spend generously on travel and cook every meal at home. Another might love
restaurants and drive a twelve year old car. Both are frugal, in their own way.""",
"""Make it yours. Write down three things you love spending on and three you don't care about. Cut the second list.""",
"Person enjoying hobby", "SPEND ON WHAT YOU LOVE",
"Two lists in notebook", "CUT THE REST",
"Happy person traveling", "NO GUILT")

good(15, "Use sinking funds", "no more surprise bills",
"""Habit number fifteen. Save ahead for irregular expenses.""",
"""Car repairs, holidays, annual subscriptions, insurance premiums. These aren't surprises. They just don't happen
every month. Sinking funds are separate savings for each one.""",
"""When the bill arrives, the money is already there. No credit card, no stress, no interest. Sinking funds also make
your monthly budget honest. Instead of pretending expenses are lower than they really are, you spread the true yearly
cost across every month.""",
"""Make it yours. List your irregular expenses for a year. Divide each by twelve. Save that amount monthly in separate
accounts or labeled savings buckets.""",
"Labeled savings jars", "SINKING FUNDS",
"Car repair invoice", "NOT REALLY SURPRISES",
"Savings buckets in bank app", "DIVIDE BY TWELVE")

body_hook = "Do this once a year and save hundreds without changing your life."
good(16, "Do a yearly bill audit", "one afternoon, big savings",
"""Habit number sixteen. Audit your bills once a year.""",
"""Phone, internet, insurance, subscriptions, bank fees. Once a year, review every recurring bill. Call providers and
ask for better rates. Many will offer discounts to keep you.""",
"""One afternoon can often save hundreds of dollars a year. It's one of the best returns on time in personal finance.
Many companies have retention departments with discounts reserved for customers who ask. Just saying I'm thinking
about switching, can you do anything on my rate, is often enough to start the conversation.""",
"""Make it yours. Pick one afternoon each year. Make a list of every recurring bill, and call the top five.""",
"Bills spread on table", "THE YEARLY AUDIT",
"Person on phone negotiating", "ASK FOR BETTER RATES",
"Checklist of bills", "CALL THE TOP FIVE")

good(17, "Plan your meals", "the grocery system",
"""Habit number seventeen. Plan meals weekly.""",
"""Meal planning reduces food waste, cuts takeout, and makes grocery trips faster. It turns one of the biggest budget
categories into a simple routine.""",
"""It also beats decision fatigue. When dinner is already decided, you're far less likely to order delivery on a tired
night. And because you buy only what the plan needs, less food goes bad in the back of the fridge. It's one habit that
attacks three costs at once, takeout, waste and impulse buys at the store.""",
"""Make it yours. Every weekend, pick four dinners and two lunches. Shop with a list. Leave room for leftovers night.""",
"Weekly meal plan on fridge", "THE GROCERY SYSTEM",
"Grocery shopping with list", "FASTER, CHEAPER TRIPS",
"Leftovers in containers", "LEFTOVERS NIGHT")

good(18, "Use free resources", "the library is magic",
"""Habit number eighteen. Use what's already free.""",
"""Public libraries offer books, audiobooks, movies, classes and often museum passes, for free. Parks, community events
and free online courses add even more. Many people pay for things they could get free.""",
"""Using free resources doesn't feel like sacrifice. It often opens up more options than paying for subscriptions.
Many libraries now lend e books, audiobooks, streaming movies and even tools, all through free apps. For a family that
reads and watches a lot, that alone can replace several paid subscriptions.""",
"""Make it yours. Get a library card and download your library's apps. Check your city's events calendar.""",
"Public library interior", "THE LIBRARY IS MAGIC",
"Family in public park", "FREE FUN",
"Library app on phone", "GET A CARD")

good(19, "Negotiate", "ask once, save for years",
"""Habit number nineteen. Negotiate the big stuff.""",
"""Salary, car prices, rent renewals, medical bills and large purchases are often negotiable. A single negotiation can
be worth more than months of small cuts.""",
"""Negotiating your salary is especially powerful, because future raises are often built on your current pay. A
few thousand dollars more at the start of a job can compound into tens of thousands over a career. It's frugality on the
income side, and it often takes a single conversation.""",
"""Make it yours. Before your next big purchase or review, research fair prices or salary ranges, and ask politely for
better terms.""",
"Business handshake", "ASK ONCE",
"Salary research on laptop", "RAISES BUILD ON IT",
"Person negotiating at desk", "ASK POLITELY")

good(20, "Invest the savings", "frugality's real purpose",
"""And habit number twenty. Invest what you save.""",
"""Frugality alone doesn't make you rich. It creates room. What makes you rich is investing that room for decades. Money
saved but left in a checking account usually gets spent.""",
"""Low cost index funds in tax advantaged accounts are a common choice. The goal is to turn frugal habits into assets
that grow. That's the real reason to be frugal. Not to have less, but to own more. Every dollar redirected from waste into
an investment becomes a small worker, earning for you while you sleep.""",
"""Make it yours. Every time a frugal habit frees up money, increase your automatic investment by the same amount the
same week.""",
"Investment growth chart", "FRUGALITY'S PURPOSE",
"Retirement account dashboard", "ROOM TO GROW",
"Increasing automatic investment", "SAME WEEK")

# ---------------- Happiness ----------------
ch("Frugality and happiness")
sc("""Does frugality make people happier or more miserable? Research suggests it depends on how you do it. In their book
Happy Money, psychologists Elizabeth Dunn and Michael Norton describe studies showing that experiences, time with others,
and spending on other people tend to bring more lasting happiness than buying more stuff. That fits perfectly with smart
frugality. Cut the stuff, keep the experiences.""",
   "Friends laughing on a trip", "CUT THE STUFF, KEEP THE EXPERIENCES")
sc("""Another study, led by Ashley Whillans and published in the Proceedings of the National Academy of Sciences, found
that people who spent money to buy themselves time, for example by paying for help with a disliked chore, reported greater
life satisfaction. So the smartest frugal people don't refuse to spend on everything. Sometimes paying to save time is
exactly the right call.""",
   "Person relaxing with free time", "BUYING TIME")
sc("""And financial security itself reduces stress. Having an emergency fund, no high interest debt and a growing
investment account gives a kind of peace that no purchase can match. That's the real reward of frugality done right.
Not a bigger pile of coupons, but a calmer mind.""",
   "Calm lake at sunrise", "A CALMER MIND")

# ---------------- Story ----------------
ch("Two frugal people")
pr("""Let me show you the difference between good and bad frugality with two people.""")
short("Two frugal people. Only one gets rich. Here's why.")
sc("""Pat is frugal in all the wrong ways. Pat drives across town for cheap gas, clips coupons for hours every week,
buys the cheapest everything, skips the dentist, and never goes out with friends. But Pat also has a new car on a seven
year loan, and lives in a house that eats forty percent of the household income. Pat is exhausted, lonely, and still
not getting ahead.""",
   "Stressed person with coupons", "PAT: FRUGAL THE WRONG WAY")
sc("""Chris is frugal in the right ways. Chris drives a reliable used car, lives in a right sized home, paid off high
interest debt, takes the full employer match, and automates investing. Chris still eats out with friends, travels once
a year, and doesn't think about coupons at all.""",
   "Relaxed person with friends", "CHRIS: FRUGAL THE RIGHT WAY")
sc("""After ten years, Chris has far more wealth, and a much happier life. Pat worked harder at frugality, but on the
wrong things. That's the lesson of this whole video. Frugality is about aim, not effort. Point your frugal energy at the few
decisions that move thousands of dollars, and you can stop worrying about the ones that move pennies.""",
   "Archery target bullseye", "AIM, NOT EFFORT")

# ---------------- By income ----------------
ch("Frugality at every income level")
sc("""Frugality looks different depending on your income. If money is very tight, the biggest wins are usually avoiding
fees and high interest debt, using free resources, and building a small emergency buffer so surprises don't become new
debt. At low incomes, small amounts matter a lot, and the money per hour test can favor smaller savings too.""",
   "Person counting money carefully", "WHEN MONEY IS TIGHT")
sc("""At middle incomes, cars and housing are usually the biggest levers. A smarter car and a right sized home can free
up hundreds of dollars a month. Combined with automatic investing and the full employer match, this is where many quiet
millionaires are made, over twenty or thirty years.""",
   "Middle class family home", "MIDDLE INCOMES")
sc("""At high incomes, the danger is lifestyle inflation. Spending rises with every raise, and many high earners live
paycheck to paycheck. For them, frugality means keeping fixed costs well below what they could afford, saving a large
share of every raise, and keeping investment fees and taxes low. The habits are the same. The scale is bigger.""",
   "High rise apartment city view", "HIGH INCOMES")

# ---------------- First month ----------------
ch("Your first frugal month")
sc("""Here's a simple plan for your first month. Week one, check your big three. What do your housing, car and food really
cost each month? Write the numbers down. Week two, do the quick wins. Cancel unused subscriptions, move your emergency
fund to a high yield account, and confirm you're getting the full employer match.""",
   "Calendar with week one circled", "WEEKS 1 AND 2")
sc("""Week three, drop one frugal trap. Stop driving across town for small deals, or stop buying things just because
they're on sale. Week four, automate. Set up an automatic transfer for whatever money you've freed up, straight into
savings or investments, so it doesn't drift back into spending. In thirty days, you'll have a new system, and a number
that shows it working.""",
   "Automatic savings notification", "WEEKS 3 AND 4")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. Is frugality enough to get rich? Usually not on its own. Most people also need to grow their income
over time and invest steadily. Frugality creates the gap between income and spending, and investing turns that gap into
wealth.""",
   "Two puzzle pieces fitting", "IS FRUGALITY ENOUGH?")
sc("""Question two. How do I stay frugal without feeling deprived? Focus on the big wins, automate them, and keep
spending on what you love. When the big decisions are right, you can relax about the small stuff.""",
   "Person relaxing with coffee", "WITHOUT DEPRIVATION")
sc("""Question three. What's the first habit to start with? If you have high interest debt, start there. If not, check
your car and housing costs, then automate savings and get the full employer match.""",
   "Starting line on track", "WHERE TO START")
sc("""Question four. Is it worth buying organic or premium food? That's a personal choice and part of conscious spending.
If it matters to you, spend there, and cut somewhere else. Frugality doesn't mean buying the cheapest food. It means
choosing on purpose and wasting less of what you buy.""",
   "Fresh vegetables at market", "PREMIUM FOOD?")
sc("""Question five. My partner thinks frugal means cheap. How do I explain it? Show the difference between the big
wins and the small cuts. Most people are happy to drive a used car if it means a vacation every year and less stress.
Frugality done right should make your life feel better, not smaller. Start with one shared goal and let the results
speak.""",
   "Couple talking on couch", "FRUGAL ISN'T CHEAP")
sc("""Question six. How do I know if a frugal habit is worth it? Use the two questions from this video. First, how much
does it save in a year, compared with the time it takes? Second, does it put my health, safety or relationships at risk? If
it saves real money for little time and no risk, keep it. If not, let it go and focus on the big wins.""",
   "Scale balancing time and money", "IS IT WORTH IT?")

# ---------------- Recap ----------------
ch("Recap")
sc("""Quick recap. Angle one, the numbers. Drive reliable used cars, right size your home, cook at home, kill high
interest debt, pay low fees, shop insurance, cancel unused subscriptions, take the match, use high yield savings, and buy
quality for daily use.""",
   "Checklist on clipboard", "THE NUMBERS: 10 HABITS")
sc("""Angle two, the psychology. Ten traps. Driving far to save a little, wasteful bulk buying, skipping preventive care,
cheap safety gear, cheap stuff that breaks, cutting all social life, extreme couponing, skipping insurance, risky DIY, and
buying because it's on sale.""",
   "Person thinking at window", "THE PSYCHOLOGY: 10 TRAPS")
sc("""Angle three, the playbook. Automate savings, use a waiting rule, think in cost per use, spend on what you love, use
sinking funds, audit bills yearly, plan meals, use free resources, negotiate, and invest the savings.""",
   "Notebook with plan", "THE PLAYBOOK: 10 HABITS")

# ---------------- Close ----------------
ch("What to do next")
pr("""Remember Pat and Chris. Same effort, very different results, because one aimed at the big wins and the other
aimed at pennies. Frugality done right isn't about being cheap. It's about being free. Pick one habit from angle one, drop one trap
from angle two, and set up one system from angle three this month. If you want the full plan, it's in my playbook, linked
in the description. Tell me in the comments your favorite frugal habit. I'm Ryan Rover. See you in the next one.""")

save("video29", "20 Frugal Habits That Actually Make You Rich (And 10 That Don't)", [
    "AAA, Your Driving Costs (over $12,000 a year for a new vehicle); Kelley Blue Book average transaction price above $50,000",
    "US Bureau of Labor Statistics, Consumer Expenditure Survey (housing, food away from home)",
    "Federal Reserve, G.19 Consumer Credit (credit card rates above 20%)",
    "Thomas J. Stanley, The Millionaire Next Door (1996)",
    "IRS standard mileage rate (around 70 cents a mile in recent years)",
    "USDA, food loss and waste (30-40% of the US food supply); CDC, chronic disease prevention",
    "Madrian and Shea (2001), automatic enrollment; Ramit Sethi, conscious spending",
    "Dunn and Norton, Happy Money (2013); Whillans et al., Buying Time Promotes Happiness (PNAS, 2017)",
    "Growth example: monthly compounding at 7% average yearly return (illustration, not a promise)",
], "20 frugal habits that make you rich and 10 that don't, from 3 angles: numbers, psychology, playbook")
