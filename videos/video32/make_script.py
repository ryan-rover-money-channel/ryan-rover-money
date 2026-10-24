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
        sc(text, q, c)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. You've probably heard the quote. Compound interest is the eighth wonder of the world. He who
understands it, earns it. He who doesn't, pays it. It's usually credited to Albert Einstein. Here's a fun fact. There's no
good evidence Einstein ever said it. But whoever said it was right. Compound interest is the most powerful force in
personal finance. It can make ordinary people wealthy, and it can keep ordinary people broke. Today, we're going to
explain it completely, in twenty lessons, so it works for you instead of against you.""")
short("Einstein probably never said this. But it's still true.")
card("""Here's compound interest in one picture. Would you rather have one million dollars today, or a single penny that
doubles every day for thirty days? On day thirty, the penny is worth more than five million dollars.""",
     {"type": "compare", "left": {"label": "Option A", "big": "$1,000,000", "sub": "today"},
      "right": {"label": "Option B", "big": "$5,368,709", "sub": "a penny doubled for 30 days"},
      "note": "One cent doubled every day: day 30 = $5,368,709.12"})
sc("""The penny puzzle shows the strange thing about compounding. For most of the month, the penny looks pathetic. On day
ten, it's worth about five dollars. On day twenty, about five thousand. Then it explodes. Most of the growth happens at
the very end. That's exactly how compound interest works with real money, just over years instead of days. The early
years feel slow and almost pointless. The later years feel like magic. And most people quit before the magic starts.""",
   "Penny coins stacking", "SLOW, THEN SUDDEN")
sc("""We'll explain compounding from three angles. First, the numbers. How it actually works, the rule of seventy two,
compounding frequency and the real math behind famous examples. Second, the psychology. Why our brains struggle to
understand exponential growth, and how that costs us money. And third, the playbook. How to put compounding to work in
your life, and how to stop it working against you. Quick note. Growth examples use stated returns like seven percent.
Those are illustrations, not promises.""",
   "Exponential curve chart", "THREE ANGLES")
pr("""Let's start at the very beginning. What is compound interest, exactly?""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our sources. The Einstein quote's history comes from quote researchers like the Quote Investigator, which found no
reliable source. Benjamin Franklin's bequest comes from historical records of the Franklin trusts in Boston and
Philadelphia. Research on how people misunderstand compounding comes from economists Victor Stango and Jonathan Zinman,
and from financial literacy research by Annamaria Lusardi and Olivia Mitchell. Credit card rates come from the Federal
Reserve. This is education, not financial advice.""",
   "Historical documents archive", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Seven lessons on how compounding really works.""")

item(1, "Simple vs compound", "interest on interest",
"""Lesson number one. The difference between simple and compound interest.""", [
("""Simple interest is paid only on your original amount. Put one thousand dollars in an account paying ten percent
simple interest, and you earn one hundred dollars every year. After ten years, you have two thousand dollars. Steady,
predictable, and kind of boring.""", "Calculator with simple math", "SIMPLE INTEREST"),
("""Compound interest is paid on your original amount plus all the interest you've already earned. The same one thousand
dollars at ten percent compounded yearly becomes one thousand one hundred after year one, then one thousand two hundred
ten, then one thousand three hundred thirty one. After ten years, it's about two thousand five hundred ninety four
dollars. Almost six hundred dollars more than simple interest, without adding a cent.""", "Growing stacks of coins", "INTEREST ON INTEREST"),
("""Over longer periods, the gap becomes enormous. After thirty years, simple interest gives you four thousand dollars.
Compound interest at ten percent gives you over seventeen thousand. Same starting money, same rate. The only difference
is that the interest itself starts earning interest.""", "Two diverging lines chart", "THE GAP GROWS"),
("""Remember it this way. Simple interest is a staircase. Compound interest is a snowball. The staircase climbs the same
step every year. The snowball picks up more snow the bigger it gets.""", "Snowball rolling down hill", "STAIRCASE VS SNOWBALL"),
])

body_hook = "Divide seventy two by this number and see how fast money doubles."
item(2, "The rule of 72", "the doubling shortcut",
"""Lesson number two. The rule of seventy two.""", [
("""Here's the most useful shortcut in personal finance. Divide seventy two by your yearly return, and you get roughly how
many years it takes for money to double. At six percent, about twelve years. At eight percent, about nine years. At twelve
percent, about six years. It's an estimate, but it's remarkably close for typical rates.""", "Hourglass timer", "72 ÷ RATE = YEARS"),
("""The rule works for anything that grows at a steady rate. Investments, debt, even inflation. At three percent
inflation, prices double in about twenty four years. At twenty four percent credit card interest, an unpaid balance can
double in about three years.""", "Prices rising concept", "IT WORKS FOR DEBT TOO"),
("""Now think in doublings. At seven percent, money doubles roughly every ten years. Ten thousand dollars at age thirty
could become about twenty thousand at forty, forty thousand at fifty, and eighty thousand at sixty. Each decade, the jump
is bigger than the last.""", "Doubling chart steps", "10K, 20K, 40K, 80K"),
("""Try this. Take your savings account rate and divide seventy two by it. If the answer is fifty years or more, your money
is barely growing. Then try it with your credit card rate, and see how fast debt can double.""", "Calculator on desk", "TRY YOUR OWN RATES"),
])

