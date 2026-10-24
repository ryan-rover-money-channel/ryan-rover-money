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
pr("""Hi, I'm Ryan Rover. We've all been told that the way to get rich is to save money. Skip the coffee, clip the coupons, put
something away every month. And saving matters, a lot. But here's the uncomfortable truth. Saving alone, money sitting in a bank
account, will almost never make you rich. In fact, over decades, it can quietly make you poorer. Today I'll show you why, and what
actually turns savings into wealth.""")
short("Saving money alone will never make you rich. Here's the math.")
card("""Here's the math in one picture. Five hundred dollars a month, kept in cash earning nothing for forty years, adds up to two
hundred forty thousand dollars. The same five hundred dollars a month, invested at a seven percent average yearly return, could grow
to roughly one point three million dollars. Same habit. Same effort. More than five times the result.""",
     {"type": "compare", "left": {"label": "$500 a month in cash", "big": "$240K", "sub": "after 40 years"},
      "right": {"label": "$500 a month invested", "big": "$1.3M", "sub": "at 7% average yearly return"},
      "note": "illustration, not a promise; returns vary"})
sc("""And that comparison is generous to cash, because it ignores inflation. Over forty years, rising prices would shrink what that two
hundred forty thousand dollars can actually buy, probably to well under half. Saving builds the pile. But without growth, the pile is
slowly melting while you build it. That's the core idea of this video. Saving is the start of wealth, not the whole recipe.""",
   "Melting ice sculpture of dollar sign", "SAVING IS THE START")
sc("""We'll explore this from three angles. First, the numbers. Inflation, interest, taxes and the ceiling on how much anyone can save.
Second, the psychology. Why saving feels so safe, and why that feeling can hold people back. And third, the playbook. The three things
that actually build wealth when you combine them with saving, investing, earning more and owning. Reminder, this is education, not
financial advice, and all growth examples are illustrations, not promises.""",
   "Three paths in a park", "THREE ANGLES")
pr("""Let's start with the numbers. And the first lesson is about the silent thief in every savings account.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our numbers. Inflation data comes from the Bureau of Labor Statistics. Long run returns on stocks, bonds and cash come from
research like Jeremy Siegel's Stocks for the Long Run and data from S and P Dow Jones Indices. Account rules come from the IRS. Growth
examples use monthly compounding at stated average returns, as illustrations, not predictions.""",
   "Research books on desk", "OUR NUMBERS")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Seven reasons the math of saving alone doesn't add up to wealth.""")

item(1, "Inflation eats cash", "the silent thief",
"""Lesson number one. Inflation slowly eats cash.""", [
("""Inflation means prices rise over time, so each dollar buys a little less every year. In the United States, inflation has averaged
roughly three percent a year over the long run, according to Bureau of Labor Statistics data, though some periods have been much
higher. In 2022, it rose above eight percent.""", "Grocery prices rising over years", "ABOUT 3% A YEAR ON AVERAGE"),
("""Here's what that does to savings. Ten thousand dollars in an account earning half a percent, with inflation at three percent, would
buy only about what four thousand eight hundred dollars buys today after thirty years. The balance grew a little on paper, but its
real value was cut by more than half.""", "Shrinking shopping cart", "$10,000 BUYS LIKE $4,800"),
("""That's why economists talk about real returns, your return after inflation. If your savings earn less than inflation, your real
return is negative. You're losing buying power every year, even though your balance never goes down.""", "Real return formula", "NEGATIVE REAL RETURNS"),
("""High yield savings accounts help, and sometimes they've paid more than inflation. But over long periods, cash has generally only
roughly kept pace with inflation at best. It preserves money. It rarely grows it in a meaningful way.""", "Savings account vs inflation chart", "CASH PRESERVES, RARELY GROWS"),
("""Think about what things cost when your parents were young. A movie ticket, a gallon of milk, a new car, a house. Prices that once
seemed normal now look tiny. That's inflation working slowly over decades. Your savings face the same force, which is why money that must
last thirty or forty years needs to grow, not just sit.""", "Old price tags versus new", "REMEMBER OLD PRICES"),
("""Try this. Look at the interest rate on your savings account and compare it with the latest inflation rate. If inflation is higher,
your savings are shrinking in real terms right now.""", "Comparing two numbers", "COMPARE YOUR RATE TO INFLATION"),
])

