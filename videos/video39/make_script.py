import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

body_hook = None  # set right before item() to start a Short at its first explained scene

def item(n, title, sub, card_text, scenes):
    """scenes: list of (text, query, caption) shown after the list card."""
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"ASSET {n}")
    global body_hook
    if body_hook:
        short(body_hook); body_hook = None
    for text, q, c in scenes:
        sc(text, q, c)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Imagine checking your bank account at the start of every month and seeing money arrive that you didn't
work for that month. Not a paycheck. Not a side gig. Just income from things you own. That's what wealthy people mean when they
talk about making their money work for them. Today I'll walk you through fifteen assets that can pay you every month, what they
really pay, the traps to avoid and how to build your own monthly income machine.""")
short("How much money do you need to earn a thousand dollars a month without working?")
card("""Here's the core math. At a four percent yearly yield, one hundred thousand dollars produces about three hundred thirty three
dollars a month. To earn one thousand dollars a month, you'd need roughly three hundred thousand dollars. At a six percent yield,
about two hundred thousand. Higher yields need less money, but usually come with more risk.""",
     {"type": "compare", "left": {"label": "$1,000 a month at 4%", "big": "$300K", "sub": "needed"},
      "right": {"label": "$1,000 a month at 6%", "big": "$200K", "sub": "needed, more risk"},
      "note": "yields change over time; illustrations, not promises"})
sc("""That math is the key to everything in this video. Monthly income from assets is simply the amount you own multiplied by the yield,
divided by twelve. So there are only two ways to get more monthly income. Own more, or earn a higher yield. And because higher yields
almost always come with higher risk, the most reliable path is usually owning more, steadily, over time.""",
   "Simple formula on chalkboard", "OWN MORE OR EARN MORE")
sc("""We'll go through these fifteen assets from three angles. First, the numbers. Five safer, cash like assets and what they actually
pay. Second, the psychology. Five higher yield assets, and the mental traps that make people overpay for income. And third, the
playbook. Five ownership assets and a step by step plan to build monthly income. Reminder, this is education, not financial advice.
Rates and yields change constantly, so always check current numbers.""",
   "Three paths in a park", "THREE ANGLES")
pr("""Let's start with the numbers. And the first asset is one almost everyone can open today.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our numbers. Deposit insurance rules come from the FDIC and NCUA. Treasury information comes from TreasuryDirect and the U.S.
Treasury. Fund information comes from the SEC and fund disclosures. Social Security rules come from the Social Security
Administration. Yields mentioned are illustrations, because real rates change with the economy. This is education, not financial
advice.""",
   "Financial documents on desk", "OUR NUMBERS")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Five safer assets that pay monthly, and what you can realistically expect from them.""")

item(1, "High yield savings account", "the easiest monthly payer",
"""Asset number one. A high yield savings account.""", [
("""The simplest monthly paying asset is a high yield savings account. Most banks and credit unions pay interest monthly, and many
online banks pay far more than traditional savings accounts. In recent years, many high yield accounts have paid several percent,
while some big bank savings accounts paid close to zero.""", "Online bank app with interest", "INTEREST EVERY MONTH"),
("""Money in a bank is typically protected by FDIC insurance, and at credit unions by NCUA insurance, up to two hundred fifty thousand
dollars per depositor, per institution, per ownership category. That makes it one of the safest places for money you might need.""", "FDIC sign at bank", "INSURED UP TO $250,000"),
("""The downside is that rates can change at any time, and they usually fall when the Federal Reserve cuts interest rates. Over long
periods, savings rates have often barely kept up with inflation, or fallen behind.""", "Interest rate chart falling", "RATES CAN DROP ANYTIME"),
("""So a high yield savings account is perfect for your emergency fund and short term goals, but usually not the best place for money
you won't need for decades. It's a parking spot, not a growth engine.""", "Parking lot", "A PARKING SPOT"),
("""Here's what that means in dollars. On a twenty thousand dollar emergency fund, the difference between a rate near zero and a rate
of four percent is roughly eight hundred dollars a year, or about sixty seven dollars a month. That's real money for doing nothing more than
moving your savings to a better account at an insured bank. It's one of the easiest monthly raises you'll ever give yourself.""", "Two savings accounts compared", "ABOUT $67 A MONTH ON $20K"),
("""Try this. Compare your current savings rate with a few reputable online banks. If yours pays far less, moving your emergency fund
could earn you real money every month with almost no extra risk.""", "Comparing bank rates", "COMPARE YOUR RATE"),
])

