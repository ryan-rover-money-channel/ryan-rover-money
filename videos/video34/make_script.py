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
pr("""Hi, I'm Ryan Rover. What if the best investing strategy for most people was also the most boring one? No stock
picking. No watching the news. No guessing what the market will do next. Just buying the whole market, cheaply, and holding
it for decades. That's what an index fund does. And today I'm going to show you why boring investing beats most of the
experts, from three different angles.""")
short("Most professional fund managers lose to this boring investment.")
card("""Here's the headline. In recent SPIVA reports from S and P Dow Jones Indices, roughly nine out of ten actively
managed large company U.S. stock funds trailed the S and P five hundred over fifteen years. The professionals, with all
their research, mostly lost to a simple index.""",
     {"type": "stat", "label": "Active large-cap funds that trailed the S&P 500", "big": "~9 in 10", "sub": "over 15 years, recent SPIVA U.S. scorecards"})
sc("""That sounds unbelievable, so let's be careful about what it means. These are professional fund managers, with teams
of analysts, expensive data and years of experience. Many of them are genuinely smart. But after fees and trading costs,
most of them still end up behind a fund that simply buys every company in the index and does almost nothing. Over long
periods, doing less has usually won.""",
   "Fund managers in office", "THE PROS MOSTLY LOST")
sc("""We'll explore this from three angles. First, the numbers. What an index fund is, why costs matter so much, and how
the math of averages works in your favor. Second, the psychology. Why boring is so hard for humans, and why that's exactly
why it works. And third, the playbook. How to actually start investing in index funds, step by step. Quick reminder, this
is education, not financial advice, and past results don't guarantee future returns.""",
   "Three paths in a park", "THREE ANGLES")
pr("""Let's start with the numbers. And first, what exactly is an index fund?""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our numbers. Fund performance comparisons come from S and P Dow Jones Indices' SPIVA scorecards. Fee data comes from
the Investment Company Institute. Warren Buffett's bet and advice come from his Berkshire Hathaway shareholder letters.
Investor behavior data comes from Morningstar's Mind the Gap research. Growth examples use monthly compounding at a stated
average yearly return, as illustrations, not promises.""",
   "Financial reports on desk", "OUR NUMBERS")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Seven lessons about how index funds actually work, and why the math favors them.""")

item(1, "What an index fund is", "buy the whole market",
"""Lesson number one. An index fund buys the whole market, or a big slice of it.""", [
("""An index is just a list of companies, chosen by a set of rules. The S and P five hundred, for example, tracks about five
hundred of the largest publicly traded companies in the United States. An index fund simply buys all the companies on that
list, in roughly the same proportions, so its performance follows the index.""", "List of company names", "AN INDEX IS A LIST"),
("""So when you buy one share of an S and P five hundred index fund, you own a tiny piece of hundreds of companies at once.
Technology companies, banks, retailers, health care, energy. One purchase gives you a slice of a large part of the American
economy, instead of betting on a single business.""", "Pie chart of sectors", "ONE SHARE, HUNDREDS OF COMPANIES"),
("""There are index funds for almost everything. Total U.S. stock market funds hold thousands of companies, large and small.
International index funds hold companies outside the United States. Bond index funds hold thousands of bonds. The idea is
always the same. Don't try to pick winners. Own the whole haystack.""", "Haystack in field", "OWN THE HAYSTACK"),
("""Index funds come as mutual funds or as exchange traded funds, usually called ETFs. ETFs trade during the day like stocks,
while mutual funds trade once a day at the closing price. For a long term investor, either can work well. The fund's cost and
what it holds matter far more than the format.""", "Brokerage app showing ETF", "MUTUAL FUND OR ETF"),
])

item(2, "Bogle's folly", "the idea everyone laughed at",
"""Lesson number two. The idea Wall Street laughed at.""", [
("""In 1975, John Bogle founded Vanguard. The next year, his company launched one of the first index mutual funds available
to ordinary investors, tracking the S and P five hundred. Critics mocked it. Some called it Bogle's folly. Why would anyone
settle for average returns, they asked, when you could hire a manager to beat the market?""", "Vintage newspaper", "BOGLE'S FOLLY"),
("""Bogle's answer was simple arithmetic. Before costs, all investors together earn the market's return, because together
they are the market. After costs, the average investor must earn less than the market. So a fund that charges very little and
simply matches the market should beat most investors who pay more, over time.""", "Simple math on chalkboard", "THE ARITHMETIC"),
("""It took decades, but Bogle's idea won. According to Morningstar, by early 2024, assets in passive funds in the United
States, mostly index funds, had overtaken assets in actively managed funds. The folly became the mainstream.""", "Graph lines crossing", "THE FOLLY WON"),
("""Try this. Next time someone tells you they have a strategy to beat the market, ask a simple question. Have you beaten a
low cost index fund over the last fifteen years, after all fees? Most people, and most professionals, can't say yes.""", "Two people talking", "ASK THIS QUESTION"),
])

