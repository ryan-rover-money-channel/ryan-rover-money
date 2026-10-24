import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

body_hook = None  # set right before item() to start a Short at its first explained scene

def item(n, title, sub, card_text, scenes):
    """scenes: list of (text, query, caption) shown after the list card."""
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"MISTAKE {n}")
    global body_hook
    if body_hook:
        short(body_hook); body_hook = None
    for text, q, c in scenes:
        sc(text, q, c)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Investing has never been easier to start. You can open an account on your phone in minutes, buy a
fraction of a share with a few dollars, and trade without paying commissions. But easier to start doesn't mean easier to do
well. In fact, it's never been easier to make expensive beginner mistakes. Today we're going through twenty of them, and
what to do instead.""")
short("Most beginner investors lose money for the same few reasons.")
card("""Here's the good news. Most investing mistakes aren't about picking the wrong stock. They're about waiting too long,
paying too much, reacting too emotionally and skipping the basics. And every one of those can be fixed.""",
     {"type": "stat", "label": "Beginner investing mistakes", "big": "20", "sub": "and what to do instead of each one"})
sc("""Think about it like learning to drive. Most crashes don't happen because someone lacked advanced racing skills. They
happen because of basic mistakes, like speeding, not paying attention or panicking at the wrong moment. Investing works the
same way. Avoiding the big basic mistakes matters far more than finding a clever strategy.""",
   "Learner driver in car", "BASICS BEAT CLEVERNESS")
sc("""We'll go through these from three angles. First, the numbers. Mistakes that quietly cost you money through math, like
waiting, fees and taxes. Second, the psychology. Mistakes our brains push us into, like panic and hype. And third, the
playbook. Mistakes in how people set up and run their investments. Quick reminder, this is education, not financial advice,
and all growth examples are illustrations, not promises.""",
   "Three paths in a forest", "THREE ANGLES")
pr("""Let's start with the numbers. And the first mistake is the most expensive one of all.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our numbers. Growth examples use monthly compounding at a stated average yearly return, usually seven percent. Account
and tax rules come from the IRS. Fund cost data comes from the Investment Company Institute, and fund performance data from S
and P Dow Jones Indices. Investor warnings come from the SEC and FINRA. This is education, not financial advice.""",
   "Financial documents on desk", "OUR NUMBERS")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Seven mistakes that quietly cost beginners money, often without them ever noticing.""")

item(1, "Waiting to start", "the most expensive mistake",
"""Mistake number one. Waiting for the right time to start.""", [
("""Beginners often wait. For a bigger paycheck, for the market to drop, for more knowledge, for less stress. But the most
important ingredient in investing is time, and every year you wait is a year of compounding you can never get back. Waiting
feels safe, but it's often the most expensive choice of all.""", "Person waiting by window", "WAITING FEELS SAFE"),
("""Here's the math. Two hundred dollars a month at a seven percent average yearly return, invested for thirty five years,
grows to roughly three hundred sixty thousand dollars. Start ten years later and invest for twenty five years, and it grows to
roughly one hundred sixty two thousand. Waiting ten years cut the result by more than half.""", "Two growth charts compared", "$360K VS $162K"),
("""Waiting for the market to dip is a special version of this mistake. Nobody can reliably predict short term moves. People
who wait for a crash sometimes watch the market rise for years before it comes, and by then, the crash may still leave prices
higher than when they started waiting.""", "Person watching chart rise", "WAITING FOR A DIP"),
("""What to do instead. Start now with whatever you can, even fifty or one hundred dollars a month, and increase it over time.
You'll learn more from one year of actually investing than from five years of waiting to feel ready.""", "Person starting on phone", "START NOW, START SMALL"),
])

item(2, "Ignoring fees", "small percentages, big losses",
"""Mistake number two. Ignoring fees.""", [
("""Fees look tiny because they're shown as percentages. One percent a year sounds like nothing. But that percentage comes out
of your whole balance, every year, for decades. Beginners often don't even know what they're paying.""", "Small print on document", "FEES HIDE IN PERCENTAGES"),
("""According to the Investment Company Institute, the average index equity mutual fund recently charged around five
hundredths of a percent a year, while the average actively managed equity fund charged around sixty five hundredths. Over
forty years of steady investing, a gap like that can cost hundreds of thousands of dollars.""", "Fee comparison table", "0.05% VS 0.65%"),
("""And fund fees aren't the only ones. Some advisors charge around one percent a year on top of fund fees. Some accounts charge
maintenance fees. Some products have sales charges when you buy. Fees stack, and they compound against you.""", "Stack of fee receipts", "FEES STACK UP"),
("""Here's a quick way to see fees in dollars. Multiply your balance by the expense ratio. On a fifty thousand dollar balance,
a one percent fee is five hundred dollars a year. A five hundredths of a percent fee is twenty five dollars. Same market
exposure in many cases, very different cost, and that difference compounds every single year.""", "Calculator showing fee in dollars", "$500 VS $25 A YEAR"),
("""What to do instead. Find the expense ratio of every fund you own, and know exactly how any advisor is paid. Favor broad, low
cost index funds, and treat every fee as something that has to justify itself.""", "Person reviewing fund costs", "KNOW EVERY FEE"),
])

