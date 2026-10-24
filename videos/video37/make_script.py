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
pr("""Hi, I'm Ryan Rover. If you ask ten wealthy people how they built their money, you'll hear three answers over and over.
Stocks. Real estate. Or a business. Each one has created millions of millionaires. Each one has also ruined people who
didn't understand it. So which one builds wealth faster? Today we're putting all three side by side, with real numbers, real
psychology and a practical plan for choosing.""")
short("Stocks, real estate or a business. Which one makes you rich faster?")
card("""Here's the short answer. There isn't one winner. Stocks are the easiest and most hands off. Real estate adds leverage
and steady rent, but takes work and cash. A business has the highest potential, and the highest chance of failure. The best
choice depends on your money, your time and your stomach for risk.""",
     {"type": "stat", "label": "Three roads to wealth", "big": "3", "sub": "stocks, real estate, business"})
sc("""Think of them like three vehicles. Stocks are a reliable train. You buy a ticket, sit down and let it carry you, slowly
but steadily, with occasional scary bumps. Real estate is a truck. It can carry a heavy load, especially with borrowed fuel, but
you have to drive and maintain it yourself. A business is a race car. It can go incredibly fast, but it crashes often, and the
driver needs real skill.""",
   "Train, truck and race car", "TRAIN, TRUCK, RACE CAR")
sc("""We'll compare them from three angles. First, the numbers. Long term returns, leverage, failure rates, costs, taxes and
time. Second, the psychology. Why people fall in love with one and fear another, often for the wrong reasons. And third, the
playbook. How to choose and combine them based on your stage of life. Reminder, this is education, not financial advice, and
all examples are illustrations, not promises.""",
   "Three roads splitting", "THREE ANGLES")
pr("""Let's start with the numbers. And first, the one most people can start with today. Stocks.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our numbers. Stock market history comes from sources like S and P Dow Jones Indices. Long run comparisons of housing and
stock returns come from the research paper The Rate of Return on Everything by Oscar Jorda and colleagues. Home price history
comes from Robert Shiller's work and the S and P CoreLogic Case Shiller indices. Business survival data comes from the U.S.
Bureau of Labor Statistics. Growth examples use stated average returns, as illustrations, not promises.""",
   "Research papers on desk", "OUR NUMBERS")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Seven ways to compare stocks, real estate and business.""")

item(1, "Stocks: the long run engine", "ownership with no effort",
"""Lesson number one. Stocks have been a powerful long run engine.""", [
("""When you buy a broad stock index fund, you own a small piece of hundreds or thousands of companies. Those companies employ
people, invent products and earn profits. Over long periods, those profits have pushed stock prices higher. Historically, the S
and P five hundred has averaged roughly ten percent a year before inflation, including dividends, over many decades.""", "Stock market chart long term", "ABOUT 10% A YEAR HISTORICALLY"),
("""Here's what that can look like. Fifty thousand dollars invested for twenty years at a seven percent average yearly return,
a more conservative illustration, grows to roughly two hundred thousand dollars. At ten percent, roughly three hundred sixty
six thousand. And you don't have to fix a roof, manage a tenant or hire an employee.""", "Growing money pile", "$50K TO $200K OR MORE"),
("""The catch is volatility. Stocks can fall thirty, forty or even fifty percent in a bad market, and recoveries can take years.
The long term average hides some very painful short term stretches.""", "Red falling chart", "THE PRICE IS VOLATILITY"),
("""Dividends are part of that return too. Many companies share profits with shareholders as dividends, and reinvesting
them buys more shares. Over long periods, reinvested dividends have made up a meaningful share of the stock market's total
return. So stock investors get two engines working at once, rising company values and a growing stream of dividends.""", "Dividend reinvestment chart", "TWO ENGINES"),
("""Stocks shine on one measure above all, effort. With low cost index funds and automatic investing, they can build wealth
while you focus on your career and your life. No other path on this list asks for less of your time.""", "Relaxed person with coffee", "THE LOWEST EFFORT PATH"),
])

