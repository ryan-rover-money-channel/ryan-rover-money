import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

body_hook = None  # set right before item() to start a Short at its first explained scene

def item(n, title, sub, card_text, body, example, fix, q1, c1, q2, c2, q3, c3):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"WASTE {n}")
    global body_hook
    if body_hook:
        short(body_hook); body_hook = None
    sc(body, q1, c1)
    sc(example, q2, c2)
    sc(fix, q3, c3)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. The American middle class works harder than almost anyone. Two incomes, long hours,
kids, a mortgage. And yet, so many middle class families feel like they're running in place. They earn more
than their parents did, and somehow have less breathing room. Part of that is rising costs, no doubt. But
part of it is where the money goes. Today, twenty things the middle class wastes money on, and what to do
with that money instead.""")
short("The middle class is shrinking. Here's the proof.")
card("""Here's the squeeze in one number. According to the Pew Research Center, the share of American adults
living in middle income households fell from sixty one percent in nineteen seventy one to about fifty one
percent in twenty twenty three.""",
     {"type": "compare", "left": {"label": "1971", "big": "61%", "sub": "adults in middle-income households"},
      "right": {"label": "2023", "big": "51%", "sub": "adults in middle-income households"},
      "note": "Pew Research Center"})
sc("""Pew's research shows the middle class has been shrinking for decades, while costs like housing,
health care and college have climbed faster than many paychecks. That's real, and it's not your fault. But
here's the hopeful part. Inside a typical middle class budget, there's often a surprising amount of money
leaking into things that don't make life much better. Find those leaks, and you can create room to save,
invest and breathe, even in an expensive world.""",
   "Suburban neighborhood houses", "THE SQUEEZE")
sc("""We'll go through these twenty from three angles. First, the numbers. The big ticket items where the
math is brutal. Second, the psychology. The social pressure and emotions that push middle class families to
overspend. And third, the playbook. The quiet leaks in the system, from taxes to insurance, and exactly how to
plug them. By the end, you'll probably find at least a few hundred dollars a month you didn't know you had.""",
   "Three paths in a park", "THREE ANGLES")
pr("""Let's start with the numbers, and the biggest one is sitting in almost every driveway in America.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our sources. Middle class data comes from the Pew Research Center. Car prices and loans come from Kelley
Blue Book and Edmunds. Wedding costs come from The Knot's Real Weddings Study. Food waste comes from the US
Department of Agriculture. Home renovation returns come from the Cost versus Value report. Sports betting
data comes from the American Gaming Association. Growth examples use a stated seven percent average yearly
return, which is an illustration, not a promise. This is education, not financial advice.""",
   "Research papers on desk", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Seven big expenses where a single decision can cost or save tens of thousands
of dollars.""")

item(1, "New cars on long loans", "the driveway drain",
"""Waste number one. New cars on long loans.""",
"""Kelley Blue Book reported that the average price paid for a new vehicle passed fifty thousand dollars in
twenty twenty five. To make that affordable, many buyers stretch loans to six or seven years. Edmunds has
reported average new car payments above seven hundred dollars a month. For a two car household, that can
mean well over a thousand dollars a month going to vehicles that lose value every single year.""",
"""The real cost isn't just the payment. It's depreciation, higher insurance on newer cars, and the interest
on a long loan. And because long loans often leave you owing more than the car is worth, many people roll
negative equity into the next loan, starting the cycle over. It's one of the biggest reasons middle class
households struggle to save, and one of the least questioned.""",
"""The fix. Buy reliable used cars, ideally a few years old, and pay as much as possible in cash. Keep them
for many years. When a car loan ends, keep making the same payment into a savings account for your next car.
Over a lifetime, this one habit can be worth hundreds of thousands of dollars.""",
"New car dealership showroom", "$50,000 AVERAGE",
"Car loan paperwork", "THE LONG LOAN",
"Reliable used car", "BUY USED, KEEP LONG")

item(2, "More house than they need", "the bigger mortgage trap",
"""Waste number two. More house than they need.""",
"""Lenders often approve buyers for much more than they can comfortably afford. And a bigger house costs
more in every direction. A bigger mortgage, higher property taxes, higher insurance, higher utilities, more
furniture and more repairs. A common rule of thumb is to budget around one to two percent of a home's value
every year for maintenance alone.""",
"""When housing takes too large a share of income, families become house poor. Beautiful home, no savings.
The Department of Housing and Urban Development considers spending more than thirty percent of income on
housing a burden. Many middle class families go well beyond that in pursuit of the extra bedroom or the
better zip code.""",
"""The fix. Decide your budget before you talk to a lender, not after. Keep total housing costs around or
below thirty percent of gross income if you can. Remember, the house is a place to live, not a scoreboard.
The smaller house with savings in the bank is often the richer life.""",
"Large suburban house", "BIGGER EVERYTHING",
"Family stressed with bills at home", "HOUSE POOR",
"Cozy modest home", "DECIDE BEFORE THE LENDER")