body_hook = "If your job offers this and you skip it, you're turning down free money."
item(3, "Skipping the employer match", "free money left behind",
"""Mistake number three. Skipping the employer match.""", [
("""Many employers match part of what you contribute to a workplace retirement plan. A common example is fifty cents for every
dollar you contribute, up to six percent of your salary. Not contributing enough to get the full match is like turning down
part of your pay.""", "Employee benefits booklet", "THE MATCH IS PART OF YOUR PAY"),
("""Here's what that can mean. On a sixty thousand dollar salary, contributing six percent is three thousand six hundred
dollars a year, and a fifty percent match adds one thousand eight hundred. Invested for thirty years at a seven percent average
yearly return, that match alone could grow to roughly one hundred eighty thousand dollars.""", "Growing pile of money", "THE MATCH COULD BE $180K"),
("""Some matches come with a vesting schedule, meaning you have to stay a certain number of years to keep all of the employer's
money. Even so, for most people, getting the match is one of the best returns available anywhere.""", "Vesting schedule chart", "CHECK THE VESTING"),
("""What to do instead. Find your plan's match formula in your benefits information, and set your contribution at least high
enough to get every dollar of it.""", "Person adjusting contribution", "GET THE FULL MATCH"),
])

item(4, "Investing while carrying expensive debt", "the race you can't win",
"""Mistake number four. Investing while carrying high interest debt.""", [
("""Investing feels more exciting than paying off debt. But credit card interest rates in the United States have averaged above
twenty percent in recent years, according to Federal Reserve data. Long term stock market returns have historically been much
lower than that.""", "Credit card and stock chart", "20% DEBT VS MARKET RETURNS"),
("""So if you invest while carrying a large credit card balance, you're usually losing the race. The debt grows faster than your
investments are likely to. Paying off a twenty percent card is like earning a guaranteed twenty percent return.""", "Race between two runners", "A RACE YOU USUALLY LOSE"),
("""The exception is usually the employer match. Many people still contribute enough to get it while paying down debt, because
the match is such a high immediate return.""", "Balance between two goals", "THE MATCH EXCEPTION"),
("""What to do instead. List your debts by interest rate. Attack the highest rate first while making minimum payments on the
rest, then redirect those payments into investing once the expensive debt is gone.""", "Debt list sorted by rate", "HIGHEST RATE FIRST"),
])

item(5, "No emergency fund", "forced to sell at the worst time",
"""Mistake number five. Investing without an emergency fund.""", [
("""Picture this. You invest everything you have. Then the market drops, and around the same time, your car breaks down or you
lose your job. Now you have to sell investments at a loss to pay bills. That's how beginners turn temporary drops into
permanent losses.""", "Broken down car", "FORCED TO SELL LOW"),
("""An emergency fund is cash set aside for surprises, often three to six months of essential expenses, kept somewhere safe
and easy to reach, like a high yield savings account. It's not an investment. It's insurance for your investments.""", "Savings jar labeled emergency", "INSURANCE FOR YOUR INVESTMENTS"),
("""It also helps you stay calm. When you know your bills are covered, market drops feel less scary. You can leave your
investments alone and let them recover, instead of panicking.""", "Calm person reading news", "CASH CREATES CALM"),
("""What to do instead. Build at least a starter emergency fund, maybe one thousand dollars, before investing heavily, then
grow it toward three to six months of essentials over time.""", "Progress bar filling", "BUILD THE CUSHION FIRST"),
])