item(2, "Real estate: rent plus growth", "two kinds of return",
"""Lesson number two. Real estate returns come from rent and appreciation.""", [
("""Many people think of real estate returns as just rising home prices. But Robert Shiller's research found that, adjusted for
inflation, U.S. home prices rose only modestly over much of the twentieth century. Price growth alone hasn't usually been the
main story.""", "Old and new house photos", "PRICES ALONE GREW MODESTLY"),
("""The bigger story for investors is rent. A rental property can produce income every month on top of any appreciation. A
major study called The Rate of Return on Everything, covering sixteen countries from 1870 to 2015, found that housing's total
return, rent plus price growth, was roughly comparable to stocks over the long run, with less volatility.""", "Rent check and house", "RENT PLUS GROWTH"),
("""But those research returns are averages, before many real world costs. Property taxes, insurance, repairs, vacancies,
property management and the time you spend all reduce what an individual landlord actually earns.""", "Repair bills on table", "COSTS ARE REAL"),
("""There's also the question of what you'd pay to live there yourself. A home you live in saves you rent, which is a real
economic return even though no check arrives. Economists call this imputed rent. It's one reason owning a home can make financial
sense over long periods, even when the price itself grows slowly.""", "Family in living room", "SAVED RENT IS A RETURN"),
("""Real estate is also local. One neighborhood can boom while another declines. Unlike an index fund, a single property means
your result depends heavily on one location, one building and one set of tenants.""", "Map with neighborhoods", "REAL ESTATE IS LOCAL"),
])

body_hook = "This is the secret weapon of real estate, and it cuts both ways."
item(3, "Leverage", "borrowed money magnifies everything",
"""Lesson number three. Leverage magnifies results, both ways.""", [
("""Real estate's secret weapon is leverage. Most people buy property with a mortgage. Say you buy a three hundred thousand
dollar property with sixty thousand dollars down. If its value rises four percent in a year, that's twelve thousand dollars,
which is a twenty percent gain on your sixty thousand, before costs.""", "Mortgage documents and keys", "4% GROWTH, 20% ON YOUR CASH"),
("""But leverage works in reverse too. If the property falls ten percent, you lose thirty thousand dollars, half of your down
payment, on paper. During the housing crash around 2008, many owners ended up owing more than their homes were worth.""", "Foreclosure sign", "A 10% DROP, HALF YOUR CASH"),
("""You can also use leverage with stocks, through margin loans, but most experts strongly discourage it for regular investors,
because margin calls can force you to sell at the worst time. Mortgages are generally more forgiving, with fixed payments and no
daily price checks.""", "Margin warning on screen", "MORTGAGES ARE MORE FORGIVING"),
("""Leverage also changes how you should measure returns. Real estate investors often talk about cash on cash return, the yearly
cash profit divided by the cash they put in. A property earning three thousand dollars a year after all costs on sixty thousand dollars
down has a five percent cash on cash return, before any appreciation or mortgage paydown.""", "Calculator with rental numbers", "CASH ON CASH RETURN"),
("""The key to safe leverage is cash flow and reserves. If the rent covers the mortgage and costs, and you have cash for
emergencies, you can survive a downturn. If not, leverage can turn a bad year into a disaster.""", "Emergency cash reserve", "CASH FLOW PLUS RESERVES"),
])

body_hook = "About half of new businesses don't survive five years. But the winners win big."
item(4, "Business: highest ceiling, highest risk", "the race car",
"""Lesson number four. A business has the highest ceiling, and the highest risk.""", [
("""Many of the wealthiest people in the world built their fortunes by owning businesses. Federal Reserve survey data has
shown that privately owned businesses make up a large share of wealth for the richest households. No other path can turn a small
amount of money into so much, so fast.""", "Successful founder in office", "THE HIGHEST CEILING"),
("""But the failure rate is high. According to the Bureau of Labor Statistics, roughly one in five new businesses fail in their
first year, and around half don't make it to year five. Many owners lose their savings and years of effort.""", "Closed shop sign", "ABOUT HALF FAIL BY YEAR 5"),
("""A successful business also creates value in two ways. It produces income, and it can be sold. Small businesses often sell
for a few times their yearly profit, so building a profitable business also builds an asset you can eventually cash in.""", "Business sale handshake", "INCOME PLUS A SELLABLE ASSET"),
("""Business returns also depend on what you pay yourself. Many small business owners earn something closer to a salary for
long hours, especially in the early years. The real wealth often comes later, when the business can run without the owner every day,
or when it's sold. A business that depends completely on you is more like a demanding job than an asset.""", "Owner leaving shop with manager in charge", "CAN IT RUN WITHOUT YOU?"),
("""The business path rewards skill, effort and some luck. It's less of an investment and more of a second career. For the right
person, it can be life changing. For the wrong one, it can be devastating.""", "Entrepreneur working late", "MORE CAREER THAN INVESTMENT"),
])