item(3, "Credit card interest", "paying 20% for ordinary life",
"""Waste number three. Credit card interest.""",
"""The Federal Reserve reports that the average rate on credit card accounts that paid interest has been above
twenty percent in recent years. The Federal Reserve Bank of New York reported that total credit card balances
in America passed one trillion dollars. A lot of that is middle class families covering the gap between their
income and their life.""",
"""Interest is pure waste. You get nothing for it. On a ten thousand dollar balance at twenty two percent,
that's around two thousand two hundred dollars a year in interest. That's a vacation, a car repair fund, or a
year of retirement contributions for many people, handed to a bank.""",
"""The fix. Stop adding to the balance. Make a list of every card and attack the highest rate first with every
extra dollar. Call your issuer and ask for a lower rate. And once it's paid off, use cards only for purchases
you'll pay in full that month.""",
"Credit cards fanned out", "OVER $1 TRILLION",
"Interest charges on statement", "$2,200 A YEAR",
"Paid in full stamp", "PAY IN FULL")

body_hook = 'The average wedding now costs this much.'
item(4, "The very expensive wedding", "one day, years of debt",
"""Waste number four. The very expensive wedding.""",
"""According to The Knot's Real Weddings Study, the average cost of a wedding in the United States was
around thirty three thousand dollars in twenty twenty four. For many couples, that's more than a down payment
on a starter home in many parts of the country, or a big head start on retirement.""",
"""Some couples pay cash, and if that's what they truly value, great. But many borrow, or drain savings they
worked years to build, and start married life behind. Interestingly, a widely cited study by economists at
Emory University found that higher wedding spending was not associated with longer marriages. The party is
one day. The bills can last much longer.""",
"""The fix. Decide what matters most to both of you, maybe the people, the food or the photos, and spend
there. Cut the rest. Consider smaller guest lists, off peak dates, or simpler venues. And whatever you do,
avoid starting your marriage in debt.""",
"Wedding reception hall decorated", "$33,000 AVERAGE",
"Couple getting married outdoors", "ONE DAY",
"Small wedding in garden", "SPEND ON WHAT MATTERS")

item(5, "Investment fees", "the silent 1%",
"""Waste number five. High investment fees.""",
"""Many middle class investors pay fees they don't even know about. Fund expense ratios, account fees,
advisor fees. A one percent yearly fee sounds tiny, but on a growing retirement account it can add up to tens
of thousands of dollars or more over a working lifetime, because you lose the fee and all the growth it would
have produced.""",
"""Low cost index funds became popular exactly because of this. Many broad market index funds charge a small
fraction of a percent per year. Paying for good advice can be worth it, but you should always know exactly
what you're paying and what you're getting.""",
"""The fix. Look up the expense ratio of every fund you own, in your four oh one k and elsewhere. Convert the
fees into dollars per year. If you use an advisor, ask exactly how they're paid. Consider a fee only fiduciary
if you want advice.""",
"Investment statement document", "THE SILENT 1%",
"Index fund chart", "LOW COST WINS",
"Calculator with fees", "FEES IN DOLLARS")

item(6, "Food that gets thrown away", "the garbage can budget",
"""Waste number six. Food that ends up in the trash.""",
"""The US Department of Agriculture estimates that thirty to forty percent of the American food supply is
wasted. A lot of that happens at home. Produce that goes bad, leftovers forgotten in the back of the fridge,
and too much food bought on impulse at the store.""",
"""For a typical family, wasted food can easily mean hundreds of dollars or more a year thrown in the trash.
It's money spent and then literally thrown away. And it often goes hand in hand with ordering takeout because
there's nothing planned at home, so families pay twice.""",
"""The fix. Plan meals for the week, shop with a list, and check the fridge before you shop. Make one night
a week leftovers night. Freeze what you won't eat in time. These small habits can cut both food waste and
takeout spending.""",
"Food waste in trash can", "30 TO 40% WASTED",
"Fridge full of leftovers", "PAYING TWICE",
"Shopping list and meal plan", "PLAN, LIST, CHECK")