body_hook = "A tiny fee can cost you two hundred thousand dollars. Here's the math."
item(3, "Costs are everything", "the fee that compounds",
"""Lesson number three. Costs matter more than almost anything.""", [
("""Every fund charges a yearly fee called an expense ratio. According to the Investment Company Institute, in recent years
the average index equity mutual fund charged around five hundredths of a percent, while the average actively managed equity
fund charged around sixty five hundredths of a percent. That difference sounds tiny. It isn't.""", "Fee table on document", "0.05% VS 0.65%"),
("""Imagine investing five hundred dollars a month for forty years with a seven percent average yearly return before fees.
With a five hundredths of a percent fee, you'd end with roughly one point two nine million dollars. With a sixty five
hundredths of a percent fee, roughly one point one million. That's around two hundred thousand dollars lost to fees.""", "Two stacks of money", "ABOUT $200,000 LOST TO FEES"),
("""Why so much? Because fees compound too. Every dollar taken in fees is a dollar that never grows again, along with all
the growth it would have earned for decades. And unlike returns, fees are guaranteed. You pay them in good years and bad.""", "Coins slipping through fingers", "FEES COMPOUND TOO"),
("""Try this. Look up the expense ratio of every fund you own. It's listed on the fund's page. If any are above half a
percent, check whether a low cost index fund covers the same part of the market.""", "Person checking fund page", "CHECK YOUR EXPENSE RATIOS"),
])

item(4, "Why the pros lose", "the math of beating average",
"""Lesson number four. Why most professionals lose to the index.""", [
("""It's not that fund managers are bad at their jobs. It's that beating the market is incredibly hard. Every time a
professional buys a stock, another professional is usually selling it. They can't both be right. Together, they're competing
against each other, and the competition is fierce.""", "Traders on trading floor", "PROS COMPETE WITH PROS"),
("""Then come the costs. Active funds pay for research, analysts and frequent trading. Those costs come out of returns
every year. So even a manager who picks slightly better stocks than average can end up behind the index once costs are
subtracted.""", "Calculator subtracting costs", "COSTS DRAG RETURNS"),
("""And even the funds that do win often don't keep winning. S and P Dow Jones Indices also publishes persistence
scorecards, which track whether top performing funds stay on top. Historically, relatively few do. Picking last year's
winning fund is no guarantee of picking next year's.""", "Trophy falling over", "WINNERS RARELY REPEAT"),
("""Try this. If you're paying for an actively managed fund, compare its fifteen year return after fees with a similar
index fund. Numbers usually settle the debate quickly.""", "Comparison chart on laptop", "COMPARE 15 YEARS"),
])

item(5, "Diversification for free", "no single point of failure",
"""Lesson number five. Diversification you get almost for free.""", [
("""When you own one company's stock, your money depends on that one business. If it fails, you can lose everything you put
in. History is full of companies that once seemed unstoppable and later collapsed or disappeared.""", "Closed store with sign", "ONE COMPANY CAN FAIL"),
("""An index fund spreads your money across hundreds or thousands of companies. If one fails, it's a tiny piece of the fund.
Meanwhile, the companies that grow into giants automatically become bigger parts of the index. You don't need to know in
advance which ones they'll be.""", "Many small boats in harbor", "WINNERS GROW AUTOMATICALLY"),
("""Research by Hendrik Bessembinder found that a small share of stocks created most of the U.S. stock market's long term
wealth, while many individual stocks did worse than safe Treasury bills over their lifetimes. Owning the whole market is the
easiest way to make sure you own the rare big winners.""", "Few tall bars on chart", "A FEW STOCKS DO MOST OF THE WORK"),
("""Try this. If most of your investments are in one or two stocks, especially your employer's, think about whether you'd be
okay if that company had a terrible decade. If the answer is no, an index fund can spread that risk.""", "Person thinking at desk", "TOO MUCH IN ONE STOCK?"),
])