item(5, "Costs and friction", "what it costs to get in and out",
"""Lesson number five. Costs and friction differ enormously.""", [
("""Buying a broad index fund can cost almost nothing. Many brokerages charge no commissions, and the best funds charge only a
few hundredths of a percent a year. You can buy or sell in seconds.""", "Phone with zero commission", "STOCKS: NEARLY FREE"),
("""Real estate is expensive to buy and sell. Closing costs, inspections, loan fees, agent commissions and moving costs can add
up to a significant percentage of the property's price when you include both buying and selling. That's why short holding periods
often lose money.""", "Closing documents with fees", "REAL ESTATE: EXPENSIVE TO TRADE"),
("""Businesses can be the most expensive of all to start. Equipment, inventory, rent, licenses, marketing and months of low or
no income. Many businesses take years to become profitable.""", "Startup expenses list", "BUSINESS: COSTLY TO START"),
("""There are ongoing costs too. Index funds charge a small yearly expense ratio. Properties need regular maintenance, often
estimated by landlords at around one percent of the property's value per year, though it varies widely. Businesses face rising rent,
wages, software and insurance costs. Always count ongoing costs, not just the price of getting in.""", "Monthly bills on table", "ONGOING COSTS COUNT"),
("""The lesson is that friction rewards patience. The more expensive an investment is to buy and sell, the longer you need to
hold it to come out ahead.""", "Hourglass", "FRICTION REWARDS PATIENCE"),
])

item(6, "Taxes", "each path has its own breaks",
"""Lesson number six. Each path has different tax advantages.""", [
("""Stocks can be held in tax advantaged accounts like a four oh one k, IRA or Roth IRA. In regular accounts, gains aren't taxed
until you sell, and long term gains usually get lower rates. That's a powerful, simple tax setup.""", "Retirement account statement", "STOCKS: TAX ADVANTAGED ACCOUNTS"),
("""Real estate investors can deduct expenses and depreciation, which can reduce taxable rental income. Some can defer gains by
exchanging one investment property for another through a 1031 exchange. And homeowners can often exclude a large amount of gain
when selling a primary residence, if they meet the rules.""", "Rental property with tax forms", "REAL ESTATE: DEPRECIATION AND MORE"),
("""Business owners can deduct ordinary and necessary business expenses, may qualify for special deductions, and can open
retirement plans like a solo four oh one k. But business taxes are complex and often require professional help.""", "Accountant with business owner", "BUSINESS: DEDUCTIONS AND PLANS"),
("""The simplest tax advantage of all may be the Roth IRA. Qualified withdrawals, including decades of growth, can be completely
tax free. For most people, maximizing tax advantaged retirement accounts is the first and easiest tax move, no matter which of the three
paths they eventually take.""", "Roth IRA document", "THE SIMPLEST TAX BREAK"),
("""Tax rules change often and have many conditions. Check current IRS guidance or a tax professional before relying on any of
these.""", "IRS website", "CHECK CURRENT RULES"),
])

item(7, "Time and liquidity", "return per hour",
"""Lesson number seven. Count your time, and how fast you can get your money out.""", [
("""Returns don't tell the whole story. If a rental earns two thousand dollars more a year than an index fund, but takes two hundred
hours of your time, you're effectively earning ten dollars an hour for that extra work. It's worth asking what your time is worth.""", "Clock and money", "RETURN PER HOUR"),
("""Liquidity matters too. You can sell index fund shares on almost any business day. Selling a property can take months. Selling a
business can take a year or more, and sometimes it can't be sold at all.""", "For sale sign waiting", "HOW FAST CAN YOU GET OUT?"),
("""Stocks are high liquidity and low time. Real estate is lower liquidity and medium time. A business is usually the lowest
liquidity and highest time. That doesn't make one better. It makes them suited to different people.""", "Comparison chart", "DIFFERENT TRADE OFFS"),
("""Time can also be bought. Landlords can hire property managers, often for a percentage of the rent. Business owners can hire
employees and managers. That frees time, but it also reduces returns. The question is always whether the extra return is worth the
extra time, or whether you'd rather pay to get your time back.""", "Property manager with keys", "YOU CAN BUY TIME BACK"),
("""Try this. Estimate how many hours a month you could realistically give to building wealth outside your job. Your answer is a big
clue about which path fits you.""", "Person with calendar", "HOW MUCH TIME DO YOU HAVE?"),
])