item(2, "Money market funds", "cash that pays dividends",
"""Asset number two. Money market funds.""", [
("""Money market funds are mutual funds that invest in very short term, high quality debt, like Treasury bills and commercial paper.
They usually aim to keep a stable value of one dollar per share and pay dividends that are typically credited monthly.""", "Money market fund statement", "STABLE $1 SHARE, MONTHLY DIVIDENDS"),
("""Their yields usually move closely with short term interest rates. When rates were high in recent years, many money market funds
paid yields similar to or above high yield savings accounts.""", "Rates comparison chart", "YIELDS FOLLOW SHORT RATES"),
("""One important difference is that money market funds are not FDIC insured. They're considered very low risk, but not risk free. A
few have fallen below one dollar per share in rare crises, such as 2008.""", "Not FDIC insured label", "NOT FDIC INSURED"),
("""Government money market funds, which invest mostly in U.S. Treasury securities, are generally considered among the safest. Some
also generate income that's exempt from state income taxes, depending on holdings and your state.""", "Treasury building", "GOVERNMENT FUNDS ARE SAFEST"),
("""Money market funds are also extremely convenient. They usually sit right inside your brokerage account, so you can move money between
them and your investments in a day or two. Many investors use them as a holding place for cash they plan to invest soon, or for the cash part
of a retirement portfolio. The monthly dividends simply accumulate, or can be paid out to your bank.""", "Brokerage account transfers", "CONVENIENT AND FLEXIBLE"),
("""Try this. Check what your brokerage does with uninvested cash. Some pay very little on cash by default, while their money market
funds pay much more. Moving idle cash can be an easy upgrade.""", "Brokerage cash settings", "CHECK YOUR IDLE CASH"),
])

body_hook = "The U.S. government will pay you interest. Here's how to get it every month."
item(3, "Treasury bill ladder", "government backed, monthly by design",
"""Asset number three. A Treasury bill ladder.""", [
("""Treasury bills are short term loans to the U.S. government, maturing in anywhere from a few weeks to one year. They're backed by
the full faith and credit of the United States, which is why they're often considered one of the safest investments in the world.""", "U.S. Treasury building", "BACKED BY THE U.S. GOVERNMENT"),
("""T bills don't pay monthly interest. You buy them at a discount and receive the full value at maturity. But you can create monthly
income by building a ladder, buying bills that mature in different months so money comes back to you regularly.""", "Ladder illustration", "BUILD A LADDER"),
("""Interest on Treasury bills is subject to federal income tax, but exempt from state and local income taxes. For people in high tax
states, that can make them more attractive than similar bank yields.""", "Tax form with state exemption", "NO STATE INCOME TAX"),
("""You can buy T bills directly through TreasuryDirect or through most brokerage accounts, often with no fees. Many brokerages also
offer automatic rollover, so maturing bills are reinvested.""", "TreasuryDirect website", "BUY DIRECT OR AT A BROKER"),
("""Here's how a simple monthly ladder can work. Say you have twelve thousand dollars. You buy one thousand dollars of T bills maturing
each month for the next year. Every month, one thousand dollars plus interest comes back. You can spend it, or buy a new twelve month bill to keep
the ladder going. It's a simple way to turn the safest investment in the world into a monthly cash flow.""", "Twelve month ladder diagram", "A SIMPLE 12 MONTH LADDER"),
("""Try this. If you have cash you won't need for a few months, compare the current yield on a three month T bill with your savings
account.""", "Yield comparison", "COMPARE THE YIELD"),
])

item(4, "CDs with monthly interest", "locked rate, steady payments",
"""Asset number four. Certificates of deposit with monthly interest.""", [
("""A certificate of deposit, or CD, is a bank deposit where you agree to leave your money for a set period, like six months, a year or
five years, in exchange for a fixed interest rate. Many banks let you choose to receive interest monthly.""", "CD certificate", "A FIXED RATE FOR A FIXED TIME"),
("""The advantage is certainty. If rates fall, your CD keeps paying the rate you locked in. And CDs at insured banks are covered by
FDIC insurance within the limits.""", "Locked padlock", "LOCK IN THE RATE"),
("""The downside is that withdrawing early usually triggers a penalty, often several months of interest. And if rates rise, you're
stuck with your lower rate until the CD matures.""", "Early withdrawal penalty notice", "EARLY WITHDRAWAL PENALTIES"),
("""A CD ladder, with CDs maturing at different times, gives you regular access to some of your money while capturing higher rates on
longer terms.""", "CD ladder diagram", "A CD LADDER"),
("""Some banks also offer no penalty CDs, which let you withdraw early without a penalty, usually at a slightly lower rate. And brokered
CDs, bought through a brokerage account, can be sold before maturity on a secondary market, though their price can rise or fall. Each type trades
a bit of yield for a bit of flexibility, so choose based on how sure you are about when you'll need the money.""", "Different CD options", "NO PENALTY AND BROKERED CDS"),
("""Try this. If you're saving for a specific goal one to three years away, like a car or a down payment, compare CD rates with your
savings account.""", "Goal planning", "MATCH CDS TO GOALS"),
])

