import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short


def danger(n, title, sub, card_text, what, why, fix, q1, c1, q2, c2, q3, c3):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"DANGER {n}")
    sc(what, q1, c1)
    sc(why, q2, c2)
    sc(fix, q3, c3)

# ---------------- Intro ----------------
ch("Intro")
short("Fifty thousand dollars is the most dangerous amount of money you can have. Here's why.")
pr("""Hi, I'm Ryan Rover. Here's a strange idea. Fifty thousand dollars might be the most dangerous amount of money you
can have. Not because it's a lot. Because it's just enough to feel rich, and not nearly enough to actually be rich. And
that gap, between how it feels and what it really is, is where a lot of people lose years of progress.""")
card("""Fifty thousand dollars. Enough to buy a new truck in cash. Enough for a down payment. Enough to quit your job for a
while. And that's exactly the problem.""",
     {"type": "stat", "label": "the danger zone", "big": "$50,000", "sub": "feels rich, isn't rich yet"})
sc("""Think about what fifty thousand dollars looks like in your account. For most people, it's more money than they've ever
had in one place. It feels like you've made it. And suddenly, every salesperson, every friend with a business idea, and
every voice in your own head has a suggestion for what to do with it.""",
   "Bank building United States", "IT FEELS LIKE YOU MADE IT")
sc("""But here's the reality check. Using the four percent rule of thumb, fifty thousand dollars invested could support about
two thousand dollars a year. That's less than two hundred dollars a month. It's a fantastic start. It's a terrible finish
line. In this video, fifteen dangers that hit people right around this level, and how to walk past every one of them.""",
   "Calculator with financial charts", "$50K = ~$2,000 A YEAR")
sc("""We'll also look at the whole thing from three angles. The numbers: what fifty thousand can really become if you protect
it. The psychology: why this amount messes with your head. And the playbook: exactly what to do with fifty thousand dollars
so it turns into five hundred thousand instead of zero.""",
   "Map and compass", "3 ANGLES, 15 DANGERS")
pr("""First, the numbers, because they show you exactly what's at stake.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Household wealth figures come from the Federal Reserve's Survey of Consumer Finances. Car price and payment data comes
from Edmunds and Kelley Blue Book. Fraud data comes from the Federal Trade Commission and the Federal Reserve. Growth examples
use a seven percent average yearly return as an illustration, which is not a promise. Markets go up and down. This video is
education, not financial advice.""",
   "Federal Reserve Bank building columns", "OUR SOURCES")

# ---------------- Angle 1: numbers ----------------
ch("Angle 1: The numbers")
pr("""Angle one. The numbers. What could fifty thousand dollars become if you just leave it alone?""")
card("""At a seven percent illustration, fifty thousand dollars with nothing added grows to roughly one hundred thousand in ten
years, about two hundred thousand in twenty years, and about four hundred six thousand in thirty years.""",
     {"type": "compare", "left": {"label": "Today", "big": "$50,000", "sub": "nothing added"},
      "right": {"label": "In 30 years", "big": "~$406,000", "sub": "at 7% a year"},
      "note": "Illustration, compounded monthly. Returns are not guaranteed."})
sc("""Read that again. Fifty thousand dollars, untouched, could become around four hundred thousand dollars in thirty years. So
when someone spends fifty thousand dollars on a new truck at thirty five, the real cost isn't fifty thousand. It's the four
hundred thousand that money could have become by sixty five. That's what economists call opportunity cost, and at this level
it's enormous.""",
   "Pickup truck parked", "THE REAL COST")
card("""And if you keep adding, it gets much bigger. Fifty thousand dollars plus five hundred dollars a month, at the same seven
percent illustration, reaches roughly one million dollars in about thirty years.""",
     {"type": "compare", "left": {"label": "Start", "big": "$50,000", "sub": "+ $500 a month"},
      "right": {"label": "About 30 years", "big": "~$1,000,000", "sub": "at 7% a year"},
      "note": "Illustration, compounded monthly. Returns are not guaranteed."})
sc("""This is why fifty thousand is such a pivotal number. You're far enough along that compounding has real material to work
with. You've proven you can save. And if you keep going, a million dollars is no longer a fantasy. It's a timeline. But if
you spend it, you go back to the start, and the hardest part of the climb begins again.""",
   "Mountain climber reaching summit", "A MILLION IS A TIMELINE")