pr("""That's angle one. Stocks as the long run engine, real estate's rent plus growth, leverage, business risk and reward, costs,
taxes, and time and liquidity. Now angle two. The psychology.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
sc("""People rarely choose stocks, real estate or a business based on a spreadsheet. They choose based on feelings, family stories
and what feels safe. Here are seven psychological forces that shape these choices, sometimes in ways that cost money.""",
   "Brain with three icons", "FEELINGS DRIVE CHOICES")

item(8, "The comfort of something you can touch", "tangible feels safer",
"""Lesson number eight. Things you can touch feel safer.""", [
("""Many people trust real estate more than stocks because they can see it, walk through it and touch it. A house feels real. A stock
feels like a number on a screen. That tangibility gives real estate a sense of safety and control.""", "Hand touching brick wall", "YOU CAN TOUCH IT"),
("""But tangible doesn't automatically mean safer. A single property is concentrated in one location, and can face problems like
major repairs, bad tenants or a local downturn. An index fund is spread across hundreds of businesses.""", "Single house versus many companies", "TANGIBLE ISN'T ALWAYS SAFER"),
("""Stocks are also real. Each share represents ownership in actual companies, with buildings, products, workers and profits. It
just doesn't feel that way because you don't see them.""", "Factory and office buildings", "STOCKS ARE REAL TOO"),
("""Real estate's sense of control is real in some ways. You can renovate, raise rents or improve management to increase value.
With a stock index fund, you can't change anything about the companies. Some people love that control. Others find it exhausting.
Knowing which kind of person you are helps you choose.""", "Person renovating kitchen", "CONTROL CAN BE A BURDEN"),
("""Try this. Look up the top ten holdings of an index fund. Seeing the real companies you own can make stocks feel as concrete as a
building.""", "Fund holdings list", "SEE WHAT YOU OWN"),
])

body_hook = "Your house drops in value all the time. You just don't see it."
item(9, "Invisible volatility", "what you don't see can't scare you",
"""Lesson number nine. Real estate's volatility is hidden.""", [
("""Stock prices update every second, so you see every drop. Home values aren't priced every day. You might only learn your home's
value when you sell or get an appraisal. So real estate feels calmer, even when values are falling.""", "Stock ticker versus quiet house", "HIDDEN VOLATILITY"),
("""During the housing crash around 2008, national home prices fell sharply, and in some areas far more. Many owners didn't feel it
day to day, but it was real, and those who had to sell felt it painfully.""", "Housing crash headline", "HOUSES FALL TOO"),
("""Interestingly, that hidden volatility can help real estate investors. Because they don't see daily prices, they're less tempted
to panic sell. Stock investors could learn from this by checking their accounts less often.""", "Person not checking phone", "SEEING LESS HELPS"),
("""Private businesses have hidden volatility too. Because there's no daily price, owners often feel their business is worth a
steady amount. But the value of a small business can swing a lot with the economy, competition and the owner's health. The lack of
a price tag doesn't mean a lack of risk.""", "Small business with no price tag", "NO PRICE TAG, STILL RISK"),
("""Try this. If daily stock prices make you anxious, check your investments only once a quarter. Treat them more like a house you
own for decades.""", "Quarterly calendar", "CHECK LESS OFTEN"),
])

item(10, "Survivorship bias", "you only hear the winners",
"""Lesson number ten. Survivorship bias.""", [
("""We hear about the founders who became billionaires and the landlords who built empires. We rarely hear about the businesses
that closed or the investors who lost properties to foreclosure. That makes risky paths look safer than they are.""", "Magazine cover of successful founder", "YOU HEAR ABOUT WINNERS"),
("""Survivorship bias makes business ownership look like a sure path to riches. But for every famous founder, there are many who
tried and failed, often losing savings along the way.""", "Many closed shops", "MANY TRIED AND FAILED"),
("""It also affects real estate. Social media is full of investors showing their portfolios, but rarely their vacancies, repair
bills or sleepless nights.""", "Real estate influencer video", "THE HIDDEN STRUGGLES"),
("""Stocks have survivorship bias too. Market indexes regularly remove failing companies and add growing ones. That's why owning the
whole index works better than owning a few companies that look great today. The index automatically keeps up with the survivors, so you
don't have to guess which ones they'll be.""", "Index changes list", "THE INDEX UPDATES ITSELF"),
("""Try this. When you hear a success story, ask how many people tried the same thing and didn't succeed. The answer changes how
you see the odds.""", "Person thinking", "ASK ABOUT THE FAILURES"),
])

pr("""Quick pause. If this comparison is helping you think more clearly about your path, please subscribe to Ryan Rover Money.
It's free, and it helps us keep making these. Now, lesson eleven.""")