body_hook = "Five hundred dollars a month can become two hundred forty thousand, or one point three million."
item(2, "The growth gap", "cash vs invested",
"""Lesson number two. The growth gap between cash and investing.""", [
("""Let's go deeper into the opening example. Five hundred dollars a month for forty years, earning nothing, is two hundred forty thousand
dollars. Earning half a percent in a typical savings account, it's roughly two hundred sixty six thousand. Invested at seven percent,
roughly one point three million.""", "Three growth curves", "$240K, $266K OR $1.3M"),
("""Why such a huge gap? Because compounding needs a meaningful rate to work. At half a percent, your money barely snowballs. At seven
percent, growth starts producing its own growth, and over decades, that growth becomes most of the total.""", "Snowball rolling", "COMPOUNDING NEEDS A REAL RATE"),
("""Historically, long term research like Jeremy Siegel's has found that U.S. stocks returned roughly six to seven percent a year after
inflation over very long periods, while short term government bills returned well under one percent after inflation. The difference
compounds into a massive gap.""", "Long term returns chart", "STOCKS VS CASH, AFTER INFLATION"),
("""Of course, stocks come with risk. They can fall sharply and stay down for years. That's why cash still has a role for short term
needs. But for money you won't touch for decades, cash's safety comes at an enormous long term cost.""", "Risk and reward scale", "SAFETY HAS A COST"),
("""Here's another way to see the gap. In the cash example, every dollar of the final balance is a dollar you put in yourself. In the
invested example, more than four out of every five dollars at the end came from growth, not from your contributions. Investing doesn't ask
you to work harder. It asks your money to work too.""", "Pie chart of contributions vs growth", "MOST OF IT IS GROWTH"),
("""Try this. Calculate how much you've saved in cash beyond your emergency fund. Then use a compound interest calculator to see what that
money might become if invested for twenty years.""", "Online calculator", "SEE YOUR GAP"),
])

item(3, "The savings ceiling", "you can only cut so much",
"""Lesson number three. There's a ceiling on how much you can save.""", [
("""Saving comes from the gap between what you earn and what you spend. You can cut spending, but only so far. Rent, food, transportation
and insurance have a floor. For someone earning fifty thousand dollars a year, even an aggressive twenty percent savings rate is ten
thousand dollars a year.""", "Budget with essential costs", "SPENDING HAS A FLOOR"),
("""Income, on the other hand, has no fixed ceiling. A raise, a promotion, a new job, a side business or a skill that's in demand can
increase what you earn far more than cutting can reduce what you spend.""", "Rising income chart", "INCOME HAS NO CEILING"),
("""Personal finance writer Ramit Sethi often makes this point. There's a limit to how much you can cut, but no limit to how much you can
earn. Cutting spending is important, but it eventually runs out of room.""", "Scissors and ladder", "CUTTING RUNS OUT OF ROOM"),
("""This doesn't mean frugality is useless. It means frugality works best combined with growing income and investing the difference.""", "Three tools together", "FRUGALITY PLUS GROWTH"),
("""Here's a simple comparison. Cutting a fifteen dollar streaming service saves one hundred eighty dollars a year. Negotiating a three
percent raise on a fifty thousand dollar salary adds one thousand five hundred dollars a year, and that raise often carries into every future
raise too. Both are worth doing, but they aren't the same size.""", "Small savings vs raise", "$180 VS $1,500 A YEAR"),
("""Try this. Write down your biggest three expenses and your current income. Ask which has more room to change in the next two years.""", "Person writing list", "WHERE IS THE ROOM?"),
])

item(4, "Interest gets taxed", "the hidden drag on savings",
"""Lesson number four. Interest is taxed as ordinary income.""", [
("""Interest from a savings account, CD or money market fund is generally taxed as ordinary income at your regular rate. If you're in the
twenty two percent federal bracket and earn four percent interest, you keep roughly three point one percent before state taxes.""", "Tax form with interest", "INTEREST IS TAXED LIKE WAGES"),
("""Now subtract inflation. If inflation is three percent, your after tax, after inflation return is close to zero. Your savings are
treading water at best.""", "Treading water illustration", "AFTER TAXES AND INFLATION"),
("""Investments held in tax advantaged accounts like four oh one ks, IRAs and Roth IRAs avoid yearly taxes on growth. And long term
capital gains and qualified dividends in regular accounts often get lower tax rates than interest.""", "Retirement account statement", "INVESTMENTS CAN BE TAX ADVANTAGED"),
("""So the same dollar, saved in cash or invested in a tax advantaged account, can have very different results after decades of taxes.""", "Two jars compared", "SAME DOLLAR, DIFFERENT RESULTS"),
("""This doesn't mean you should avoid interest entirely. Your emergency fund still belongs in safe, interest earning accounts. It just
means that for long term money, the tax drag on interest is one more reason cash struggles to build wealth, and one more reason to use tax
advantaged accounts for growth.""", "Emergency fund and retirement account", "THE RIGHT MONEY IN THE RIGHT PLACE"),
("""Try this. Look at last year's tax forms for interest income. That's money you paid tax on that might have grown tax deferred in a
retirement account.""", "1099 INT form", "CHECK YOUR INTEREST INCOME"),
])