item(6, "Taxes and turnover", "less trading, fewer taxes",
"""Lesson number six. Index funds are often tax efficient.""", [
("""When a fund sells investments at a profit, it may have to distribute capital gains to its shareholders. In a regular
taxable brokerage account, you can owe taxes on those distributions, even if you didn't sell a single share yourself.""", "Tax form close up", "FUNDS CAN CREATE TAXES"),
("""Active funds often trade a lot, which can create more of these taxable gains. Index funds usually trade much less,
because they only change holdings when the index changes. Less trading usually means fewer taxable distributions.""", "Low turnover illustration", "LESS TRADING, FEWER TAXES"),
("""Many index ETFs are especially tax efficient because of how ETF shares are created and redeemed. That's one reason they're
popular for taxable accounts. In retirement accounts like a four oh one k or IRA, this matters less, because growth there is
tax deferred or tax free.""", "ETF on screen", "ETFS CAN BE EVEN MORE EFFICIENT"),
("""Try this. If you invest in a regular taxable account, check your funds' history of capital gains distributions. Low
distributions mean more of your money stays invested and compounding.""", "Person reviewing statement", "CHECK DISTRIBUTIONS"),
])

item(7, "The market's long run", "boring, not risk free",
"""Lesson number seven. Boring doesn't mean risk free.""", [
("""Here's an honest warning. An index fund follows the market, and that includes the bad times. In 2008, the S and P five
hundred fell by more than a third. In early 2020, it dropped sharply in a matter of weeks. An index fund doesn't avoid these
drops. It goes through them.""", "Red market chart crash", "IT FALLS WITH THE MARKET"),
("""Historically, the broad U.S. market has recovered from its past crashes and gone on to new highs, though recoveries
sometimes took years. That's why index funds work best for money you won't need for a long time, often five years or more.""", "Chart recovering upward", "RECOVERIES TAKE TIME"),
("""Bond index funds and cash can balance the ups and downs for money you need sooner, or for people who can't stomach big
drops. Many investors hold a mix, more stocks when they're young, more bonds as they get closer to needing the money.""", "Balanced scale", "MIX STOCKS AND BONDS"),
("""Try this. Ask yourself honestly. If my investments fell thirty percent next year, would I sell? If yes, you may want
more bonds in your mix, so you can stay invested through the hard times.""", "Person reflecting", "KNOW YOUR LIMIT"),
])

