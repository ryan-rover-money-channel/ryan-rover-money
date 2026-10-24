import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short


def trap(n, title, sub, card_text, what, why, fix, q1, c1, q2, c2, q3, c3):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"TRAP {n}")
    sc(what, q1, c1)
    sc(why, q2, c2)
    sc(fix, q3, c3)

# ---------------- Intro ----------------
ch("Intro")
short("Most middle class families never pass two hundred fifty thousand dollars. Here's the trap.")
pr("""Hi, I'm Ryan Rover. There's an invisible ceiling in American money. Millions of hardworking families reach a certain
point, a decent income, a house, a couple of cars, some retirement savings, and then they stop moving up. Year after year,
the income rises, but the wealth doesn't. I call it the middle class trap. And today we're going to take it apart, piece by
piece.""")
card("""Two hundred fifty thousand dollars of net worth. A line that many middle class families hover around for decades,
often with most of it tied up in their home.""",
     {"type": "stat", "label": "the invisible ceiling", "big": "$250,000", "sub": "where many families stall"})
sc("""Here's what makes it a trap. Nothing about it feels wrong. You have a job, a mortgage, a car payment, kids in
activities, a vacation every year, and something in a 401k. You're doing what you were told. But when you look closely,
almost all of your money is either locked in your house or spent the moment it arrives. And there's very little left
working for you.""",
   "Suburban houses street United States", "NOTHING FEELS WRONG")
sc("""In this video, fifteen traps that keep middle class families stuck, with real numbers from the Federal Reserve and other
sources. And we'll look at it from three angles. The numbers: where middle class wealth actually sits. The psychology: why
smart people stay in the trap. And the playbook: how families break through to five hundred thousand, a million, and beyond.""",
   "Calculator with financial charts", "15 TRAPS, 3 ANGLES")
pr("""If you've ever wondered why you work so hard and still feel like you're running in place, this video is for you. And if
you're just starting out, it's a map of the traps to avoid before they ever close around you. First,
the sources.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Household wealth data comes from the Federal Reserve's Survey of Consumer Finances and the Federal Reserve's Distributional
Financial Accounts. Income data comes from the U.S. Census Bureau. Retirement account data comes from Vanguard's How America
Saves report. Car prices come from Kelley Blue Book, and child care costs from Child Care Aware of America. Growth examples use a
seven percent average yearly return as an illustration, not a promise. This is education, not financial advice.""",
   "Federal Reserve Bank building columns", "OUR SOURCES")

# ---------------- Angle 1: numbers ----------------
ch("Angle 1: The numbers")
pr("""Angle one. The numbers. Let's look at where middle class wealth actually lives, because once you see it, the trap becomes
obvious.""")
card("""The U.S. Census Bureau reported a median household income of about eighty three thousand seven hundred dollars in twenty
twenty four. The Federal Reserve found a median family net worth of about one hundred ninety two thousand seven hundred dollars in
twenty twenty two.""",
     {"type": "compare", "left": {"label": "Median income", "big": "$83,730", "sub": "Census Bureau, 2024"},
      "right": {"label": "Median net worth", "big": "$192,700", "sub": "Federal Reserve, 2022"},
      "note": "Different surveys and years, shown for scale"})
sc("""So the typical household earns over eighty thousand dollars a year, and has a net worth of a little more than two years of
that income. And for many middle class families, the largest part of that net worth is home equity. The Federal Reserve's data
consistently shows that the primary home is the biggest asset for families in the middle of the wealth distribution, while
wealthier families hold much more in stocks and businesses.""",
   "House with for sale sign", "THE HOME IS THE WEALTH")
card("""The Federal Reserve's Distributional Financial Accounts show the top ten percent of households hold about two thirds of all
household wealth in America. The bottom half holds only a few percent.""",
     {"type": "compare", "left": {"label": "Top 10%", "big": "~2/3", "sub": "of household wealth"},
      "right": {"label": "Bottom 50%", "big": "a few %", "sub": "of household wealth"},
      "note": "Federal Reserve, Distributional Financial Accounts"})
sc("""Why does that gap exist? A big part of the answer is ownership. Wealthier households own most of the stocks, the
businesses and the investment properties, assets that can grow faster than incomes over long periods. Middle class households
mostly own their home and their ability to work. When the economy grows, owners tend to capture more of that growth.""",
   "New York Stock Exchange trading floor", "OWNERS VS EARNERS")