item(7, "Gym memberships nobody uses", "paying for good intentions",
"""Waste number seven. Gym memberships that go unused.""",
"""Gyms know that many members sign up with good intentions and stop going. Economists Stefano DellaVigna
and Ulrike Malmendier studied gym members and found that people on monthly contracts paid much more per
visit than they would have paid with a pay per visit option, because they went far less than they
expected.""",
"""It's a perfect example of paying for the person we hope to become, rather than the person we are. The same
pattern shows up with online courses, hobby gear and subscriptions. The intention feels good. The monthly
charge keeps coming.""",
"""The fix. Look at how many times you actually went to the gym in the last three months. Divide the cost by
the visits. If it's more than a day pass would cost, switch plans or cancel. Walking, running and home workouts
are free.""",
"Empty gym with machines", "PAYING PER VISIT",
"Exercise equipment at home", "THE PERSON WE HOPE TO BE",
"Person running outdoors", "FREE WORKOUTS")

card("""Fixing just these first seven can free up a lot of money. If it's four hundred dollars a month,
invested at a seven percent average yearly return, after twenty years that's roughly two hundred eight
thousand dollars.""",
     {"type": "growth", "monthly": 400, "rate": 0.07, "years": 20})

ch("Where the middle class budget really goes")
sc("""Let's zoom out for a moment. According to the Bureau of Labor Statistics Consumer Expenditure Survey,
housing is the biggest share of the typical American household budget, followed by transportation, then food,
then health care and insurance. Those big categories are exactly where most of the middle class waste lives.
Not in coffee. In houses, cars and food.""",
   "Pie chart household budget", "THE BIG THREE")
sc("""That's actually good news. It means you don't need to track every penny to make a big difference. A
smarter decision on your next car or your next home can be worth more than years of skipping lattes. Focus
your energy on the big three, and the small stuff matters much less.""",
   "House car and groceries icons", "FOCUS ON THE BIG THREE")
sc("""It also means the biggest wins come at specific moments. When you buy a car. When you sign a lease or a
mortgage. When you plan a wedding. When you choose your retirement funds. Those moments only come every few
years, so it's worth slowing down and getting them right. One good decision at the right moment can echo for
decades.""",
   "Signing documents at desk", "THE BIG MOMENTS")

pr("""That's angle one. Cars, houses, interest, weddings, fees, wasted food and unused memberships. Now angle
two, the psychology. Because middle class waste is often driven less by math and more by pressure.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
sc("""The middle class lives in a constant comparison. Neighbors, coworkers, parents at school, friends on
social media. Everyone is quietly measuring. And because middle class families are close enough to see
the upper middle class lifestyle, the pressure to reach for it is strong. That's where the next seven
wastes come from.""",
   "Neighbors talking over fence", "THE COMPARISON")

item(8, "Keeping up with the neighbors", "the Joneses effect",
"""Waste number eight. Keeping up with the neighbors.""",
"""Economists have studied whether people spend more when the people around them do. One study by
researchers at the Federal Reserve Bank of Philadelphia found that when a neighbor won the lottery, nearby
households were more likely to buy visible items like cars, and later more likely to face financial
trouble. Seeing others spend makes us spend.""",
"""The new SUV next door, the kitchen remodel down the street, the pool in the backyard. Each one quietly
resets what feels normal. And because these purchases are visible, they feel like status. But status bought
with debt is borrowed status.""",
"""The fix. Remember that you only see your neighbors' purchases, not their bank balances. Many of them may be
struggling. Set your own goals, write them down, and measure yourself against those goals, not against the
driveway next door.""",
"Neighbor new car in driveway", "THE JONESES",
"Lottery ticket and car keys", "SEEING OTHERS SPEND",
"Notebook with family goals", "YOUR OWN GOALS")

item(9, "Over the top kids' parties and gear", "love measured in dollars",
"""Waste number nine. Over the top kids' parties and gear.""",
"""Birthday parties with rented venues, entertainers and goody bags. Designer kids' clothes they'll outgrow
in months. The newest gadgets for children. Many parents feel enormous pressure to give their kids
everything, partly out of love, and partly because other parents are doing it.""",
"""Kids rarely remember how much a party cost. They remember time, attention and fun. And children who learn
early that money is limited, and that choices matter, often grow into more financially capable adults.
Stanley found that many millionaires deliberately avoided spoiling their children.""",
"""The fix. Set a budget for parties and gifts before the season starts. Choose experiences over things. Buy
kids' clothes and gear used when you can. And involve older kids in the choices, which teaches them about
money at the same time.""",
"Kids birthday party balloons", "THE PARTY PRESSURE",
"Parent and child playing in park", "TIME OVER THINGS",
"Kids clothes thrift store", "BUY USED")