item(5, "Bond funds", "monthly distributions from many bonds",
"""Asset number five. Bond funds.""", [
("""Bond funds hold many bonds at once, from governments, companies or municipalities. Many bond funds and ETFs pay distributions monthly,
from the interest their bonds earn.""", "Bond fund statement", "MANY BONDS, MONTHLY INCOME"),
("""Unlike CDs, bond fund prices move. When interest rates rise, existing bonds lose value, and bond fund prices fall. In 2022, as rates
rose quickly, many bond funds had one of their worst years on record.""", "Falling bond price chart", "PRICES MOVE WITH RATES"),
("""Duration measures how sensitive a bond fund is to interest rate changes. Short term bond funds usually move less. Long term bond funds
can move a lot.""", "Duration chart", "KNOW THE DURATION"),
("""Municipal bond funds can pay income that's free from federal income tax, and sometimes state tax too. They can be useful for people in
higher tax brackets investing in taxable accounts.""", "Municipal building", "MUNICIPAL BONDS"),
("""Bond funds earn their place in a portfolio by doing something stocks don't. In many stock market crashes, high quality government bonds
have held their value or even risen, cushioning the fall. Not always, as 2022 showed, but often. That's why many retirees hold bond funds not just
for their monthly income, but as a stabilizer that makes the whole portfolio easier to live with.""", "Cushion under falling chart", "A STABILIZER"),
("""Try this. If you own a bond fund, look up its duration and its credit quality. Those two numbers tell you most of what you need to
know about its risk.""", "Fund fact sheet", "CHECK DURATION AND QUALITY"),
])

pr("""That's angle one. High yield savings, money market funds, Treasury bills, CDs and bond funds. Safer assets with modest monthly
income. Now angle two. Higher yields, and the psychology that gets people in trouble.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
sc("""As yields go up, so does risk, and so do the mental traps. Monthly income feels wonderful, and that feeling can push people into
investments they don't fully understand. Here are five higher yield assets, each with a psychological lesson.""",
   "Brain illustration with money", "HIGHER YIELD, MORE TRAPS")

item(6, "Monthly dividend stocks and ETFs", "income from ownership",
"""Asset number six. Monthly dividend stocks and ETFs.""", [
("""Most U.S. companies that pay dividends pay them quarterly, but some pay monthly. One well known example is Realty Income, a real
estate company that calls itself The Monthly Dividend Company. There are also ETFs that collect dividends from many companies and pay
monthly.""", "Dividend check in mailbox", "SOME PAY MONTHLY"),
("""Here's the psychological trap. People love monthly payments, so they sometimes choose investments just because they pay monthly,
even if they're more expensive or riskier than quarterly payers. The payment schedule doesn't change the total return.""", "Calendar with paydays", "MONTHLY ISN'T BETTER BY ITSELF"),
("""Remember also that dividends aren't free money. When a company pays a dividend, its share price typically drops by roughly the
dividend amount on the ex dividend date. What matters is total return, dividends plus price changes.""", "Stock price dropping on ex dividend date", "DIVIDENDS AREN'T FREE MONEY"),
("""Dividends can also be cut. During tough times, many companies have reduced or suspended dividends. A dividend is a decision by the
company's board, not a promise.""", "Dividend cut headline", "DIVIDENDS CAN BE CUT"),
("""There's also a concentration trap. Some people build a portfolio of only a handful of high yield dividend stocks, often clustered in
the same few industries, like utilities, energy or real estate. If that sector struggles, much of their income can shrink at once. A diversified
dividend fund spreads that risk across many companies and industries, so no single cut hurts too much.""", "Few eggs in one basket", "DON'T CONCENTRATE FOR YIELD"),
("""Try this. Before buying any dividend investment, look at its total return over ten years, not just its yield. A high yield with poor
total return is a warning sign.""", "Total return chart", "CHECK TOTAL RETURN"),
])