pr("""That's angle one. What an index fund is, Bogle's folly, costs, why the pros lose, diversification, taxes, and boring
but not risk free. Now angle two. The psychology.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
sc("""If index funds are so effective, why doesn't everyone just buy them and relax? Because human brains crave excitement,
control and stories. Index investing offers none of that. In this angle, we'll look at seven psychological reasons boring
investing is hard, and why getting past them is where the real returns come from.""",
   "Brain illustration", "WHY BORING IS HARD")

item(8, "The excitement trap", "boring feels wrong",
"""Lesson number eight. Our brains want excitement.""", [
("""Picking stocks feels exciting. Researching a company, buying it, watching it jump. It's like a game. Buying an index fund
and leaving it alone feels like doing nothing. And many people assume that doing nothing must be a mistake.""", "Person excited at trading screen", "STOCK PICKING FEELS FUN"),
("""Economist Paul Samuelson reportedly said investing should be more like watching paint dry or watching grass grow. If you
want excitement, he suggested, take eight hundred dollars and go to Las Vegas. His point was that excitement is often a sign
of risk, not skill.""", "Paint drying on wall", "LIKE WATCHING PAINT DRY"),
("""That doesn't mean you can never pick a stock. But it helps to separate your money. Keep your serious, long term money in
boring index funds, and if you want some fun, use a small amount you can afford to lose.""", "Two jars labeled", "SEPARATE FUN MONEY"),
("""Try this. If you enjoy stock picking, cap it at five percent of your investments. Then compare its results to your index
funds after a few years. The comparison is often eye opening.""", "Five percent on screen", "CAP IT AT 5%"),
])

item(9, "Overconfidence", "everyone thinks they're above average",
"""Lesson number nine. Overconfidence costs money.""", [
("""Most people believe they're above average drivers, and many investors believe they're above average stock pickers. But
by definition, not everyone can be above average. Overconfidence leads people to trade more, take bigger risks and pay more
in costs.""", "Confident person with sunglasses", "EVERYONE THINKS THEY'RE ABOVE AVERAGE"),
("""Brad Barber and Terrance Odean studied tens of thousands of household brokerage accounts. They found that the investors
who traded the most earned noticeably lower returns than those who traded the least. Their paper's title says it all.
Trading is hazardous to your wealth.""", "Research paper", "TRADING IS HAZARDOUS"),
("""Index investing is a kind of humility. It accepts that you probably can't predict which stocks will win, and turns that
humility into an advantage. You stop competing in a game that's very hard to win, and simply collect the market's return.""", "Humble person smiling", "HUMILITY AS A STRATEGY"),
("""Try this. Write down every investment decision you make this year, with the reason. A year later, check how they turned
out. Most people find their predictions were far less reliable than they felt.""", "Investment journal", "KEEP A DECISION JOURNAL"),
])

body_hook = "Most investors earn less than the funds they own. Here's why."
item(10, "The behavior gap", "good funds, bad timing",
"""Lesson number ten. Investors often earn less than their own funds.""", [
("""Here's something surprising. Morningstar's Mind the Gap research compares the returns funds report with the returns their
investors actually receive. Investors often earn less than the funds they own, because they buy after prices rise and sell
after prices fall. In recent studies, that gap was roughly one percentage point a year.""", "Gap between two lines", "THE BEHAVIOR GAP"),
("""One percentage point might not sound like much, but over decades it's enormous. One hundred thousand dollars growing at
seven percent a year for thirty years becomes roughly seven hundred sixty thousand. At six percent, roughly five hundred
seventy thousand. Bad timing can cost almost two hundred thousand dollars.""", "Two growth curves", "BAD TIMING IS EXPENSIVE"),
("""Index funds don't fix this by themselves. You can buy and sell an index fund at the wrong times too. The advantage comes
when you pair index funds with automatic investing and a commitment to hold. The fund is boring, and your behavior has to be
boring too.""", "Automatic investment confirmation", "BORING FUND, BORING BEHAVIOR"),
("""Try this. Set up automatic monthly investing, and decide in advance that you'll only review your portfolio once or twice a
year. Fewer looks usually mean fewer mistakes.""", "Calendar with two review dates", "LOOK LESS OFTEN"),
])

pr("""Quick pause. If boring investing is starting to make sense, please subscribe to Ryan Rover Money. It's free, and it helps
us keep making these. Now, lesson eleven.""")

item(11, "Headlines and noise", "the news isn't a plan",
"""Lesson number eleven. Ignore most financial news.""", [
("""Financial news is designed to keep you watching. Markets soar, markets plunge, experts predict a crash, other experts
predict a boom. Every day there's a new reason to act. But for a long term index investor, most of it is noise.""", "Breaking news on TV", "NEWS IS NOISE"),
("""Predictions are especially unreliable. Market forecasts from experts have a long history of being wrong, in both
directions. If someone could reliably predict the market, they probably wouldn't be telling you on television.""", "Crystal ball", "PREDICTIONS ARE UNRELIABLE"),
("""The index investor's advantage is not needing to know what happens next. You own the whole market, so whatever happens,
you get the market's result. That frees you from needing to react to every headline.""", "Calm person reading book", "YOU DON'T NEED TO KNOW"),
("""Try this. Unfollow or mute the market news sources that make you anxious. Replace them with one or two good books about
long term investing.""", "Phone unfollow button", "MUTE THE NOISE"),
])

item(12, "Fear of missing out", "chasing the hot thing",
"""Lesson number twelve. Fear of missing out.""", [
("""Every few years there's a new hot investment. A sector, a coin, a single stock everyone's talking about. Index investors
watch other people brag about huge gains and feel left behind. That feeling is called fear of missing out, and it pushes
people to abandon good plans.""", "People cheering at screen", "FEAR OF MISSING OUT"),
("""The hot investment sometimes does keep rising for a while. But many manias end painfully, and the people who join late
often buy near the top. Meanwhile, the index investor already owns many of the companies that become truly big, without
having to guess.""", "Bubble popping", "MANIAS OFTEN END BADLY"),
("""Remember, you only hear about the winners. The people who lost money on the last hot thing rarely post about it. Your
picture of how everyone else is doing is badly biased.""", "Social media highlight reel", "YOU ONLY SEE WINNERS"),
("""Try this. When you feel the urge to chase something hot, wait thirty days before acting. Most urges fade, and the ones
that don't deserve careful thought.""", "Thirty day calendar", "WAIT 30 DAYS"),
])