sc("""Where does fifty thousand put you? The Federal Reserve's Survey of Consumer Finances found the median net worth of
families under thirty five was about thirty nine thousand dollars in twenty twenty two. So if you're young and you have fifty
thousand dollars, you're already above the middle for your age group. You're doing something right. The goal now is not to
undo it.""",
   "Young people graduation", "ABOVE THE MEDIAN")
sc("""There's one more number that makes this level special. At fifty thousand dollars, a normal year in the market can move your
balance by thousands of dollars, up or down. A ten percent drop is five thousand dollars gone on paper. A good year can add the same.
For the first time, the market's mood can swing your account by more than you save in a month or two. That's thrilling and
terrifying, and it's one of the reasons people make emotional decisions right around here.""",
   "Stock market chart falling on screen", "$5,000 SWINGS")
sc("""The way to handle those swings is to zoom out. A single year doesn't matter much on a thirty year journey. What matters is that
you stay invested, keep adding money, and give compounding the time it needs. If daily or weekly swings make you nervous, check your
balance less often. Once a month is plenty. Once a quarter is even better.""",
   "Calendar planning", "ZOOM OUT")
pr("""So what are the dangers? Here are fifteen of them. The first one is the most common, and it has four wheels.""")

# ---------------- Dangers ----------------
danger(1, "The new car", "the fastest way to lose $50,000",
"""Danger number one. The new car.""",
"""Kelley Blue Book has reported average new vehicle transaction prices around forty eight to fifty thousand dollars in recent
years. In other words, the average new car costs roughly the entire balance we're talking about. And when you have fifty
thousand in the bank, buying one in cash, or with a big down payment, feels responsible.""",
"""But cars lose value fast. Many new cars lose a large share of their value in the first few years. So you trade fifty thousand
dollars of money that could grow into hundreds of thousands, for an asset that shrinks every month. And you'll pay insurance,
registration and maintenance on top.""",
"""The fix: if your current car runs well, keep it. When you do need one, a reliable used car that's a few years old lets
someone else absorb the steepest drop in value. Set a rule, like never spending more than a fraction of your yearly income on
a vehicle. Your fifty thousand stays invested and keeps working.""",
"Car dealership lot", "~$50K AVERAGE NEW CAR",
"Old car parked on street", "CARS SHRINK",
"Car with for sale sign", "BUY USED, KEEP IT LONG")

danger(2, "The house you can't afford yet", "a down payment is not a budget",
"""Danger number two. Rushing into a house that's too expensive.""",
"""Fifty thousand dollars looks like a perfect down payment. And for some people, at the right price, it is. But many buyers
use every dollar for the down payment and closing costs, then move in with no emergency fund at all. The first broken water
heater goes straight on a credit card.""",
"""A house also comes with costs the mortgage payment doesn't show: property taxes, insurance, maintenance and repairs. A
common rule of thumb is to budget one to two percent of the home's value every year just for maintenance. On a four hundred
thousand dollar home, that could be four to eight thousand dollars a year.""",
"""The fix: before buying, keep a separate emergency fund that survives the purchase, ideally three to six months of expenses.
Make sure the total monthly cost, including taxes and insurance, fits comfortably in your budget. A slightly cheaper house with
a cushion beats a dream house with nothing left.""",
"House with for sale sign", "DON'T EMPTY THE ACCOUNT",
"House repair roof", "HIDDEN HOUSE COSTS",
"Suburban houses street United States", "KEEP A CUSHION")

danger(3, "Lifestyle creep", "the slow leak",
"""Danger number three. Lifestyle creep.""",
"""When you have fifty thousand dollars, small upgrades feel easy. A nicer apartment. A gym with a pool. More restaurants. Better
vacations. None of them looks dangerous on its own. But each one raises your monthly costs, and higher monthly costs mean less
saving, forever.""",
"""Here's the hidden math. Every extra one hundred dollars a month you spend, permanently, is about twelve hundred dollars a
year that's not being invested. Over thirty years at a seven percent illustration, one hundred dollars a month could have grown
to roughly one hundred twenty two thousand dollars. A few small upgrades can quietly cost hundreds of thousands.""",
"""The fix: upgrade on purpose. Choose the one or two things that genuinely make your life better, and enjoy them without guilt.
Keep everything else the same. And whenever you increase a monthly cost, ask how much it adds up to over thirty years.""",
"Luxury car dealership", "SMALL UPGRADES",
"Calculator and pen on financial papers", "$100/MO = ~$122K",
"Person smiling at laptop", "UPGRADE ON PURPOSE")