item(7, "REITs", "real estate income without the landlord",
"""Asset number seven. Real estate investment trusts.""", [
("""REITs are companies that own or finance income producing real estate, like apartments, warehouses, offices or shopping centers. By
law, to keep their special tax status, REITs generally must distribute at least ninety percent of their taxable income to shareholders.""", "Apartment and warehouse buildings", "90% PAYOUT REQUIREMENT"),
("""That's why REITs often have higher yields than average stocks. Some pay monthly, and REIT index funds give you diversified exposure to
many properties at once.""", "REIT fund chart", "HIGHER YIELDS"),
("""The psychological trap with REITs is assuming real estate is always safe. REIT prices can fall sharply, especially when interest rates
rise or a property type struggles. Office REITs, for example, faced serious challenges as remote work spread.""", "Empty office building", "REAL ESTATE ISN'T ALWAYS SAFE"),
("""REIT dividends are often taxed as ordinary income rather than at lower qualified dividend rates, so many investors hold REITs in tax
advantaged accounts like IRAs.""", "IRA account", "TAX CONSIDERATIONS"),
("""REITs also have a useful feature for monthly income seekers. They trade like stocks, so you can buy as little as one share, or even a
fraction, and sell any business day. Compare that with a rental property, which might take months and thousands of dollars in fees to sell. For
many people, that liquidity makes REITs a far easier way to add real estate income to a portfolio.""", "Trading app with REIT", "LIQUID REAL ESTATE"),
("""Try this. If you want real estate income without being a landlord, compare a low cost REIT index fund with individual REITs. The index
fund spreads your risk across many property types.""", "Fund comparison", "CONSIDER A REIT INDEX FUND"),
])

item(8, "Rental property", "rent checks every month",
"""Asset number eight. Rental property.""", [
("""Rental property is the classic monthly income asset. Tenants pay rent every month, and after expenses and mortgage payments, the
leftover cash flow is yours. Over time, rents may rise and the mortgage shrinks.""", "Rent check and house keys", "RENT EVERY MONTH"),
("""The psychological trap is focusing on gross rent instead of net cash flow. Property taxes, insurance, repairs, vacancies, maintenance
and management fees can consume a large share of rent. Many new landlords discover their real profit is much smaller than they expected.""", "List of rental expenses", "GROSS RENT ISN'T PROFIT"),
("""Rental income is also not passive for most people. Finding tenants, handling repairs and dealing with problems takes time. Hiring a
property manager helps, but it reduces your income.""", "Landlord fixing sink", "NOT REALLY PASSIVE"),
("""On the positive side, rental property offers leverage, potential appreciation and tax benefits like depreciation. For the right person,
it can be a powerful monthly income source.""", "Rental property sold sign", "POWERFUL FOR THE RIGHT PERSON"),
("""Here's a rough illustration. A property renting for two thousand dollars a month might have a mortgage of one thousand two hundred,
property taxes and insurance of three hundred, and a repair and vacancy reserve of three hundred. That leaves about two hundred dollars a month of
cash flow. Not huge, but it can grow as rents rise and the mortgage is eventually paid off. The real wealth often comes over decades.""", "Rental cash flow breakdown", "$2,000 RENT, ABOUT $200 CASH FLOW"),
("""Try this. Before buying a rental, estimate your net cash flow using conservative numbers, including at least one month of vacancy per
year and a repair budget.""", "Rental spreadsheet", "USE CONSERVATIVE NUMBERS"),
])

pr("""Quick pause. If you're starting to picture your own monthly income machine, please subscribe to Ryan Rover Money. It's free, and it
helps us keep making these. Now, asset number nine.""")

body_hook = "That fund paying ten percent a year has a hidden cost most people miss."
item(9, "Covered call ETFs", "high yield with a catch",
"""Asset number nine. Covered call ETFs.""", [
("""Covered call ETFs own stocks and sell call options on them, collecting option premiums. Those premiums can create very high yields,
often paid monthly, which makes these funds popular with income investors.""", "Options chart", "HIGH YIELDS, OFTEN MONTHLY"),
("""Here's the catch. By selling call options, these funds give up much of the upside when stocks rise sharply. In strong markets, they can
lag far behind a regular index fund, while still taking most of the losses when markets fall.""", "Capped upside graph", "CAPPED UPSIDE, FULL DOWNSIDE"),
("""The psychological trap is yield fixation. A big yield feels like a big return. But some covered call funds have delivered lower total
returns than simple index funds over time, even with their high monthly payments.""", "Big yield number with warning", "YIELD ISN'T RETURN"),
("""Part of a high distribution can also come from returning your own capital, rather than true income. That can slowly shrink your
investment.""", "Shrinking pile of money", "RETURN OF CAPITAL"),
("""Covered call funds can still have a place. Some retirees value a smoother, higher monthly payout more than maximum growth, and accept
lagging in strong bull markets in exchange. That's a reasonable choice, as long as it's a choice made with open eyes. The problem is only when
people buy them believing a high yield means a high return with no trade off.""", "Retiree reading fund report", "A CHOICE, WITH OPEN EYES"),
("""Try this. Before buying a covered call fund, compare its total return with a plain index fund over five or ten years. Then decide whether
the steady income is worth the trade off.""", "Comparison chart", "COMPARE TOTAL RETURNS"),
])