card("""Here's the doubling in action. Ten thousand dollars at a seven percent average yearly return, roughly doubles about
every ten years. After thirty years, it's about eighty one thousand dollars, without adding a single dollar.""",
     {"type": "compare", "left": {"label": "Today", "big": "$10,000", "sub": "invested once"},
      "right": {"label": "In 30 years", "big": "~$81,000", "sub": "at 7% a year"},
      "note": "Illustration, compounded monthly. Returns are not guaranteed."})

item(3, "Compounding frequency", "daily, monthly, yearly",
"""Lesson number three. How often interest compounds matters, a little.""", [
("""Interest can compound yearly, monthly or even daily. The more often it compounds, the faster the balance grows,
because interest starts earning interest sooner. Twelve percent compounded monthly is slightly more than twelve percent
compounded yearly.""", "Calendar with days", "HOW OFTEN?"),
("""That's why banks show two numbers. The annual percentage rate, or APR, is the simple yearly rate. The annual
percentage yield, or APY, includes the effect of compounding. On savings, compare APYs. On debt, remember that the
effective cost can be a little higher than the APR, because interest compounds.""", "Bank rate sign APY", "APR VS APY"),
("""Most credit cards calculate interest daily, using a daily rate based on the APR. So a card at twenty four percent
charges roughly six and a half hundredths of a percent every single day on your balance, and that interest becomes part
of the balance.""", "Credit card terms fine print", "CARDS COMPOUND DAILY"),
("""In practice, frequency matters much less than rate and time. Don't obsess over daily versus monthly. Focus on getting
a good rate on savings, a low rate on debt, and as much time as possible.""", "Hourglass and coins", "RATE AND TIME MATTER MORE"),
])

item(4, "Adding money every month", "contributions supercharge it",
"""Lesson number four. Regular contributions supercharge compounding.""", [
("""A single deposit compounds nicely. But adding money every month is where compounding really shines. Each new deposit
starts its own little snowball. Over the years, you're rolling hundreds of snowballs at once.""", "Many snowballs rolling", "HUNDREDS OF SNOWBALLS"),
("""Two hundred dollars a month for thirty years at a seven percent average yearly return grows to roughly two hundred
forty four thousand dollars. You contribute seventy two thousand. The other one hundred seventy two thousand is growth.""", "Growth chart rising", "$72K IN, $244K OUT"),
("""Notice that in the early years, your contributions are most of the balance. Somewhere around year fifteen or twenty in
this example, yearly growth starts to rival what you add each year. After that, the money is doing more work than you
are.""", "Crossover chart lines", "THE CROSSOVER POINT"),
("""Try this. Set up an automatic monthly investment, even small. Then look up the year when your yearly growth might
exceed your yearly contributions. That's a milestone worth celebrating.""", "Automatic investing app", "FIND YOUR CROSSOVER"),
])

card("""Two hundred dollars a month for thirty years, at a seven percent average yearly return, grows to roughly two hundred
forty four thousand dollars. Total contributed, seventy two thousand.""",
     {"type": "growth", "monthly": 200, "rate": 0.07, "years": 30})

item(5, "Franklin's 200 year experiment", "compounding across centuries",
"""Lesson number five. Benjamin Franklin's two hundred year experiment.""", [
("""When Benjamin Franklin died in seventeen ninety, he left one thousand pounds each to the cities of Boston and
Philadelphia, with instructions to lend the money to young tradesmen at interest and let it grow for two hundred years.
It was a deliberate demonstration of compounding.""", "Benjamin Franklin portrait", "FRANKLIN'S GIFT"),
("""Part of the money was released after one hundred years, as Franklin instructed. The rest kept growing. By nineteen
ninety, the funds had grown into millions of dollars. Boston's fund was worth around five million, and Philadelphia's
around two million, according to historical accounts.""", "Boston and Philadelphia skyline", "MILLIONS BY 1990"),
("""The returns weren't spectacular, and the funds faced management problems over the centuries. But even modest growth,
given two hundred years, turned a gift into a fortune. Time can make up for a lot.""", "Old ledger book", "TIME MAKES UP FOR A LOT"),
("""The lesson for us. We don't have two hundred years. But we might have forty or fifty. That's plenty of time for
compounding to do something remarkable.""", "Calendar decades", "YOU HAVE DECADES")
])