short("The moment you have fifty thousand dollars, everyone has a hot tip for you.")
danger(4, "The hot investment tip", "fast money, fast losses",
"""Danger number four. The hot investment tip.""",
"""Once people know you have money, tips start arriving. A stock that's about to explode. A crypto coin that went up five times
last month. A friend who made a fortune on options. With fifty thousand dollars, it's tempting to try to turn it into five
hundred thousand overnight.""",
"""But concentrated bets are how people lose big. A single stock can fall eighty or ninety percent and never recover. Many
speculative coins have collapsed. And research on active trading, like work by economists Brad Barber and Terrance Odean, has
found that individual investors who trade the most tend to earn less than those who trade the least.""",
"""The fix: keep the core of your money in broad, low cost, diversified funds. If you really want to speculate, limit it to a
small amount you could lose completely without changing your life, maybe a few percent. That way, curiosity doesn't become a
catastrophe.""",
"Stock market chart on screen", "THE HOT TIP",
"Stock market crash newspaper", "TRADERS EARN LESS",
"Pie chart on paper", "KEEP SPECULATION SMALL")

danger(5, "Leaving it all in cash", "the quiet danger",
"""Danger number five. Leaving all of it in cash forever.""",
"""This one is the opposite of the hot tip. Some people get to fifty thousand and are so afraid of losing it that they never
invest at all. It sits in a checking account earning nearly nothing, year after year.""",
"""The problem is inflation. At three percent inflation, money loses about a quarter of its buying power in roughly ten years.
So fifty thousand dollars sitting in a zero interest account for a decade might only buy what thirty seven thousand buys today.
Playing it too safe is its own kind of risk.""",
"""The fix: decide how much you need as an emergency fund, and keep that in a high yield savings account. Then invest the rest
for the long term, gradually if that feels better, in a diversified mix that matches your timeline and your stomach for ups and
downs.""",
"Bank vault door", "TOO SAFE IS RISKY",
"Grocery store shelves prices", "INFLATION EATS CASH",
"Graph trending upward", "INVEST THE REST")

danger(6, "The friend's business idea", "love and money don't mix well",
"""Danger number six. Investing in a friend's or relative's business.""",
"""Your cousin is opening a restaurant. Your friend has an app idea. They need twenty thousand dollars to get started, and you
have fifty. Saying no feels selfish. Saying yes feels generous. But small businesses are risky, and a large share don't survive
their first several years, according to Bureau of Labor Statistics data on business survival.""",
"""And when money and relationships mix, you can lose both. If the business struggles, you may feel resentful, and they may feel
pressured or ashamed. Some families and friendships never fully recover from a failed investment.""",
"""The fix: if you want to help, decide on an amount you'd be comfortable treating as a gift, not a loan. Put any real investment
in writing, with clear terms. And never invest money you need for your own safety net or retirement.""",
"Small business storefront", "A FRIEND'S BUSINESS",
"Friends talking coffee", "LOVE AND MONEY",
"Paperwork documents desk", "PUT IT IN WRITING")

danger(7, "Quitting too early", "freedom that runs out",
"""Danger number seven. Quitting your job because you finally have money.""",
"""Fifty thousand dollars feels like freedom. And for some people, a planned break, a career change or a business launch is
exactly right. But many people quit without a plan, assuming the money will last. Spending four thousand dollars a month, fifty
thousand lasts about one year. Add health insurance, and it goes faster.""",
"""And when the money's gone, people often return to work in a worse position, with no savings and a gap on their resume. The
fifty thousand that could have grown for decades is gone, and they're back at zero.""",
"""The fix: if you want to leave, make a plan first. How many months will you fund? What's the goal, a new job, a business, a
degree? What's the plan if it doesn't work out? Keep part of your money invested and untouchable, so a break doesn't erase your
progress.""",
"Office building at dusk", "QUITTING WITHOUT A PLAN",
"Calendar planning", "$50K = ~1 YEAR OF SPENDING",
"Person writing list notebook", "MAKE A PLAN FIRST")

pr("""Quick pause. If you're near fifty thousand, or on your way there, subscribe to the channel. I'm building a full series on
every money level, from the first dollar to one million, and new videos come out every couple of days. Okay, danger number eight.""")