item(10, "Vacations on credit", "paying for the trip for a year",
"""Waste number ten. Vacations paid with credit cards.""",
"""Vacations are wonderful, and rest matters. But putting a trip on a credit card you can't pay off right away
means paying interest on memories. At twenty percent or more, a three thousand dollar vacation can end up
costing hundreds of dollars more, and you could still be paying for it next summer.""",
"""There's also research suggesting that people enjoy experiences more when they're paid for in advance,
because the pain of paying is separated from the experience itself. Paying for a trip months later can take
some of the joy out of the memory.""",
"""The fix. Open a separate vacation savings account and automate a transfer each month. When the trip comes,
pay cash. You'll enjoy it more, and it will cost less. And look for ways to travel cheaper, like off season
dates or driving instead of flying.""",
"Family at beach vacation", "INTEREST ON MEMORIES",
"Credit card at hotel desk", "STILL PAYING NEXT SUMMER",
"Vacation savings jar", "SAVE FIRST, TRAVEL LATER")

body_hook = "That kitchen remodel probably won't pay for itself."
item(11, "Renovations that don't pay back", "the remodel trap",
"""Waste number eleven. Renovations they expect to pay for themselves.""",
"""Many homeowners believe a big remodel will add more value than it costs. But the annual Cost versus Value
report, which compares the cost of common projects with the value they add at resale, has consistently found
that most major remodels recoup less than their cost. Upscale kitchen and bathroom remodels often recover only
part of what was spent.""",
"""Renovating because you love your home and want to enjoy it is a fine choice. The waste is renovating on
debt and telling yourself it's an investment. And sometimes the renovation is driven by what the neighbors did,
not by what you actually need.""",
"""The fix. Before a big project, look up the Cost versus Value numbers for your region. Prioritize repairs
and maintenance over upgrades. And if you do renovate, save and pay cash, or at least know exactly what the loan
will cost in total.""",
"Kitchen renovation construction", "THE REMODEL",
"Home value appraisal", "RECOUPS LESS THAN COST",
"Home repair tools", "REPAIRS BEFORE UPGRADES")

pr("""Quick pause. If you're finding this useful, subscribe to Ryan Rover Money. It's free, it really helps,
and we break down money topics like this every week. Okay, back to the psychology. Number twelve is growing
faster than almost anything else on this list.""")

item(12, "Sports betting", "the new middle class habit",
"""Waste number twelve. Sports betting.""",
"""Since a Supreme Court decision in twenty eighteen allowed states to legalize sports betting, it has spread
across much of the country. The American Gaming Association has reported that Americans legally wagered well
over one hundred billion dollars on sports in a single year. Betting apps make it possible to bet any time,
from anywhere.""",
"""Sportsbooks build an edge into their odds, so over time, the average bettor loses. Researchers have also
found signs that easy access to betting is linked with more financial strain for some households, like lower
savings and more debt. The apps are designed to keep you playing.""",
"""The fix. If you bet for fun, set a strict monthly limit you can afford to lose completely, and never chase
losses. Use the app's limit tools. And if betting is causing stress or debt, help is available, including the
national problem gambling helpline at one eight hundred GAMBLER.""",
"Sports stadium crowd", "$100 BILLION+ WAGERED",
"Betting app on phone", "THE HOUSE EDGE",
"Phone with limits setting", "SET A HARD LIMIT")

item(13, "Upgrading phones and gadgets", "the annual upgrade",
"""Waste number thirteen. Upgrading phones and gadgets every year or two.""",
"""Flagship phones can cost a thousand dollars or more. Many families have several, plus tablets, smart
watches and laptops, often on payment plans bundled into the phone bill. The upgrade cycle is designed to make
last year's model feel old, even when it works perfectly.""",
"""Multiply that across a family of four, and gadget upgrades can cost thousands of dollars a year. Meanwhile,
each new model usually brings small improvements over the last one. The excitement of new tech fades quickly.
The payments don't.""",
"""The fix. Keep your devices until they genuinely stop meeting your needs. Consider buying the previous
year's model, or a certified refurbished one. And check your phone bill for device payments you may have
forgotten about.""",
"Family with many devices", "A FAMILY OF GADGETS",
"New phone launch event", "THE UPGRADE CYCLE",
"Refurbished phone", "KEEP IT LONGER")