body_hook = "Most of Warren Buffett's fortune came after he turned sixty five."
item(6, "Buffett's late fortune", "time beats talent",
"""Lesson number six. Why most of Warren Buffett's fortune came late in life.""", [
("""Warren Buffett is one of the most successful investors in history. But as writer Morgan Housel points out in The
Psychology of Money, the vast majority of Buffett's net worth was accumulated after his sixty fifth birthday.""", "Warren Buffett portrait", "AFTER AGE 65"),
("""Buffett started investing as a child and never stopped. His skill matters, of course. But Housel argues the real
secret is time. Buffett has been compounding for more than eighty years.""", "Old man reading newspaper", "80 YEARS OF COMPOUNDING"),
("""Housel makes the point that if Buffett had started at thirty and retired at sixty, he'd be wealthy, but nowhere near
as famous. The extra decades at both ends made the difference.""", "Timeline chart", "THE EXTRA DECADES"),
("""For regular people, the lesson is simple. Start as early as you can, and stay invested as long as you can.""", "Young investor and older investor", "START EARLY, STAY LONG"),
])

item(7, "Compounding works against you", "debt snowballs too",
"""Lesson number seven. Compounding works against you when you owe money.""", [
("""Everything we've said about growth applies to debt in reverse. The Federal Reserve reports average credit card rates
above twenty percent for accounts paying interest. At those rates, unpaid balances grow quickly.""", "Credit card debt statement", "DEBT COMPOUNDS"),
("""If you only make the minimum payment, it can take many years to pay off a balance, and the total interest can be a
large share of the original amount. Credit card statements are required to show this.""", "Minimum payment warning", "YEARS OF PAYMENTS"),
("""This is why the quote ends the way it does. He who understands it, earns it. He who doesn't, pays it.""", "Two paths sign", "EARN IT OR PAY IT"),
("""Try this. Find the minimum payment warning box on your card statement. It shows how long payoff takes at the minimum.""", "Credit card statement box", "READ THE BOX"),
])

pr("""That's angle one. Simple versus compound, the rule of seventy two, frequency, monthly contributions, Franklin's
experiment, Buffett's late fortune, and compounding debt. Now angle two. The psychology. Why our brains get this so
wrong.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
sc("""Humans evolved in a world of straight lines. If you walk twice as far, it takes about twice as long. If you gather
twice as many berries, you have twice as much food. Exponential growth is unnatural for our brains, and that's why
compounding surprises nearly everyone. In this angle, we'll look at seven ways our psychology gets in the way of
compounding, and what to do about each one.""",
   "Brain illustration", "BRAINS THINK IN STRAIGHT LINES")

item(8, "Exponential growth bias", "we underestimate curves",
"""Lesson number eight. Exponential growth bias.""", [
("""Economists Victor Stango and Jonathan Zinman studied what they called exponential growth bias. When people are asked
to estimate how something grows at a steady percentage, they tend to imagine a straight line instead of a curve. So they
badly underestimate long term growth, on both savings and debt.""", "Straight line vs curve", "THE BIAS"),
("""Their research found that households with stronger bias tended to borrow more at high rates and save less. That makes
sense. If you think a credit card balance grows slowly, borrowing feels cheap. If you think savings grow slowly, saving
feels pointless. Underestimating compounding costs money on both sides of the ledger.""", "Person borrowing money", "IT COSTS MONEY TWICE"),
("""The penny puzzle from the beginning works because it shocks this bias. Almost nobody guesses that a penny doubled for
thirty days ends up above five million dollars. Our intuition simply isn't built for doubling. That's not a personal
failing. It's how human brains work, which is why we need tools instead of gut feelings.""", "Penny on table", "NOBODY GUESSES RIGHT"),
("""Try this. Before calculating, guess what one hundred dollars a month becomes in forty years at seven percent. Write your
guess down. Then check it with a calculator. The real answer is roughly two hundred sixty thousand dollars. Most people
guess far too low, and that gap is the cost of straight line thinking.""", "Calculator screen result", "GUESS, THEN CHECK"),
])