item(13, "Average is extraordinary", "the paradox of settling",
"""Lesson number thirteen. Average returns create above average results.""", [
("""Many people hate the idea of settling for average returns. But here's the paradox. Because most active investors trail
the market after costs, simply earning the market's return puts you ahead of most of them over long periods.""", "Podium with medals", "AVERAGE BEATS MOST"),
("""Think of it like a marathon where most runners carry heavy backpacks full of fees, trading costs and bad timing. You run
at an average pace, but with no backpack. You end up finishing ahead of most of the field.""", "Marathon runners", "NO BACKPACK"),
("""And average returns, compounded for decades, can be life changing. Three hundred dollars a month for thirty years at a
seven percent average yearly return grows to roughly three hundred sixty six thousand dollars. No genius required.""", "Growing savings chart", "AVERAGE CAN BE LIFE CHANGING"),
("""Try this. Stop measuring yourself against the best investor you've heard of. Measure yourself against what you'd have if
you did nothing at all. That's the real comparison.""", "Person comparing notes", "THE REAL COMPARISON"),
])

item(14, "The power of not deciding", "fewer decisions, better results",
"""Lesson number fourteen. Fewer decisions, better results.""", [
("""Every investing decision is a chance to make a mistake. Which stock, when to buy, when to sell, which manager, which
strategy. Index investing removes most of those decisions. You choose a few funds and a mix, and then keep buying.""", "Fork in the road", "EVERY DECISION IS A RISK"),
("""Fewer decisions also means less stress. You don't have to research companies every weekend or worry about every
earnings report. Your time and attention are freed up for your career, your family and your life.""", "Family having picnic", "LESS STRESS"),
("""That's why many index investors use something like a three fund portfolio, a U.S. stock index fund, an international
stock index fund and a bond index fund. Or even a single target date fund that handles the mix automatically.""", "Three jars", "THE THREE FUND PORTFOLIO"),
("""Try this. Write down your investing plan on one page. Which funds, what percentages, how much each month. If your plan
doesn't fit on one page, it may be too complicated.""", "One page plan", "ONE PAGE PLAN"),
])

pr("""That's angle two. The excitement trap, overconfidence, the behavior gap, headlines, fear of missing out, the paradox of
average and the power of not deciding. Now angle three. The playbook.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
sc("""Let's turn this into action. Six moves to start investing in index funds the right way. You can do most of them in an
afternoon, and then let time and consistency do the rest.""",
   "Toolbox on table", "SIX MOVES")

item(15, "Pick the right account", "where your funds live",
"""Move number fifteen. Pick the right account first.""", [
("""Before you choose a fund, choose where it lives. If your employer offers a four oh one k with a match, that's often the
best place to start, because the match is an immediate return. Most plans offer at least one low cost index fund.""", "Employee benefits paperwork", "START WITH THE MATCH"),
("""Next, many people open an IRA, either traditional or Roth, at a low cost brokerage. Roth IRA contributions are made with
after tax money, but qualified withdrawals in retirement are tax free. There are income limits and yearly contribution
limits, so check the current rules on the IRS website.""", "IRA account opening", "THEN AN IRA"),
("""After that, a regular taxable brokerage account gives you flexibility with no contribution limits. Index ETFs are often a
good fit there because of their tax efficiency.""", "Brokerage account screen", "THEN A TAXABLE ACCOUNT"),
("""Try this. Log into your employer's retirement plan and find the list of investment options. Look for the words index,
S and P five hundred, total market or target date, and check each fund's expense ratio.""", "Retirement plan fund list", "FIND THE INDEX OPTIONS"),
])

item(16, "Choose simple funds", "broad and cheap",
"""Move number sixteen. Choose broad, cheap funds.""", [
("""Look for funds that cover a big part of the market, like a total U.S. stock market fund, an S and P five hundred fund or
a total world stock fund. The broader the fund, the less you depend on any single company or sector.""", "World map with markets", "BROAD MARKET FUNDS"),
("""Then compare costs. Many broad index funds charge less than one tenth of one percent a year. Between two funds that track
the same index, the cheaper one usually comes out ahead over time.""", "Two fund cards compared", "CHEAPER USUALLY WINS"),
("""If you want maximum simplicity, consider a target date fund. You pick the fund with the year closest to your expected
retirement, and it holds a mix of stock and bond index funds that gradually becomes more conservative. Just check its expense
ratio, because target date fund costs vary.""", "Target date fund brochure", "TARGET DATE FUNDS"),
("""Try this. Choose no more than three funds to start. Simple portfolios are easier to stick with, and sticking with it is
what matters most.""", "Three simple icons", "THREE FUNDS OR FEWER"),
])