item(14, "Brand names on everything", "paying for the logo",
"""Waste number fourteen. Brand names on everyday products.""",
"""Groceries, cleaning products, medicine, clothing. Store brands often cost noticeably less. A study by
economists published in the Quarterly Journal of Economics found that pharmacists and doctors were much more
likely than other shoppers to buy store brand headache medicine. When people know what's in the box, they stop
paying for the brand.""",
"""Brand loyalty is often built in childhood. We buy what our parents bought. And brands spend enormous sums on
advertising to keep it that way. But for many everyday items, the difference is mostly packaging.""",
"""The fix. Pick ten items you buy regularly and try the store brand version of each. Keep the swaps you can't
tell apart. Many families save meaningful money every month this way, without feeling any difference.""",
"Grocery store brands shelf", "PAYING FOR THE LOGO",
"Pharmacist at counter", "WHAT EXPERTS BUY",
"Grocery cart with store brands", "TRY TEN SWAPS")

ch("Why the middle class feels the pressure most")
sc("""Why do these psychological traps hit the middle class so hard? Part of it is visibility. Lower income
families often can't access the credit to keep up, and very wealthy families can afford to. The middle class
is in between. Close enough to the next level to see it every day, and just able enough to borrow to reach
for it.""",
   "Ladder reaching up", "CLOSE ENOUGH TO REACH")
sc("""Another part is identity. Many middle class families feel that certain things define them as middle
class. The house in the suburbs, two cars, a yearly vacation, kids in activities, a college degree. When
costs rise faster than income, families often borrow to keep the identity intact, rather than adjusting the
lifestyle.""",
   "Suburban family picture", "THE MIDDLE CLASS IDENTITY")
sc("""The way out is to define success on your own terms. Maybe for your family it's less debt, more time
together, and a strong safety net, rather than a bigger house. That's not settling for less. It's choosing
what actually makes your life better.""",
   "Family walking in nature", "SUCCESS ON YOUR TERMS")

pr("""That's angle two. Neighbors, kids' parties, vacations on credit, renovations, betting, gadgets and
brands. Now angle three, the playbook. These are the quiet leaks in the system, and they're some of the easiest
money you'll ever find.""")

ch("The real price tag: opportunity cost")
sc("""Before the last six, let's talk about the most important idea in this whole video. Every dollar you
spend has two prices. The price on the tag, and what that dollar could have become. Economists call the
second one opportunity cost. It's invisible, which is exactly why the middle class underestimates it.""",
   "Price tag close up", "TWO PRICES")
short('Two hundred dollars of waste really costs this much.')
sc("""Take a two hundred dollar monthly waste, like an unused gym, two forgotten streaming services and a
bit of food waste. Over thirty years, that's seventy two thousand dollars spent. But invested at a seven
percent average yearly return, the same two hundred dollars a month could grow to roughly two hundred
forty four thousand dollars. The real cost of that waste isn't seventy two thousand. It's closer to a
quarter of a million.""",
   "Calculator and coins growing", "THE INVISIBLE PRICE")
sc("""Once you start seeing that second price tag, many purchases change. A new SUV is not just fifty thousand
dollars. It's what fifty thousand dollars could have become by retirement. That doesn't mean you should never
buy anything. It means you should buy things that are worth both prices.""",
   "Person thinking in store aisle", "WORTH BOTH PRICES")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
sc("""The last six wastes are boring. Taxes, insurance, subscriptions, college planning. Nobody brags about
fixing them. But that's exactly why they're so often ignored, and why fixing them can free up money with almost
no change to your lifestyle.""",
   "Office paperwork organized", "THE BORING LEAKS")

body_hook = 'Your big tax refund is a free loan to the government.'
item(15, "A giant tax refund", "an interest free loan to the government",
"""Waste number fifteen. A huge tax refund every year.""",
"""The IRS has reported average federal tax refunds of around three thousand dollars in recent years. Many
people love getting a big refund. But a refund means you overpaid your taxes all year, and the government kept
that money without paying you any interest.""",
"""Three thousand dollars a year is about two hundred fifty dollars a month. If that money stayed in your
paycheck, it could have paid down a credit card at twenty percent, or been invested every month. Instead, it
sat with the government for free.""",
"""The fix. Use the IRS tax withholding estimator on irs.gov to adjust your W four, so your withholding is
closer to what you actually owe. Then automate the extra take home pay into savings or debt payoff, so it
doesn't just disappear.""",
"IRS tax form", "$3,000 AVERAGE REFUND",
"Government building", "AN INTEREST FREE LOAN",
"W4 form on desk", "ADJUST YOUR WITHHOLDING")