sc("""And look at retirement accounts. Vanguard's How America Saves report found the average balance in the plans it administers was
around one hundred forty eight thousand dollars in twenty twenty four, but the median was only about thirty eight thousand. Like
net worth, a smaller group with big balances pulls the average up. The typical worker has far less invested than the headlines
suggest.""",
   "Office workers meeting", "MEDIAN 401K: ~$38,000")
sc("""Put it together and you get the shape of the trap. A good income that mostly gets spent. A house that holds most of the
wealth. A small amount invested. And a monthly budget full of payments that leave little room to change any of it. Now let's go
through the fifteen traps that create that shape.""",
   "Hamster wheel", "THE SHAPE OF THE TRAP")
sc("""There's also a timing problem. Middle class costs tend to peak at the same time: a mortgage, car loans, child care, kids'
activities and sometimes help for aging parents, all landing in your thirties and forties. Those are also the years when investing
has the most time to grow. So the decades when money could compound the most are often the decades when there's the least left to
invest. That collision is one of the quiet engines of the trap.""",
   "Family dinner table", "EVERYTHING PEAKS AT ONCE")
sc("""And retirement has shifted onto workers' shoulders. Decades ago, many middle class workers had traditional pensions that
promised a monthly check for life. Today, most private sector workers rely on 401k style plans, where the amount you retire with
depends on how much you put in, how it's invested and how long it grows. That's more flexible, but it means the trap now has a direct
cost: if you don't invest enough, nobody else will do it for you.""",
   "Office workers meeting", "FROM PENSIONS TO 401Ks")
pr("""Trap number one is the one almost every middle class family falls into, and it's the place they live.""")

# ---------------- Traps ----------------
trap(1, "The house is the only asset", "house rich, cash poor",
"""Trap number one. The house is the only real asset.""",
"""For many families, the house is the retirement plan, the emergency fund and the investment portfolio, all in one. They pour
money into the mortgage, the renovations and the upgrades, and very little into anything else. On paper, their net worth looks
healthy. In real life, they can't touch most of it.""",
"""A house is a fine thing to own. But it doesn't pay you income while you live in it. It costs you money every year in taxes,
insurance and repairs. And to unlock its value, you have to sell it, borrow against it, or move. A family with four hundred
thousand dollars of home equity and twenty thousand invested is much less free than the number suggests.""",
"""The fix: track two numbers, your net worth with the house and without it. Aim to grow the second number steadily, through
retirement accounts and other investments. Your home is part of your wealth, not all of it.""",
"House with for sale sign", "HOUSE RICH",
"House repair roof", "IT DOESN'T PAY YOU",
"Spreadsheet on laptop", "NET WORTH WITHOUT THE HOUSE")

trap(2, "Too much house", "the payment that eats your future",
"""Trap number two. Buying too much house.""",
"""Lenders will often approve you for more than you should borrow. And when you're approved for a bigger house, it's tempting to
buy it. A bigger mortgage, bigger property taxes, bigger insurance, bigger utility bills, and more rooms to furnish. Each one
locks in higher costs for decades.""",
"""Harvard's Joint Center for Housing Studies reports that millions of American households are cost burdened, meaning they spend
more than thirty percent of their income on housing. When housing takes that much, saving and investing get squeezed out. The
house becomes the reason you can't build wealth anywhere else.""",
"""The fix: keep your total housing cost, including taxes and insurance, well below what the bank says you can afford. Many
planners suggest staying around twenty five to thirty percent of your gross income or less. The difference between a good house
and a dream house can be the difference between stuck and free.""",
"Mansion house exterior", "TOO MUCH HOUSE",
"Bills on table", "COST BURDENED",
"Calculator and pen on financial papers", "BELOW WHAT THE BANK SAYS")

trap(3, "Car payments forever", "always one payment away",
"""Trap number three. The permanent car payment.""",
"""Many middle class families always have a car payment. When one loan ends, they trade in for a new car and start another. Kelley
Blue Book has reported average new vehicle prices near fifty thousand dollars, and Edmunds has reported average new car payments
above seven hundred dollars a month.""",
"""Seven hundred dollars a month, forever, is eight thousand four hundred dollars a year. Over thirty years, at a seven percent
illustration, that money invested could grow to roughly eight hundred fifty thousand dollars. For a two car household, the
permanent car payment can quietly cost a family a seven figure retirement.""",
"""The fix: buy reliable cars, keep them long after they're paid off, and when the loan ends, keep making the payment, but to your
own investment account. Every year you drive a paid off car is a year you're paying yourself instead of a lender.""",
"Car dealership lot", "ALWAYS A PAYMENT",
"Graph trending upward", "$700/MO = ~$850K",
"Old car parked on street", "PAY YOURSELF INSTEAD")