item(6, "Expecting the average every year", "returns are lumpy",
"""Mistake number six. Expecting smooth returns.""", [
("""Beginners often hear that the stock market has averaged around ten percent a year historically, before inflation, and
expect something close to that every year. But averages hide huge swings. Individual years can be up thirty percent or down
more than thirty percent.""", "Bumpy road", "AVERAGES HIDE SWINGS"),
("""The S and P five hundred fell by more than a third in 2008. It dropped sharply in early 2020, then recovered quickly. In 2022
it fell by around a fifth. Long term investors have been rewarded historically, but the path has never been smooth.""", "Stock chart with big drops", "THE PATH IS NEVER SMOOTH"),
("""Here's another quirk of the math. If your investment falls thirty percent, you need a gain of about forty three percent just
to get back to even. Losses and gains aren't symmetrical, which is one more reason to avoid panic selling after a drop.""", "Loss and recovery bars", "-30% NEEDS +43%"),
("""It also helps to know how often bad years happen. Historically, the S and P five hundred has had a negative calendar
year roughly one year in four, give or take. That means a forty year investing life could include about ten losing years. They
are not a sign that something is broken. They are the price of admission for long term growth.""", "Calendar with red and green years", "ROUGHLY 1 YEAR IN 4 IS DOWN"),
("""What to do instead. Plan for bad years. Expect them, write down how you'll respond, and only invest money in stocks that you
won't need for at least five years.""", "Written plan on desk", "PLAN FOR BAD YEARS"),
])

item(7, "Ignoring taxes", "the wrong account, the wrong timing",
"""Mistake number seven. Ignoring taxes.""", [
("""Taxes can take a big bite out of returns, but beginners often ignore them. One common mistake is investing in a regular
taxable account while ignoring tax advantaged accounts like a four oh one k, a traditional IRA or a Roth IRA.""", "Tax forms on table", "USE TAX ADVANTAGED ACCOUNTS"),
("""Another is selling too quickly. In the United States, profits on investments held one year or less are generally taxed as
ordinary income, while investments held longer than a year usually qualify for lower long term capital gains rates. Frequent
trading can mean paying more tax.""", "Calendar showing one year", "HOLD OVER A YEAR"),
("""Each tax advantaged account has rules, income limits and yearly contribution limits that change over time. The IRS website
lists the current numbers.""", "IRS website on laptop", "KNOW THE RULES"),
("""What to do instead. Use tax advantaged accounts first where it makes sense, hold investments for the long term, and consider
talking to a tax professional if your situation is complex.""", "Tax professional meeting", "TAXES ARE PART OF RETURNS"),
])

pr("""That's angle one. Waiting, fees, skipping the match, expensive debt, no emergency fund, expecting smooth returns and
ignoring taxes. Now angle two. The psychology.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
sc("""Most investing mistakes aren't caused by a lack of knowledge. They're caused by emotions. Fear, greed, excitement, envy.
In this angle, we'll look at seven mistakes our brains push us into, and how to protect yourself from your own instincts.""",
   "Brain with emotions illustration", "EMOTIONS DRIVE MISTAKES")

body_hook = "The worst investing move happens when you're most scared."
item(8, "Panic selling", "locking in losses",
"""Mistake number eight. Panic selling during a crash.""", [
("""When markets fall, it feels like the drop will never end. The news is scary, your balance is shrinking and every instinct
says get out before it gets worse. So many beginners sell, turning a temporary paper loss into a real, permanent one.""", "Panicked person at computer", "THE URGE TO GET OUT"),
("""The problem is that some of the market's best days have historically come close to its worst ones. Investors who sell in a
panic often miss the rebound, and then buy back in later at higher prices, if they buy back at all.""", "Chart with sharp rebound", "MISSING THE REBOUND"),
("""Historically, the broad U.S. market has recovered from every past crash, although some recoveries took years and there's no
guarantee for the future. The investors who stayed in through those drops were usually the ones rewarded.""", "Recovery chart", "STAYING IN HAS BEEN REWARDED"),
("""There's also a hidden cost to panic selling in a taxable account. If you sell investments that had gains, you may owe
taxes, and if you buy back later, you start over with a new cost basis. So panic can cost you twice, once in missed recovery
and once in taxes. Staying invested avoids both.""", "Tax bill and falling chart", "PANIC CAN COST YOU TWICE"),
("""What to do instead. Decide now how you'll act in a crash. Write it down. When a crash comes, keep your automatic
investments running and avoid making big decisions while you're scared.""", "Note saying do not sell", "DECIDE BEFORE THE CRASH"),
])

item(9, "Chasing last year's winners", "performance chasing",
"""Mistake number nine. Chasing last year's winners.""", [
("""Beginners often look at which fund or stock went up the most last year and buy it. It feels logical. If it went up a lot,
it must be good. But past performance often doesn't continue.""", "Trophy on shelf", "LAST YEAR'S WINNER"),
("""S and P Dow Jones Indices tracks whether top performing funds stay on top. Their persistence research has found that
relatively few top funds keep their top ranking over the following years. Yesterday's winner is often tomorrow's average, or
worse.""", "Leaderboard changing", "WINNERS RARELY REPEAT"),
("""Chasing performance also means buying after prices have already risen a lot, which can mean buying high. Then, when the
fund cools off, many people sell low and move to the next hot thing.""", "Person running after bus", "BUY HIGH, SELL LOW"),
("""Fund companies know this, which is why advertisements often highlight a fund's best recent returns. A fund family with
dozens of funds will almost always have a few with great recent numbers, just by chance. Seeing a strong track record in an ad
tells you very little about what that fund will do next.""", "Fund advertisement", "ADS SHOW THE WINNERS"),
("""What to do instead. Choose investments based on cost, diversification and your plan, not on recent returns. Broad, low cost
index funds remove the need to guess who'll win next.""", "Index fund chart", "CHOOSE BY PLAN, NOT RETURNS"),
])

