import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

def item(n, title, sub, card_text, body, example, q1, c1, q2, c2):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"MYTH {n}")
    sc(body, q1, c1)
    sc(example, q2, c2)
    o = ORIGIN[n]
    sc(o[0], o[1], o[2])

ORIGIN = {
1: ("""Where does this myth come from? Mostly from how slow the start feels. In the first year, fifty dollars
a week invested might earn only a little growth, so it really does look like it doesn't matter. The payoff
shows up years later, when you've stopped paying attention. Our brains judge a habit by what it does this
month, not what it does in twenty years. That's exactly why small amounts get ignored, and exactly why the
people who don't ignore them end up ahead.""", "Seedling growing timelapse", "SLOW START, BIG FINISH"),
2: ("""This myth comes from real pain. Many people watched their parents lose money in a crash, or lost money
themselves, and decided never again. That fear is understandable. But it swaps a visible risk, a crash, for
an invisible one, inflation. The answer isn't all cash or all stocks. It's matching each dollar to its job.
Money for emergencies and near term goals stays stable. Money for twenty years from now can take more
risk, because it has time to recover.""", "Worried man reading newspaper", "VISIBLE RISK VS INVISIBLE RISK"),
3: ("""Why do so many people believe it? Because for many families, the house really was the biggest pile of
wealth they ever had. But often that's because the mortgage forced them to save every month, not because
the house was a spectacular investment. The mortgage payment was automatic and non negotiable. That's the
real lesson. Forced, automatic saving works. You can get the same effect with automatic investing, without
putting everything into one property in one city.""", "Family in front of house", "THE FORCED SAVINGS EFFECT"),
4: ("""This myth is often repeated by people selling homes and mortgages, and by parents who bought decades
ago when prices relative to income were often lower. Renting has real advantages: flexibility to move for
a better job, no surprise repair bills, and a smaller upfront cost. Owning has its own: stability, control,
and a payment that doesn't rise with the market if your rate is fixed. Neither is automatically smarter. The
smartest choice is the one that fits your life and your numbers.""", "Moving truck boxes", "FLEXIBILITY VS STABILITY"),
5: ("""The myth survives partly because older generations often had pensions on top of Social Security,
guaranteed monthly checks from their employer for life. Today, far fewer private sector workers have a
traditional pension. Most have a four oh one k or nothing at all, which means the responsibility for the
gap moved from the employer to you. If your parents retired comfortably on Social Security plus a pension,
your plan probably needs to look different.""", "Factory workers vintage photo", "THE MISSING PENSION"),
6: ("""Refund season is also a big season for retailers, car dealers and travel companies, and they know
it. Ads land right when the money does. That's one reason refunds disappear so fast. A simple defense is
to decide the refund's job before it arrives, and move it there the same day it lands. The less time it
sits in checking, the less likely it is to be spent on something you won't remember by summer.""", "Shopping mall sale signs", "REFUND SEASON IS SALES SEASON"),
7: ("""This myth is fed by stories. Everybody has heard about someone who sold right before a crash. Fewer
people hear about the many who sold too early, or never got back in and missed the recovery. Being right
once makes a great story. Being right over and over, on both the exit and the re entry, is something
even many professionals struggle to do consistently. A boring schedule beats a brilliant guess most of
the time.""", "Fortune teller crystal ball", "STORIES VS STATISTICS"),
8: ("""Why do we believe it? Because when money is tight, more income really does help, and that feeling
sticks. We assume the relief scales forever. But spending has a way of rising to meet income. Researchers
call it lifestyle inflation. The people who escape it usually do one thing: they decide in advance where
new money goes, before they get used to having it. Income is fuel. Habits are the engine.""", "Fuel pump gas station", "INCOME IS FUEL, HABITS ARE THE ENGINE"),
9: ("""Part of this myth comes from what we can see. Visible wealth is often the flashy kind, new money
spending loudly. Quiet wealth is invisible by design. The teacher with a paid off house and a large
retirement account doesn't post about it. So our picture of rich people is skewed toward the ones who
show it, and those are often not the ones who keep it.""", "Quiet neighborhood street", "QUIET WEALTH IS INVISIBLE"),
10: ("""The myth often comes from bad budget experiences. Someone tried tracking every coffee in a
spreadsheet, felt guilty for a month, and quit. That's not a budget problem. That's a design problem. The
best budget is the one you barely notice: automatic savings, automatic bill payments, and a clear amount
you're free to spend without tracking every dollar. Less effort, more results.""", "Spreadsheet frustration", "DESIGN, NOT GUILT"),
11: ("""This myth has real costs at work. When nobody knows what anyone else earns, it's hard to tell if
you're underpaid, and harder to negotiate. In recent years, a number of states have passed pay
transparency laws requiring many employers to share salary ranges in job postings. That's a sign the
silence is breaking. Use it. Look up the posted ranges for your role before your next review.""", "Job posting on laptop", "KNOW YOUR RANGE"),
12: ("""Both versions of this myth are really the same thing: a reason to wait. Too young means not yet. Too
old means not anymore. Either way, the result is the same, no action. The fix is to make the first step
so small it's hard to say no. One percent of your paycheck. Twenty dollars a week. A single phone call to
your benefits office. Momentum matters more than size at the start.""", "First step on staircase", "MAKE THE FIRST STEP SMALL"),
13: ("""This myth survives because people confuse frugality with misery. Nobody wants to be the friend who
never pays their share. But real frugality looks generous on the outside. The frugal person can host
dinner at home, help a friend in trouble and give to causes they care about, because they're not spending
everything on things that don't matter to them.""", "Dinner party at home friends", "FRUGAL LOOKS GENEROUS"),
14: ("""The myth is strengthened every time a market crashes and the headlines scream. Drops of twenty or
thirty percent are scary, and they do happen. But the difference between a gambler and an owner is what
they do next. A gambler wants the money back fast. An owner keeps owning, keeps adding, and waits. Over
long periods, patience has historically been rewarded, though never guaranteed.""", "Patient fisherman lake", "OWNERS WAIT"),
15: ("""Where did this myth come from? It's a mix up. Using a credit card regularly and paying it on time
does help build credit history. Somewhere along the way, using a card turned into carrying a balance in
people's minds. They're not the same. You can use the card every month, pay it off completely, and get all
the benefits without paying a dollar of interest.""", "Paying bill online laptop", "USE IT, DON'T CARRY IT"),
16: ("""This myth comes from a half truth. Applying for lots of new credit in a short time can lower your
score a bit, because lenders may see it as a sign of risk. People heard credit checks hurt your score,
and lumped every check together. But checking your own report is not applying for anything. Many banks
and card apps now show your score for free, and looking at it is completely safe.""", "Banking app credit score", "LOOKING IS SAFE"),
17: ("""This myth comes from good instincts. Fewer cards can mean less temptation and less to track. For
some people that's worth it. The key is knowing the trade off. If you close a card, try to keep your
other balances low so your overall credit use stays healthy. And never close your oldest card right
before applying for a mortgage or car loan.""", "Mortgage application papers", "TIMING MATTERS"),
18: ("""This myth often comes from people who were badly burned by debt, and their caution makes sense. But
fear of all debt can lead to its own mistakes, like draining every dollar of savings to avoid a low rate
loan, leaving no cushion for emergencies. Being debt free is a great goal. Being debt free with zero
savings is fragile. Balance matters.""", "Balance scale weights", "DEBT FREE AND FRAGILE"),
19: ("""This myth hurts younger people the most. They wait to have a big amount before starting, and lose
the years when time is most powerful. The first investment isn't really about the money. It's about
learning. How to open an account, how to pick a low cost fund, how it feels when the balance drops. Better
to learn those lessons with one hundred dollars than with one hundred thousand.""", "Student with laptop", "LEARN WITH SMALL MONEY"),
20: ("""Part of this myth is marketing. Complexity sells. If investing looked simple, fewer people would pay
for help. Some of the most respected investors, including Warren Buffett, have said that for most people,
low cost index funds are a sensible choice. That doesn't mean advice is useless. It means simple is not the
same as amateur.""", "Simple tools on table", "SIMPLE IS NOT AMATEUR"),
}

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Most money mistakes don't come from bad luck. They come from bad ideas. Things you
heard from a parent, a coworker, a TV show, or a video like this one, that sounded true, and quietly cost
you thousands of dollars. Today, we're going to break twenty money myths that keep people poor.""")
short("This money myth is quietly costing you thousands")
card("""Twenty myths. Some are about math, some are about mindset, and some are about the everyday moves
people make with credit, debt and investing.""",
     {"type": "stat", "label": "money myths", "big": "20", "sub": "that keep people poor"})