item(9, "The boring middle", "why people quit",
"""Lesson number nine. The boring middle.""", [
("""In the first years of investing, growth is tiny. After five years of one hundred dollars a month at seven percent, you
might have around seven thousand dollars, and most of that is your own money. The growth part might be about a thousand
dollars. It honestly feels like nothing is happening.""", "Person bored looking at phone", "NOTHING IS HAPPENING"),
("""This is where many people quit. They stop contributing, cash out for something more exciting, or switch strategies
every few months. They leave right before the curve starts bending upward, which means they do all the hard, slow work and
miss the rewarding part.""", "Person walking away", "QUITTING TOO EARLY"),
("""Think back to the penny. On day ten, it's worth about five dollars. On day twenty, about five thousand. On day thirty,
more than five million. If you'd judged the penny on day ten, you'd have called it a failure. The boring middle isn't a
sign that compounding isn't working. It's a normal part of how compounding works.""", "Penny doubling calendar", "DAY 10 VS DAY 30"),
("""Try this. For the first five years, measure your success by the habit, not the balance. Did the automatic investment
happen every month? Did you raise it when you got a raise? If yes, you're winning, even if the balance looks small. The
balance will take care of itself later.""", "Habit tracker calendar", "TRACK THE HABIT")
])

item(10, "Impatience", "chasing faster returns",
"""Lesson number ten. Impatience leads people to chase faster returns.""", [
("""Because normal compounding is slow at first, people look for shortcuts. Hot stocks, trendy coins, leveraged bets, get
rich quick schemes. The promise of fast returns is especially tempting when steady growth feels painfully slow. And social
media is full of people showing off their wins, but rarely their losses.""", "Hot stock tip on phone", "CHASING SPEED"),
("""Here's the math that makes chasing so dangerous. Big losses destroy compounding. Lose fifty percent, and you need a one
hundred percent gain just to get back to where you started. Lose eighty percent, and you need a four hundred percent gain.
Avoiding large losses matters just as much as earning good returns, maybe more.""", "Graph of loss and recovery", "-50% NEEDS +100%"),
("""That's why so many successful long term investors emphasize steady, diversified investing over chasing big wins. A
portfolio that grows steadily without huge crashes often ends up ahead of one that soars and collapses. Slow and steady
compounding tends to beat boom and bust.""", "Tortoise and hare illustration", "SLOW AND STEADY"),
("""Try this. Keep your core long term investments boring and diversified, like broad index funds. If you really want to
speculate, set aside a small amount you can afford to lose completely, and never add to it after a loss.""", "Two buckets of money", "BORING CORE, SMALL FUN BUCKET"),
])

pr("""Quick pause. If compounding is finally clicking for you, please subscribe to Ryan Rover Money. It's free, and it helps
us keep explaining money in plain English. Now, lesson eleven.""")

item(11, "Present bias", "today beats decades",
"""Lesson number eleven. Present bias works against compounding.""", [
("""Compounding rewards patience, but our brains are wired to prefer rewards right now. Spending one hundred dollars today
on something fun feels much more real than having several hundred dollars more in thirty years. Economists call this present
bias, and it's one of the strongest forces in personal finance.""", "Person shopping happily", "NOW FEELS BETTER"),
("""That's exactly why automatic investing works so well. You make the decision once, when you're calm and thinking about
the long term. After that, the money moves before present bias ever gets a vote. You don't have to win the battle with
temptation every month, because there's no battle.""", "Automatic investment setup", "DECIDE ONCE"),
("""Picturing your future self also helps. Research by Hal Hershfield and colleagues found that people who viewed
digitally aged images of themselves were more willing to save for the future. When the future version of you feels like a
real person, saving feels less like losing money and more like helping someone you care about.""", "Aging face illustration", "MEET FUTURE YOU"),
("""Try this. Write down exactly what your investments are for. Not just retirement, but something specific. Freedom to
leave a job you dislike. A paid off home. Retiring at sixty. Specific goals make the future feel close enough to fight for.""", "Goals written on paper", "WRITE IT DOWN"),
])

item(12, "Interruption is the enemy", "never break the chain",
"""Lesson number twelve. Interrupting compounding is very expensive.""", [
("""Charlie Munger, Warren Buffett's longtime business partner, put it simply. The first rule of compounding is never to
interrupt it unnecessarily. Cashing out early, stopping contributions for years, or panic selling during a crash all break
the chain, and the chain is where the magic lives.""", "Broken chain links", "NEVER INTERRUPT IT"),
("""Early withdrawals from retirement accounts are a common interruption. Depending on the account and your situation,
withdrawing before retirement age can trigger income taxes and a penalty, and the money withdrawn loses all its future
compounding. A ten thousand dollar withdrawal at thirty could cost far more than ten thousand dollars by retirement.""", "Early withdrawal penalty form", "EARLY WITHDRAWALS COST"),
("""Job changes are another. When people leave a job, many cash out their old four oh one k instead of rolling it over,
especially when the balance is small. It feels like free money. But it often means taxes, penalties, and starting the
snowball over from zero.""", "Person changing jobs", "ROLL IT OVER"),
("""Try this. If you change jobs, roll your old retirement account into an IRA or your new employer's plan. And keep an
emergency fund, so a surprise expense never forces you to break the chain.""", "Rollover paperwork", "DON'T CASH OUT"),
])