item(10, "Falling for hype", "the next big thing",
"""Mistake number ten. Falling for hype.""", [
("""Every few years, something becomes the investment everyone's talking about. A hot sector, a meme stock, a new coin. Prices
soar, people brag online and beginners rush in so they don't miss out.""", "Crowd excited at screen", "THE NEXT BIG THING"),
("""Some hyped investments keep rising for a while. But many end with sharp crashes, and the people who buy in late, often
beginners, tend to buy near the top. History is full of bubbles that felt like sure things at the time.""", "Bubble popping illustration", "BUBBLES FEEL LIKE SURE THINGS"),
("""The SEC and FINRA regularly warn investors about pump and dump schemes, where promoters hype an investment to push its
price up, then sell their own shares to the people they convinced to buy.""", "Warning sign on screen", "BEWARE PUMP AND DUMP"),
("""A useful test is to ask how the investment actually makes money. A company earns profits. A bond pays interest. A rental
property collects rent. If the only reason something should go up is that other people will want to buy it later at a higher
price, you're speculating, not investing, and you should size it that way.""", "Person asking question", "HOW DOES IT MAKE MONEY?"),
("""What to do instead. If you want to try a speculative investment, use only a small amount you can afford to lose completely,
and never borrow money to do it.""", "Small separate jar of money", "ONLY WHAT YOU CAN LOSE"),
])

pr("""Quick pause. If this list is saving you from even one of these mistakes, please subscribe to Ryan Rover Money. It's free,
and it helps us keep making these. Now, mistake eleven.""")

item(11, "Overconfidence after early wins", "beginner's luck",
"""Mistake number eleven. Getting overconfident after early wins.""", [
("""Many beginners start investing during a rising market. Their first picks go up, and they conclude they're naturally good at
this. So they invest more aggressively, trade more often and take bigger risks.""", "Confident person celebrating", "BEGINNER'S LUCK"),
("""But in a rising market, almost everything goes up. Early gains often say more about the market than about skill. When the
market turns, the bigger risks lead to bigger losses.""", "Rising tide lifting boats", "A RISING TIDE LIFTS ALL BOATS"),
("""Research by Brad Barber and Terrance Odean found that the individual investors who traded most often earned lower returns
after costs than those who traded least. Confidence led to activity, and activity often hurt returns.""", "Research paper on desk", "MORE TRADING, LOWER RETURNS"),
("""What to do instead. Compare your results with a simple index fund over several years, including bad ones. If you're not
beating it, the index fund is the better choice.""", "Comparison chart", "BENCHMARK YOURSELF"),
])

item(12, "Checking too often", "every look is a risk",
"""Mistake number twelve. Checking your investments too often.""", [
("""Investing apps make it easy to check your balance dozens of times a day. But the more often you look, the more often you see
losses. Over short periods, markets go down quite often, even when they rise over the long run.""", "Person staring at phone", "MORE LOOKS, MORE LOSSES"),
("""Economists Shlomo Benartzi and Richard Thaler called this myopic loss aversion. Because losses feel worse than gains feel
good, investors who check often feel more pain and tend to make more cautious, emotional decisions, which can hurt long term
returns.""", "Magnifying glass on chart", "MYOPIC LOSS AVERSION"),
("""Frequent checking also creates the urge to do something. And for long term investors, doing something is often worse than
doing nothing.""", "Hand hovering over sell button", "THE URGE TO ACT"),
("""Think about it this way. If you owned a rental house, you wouldn't ask for a price quote every hour and panic when it
came in lower than yesterday. You'd look at the rent, the condition and the long term value. Treat your index funds the same
way, as long term assets you own, not as numbers on a scoreboard.""", "House with for rent sign", "THINK LIKE AN OWNER"),
("""What to do instead. Turn off price notifications, move the app off your home screen, and review your investments on a
schedule, like once a quarter or twice a year.""", "Notification settings", "CHECK ON A SCHEDULE"),
])