item(5, "Cash has a job", "but only one job",
"""Lesson number five. Cash has an important job, just not the job of making you rich.""", [
("""Let's be fair to saving. Cash is essential. An emergency fund of three to six months of essential expenses protects you from job loss,
medical bills and car repairs. It stops a bad month from becoming a debt spiral.""", "Emergency fund jar", "CASH PROTECTS YOU"),
("""Cash is also right for short term goals, like a car purchase, a down payment in the next year or two, or a planned trip. Money you'll
need soon shouldn't be exposed to stock market swings.""", "Down payment savings", "SHORT TERM GOALS"),
("""The problem isn't having cash. It's having too much cash for too long. Money beyond your emergency fund and near term goals often sits
idle for years, losing buying power.""", "Pile of idle cash", "TOO MUCH, TOO LONG"),
("""A useful mental model is to give every dollar a job. Safety dollars stay in cash. Goal dollars wait in savings or CDs. Growth dollars get
invested for the long term.""", "Labeled jars", "GIVE EVERY DOLLAR A JOB"),
("""Some people find it helps to see cash as insurance, not as an investment. You don't buy car insurance expecting it to make you
rich. You buy it so a bad day doesn't ruin you. An emergency fund works the same way. Its return is peace of mind, and that's worth
paying for, up to a point.""", "Insurance policy and jar", "CASH IS INSURANCE"),
("""Try this. Split your savings into three labels, safety, goals and growth. Any growth money still sitting in cash is probably ready to be
invested.""", "Three labels", "SAFETY, GOALS, GROWTH"),
])

item(6, "Time is the multiplier", "starting late costs more than saving less",
"""Lesson number six. Time multiplies investing, not saving.""", [
("""In a savings account, time barely helps, because the rate is low. In an investment account, time is the biggest multiplier there is.
Every extra year gives compounding more room to work.""", "Hourglass with growing money", "TIME MULTIPLIES INVESTING"),
("""Three hundred dollars a month for thirty five years, kept in cash, totals one hundred twenty six thousand dollars. Invested at a seven
percent average yearly return, it could grow to roughly five hundred forty thousand.""", "Two totals compared", "$126K VS $540K"),
("""That means the longer you leave long term money in cash, the more you lose. A decade of saving without investing can cost far more than
the decade itself, because those dollars miss their most powerful compounding years.""", "Lost years on calendar", "LOST YEARS COST THE MOST"),
("""The good news is that it's never too late to start investing. But the sooner long term money starts working, the less you need to save
to reach the same goal.""", "Person starting to invest", "START SOONER, SAVE LESS"),
("""Here's a striking way to think about it. For a twenty five year old, each dollar invested at seven percent could become roughly fifteen
dollars by age sixty five. For a forty five year old, the same dollar might become about four. Your earliest dollars are your most powerful
ones, which is exactly why leaving them in cash is so costly.""", "Dollar growing over time", "EARLY DOLLARS ARE POWERFUL"),
("""Try this. If you're saving for retirement in cash, move it into a retirement account invested in a low cost, diversified fund.""", "Retirement account setup", "PUT TIME TO WORK"),
])

item(7, "Earning more beats cutting more", "the power of a raise",
"""Lesson number seven. A raise invested beats a lifetime of coupons.""", [
("""Imagine you get a ten thousand dollar raise and invest all of it, about eight hundred thirty three dollars a month, for thirty years at a
seven percent average yearly return. That could grow to roughly one million dollars.""", "Raise letter and growing chart", "A $10K RAISE COULD BECOME $1M"),
("""To match that by cutting, you'd need to cut eight hundred thirty three dollars a month from your spending, every month, for thirty years.
For most people, that's far harder than earning more.""", "Long list of cuts", "MATCHING IT BY CUTTING IS HARD"),
("""Research on job changes, such as wage data from the Federal Reserve Bank of Atlanta, has shown that people who switch jobs have often seen
faster wage growth than those who stay, at least during many periods.""", "Wage growth tracker chart", "JOB SWITCHERS OFTEN EARN MORE"),
("""Skills, certifications, negotiation and career moves can raise income for decades. Every raise you invest builds wealth far faster than
saving alone.""", "Person learning new skill", "INVEST IN YOUR EARNING POWER"),
("""Earning more also makes saving easier emotionally. When your income rises and you invest part of each raise, you can save more without
cutting anything you enjoy. That's far more sustainable than squeezing an already tight budget year after year.""", "Comfortable family budget", "EARNING MORE MAKES SAVING EASIER"),
("""Try this. Research the market pay for your role. If you're below it, prepare a case for a raise, or explore other opportunities.""", "Salary research on laptop", "KNOW YOUR MARKET VALUE"),
])