sc("""Here's why myths are so dangerous. A bad habit you know is bad. You can work on it. A myth feels like
common sense. You don't question it, so you repeat it for years. And because money compounds, a small
wrong belief held for twenty years can cost far more than one big mistake.""",
   "Old books on shelf", "COMMON SENSE THAT ISN'T")
sc("""We'll go through them from three angles. Angle one, the numbers: myths that fall apart the moment you
do the math. Angle two, the psychology: myths about money and who you are. And angle three, the playbook:
myths about credit, debt and investing that change what you do this month.""",
   "Three doors hallway", "THREE ANGLES")
pr("""Some of these will surprise you. Number five, number eight and number fifteen surprise almost
everyone. Let's start with the numbers.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Every number here comes from a named source. Social Security figures come from the Social Security
Administration. Tax refund data comes from the IRS. Credit score guidance comes from the Consumer Financial
Protection Bureau. Growth examples use stated math, like a seven percent average yearly return. That's an
illustration, not a promise. This is education, not financial advice.""",
   "Social Security Administration building", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. Myths that fall apart with simple math.""")

item(1, "Small amounts don't matter", "the math says otherwise",
"""Myth number one. Small amounts don't matter.""",
"""This myth sounds reasonable. What's fifty dollars? It won't change my life. And on its own, one fifty
dollar decision doesn't. But money decisions aren't one time events. They repeat. Fifty dollars a week is
twenty six hundred dollars a year. And if that money is invested instead of spent, it doesn't just add up.
It compounds.""",
"""Picture two coworkers. One spends an extra fifty dollars a week on things she barely remembers. The
other invests it automatically. Neither feels richer or poorer week to week. But after twenty or thirty
years, the gap between them can be life changing. Try this: pick one small recurring expense and redirect
it to savings for ninety days. Watch the balance.""",
"Coins stacked growing", "$50 A WEEK = $2,600 A YEAR",
"Two coworkers office", "SAME WEEK, DIFFERENT FUTURE")
card("""Here's the math. About two hundred dollars a month, invested at a seven percent average yearly return,
for thirty years. You'd put in seventy two thousand dollars. Look where it could end up.""",
     {"type": "growth", "monthly": 200, "rate": 0.07, "years": 30})