danger(8, "Scams", "you just became a target",
"""Danger number eight. Scams.""",
"""The Federal Trade Commission has reported that consumers lost more than twelve billion dollars to fraud in twenty twenty four,
with investment scams among the costliest categories. And the more money you have, the more attractive you are to scammers.""",
"""Modern scams are sophisticated. Fake investment platforms that show impressive gains, until you try to withdraw. Romance scams
that build trust for months. Calls pretending to be your bank, asking you to move money to a safe account. People who are smart
and careful still fall for them.""",
"""The fix: never move money because someone contacted you and created urgency. Hang up and call your bank using the number on
your card. Be suspicious of any investment promising high returns with little risk. And talk to someone you trust before any
large transfer.""",
"Computer hacker keyboard", "YOU'RE A TARGET",
"Phone call customer service", "URGENCY IS A RED FLAG",
"Bank building United States", "HANG UP AND CALL BACK")

danger(9, "Overconfidence", "you did it once, so you can't lose",
"""Danger number nine. Overconfidence.""",
"""Reaching fifty thousand dollars takes discipline, and it's natural to feel proud. But pride can turn into overconfidence. People
start believing they have a special talent for money. They take bigger risks, trade more often, or put money into things they
don't fully understand.""",
"""Behavioral finance research has found that overconfident investors tend to trade too much and diversify too little, both of
which can hurt returns. Getting to fifty thousand was mostly about saving consistently. Growing it to five hundred thousand is
mostly about not interrupting compounding.""",
"""The fix: remember what got you here. Consistent saving, spending less than you earn, and patience. Write your investment plan
down while you're calm, including what you'll do in a market crash, and follow it when you're not.""",
"Chess game", "OVERCONFIDENCE",
"Stock market chart falling on screen", "TRADING TOO MUCH",
"Notebook with financial notes", "WRITE THE PLAN DOWN")

danger(10, "The wrong advisor", "fees that eat growth",
"""Danger number ten. The wrong financial advisor.""",
"""At fifty thousand dollars, you start getting attention from people selling financial products. Some are excellent, and some
are paid by commission on what they sell, which can create conflicts of interest. High fee products can quietly eat a large
part of your growth over decades.""",
"""A one percent yearly fee doesn't sound like much. But over thirty years, the difference between paying one percent and paying a
small fraction of a percent can add up to tens of thousands of dollars, even on a fifty thousand dollar starting balance, because
fees compound just like returns.""",
"""The fix: ask any advisor how they're paid, in writing. Look for fee only advisors who are fiduciaries, meaning they're
required to act in your best interest. And compare costs in dollars per year, not just percentages.""",
"Business meeting handshake", "HOW ARE THEY PAID?",
"Receipt and coins on table", "FEES COMPOUND TOO",
"Paperwork documents desk", "ASK IN WRITING")

danger(11, "Lending money", "the loan that becomes a gift",
"""Danger number eleven. Lending money to people you know.""",
"""When family and friends know you have money, requests come in. Rent help, a car repair, a medical bill, a fresh start. Many of
these are real needs, and wanting to help is a good thing. But informal loans often don't get paid back, and asking for repayment
can damage relationships.""",
"""Every loan that becomes an unplanned gift is money that won't grow for your future. And once word gets around that you lend
money, requests tend to multiply.""",
"""The fix: decide on a yearly helping budget, an amount you can give without hurting your plan. When you help, consider it a gift,
not a loan. That way, if it comes back, it's a pleasant surprise. If it doesn't, the relationship survives.""",
"Family dinner table", "THE FAMILY LOAN",
"Friends talking coffee", "REQUESTS MULTIPLY",
"Gift box present", "GIVE, DON'T LEND")

danger(12, "No emergency fund", "all your eggs in one basket",
"""Danger number twelve. Having everything invested and no emergency fund.""",
"""Some people invest every dollar of their fifty thousand, and keep nothing in cash. Then a job loss or a big bill arrives during a
market crash, and they're forced to sell investments at a loss. That turns a temporary drop into a permanent one.""",
"""Market declines often arrive at the same time as layoffs, because both happen during recessions. That's exactly when you're most
likely to need cash, and exactly when selling investments hurts the most.""",
"""The fix: split your money by job. Three to six months of essential expenses in a high yield savings account. The rest invested
for the long term. That way, emergencies never force you to sell at the worst possible moment.""",
"Stock market crash newspaper", "FORCED TO SELL",
"Office building at dusk", "LAYOFFS AND CRASHES",
"Piggy bank coins", "SPLIT BY JOB")