item(13, "Taking advice from social media", "finfluencers",
"""Mistake number thirteen. Taking investing advice from social media.""", [
("""Social media is full of people sharing stock tips, trading strategies and screenshots of huge gains. Some are honest. Some
are paid to promote products. Some are simply lucky. And it's very hard to tell which is which.""", "Influencer recording video", "WHO'S GIVING THE ADVICE?"),
("""FINRA and the SEC have warned investors about financial influencers who promote investments without disclosing that they're
being paid, and about scams that use fake testimonials and impersonations. If something promises guaranteed high returns with
little risk, that's a major red flag.""", "Red flag icon", "GUARANTEED RETURNS ARE A RED FLAG"),
("""You also only see the winners. People rarely post their losses, so social media gives a distorted picture of how investing
usually goes.""", "Highlight reel on phone", "YOU ONLY SEE THE WINS"),
("""Ask yourself how the person makes money. If they earn commissions, referral fees or sponsorships from the products they
recommend, their advice may not be neutral. That doesn't make them dishonest, but it does mean you should be more skeptical,
and look for independent sources before acting.""", "Money changing hands", "FOLLOW THE MONEY"),
("""What to do instead. Learn from sources with accountability, like books by established authors, official resources like
Investor dot gov, and fee only fiduciary advisors. And check any professional's background on FINRA's BrokerCheck.""", "BrokerCheck website", "CHECK THE SOURCE"),
])

body_hook = "Thousands of employees lost their retirement savings because of this one mistake."
item(14, "Too much in one company", "the Enron lesson",
"""Mistake number fourteen. Putting too much in one company, especially your employer.""", [
("""When Enron collapsed in 2001, many employees had a large share of their retirement savings in Enron stock. They lost their
jobs and much of their retirement money at the same time. It's one of the most painful lessons in investing history.""", "Empty office building", "THE ENRON LESSON"),
("""Owning a lot of your employer's stock feels natural. You know the company, you believe in it and sometimes it's offered at a
discount. But your paycheck already depends on that company. Putting your savings there too doubles your risk.""", "Employee badge and stock chart", "DOUBLE RISK"),
("""The same goes for any single stock. Even great companies can stumble, and research by Hendrik Bessembinder has shown that
most individual stocks have underperformed the overall market over their lifetimes.""", "Single stock falling", "ANY SINGLE STOCK CAN FAIL"),
("""What to do instead. Many financial planners suggest keeping any single stock, including your employer's, to a small share of
your portfolio, often ten percent or less. Spread the rest across broad, diversified funds.""", "Diversified pie chart", "KEEP IT SMALL"),
])

pr("""That's angle two. Panic selling, chasing winners, hype, overconfidence, checking too often, social media advice and too
much in one company. Now angle three. The playbook.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
sc("""The final six mistakes are about how people set up and manage their investments. These are often the easiest to fix,
because they don't require changing your personality, just changing your system.""",
   "Toolbox on table", "SIX SYSTEM MISTAKES")

item(15, "No written plan", "investing without a map",
"""Mistake number fifteen. Investing without a plan.""", [
("""Many beginners buy investments randomly. A stock a friend mentioned, a fund they saw online, something that seemed popular.
Without a plan, every decision is based on whatever feels right that day, and feelings change with the market.""", "Person lost with map", "NO MAP"),
("""A simple plan answers a few questions. What is this money for? When will I need it? How much will I invest each month? What
mix of stocks and bonds will I hold? And what will I do when the market crashes?""", "Plan questions on paper", "FIVE SIMPLE QUESTIONS"),
("""Professional investors often use a written investment policy statement for exactly this reason. Writing it down when you're
calm protects you from decisions made when you're emotional.""", "Signed document", "WRITE IT WHEN CALM"),
("""Your plan should also include your rules for changes. For example, I'll only change my mix if my goals or timeline
change, not because of the news. I'll review once a year. I'll increase contributions with every raise. Rules like these turn
dozens of emotional decisions into a few calm ones.""", "List of personal rules", "RULES FOR CHANGES"),
("""What to do instead. Write a one page plan this week. Keep it somewhere you'll see it, and read it before making any big
investment decision.""", "One page plan on fridge", "ONE PAGE PLAN"),
])

item(16, "Too complicated", "more funds, more confusion",
"""Mistake number sixteen. Making it too complicated.""", [
("""Some beginners think more investments means more safety. So they buy ten or fifteen funds, a handful of stocks and accounts
at several brokerages. But many of those funds often hold the same companies, so they add complexity without much real
diversification.""", "Messy desk with papers", "MORE ISN'T SAFER"),
("""Complexity makes it harder to know what you own, harder to rebalance and easier to make mistakes. It also makes it easier to
lose track of accounts and fees.""", "Confused person with spreadsheets", "COMPLEXITY CAUSES MISTAKES"),
("""Many successful investors use just two to four broad funds. Some use a single target date fund that holds a diversified mix
and adjusts it automatically over time.""", "Simple three fund setup", "TWO TO FOUR FUNDS"),
("""What to do instead. Check the top holdings of each fund you own. If several look nearly identical, simplify. A portfolio
you understand is a portfolio you can stick with.""", "Fund holdings comparison", "SIMPLIFY"),
])