pr("""That's angle one. Inflation, the growth gap, the savings ceiling, taxes on interest, cash's real job, time and earning more. Now angle
two. The psychology.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
sc("""If the math is so clear, why do so many people keep their money in cash? Because the psychology of saving is powerful. Cash feels safe,
investing feels risky, and our brains are wired to avoid losses. Here are seven psychological reasons people get stuck as savers, and how to
move forward.""",
   "Brain with piggy bank", "WHY PEOPLE GET STUCK")

item(8, "The illusion of safety", "cash feels safe",
"""Lesson number eight. Cash feels safe, but it isn't risk free.""", [
("""The number in a savings account never goes down. That stability feels like safety. But inflation is a risk too. It's just slow and
invisible, so it doesn't trigger the same fear as a falling stock price.""", "Calm savings balance", "STABLE ISN'T THE SAME AS SAFE"),
("""Economists sometimes call this money illusion, the tendency to think in nominal dollars instead of real buying power. A balance of ten
thousand dollars feels the same today and in twenty years, even though it buys much less later.""", "Dollar bills fading", "MONEY ILLUSION"),
("""Long term, the biggest financial risk for many savers isn't a market crash. It's running out of money in retirement, or never building
enough to have options.""", "Worried retiree", "THE BIGGER RISK"),
("""Recognizing both risks, market risk and inflation risk, helps you balance them, instead of only avoiding the one that feels scarier.""", "Balance scale", "BALANCE BOTH RISKS"),
("""There's also a risk in being too cautious with your career and income. Never asking for a raise, never learning new skills or never
taking a chance on a better job can quietly cost far more over a lifetime than a market crash. Playing it safe isn't always the safe choice.""", "Person at career crossroads", "PLAYING SAFE ISN'T ALWAYS SAFE"),
("""Try this. Ask yourself which worries you more, a temporary market drop or not having enough at seventy. Your answer can guide how much you
keep in cash.""", "Person thinking", "WHICH RISK SCARES YOU MORE?"),
])

body_hook = "Being a good saver can secretly hold you back. Here's how."
item(9, "Frugality fatigue", "cutting forever doesn't work",
"""Lesson number nine. Frugality fatigue is real.""", [
("""Some people try to get rich by cutting every possible expense. No vacations, no dinners out, no small pleasures. It can work for a while,
but many people burn out, and then swing back to overspending.""", "Tired person with coupons", "CUTTING EVERYTHING BURNS PEOPLE OUT"),
("""Extreme frugality can also take time and energy away from things that grow wealth faster, like building skills, networking or starting a
business. Spending hours to save a few dollars can be a poor trade.""", "Clock and coins", "TIME HAS VALUE TOO"),
("""A more sustainable approach is to cut ruthlessly on things you don't care about, and spend on things that truly matter to you. That keeps
saving sustainable for decades.""", "Happy person on vacation", "CUT WHAT YOU DON'T CARE ABOUT"),
("""Being a great saver is a strength. The trap is believing saving is the only lever. The most successful wealth builders pull several levers at
once.""", "Several levers", "SAVING IS ONE LEVER"),
("""Ramit Sethi calls this spending extravagantly on the things you love and cutting costs mercilessly on the things you don't. It
turns saving from a punishment into a choice, and choices are much easier to stick with than rules that feel like punishment.""", "Person enjoying favorite hobby", "SPEND ON WHAT YOU LOVE"),
("""Try this. List three expenses you'd happily cut and three you'd never give up. Cut the first three, keep the second three, and invest the
difference.""", "Two lists", "CUT THREE, KEEP THREE"),
])

item(10, "Fear of losing money", "loss aversion keeps people in cash",
"""Lesson number ten. Fear of losing money keeps people in cash.""", [
("""Psychologists Daniel Kahneman and Amos Tversky found that losses tend to feel about twice as painful as equal gains feel good. That makes
investing, where losses are visible, feel much scarier than keeping cash.""", "Scale with loss heavier", "LOSSES HURT ABOUT TWICE AS MUCH"),
("""Many people who lived through crashes, like 2008, kept their money in cash for years afterward, missing much of the recovery that followed.""", "Person hiding money under mattress", "AFTER A CRASH"),
("""One way to reduce fear is to start small and invest automatically, so you're not making a big emotional decision all at once. Another is
choosing a balanced fund with both stocks and bonds, which tends to swing less.""", "Small automatic investment", "START SMALL AND AUTOMATIC"),
("""Over time, as you see your investments recover from dips, fear usually fades. Experience builds confidence.""", "Growing confidence chart", "EXPERIENCE BUILDS CONFIDENCE"),
("""It also helps to zoom out. Over a single day, the stock market falls quite often. Over a single year, it has risen more often than it has
fallen historically. Over twenty year periods, the S and P five hundred has historically delivered positive total returns, though the past
doesn't guarantee the future. The longer your time horizon, the less frightening the short term swings look.""", "Zooming out on chart", "ZOOM OUT"),
("""Try this. Invest a small amount automatically each month for one year, and watch what happens without reacting. Then decide whether to
increase it.""", "Calendar with checkmarks", "A ONE YEAR EXPERIMENT"),
])

pr("""Quick pause. If this is changing how you think about your savings, please subscribe to Ryan Rover Money. It's free, and it helps us keep
making these. Now, lesson eleven.""")