item(2, "Cash is the safest place", "inflation is a slow leak",
"""Myth number two. Cash is the safest place for your money.""",
"""In the short term, cash is safe. It won't drop twenty percent in a month. That's exactly why it's
perfect for an emergency fund. But over decades, cash has a hidden enemy: inflation. Prices rise over time,
so the same dollar buys less. At three percent inflation, by the rule of seventy two, prices roughly double
in about twenty four years.""",
"""That means one hundred thousand dollars sitting in a zero interest account for twenty four years could
buy only about half of what it buys today. The balance looks the same. The value isn't. Cash is safe from
crashes, but not from time. Try this: keep your emergency fund in cash, ideally earning interest, and let
your long term money grow in investments that have historically beaten inflation over long periods.""",
"Dollar bills in safe", "SAFE FROM CRASHES, NOT FROM TIME",
"Grocery prices supermarket", "PRICES DOUBLE IN ~24 YEARS")

item(3, "Your house is your best investment", "a home is not a portfolio",
"""Myth number three. Your house is your best investment.""",
"""A home can be a great thing to own. It gives you stability, and paying down a mortgage builds equity.
But calling it your best investment ignores the costs. Property taxes, insurance, maintenance, repairs,
closing costs when you buy and sell. Many planners use a rule of thumb of setting aside around one to two
percent of a home's value each year just for upkeep.""",
"""And historically, home prices have grown more slowly than many people assume once you account for
inflation and all those costs, though it varies hugely by city and decade. The best way to see a home is
as a place to live that may also build wealth, not as your retirement plan. Try this: add up what your
home really costs you each year, beyond the mortgage. Taxes, insurance, repairs. Most people are
surprised.""",
"House with for sale sign", "A HOME IS NOT A PORTFOLIO",
"Roof repair workers", "1-2% A YEAR IN UPKEEP")