trap(4, "Lifestyle matches income", "every raise disappears",
"""Trap number four. Your lifestyle rises exactly as fast as your income.""",
"""When middle class incomes rise, spending usually follows. The apartment becomes a house. The house gets a renovation. The
vacations get nicer. None of it is wrong. But if spending rises as fast as income, your savings rate never changes, and neither
does your financial position.""",
"""This is the core mechanism of the middle class trap. Two families can earn the same raises over twenty years. The one that
spends every raise ends up with a nicer lifestyle and no extra wealth. The one that saves half of every raise ends up with both a
better lifestyle and a much larger net worth.""",
"""The fix: decide in advance that at least half of every raise goes to savings and investing. Automate it the moment the raise
arrives, before you get used to the extra money. Your life still improves every year, just not as fast as your income.""",
"Luxury car dealership", "EVERY RAISE DISAPPEARS",
"Two people office", "SAME RAISE, DIFFERENT RESULT",
"Online banking smartphone app", "HALF OF EVERY RAISE")

trap(5, "Saving without investing", "money that sleeps",
"""Trap number five. Saving, but not investing.""",
"""Some middle class families are good savers, but they keep everything in a checking or savings account. It feels safe. But money
sitting in cash for decades loses buying power to inflation, and misses out on the growth that builds real wealth.""",
"""At three percent inflation, prices roughly double in about twenty four years. So money that just sits still is slowly getting
smaller. Meanwhile, broad stock markets have historically grown faster than inflation over long periods, though with ups and downs
along the way and no guarantee for the future.""",
"""The fix: keep your emergency fund in safe, high yield savings. Invest money you won't need for many years in diversified, low
cost funds, in tax advantaged accounts first. Saving is the first step. Investing is what turns savings into wealth.""",
"Bank vault door", "MONEY THAT SLEEPS",
"Grocery store shelves prices", "INFLATION",
"Pie chart on paper", "INVEST FOR THE LONG TERM")

trap(6, "Investing just enough", "stopping at the match",
"""Trap number six. Investing only enough to get the match.""",
"""Many workers contribute exactly enough to get their employer match, often around four to six percent of pay, and stop there.
Getting the match is smart. But for most people, it's not enough to build a comfortable retirement on its own.""",
"""Many retirement planners suggest saving around fifteen percent of income, including any employer match, over a full career.
Someone saving six percent total may end up with a fraction of what they'll need. The match is the floor, not the goal.""",
"""The fix: raise your contribution by one percentage point every year, ideally timed with your raise so you never feel it. Many
plans offer an automatic increase feature that does this for you. In a few years, you'll be at fifteen percent without ever having
made a painful cut.""",
"Office workers meeting", "THE MATCH IS THE FLOOR",
"Calculator with financial charts", "AIM FOR ~15%",
"Graph trending upward", "+1% EVERY YEAR")

trap(7, "Income that stalls", "staying put too long",
"""Trap number seven. An income that stops growing.""",
"""Many middle class workers stay in the same job for years, getting small annual raises that barely beat inflation. Loyalty feels
safe. But wage data from the Federal Reserve Bank of Atlanta has often shown that people who switch jobs see faster pay growth
than those who stay.""",
"""When income stalls, every other part of the plan gets harder. It's the one input that can grow without limit, and it compounds,
because future raises are based on your current salary. A few years of stalled pay can cost far more than any budgeting mistake.""",
"""The fix: know your market value. Check job listings for your role every year. Learn one skill that's in demand. Ask for raises
with evidence. And be willing to move, inside your company or outside, when the pay difference is meaningful.""",
"Office building at dusk", "STALLED INCOME",
"Job interview handshake", "MOVERS EARN MORE",
"Person studying laptop at night", "KNOW YOUR WORTH")