item(13, "The financial literacy gap", "most people can't answer",
"""Lesson number thirteen. Most people misunderstand compounding.""", [
("""Economists Annamaria Lusardi and Olivia Mitchell created three simple questions to measure financial literacy. One asks
about compound interest, one about inflation, and one about diversification. In surveys over many years, a large share of
American adults couldn't answer all three correctly.""", "Survey questionnaire", "THE BIG THREE QUESTIONS"),
("""Their research found that people who answered correctly were more likely to plan for retirement, invest and avoid high
cost borrowing. In other words, understanding concepts like compounding is linked with better financial outcomes, not just
better test scores.""", "Person planning retirement", "KNOWLEDGE PAYS"),
("""The encouraging part is that compounding isn't hard to learn. If you've watched this far, you now understand more about
it than many adults ever will. You know the difference between simple and compound interest, the rule of seventy two, and
why time matters so much.""", "Light bulb idea", "NOW YOU KNOW"),
("""Try this. Explain the rule of seventy two to a friend, partner or child this week. Teaching is one of the best ways to
remember something, and you might change their financial future too.""", "Two people talking", "TEACH SOMEONE"),
])

item(14, "Small rates, big differences", "1% matters",
"""Lesson number fourteen. Small differences in rate become huge over time.""", [
("""One percent sounds tiny. But compounding magnifies small differences. Over decades, a one percent difference in your
yearly return, whether it comes from fees, investment choices or idle cash, can change your final balance dramatically.""", "Percent sign close up", "1% MATTERS"),
("""Here's an example. Five hundred dollars a month for forty years at seven percent grows to roughly one point three
million dollars. At six percent, it's roughly one million. That single percentage point is worth around three hundred
thousand dollars in this example.""", "Two lines diverging", "6% VS 7% OVER 40 YEARS"),
("""That's why investment fees matter so much. Unlike market returns, fees are certain. They come out every year, in good
markets and bad. Choosing a fund with a fee of one percent instead of a small fraction of a percent is effectively choosing
a lower return for decades.""", "Fee schedule document", "FEES ARE CERTAIN"),
("""Try this. List every fund you own and its expense ratio. If any are around one percent or higher, check whether a lower
cost alternative exists in the same category.""", "Fund comparison on laptop", "LOWER YOUR FEES"),
])

pr("""That's angle two. Straight line thinking, the boring middle, impatience, present bias, interruptions, the literacy gap
and small rate differences. Now angle three. The playbook.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
sc("""Now let's turn knowledge into action. Here are six moves that put compounding to work for you, and stop it working
against you. None of them require a big income, special skills or perfect timing. They just require starting, and then
staying out of compounding's way.""",
   "Toolbox on table", "SIX MOVES")

item(15, "Start now", "time is the multiplier",
"""Move number fifteen. Start now, with whatever you have.""", [
("""The single biggest factor in compounding is time. Every year you wait is a year of growth you never get back, and those
early years are the ones that compound the longest. A dollar invested at twenty five has roughly forty years to grow. A
dollar invested at fifty five has about ten.""", "Clock ticking", "TIME IS THE MULTIPLIER"),
("""You don't need much. Many brokerages offer accounts with no minimums and fractional shares of broad index funds. Fifty
or one hundred dollars a month, in a tax advantaged account like a four oh one k or an IRA, is a real start.""", "Small investment app", "START SMALL"),
("""You can always increase the amount later, when your income grows or debts are paid off. What you can never do is go
back and start earlier. That's why the best time to start is always as soon as possible.""", "Calendar going forward", "YOU CAN'T START EARLIER"),
("""Try this. Open an account and set up your first automatic investment this week, even if it's small. Then set a calendar
reminder to increase it in six months.""", "Person opening account", "THIS WEEK"),
])

item(16, "Kill compounding debt", "stop the reverse snowball",
"""Move number sixteen. Eliminate high interest debt.""", [
("""Paying off a credit card at twenty percent is like earning a guaranteed twenty percent return, something no investment
reliably offers. Before compounding can work for you, it helps to stop it working against you.""", "Credit card cut up", "GUARANTEED RETURN"),
("""A simple method is to list every debt by interest rate, pay the minimum on all of them, and put every extra dollar on
the highest rate. When that one's gone, roll its payment into the next one. Each payoff makes the next one faster.""", "Debt list by rate", "HIGHEST RATE FIRST"),
("""Once the high interest debt is gone, redirect those same monthly payments into investing. Now the snowball rolls in
your direction. The money that used to compound for the bank starts compounding for you.""", "Arrow flipping direction", "FLIP THE SNOWBALL"),
("""Try this. Stop adding new charges to any card that carries a balance. Use a debit card or cash for everyday spending
until the balance is gone.""", "Credit card in drawer", "STOP ADDING"),
])