item(17, "Using leverage and options too early", "borrowed risk",
"""Mistake number seventeen. Using margin, leverage or options as a beginner.""", [
("""Many trading apps make it easy to borrow money to invest, called trading on margin, or to trade options and leveraged funds.
These tools can multiply gains, but they also multiply losses, sometimes beyond what you put in.""", "Warning label on app", "MULTIPLIED LOSSES"),
("""With margin, if your investments fall far enough, your broker can demand more money or sell your holdings, often at the
worst possible time. Beginners can lose much more than they expected, very quickly.""", "Margin call notice", "MARGIN CALLS"),
("""Leveraged ETFs are designed for short term trading. Because they reset daily, their long term results can differ sharply
from what people expect. The SEC has published investor alerts about them.""", "ETF warning document", "LEVERAGED ETFS ARE SHORT TERM TOOLS"),
("""Options deserve their own warning. They can be useful tools for experienced investors, but many beginners use them as
lottery tickets, buying short term contracts that often expire worthless. Without a deep understanding of how options are
priced, it's very easy to lose your entire stake in a matter of days.""", "Expired ticket", "OPTIONS AS LOTTERY TICKETS"),
("""What to do instead. Stick with simple, unleveraged investments until you have years of experience, and understand exactly
how any complex product works before using it.""", "Simple investment screen", "KEEP IT SIMPLE"),
])

item(18, "Never rebalancing", "letting risk drift",
"""Mistake number eighteen. Never rebalancing.""", [
("""Say you start with seventy percent stocks and thirty percent bonds. After a few strong years for stocks, you might drift to
eighty five percent stocks without noticing. Your portfolio is now riskier than you planned.""", "Pie chart shifting", "YOUR RISK DRIFTS"),
("""Rebalancing means bringing your mix back to your target. You trim what grew and add to what lagged. It forces you to sell a
bit high and buy a bit low, the opposite of what emotions usually push you to do.""", "Balancing scale", "SELL HIGH, BUY LOW"),
("""Target date funds rebalance automatically. If you hold separate funds, a yearly check is plenty for most people.""", "Annual calendar", "ONCE A YEAR"),
("""What to do instead. Pick a date each year to check your mix. If it has drifted more than about five percentage points,
rebalance, ideally using new contributions to avoid selling.""", "Birthday calendar reminder", "PICK A DATE"),
])

item(19, "Forgetting old accounts and beneficiaries", "the paperwork mistakes",
"""Mistake number nineteen. Forgetting old accounts and beneficiaries.""", [
("""People change jobs many times over a career, and old retirement accounts get left behind. Some studies estimate there are
millions of forgotten four oh one k accounts in the United States, holding large amounts of money. Old accounts can carry
higher fees and are easy to lose track of.""", "Old paperwork in box", "FORGOTTEN ACCOUNTS"),
("""Another overlooked detail is beneficiaries. Retirement accounts usually pass to whoever is named as beneficiary on the
account, which can override what a will says. An outdated beneficiary can send money to the wrong person.""", "Beneficiary form", "UPDATE BENEFICIARIES"),
("""Neither of these is exciting, which is exactly why they get ignored. But a single afternoon of paperwork can protect years of
savings.""", "Person filing documents", "BORING BUT IMPORTANT"),
("""If you think you might have lost track of an old account, there are ways to look. Contact former employers' benefits
departments, check old statements, and search the Department of Labor's retirement savings lost and found database, created
under recent federal legislation to help people find old plans.""", "Searching database on laptop", "FIND LOST ACCOUNTS"),
("""What to do instead. List every account you've ever had. Consider rolling old workplace plans into your current plan or an
IRA, and check the beneficiaries on each one.""", "Account checklist", "LIST EVERY ACCOUNT"),
])

item(20, "Never increasing contributions", "stuck at the starting amount",
"""Mistake number twenty. Never increasing what you invest.""", [
("""Many beginners start investing a small amount, which is great, and then never change it. Ten years later, they earn much
more, but they're still investing the same amount as when they started.""", "Same small coin pile", "STUCK AT THE START"),
("""Economists Richard Thaler and Shlomo Benartzi designed Save More Tomorrow, where employees agreed in advance to increase
their savings rate with each raise. Participants in their study ended up saving far more than before.""", "Escalator going up", "SAVE MORE TOMORROW"),
("""Increasing contributions over time can matter as much as the return you earn. Your investing should grow as your income
grows.""", "Growing staircase", "GROW WITH YOUR INCOME"),
("""What to do instead. Turn on automatic increases in your retirement plan if it offers them, or set a yearly reminder to raise
your contributions by one percent of your income.""", "Auto increase setting", "ONE PERCENT MORE EACH YEAR"),
])