short("Paying for your kids' college before your retirement is a trap. Here's why.")
trap(8, "Kids before retirement", "the loving mistake",
"""Trap number eight. Funding everything for the kids before your own retirement.""",
"""Middle class parents often put their children first: activities, sports, private lessons, college savings. Child Care Aware of
America reports that the national average price of child care has been more than eleven thousand dollars a year. These costs are
real, and they come from love.""",
"""But here's the hard truth many financial planners repeat: your kids can borrow for college, but you can't borrow for retirement.
If you reach sixty with no savings, your kids may end up supporting you. Securing your own future can be one of the best gifts you
give them.""",
"""The fix: fund your own retirement first, at least to the point of getting the full match and a healthy savings rate. Then save
for college with what's left, often in a tax advantaged 529 plan. And be selective about activities. Kids need your time more than
your money.""",
"Family dinner table", "KIDS FIRST?",
"Graduation cap diploma", "THEY CAN BORROW, YOU CAN'T",
"Family walking on beach", "TIME OVER MONEY")

trap(9, "Revolving credit card debt", "the quiet drain",
"""Trap number nine. Carrying credit card debt month to month.""",
"""Credit card interest rates have been above twenty percent, according to the Federal Reserve. Many middle class families carry a
balance from month to month, using the card to cover the gap between income and spending.""",
"""A ten thousand dollar balance at twenty two percent costs about two thousand two hundred dollars a year in interest. That's money
flowing out of your household to the bank every year, for things you already bought. It's compound interest working directly
against you.""",
"""The fix: stop adding to the balance, build a small cushion so emergencies don't land on the card, then pay off the highest rate
debt first. Once it's gone, pay the card in full every month. Every dollar of interest you stop paying is a dollar you can invest.""",
"Credit card close up", "OVER 20% A YEAR",
"Credit card bills on table", "$10K = ~$2,200 A YEAR",
"Scissors cutting credit card", "PAY IN FULL")

pr("""Quick pause. If you see your family in some of these traps, you're not alone, and you're not stuck. Subscribe to the channel,
because the next videos go step by step through how to break out, from the first ten thousand to the first million. Now, trap
number ten.""")

trap(10, "Fees that compound", "the hidden tax on your savings",
"""Trap number ten. High fees on investments.""",
"""Some retirement plans, funds and advisory arrangements charge one percent a year or more. It sounds tiny. But fees come out every
year, whether your investments go up or down, and they compound just like returns do.""",
"""Over thirty years, the difference between paying around one percent and paying a small fraction of a percent can add up to a
large share of your final balance. On a middle class retirement account, that can easily be tens of thousands of dollars, or more,
simply transferred from you to the financial industry.""",
"""The fix: look up the expense ratio of every fund you own. In your workplace plan, look for low cost index funds or target date
funds. If you pay an advisor, know exactly what you pay in dollars per year, and what you get for it.""",
"Receipt and coins on table", "FEES COMPOUND",
"Investment fund prospectus document", "KNOW YOUR EXPENSE RATIO",
"Business meeting handshake", "ASK IN DOLLARS")

trap(11, "Ignoring tax advantages", "leaving free money on the table",
"""Trap number eleven. Not using tax advantaged accounts.""",
"""The tax code gives middle class families powerful tools: workplace retirement plans, IRAs, health savings accounts for eligible
plans, and 529 college savings plans. Each one lets money grow with tax advantages. Yet many families don't use them fully, or at
all.""",
"""Wealthy families use these tools aggressively, along with others. Middle class families often leave them partly empty. Over
decades, the difference between growing money with tax advantages and without them can be substantial.""",
"""The fix: learn the basic accounts available to you, check the current IRS limits each year, and fill the most valuable ones
first. Often that's the employer match, then a health savings account if eligible, then an IRA, then more in the workplace plan.""",
"Tax forms on desk", "TAX ADVANTAGES",
"Paperwork documents desk", "FILL THE BUCKETS",
"Calendar planning", "CHECK LIMITS EVERY YEAR")

trap(12, "No protection", "one bad event erases years",
"""Trap number twelve. Missing insurance and protection.""",
"""Middle class wealth is fragile because it's often built on a single income and a single house. A disability, a serious illness,
a lawsuit or a death without life insurance can erase decades of progress in months.""",
"""Many people insure their car and their phone but not their ability to earn an income, which is often their biggest asset. Long
term disability insurance and term life insurance, if anyone depends on you, protect the foundation everything else is built on.""",
"""The fix: check whether your employer offers disability insurance and how much it covers. If people depend on your income,
consider affordable term life insurance. Write a basic will and name beneficiaries on every account. It's boring, and it's
essential.""",
"Hospital building exterior", "FRAGILE WEALTH",
"Lawyer office documents", "PROTECT YOUR INCOME",
"Paperwork documents desk", "WILL AND BENEFICIARIES")