item(11, "What you enjoy matters", "fit beats returns",
"""Lesson number eleven. Choose what you can stick with.""", [
("""The best investment is often the one you'll stick with for decades. If you hate dealing with repairs and tenants, real estate
might make you miserable, even if it earns more on paper. If you hate risk, a business could keep you up at night.""", "Person stressed with repairs", "FIT MATTERS"),
("""Some people love the hands on work of real estate. Finding deals, renovating, managing properties. For them, it's not a chore.
It's a satisfying project that also builds wealth.""", "Person renovating happily", "SOME LOVE THE WORK"),
("""Others love building something from nothing, solving problems and leading people. For them, business ownership can be deeply
rewarding, beyond the money.""", "Entrepreneur leading team", "SOME LOVE BUILDING"),
("""Your skills matter as much as your preferences. Someone who's handy with repairs has a real advantage in real estate. Someone
with sales skills or deep industry knowledge has an edge in business. Someone with a busy career and no extra skills may get the best
results from simple index funds. Use your strengths.""", "Toolbelt and laptop", "USE YOUR STRENGTHS"),
("""Try this. Ask yourself which of these you'd do even if the returns were the same. That's often the path you'll stick with
longest.""", "Person reflecting", "WHAT WOULD YOU ENJOY?"),
])

item(12, "Risk and sleep", "the sleep test",
"""Lesson number twelve. Pass the sleep test.""", [
("""A useful rule is the sleep test. If an investment keeps you awake at night, you probably have too much of it, or it's the wrong
one for you. Stress leads to bad decisions, like panic selling or giving up too early.""", "Person awake in bed", "THE SLEEP TEST"),
("""For some people, a stock market drop is terrifying, while a rental property feels calm. For others, the thought of a tenant
calling about a broken heater at midnight is far worse. Risk isn't just math. It's personal.""", "Phone ringing at night", "RISK IS PERSONAL"),
("""Business risk can be the most stressful of all, because your income, savings and identity can all be tied to one venture.""", "Business owner worried", "BUSINESS RISK IS PERSONAL"),
("""Your risk tolerance also changes over time. Young people with stable jobs can often handle more ups and downs, because they have
decades to recover. People close to retirement usually need more stability. A path that fits you at thirty may not fit you at sixty.""", "Person at different ages", "RISK TOLERANCE CHANGES"),
("""Try this. Imagine your investment drops by a third next year. Would you hold, sell or panic? Your honest answer tells you how much
risk to take.""", "Person imagining scenario", "IMAGINE THE DROP"),
])

item(13, "Concentration versus diversification", "all eggs, one basket",
"""Lesson number thirteen. Concentration builds fortunes, diversification protects them.""", [
("""Many great fortunes come from concentration, putting most of your money and effort into one business or one strategy. But
concentration is also how many people lose everything.""", "Eggs in one basket", "CONCENTRATION CUTS BOTH WAYS"),
("""Stocks through index funds are the most diversified option. A single rental property is concentrated. A business is often the
most concentrated of all, with your job and savings in one place.""", "Diversification spectrum", "FROM DIVERSIFIED TO CONCENTRATED"),
("""A common approach is to concentrate effort, but diversify savings. Work hard on your career or business, and invest your savings
in diversified funds so one setback can't wipe you out.""", "Person balancing work and savings", "CONCENTRATE EFFORT, DIVERSIFY SAVINGS"),
("""Diversification across all three paths is possible too. Someone could own index funds, a rental property and a small side
business. If one struggles, the others can carry the load. Many wealthy families deliberately spread their wealth this way over time.""", "Three baskets of eggs", "DIVERSIFY ACROSS PATHS"),
("""Try this. Look at your total net worth. If more than half depends on one asset, consider whether you'd be okay if that asset failed.""", "Net worth pie chart", "CHECK YOUR CONCENTRATION"),
])

item(14, "Family stories", "what you grew up hearing",
"""Lesson number fourteen. Family stories shape your choices.""", [
("""If your parents lost money in the stock market, you may distrust stocks. If they built wealth with rental properties, real
estate may feel natural. If they ran a business, you may see it as normal, or as too stressful.""", "Family photo album", "FAMILY STORIES"),
("""These stories carry real lessons, but they're based on specific times and places. A crash your parents lived through doesn't
predict your future, and their success doesn't guarantee yours.""", "Old newspaper headlines", "ONE TIME, ONE PLACE"),
("""Morgan Housel, in The Psychology of Money, argues that people's investing decisions are shaped heavily by their personal
experiences, especially early in life. Recognizing that helps you make choices based on evidence, not just memory.""", "Book on desk", "EXPERIENCE SHAPES BELIEFS"),
("""Culture plays a role too. In some families and communities, owning land or a home is a top priority. In others, owning a business is
a source of pride. These values are meaningful. Just make sure the financial side makes sense, so tradition and math work together.""", "Family dinner conversation", "VALUES AND MATH TOGETHER"),
("""Try this. Write down what you believe about stocks, real estate and business, and where each belief came from. Some may be
worth keeping. Some may be worth questioning.""", "Person writing beliefs", "QUESTION YOUR BELIEFS"),
])