# ---------------- Why 2027 ----------------
ch("Why these mistakes are easier than ever")
sc("""Why are these mistakes so common now? Part of the reason is that investing apps have made trading feel like a game.
Colorful animations, constant notifications and one tap trades make it easy to act on impulse. Regulators have raised concerns
about these game like features and how they can encourage frequent trading.""",
   "Gamified trading app", "INVESTING FEELS LIKE A GAME")
sc("""Another reason is the flood of information. Videos, posts, chat groups and online tools all offer opinions, predictions
and tips. More information doesn't automatically mean better decisions. Often it means more noise, more temptation and more
confusion.""",
   "Flood of notifications", "MORE NOISE THAN EVER")
sc("""And scammers have new tools too. Fake investment platforms, impersonations of well known investors and too good to be true
offers are common. The basic rules still protect you. Never send money to someone you only know online, verify every platform
and professional, and walk away from guaranteed returns.""",
   "Fake website warning", "SCAMS ARE EVOLVING")

# ---------------- Checklist ----------------
ch("The beginner investor checklist")
pr("""Let's turn all twenty mistakes into a simple checklist. If you can tick these boxes, you're ahead of most beginners.""")
sc("""Box one. I have a starter emergency fund, and I'm building toward three to six months of essential expenses. Box two. I
have no credit card debt, or I have a clear plan to pay it off, highest rate first. These two boxes protect everything else you
build, because they stop a single bad month from forcing you to sell or borrow at the worst time.""",
   "Checklist with first two boxes ticked", "BOXES 1 AND 2: PROTECTION")
sc("""Box three. I contribute at least enough to get my full employer match. Box four. I use tax advantaged accounts, like a four
oh one k or an IRA, before a regular taxable account where that makes sense. These two boxes are the closest thing investing
has to free money, and skipping them is one of the most common and expensive beginner mistakes.""",
   "Retirement plan paperwork", "BOXES 3 AND 4: FREE MONEY")
sc("""Box five. My money is in broad, low cost funds, and I know the expense ratio of every one. Box six. I own two to four funds,
or a single target date fund, and I understand what each one holds. Simple and cheap is not a compromise. For most people, it's
the strategy that works best over decades.""",
   "Simple portfolio on screen", "BOXES 5 AND 6: SIMPLE AND CHEAP")
sc("""Box seven. My contributions are automatic, and they increase every year. Box eight. I have a one page written plan, including
what I'll do in a crash. Box nine. I review my portfolio once or twice a year and rebalance if needed. Box ten. My beneficiaries
are up to date, and I know where every account is.""",
   "Checklist fully ticked", "BOXES 7 TO 10: THE SYSTEM")
sc("""Ten boxes. None of them require predicting the market, picking stocks or watching the news. That's the secret most beginners
miss. Successful investing is mostly about building a good system and then leaving it alone long enough to work.""",
   "Calm person closing laptop", "BUILD THE SYSTEM, THEN LEAVE IT")

# ---------------- By age ----------------
ch("Mistakes by age")
sc("""In your twenties, the biggest mistakes are usually waiting, chasing hype and carrying expensive debt. Your greatest asset is
time, so the best move is to start small, automate and avoid gambling with money you'll need. Even modest amounts invested now
have decades to compound.""",
   "Young adult at laptop", "IN YOUR 20s")
sc("""In your thirties and forties, the big risks shift. Lifestyle creep, skipping increases as income rises, too much employer
stock and forgotten old accounts from job changes. This is the stage to raise contributions, consolidate accounts and protect
your family with insurance and updated beneficiaries.""",
   "Family at home", "IN YOUR 30s AND 40s")
sc("""In your fifties and beyond, the biggest mistakes are often taking too much risk too close to needing the money, or panicking
and selling everything after a drop. A thoughtful mix of stocks, bonds and cash, plus catch up contributions after fifty, can
help. Check current limits with the IRS.""",
   "Mature couple planning retirement", "IN YOUR 50s AND BEYOND")

# ---------------- Story ----------------
ch("Two beginners")
short("Two beginners started investing the same year. Only one made money.")
sc("""Imagine two beginners who both start investing three hundred dollars a month. The first one downloads a trading app, buys
whatever is trending, checks constantly, sells during the first big drop and jumps back in after prices recover. After a few
years, they've paid more in taxes, missed the rebound and feel that investing doesn't work.""",
   "Stressed young person with phone", "BEGINNER ONE")