item(4, "Renting is throwing money away", "it depends on the math",
"""Myth number four. Renting is throwing money away.""",
"""Rent pays for a place to live. That's not throwing money away. It's buying shelter. Owners also pay for
things they never get back: mortgage interest, property taxes, insurance and maintenance. The real
question is not rent versus nothing. It's rent versus the unrecoverable costs of owning.""",
"""In some cities and some years, renting and investing the difference can come out ahead. In others,
buying wins, especially if you stay many years. It depends on prices, interest rates, how long you'll
stay, and whether you actually invest the difference. Try this: before buying, compare your rent with the
full monthly cost of owning, not just the mortgage. Then decide with numbers, not a slogan.""",
"Apartment building windows", "RENT BUYS SHELTER",
"Calculator with house keys", "COMPARE THE REAL COSTS")

item(5, "Social Security will cover retirement", "it was never designed to",
"""Myth number five. Social Security will cover your retirement.""",
"""This is one of the most expensive myths in America. According to the Social Security Administration,
for the average worker, retirement benefits replace only about forty percent of their earnings before
retirement. Most financial planners say people need considerably more than that to keep a similar
lifestyle.""",
"""Social Security is valuable. It's protected against inflation, and it lasts for life. But it was
designed as a foundation, not a full income. The gap has to come from somewhere: workplace plans, IRAs,
other savings, or working longer. Try this: create an account on the official Social Security website and
look at your estimated benefit. Then compare it with what you spend today.""",
"Social Security card", "ABOUT 40% OF YOUR PAY",
"Retired couple budget kitchen table", "MIND THE GAP")
card("""The Social Security Administration says benefits replace about forty percent of an average worker's
pre retirement earnings. The rest has to come from your own savings.""",
     {"type": "compare", "left": {"label": "Social Security", "big": "~40%", "sub": "average worker"},
      "right": {"label": "Your savings", "big": "the rest", "sub": "401(k), IRA, other"},
      "note": "Source: Social Security Administration"})

item(6, "The tax refund is free money", "it was always yours",
"""Myth number six. The tax refund is free money.""",
"""A tax refund feels like a bonus. But it's not a gift from the government. It's your own money, which
you overpaid during the year, coming back to you without interest. IRS data shows the average refund in
recent filing seasons has been around three thousand dollars. That's roughly two hundred fifty dollars a
month that people lent to the government for free.""",
"""For some people, a big refund works as forced savings, and that's okay. But if you're carrying credit
card debt at twenty percent while waiting for a refund, that's an expensive trade. Try this: if you get
a large refund every year, consider adjusting your withholding with your employer. Then send that extra
monthly money straight to debt or savings.""",
"Tax return forms", "YOUR MONEY, RETURNED",
"Paycheck stub calculator", "ADJUST YOUR WITHHOLDING")