item(11, "Scarcity mindset", "focused on now, not later",
"""Lesson number eleven. A scarcity mindset narrows your focus.""", [
("""Economist Sendhil Mullainathan and psychologist Eldar Shafir wrote a book called Scarcity. They argue that when people feel they don't
have enough, money or time, their attention narrows to immediate needs, making long term planning harder.""", "Book on desk", "SCARCITY NARROWS FOCUS"),
("""For savers, a scarcity mindset can show up as hoarding cash out of fear, even when there's enough for emergencies. It feels safe, but it can
block growth.""", "Person clutching money", "HOARDING FROM FEAR"),
("""Building a solid emergency fund first can help break this cycle. Once you know emergencies are covered, it becomes easier to think about
investing for the future.""", "Full emergency fund", "SECURITY ENABLES GROWTH"),
("""Reframing helps too. Investing isn't spending money. It's moving money from a place where it shrinks to a place where it can grow.""", "Money moving between jars", "INVESTING ISN'T SPENDING"),
("""Scarcity can also be a phase, not a permanent state. Many people who once lived paycheck to paycheck later build real wealth. The key
is moving step by step, first stability, then savings, then investing, so each stage gives you the breathing room to think about the next.""", "Steps leading upward", "SCARCITY CAN BE A PHASE"),
("""Try this. Once your emergency fund is full, write down a specific long term goal for the next dollar you save. Purpose makes investing feel
less risky.""", "Goal written on paper", "GIVE IT PURPOSE"),
])

item(12, "The saver identity", "who you think you are",
"""Lesson number twelve. Being a saver can become your whole identity.""", [
("""Many careful people proudly see themselves as savers. That identity is valuable, but it can also make investing feel like a betrayal of who
they are, as if taking any risk is irresponsible.""", "Proud saver", "PROUD TO BE A SAVER"),
("""Expanding your identity from saver to investor or owner can be powerful. Investors still save. They just put their savings to work.""", "Person changing hats", "FROM SAVER TO INVESTOR"),
("""Many millionaires studied by Thomas Stanley and William Danko in The Millionaire Next Door were careful savers, but they also invested
consistently and often owned businesses.""", "Book cover", "MILLIONAIRES SAVE AND INVEST"),
("""Saving is how you collect the seeds. Investing is how you plant them.""", "Seeds being planted", "COLLECT SEEDS, THEN PLANT"),
("""Your saving skills are a huge advantage as an investor. The discipline to live below your means is exactly what lets you invest
consistently through good markets and bad. Many people who earn more never build wealth because they can't save. You already have the
hardest part.""", "Disciplined person with plan", "YOU HAVE THE HARDEST PART"),
("""Try this. Say out loud, I'm a saver and an investor. Then take one small action this week that an investor would take.""", "Person speaking confidently", "SAVER AND INVESTOR"),
])

item(13, "Waiting for certainty", "the perfect time never comes",
"""Lesson number thirteen. Waiting for certainty keeps money idle.""", [
("""Many savers plan to invest once things settle down, once the market drops, once they understand everything. But markets are never certain,
and there's always a reason to wait.""", "Person waiting at window", "THERE'S ALWAYS A REASON TO WAIT"),
("""Meanwhile, months turn into years. Every year in cash is a year of missed compounding and lost buying power.""", "Calendar pages flying", "YEARS SLIP AWAY"),
("""Dollar cost averaging, investing a fixed amount on a regular schedule, removes the need to pick the perfect time. You buy more shares when
prices are low and fewer when they're high.""", "Shares at different prices", "DOLLAR COST AVERAGING"),
("""You don't need to understand everything to start. A simple, low cost, diversified fund is a reasonable starting point for many people.""", "Simple fund on screen", "START SIMPLE"),
("""Remember too that investing isn't all or nothing. You don't have to move all your savings at once. You can invest a portion now and
add more each month. That spreads out your timing and makes the first step much less intimidating.""", "Gradual steps", "NOT ALL OR NOTHING"),
("""Try this. Set a date within the next two weeks to make your first investment. A deadline turns waiting into action.""", "Calendar with circled date", "SET A START DATE"),
])

item(14, "The world changed", "pensions disappeared",
"""Lesson number fourteen. The rules changed since our grandparents' time.""", [
("""Decades ago, many workers had pensions. Employers promised a monthly check for life in retirement, and they managed the investing. Workers
could simply save a little and rely on the pension.""", "Vintage factory workers", "PENSIONS USED TO BE COMMON"),
("""Today, most private sector workers rely on four oh one k style plans instead. The responsibility for investing and making money last has
shifted from employers to individuals.""", "401k paperwork", "NOW IT'S ON YOU"),
("""That means saving alone isn't enough anymore. Without investing, there's nothing to replace the growth a pension fund used to provide.""", "Empty pension envelope", "YOU NEED THE GROWTH"),
("""The upside is control. You choose how much to invest, where to invest it and when to increase it.""", "Person in control at desk", "THE UPSIDE IS CONTROL"),
("""People are also living longer. A retirement that starts at sixty five can last thirty years or more. Money that needs to last three
decades can't just sit still. It needs to keep growing, even during retirement, to keep up with rising costs.""", "Elderly couple hiking", "RETIREMENTS LAST LONGER"),
("""Try this. If your employer offers a retirement plan, find out how it's invested and make sure your money isn't sitting in a cash option by
default.""", "Retirement plan options", "CHECK YOUR PLAN'S DEFAULT"),
])