item(17, "Reinvest everything", "let it compound",
"""Move number seventeen. Reinvest dividends and interest.""", [
("""Dividends and interest are the fuel of compounding. When a company pays a dividend and you spend it, the snowball stops
growing. When you reinvest it, it buys more shares, which pay more dividends, which buy more shares.""", "Dividend reinvestment setting", "REINVEST"),
("""Most brokerages let you automatically reinvest dividends, often called a DRIP, short for dividend reinvestment plan. For
long term money, turning it on is one of the easiest ways to keep compounding running at full speed.""", "Brokerage settings screen", "TURN ON DRIP"),
("""Historical data from S and P Dow Jones Indices shows that reinvested dividends have made up a significant share of the
S and P five hundred's total return over long periods. Investors who spent their dividends saw much less growth than those
who reinvested them.""", "Total return chart", "DIVIDENDS ADD UP"),
("""Try this. Log into your accounts and check that dividend reinvestment is turned on for your long term investments.""", "Account settings checklist", "CHECK IT"),
])

item(18, "Lower your costs", "keep more of the growth",
"""Move number eighteen. Keep investment costs low.""", [
("""Every dollar paid in fees is a dollar that stops compounding for you, along with all the growth it would have produced.
Over decades, that adds up. Fees are one of the few parts of investing you can fully control.""", "Coins falling away", "FEES STOP COMPOUNDING"),
("""Low cost broad index funds often charge a small fraction of a percent per year. Many actively managed funds charge
much more, and research such as the SPIVA reports has found that most of them underperformed their benchmarks over long
periods after fees.""", "Index fund chart", "LOW COST FUNDS"),
("""If you work with an advisor, that can be valuable, but know exactly what you pay and how they're paid. A fee only
fiduciary is required to act in your best interest.""", "Advisor meeting", "KNOW WHAT YOU PAY"),
("""Try this. Add up your total yearly investment fees in dollars, not percentages. Seeing the dollar amount often motivates
a change.""", "Calculator with fees", "FEES IN DOLLARS"),
])

body_hook = "The secret to compounding? Do almost nothing for a very long time."
item(19, "Automate and ignore", "the lazy advantage",
"""Move number nineteen. Automate, then mostly ignore it.""", [
("""The best compounders often do the least. They set up automatic investing into diversified, low cost funds, and then
they leave it alone for years. No constant trading, no reacting to headlines, no switching strategies every time something
new is popular.""", "Person relaxing hammock", "THE LAZY ADVANTAGE"),
("""Research by Brad Barber and Terrance Odean found that individual investors who traded most frequently earned lower
returns after costs than those who traded less. Activity often feels productive, but with investing, it frequently
interrupts compounding.""", "Stressed person checking phone", "TRADING LESS WINS"),
("""A simple routine works for most people. Review your accounts once or twice a year. Rebalance if your mix has drifted far
from your plan. Raise your contributions when you can. Otherwise, let time do its work.""", "Annual review calendar", "REVIEW TWICE A YEAR"),
("""Try this. Turn off daily price notifications from your investing app, and move the app off your home screen.""", "Phone notification settings", "NOTIFICATIONS OFF"),
])

item(20, "Compound yourself too", "skills compound",
"""Move number twenty. Compound your skills, health and relationships too.""", [
("""Compounding isn't only about money. Skills build on skills. Knowledge builds on knowledge. Trust in relationships builds
over years. A little improvement every day, kept up for decades, can produce enormous results.""", "Person learning new skill", "SKILLS COMPOUND"),
("""Reading thirty minutes a day adds up to many books a year. Exercising regularly protects your health, which protects
your ability to earn. Learning a valuable skill can raise your income for the rest of your career.""", "Person reading book", "SMALL DAILY HABITS"),
("""And these forms of compounding feed your financial compounding. A higher income lets you invest more, which compounds
faster. Better health means more working years and fewer medical bills. It's a double snowball.""", "Career growth chart", "A DOUBLE SNOWBALL"),
("""Try this. Pick one skill that could raise your income, and spend fifteen minutes a day on it this month. Fifteen minutes
a day is over ninety hours a year.""", "Timer fifteen minutes", "15 MINUTES A DAY"),
])