pr("""That's angle two. Tangible comfort, hidden volatility, survivorship bias, enjoyment, the sleep test, concentration and family
stories. Now angle three. The playbook.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
sc("""Here's the good news. You don't have to pick just one. Many wealthy people use all three at different stages. Here are six moves
to choose and combine them wisely.""",
   "Three puzzle pieces fitting", "YOU CAN COMBINE THEM")

item(15, "Build the stock base first", "the foundation",
"""Move number fifteen. Start with a stock foundation.""", [
("""For most people, stocks through retirement accounts and index funds are the easiest place to start. You can begin with small
amounts, get tax advantages and an employer match, and build wealth without extra work.""", "Foundation of a building", "THE FOUNDATION"),
("""This base also protects you if you later try riskier paths. If a rental property or business struggles, you still have a growing,
diversified portfolio behind you.""", "Safety net", "A SAFETY NET"),
("""Many financial planners suggest getting your emergency fund and retirement savings on track before taking on large real estate
or business risks.""", "Checklist of basics", "BASICS FIRST"),
("""Stocks also give you a benchmark. Once you're invested in a low cost index fund, every other opportunity has to beat it, after
costs, taxes and your time. If a rental or business can't clearly beat simply adding more to your index fund, it may not be worth the
extra risk and work.""", "Benchmark chart", "THE BENCHMARK TO BEAT"),
("""Try this. Make sure you're getting your full employer match and investing regularly in low cost index funds before putting big
money into anything else.""", "Retirement plan screen", "MATCH AND INDEX FIRST"),
])

item(16, "Your home is a home first", "not your best investment",
"""Move number sixteen. Treat your home as a home first.""", [
("""Many people consider their house their biggest investment. A home can build wealth through mortgage paydown and appreciation,
and it provides stability. But it also costs money every year, in taxes, insurance, maintenance and interest.""", "Family in front of home", "A HOME COSTS MONEY"),
("""Buying too much house is one of the most common ways people stall their wealth building. A huge mortgage can leave little money
for investing.""", "Large house with big mortgage", "DON'T BUY TOO MUCH HOUSE"),
("""Buy a home because you want stability and it fits your budget, not just because you expect it to be your best investment.""", "Comfortable modest home", "BUY FOR LIFE, NOT JUST RETURNS"),
("""Renting isn't throwing money away, either. Renting can make sense if you might move soon, if buying costs much more than renting
in your area, or if renting lets you invest the difference. The best choice depends on prices, your plans and your discipline to invest
what you save.""", "Apartment building", "RENTING CAN MAKE SENSE"),
("""Try this. Before buying a home, calculate the full monthly cost, including taxes, insurance and maintenance, and make sure you can
still invest for retirement.""", "Home budget calculator", "COUNT THE FULL COST"),
])

item(17, "Try real estate the easy way", "REITs and house hacking",
"""Move number seventeen. Try real estate without going all in.""", [
("""Real estate investment trusts, or REITs, let you invest in portfolios of properties through the stock market. Many REIT index funds
are low cost and diversified, giving you real estate exposure without being a landlord.""", "REIT fund on screen", "REITS"),
("""Another option is house hacking. Buying a small multi unit property, living in one unit and renting the others. The rent can help
cover your mortgage, and you learn the landlord business on a small scale.""", "Duplex house", "HOUSE HACKING"),
("""If you buy a rental, run the numbers carefully. Include vacancies, repairs, insurance, taxes and management. Many new landlords
overestimate rent and underestimate costs.""", "Rental spreadsheet", "RUN THE REAL NUMBERS"),
("""Learn the landlord rules before you start. Many states and cities have specific rules about leases, deposits, repairs and
evictions. Understanding them protects both you and your tenants, and helps you avoid costly mistakes.""", "Lease agreement", "LEARN THE RULES"),
("""Try this. Before buying any rental, track the local rents and expenses for three months. Patience in buying is one of real estate's
most important skills.""", "Notebook with rental data", "STUDY BEFORE BUYING"),
])

item(18, "Start a business small", "keep your job at first",
"""Move number eighteen. Start a business small.""", [
("""Many successful businesses start as side projects. Keeping your job while you test an idea reduces risk dramatically. You find out
whether customers will pay before risking your savings.""", "Person working on side project at night", "START ON THE SIDE"),
("""Service businesses, like consulting, cleaning, landscaping or design, often need little upfront money. You can start with skills
you already have.""", "Service business tools", "START WITH YOUR SKILLS"),
("""Set a limit on what you're willing to lose, in money and time. If the idea doesn't work within that limit, stop and try something
else.""", "Stop sign", "SET A LOSS LIMIT"),
("""Buying an existing small business is another route. Instead of starting from zero, you buy a company that already has customers
and profits, often with a loan. It has its own risks, but it skips the most dangerous early stage. Some buyers use loan programs backed by
the Small Business Administration.""", "Business for sale sign", "BUY INSTEAD OF START"),
("""Try this. Find one paying customer for your idea before spending any significant money. A real customer is the best proof.""", "First sale receipt", "FIND ONE CUSTOMER"),
])

body_hook = "The richest people often use all three. Here's the order."
item(19, "Combine them", "the wealth flywheel",
"""Move number nineteen. Combine them into a flywheel.""", [
("""Many wealthy people follow a pattern. They earn income through a career or business, invest the profits in stocks and real
estate, and let those assets grow. Each path feeds the others.""", "Flywheel diagram", "THE WEALTH FLYWHEEL"),
("""A business owner might use profits to buy the building their business operates in, becoming their own landlord, while investing
the rest in index funds for diversification.""", "Business owner buying building", "BE YOUR OWN LANDLORD"),
("""A worker might max out retirement accounts, then buy a small rental, then later start a side business. Each step builds on the
last.""", "Steps upward", "ONE STEP AT A TIME"),
("""The flywheel works in small steps too. A side hustle earning five hundred dollars a month, invested in index funds, can build a
meaningful portfolio over time. Later, that portfolio could fund a down payment, or seed a bigger business. Small wins compound, just
like money does.""", "Small gears turning big gears", "SMALL WINS COMPOUND"),
("""Try this. Sketch your own flywheel. Where does your money come from today, and where could it go next?""", "Person sketching plan", "SKETCH YOUR FLYWHEEL"),
])

item(20, "Choose by your stage", "time, money and skill",
"""Move number twenty. Choose based on your stage of life.""", [
("""Early on, you may have more time than money. Building skills, a career or a small business can grow your income, which is the fuel
for everything else. Investing small amounts in index funds keeps compounding running.""", "Young professional learning", "EARLY: MORE TIME THAN MONEY"),
("""In the middle years, you may have more money and less time. Index funds, retirement accounts and perhaps a few well chosen
properties can work, without demanding too much attention.""", "Busy parent at work", "MIDDLE: MORE MONEY, LESS TIME"),
("""Later in life, simplicity and income often matter more. Many people shift toward diversified investments and steady income,
selling or simplifying properties and businesses.""", "Retired couple relaxing", "LATER: SIMPLICITY AND INCOME"),
("""Whatever your stage, your income is your biggest wealth building tool. Growing it through skills, promotions or a business
creates more money to invest in every path. Many people focus too much on returns and too little on increasing what they have to invest
in the first place.""", "Career ladder", "INCOME IS THE FUEL"),
("""Try this. Write down your current stage, how much time and money you have, and your risk tolerance. Then choose the path that fits
now, knowing you can change later.""", "Planning worksheet", "CHOOSE FOR NOW"),
])

# ---------------- Story ----------------
ch("Three friends")
short("Three friends picked three different paths. Here's what happened.")
sc("""Imagine three friends, each with fifty thousand dollars at age thirty. The first puts it in a low cost index fund and keeps
investing monthly. Over twenty years at a seven percent average yearly return, that first fifty thousand alone could grow to roughly two
hundred thousand dollars, with almost no extra effort.""",
   "Friend with laptop", "FRIEND 1: STOCKS")
sc("""The second uses it as a down payment on a small rental. Some years bring vacancies and big repairs. Others bring rising rents.
After twenty years, the mortgage is much smaller, rent has grown, and the property may be worth much more. Their result depends heavily
on the location, the financing and how well they managed it.""",
   "Friend with rental house", "FRIEND 2: REAL ESTATE")
sc("""The third starts a business. The first attempt fails and costs half the money. The second attempt slowly grows into a profitable
company. By fifty, they might be the wealthiest of the three, or they might have nothing. That's the honest range of outcomes for
business owners.""",
   "Friend in small business", "FRIEND 3: BUSINESS")
sc("""The lesson isn't that one friend was right. It's that each path has a different shape. Stocks are steady and simple. Real estate
is slower and hands on, with leverage. Business has the widest range of outcomes. Knowing that shape helps you choose with open eyes.""",
   "Three friends together", "DIFFERENT SHAPES")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. Which has the best returns historically? Over long periods, research suggests stocks and housing, including rent,
have had broadly similar total returns, with business ownership having the widest range, from total loss to enormous gains. The best
choice depends on you.""",
   "Comparison chart", "WHICH RETURNS MORE?")