trap(13, "Panic in the crash", "selling at the bottom",
"""Trap number thirteen. Selling investments in a market crash.""",
"""Every decade or so, markets fall sharply. When middle class families finally have some money invested and watch it drop, the fear
is overwhelming. Many sell near the bottom, then wait on the sidelines until prices have already recovered.""",
"""Research firms like DALBAR have repeatedly found that the average investor earns less than the funds they invest in, largely
because of buying high and selling low. Panic turns a temporary decline into a permanent loss, and it can set a family back by
years.""",
"""The fix: decide now what you'll do in a crash, and write it down. For most long term investors, the answer is to keep
contributing and not sell. Keep your emergency fund separate so you're never forced to sell. And check your accounts less often.""",
"Stock market crash newspaper", "PANIC SELLING",
"Stock market chart falling on screen", "BUY HIGH, SELL LOW",
"Notebook with financial notes", "WRITE YOUR CRASH PLAN")

trap(14, "Only earning, never owning", "trading time for money forever",
"""Trap number fourteen. Relying only on your labor, and never owning assets.""",
"""Most middle class income comes from one source: a paycheck. When you stop working, the income stops. Wealthier families earn a
large share of their income from what they own: stocks, businesses and real estate. Their money works even when they don't.""",
"""This is the deepest reason the trap exists. Wages tend to grow slowly. Ownership can compound. The goal isn't to stop working,
it's to gradually shift from earning everything with your time to having your assets earn more and more of it.""",
"""The fix: become an owner, step by step. Broad index funds make you a part owner of thousands of companies. Some people add rental
property or a small business over time. Every dollar you invest is a small employee working for you.""",
"Small business storefront", "EARNERS VS OWNERS",
"Factory machine gears", "ASSETS WORK FOR YOU",
"New York Stock Exchange trading floor", "BECOME AN OWNER")

trap(15, "Waiting for later", "the most expensive trap of all",
"""Trap number fifteen. The most expensive one. Waiting to get serious until later.""",
"""Later is when the kids are older. When the car is paid off. When the next raise comes. Middle class life always has a reason to
wait. And every year of waiting costs more than the last, because you lose the years when compounding works best.""",
"""At a seven percent illustration, five hundred dollars a month for thirty years grows to roughly six hundred ten thousand dollars.
Wait ten years and invest the same amount for only twenty years, and you'd end with roughly two hundred sixty thousand. Ten years of
waiting can cost more than half of the final result.""",
"""The fix: start now, with whatever you can. Even a small amount, automated today, beats a perfect plan that starts someday. Then
increase it every year. The best time was ten years ago. The second best time is this week.""",
"Wall clock office", "LATER COSTS MORE",
"Calendar planning", "10 YEARS = HALF THE RESULT",
"Sunrise over mountains", "START THIS WEEK")

# ---------------- Warning signs ----------------
ch("Eight signs you're in the trap")
pr("""How do you know if your family is in the middle class trap? Here are eight warning signs. Count how many apply to you.""")
sc("""Sign one. Your income has gone up a lot over the past ten years, but your savings haven't grown much. Sign two. You've had a
car payment for most of your adult life, and you can't remember the last time you didn't. Sign three. Your home equity is more than
three quarters of your net worth.""",
   "Car dealership lot", "SIGNS 1 TO 3")
sc("""Sign four. You contribute exactly enough to your retirement plan to get the match, and no more. Sign five. You carry a credit
card balance more months than not. Sign six. If you lost your job, you'd have less than three months before you needed to borrow.""",
   "Credit card bills on table", "SIGNS 4 TO 6")
sc("""Sign seven. You don't know what fees you pay on your investments. And sign eight. When you imagine retiring, the plan is mostly,
we'll figure it out, or, we'll sell the house. If three or more of these sound familiar, the trap has a grip on your finances. The
good news is that every sign on this list can be reversed, usually within a few years.""",
   "Person thinking by window", "SIGNS 7 AND 8")