danger(13, "Paying off cheap debt first", "the wrong order",
"""Danger number thirteen. Using your fifty thousand to pay off cheap debt while ignoring better options.""",
"""Paying off debt feels great, and high interest debt should usually go first. But some people use all their savings to pay off
low interest debt, like a mortgage or a car loan at a low rate, and leave themselves with no cushion and no investments.""",
"""If your mortgage rate is low and your emergency fund is empty, paying it off early might make you less safe, not more. You can't
easily get that money back out of your house in an emergency.""",
"""The fix: pay off high interest debt first, especially credit cards. Keep a solid emergency fund. Get your full employer match.
Then decide about low interest debt, based on your rate, your goals, and how you feel about debt. Order matters.""",
"Credit card bills on table", "WRONG ORDER",
"House with for sale sign", "MONEY STUCK IN A HOUSE",
"Staircase steps", "ORDER MATTERS")

danger(14, "Ignoring taxes", "where you hold money matters",
"""Danger number fourteen. Ignoring taxes.""",
"""If your fifty thousand dollars sits in a regular taxable account, interest and some gains may be taxed every year. If you're not
using tax advantaged accounts, like a 401k, an IRA or a health savings account where eligible, you may be paying more tax than you
need to.""",
"""And selling investments in a regular account can create capital gains taxes. Short term gains, on things held a year or less,
are usually taxed at higher rates than long term gains. Frequent trading can quietly raise your tax bill.""",
"""The fix: use tax advantaged accounts first, within the current IRS limits. Hold long term investments for more than a year
when it makes sense. And consider talking to a tax professional once, to make sure your money is in the right buckets.""",
"Tax forms on desk", "TAXES MATTER",
"Calendar planning", "LONG TERM VS SHORT TERM",
"Paperwork documents desk", "THE RIGHT BUCKETS")

danger(15, "Stopping too soon", "the biggest danger of all",
"""Danger number fifteen. The biggest one. Stopping.""",
"""Many people reach fifty thousand dollars, feel safe, and stop pushing. They lower their contributions. They stop tracking. They
coast. And because fifty thousand feels like a lot, they don't notice that they've stalled.""",
"""But the difference between stopping and continuing is huge. Fifty thousand left alone might become about four hundred thousand in
thirty years at a seven percent illustration. Fifty thousand plus five hundred a month might become about one million. Keeping the
habit going is worth more than half a million dollars.""",
"""The fix: set the next goal before you reach the current one. When you hit fifty thousand, you should already be aiming for one
hundred thousand. Keep your automatic contributions running, and raise them every time your income goes up.""",
"Person relaxing on couch", "DON'T COAST",
"Graph trending upward", "THE HABIT IS WORTH $600K",
"Mountain climber reaching summit", "SET THE NEXT GOAL")

# ---------------- Three people ----------------
short("Three people had fifty thousand dollars. Ten years later, one had zero.")
ch("Three people, $50,000 each")
pr("""Let's see these dangers play out. Three example people, each with fifty thousand dollars at age thirty two. They're made
up, but each path is one that real people take every day.""")
sc("""Person one, Ethan. Ethan has fifty thousand dollars and a car that runs fine but feels old. He buys a new truck for forty
eight thousand, pays cash, and feels great. Over the next few years, he upgrades his apartment and takes a couple of expensive
trips. He keeps saving a little, but there's no plan. Ten years later, the truck is worth a fraction of what he paid, and Ethan's
savings are around fifteen thousand dollars. He's forty two and almost back where he started.""",
   "Pickup truck parked", "ETHAN: THE TRUCK")
sc("""Person two, Sofia. Sofia was so nervous about losing her fifty thousand that she left it in her checking account. She kept
saving, adding three hundred dollars a month, all in cash. Ten years later, she has about eighty six thousand dollars. That sounds
good, but inflation has eaten a large part of its buying power, and she missed a decade of potential growth. She's safe, but she's
falling behind without realizing it.""",
   "Bank vault door", "SOFIA: TOO SAFE")
sc("""Person three, Marcus. Marcus keeps his old car. He sets aside fifteen thousand as an emergency fund in a high yield account,
and invests the other thirty five thousand in low cost index funds. He adds five hundred dollars a month, automatically. He ignores
the hot tips, says no to a friend's restaurant idea, and keeps going through a market drop. At a seven percent illustration, his
investments could be around one hundred fifty seven thousand dollars after ten years, plus his emergency fund.""",
   "Young man working on laptop", "MARCUS: THE PLAN")