item(16, "Never shopping insurance", "loyalty that costs money",
"""Waste number sixteen. Never shopping around for insurance.""",
"""Car insurance and home insurance premiums have risen sharply in recent years. And many people renew with
the same company year after year without comparing. Consumer groups have reported that some insurers may
charge loyal customers more than new ones for similar coverage.""",
"""Insurance is one of the few big bills where a phone call or a few online quotes can save hundreds of dollars
a year with no change in coverage. Bundling policies, raising deductibles if you have an emergency fund, and
asking about discounts can all help.""",
"""The fix. Once a year, get at least three quotes for your car and home or renters insurance. Compare the
same coverage. If you have a solid emergency fund, consider a higher deductible to lower your premium.""",
"Car insurance documents", "PREMIUMS RISING",
"Person comparing quotes on laptop", "LOYALTY COSTS",
"Phone call to insurer", "THREE QUOTES A YEAR")

item(17, "The streaming stack", "cable came back",
"""Waste number seventeen. The streaming stack.""",
"""Streaming was supposed to be cheaper than cable. But many households now pay for several services at once,
and prices have gone up. Add music, cloud storage, apps and other subscriptions, and many families pay well
over one hundred dollars a month without realizing it.""",
"""The trick is that each service feels cheap on its own. And because they renew automatically, the monthly
total rarely gets reviewed. Many people pay for services they haven't opened in weeks.""",
"""The fix. Rotate. Keep one or two services at a time, and switch every few months based on what you actually
want to watch. List every subscription you pay for, and cancel anything you haven't used in the past month.""",
"Streaming apps on television", "THE STREAMING STACK",
"Subscription charges on statement", "$100+ A MONTH",
"Person canceling subscription", "ROTATE SERVICES")

item(18, "College without a plan", "the debt that follows",
"""Waste number eighteen. College without a financial plan.""",
"""Education can be one of the best investments a person makes. But choosing a school without comparing net
cost, and borrowing heavily without a plan, can leave graduates with debt that shapes their life for decades.
Federal data shows Americans owe more than one and a half trillion dollars in student loans.""",
"""Many families focus on the sticker price, or on the prestige of a name, instead of the net price after
grants and scholarships. Community college for the first two years, in state public schools, and applying for
aid can dramatically cut the cost.""",
"""The fix. Use each school's net price calculator, which colleges are required to provide. Fill out the
FAFSA every year. Compare total borrowing with expected starting salaries in the chosen field. And if you're
saving for a child, look into a five twenty nine plan.""",
"College campus students", "$1.5 TRILLION OWED",
"Student looking at college brochures", "NET PRICE, NOT STICKER",
"FAFSA form on laptop", "PLAN BEFORE YOU BORROW")

item(19, "Boats, RVs and toys", "the second payment",
"""Waste number nineteen. Big toys bought on credit.""",
"""Boats, RVs, jet skis, motorcycles. They can bring a lot of joy. But they also bring loans, insurance,
storage, maintenance and fuel. And many depreciate quickly. There's an old joke that the two happiest days of a
boat owner's life are the day they buy it, and the day they sell it.""",
"""Many owners use these toys only a few weekends a year. Divide the full yearly cost by the days used, and
the price per day can be shocking. Renting for those same days is often far cheaper.""",
"""The fix. Before buying, rent the same type of boat or RV several times. If you still love it after a year
of renting, consider buying used, with cash. And add up the full yearly cost, not just the payment.""",
"Boat at marina", "THE HAPPIEST TWO DAYS",
"RV parked in driveway", "COST PER DAY USED",
"Rental boat on lake", "RENT FIRST")