item(7, "You can time the market", "almost nobody can",
"""Myth number seven. You can wait for the perfect moment to invest.""",
"""Waiting for the dip sounds smart. Buy low, sell high. The problem is that nobody knows when the dip
will come, how deep it will be, or when it ends. Many of the market's best days have historically come
very close to its worst days, during the scariest periods. If you're out waiting, you often miss both.""",
"""Studies of long term returns have repeatedly found that missing even a handful of the best days over
decades can sharply reduce your total return. Time in the market has generally beaten timing the market,
though no strategy is guaranteed. Try this: instead of waiting, invest a fixed amount on a fixed day every
month. It's called dollar cost averaging, and it removes the guessing.""",
"Stock market chart volatile", "NOBODY KNOWS WHEN",
"Calendar with payday marked", "SAME DAY EVERY MONTH")
pr("""That's the math myths. Now the harder ones. The myths that live in your head.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
pr("""Angle two. Myths about money and mindset. These are harder to see, because they feel like who you
are.""")
short("Why more money won't fix your money problems")

item(8, "More income will fix it", "income without habits leaks",
"""Myth number eight. More income will fix my money problems.""",
"""Higher income helps. But it doesn't fix habits, and history shows it. A well known study by economists
looking at professional football players found that roughly one in six filed for bankruptcy within about
twelve years of retiring, despite earning millions during their careers. Big income, no system.""",
"""You don't have to be a pro athlete to see it. Many people get a raise, and within a year, the extra
money has been absorbed by a nicer car, a bigger place and more dinners out. Their stress stays the same.
The fix is to build habits at your current income, so that when more money arrives, it has somewhere to go.
Try this: decide now what percent of your next raise goes to savings.""",
"American football stadium", "MILLIONS, THEN BANKRUPT",
"New car showroom", "THE RAISE DISAPPEARS")

item(9, "Rich people just got lucky", "luck helps, habits compound",
"""Myth number nine. Rich people just got lucky or inherited it.""",
"""Some did. Luck and family money are real. But researchers Thomas Stanley and William Danko, in their
book The Millionaire Next Door, found that most of the American millionaires they studied were first
generation wealthy. Many were business owners or professionals who lived below their means, drove
ordinary cars and invested steadily for decades.""",
"""This myth is dangerous because it makes effort feel pointless. If it's all luck, why try? But the
habits Stanley described are boring and available to most people. Spend less than you earn. Avoid
showing off. Invest consistently. Try this: next time you see someone with wealth, ask what habits might
be behind it, not just what luck.""",
"Ordinary suburban house", "THE MILLIONAIRE NEXT DOOR",
"Older man driving ordinary car", "BORING HABITS")

item(10, "Budgets are for broke people", "budgets are for free people",
"""Myth number ten. Budgets are for broke people.""",
"""Lots of people think a budget means deprivation. Counting every penny, never having fun. But a budget
is just a plan for your money before it arrives. Wealthy households and businesses budget all the time.
Without a plan, money tends to drift toward whatever is loudest this week.""",
"""A good budget can be very simple. One popular approach splits after tax income into needs, wants and
savings. Another just automates savings first and lets you spend the rest freely. The point isn't the
method. It's the decision. Try this: write three numbers. What you need each month, what you want to
save, and what's left for fun. That's a budget.""",
"Notebook budget planning", "A PLAN, NOT A PRISON",
"Friends having dinner restaurant", "FUN IS IN THE PLAN")

item(11, "Talking about money is rude", "silence protects bad deals",
"""Myth number eleven. Talking about money is rude.""",
"""Many families never talk about money. Kids grow up not knowing what things cost, how debt works, or how
their parents saved. Coworkers don't share salaries, so they don't know if they're underpaid. Couples avoid
the topic until it becomes a fight. Silence feels polite, but it mostly protects bad deals.""",
"""You don't need to announce your net worth at dinner. But talking openly with a partner, sharing salary
ranges with trusted coworkers, and teaching kids how money works can be worth a lot. Try this: have one
money conversation this week. With a partner, a friend or your kids. Keep it simple. What's one money
thing you wish you'd learned earlier?""",
"Family talking around table", "SILENCE IS EXPENSIVE",
"Parent teaching child with coins", "TEACH THE KIDS")

item(12, "I'm too young or too old", "the best time is now",
"""Myth number twelve. I'm too young to worry about it, or too old to start.""",
"""In your twenties, retirement feels like science fiction. But that's exactly when time is most
powerful. Money invested at twenty five has forty years to compound before sixty five. In your fifties, it
can feel too late. But you may have fifteen or more years of work left, your highest income, and extra
catch up contribution limits in retirement accounts.""",
"""Both ages have a superpower. The young have time. The older have income. The only real mistake is
waiting for a better age that never comes. Try this: if you're young, start with any amount and automate
it. If you're older, find out your current catch up contribution limits, and aim to save a bigger share of
each raise.""",
"Young graduate cap", "THE YOUNG HAVE TIME",
"Older professional at desk", "THE OLDER HAVE INCOME")

item(13, "Frugal means cheap", "spend on what matters",
"""Myth number thirteen. Being frugal means being cheap.""",
"""Cheap is buying the lowest price every time, even when it costs more later, or making other people pay
for you. Frugal is different. Frugal means spending deliberately. Cutting hard on things you don't care
about, so you can spend generously on the things you do.""",
"""A frugal person might drive a ten year old car and skip the latest phone, then spend happily on travel
with family. A cheap person buys shoes that fall apart in six months, then buys them again. Frugality is
about value, not price. Try this: list your top three priorities in life. Then look at your spending.
Does your money match the list?""",
"Old reliable car", "FRUGAL IS NOT CHEAP",
"Family travel vacation beach", "SPEND ON WHAT MATTERS")