body_hook = "The secret to index funds isn't which one you pick. It's this."
item(17, "Automate it", "set it and mostly forget it",
"""Move number seventeen. Automate your contributions.""", [
("""Set up automatic investments on payday, every month. When the money moves before you see it, you're not tempted to spend
it, and you're not tempted to wait for the perfect moment to buy.""", "Calendar with payday", "AUTOMATE ON PAYDAY"),
("""Investing a fixed amount on a regular schedule is often called dollar cost averaging. When prices are high, your money buys
fewer shares. When prices are low, it buys more. You don't need to time anything.""", "Shares bought at different prices", "DOLLAR COST AVERAGING"),
("""Also turn on automatic dividend reinvestment. Index funds pay dividends from the companies they own, and reinvesting them
buys more shares, which keeps compounding running.""", "Dividend reinvestment toggle", "REINVEST DIVIDENDS"),
("""Try this. Set up your automatic investment today, even if it's small. Then add a reminder to increase it whenever your pay
goes up.""", "Phone reminder", "START TODAY"),
])

item(18, "Rebalance once a year", "keep your mix",
"""Move number eighteen. Rebalance once a year.""", [
("""Over time, your mix drifts. If stocks grow faster than bonds, your portfolio becomes riskier than you planned. Rebalancing
means selling a little of what grew and buying a little of what lagged, to get back to your target.""", "Balance scale tipping", "YOUR MIX DRIFTS"),
("""Once a year is plenty for most people. Some people rebalance only when their mix drifts more than five percentage points
from the target. Either approach is fine. What matters is having a rule.""", "Annual calendar reminder", "ONCE A YEAR IS PLENTY"),
("""In retirement accounts, rebalancing usually doesn't trigger taxes. In taxable accounts, you can often rebalance just by
directing new money into whatever is underweight, which avoids selling.""", "New money arrow", "USE NEW MONEY TO REBALANCE"),
("""Try this. Pick a date, like your birthday, and make it your yearly portfolio check. Rebalance if needed, then leave it alone
for another year.""", "Birthday cake calendar", "YOUR BIRTHDAY CHECKUP"),
])

item(19, "Stay the course", "the hardest move",
"""Move number nineteen. Stay the course.""", [
("""Bogle's favorite advice was two words. Stay the course. It sounds easy, but it's the hardest part of index investing.
When markets crash, every instinct tells you to sell. When markets boom, every instinct tells you to chase.""", "Ship on stormy sea", "STAY THE COURSE"),
("""The investors who do best with index funds are often the ones who do the least. They keep buying through crashes, don't
chase booms and let decades of compounding work.""", "Calm sailor at helm", "DO THE LEAST"),
("""It helps to have a written plan and an emergency fund. The plan reminds you why you invested. The emergency fund means you
never have to sell investments in a downturn to pay a surprise bill.""", "Written plan and emergency jar", "PLAN PLUS CUSHION"),
("""Try this. Write one sentence at the top of your investing plan. I will not sell my index funds because of the news. Read
it when the market feels scary.""", "Handwritten sentence", "ONE SENTENCE RULE"),
])

item(20, "Let time do the work", "decades, not days",
"""Move number twenty. Let time do the heavy lifting.""", [
("""Index investing is a decades long strategy. The returns you see in any single year can be wildly different from the
long term average. But over twenty, thirty or forty years, the ups and downs tend to smooth out, and compounding takes over.""", "Long road into distance", "DECADES, NOT DAYS"),
("""Five hundred dollars a month for forty years at a seven percent average yearly return grows to roughly one point three
million dollars before fees. You'd contribute two hundred forty thousand. The rest would be growth. That's what patience
can do.""", "Growing money tree", "ABOUT $1.3 MILLION"),
("""And the beauty is, it doesn't require you to be brilliant. It requires you to start, keep costs low, keep contributing and
not panic. Ordinary people with ordinary incomes have built real wealth this way.""", "Ordinary family at home", "NO GENIUS REQUIRED"),
("""Try this. Calculate what your current monthly investment could become in thirty years at seven percent. Let that number
remind you why boring is worth it.""", "Calculator on desk", "SEE YOUR NUMBER"),
])

# ---------------- One afternoon ----------------
ch("Getting started in one afternoon")
pr("""Let's make this really concrete. Here's what getting started with index funds can look like, in a single afternoon.""")
sc("""Hour one. Check your workplace plan. Log into your four oh one k or similar plan, find out whether your employer offers a
match, and make sure you contribute at least enough to get the full match. Then look at the fund list and find the lowest cost
broad index fund or target date fund. Switching your contributions there usually takes just a few clicks.""",
   "Person at laptop with coffee", "HOUR ONE: YOUR WORK PLAN")
sc("""Hour two. Open an IRA at a low cost brokerage, if you're eligible. You'll need basic personal information and your bank
details. Then fund it with whatever amount you can, even a small one. Choose a broad index fund or ETF, or a single target date
fund if you want everything handled in one place.""",
   "Online account sign up form", "HOUR TWO: OPEN AN IRA")