item(20, "Paying for convenience by default", "the busy family tax",
"""And waste number twenty. Paying for convenience by default.""",
"""Busy middle class families often pay for convenience everywhere. Delivery, pre cut produce, last minute
takeout, express shipping, dry cleaning, rideshares. Each one solves a real problem. Together, they can add
hundreds of dollars a month.""",
"""Convenience isn't bad. Time is valuable, especially for working parents. The waste happens when
convenience becomes the default, not the choice. When you pay delivery fees for meals you could have planned,
or express shipping for things that could wait.""",
"""The fix. Pick your top three convenience expenses and decide on purpose how much you want to spend on each
per month. Keep the conveniences that truly save you time and stress, and cut the ones that are just habits.""",
"Delivery bags at front door", "THE BUSY FAMILY TAX",
"Busy parent with kids", "TIME IS VALUABLE",
"Family planning weekly schedule", "CHOOSE ON PURPOSE")

# ---------------- Story ----------------
ch("A middle class makeover")
pr("""Let me show you what fixing a few of these can look like for a real middle class budget.""")
sc("""Imagine a family of four with a household income of about ninety thousand dollars. Two car payments
totaling twelve hundred dollars a month. A credit card balance of eight thousand. Three streaming services,
an unused gym membership, takeout three nights a week, and a three thousand dollar tax refund every spring.
They're not reckless. They're normal. And they feel stuck.""",
   "Family at kitchen table with bills", "A NORMAL FAMILY")
sc("""They make a plan. They adjust their tax withholding and send the extra two hundred fifty dollars a month
to the credit card. They cancel the gym and two streaming services. They plan meals and cut takeout to once a
week. They shop their insurance and save a little there too. Within about two years, the card is gone.""",
   "Family cooking dinner together", "THE PLAN")
sc("""When one car loan ends, they keep the old car and redirect that payment to savings and investing. Within
five years, they have a full emergency fund, a car fund, and steady retirement contributions. Their income
barely changed. Their stress changed completely.""",
   "Family relaxing in backyard", "FIVE YEARS LATER")
sc("""Nobody at work or in the neighborhood noticed anything different. They still went out to eat, still
took a summer trip, still bought birthday presents. They just stopped paying for things that didn't matter to
them. That's the middle class opportunity. Not a dramatic transformation. Just plugging leaks, one by one,
and pointing the money toward things that grow. It's slower than people want, and much faster than they
expect.""",
   "Plant growing in pot", "PLUG THE LEAKS")

# ---------------- Instead ----------------
ch("What to do with the money instead")
sc("""Once you've found the money, the order matters. First, build a starter emergency fund of around one
thousand dollars, so the next surprise doesn't land on a credit card. Second, attack high interest debt
aggressively, starting with the highest rate.""",
   "Steps going up", "STEPS 1 AND 2")
sc("""Third, get your full employer retirement match, because that's an instant return on your money. Fourth,
build your emergency fund to three to six months of expenses. Fifth, invest more for retirement, often in low
cost index funds. And sixth, save for bigger goals like a car fund, a home, or your children's education.""",
   "Stair steps to goal", "STEPS 3 TO 6")
sc("""Follow that order, and every dollar you rescue from waste goes to work where it does the most good. The
waste stops being invisible, and starts becoming your family's safety net and future.""",
   "Safety net concept", "A SAFETY NET")

# ---------------- Mistakes ----------------
ch("Mistakes when cutting back")
sc("""A few warnings before you start cutting. Mistake one. Cutting the wrong things. Some spending is an
investment in your health, your relationships or your career. Don't skip the doctor, cancel the child's
music lessons they love, or stop learning skills just to save a few dollars. Cut waste, not value.""",
   "Scissors cutting paper", "CUT WASTE, NOT VALUE")
sc("""Mistake two. Cutting everything at once. Extreme budgets tend to snap back. Change one or two things a
month, and let each new habit settle in before adding the next. Mistake three. Not giving the saved money a
job. If you cancel a subscription but leave the money in checking, it usually gets spent somewhere else.
Move it automatically to savings or debt the same day.""",
   "Money transfer on phone", "GIVE IT A JOB")
sc("""And mistake four. Feeling guilty about past spending. Everyone has wasted money. The point isn't to
punish yourself for yesterday. It's to make tomorrow's money work harder. Start where you are, with what
you have, and let the progress build.""",
   "Sunrise over field", "START WHERE YOU ARE")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. Isn't the real problem that costs have gone up? Rising costs are real, and many families