item(14, "Investing is gambling", "owning is not betting",
"""Myth number fourteen. Investing is just gambling.""",
"""Gambling has a built in negative expected outcome for the player. The house wins over time. Owning a
broad, diversified slice of many businesses for decades is different. Companies produce goods, services
and profits, and over long periods broad markets have historically grown, though with painful drops along
the way.""",
"""That said, some things people call investing really are closer to gambling. Betting your savings on one
hot stock, trading options you don't understand, or chasing whatever went up last week. The difference is
time, diversification and cost. Try this: if you invest, ask three questions. How many companies do I own
through this? What does it cost per year? And can I hold it for ten years without touching it?""",
"Casino slot machines", "THE HOUSE WINS",
"Diverse businesses city street", "OWNING MANY BUSINESSES")

# ---------------- Mid ----------------
ch("A quick favor")
pr("""Quick pause. If one of these myths hit a little close to home, subscribe to the channel. It's free,
and it helps me keep making these videos. Now the last angle, the one that changes what you do this
month.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
pr("""Angle three. Myths about credit, debt and investing that change your next move.""")
short("Carrying a credit card balance does NOT build credit")

item(15, "Carry a balance to build credit", "pay in full, every month",
"""Myth number fifteen. You need to carry a credit card balance to build credit.""",
"""This one costs Americans a lot of money. You don't need to carry a balance and pay interest to build
credit. The Consumer Financial Protection Bureau explains that paying on time and keeping your balances low
compared with your limits are among the most important factors. Paying the full statement balance every
month shows you can handle credit, and costs nothing in interest.""",
"""Here's the difference in dollars. Carrying a two thousand dollar balance at twenty two percent costs
roughly four hundred forty dollars a year in interest, for zero benefit to your score. Paying in full
costs nothing. Try this: set your card to automatically pay the full statement balance each month. If you
can't yet, set it to pay well above the minimum.""",
"Credit card statement", "NO BALANCE NEEDED",
"Autopay setting phone", "PAY IN FULL")

item(16, "Checking your score hurts it", "soft checks are free",
"""Myth number sixteen. Checking your own credit score hurts it.""",
"""When you check your own credit, it's called a soft inquiry, and it doesn't affect your score. Hard
inquiries happen when a lender checks your credit because you applied for new credit, and those can have
a small, temporary effect. Looking at your own numbers is free and harmless.""",
"""People who avoid checking often miss errors. A wrong late payment, an account that isn't theirs, an
old debt reported twice. Mistakes on credit reports aren't rare, and fixing them can raise your score.
Try this: get your free reports from annual credit report dot com, the official site, and read every
line once a year.""",
"Credit report on laptop", "SOFT CHECKS DON'T HURT",
"Person reading report carefully", "CHECK FOR ERRORS")

item(17, "Close old cards to boost your score", "it can backfire",
"""Myth number seventeen. Closing old credit cards improves your score.""",
"""It feels responsible to close cards you don't use. But it can backfire. Your score looks at how much of
your available credit you're using. Close a card, and your available credit drops, so the same balance
suddenly looks bigger. Older accounts can also help the average age of your credit history.""",
"""If an old card has no annual fee and doesn't tempt you to spend, it's often fine to keep it open and
use it for a small purchase now and then. If it has a high annual fee or it really tempts you, closing it
may still be the right call. Try this: before closing any card, check its fee and your total credit
use, and decide with both.""",
"Scissors cutting credit card", "CLOSING CAN BACKFIRE",
"Wallet with few cards", "KEEP THE OLD, NO FEE CARD")

item(18, "All debt is bad", "rate and purpose matter",
"""Myth number eighteen. All debt is bad.""",
"""Debt is a tool. A low rate mortgage on a home you can afford, a reasonable student loan for a degree
that raises your income, or a business loan with a clear plan can make sense. Credit card debt at twenty
percent for things that lose value is a very different thing. The interest rate, and what the money buys,
decide whether debt helps or hurts.""",
"""A simple test. Does this debt help me earn more, or own something that holds value, at a reasonable
rate I can comfortably pay? If yes, it might be useful. If it's for something that's gone in a month, at
a high rate, it's usually a trap. Try this: label every debt you have as tool or trap. Pay off the traps
first.""",
"Hammer and tools workbench", "A TOOL OR A TRAP",
"Graduation ceremony", "DEBT WITH A PURPOSE")