item(10, "Income annuities", "a paycheck for life",
"""Asset number ten. Income annuities.""", [
("""A simple income annuity, sometimes called a single premium immediate annuity, works like buying a pension. You give an insurance company
a lump sum, and it pays you a fixed amount every month for life, or for a set period.""", "Insurance company building", "BUY YOURSELF A PENSION"),
("""The big benefit is protection against outliving your money. No matter how long you live, the checks keep coming, backed by the insurer.
Economists have long noted that annuities can be valuable, yet relatively few retirees buy them, sometimes called the annuity puzzle.""", "Retiree receiving check", "PROTECTION AGAINST LONG LIFE"),
("""The psychological barrier is the fear of dying early and losing the money. That fear is real, but some annuities offer guaranteed periods
or refunds to heirs, at the cost of lower payments.""", "Thinking retiree", "THE FEAR OF LOSING OUT"),
("""Be careful. Many complex annuities have high fees, surrender charges and confusing terms. Simple income annuities are usually easier to
understand. Payments generally aren't inflation adjusted unless you pay for that feature, and they depend on the insurer's strength.""", "Complex contract", "BEWARE COMPLEX ANNUITIES"),
("""Here's how annuity payments generally work. The older you are when you buy, the higher the monthly payment, because the insurer expects
to pay for fewer years. Payments also depend on interest rates at the time you buy. That's why some retirees buy annuities in stages over several
years, rather than all at once, to spread out their timing.""", "Age and payment chart", "OLDER BUYERS GET MORE"),
("""Try this. If you're near retirement, ask a fee only fiduciary planner whether covering basic expenses with Social Security plus a simple
annuity makes sense for you.""", "Advisor meeting", "ASK A FIDUCIARY"),
])

pr("""That's angle two. Monthly dividend stocks, REITs, rental property, covered call ETFs and income annuities. Higher yields with real trade
offs. Now angle three. The playbook.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
sc("""The final five assets are about ownership and long term strategy, plus a plan to combine everything into reliable monthly income.
Some of these take years to build, but they can become the strongest income sources of all. And unlike the
safer assets in angle one, several of them can grow their payments over time, which is exactly what you need to keep up with inflation over a
long retirement.""",
   "Toolbox on table", "OWNERSHIP AND STRATEGY")

item(11, "A staggered dividend portfolio", "turning quarterly into monthly",
"""Asset number eleven. A staggered dividend portfolio.""", [
("""Most dividend stocks and index funds pay quarterly. But because different companies pay in different months, a diversified portfolio can
produce income almost every month.""", "Calendar with dividend dates", "QUARTERLY BECOMES MONTHLY"),
("""A broad dividend index fund, or simply a total market index fund, gives you dividends from hundreds of companies. Many investors also hold
cash reserves to smooth out the months with smaller payments.""", "Index fund statement", "BROAD FUNDS WORK"),
("""Some retirees simply set up a fixed monthly withdrawal from their portfolio, combining dividends and small sales. That creates a steady
paycheck, regardless of when dividends arrive.""", "Automatic monthly transfer", "CREATE YOUR OWN PAYCHECK"),
("""Focusing on dividend growth rather than high yield can help income rise over time. Companies with long records of raising dividends often
have strong businesses, though past increases don't guarantee future ones.""", "Rising dividend chart", "DIVIDEND GROWTH"),
("""Here's an example of the math. A diversified stock index fund yielding around one and a half percent pays far less monthly income than a
high yield fund. But over long periods, its growth has often been much stronger. Many retirees combine a modest dividend with small regular sales,
creating a sustainable paycheck while keeping the growth engine running.""", "Dividend plus growth chart", "DIVIDENDS PLUS GROWTH"),
("""Try this. Look at your brokerage's dividend calendar to see when your investments pay. You may already have more monthly income than you
realize.""", "Brokerage dividend calendar", "CHECK YOUR CALENDAR"),
])

item(12, "A small business", "owner income every month",
"""Asset number twelve. A small business.""", [
("""A profitable small business can pay its owner every month. Some business owners eventually hire managers, so the business runs without them
being there every day, turning it into a true income asset.""", "Small business storefront", "OWNER INCOME"),
("""Businesses with recurring revenue, like subscriptions, service contracts or maintenance plans, are especially valuable, because they produce
predictable monthly income.""", "Recurring revenue chart", "RECURRING REVENUE"),
("""But businesses take work, money and risk to build, and many fail. Most owners spend years working hard before income becomes even partly
passive.""", "Entrepreneur working late", "IT TAKES WORK"),
("""Some people buy existing businesses with steady cash flow instead of starting from scratch. That still requires careful research, and often
financing.""", "Business purchase agreement", "BUY OR BUILD"),
("""The real value of a business often shows up when it's sold. Small businesses frequently sell for a few times their yearly profit. So a
business that pays its owner fifty thousand dollars a year could also be worth one hundred to two hundred thousand dollars to a buyer. That's a
double benefit, monthly income now and a valuable asset later.""", "Business valuation chart", "INCOME NOW, VALUE LATER"),
("""Try this. Think about skills you already have that people pay for monthly, like lawn care, bookkeeping or tutoring. Recurring services can
grow into a real business.""", "Person offering service", "START WITH RECURRING SERVICES"),
])