# ---------------- Story ----------------
ch("Two savers")
pr("""Here's a classic example that shows compounding's power.""")
short("Ten years of saving beat thirty years. Here's how.")
sc("""Saver one invests two hundred dollars a month from age twenty five to thirty five, then stops completely. That's ten
years and twenty four thousand dollars. Saver two starts at thirty five and invests two hundred dollars a month until sixty
five. That's thirty years and seventy two thousand dollars.""",
   "Two people different ages", "TWO SAVERS")
sc("""At a seven percent average yearly return, who has more at sixty five? Saver one. The money invested early had thirty
extra years to compound, and that head start is enough to beat three times the contributions in this example. Time beat
money.""",
   "Older person celebrating", "TIME BEAT MONEY")
sc("""Of course, the best plan is to start early and keep going. But if you take away one idea from this video, let it be
this. The dollars you invest early are the most powerful dollars you'll ever invest.""",
   "Young person investing on phone", "EARLY DOLLARS ARE POWERFUL")

# ---------------- By age ----------------
ch("Compounding at every age")
pr("""Let's make this personal. Here's what compounding looks like depending on when you start. Same habit for everyone,
three hundred dollars a month, a seven percent average yearly return. Remember, this is an illustration, not a promise.""")
sc("""Start at twenty five and keep going until sixty five. That's forty years. Three hundred dollars a month grows to roughly
seven hundred eighty thousand dollars. You contributed one hundred forty four thousand. The other six hundred thousand or so
is growth. Compounding did most of the work, not you.""",
   "Young adult at first job", "AGE 25: ABOUT $787K")
sc("""Start at thirty five. Thirty years of the same habit grows to roughly three hundred sixty six thousand dollars. That's
still a very real retirement cushion, but notice something. Waiting just ten years cut the final number by more than half.
That's the cost of delay, in one sentence.""",
   "Person in their thirties with family", "AGE 35: ABOUT $366K")
sc("""Start at forty five. Twenty years grows to roughly one hundred fifty six thousand dollars. Start at fifty five, and ten
years grows to roughly fifty two thousand. Less dramatic, but still meaningful. And people who start later often earn more,
so they can invest more each month to make up some of the gap.""",
   "Mature person reviewing finances", "AGE 45: $156K, AGE 55: $52K")
sc("""Here's the catch up math. If you start at forty and invest one thousand dollars a month for twenty five years at the
same seven percent, you could reach roughly eight hundred ten thousand dollars. So a late start isn't hopeless. It just means
time is scarcer, so your contributions have to work harder.""",
   "Person at forty planning", "CATCHING UP IS POSSIBLE")
sc("""And in the United States, people fifty and older are generally allowed extra catch up contributions in retirement
accounts like four oh one ks and IRAs. The limits change, so check the current numbers on the IRS website. The rules were
written with late starters in mind.""",
   "Retirement account form", "CATCH UP CONTRIBUTIONS")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. Do savings accounts compound? Yes, most pay compound interest, usually daily or monthly. But rates on
many traditional savings accounts are low. High yield savings accounts usually pay more.""",
   "Savings account statement", "DO SAVINGS COMPOUND?")
sc("""Question two. Do stocks compound? Stocks don't pay a set interest rate, but they compound through rising company
values and reinvested dividends. That's why long term stock investing is often described as compounding.""",
   "Stock market chart", "DO STOCKS COMPOUND?")
sc("""Question three. Is it too late to benefit from compounding? No. Even ten or twenty years of compounding can make a big
difference. Start now and invest as much as you reasonably can.""",
   "Older person starting to invest", "TOO LATE?")

sc("""Question four. Does inflation cancel out compounding? It works against it. Inflation slowly shrinks what each dollar
can buy. At three percent inflation, five thousand dollars twenty years from now buys roughly what two thousand eight hundred
dollars buys today. That's why money that must grow for decades usually needs to earn more than inflation.""",
   "Grocery prices rising", "INFLATION FIGHTS BACK")
sc("""Question five. What's the difference between APR and APY? APR is the yearly rate before compounding is counted. APY,
the annual percentage yield, includes compounding. So when you're saving, compare APYs. And when you're borrowing, remember
that the true cost of a card with a twenty four percent APR is even a little higher once compounding kicks in.""",
   "Bank rate sign", "APR VS APY")
sc("""Question six. Should I pay off my mortgage or invest? It depends on your rate, your taxes and your peace of mind.
Generally, the higher your mortgage rate, the more paying it down acts like a guaranteed return. Many people do both. A low
rate mortgage is very different from a twenty percent credit card.""",
   "House with calculator", "MORTGAGE OR INVEST?")
sc("""Question seven. How do I know my real return? Most brokerages show a personal rate of return in your account. Look for
it, and compare it to a simple broad index fund over the same period. If you're far behind, high fees or too much trading may
be the reason.""",
   "Brokerage performance screen", "KNOW YOUR REAL RETURN")