sc("""And here's the encouraging part. Families who reverse just two or three of these signs often see a dramatic change. Paying off
the cards and stopping the car payment cycle alone can free up over a thousand dollars a month for many households. Invested over
twenty years, that's the difference between hoping and knowing.""",
   "Sunrise over mountains", "REVERSE TWO OR THREE")
sc("""If you counted zero or one sign, congratulations, you're probably already on your way through the ceiling. Your job now is to
protect what's working: keep the savings rate high as your income grows, keep fees low, and don't let a big house or a new truck
reverse years of progress. Staying out of the trap takes far less effort than climbing out of it, but it still takes attention every
time your income or your family changes.""",
   "Mountain climber reaching summit", "ZERO OR ONE SIGN?")

# ---------------- Past the ceiling ----------------
ch("Life past the ceiling")
pr("""So what does it actually look like when a middle class family breaks through? Let's walk through the next milestones.""")
sc("""At five hundred thousand dollars of net worth, with a good share of it invested rather than in the house, life feels different.
A job loss is a setback, not a crisis. Investment growth in a good year can rival a year of saving. And for the first time, early or
flexible retirement starts to look like a real possibility, not a fantasy.""",
   "Family relaxing at home", "$500,000")
sc("""At one million dollars, especially with the house mostly paid off, many families reach what planners call optionality. They can
choose work they like, help their kids without risking their own future, and handle almost any emergency. Using the four percent rule
of thumb, seven hundred fifty thousand dollars invested could support about thirty thousand dollars a year, on top of Social
Security.""",
   "Retired couple walking in park", "$1,000,000")
sc("""And here's the most important thing families say about breaking through. It didn't feel dramatic. There was no single moment.
It was the same boring choices, made over and over: keeping the cars, investing the raises, not upgrading the house, staying invested
in the crash. The trap is broken by habits, not by heroics.""",
   "Staircase steps", "HABITS, NOT HEROICS")

# ---------------- Two families ----------------
short("Two families earn the same income. Twenty five years later, one has four times more.")
ch("Two families, same income")
pr("""Let's see how these traps play out over time. Two example families. Same income, same city, same starting point. Made up, but
the math is real.""")
sc("""The Millers earn ninety thousand dollars a year combined. They buy the biggest house the bank approves. They always have two car
payments, about thirteen hundred dollars a month together. They contribute five percent to their 401ks to get the match, and their
spending rises with every raise. They're not reckless. They're normal.""",
   "Suburban houses street United States", "THE MILLERS")
sc("""The Parkers earn the same ninety thousand. They buy a smaller house, comfortably within budget. They drive paid off cars for
years and buy reliable used ones when needed. They save fifteen percent for retirement, including the match, and send half of every
raise to investing. They take vacations and enjoy life, just without the big monthly payments.""",
   "Family relaxing at home", "THE PARKERS")
sc("""After twenty five years, both families have paid down their mortgages. But the Parkers have been investing roughly an extra
thousand dollars a month that the Millers spent on cars and a bigger house. At a seven percent illustration, one thousand dollars a
month for twenty five years grows to roughly eight hundred ten thousand dollars. That difference alone could separate a family stuck
near two hundred fifty thousand from one well past a million.""",
   "Graph trending upward", "~$810K DIFFERENCE")
sc("""Here's what's striking. From the outside, the Millers looked more successful for most of those years. Bigger house, newer cars.
The Parkers looked ordinary. But in their fifties, the Parkers have choices: retire early, work part time, help their kids. The Millers
have a big house and a lot of worry. That's the middle class trap in one picture.""",
   "Retired couple on porch", "CHOICES VS WORRY")

# ---------------- Angle 2: psychology ----------------
short("Why do smart, hardworking people stay stuck in the middle class? It's not the math.")
ch("Angle 2: The psychology")
pr("""Angle two. The psychology. Why do smart, hardworking people stay in the trap, even when they know the math?""")
sc("""The first reason is social norms. In most middle class neighborhoods, the big house, the new cars and the expensive activities
are normal. Doing less can feel like falling behind, or even like failing your family. Economists have long noted that people judge
their own well being partly by comparing themselves to those around them.""",
   "Suburban houses street United States", "KEEPING UP")
sc("""The second reason is that payments hide prices. A fifty thousand dollar truck is scary. Seven hundred dollars a month feels
manageable. A bigger mortgage is just a few hundred more per month. Monthly payments make big decisions feel small, which is exactly
why they're so effective at keeping people stuck.""",
   "Car dealership lot", "PAYMENTS HIDE PRICES")