sc("""The second one opens a retirement account, gets the full employer match, picks one low cost target date fund, automates
contributions and checks twice a year. During the same drop, they keep investing, buying shares at lower prices. Their plan is
boring, and it's working.""",
   "Calm young person with coffee", "BEGINNER TWO")
sc("""Same income. Same market. Same starting amount. The difference wasn't intelligence or luck. It was avoiding a handful of
basic mistakes. That's the real secret of beginner investing.""",
   "Two paths diverging", "THE DIFFERENCE WAS MISTAKES")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. What's the single biggest mistake? For most people, it's not starting, or starting late. Time in the market
is the ingredient you can't buy back. Many other mistakes can be fixed later. Lost years can't.""",
   "Hourglass", "THE BIGGEST MISTAKE")
sc("""Question two. I've already made some of these mistakes. Is it too late? Not at all. Almost every investor has made some of
them. The best time to fix them is now. Simplify, cut fees, automate, and keep going.""",
   "Person starting fresh", "IS IT TOO LATE?")
sc("""Question three. Do I need a financial advisor? Not necessarily. Many people do well with a simple, low cost plan on their
own. If you want help, look for a fee only fiduciary, who's required to act in your best interest, and understand exactly what
you're paying.""",
   "Advisor meeting", "DO I NEED AN ADVISOR?")

sc("""Question four. Should I invest a lump sum all at once, or spread it out? Historically, investing a lump sum right away has
often come out ahead, because markets have risen more often than they've fallen. But spreading it over several months can feel
easier emotionally. Either is far better than leaving money uninvested for years while you decide.""",
   "Lump sum versus monthly chart", "LUMP SUM OR SPREAD IT?")
sc("""Question five. How much should I have in stocks versus bonds? It depends on your timeline and how well you handle drops. A
common starting point is to hold more stocks when your goal is decades away and gradually add bonds as it gets closer. Target
date funds do this for you automatically.""",
   "Stocks and bonds pie chart", "STOCKS OR BONDS?")
sc("""Question six. Is it okay to invest if I don't understand everything yet? Yes. You don't need to understand every detail to
start with a simple, diversified, low cost fund. You can keep learning while your money works. Just avoid anything complex you
can't explain in a sentence or two.""",
   "Person reading investing book", "DO I NEED TO KNOW EVERYTHING?")

# ---------------- Recap ----------------
ch("Recap")
sc("""Quick recap. Angle one, the numbers. Waiting, fees, skipping the match, expensive debt, no emergency fund, expecting smooth
returns and ignoring taxes.""",
   "Checklist on clipboard", "THE NUMBERS: 1 TO 7")
sc("""Angle two, the psychology. Panic selling, chasing winners, hype, overconfidence, checking too often, social media advice and
too much in one company.""",
   "Person thinking", "THE PSYCHOLOGY: 8 TO 14")
sc("""Angle three, the playbook. No plan, too much complexity, leverage too early, never rebalancing, forgotten accounts and
never increasing contributions.""",
   "Notebook with plan", "THE PLAYBOOK: 15 TO 20")

# ---------------- Close ----------------
ch("What to do next")
pr("""You don't need to be brilliant to invest well. You just need to avoid the big mistakes, keep it simple and give it time. If
you want my full step by step plan, it's in my playbook, linked in the description. Tell me in the comments, which of these
mistakes have you made? I'm Ryan Rover. See you in the next one.""")

save("video35", "20 Investing Mistakes Beginners Make in 2027", [
    "Investment Company Institute, Investment Company Fact Book: fund expense ratios",
    "Federal Reserve, G.19 Consumer Credit (credit card interest rates)",
    "S&P Dow Jones Indices, SPIVA and Persistence Scorecards",
    "IRS, retirement accounts, contribution limits and capital gains tax rules",
    "SEC and FINRA investor alerts (pump and dump, finfluencers, leveraged ETFs, margin)",
    "Benartzi and Thaler, Myopic Loss Aversion and the Equity Premium Puzzle (Quarterly Journal of Economics, 1995)",
    "Barber and Odean, Trading Is Hazardous to Your Wealth (Journal of Finance, 2000)",
    "Thaler and Benartzi, Save More Tomorrow (Journal of Political Economy, 2004)",
    "Hendrik Bessembinder, Do Stocks Outperform Treasury Bills? (Journal of Financial Economics, 2018)",
    "Enron collapse (2001) and employee retirement losses, news and congressional record",
    "Growth examples: monthly compounding at stated average yearly returns (illustrations, not promises)",
], "20 beginner investing mistakes, from 3 angles: numbers, psychology, playbook")