item(19, "You need a lot to start investing", "start with what you have",
"""Myth number nineteen. You need a lot of money to start investing.""",
"""Decades ago, investing often required large minimums and expensive commissions. Today, many
brokerages have no minimum to open an account and offer fractional shares, so you can buy a slice of a fund
with a small amount. Many workplace retirement plans let you contribute a small percent of each
paycheck.""",
"""Starting small isn't just possible. It's smart. It builds the habit and teaches you how markets feel
when they move, while the stakes are low. Try this: if your employer offers a retirement plan with a
match, contribute at least enough to get the full match. That match is part of your pay.""",
"Smartphone investing app", "NO BIG MINIMUM",
"Paycheck and retirement plan form", "GET THE MATCH")

item(20, "You need an expert to begin", "simple beats complex",
"""Myth number twenty. You need a financial expert before you can start.""",
"""Good advice can be valuable, especially for complex situations like a business, an inheritance or
taxes. But the basics don't require an expert. An emergency fund, no high interest debt, and steady
contributions to low cost diversified funds is a plan many people can run on their own.""",
"""If you do hire help, know how they're paid. Ask whether they're a fiduciary, meaning legally required
to act in your best interest. Ask about every fee, in dollars. Try this: write a one page plan for
yourself. What you're saving for, how much each month, and where it goes. If you can't fill it in, that's
when an hour with a fee only advisor might be worth it.""",
"Financial advisor meeting", "SIMPLE BEATS COMPLEX",
"One page plan notebook", "YOUR ONE PAGE PLAN")

# ---------------- Replacement rules ----------------
ch("Ten rules to replace the myths")
pr("""Breaking a myth isn't enough. You need something to replace it. So here are ten simple rules to live
by instead.""")
short("10 money rules that replace the biggest myths")
sc("""Rule one. Small amounts, repeated and invested, are how most people build wealth. Rule two. Cash for
emergencies, investments for the long term. Rule three. Your home is a place to live first. Rule four.
Compare the full costs of renting and owning before you decide.""",
   "Notebook with written rules", "RULES 1 TO 4")
sc("""Rule five. Plan for Social Security to be part of your retirement, not all of it. Rule six. A big tax
refund is a loan you gave for free. Rule seven. Invest on a schedule, not on a feeling.""",
   "Calendar planner pen", "RULES 5 TO 7")
sc("""Rule eight. Build the habit before the income. Rule nine. Pay your cards in full and check your
credit every year. And rule ten. Keep it simple, keep it cheap, and keep going for a very long time.""",
   "Road stretching into distance", "RULES 8 TO 10")

# ---------------- Stories ----------------
ch("How myths cost real money")
sc("""Let's put a price on a few of these myths with simple examples. Take Kevin. He believed small
amounts don't matter, so for ten years he never started investing. When he finally began at thirty five,
he had to save much more each month to reach the same goal as a friend who started at twenty five with
less. The myth didn't feel expensive. It cost him a decade of compounding.""",
   "Man looking at old photos", "KEVIN: THE LOST DECADE")
sc("""Then there's Priya. She thought carrying a small balance helped her credit, so she always left a few
hundred dollars on her card. Over five years, she paid hundreds of dollars in interest for nothing. When
she switched to paying in full, her score kept improving, and her interest dropped to zero.""",
   "Woman using credit card online", "PRIYA: INTEREST FOR NOTHING")
sc("""And Tom and Rachel believed renting was throwing money away. They stretched to buy a house at the top
of their budget. Between taxes, insurance and a roof repair in year two, they had no cushion left, and
put the repairs on credit cards. Owning wasn't the mistake. Buying with no margin was. A few years later,
after building savings back up, they were glad they owned. The order mattered.""",
   "Couple in front of new home", "TOM AND RACHEL: NO MARGIN")