sc("""Same starting point. Same age. Ten years later, Ethan has about fifteen thousand, Sofia about eighty six thousand, and Marcus
around one hundred seventy thousand, counting his cushion. And the gap keeps widening every year after that. Nobody in this story
did anything crazy. Ethan bought a truck. Sofia was careful. Marcus was boring. Boring won.""",
   "Three people silhouettes", "BORING WON")

# ---------------- Scenarios ----------------
ch("What $50,000 can become")
pr("""Now let's put some numbers on the choices. Here's what fifty thousand dollars could become over thirty years, depending on
what you do next. All of these use simple illustrations, not promises.""")
sc("""Scenario one. Spend it. A car, a wedding, a renovation. In thirty years, that fifty thousand is worth nothing financially,
though you may have memories or a nicer kitchen. Sometimes that's a fine choice. Just make it knowingly. Scenario two. Leave it in
cash at no interest. Thanks to inflation, its buying power in thirty years could be less than half of what it is today.""",
   "Shopping bags mall", "SPEND IT OR SIT ON IT")
sc("""Scenario three. Invest it and never add another dollar. At seven percent, roughly four hundred six thousand dollars in thirty
years. Scenario four. Invest it and add five hundred a month. Roughly one million dollars. Scenario five. Invest it and add one
thousand a month. Roughly one point six million dollars. Same fifty thousand. Wildly different futures.""",
   "Graph trending upward", "INVEST AND KEEP GOING")
sc("""The lesson isn't that you can never spend money. It's that at fifty thousand, every big decision has a long shadow. A forty
thousand dollar purchase today isn't a forty thousand dollar decision. Over thirty years, it could be a three hundred thousand dollar
decision. Knowing that doesn't mean saying no to everything. It means saying yes only to the things that are truly worth it.""",
   "Hourglass sand timer", "EVERY DECISION HAS A SHADOW")

# ---------------- Angle 2: psychology ----------------
short("Why does fifty thousand dollars make smart people do dumb things?")
ch("Angle 2: The psychology")
pr("""Angle two. The psychology. Why is fifty thousand dollars so dangerous for our brains specifically?""")
sc("""The first reason is what psychologists call the wealth effect. When people feel richer, they tend to spend more, even if their
income hasn't changed. Seeing a big number in your account makes larger purchases feel safe. That feeling is real, but it's
misleading, because fifty thousand dollars is not a lot of yearly income.""",
   "Person looking at laptop calm", "THE WEALTH EFFECT")
sc("""The second reason is mental accounting, an idea from economist Richard Thaler. We treat money differently depending on where
it came from and what bucket we put it in. A bonus or a tax refund feels like fun money. A savings balance that's grown big feels
like it's allowed to be spent. But money is money. A dollar from a bonus grows just as well as a dollar from your paycheck.""",
   "Jars with labels", "MENTAL ACCOUNTING")
sc("""The third reason is that fifty thousand is just big enough to buy something big. Ten thousand dollars can't buy a new truck or a
house. A million dollars is so much that one purchase doesn't make a dent. But fifty thousand is right at the size of a single
life changing purchase. That makes the temptation stronger than at almost any other level.""",
   "Pickup truck parked", "BIG ENOUGH TO SPEND")
sc("""The fourth reason is the end of urgency. Before fifty thousand, many people were saving out of fear. Fear of emergencies, fear
of debt. Once they have a cushion, the fear goes away, and so does the motivation. That's why it's so important to replace fear
with a goal. Not, I need money. But, I want to be financially independent by fifty five.""",
   "Road sign highway", "FROM FEAR TO A GOAL")
sc("""And the fifth is social. When people around you notice you're doing well, there's pressure to show it, or to share it. Bigger
house, nicer car, more expensive gifts. Remember the research in The Millionaire Next Door: many real millionaires looked completely
ordinary. Not showing your wealth is one of the best ways to keep it growing.""",
   "Suburban houses street United States", "DON'T SHOW IT")

# ---------------- Warning signs ----------------
ch("Six signs you're in the danger zone")
pr("""How do you know if fifty thousand dollars is starting to change your behavior? Here are six warning signs. If you notice two
or more, it's time to pause and revisit your plan.""")
sc("""Sign one. You've started browsing cars, houses or big trips much more than before, and telling yourself you deserve it. You
might. But notice that the browsing started when the balance grew. Sign two. You've stopped tracking your spending, because it
doesn't feel necessary anymore. That's exactly when lifestyle creep sneaks in.""",
   "Person browsing laptop", "SIGNS 1 AND 2")