pr("""That's angle two. The illusion of safety, frugality fatigue, fear of loss, scarcity, the saver identity, waiting for certainty and a changed
world. Now angle three. The playbook.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
sc("""Here's how to turn saving into wealth. Six moves that combine saving with the three real engines of wealth, investing, earning more and
owning.""",
   "Toolbox on table", "SIX MOVES")

item(15, "Save with a destination", "every dollar has a next step",
"""Move number fifteen. Save with a destination.""", [
("""Start by saving an emergency fund of three to six months of essential expenses in a high yield savings account. That's your foundation.""", "Emergency fund in bank app", "THE FOUNDATION"),
("""Then set a rule. Every dollar saved beyond that has a destination, a specific short term goal or long term investing.""", "Arrow pointing forward", "EVERY DOLLAR HAS A DESTINATION"),
("""Automation makes this easy. Set up automatic transfers on payday to your emergency fund, then to your investment accounts.""", "Automatic transfers", "AUTOMATE THE FLOW"),
("""Once your emergency fund is full, redirect that transfer to investing. The habit stays the same, but the money starts growing.""", "Redirected transfer", "REDIRECT WHEN FULL"),
("""Short term goals deserve a plan too. Money for a car in two years or a home down payment in three can sit in a high yield savings
account, CDs or Treasury bills, where it earns some interest without stock market risk. Matching each goal to the right account is what
saving with a destination really means.""", "Goal labeled savings accounts", "MATCH GOALS TO ACCOUNTS"),
("""Try this. Check your emergency fund. If it's full, set up an automatic transfer of your extra savings into an investment account this week.""", "Person setting up transfer", "REDIRECT THIS WEEK"),
])

item(16, "Invest automatically", "let compounding work",
"""Move number sixteen. Invest automatically.""", [
("""Investing doesn't have to be complicated. Low cost, broad index funds or target date funds let you own a diversified portfolio with one or two
choices.""", "Simple fund options", "KEEP IT SIMPLE"),
("""Automatic monthly investing removes emotion and timing from the process. The money moves before you can spend it or worry about the market.""", "Calendar with automatic investment", "REMOVE EMOTION"),
("""Turn on dividend reinvestment, so every dividend buys more shares and compounding keeps running.""", "Dividend reinvestment setting", "REINVEST DIVIDENDS"),
("""Increase your automatic investment every time your income rises. Your savings rate grows without feeling painful.""", "Increasing contributions", "INCREASE WITH RAISES"),
("""Keep costs low as you invest. Fund fees come out of your returns every year. A fund charging a few hundredths of a percent leaves far
more of the growth to you than one charging one percent, and over decades the difference can be tens or even hundreds of thousands of
dollars.""", "Fee comparison chart", "KEEP COSTS LOW"),
("""Try this. Set up an automatic monthly investment into a low cost index fund, even if it's small, and schedule a reminder to raise it in six months.""", "Phone reminder", "START TODAY"),
])

body_hook = "The fastest way to build wealth isn't saving more. It's this."
item(17, "Grow your income", "the biggest lever",
"""Move number seventeen. Grow your income.""", [
("""Your income is your biggest wealth building tool. Every extra dollar earned and invested can compound for decades.""", "Rising paycheck", "YOUR BIGGEST TOOL"),
("""Ways to grow income include asking for raises, switching jobs, getting certifications, learning in demand skills or starting a side business.""", "Ladder of income options", "MANY WAYS TO EARN MORE"),
("""Negotiating your starting salary matters too, because future raises often build on it. A small difference early can grow over an entire career.""", "Negotiation meeting", "NEGOTIATE EARLY"),
("""The key is to invest income increases, not spend them all. If you raise your lifestyle with every raise, your wealth won't grow.""", "Split raise illustration", "INVEST YOUR RAISES"),
("""Side income counts too. Even a few hundred dollars a month from freelancing or a small business, invested consistently, can add up to
a meaningful amount over a decade or two. And unlike cutting expenses, side income can grow over time as your skills and reputation grow.""", "Freelancer at laptop", "SIDE INCOME CAN GROW"),
("""Try this. Choose one skill that could increase your income in the next year, and spend thirty minutes a day learning it.""", "Person studying", "ONE SKILL, 30 MINUTES A DAY"),
])