item(13, "Royalties and digital products", "create once, earn repeatedly",
"""Asset number thirteen. Royalties and digital products.""", [
("""Books, music, online courses, templates, stock photos and apps can earn money long after they're created. Many platforms pay creators
monthly.""", "Creator at laptop", "CREATE ONCE, EARN REPEATEDLY"),
("""The appeal is scalability. Selling one more digital copy costs almost nothing. A successful product can earn for years.""", "Downloads counter", "SCALABLE INCOME"),
("""The reality is that most creative products earn very little. It often takes many products, consistent marketing and years of effort before
income becomes meaningful.""", "Small earnings dashboard", "MOST EARN LITTLE"),
("""Treat it like planting seeds. Each product is a small seed. Most stay small, but a few can grow into steady monthly income.""", "Seeds sprouting", "PLANT MANY SEEDS"),
("""Traditional royalties exist too. Authors earn royalties from book sales, musicians from streams and licensing, and some investors even
buy existing royalty streams on specialized marketplaces. These can produce monthly payments, but they often decline over time as a song or book
gets older, so they're best treated as a bonus, not a foundation.""", "Music and books with royalties", "ROYALTIES OFTEN FADE"),
("""Try this. If you have knowledge people want, create one small digital product, like a guide or template, and see whether anyone buys it.""", "Simple digital product", "CREATE ONE SMALL PRODUCT"),
])

body_hook = "The most underrated monthly income asset might be the roof over your head."
item(14, "A paid off home", "income you don't have to pay",
"""Asset number fourteen. A paid off home.""", [
("""A paid off home doesn't send you a check, but it does something similar. It removes one of the biggest monthly expenses most people have.
Every month without a mortgage payment is money that stays in your pocket.""", "Paid off mortgage document", "NO MORTGAGE PAYMENT"),
("""Economists call the value of living in a home you own imputed rent. You're effectively paying rent to yourself. For retirees, a paid off
home can dramatically lower how much income they need.""", "Family home", "IMPUTED RENT"),
("""You still pay property taxes, insurance and maintenance, so it's not free. But those costs are usually much lower than a full mortgage or
rent payment.""", "Property tax bill", "STILL SOME COSTS"),
("""Whether to pay off a mortgage early depends on your interest rate and other goals. A low rate mortgage might be fine to keep while you invest,
while a high rate mortgage might be worth paying down faster.""", "Mortgage rate comparison", "IT DEPENDS ON YOUR RATE"),
("""A paid off home also gives you options. Some retirees downsize and invest the difference. Others use a reverse mortgage, a loan that lets
homeowners sixty two and older convert part of their home equity into income, though these come with costs and rules that deserve careful
review. And for many, simply having no housing payment is the greatest financial peace of mind there is.""", "Retired couple on porch", "A PAID OFF HOME CREATES OPTIONS"),
("""Try this. Calculate how much lower your monthly expenses would be without a mortgage. That number shows how much income a paid off home is
worth to you.""", "Budget without mortgage", "CALCULATE ITS VALUE"),
])

item(15, "Delayed Social Security", "the inflation adjusted annuity",
"""Asset number fifteen. Delayed Social Security.""", [
("""Social Security pays monthly for life and adjusts for inflation, features that would be expensive to buy privately. For many people, it's
their most valuable monthly income asset.""", "Social Security card", "MONTHLY, FOR LIFE, INFLATION ADJUSTED"),
("""You can claim as early as sixty two, but benefits are permanently reduced. For each year you delay past full retirement age, up to age seventy,
benefits increase by about eight percent, according to the Social Security Administration.""", "Age timeline 62 to 70", "ABOUT 8% MORE PER YEAR OF DELAY"),
("""Delaying isn't right for everyone. Health, other savings and marriage all matter. But for many people, especially those who expect to live long,
delaying can significantly increase lifetime income.""", "Couple planning", "NOT RIGHT FOR EVERYONE"),
("""Some retirees use savings to cover the years between retirement and claiming Social Security, effectively buying a larger lifetime income.""", "Bridge over river", "BRIDGE TO A BIGGER CHECK"),
("""Here's an example. Someone with a full retirement age benefit of two thousand dollars a month might receive roughly one thousand four
hundred dollars if they claim at sixty two, and roughly two thousand four hundred eighty at seventy, if their full retirement age is sixty seven.
That's a difference of more than one thousand dollars a month, for life, adjusted for inflation.""", "Three benefit amounts", "$1,400 VS $2,480 A MONTH"),
("""Try this. Check your Social Security statement to see your estimated monthly benefit at sixty two, full retirement age and seventy.""", "SSA statement", "CHECK YOUR OPTIONS"),
])