sc("""The third reason is that the trap feels like success. The middle class markers, a house, cars, vacations, are visible. Wealth
isn't. You can't see someone's brokerage account from the street. So families optimize for what can be seen, and neglect what can't.
Thomas Stanley and William Danko described exactly this in The Millionaire Next Door.""",
   "Mansion house exterior", "VISIBLE VS INVISIBLE")
sc("""The fourth reason is exhaustion. Middle class life is busy: work, kids, commuting, caring for parents. When you're exhausted,
the easiest decision is to keep doing what you've always done. That's why automation matters so much. It lets good decisions happen
even when you're too tired to make them.""",
   "Person stressed looking at bills", "TOO TIRED TO CHANGE")
sc("""And the fifth reason is hope that something big will fix it. A promotion, an inheritance, a winning stock, a house that doubles
in value. People wait for the big break instead of making small changes now. But for most families, wealth comes from small changes
repeated for decades, not from one big moment.""",
   "Slot machines casino", "WAITING FOR THE BIG BREAK")

# ---------------- Angle 3: playbook ----------------
short("Here's how middle class families break through to their first million dollars.")
ch("Angle 3: The playbook")
pr("""Angle three. The playbook. Here's how middle class families break through the ceiling, in six moves.""")
sc("""Move one. Know your numbers. Calculate your net worth with and without your home, and your savings rate: the share of your
income that goes to savings, investing and paying down debt. Most families have never calculated either. You can't escape a trap
you can't see.""",
   "Spreadsheet on laptop", "MOVE 1: KNOW YOUR NUMBERS")
sc("""Move two. Free up the big money. Housing, cars and child care are usually the biggest costs. You don't need to slash all three.
But one big change, like keeping your cars for years longer or not upgrading your home, can free hundreds of dollars a month. Small
savings help, but the big three move the needle.""",
   "Old car parked on street", "MOVE 2: FREE THE BIG MONEY")
sc("""Move three. Automate your way to fifteen percent or more. Retirement contributions through payroll, automatic transfers to an IRA
and a brokerage account, and an automatic increase every year. The goal is a system that builds wealth whether or not you're paying
attention.""",
   "Clock gears mechanism", "MOVE 3: AUTOMATE 15%")
sc("""Move four. Become an owner. Invest consistently in low cost, diversified funds. Consider other ownership over time, like a small
business or real estate, only once your foundation is solid. The more of your income that comes from what you own, the less you
depend on your next paycheck.""",
   "New York Stock Exchange trading floor", "MOVE 4: BECOME AN OWNER")
sc("""Move five. Grow your income on purpose. Ask for raises, switch jobs when it makes sense, build skills, and consider side income.
Then send at least half of every increase to investing. And move six. Protect it. Emergency fund, disability insurance, term life if
needed, a will, and a written plan for market crashes.""",
   "Job interview handshake", "MOVES 5 AND 6")
sc("""None of these moves require you to stop enjoying life. They require you to decide what matters most, and to stop letting monthly
payments make that decision for you. Families who do this often find they're happier, not less happy, because money stops being a
constant source of stress.""",
   "Family walking on beach", "LESS STRESS")

# ---------------- Questions ----------------
ch("Questions people ask")
pr("""Let me answer the questions people ask most about the middle class trap.""")
sc("""Question one. Is buying a house a mistake? No. Owning a home can be a good way to build wealth and stability. The trap is buying
too much house, or letting the house be your only asset. Question two. Should we stop saving for college? Not necessarily. Just make
sure your own retirement is on track first, and be realistic about how much you can contribute.""",
   "House with for sale sign", "IS A HOUSE A MISTAKE?")
sc("""Question three. We're in our forties and stuck. Is it too late? No. Your forties and fifties are often your peak earning years.
Freeing up a thousand dollars a month and investing it for twenty years, at a seven percent illustration, could grow to roughly five
hundred twenty thousand dollars. That alone can break the ceiling.""",
   "Older man reading financial newspaper", "STUCK IN OUR FORTIES?")
sc("""Question four. How do we talk to our kids about this? Be honest in an age appropriate way. Explain that you're choosing to save
for the family's future, and involve them in small decisions. Kids who learn early that money is a tool, not a scoreboard, are more
likely to avoid the trap themselves.""",
   "Family dinner table", "TALKING TO KIDS")