sc("""Hour three. Automate. Set a monthly automatic transfer from your bank to your IRA, scheduled right after payday, and set
it to buy your chosen fund automatically if your brokerage allows it. Turn on dividend reinvestment. Then write your one page
plan, and put a yearly review on your calendar.""",
   "Automation settings screen", "HOUR THREE: AUTOMATE")
sc("""That's it. Three hours, and you've built a system that can run for decades. You'll want to raise contributions over time
and check in once or twice a year. But the hard part, getting started, is done. Most people spend more time choosing a new
phone than building the investing system that could fund their retirement.""",
   "Person relaxing on couch", "THREE HOURS, DECADES OF RESULTS")

# ---------------- By age ----------------
ch("Index funds at every age")
sc("""In your twenties and thirties, time is your biggest asset. Many young investors hold mostly stock index funds, because
they have decades to ride out market drops. This is also when small monthly amounts have the longest time to compound.""",
   "Young professional at desk", "20s AND 30s: MOSTLY STOCKS")
sc("""In your forties and fifties, many investors gradually add bond index funds to reduce the size of potential drops. Income
is often higher, so this is a great time to increase contributions and use catch up contributions once you turn fifty.""",
   "Middle aged couple reviewing plan", "40s AND 50s: ADD BALANCE")
sc("""In your sixties and beyond, many people hold a bigger share of bonds and cash, so they can cover several years of
spending without selling stocks in a downturn. But even in retirement, some stock exposure often helps money keep growing
faster than inflation over a retirement that can last decades.""",
   "Retired couple walking", "60s AND BEYOND: PROTECT AND GROW")

# ---------------- Story ----------------
ch("The million dollar bet")
pr("""Let's end with one of the most famous bets in investing history.""")
short("A hedge fund bet against an index fund for ten years. Here's who won.")
sc("""In 2007, Warren Buffett offered a bet. He wagered that over ten years, a simple low cost S and P five hundred index fund
would beat a group of hedge funds picked by professionals, after fees. A firm called Protege Partners took the bet, choosing
five funds of hedge funds. The money would go to charity.""",
   "Two people shaking hands", "THE BET")
sc("""The bet ran from 2008 through 2017. It started badly for the index fund, because 2008 brought a huge market crash. But
over the full ten years, according to Buffett's shareholder letter, the index fund returned about seven percent a year, while
the hedge fund picks averaged about two percent a year.""",
   "Chart comparing two lines", "7% VS 2% A YEAR")
sc("""Buffett won, and the money went to Girls Incorporated of Omaha. His lesson was clear. High fees and complexity often
work against investors. In fact, Buffett has written that his instructions for money left to his wife call for ninety percent
in a very low cost S and P five hundred index fund, and ten percent in short term government bonds.""",
   "Charity check", "BUFFETT'S OWN ADVICE")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. Is an S and P five hundred fund enough on its own? Many investors use it as their core holding. Others
prefer a total market fund for even broader coverage, plus international stocks for global diversification. Both approaches
are reasonable. The key is low costs and broad diversification.""",
   "Fund comparison chart", "IS ONE FUND ENOUGH?")
sc("""Question two. Are index funds safe? They're diversified, but they still go up and down with the market, sometimes
sharply. They're best for long term money. For money you need within a few years, safer options like high yield savings or
short term bonds usually make more sense.""",
   "Safety helmet and chart", "ARE THEY SAFE?")
sc("""Question three. How much money do I need to start? Often very little. Many brokerages have no account minimums and allow
fractional shares, so you can start with a small amount. Some index mutual funds do have minimums, but ETFs typically
don't.""",
   "Small investment on phone", "HOW MUCH TO START?")
sc("""Question four. Isn't the market too high right now? People have asked that question at almost every point in history.
Nobody can reliably predict short term moves. Regular automatic investing spreads your purchases over time, so you don't
have to guess.""",
   "Person looking at chart worried", "IS THE MARKET TOO HIGH?")
sc("""Question five. What if everyone buys index funds? Some people worry that if everyone indexes, markets stop working. In
reality, plenty of active traders and investors are still setting prices every day. It's a debate among economists, but for
an individual investor, it's not a reason to avoid index funds.""",
   "Crowd of people", "WHAT IF EVERYONE INDEXES?")