# ---------------- Income ladder ----------------
ch("Building your monthly income machine")
pr("""Now let's put it all together. Here's how many people build monthly income in layers, from safest to riskiest.""")
sc("""Layer one is your emergency fund, in a high yield savings account or money market fund. It pays a little monthly interest, but its real job is
protecting everything else. Without it, an unexpected bill can force you to sell investments at a bad time.""",
   "Foundation layer", "LAYER 1: EMERGENCY FUND")
sc("""Layer two is guaranteed income, like Social Security, a pension or a simple annuity. This covers your most basic expenses, so a market crash
never threatens your ability to pay for food and housing.""",
   "Second layer", "LAYER 2: GUARANTEED INCOME")
sc("""Layer three is your diversified investment portfolio, stock and bond index funds, producing dividends, interest and growth. This covers lifestyle
expenses and protects against inflation over decades.""",
   "Third layer", "LAYER 3: DIVERSIFIED PORTFOLIO")
sc("""Layer four is optional ownership income, like rental property, a business or royalties. These can add a lot, but they come with more work and
risk.""",
   "Top layer", "LAYER 4: OWNERSHIP INCOME")

sc("""Here's a simple example of the layers working together. A retired couple spends five thousand dollars a month. Social Security covers
three thousand two hundred. Their diversified portfolio of about five hundred forty thousand dollars, withdrawn at four percent, covers about one
thousand eight hundred more. Their emergency fund sits in a money market fund. Every layer has a job, and no single asset has to carry the whole
load.""",
   "Couple reviewing income layers", "EVERY LAYER HAS A JOB")

# ---------------- By age ----------------
ch("Monthly income at every age")
sc("""In your twenties and thirties, monthly income from assets is mostly about planting. Your emergency fund earns a little interest, and
your retirement accounts reinvest every dividend automatically. You probably don't need the income yet, so letting it compound is usually the
smartest move. Every dividend reinvested now becomes a bigger dividend later.""",
   "Young adult planting tree", "20s AND 30s: PLANT AND REINVEST")
sc("""In your forties and fifties, many people start shaping their future income. Paying down the mortgage, checking Social Security estimates,
maybe adding a rental property or building a business. This is when you decide which layers you'll rely on, and start building them on
purpose.""",
   "Middle aged couple planning", "40s AND 50s: SHAPE THE LAYERS")
sc("""In your sixties and beyond, the focus shifts from growing assets to drawing income from them. Deciding when to claim Social Security,
whether an annuity makes sense, how much to keep in cash and bonds, and setting up a steady monthly paycheck from your portfolio.""",
   "Retired couple with tea", "60s AND BEYOND: DRAW THE INCOME")

# ---------------- Story ----------------
ch("Two income investors")
short("Two investors wanted monthly income. One chased yield. One built a system.")
sc("""Imagine two investors, each with three hundred thousand dollars, each wanting monthly income. The first chases the highest yields they can
find, putting everything into a few funds paying ten or twelve percent. For a while, the monthly checks feel amazing.""",
   "Excited investor with high yield", "INVESTOR ONE CHASES YIELD")
sc("""But over time, some of those funds cut their payouts, and their share prices slowly fall. The income shrinks, and so does the principal. The high
yield turned out to be partly their own money coming back to them.""",
   "Shrinking balance", "THE YIELD TRAP")
sc("""The second investor builds layers. An emergency fund, a diversified portfolio yielding a more modest amount, and a plan to withdraw a sustainable
percentage. Their income starts smaller but grows over time, and their principal stays intact.""",
   "Calm investor with balanced plan", "INVESTOR TWO BUILDS LAYERS")
sc("""Ten years later, the difference is striking. The first investor's monthly checks are smaller than when they started, and their account
is worth less than the original three hundred thousand. The second investor's income has grown with their dividends and withdrawals, and their
portfolio is likely worth more than they put in. Same starting money. One chased a number. The other built a system that could last.""",
   "Two account balances after ten years", "TEN YEARS LATER")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. What's the safest monthly income asset? Insured bank accounts and CDs within FDIC or NCUA limits, and U.S. Treasury bills, are