item(18, "Build ownership", "own things that grow",
"""Move number eighteen. Build ownership.""", [
("""Wealth usually comes from owning things that grow, like stocks, businesses and real estate. Wages pay your bills. Ownership builds wealth.""", "House, stocks and business icons", "OWNERSHIP BUILDS WEALTH"),
("""Owning index funds makes you a part owner of hundreds of companies. Their profits and growth become your growth.""", "Index fund ownership", "OWN PIECES OF COMPANIES"),
("""Some people also build ownership through a small business or rental property. These take more work and risk, but can grow wealth faster.""", "Small business owner", "BUSINESS AND REAL ESTATE"),
("""Even employee stock purchase plans or equity compensation can add ownership, though it's wise not to concentrate too much in your employer.""", "Stock options document", "EMPLOYER EQUITY, CAREFULLY"),
("""Ownership also changes how you experience the economy. When companies grow profits, workers might get a raise, but owners get the
growth. Being both a worker and an owner lets you benefit from your paycheck and from the economy's growth at the same time.""", "Worker and owner icons", "BE A WORKER AND AN OWNER"),
("""Try this. Look at your net worth and calculate what percentage is in assets that can grow. Aim to increase it each year.""", "Net worth breakdown", "INCREASE YOUR OWNERSHIP"),
])

item(19, "Use tax advantaged accounts", "keep more of the growth",
"""Move number nineteen. Use tax advantaged accounts.""", [
("""Four oh one ks, IRAs, Roth IRAs and HSAs let your investments grow with tax advantages. That means more money stays invested and compounding.""", "Retirement account icons", "TAX ADVANTAGED GROWTH"),
("""If your employer offers a match, contribute at least enough to get it. It's one of the best returns available anywhere.""", "Employer match illustration", "GET THE MATCH"),
("""Roth accounts can provide tax free withdrawals in retirement, which can be especially valuable if you start early.""", "Roth IRA", "TAX FREE LATER"),
("""Check current contribution limits and rules on the IRS website, because they change over time.""", "IRS website", "CHECK THE LIMITS"),
("""Health savings accounts deserve a special mention. If you're eligible, HSAs can offer tax deductible contributions, tax free growth and
tax free withdrawals for qualified medical expenses. Some people invest their HSA for the long term and pay current medical costs out of
pocket.""", "HSA card", "DON'T FORGET THE HSA"),
("""Try this. Make sure you're contributing enough to get your full employer match, and open an IRA if you're eligible and don't have one.""", "Opening IRA on phone", "MATCH AND IRA"),
])

item(20, "Spend on what grows you", "investing in yourself",
"""Move number twenty. Spend on what grows you.""", [
("""Not all spending is equal. Spending on education, skills, health and relationships can increase your earning power and quality of life for
decades.""", "Person in class", "SOME SPENDING GROWS YOU"),
("""A course that leads to a promotion, a certification that raises your pay or a gym membership that keeps you healthy can pay off far more than
saving that money in cash.""", "Certification certificate", "INVESTMENTS IN YOURSELF"),
("""The key is to be intentional. Ask whether each big expense will grow your income, health or happiness over time.""", "Person evaluating purchase", "BE INTENTIONAL"),
("""Saving, investing, earning and growing yourself work together. Each one makes the others more powerful.""", "Four gears turning together", "THEY WORK TOGETHER"),
("""Think of it as a portfolio of your whole life. Cash for safety, investments for growth, skills for earning power, health for energy and
relationships for opportunity and happiness. Saving alone fills only one corner of that portfolio. Wealth comes from building all of it.""", "Life portfolio diagram", "A WHOLE LIFE PORTFOLIO"),
("""Try this. Pick one investment in yourself this year that could raise your income or improve your health, and commit to it.""", "Goal written down", "INVEST IN YOURSELF"),
])

# ---------------- Story ----------------
ch("Two siblings")
short("Two siblings saved the same amount for thirty years. One ended up far richer.")
sc("""Imagine two siblings who each save five hundred dollars a month for thirty years. Both are disciplined. Both skip the fancy cars. The first
keeps everything in a savings account earning about half a percent. The second keeps an emergency fund, then invests the rest in a low cost
index fund.""",
   "Two siblings side by side", "SAME HABIT")
sc("""After thirty years, the first sibling has roughly one hundred ninety four thousand dollars. The second, at a seven percent average yearly
return, could have roughly six hundred ten thousand. Same discipline, same savings, very different results.""",
   "Two account balances", "$194K VS $610K")
sc("""Both siblings were great savers. The difference wasn't how much they saved. It was what they did with their savings. Saving built the
foundation. Investing built the wealth.""",
   "Siblings at family dinner", "SAVING BUILT THE FOUNDATION")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. Should I stop saving and just invest? No. Keep an emergency fund in cash, then invest money you won't need for at least