sc("""Question two. Can I invest in real estate without buying property? Yes. REITs and real estate index funds let you invest in
property portfolios through a brokerage account, often with low costs and easy liquidity.""",
   "REIT on phone", "REAL ESTATE WITHOUT PROPERTY")
sc("""Question three. Should I quit my job to start a business? Usually not right away. Many successful founders start on the side,
test their idea and build savings before making the leap.""",
   "Person at office desk", "QUIT YOUR JOB?")
sc("""Question four. What if I don't have much money? Start with what's available. A retirement account with an employer match, small
monthly index fund investments and building skills that raise your income. Bigger paths can come later.""",
   "Small savings jar", "WHAT IF I HAVE LITTLE MONEY?")

sc("""Question five. Is gold or crypto a better path than these three? Gold and crypto don't produce profits, rent or dividends.
Their returns depend on what someone else will pay later, so they behave more like speculation than ownership. Some investors hold a
small amount for diversification, but stocks, real estate and businesses are the classic engines of long term wealth because they
produce income.""",
   "Gold coins and crypto symbols", "WHAT ABOUT GOLD OR CRYPTO?")
sc("""Question six. How do I know when I'm ready for real estate or a business? A common checklist is a full emergency fund, no high
interest debt, retirement savings on track and extra cash you could lose without derailing your life. If you can tick those boxes,
you're in a much better position to take a bigger swing.""",
   "Checklist ticked", "WHEN AM I READY?")