sc("""Question six. Should I pick individual stocks too? You can, but it's not necessary. Many successful investors own only
index funds for their entire lives. If you enjoy picking stocks, keep it to a small share of your money, and be honest with
yourself about whether it's beating your index funds over time.""",
   "Stock picking on tablet", "SHOULD I PICK STOCKS TOO?")
sc("""Question seven. What about international index funds? U.S. stocks have performed very well in recent decades, but there
have been long periods when international stocks did better. Many investors hold some international index funds for
diversification. Total world funds include both in one fund.""",
   "Globe with markets", "WHAT ABOUT INTERNATIONAL?")

sc("""Question eight. Do index funds pay dividends? Yes. Stock index funds collect dividends from the companies they own and
pass them on to shareholders, usually every quarter. You can take them as cash or reinvest them automatically. For long term
money, reinvesting is usually the better choice, because those dividends buy more shares that pay even more dividends later.""",
   "Dividend payment notification", "DO THEY PAY DIVIDENDS?")

# ---------------- Mistakes ----------------
ch("Four index fund mistakes")
sc("""Mistake one. Buying an expensive index fund. Not all index funds are cheap. Some charge far more than others for nearly
the same holdings. Always compare expense ratios before buying. A fund tracking
the S and P five hundred at half a percent a year is doing the same job as one charging a few hundredths of a percent, and
you'd be paying many times more for it, every year, for decades.""",
   "Price tags compared", "MISTAKE 1: HIGH FEES")
sc("""Mistake two. Owning too many overlapping funds. Five different large company U.S. funds often hold mostly the same stocks.
That adds complexity without adding real diversification. It
can also make your mix harder to understand and rebalance. Check the top holdings of each fund you own. If they look nearly
identical, you can probably simplify.""",
   "Overlapping circles", "MISTAKE 2: OVERLAP")
sc("""Mistake three. Trading index funds like stocks. Buying and selling based on news defeats the purpose. The power comes from
holding for years. Every trade is a chance to sell low, buy high and pay taxes in a taxable account. The best index investors
often go months without logging in.""",
   "Person frantically trading", "MISTAKE 3: OVERTRADING")
sc("""Mistake four. Stopping contributions during a crash. That's when your monthly money buys the most shares. Many long term
investors see crashes as sales. When the price of something you plan to own for thirty years drops, your monthly
contribution buys more of it. Stopping right then means missing the cheapest shares you may ever get.""",
   "Sale sign in store", "MISTAKE 4: STOPPING IN A CRASH")

# ---------------- Recap ----------------
ch("Recap")
sc("""Quick recap. Angle one, the numbers. What an index fund is, Bogle's folly, costs, why the pros lose, diversification,
taxes, and boring but not risk free.""",
   "Checklist on clipboard", "THE NUMBERS: 1 TO 7")
sc("""Angle two, the psychology. The excitement trap, overconfidence, the behavior gap, headlines, fear of missing out, the
paradox of average and the power of not deciding.""",
   "Person thinking", "THE PSYCHOLOGY: 8 TO 14")
sc("""Angle three, the playbook. Pick the right account, choose simple funds, automate, rebalance once a year, stay the course,
and let time do the work.""",
   "Notebook with plan", "THE PLAYBOOK: 15 TO 20")

# ---------------- Close ----------------
ch("What to do next")
pr("""Boring investing isn't exciting, and that's exactly the point. Own the market, keep costs low, keep buying, and give it
decades. If you want my full step by step plan, it's in my playbook, linked in the description. Tell me in the comments, what
index fund are you starting with? I'm Ryan Rover. See you in the next one.""")

save("video34", "Index Funds Explained: Why Boring Investing Wins", [
    "S&P Dow Jones Indices, SPIVA U.S. Scorecards and Persistence Scorecards",
    "Investment Company Institute, Investment Company Fact Book: expense ratios of index and active equity funds",
    "Morningstar: U.S. passive fund assets overtaking active (early 2024)",
    "Morningstar, Mind the Gap: investor returns vs fund returns",
    "John C. Bogle, The Little Book of Common Sense Investing; Vanguard history (1975, first index fund 1976)",
    "Warren Buffett, Berkshire Hathaway shareholder letters (2013 instructions; 2017 bet results)",
    "Barber and Odean, Trading Is Hazardous to Your Wealth (Journal of Finance, 2000)",
    "Hendrik Bessembinder, Do Stocks Outperform Treasury Bills? (Journal of Financial Economics, 2018)",
    "IRS, IRA and Roth IRA rules and limits",
    "Growth examples: monthly compounding at stated average yearly returns (illustrations, not promises)",
], "index funds explained in 20 lessons, from 3 angles: numbers, psychology, playbook")