sc("""Sign three. You've lowered or paused your automatic savings, telling yourself you've saved enough for now. Sign four. You've
found yourself excited about a single investment that could change everything, and you're thinking about putting a big chunk of
your money in it. Excitement is a warning light, not a green light.""",
   "Stock market chart on screen", "SIGNS 3 AND 4")
sc("""Sign five. Someone has asked you for money, or for an investment, and you feel guilty saying no. That guilt can lead to
decisions you'll regret. Decide your rules in advance, so you don't have to decide under pressure. And sign six. You're thinking
about quitting your job, but you don't have a written plan for what comes next.""",
   "Friends talking coffee", "SIGNS 5 AND 6")
sc("""None of these signs mean you're doing something wrong. They're normal human reactions to having more money than before. The
point is to notice them early. A five minute pause, and a look at your written plan, can save you years of progress. That's the
difference between people who pass through the danger zone and people who get stuck in it.""",
   "Road sign curve ahead", "NOTICE THEM EARLY")

# ---------------- Angle 3: playbook ----------------
short("Here's exactly what to do with fifty thousand dollars so it becomes five hundred thousand.")
ch("Angle 3: The playbook")
pr("""Angle three. The playbook. You have fifty thousand dollars, or you're getting close. Here's what to do with it, step by step.""")
sc("""Step one. Wipe out high interest debt. Any credit card or personal loan above about eight to ten percent goes first. Paying off
a card at twenty percent is a guaranteed twenty percent return, and nothing in investing reliably beats that.""",
   "Scissors cutting credit card", "STEP 1: KILL HIGH INTEREST DEBT")
sc("""Step two. Set aside your emergency fund. Three to six months of essential expenses, in a high yield savings account. Say your
essentials are three thousand dollars a month. That's nine to eighteen thousand. This money is not for investing, not for a car,
not for a vacation. It's insurance for your plan.""",
   "Piggy bank coins", "STEP 2: EMERGENCY FUND")
sc("""Step three. Max out the free money. Make sure you're getting your full employer match on retirement contributions. Then
consider an IRA. Use tax advantaged accounts first, within the current IRS limits, before investing in a regular taxable
account.""",
   "Office workers meeting", "STEP 3: THE MATCH AND THE IRA")
sc("""Step four. Invest the rest simply. A diversified mix of low cost index funds, or a single target date fund. Decide how much goes
into stocks and how much into bonds, based on your timeline and how you'd feel in a crash. Then automate a monthly contribution on
top, and leave it alone.""",
   "New York Stock Exchange trading floor", "STEP 4: INVEST SIMPLY")
sc("""Step five. Write down your rules. No car purchases over a certain amount. No single investment over a few percent of your
money. No loans to friends, only gifts within a yearly budget. No moving money because of an urgent phone call. Rules made while
calm protect you when you're not.""",
   "Notebook with financial notes", "STEP 5: WRITE YOUR RULES")
sc("""And step six. Set the next milestone. One hundred thousand dollars. Calculate how long it takes at your current savings rate,
and put the date on your calendar. At a seven percent illustration, fifty thousand plus one thousand dollars a month reaches one
hundred thousand in about three years.""",
   "Calendar planning", "STEP 6: THE NEXT MILESTONE")

# ---------------- Questions ----------------
ch("Questions people ask")
pr("""Let me answer the questions people ask most about this level.""")
sc("""Question one. Should I use fifty thousand for a down payment? It can make sense, if you'll still have an emergency fund after
closing, the total monthly cost fits your budget, and you plan to stay for many years. If buying would empty your accounts, it's
usually better to wait and keep saving.""",
   "House with for sale sign", "DOWN PAYMENT?")
sc("""Question two. Should I invest it all at once or a bit at a time? Research by firms like Vanguard has found that investing a lump
sum right away has historically beaten spreading it out more often than not, because markets tend to rise over time. But spreading
it over several months can feel easier emotionally. Either is far better than leaving it in cash forever.""",
   "Stock market chart on screen", "ALL AT ONCE OR GRADUALLY?")
sc("""Question three. Is fifty thousand enough to start a business? For some businesses, yes. But keep your emergency fund separate,
start small, test the idea before spending most of the money, and avoid using retirement savings. Many successful businesses start
much smaller than people imagine.""",
   "Small business storefront", "START A BUSINESS?")