# ---------------- Mistakes ----------------
ch("Mistakes on each path")
sc("""The classic stock mistake is panic. Selling during a crash, chasing hot stocks or trading too often. The fix is simple but
hard. Own broad, low cost funds, invest automatically and leave them alone through the scary years.""",
   "Panicked investor", "STOCK MISTAKE: PANIC")
sc("""The classic real estate mistake is overpaying and underestimating costs. Buying with optimistic rent numbers, no repair budget
and no cash reserves. One bad tenant or one big repair can then turn a good deal into a money pit. Conservative numbers and a healthy
cash cushion are the fix.""",
   "Broken water heater", "REAL ESTATE MISTAKE: THIN MARGINS")
sc("""The classic business mistake is betting everything too soon. Quitting a job, draining savings and borrowing heavily before
proving customers will pay. Testing small, keeping costs low and growing from real sales gives a business a far better chance to
survive its first years.""",
   "Empty store with bills", "BUSINESS MISTAKE: TOO BIG TOO SOON")
sc("""And the mistake common to all three is never starting. Spending years researching the perfect path while doing nothing. Even
a small start on any path teaches you more than any amount of reading, and starting with a simple index fund costs almost nothing.""",
   "Person hesitating at start line", "ALL PATHS: NEVER STARTING")

# ---------------- Recap ----------------
ch("Recap")
sc("""Quick recap. Angle one, the numbers. Stocks as the long run engine, real estate's rent plus growth, leverage, business risk,
costs, taxes, and time and liquidity.""",
   "Checklist on clipboard", "THE NUMBERS: 1 TO 7")
sc("""Angle two, the psychology. Tangible comfort, hidden volatility, survivorship bias, enjoyment, the sleep test, concentration and
family stories.""",
   "Person thinking", "THE PSYCHOLOGY: 8 TO 14")
sc("""Angle three, the playbook. Build a stock base, treat your home as a home, try real estate the easy way, start a business small,
combine them and choose by your stage.""",
   "Notebook with plan", "THE PLAYBOOK: 15 TO 20")

# ---------------- Close ----------------
ch("What to do next")
pr("""Stocks, real estate and business can all build wealth. The question isn't which one is best. It's which one is best for you,
right now. If you want my full step by step plan, it's in my playbook, linked in the description. Tell me in the comments, which path
are you on? I'm Ryan Rover. See you in the next one.""")

save("video37", "Stocks vs Real Estate vs Business: Which Builds Wealth Faster", [
    "Jorda, Knoll, Kuvshinov, Schularick and Taylor, The Rate of Return on Everything, 1870-2015 (Quarterly Journal of Economics, 2019)",
    "Robert Shiller, Irrational Exuberance: long-run U.S. home prices adjusted for inflation",
    "S&P CoreLogic Case-Shiller U.S. National Home Price Index",
    "S&P Dow Jones Indices: S&P 500 long-run total returns",
    "U.S. Bureau of Labor Statistics, Business Employment Dynamics: establishment survival rates",
    "Federal Reserve, Survey of Consumer Finances: business equity among wealthiest households",
    "IRS: depreciation, 1031 exchanges, home sale exclusion, retirement plans for the self-employed",
    "Morgan Housel, The Psychology of Money (2020)",
    "Growth examples: monthly compounding at stated average yearly returns (illustrations, not promises)",
], "stocks vs real estate vs business in 20 lessons, from 3 angles: numbers, psychology, playbook")