sc("""Question eight. Can compounding work with very small amounts? Absolutely. Twenty five dollars a month won't make you
rich on its own, but it builds the habit, and habits are what grow. Many people who start tiny raise the amount over the
years as income grows. The habit you build at twenty five dollars is the same habit that later moves two thousand.""",
   "Coins stacking up", "SMALL AMOUNTS COUNT")
sc("""Question nine. What if the market crashes right after I start? Crashes happen, and they're painful. But for someone
investing every month, a falling market means buying more shares at lower prices. Historically, broad markets have recovered
from past crashes over time, though there's never a guarantee, and recovery can take years.""",
   "Market chart dipping and recovering", "WHAT ABOUT CRASHES?")

# ---------------- Mistakes ----------------
ch("Three compounding mistakes")
sc("""Mistake one. Keeping long term money in cash for years. Cash is great for an emergency fund and short term goals. But
money you won't need for decades, sitting in an account earning far less than inflation, loses buying power every single
year. Know which money is for safety, and which money is for growth.""",
   "Cash in a jar", "MISTAKE 1: TOO MUCH CASH")
sc("""Mistake two. Waiting for the perfect moment. People wait for the market to drop, for a raise, for the new year, for
less stress. Meanwhile, months turn into years. Nobody can reliably predict the market, and the perfect moment rarely
announces itself. A steady monthly habit removes the guessing completely.""",
   "Person waiting checking watch", "MISTAKE 2: WAITING")
sc("""Mistake three. Ignoring the reverse snowball. Some people invest diligently while carrying credit card balances at
twenty percent or more. The debt often compounds faster than the investments grow. Fixing that first is one of the highest
return moves most people will ever make.""",
   "Credit card bill and investment app", "MISTAKE 3: IGNORING DEBT")
sc("""Avoid those three, follow the playbook, and give it time. That's honestly most of what compounding asks of you. It's
simple, but it isn't easy, because it asks for patience in a world that rewards speed.""",
   "Calm person at sunrise", "SIMPLE, NOT EASY")

# ---------------- Recap ----------------
ch("Recap")
sc("""Quick recap. Angle one, the numbers. Simple versus compound, the rule of seventy two, compounding frequency, monthly
contributions, Franklin's experiment, Buffett's late fortune, and compounding debt.""",
   "Checklist on clipboard", "THE NUMBERS: 1 TO 7")
sc("""Angle two, the psychology. Exponential growth bias, the boring middle, impatience, present bias, interruptions, the
literacy gap, and small rate differences.""",
   "Person thinking at window", "THE PSYCHOLOGY: 8 TO 14")
sc("""Angle three, the playbook. Start now, kill compounding debt, reinvest everything, lower your costs, automate and
ignore, and compound yourself too.""",
   "Notebook with plan", "THE PLAYBOOK: 15 TO 20")

# ---------------- Close ----------------
ch("What to do next")
pr("""Whoever said it first, it's true. He who understands compound interest, earns it. He who doesn't, pays it. Now you
understand it. If you want the full plan for putting it to work, it's in my playbook, linked in the description. Tell me in
the comments, what's your rule of seventy two number? I'm Ryan Rover. See you in the next one.""")

save("video32", "Compound Interest Explained: The 8th Wonder of the World", [
    "Quote Investigator, on the compound interest quote attributed to Albert Einstein (no reliable source)",
    "Historical accounts of Benjamin Franklin's 1790 bequests to Boston and Philadelphia",
    "Morgan Housel, The Psychology of Money (2020): Warren Buffett's net worth after age 65",
    "Stango and Zinman, Exponential Growth Bias and Household Finance (Journal of Finance, 2009)",
    "Lusardi and Mitchell, financial literacy questions (the Big Three)",
    "Federal Reserve, G.19 Consumer Credit (credit card rates above 20%)",
    "S&P Dow Jones Indices, dividends' share of S&P 500 total return",
    "Hershfield et al., Increasing Saving Behavior Through Age-Progressed Renderings of the Future Self (Journal of Marketing Research, 2011)",
    "Barber and Odean, Trading Is Hazardous to Your Wealth (Journal of Finance, 2000)",
    "S&P Dow Jones Indices, SPIVA U.S. Scorecard (active funds vs benchmarks)",
    "Charlie Munger: the first rule of compounding is never to interrupt it unnecessarily",
    "IRS, retirement plan and IRA catch-up contribution rules for age 50 and older",
    "Growth examples: compounding at stated average yearly returns (illustrations, not promises)",
], "compound interest explained in 20 lessons, from 3 angles: numbers, psychology, playbook")