sc("""Question four. What if I got the fifty thousand as a windfall, like an inheritance or a settlement? Slow down. Park it in a safe,
insured account for a few months. Don't announce it widely. Pay off high interest debt, build your emergency fund, and consider
talking to a fee only planner before any big decision.""",
   "Bank vault door", "A WINDFALL?")
sc("""Question five. Should I buy a rental property with my fifty thousand? Real estate can build wealth, but a single rental with
most of your savings tied up in it is concentrated and illiquid. Vacancies, repairs and bad tenants can turn a good deal into a
stressful one. If you're interested, learn the numbers carefully, keep your emergency fund separate, and make sure you can cover the
mortgage for months without rent.""",
   "Apartment building", "A RENTAL PROPERTY?")
sc("""Question six. How do I stop myself from spending it? Move it. Money that's invested in a retirement account or a brokerage
account at a different institution is harder to spend on impulse than money sitting in checking. Turn off easy transfers. And give
every part of it a job: emergency fund, retirement, next goal. Money with a job is much harder to spend.""",
   "Online banking smartphone app", "HOW NOT TO SPEND IT")
sc("""Question seven. Is it okay to spend some of it? Absolutely. Money is meant to make your life better, and a plan that never
allows any enjoyment usually breaks. Many people use a simple rule for windfalls and milestones: spend a small share, maybe five or
ten percent, on something meaningful, and put the rest to work. You get the celebration without losing the momentum.""",
   "Family walking on beach", "CAN I SPEND SOME?")

# ---------------- Recap ----------------
ch("Recap: 15 dangers")
sc("""Let's recap the fifteen dangers. The new car. The house you can't afford yet. Lifestyle creep. The hot investment tip. Leaving it
all in cash. The friend's business idea. Quitting too early. And scams.""",
   "Notebook with financial notes", "DANGERS 1 TO 8")
sc("""Overconfidence. The wrong advisor. Lending money. No emergency fund. Paying off cheap debt in the wrong order. Ignoring taxes. And
the biggest danger of all: stopping too soon.""",
   "Mountain climber reaching summit", "DANGERS 9 TO 15")
sc("""And the three angles. The numbers: fifty thousand left alone could become around four hundred thousand, and with steady
additions, around a million. The psychology: the wealth effect, mental accounting and the end of urgency. And the playbook: kill
expensive debt, build the cushion, grab the free money, invest simply, write your rules, and set the next milestone.""",
   "Map and compass", "NUMBERS, PSYCHOLOGY, PLAYBOOK")
sc("""Fifty thousand dollars is a turning point. Behind you is the hardest part of the climb, the part where every dollar came from
your own effort. Ahead of you is the part where your money starts doing more and more of the work. The only thing that can stop that
is a decision you make in the next few years. Make those decisions slowly, on purpose, with a plan written down, and fifty thousand
becomes the most important milestone of your financial life instead of the most dangerous one.""",
   "Sunrise over mountains", "A TURNING POINT")

# ---------------- Close ----------------
ch("What to do next")
pr("""So here's your homework. If you're near fifty thousand, write down your rules tonight. The car limit, the speculation limit,
the lending budget. If you're not there yet, save this video for when you are, because the day that balance crosses fifty thousand, the
temptations will show up fast, and it helps to have your answers ready before they do. If you want the full step by step plan, it's in my
playbook, link in the description. I'm Ryan Rover. See you in the next one.""")

save("video09", "Why $50,000 Is the Most Dangerous Amount of Money to Have", [
    "Federal Reserve, Survey of Consumer Finances 2022 (median net worth under 35: $39,040)",
    "Kelley Blue Book, average new-vehicle transaction prices (around $48,000-$50,000 in recent years)",
    "Federal Trade Commission, Consumer Sentinel Network data 2024 (more than $12 billion reported lost to fraud)",
    "Bureau of Labor Statistics, Business Employment Dynamics (establishment survival rates)",
    "Barber and Odean, Trading Is Hazardous to Your Wealth, Journal of Finance (2000)",
    "Richard Thaler, Mental Accounting Matters, Journal of Behavioral Decision Making (1999)",
    "Vanguard research, lump-sum investing versus dollar-cost averaging",
    "Thomas J. Stanley and William D. Danko, The Millionaire Next Door (1996)",
    "Compound growth: stated illustrative math at 7% average yearly return, compounded monthly; 4% rule of thumb (Bengen, 1994)",
], "why $50,000 is the most dangerous amount")