generally considered the safest. They also tend to pay the least over long periods.""",
   "Safe vault", "THE SAFEST OPTIONS")
sc("""Question two. Is a high yield always a red flag? Not always, but it's a reason to look closer. Ask where the yield comes from, whether it's
sustainable and what the total return has been.""",
   "Magnifying glass on yield", "IS HIGH YIELD A RED FLAG?")
sc("""Question three. How much do I need for passive income to replace my salary? Divide your yearly spending by a sustainable withdrawal or yield rate.
At four percent, sixty thousand dollars a year needs about one point five million dollars, before considering Social Security or other income.""",
   "Calculator", "REPLACING A SALARY")

sc("""Question four. Should I reinvest my monthly income or spend it? If you don't need it yet, reinvesting usually builds more future income,
because each payment buys more income producing assets. If you're retired and rely on it, spending it is exactly the point. Many people reinvest
during their working years and switch to taking the income in retirement.""",
   "Reinvest or spend choice", "REINVEST OR SPEND?")
sc("""Question five. How are these income sources taxed? It varies a lot. Interest is usually taxed as ordinary income, qualified dividends often
get lower rates, Treasury interest skips state tax, municipal bond interest may skip federal tax, and Roth withdrawals can be tax free. Where you
hold each asset can matter as much as which asset you hold.""",
   "Tax forms and income types", "HOW IS IT TAXED?")

sc("""Question six. Can I build monthly income with a small amount of money? Yes, just slowly. Even a few thousand dollars in a high yield savings
account or a dividend fund starts producing a little income. The amounts feel tiny at first, but every dollar you add, and every payment you
reinvest, makes the next month's income a bit bigger. That's how every large income portfolio started.""",
   "Small coins growing into stack", "STARTING SMALL")

# ---------------- Mistakes ----------------
ch("Monthly income mistakes")
sc("""Mistake one. Chasing the highest yield. Unusually high yields often signal higher risk, unsustainable payouts or a return of your own
capital. Always ask where the yield comes from and how the total return has looked over many years.""",
   "Bait on a hook", "MISTAKE 1: CHASING YIELD")
sc("""Mistake two. Putting everything in one income source. One property, one stock or one fund can disappoint. Spreading income across several
layers, like Social Security, a diversified portfolio and cash, makes your monthly income much more reliable.""",
   "Eggs in one basket", "MISTAKE 2: ONE SOURCE")
sc("""Mistake three. Forgetting inflation. A fixed monthly payment that feels comfortable today can buy much less in twenty years. Include assets
that can grow, like stocks, and income that adjusts for inflation, like Social Security.""",
   "Shrinking dollar", "MISTAKE 3: FORGETTING INFLATION")
sc("""Mistake four. Ignoring fees and fine print. Some income products charge high yearly fees or surrender charges that quietly eat into your
monthly payments. Read the costs before you buy, and favor simple, low cost options.""",
   "Fine print with magnifying glass", "MISTAKE 4: FEES AND FINE PRINT")

# ---------------- Recap ----------------
ch("Recap")
sc("""Quick recap. Angle one, the numbers. High yield savings, money market funds, Treasury bills, CDs and bond funds. These are the safer
assets that pay modest monthly income and protect your short term money.""",
   "Checklist on clipboard", "THE NUMBERS: 1 TO 5")
sc("""Angle two, the psychology. Monthly dividend stocks, REITs, rental property, covered call ETFs and income annuities. Higher yields,
with real trade offs, and mental traps like yield fixation and the fear of spending.""",
   "Person thinking", "THE PSYCHOLOGY: 6 TO 10")
sc("""Angle three, the playbook. A staggered dividend portfolio, a small business, royalties, a paid off home and delayed Social Security.
Ownership assets that can grow, combined into layers that make your monthly income reliable for decades.""",
   "Notebook with plan", "THE PLAYBOOK: 11 TO 15")

# ---------------- Close ----------------
ch("What to do next")
pr("""Monthly income from assets isn't magic. It's ownership multiplied by time. Start with the safe layers, avoid the yield traps and keep adding to
what you own. If you want my full step by step plan, it's in my playbook, linked in the description. Tell me in the comments, which of these fifteen
assets do you already own? I'm Ryan Rover. See you in the next one.""")

save("video39", "15 Assets That Pay You Every Month", [
    "FDIC and NCUA: deposit insurance coverage limits",
    "TreasuryDirect and U.S. Treasury: Treasury bills, state tax exemption",
    "SEC investor bulletins: money market funds, bond funds, covered call and income products, annuities",
    "IRS: REIT distribution requirements, taxation of REIT dividends",
    "Realty Income: 'The Monthly Dividend Company' (company materials)",
    "Social Security Administration: delayed retirement credits (about 8% per year to age 70)",
    "Yaari (1965) and the 'annuity puzzle' literature",
    "Yields and rates mentioned are illustrations; current rates vary",
], "15 assets that pay monthly, from 3 angles: numbers, psychology, playbook")