face genuine pressure. That's exactly why waste matters more now than ever. When every dollar is stretched,
the dollars leaking into interest, fees and unused services hurt even more.""",
   "Grocery prices rising", "COSTS ARE UP")
sc("""Question two. Which one should I fix first? Start with high interest credit card debt, because it's
expensive and it grows. Then look at your car and housing costs, because they're the biggest. The small stuff
can come after.""",
   "Question mark on chalkboard", "WHICH FIRST?")
sc("""Question three. Do I need to give up vacations and fun? No. The goal isn't to stop enjoying life. It's to
stop paying for things that don't make it better. Plan for fun, save for it, and pay cash. You'll enjoy it more,
and it will cost less.""",
   "Family laughing at picnic", "KEEP THE FUN")
sc("""Question four. My spouse and I disagree about spending. What now? Start by agreeing on shared goals,
then give each person some personal money to spend without explanation. Many couples find that agreeing on the
destination makes the daily choices much easier.""",
   "Couple talking on couch", "WHEN COUPLES DISAGREE")
sc("""Question five. Is it worth paying off my car early? If the interest rate is high, paying extra can be a
great guaranteed return. If the rate is very low, many people prefer to build their emergency fund and invest
first. Either way, the biggest win comes after the loan ends, when you keep the car and keep making the
payment to yourself.""",
   "Car keys on table", "PAY THE CAR OFF EARLY?")
sc("""Question six. How do I find my waste without tracking every penny? Look at three things. Your bank and
card statements for anything that repeats each month, your biggest three categories, which are usually
housing, transportation and food, and any interest or fees you paid. Those three checks find most of the
waste in about an hour.""",
   "Bank statement with highlighter", "FIND IT IN AN HOUR")
sc("""Question seven. Will cutting waste really make me wealthy? On its own, cutting waste creates the room.
What makes you wealthy is what you do with that room. Pay off expensive debt, build a cushion, and invest
steadily for years. Cutting waste is the first step. Investing the difference is the second.""",
   "Two steps on staircase", "THE TWO STEPS")

# ---------------- Recap ----------------
ch("Recap: all 20")
sc("""Quick recap. Angle one, the numbers. New cars on long loans, too much house, credit card interest, very
expensive weddings, investment fees, wasted food and unused gym memberships.""",
   "Checklist on clipboard", "THE NUMBERS: 1 TO 7")
sc("""Angle two, the psychology. Keeping up with the neighbors, over the top kids' parties, vacations on credit,
renovations that don't pay back, sports betting, gadget upgrades and brand names.""",
   "Person thinking at window", "THE PSYCHOLOGY: 8 TO 14")
sc("""Angle three, the playbook. A giant tax refund, never shopping insurance, the streaming stack, college
without a plan, boats and toys on credit, and convenience by default.""",
   "Notebook with plan", "THE PLAYBOOK: 15 TO 20")

# ---------------- Close ----------------
ch("What to do next")
pr("""Here's what I want you to take away. The middle class is not doomed, and you are not stuck. Costs are
high, but inside almost every budget there's room hiding in plain sight, in car payments, interest, fees and
habits nobody questions. Find it, give it a job, and let it grow. The middle class doesn't need to work
harder. It needs to stop leaking. Pick one item from each angle
and fix it this month. If you want the full plan, it's in my playbook, linked in the description. Tell me in the
comments how much you think you could save. I'm Ryan Rover. See you in the next one.""")

save("video25", "20 Things the Middle Class Wastes Money On", [
    "Pew Research Center, share of adults in middle-income households (61% in 1971, 51% in 2023)",
    "Kelley Blue Book, average new-vehicle transaction price above $50,000 (2025); Edmunds, average new-car payment above $700",
    "Federal Reserve G.19 credit card rates; Federal Reserve Bank of New York, Household Debt and Credit Report (card balances over $1 trillion)",
    "The Knot, Real Weddings Study 2024 (average cost about $33,000); Francis-Tan and Mialon, Emory University (2014)",
    "USDA, food loss and waste (30-40% of the US food supply)",
    "DellaVigna and Malmendier, Paying Not to Go to the Gym (American Economic Review, 2006)",
    "Agarwal, Mikhed and Scholnick, Federal Reserve Bank of Philadelphia, lottery prizes and neighbors' spending",
    "Zonda, Cost vs. Value Report; American Gaming Association, commercial gaming revenue tracker",
    "Bronnenberg et al., Do Pharmacists Buy Bayer? (QJE 2015); IRS filing season statistics; IRS Tax Withholding Estimator",
    "Federal Student Aid, student loan portfolio (over $1.5 trillion); US BLS Consumer Expenditure Survey",
    "Growth example: monthly compounding at 7% average yearly return (illustration, not a promise)",
], "20 things the middle class wastes money on, from 3 angles: numbers, psychology, playbook")