sc("""Notice the pattern. None of these people were careless. They were following advice that sounded
right. That's what makes myths so expensive. The fix is simple: whenever you hear a money rule, ask for
the math behind it.""",
   "Magnifying glass on document", "ASK FOR THE MATH")

# ---------------- FAQ ----------------
ch("Questions people ask")
pr("""A few questions people ask me about these myths.""")
sc("""Question one. Where do money myths come from? Mostly from good intentions. Parents repeat what worked
for them, in a different economy. Salespeople repeat what helps them sell. And social media rewards bold,
simple claims over careful ones. The best defense is checking a claim against a neutral source, like a
government agency or an independent nonprofit.""",
   "Grandparents with grandchildren", "WHERE MYTHS COME FROM")
sc("""Question two. Is it ever smart to keep a lot of cash? Yes. Your emergency fund should be in cash. And
money you'll need in the next few years, like a down payment, usually belongs somewhere stable too. The
myth isn't that cash is bad. It's that cash is the best place for long term money.""",
   "Savings account interest rates", "WHEN CASH IS SMART")
sc("""Question three. If renting can be fine, when does buying make sense? Generally when you plan to stay
for many years, you have a solid emergency fund after the down payment, and the full monthly cost of
owning fits comfortably in your budget. Many people use online rent versus buy calculators to compare
the numbers for their own city.""",
   "Neighborhood houses aerial", "WHEN TO BUY")
sc("""Question four. Is it bad to get a tax refund at all? No. A small refund is normal, because exact
withholding is hard. The issue is a very large refund every year while you carry high interest debt.
That's money working for the government instead of for you.""",
   "IRS tax forms desk", "IS A REFUND BAD?")
sc("""And question five. What's the single most expensive myth on this list? For most people, it's number
five. Assuming Social Security will cover retirement leads to saving too little, too late. The second
most expensive is probably number one, believing small amounts don't matter, because it delays the start.
And in personal finance, the start is everything.""",
   "Retirement planning documents", "THE MOST EXPENSIVE MYTH")
sc("""One last thought on myths. Not every piece of old advice is wrong. Spend less than you earn. Avoid
debt you can't afford. Save for a rainy day. Those are old, and they're true. The skill isn't rejecting
everything you were told. It's keeping the advice that survives the math, and dropping the rest.""",
   "Old and new books stacked", "KEEP WHAT SURVIVES THE MATH")

# ---------------- Recap ----------------
ch("Recap: all 20 myths")
short("20 money myths that keep you poor")
sc("""Quick recap. The math myths: small amounts don't matter, cash is safest, your house is your best
investment, renting is throwing money away, Social Security will cover you, the tax refund is free money,
and you can time the market.""",
   "Checklist clipboard", "THE MATH MYTHS")
sc("""The mindset myths: more income will fix it, rich people just got lucky, budgets are for broke people,
talking about money is rude, you're too young or too old, frugal means cheap, and investing is gambling.""",
   "Brain thinking illustration", "THE MINDSET MYTHS")
sc("""And the playbook myths: carry a balance to build credit, checking your score hurts it, close old cards,
all debt is bad, you need a lot to start investing, and you need an expert before you begin.""",
   "Credit cards and notebook", "THE PLAYBOOK MYTHS")

# ---------------- Close ----------------
ch("What to do next")
pr("""If you want the full plan without the myths, from broke to your first million, it's in my playbook.
The link is in the description. And if you haven't seen it yet, watch my video on why most people stay
broke. It pairs perfectly with this one. I'm Ryan Rover. See you in the next one.""")

save("video42", "20 Money Myths That Keep You Poor", [
    "Social Security Administration: benefits replace about 40% of an average worker's pre-retirement earnings",
    "IRS Filing Season Statistics (average refund around $3,000 in recent seasons)",
    "Consumer Financial Protection Bureau: credit scores, soft vs hard inquiries, credit utilization; AnnualCreditReport.com",
    "Carlson, Kim, Lusardi and Camerer, Bankruptcy Rates among NFL Players with Short-Lived Income Spikes (NBER, 2015)",
    "Thomas J. Stanley and William D. Danko, The Millionaire Next Door (1996)",
    "Rule of 72, inflation and growth figures: stated illustrative math",
], "20 money myths: numbers, psychology, playbook")