sc("""Question five. What if our neighbors judge us for driving old cars? Remember, you see their car, not their debt. Many of the
people who look the wealthiest are the most stretched. And in twenty years, nobody will remember what you drove. They'll notice that
you're relaxed, and they're still working.""",
   "Old car parked on street", "WHAT WILL THE NEIGHBORS THINK?")
sc("""Question seven. We earn a good income but feel broke. Where do we start? Start with a one month spending review. Write down every
fixed payment: mortgage or rent, cars, insurance, subscriptions, child care, debt. For most families who feel broke on a good income,
the answer is in that list, not in coffee or groceries. Pick the biggest payment you can realistically change in the next year, and
make a plan to change it.""",
   "Spreadsheet on laptop", "GOOD INCOME, FEEL BROKE?")
sc("""Question six. Should we use our home equity to invest? Borrowing against your home to invest adds risk, because you could lose
money in the market and still owe the debt, with your house as collateral. For most families, it's safer to build investments from
monthly cash flow, and let home equity grow on its own.""",
   "Bank building United States", "BORROW AGAINST THE HOUSE?")

# ---------------- Recap ----------------
ch("Recap: 15 middle class traps")
sc("""Let's recap the fifteen traps. The house is the only asset. Too much house. Car payments forever. Lifestyle that matches income.
Saving without investing. Investing just enough for the match. Income that stalls. And funding the kids before your own retirement.""",
   "Notebook with financial notes", "TRAPS 1 TO 8")
sc("""Revolving credit card debt. Fees that compound. Ignoring tax advantages. No protection. Panic in the crash. Only earning, never
owning. And the most expensive trap of all: waiting for later.""",
   "Mountain climber reaching summit", "TRAPS 9 TO 15")
sc("""And the three angles. The numbers: middle class wealth is mostly home equity, and the median retirement account is small. The
psychology: social norms, payments that hide prices, and success you can see instead of wealth you can't. And the playbook: know your
numbers, free up the big money, automate fifteen percent, become an owner, grow your income, and protect it all.""",
   "Map and compass", "NUMBERS, PSYCHOLOGY, PLAYBOOK")
sc("""The middle class trap isn't a conspiracy, and it isn't your fault. It's the natural result of a culture that sells monthly
payments, a housing market that rewards stretching, and a retirement system that depends on you doing the work. But once you see it,
you can step out of it, one decision at a time. Keep the car. Invest the raise. Choose the smaller house. Stay invested in the crash.
Those choices look small. Over twenty years, they're the difference between a ceiling and a launch pad.""",
   "Sunrise over mountains", "A CEILING OR A LAUNCH PAD")

# ---------------- Close ----------------
ch("What to do next")
pr("""So here's your homework. Pick the one trap from this list that costs your family the most. Just one. And make one change this
month. Then, next month, pick the next one. Fifteen traps sounds like a lot, but most families only need to fix three or four to
break through. If you want the full step by step plan, it's in my playbook, link in the description. I'm Ryan Rover. See you in the next
one.""")

save("video10", "The Middle-Class Trap: Why Most People Never Pass $250K", [
    "U.S. Census Bureau, Income in the United States: 2024 (median household income about $83,730)",
    "Federal Reserve, Survey of Consumer Finances 2022 (median family net worth $192,700; primary residence as largest asset for middle-wealth families)",
    "Federal Reserve, Distributional Financial Accounts (top 10% hold about two thirds of household wealth)",
    "Vanguard, How America Saves 2025 (average account balance about $148,000, median about $38,000 in 2024)",
    "Kelley Blue Book, average new-vehicle transaction price; Edmunds, average new car payment above $700",
    "Harvard Joint Center for Housing Studies, The State of the Nation's Housing (cost-burdened households)",
    "Child Care Aware of America, child care price data (national average above $11,000 a year)",
    "Federal Reserve Bank of Atlanta, Wage Growth Tracker (job switchers vs stayers)",
    "Federal Reserve G.19 Consumer Credit (credit card interest rates above 20%)",
    "DALBAR, Quantitative Analysis of Investor Behavior",
    "Thomas J. Stanley and William D. Danko, The Millionaire Next Door (1996)",
    "Compound growth: stated illustrative math at 7% average yearly return, compounded monthly",
], "the middle-class trap")