five years. Saving and investing work together.""",
   "Savings and investing together", "SAVE AND INVEST")
sc("""Question two. Isn't investing risky? Yes, investments can lose value, especially in the short term. But keeping long term money in cash
has its own risk, losing buying power to inflation. Diversification and time help manage investment risk.""",
   "Risk balance", "ISN'T INVESTING RISKY?")
sc("""Question three. How much cash should I keep? Many people aim for three to six months of essential expenses, plus money for goals in the
next few years. More if your income is irregular.""",
   "Emergency fund calculator", "HOW MUCH CASH?")

sc("""Question four. What if the market crashes right after I invest? It can happen, and it's painful. But if you're investing for decades
and adding money regularly, a crash early on means your future contributions buy shares at lower prices. Historically, broad markets have
recovered from past crashes, though it sometimes took years.""",
   "Market chart dipping then rising", "WHAT IF IT CRASHES?")

# ---------------- By age ----------------
ch("From saver to investor at every age")
sc("""In your twenties, the biggest move is turning saving into investing as early as possible. Build a starter emergency fund, grab any
employer match and invest small amounts automatically. Your early dollars have the most time to grow, so even fifty or one hundred dollars a
month invested now can matter more than much larger amounts later.""",
   "Young adult with phone", "IN YOUR 20s: START INVESTING EARLY")
sc("""In your thirties and forties, income usually rises, and so does the temptation to spend it. This is the decade to invest every raise,
keep a solid emergency fund and avoid letting large cash piles sit idle for years. It's also a great time to invest in skills that raise your
income for the rest of your career.""",
   "Professional at desk", "IN YOUR 30s AND 40s: INVEST THE RAISES")
sc("""In your fifties and beyond, the balance shifts. You still need growth, because retirement can last decades, but you also need more
stability. Many people gradually add bonds and cash for near term needs while keeping a meaningful share invested for long term growth.""",
   "Mature couple planning", "IN YOUR 50s AND BEYOND: BALANCE")

# ---------------- Mistakes ----------------
ch("Three saver mistakes")
sc("""Mistake one. Keeping retirement money in cash inside a retirement account. Some people contribute to a four oh one k or IRA but never
choose investments, so the money sits in a cash option for years. Check that your contributions are actually invested.""",
   "Retirement account in cash", "MISTAKE 1: UNINVESTED RETIREMENT MONEY")
sc("""Mistake two. Saving for everything except growth. Vacations, cars and holidays all get their own savings, but long term investing comes
last, if at all. Pay your future self first by automating investments before other savings goals.""",
   "Savings jars with empty growth jar", "MISTAKE 2: GROWTH COMES LAST")
sc("""Mistake three. Waiting for a big lump sum. Some people wait until they've saved a large amount before investing. But regular small
investments started now usually beat a larger investment started years later.""",
   "Person waiting with piggy bank", "MISTAKE 3: WAITING FOR A LUMP SUM")

# ---------------- Recap ----------------
ch("Recap")
sc("""Quick recap. Angle one, the numbers. Inflation, the growth gap, the savings ceiling, taxes on interest, cash's job, time and earning more.""",
   "Checklist on clipboard", "THE NUMBERS: 1 TO 7")
sc("""Angle two, the psychology. The illusion of safety, frugality fatigue, fear of loss, scarcity, the saver identity, waiting for certainty
and a changed world.""",
   "Person thinking", "THE PSYCHOLOGY: 8 TO 14")
sc("""Angle three, the playbook. Save with a destination, invest automatically, grow your income, build ownership, use tax advantaged accounts
and spend on what grows you.""",
   "Notebook with plan", "THE PLAYBOOK: 15 TO 20")

# ---------------- Close ----------------
ch("What to do next")
pr("""Saving is where wealth begins, but it isn't where wealth is made. Put your savings to work, grow your income and own things that grow. If
you want my full step by step plan, it's in my playbook, linked in the description. Tell me in the comments, how much of your savings is
working for you? I'm Ryan Rover. See you in the next one.""")

save("video40", "Why Saving Alone Will Never Make You Rich", [
    "U.S. Bureau of Labor Statistics: Consumer Price Index, long-run inflation",
    "Jeremy Siegel, Stocks for the Long Run: long-run real returns on stocks, bonds and bills",
    "S&P Dow Jones Indices: S&P 500 total returns",
    "IRS: taxation of interest, retirement accounts and contribution limits",
    "Federal Reserve Bank of Atlanta, Wage Growth Tracker: job switchers vs stayers",
    "Kahneman and Tversky, Prospect Theory (Econometrica, 1979)",
    "Mullainathan and Shafir, Scarcity: Why Having Too Little Means So Much (2013)",
    "Stanley and Danko, The Millionaire Next Door (1996)",
    "Growth examples: monthly compounding at stated average returns (illustrations, not promises)",
], "why saving alone won't make you rich, 20 lessons from 3 angles: numbers, psychology, playbook")
