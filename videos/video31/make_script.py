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
pr("""Hi, I'm Ryan Rover. One hundred dollars a month. It's a dinner out for two. A couple of streaming services and a
takeout order. It's the kind of money that disappears without anyone noticing. But what if you didn't let it disappear?
What if you invested that one hundred dollars every single month for twenty years? Today we're going to find out exactly
what it becomes, with real math, and why such a small number can quietly change your life.""")
short("What does one hundred dollars a month become in twenty years?")
card("""Here's the headline. One hundred dollars a month for twenty years, at a seven percent average yearly return,
grows to roughly fifty two thousand dollars. You'd put in twenty four thousand. The other twenty eight thousand is
growth.""",
     {"type": "growth", "monthly": 100, "rate": 0.07, "years": 20})
sc("""Let's be honest about what that number means. Fifty two thousand dollars won't make you a millionaire. But it's
an emergency fund, a down payment on a home in many parts of the country, a year or two of retirement income, or a debt
free start for a child. And it came from money most people spend without noticing. More importantly, one hundred dollars
a month is just the beginning. Once you see how the math works, you'll understand why people who start small often end up
investing much more.""",
   "Coins stacking up growing", "$24,000 IN, $52,000 OUT")
sc("""We'll explore this from three angles. First, the numbers. What one hundred dollars a month becomes at different
returns, over different time periods, and after fees, taxes and inflation. Second, the psychology. Why small amounts feel
pointless, and why that feeling is so misleading. And third, the playbook. Exactly where to put your one hundred dollars,
in what order, so it works as hard as possible. Quick reminder. Seven percent is an illustration, not a promise. Markets go
up and down, and real returns will vary.""",
   "Three paths in a park", "THREE ANGLES")
pr("""Let's start with the numbers. And the first lesson is about the most important ingredient in this whole recipe.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our numbers. All growth examples use monthly compounding with stated average yearly returns, like four, seven and
ten percent. These are illustrations, not predictions. Historical stock market data comes from sources like the S and P
Dow Jones Indices, and long run return research from economists like Aswath Damodaran at New York University. Account
rules come from the IRS. Inflation data comes from the Bureau of Labor Statistics. This is education, not financial
advice.""",
   "Stock market data screen", "OUR NUMBERS")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Seven lessons about what one hundred dollars a month really becomes.""")

item(1, "Time is the main ingredient", "years matter more than dollars",
"""Lesson number one. Time matters more than the amount.""", [
("""Here's what one hundred dollars a month becomes at a seven percent average yearly return, over different lengths of
time. After ten years, roughly seventeen thousand dollars. After twenty years, roughly fifty two thousand. After thirty
years, roughly one hundred twenty two thousand. After forty years, roughly two hundred sixty two thousand. Notice
something. Each extra ten years more than doubles the result.""", "Hourglass with sand", "10, 20, 30, 40 YEARS"),
("""That's compounding. In the early years, most of your balance is money you put in. In the later years, most of it is
growth on growth. By year forty in our example, you've contributed forty eight thousand dollars, and the growth is more
than two hundred thousand. Time doesn't just add to the result. It multiplies it.""", "Snowball rolling downhill", "GROWTH ON GROWTH"),
("""This is why starting early is so powerful. Someone who invests one hundred dollars a month from age twenty five to
sixty five could end up with far more than someone who invests two hundred dollars a month from forty five to sixty five,
even though the second person puts in the same total amount over a shorter period. Time does the heavy lifting.""",
 "Young person and older person", "EARLY BEATS BIG"),
("""Try this. Open a free compound interest calculator online. Enter one hundred dollars a month, seven percent, and
your own number of years until retirement. Look at how much of the final number is growth. That one screen can change how
you think about every dollar.""", "Calculator on laptop screen", "RUN YOUR NUMBERS"),
])

card("""Here's the forty year version. One hundred dollars a month for forty years, at a seven percent average yearly
return, grows to roughly two hundred sixty two thousand dollars. Total put in, forty eight thousand.""",
     {"type": "growth", "monthly": 100, "rate": 0.07, "years": 40})

item(2, "The rate changes everything", "4%, 7% or 10%",
"""Lesson number two. The return rate makes a huge difference.""", [
("""Let's try different returns over twenty years. At four percent, one hundred dollars a month becomes roughly
thirty seven thousand dollars. At seven percent, roughly fifty two thousand. At ten percent, roughly seventy six thousand.
Same contributions. Same time. The only difference is the average return.""", "Three bar charts comparison", "4% VS 7% VS 10%"),
("""Where do those numbers come from? Over very long periods, the US stock market, as measured by the S and P five
hundred, has historically returned roughly ten percent a year on average before inflation, according to long run data.
After inflation, it's been closer to seven percent. Bonds have historically returned less. A savings account usually
returns less still. But past returns are no guarantee of future returns, and some decades have been much worse than
average.""", "S&P 500 historical chart", "HISTORY, NOT A PROMISE"),
("""That's why many people use seven percent for planning. It's a rough estimate of long run stock returns after
inflation, so the result is in today's dollars. If you use ten percent, you should remember that the result is in future
dollars, which will buy less because of inflation.""", "Calculator with percent sign", "WHY 7% FOR PLANNING"),
("""Try this. Run your numbers at four, seven and ten percent. Plan with the middle or lower number, and treat anything
better as a bonus. Conservative planning means fewer unpleasant surprises.""", "Planning notebook with numbers", "PLAN CONSERVATIVELY"),
])

body_hook = "A tiny fee can eat thousands of your dollars. Here's how."
item(3, "Fees quietly eat growth", "the 1% that costs thousands",
"""Lesson number three. Fees matter more than you think.""", [
("""Let's say your investment earns seven percent before fees. In a low cost index fund with a fee of a small fraction of
a percent, you keep almost all of that. In a fund charging one percent a year, your effective return drops to around six
percent. On one hundred dollars a month over twenty years, that's the difference between roughly fifty two thousand
dollars and roughly forty six thousand.""", "Receipt with fees highlighted", "7% VS 6% AFTER FEES"),
("""Over forty years, the gap gets much bigger, because fees compound just like returns. A one percent fee can take a
surprisingly large share of your final balance over a lifetime of investing. And the fee is charged every year, whether
your investments go up or down.""", "Chart with gap widening", "FEES COMPOUND TOO"),
("""This is a big reason low cost index funds became so popular. Researchers like those at S and P Dow Jones Indices,
in their SPIVA reports, have found that over long periods most actively managed funds underperformed their benchmark
index after fees. Lower costs are one of the few things investors can fully control.""", "Index fund prospectus", "COSTS YOU CAN CONTROL"),
("""Try this. Look up the expense ratio of every fund you own, in your retirement plan and anywhere else. If you see one
percent or more, check whether your plan offers a lower cost alternative in the same category.""", "Fund expense ratio on screen", "CHECK YOUR FEES"),
])

item(4, "Inflation shrinks the number", "future dollars buy less",
"""Lesson number four. Inflation means future dollars buy less.""", [
("""Inflation is the gradual rise in prices over time. The Federal Reserve targets about two percent inflation a year
over the longer run, and actual inflation has sometimes been much higher, as Americans saw in twenty twenty two. At
three percent inflation, prices roughly double in about twenty four years.""", "Grocery prices rising", "PRICES RISE"),
("""That's why the seven percent example is useful. Because it's roughly a return after inflation, fifty two thousand
dollars in twenty years means roughly the buying power of fifty two thousand dollars today. If you used a ten percent
nominal return, you'd get a bigger number, but it would buy less.""", "Old and new price tags", "TODAY'S DOLLARS"),
("""Inflation is also why keeping long term money in cash is risky in its own way. A savings account paying less than
inflation slowly loses buying power, even though the balance never goes down. For short term money, that's fine. For
twenty year money, it's a real cost.""", "Cash in jar losing value", "CASH LOSES BUYING POWER"),
("""Try this. When you see any long term projection, ask, is this in today's dollars or future dollars? It's one of the
most useful questions in personal finance.""", "Question mark on paper", "TODAY'S OR FUTURE DOLLARS?"),
])

item(5, "Taxes and the right account", "where you invest matters",
"""Lesson number five. The type of account changes what you keep.""", [
("""In a regular taxable brokerage account, you may owe taxes on dividends each year and on gains when you sell. In tax
advantaged accounts like a four oh one k or an IRA, the money can grow without yearly taxes. That difference can add up
to thousands of dollars over twenty years.""", "Tax forms and calculator", "TAXABLE VS TAX ADVANTAGED"),
("""A Roth IRA is especially powerful for small, long term contributions. You contribute money you've already paid tax
on, and if you follow the rules, qualified withdrawals in retirement are tax free, including all the growth. On our
fifty two thousand dollar example, that could mean all twenty eight thousand of growth is never taxed. Income limits and
rules apply, so check the current IRS guidelines.""", "Roth IRA paperwork", "TAX FREE GROWTH"),
("""A traditional four oh one k or IRA works differently. Contributions may reduce your taxes today, and you pay income
tax when you withdraw in retirement. Both can be great choices. The best one depends on your tax bracket now and what you
expect it to be later.""", "Retirement plan enrollment", "PAY TAX NOW OR LATER"),
("""Try this. If you're investing one hundred dollars a month, find out whether you have access to a workplace plan with
a match, and whether you're eligible for a Roth IRA. Those are usually the first places to look.""", "Laptop with retirement account", "FIND THE RIGHT ACCOUNT"),
])

item(6, "Raising it changes everything", "$100 is a starting point",
"""Lesson number six. Increasing the amount, even slowly, changes everything.""", [
("""One hundred dollars a month for twenty years at seven percent becomes roughly fifty two thousand dollars. Two hundred
dollars becomes roughly one hundred four thousand. Five hundred dollars becomes roughly two hundred sixty thousand. The
growth scales directly with the amount.""", "Stacks of coins growing", "$100, $200, $500"),
("""But you don't need to jump straight to five hundred. If you start at one hundred and raise it by just a few percent
every year, perhaps when you get a raise, the final result can be dramatically higher than staying at one hundred forever.
Small increases compound on top of compounding.""", "Graph with rising steps", "STEP IT UP"),
("""This is where many people's financial lives quietly turn around. They start small, see the balance grow, feel
motivated, and gradually increase. Five years later, they're investing several hundred dollars a month, and it feels
normal.""", "Happy person checking investments", "SMALL STARTS GROW"),
("""Try this. Set a calendar reminder for every raise or every new year, to increase your monthly investment by at
least ten dollars. You'll barely notice the difference in your budget, but your future self will.""", "Calendar reminder on phone", "PLUS TEN DOLLARS")
])

card("""Here's what five hundred dollars a month becomes over twenty years at a seven percent average yearly return. Roughly
two hundred sixty thousand dollars. Total put in, one hundred twenty thousand.""",
     {"type": "growth", "monthly": 500, "rate": 0.07, "years": 20})

item(7, "Bad years are part of it", "the path isn't smooth",
"""Lesson number seven. The path won't be smooth.""", [
("""Seven percent is an average. In real life, some years will be much better and some much worse. The US stock market
fell about thirty seven percent in two thousand eight, including dividends, and about eighteen percent in twenty twenty two,
according to S and P five hundred total return data. There will be years when your one hundred dollars a month seems to be
shrinking.""", "Stock market crash red screen", "-37% IN 2008"),
("""But here's the twist. When you invest the same amount every month, bad years mean you buy more shares at lower
prices. That's called dollar cost averaging. It doesn't guarantee profits or prevent losses, but it means market drops
aren't only bad news. They're also a sale on what you're buying.""", "Sale price tag", "BUYING ON SALE"),
("""Historically, investors who kept investing through downturns were generally better off than those who stopped or
sold in a panic. The biggest risk for a small monthly investor often isn't the market. It's quitting.""", "Person staying calm at desk", "DON'T QUIT"),
("""Try this. Write a one sentence note to your future self today. When the market drops, I will keep investing my one
hundred dollars a month. Put it where you'll see it.""", "Handwritten note on fridge", "A NOTE TO FUTURE YOU"),
])

pr("""That's angle one. Time, return rate, fees, inflation, taxes, raising the amount, and the bumpy path. Now angle two.
The psychology. Because the math is simple. The hard part is actually doing it, month after month.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
sc("""If the math is so clear, why doesn't everyone invest one hundred dollars a month? Because our brains aren't built for
long term compounding. We think in straight lines, we value today over tomorrow, and small amounts feel pointless. Let's
look at the mental hurdles, and how to jump over them.""",
   "Brain illustration thinking", "THE MENTAL HURDLES")

body_hook = "One hundred dollars feels too small to matter. It isn't."
item(8, "It feels too small to matter", "the small number trap",
"""Lesson number eight. One hundred dollars feels too small to bother.""", [
("""Many people think, what's the point of investing one hundred dollars? I'll start when I can invest real money. But
waiting costs time, and time is the most valuable ingredient. Five years of waiting can mean losing a large share of the
final result.""", "Person shrugging", "WHY BOTHER?"),
("""Economists Victor Stango and Jonathan Zinman described exponential growth bias, our tendency to underestimate
compounding. We imagine growth as a straight line, so small amounts look small forever. In reality, they curve upward over
time.""", "Straight line vs curve graph", "STRAIGHT LINE THINKING"),
("""There's also a habit benefit. Investing one hundred dollars teaches you how accounts work, how markets move, and how
it feels to see a drop. When you have more money later, you'll already know what to do.""", "Person learning on laptop", "PRACTICE WITH SMALL MONEY"),
("""Try this. Instead of asking whether one hundred dollars matters, ask what it becomes in twenty or thirty years. Then
start this month.""", "Calendar first of month", "START THIS MONTH"),
])

item(9, "Waiting for the perfect time", "time in vs timing",
"""Lesson number nine. There's no perfect time to start.""", [
("""People often wait for the market to drop, or for things to calm down, before investing. But nobody can reliably
predict short term market moves. Missing even a handful of the best days in the market historically reduced long term
returns significantly, according to analyses by firms like J.P. Morgan Asset Management.""", "Clock and stock chart", "TIMING THE MARKET"),
("""Many of the best days happened close to the worst days, during periods of high fear. Investors who sat out to avoid
the bad days often missed the recovery too. In other words, the moments that feel most dangerous are often the moments
when staying invested matters most.""", "Stock rebound chart", "BEST DAYS NEAR WORST DAYS"),
("""For a monthly investor, the solution is simple. Invest the same amount on the same day every month, regardless of
headlines. That removes the timing decision entirely.""", "Calendar with recurring date", "SAME DAY EVERY MONTH"),
("""Try this. Pick a date right after payday and set your automatic investment for that day. Then stop checking the news
to decide.""", "Automatic investment setup screen", "AUTOMATE THE DATE"),
])

item(10, "Present bias", "the latte today vs the money later",
"""Lesson number ten. Today always feels more important than twenty years from now.""", [
("""Present bias makes immediate rewards feel much bigger than future ones. One hundred dollars today feels like a nice
dinner. Fifty two thousand dollars in twenty years feels abstract.""", "Restaurant dinner table", "TODAY FEELS BIGGER"),
("""Some research has found that when people see age progressed images of themselves, they become more willing to save
for the future. Making the future feel real helps fight present bias.""", "Aging face illustration", "MEET FUTURE YOU"),
("""Another trick is to tie the future money to something specific. Not just retirement, but freedom to change careers,
a paid off house, or helping your kids. Specific goals feel more real.""", "House keys and goals", "MAKE IT SPECIFIC"),
("""Try this. Give your investment account a nickname, like freedom fund or future house. It sounds small, but naming
your goal can make it feel closer.""", "Bank app with nickname", "NAME YOUR GOAL"),
])

item(11, "Checking too often", "watching makes you nervous",
"""Lesson number eleven. Checking your account too often can make you a worse investor.""", [
("""Markets go up and down daily. If you check every day, you'll see a lot of red. Research on loss aversion shows losses
feel about twice as painful as equal gains feel good. Frequent checking magnifies the pain.""", "Phone with red stock app", "DAILY RED"),
("""Studies by Shlomo Benartzi and Richard Thaler described myopic loss aversion. Investors who looked at results more
often tended to take less risk and choose worse long term strategies.""", "Person stressed at screen", "MYOPIC LOSS AVERSION"),
("""For a twenty year plan, checking once a month or even once a quarter is plenty. You'll see the long term trend instead
of the daily noise.""", "Calendar quarterly check", "CHECK QUARTERLY"),
("""Try this. Delete the investing app from your home screen, or turn off price notifications. Let the money work while
you live your life.""", "Phone notifications settings", "TURN OFF THE NOISE"),
])

pr("""Quick break. If this is helping you see small money differently, subscribe to Ryan Rover Money. It's free and it
helps the channel grow. Okay, lesson twelve.""")

item(12, "Comparing with big investors", "your race, your pace",
"""Lesson number twelve. Don't compare your hundred dollars with someone else's thousands.""", [
("""Online, you'll see people investing thousands a month, or showing huge gains. That can make one hundred dollars feel
embarrassing. But comparison is a trap. You don't know their income, their debt, or their losses.""", "Social media investment posts", "THE COMPARISON TRAP"),
("""Every investor starts somewhere. Many people who invest large amounts today started with small automatic
contributions years ago. The difference is that they kept going.""", "Seedling growing into tree", "EVERYONE STARTS SMALL"),
("""Your plan only has to work for you. One hundred dollars a month, kept up for decades and increased over time, is a
real plan.""", "Person running own race", "YOUR OWN PLAN"),
("""Try this. Track only your own progress. Write down your balance every six months and compare it with your past self.""", "Notebook progress tracking", "COMPARE WITH YOUR PAST"),
])

item(13, "Fear of losing it", "risk vs doing nothing",
"""Lesson number thirteen. Fear of losing money keeps many people from starting.""", [
("""Investing does involve risk. Stock prices can fall, sometimes a lot. But not investing has its own risk. Inflation
slowly erodes cash, and missing decades of growth can leave you short in retirement.""", "Person hesitating at door", "FEAR OF LOSING"),
("""Diversification reduces the risk of any single company failing. Broad index funds hold hundreds or thousands of
companies. A long time horizon gives investments time to recover from downturns. Historically, the longer the holding
period, the less often broad US stock investments ended with a loss, though there are no guarantees and some long
periods have been disappointing.""", "Diversified portfolio chart", "SPREAD THE RISK"),
("""Your emergency fund also helps. If you have cash for surprises, you won't be forced to sell investments at a bad
time.""", "Emergency fund savings", "CASH FOR SURPRISES"),
("""Try this. Before investing, build a small emergency fund. Then invest money you won't need for at least five years.""", "Savings and investing jars", "EMERGENCY FUND FIRST"),
])

item(14, "Forgetting why", "keeping the habit alive",
"""Lesson number fourteen. Motivation fades, so systems matter.""", [
("""Starting is exciting. Month thirty seven is boring. Many people stop contributing after the novelty wears off, or when
life gets busy. A move, a new baby, a job change, and suddenly the transfer gets paused and never restarted. Those pauses,
more than market crashes, are what quietly shrink many people's results.""", "Person bored at desk", "MONTH 37 IS BORING"),
("""That's why automation matters so much. Once the transfer is automatic, it happens whether you feel motivated or not.
Research on automatic enrollment in retirement plans shows defaults have a huge effect on participation.""", "Automatic transfer arrow", "AUTOMATION WINS"),
("""Visual reminders help too. A chart of your balance on the fridge, or a yearly check in where you celebrate progress.""", "Progress chart on fridge", "CELEBRATE PROGRESS"),
("""Try this. Once a year, on the same date, check your balance, celebrate your progress, and raise your contribution.""", "Annual review calendar", "ONCE A YEAR"),
])

pr("""That's angle two. Small numbers, timing, present bias, checking too often, comparison, fear and fading motivation.
Now angle three. The playbook. Exactly where to put your one hundred dollars, in order.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
sc("""Here's the practical part. If you have one hundred dollars a month to invest, where should it go first? Many
financial planners suggest a similar order. It's not the only approach, but it's a solid starting point for most people.""",
   "Step by step stairs", "THE ORDER")

item(15, "Step 1: A small emergency fund", "protect the plan",
"""Step one. Build a small emergency fund first.""", [
("""Before investing, many planners suggest saving at least a starter emergency fund, often around one thousand dollars,
in a high yield savings account. This keeps surprises from landing on a credit card.""", "Emergency fund jar", "$1,000 FIRST"),
("""If you invest without a cushion, a car repair could force you to sell investments, possibly at a loss. Or worse, it
could land on a credit card at over twenty percent interest, wiping out years of investment gains in a few months. The
emergency fund protects the investing plan.""", "Car repair bill", "AVOID FORCED SALES"),
("""High yield savings accounts insured by the FDIC have offered much better rates than traditional savings accounts
in recent years. Your emergency money stays safe and easy to reach, and it still earns something while it waits. Over
time, many planners suggest growing it to three to six months of essential expenses.""", "Online savings account", "FDIC INSURED"),
("""Try this. Send your first months of one hundred dollars to a separate savings account until you hit one thousand.""", "Savings app progress", "THEN INVEST"),
])

item(16, "Step 2: Pay off high interest debt", "a guaranteed return",
"""Step two. Pay off high interest debt.""", [
("""If you carry credit card debt at twenty percent or more, paying it off is like earning a guaranteed twenty percent
return. That beats the long run average of the stock market.""", "Credit card statement", "A GUARANTEED RETURN"),
("""One hundred dollars a month extra toward a card balance can shorten payoff by years and save hundreds or thousands
in interest. And unlike the stock market, that return is certain. Every dollar of high interest debt you pay off is a
dollar that stops working against you.""", "Debt payoff chart", "YEARS FASTER"),
("""Once the debt is gone, redirect the same one hundred dollars, plus the old minimum payment, into investing.""", "Arrows redirecting money", "REDIRECT IT"),
("""Try this. List debts by interest rate. Attack the highest rate first.""", "List of debts", "HIGHEST RATE FIRST"),
])

body_hook = "If your job offers this, you're leaving free money on the table."
item(17, "Step 3: Get the employer match", "free money first",
"""Step three. Get your full employer match.""", [
("""If your employer matches part of your retirement contributions, that's an instant return. A fifty percent match
turns one hundred dollars into one hundred fifty, before any market growth.""", "Office benefits meeting", "$100 BECOMES $150"),
("""With a match, one hundred dollars a month could grow much faster than our example, because the employer is adding
money too. With a fifty percent match, the same twenty years at seven percent could produce roughly seventy eight thousand
dollars instead of fifty two thousand, and you'd still have contributed only twenty four thousand of your own money.""", "Retirement statement with match", "FASTER GROWTH"),
("""Check your plan's vesting schedule, which determines when the matched money fully belongs to you. Some employers
vest immediately, while others require a few years of service. Knowing the schedule helps you make smarter decisions if
you're thinking about changing jobs.""", "Plan documents", "CHECK VESTING"),
("""Try this. Find out your match formula and contribute at least enough to get all of it.""", "HR benefits portal", "GET THE FULL MATCH"),
])

item(18, "Step 4: A Roth IRA", "tax free growth",
"""Step four. Consider a Roth IRA.""", [
("""After the match, many people open a Roth IRA, if they're eligible based on income. You can invest small amounts, and
qualified withdrawals in retirement are tax free.""", "Roth IRA account opening", "TAX FREE LATER"),
("""Many brokerages let you open an IRA with no minimum and buy fractional shares of index funds, so one hundred dollars
a month works perfectly. You can set up a recurring transfer and a recurring investment in a few minutes, and from then on
it runs on its own.""", "Brokerage app fractional shares", "NO MINIMUMS"),
("""Roth contributions, but not earnings, can generally be withdrawn without penalty, which gives some flexibility. Rules
are detailed, so check IRS guidance.""", "IRS website on laptop", "KNOW THE RULES"),
("""Try this. Compare a few low cost brokerages and open a Roth IRA if you qualify.""", "Comparing brokerages", "OPEN ONE")
])

item(19, "Step 5: Keep it simple", "broad, low cost funds",
"""Step five. Choose simple, low cost, diversified investments.""", [
("""For many people, a broad stock market index fund or a target date fund is a simple choice. A target date fund
automatically adjusts the mix of stocks and bonds as you approach retirement.""", "Target date fund brochure", "SIMPLE CHOICES"),
("""Avoid chasing hot stocks or trends with your core money. Simple, diversified and low cost tends to win over long
periods. If you want to experiment with individual stocks for fun or learning, many people limit it to a small share of
their investments, money they can afford to lose, while the core stays in broad funds.""", "Hot stock headline", "SKIP THE HYPE"),
("""Check the expense ratio before you buy. Lower is usually better.""", "Expense ratio on screen", "LOW COST"),
("""Try this. Pick one broad, low cost fund and stick with it. Simplicity helps you stay consistent.""", "Single fund on app", "PICK ONE"),
])

item(20, "Step 6: Automate and increase", "set it and grow it",
"""Step six. Automate, then increase.""", [
("""Set your one hundred dollars to invest automatically every month. Then increase it whenever you can, especially
after raises or when debts are paid off.""", "Automatic investing setup", "AUTOMATE"),
("""Many workplace plans offer automatic yearly increases. Turning that on can raise your savings without any effort.""", "Auto increase setting", "AUTO INCREASE"),
("""Over time, one hundred dollars can become two hundred, then five hundred. The habit you build with one hundred dollars
is what makes that possible. Most people who invest large amounts today didn't start large. They started with an amount
that felt manageable, and kept nudging it upward year after year.""", "Graph rising contributions", "$100 TO $500"),
("""Try this. Set your automatic investment today, and set a reminder to raise it in six months.""", "Phone reminder six months", "START TODAY"),
])

# ---------------- Find it ----------------
ch("Where to find one hundred dollars a month")
pr("""Now, you might be thinking, I don't have an extra one hundred dollars. Let's find it. Here are ten common places it
hides in a typical budget.""")
sc("""One. Subscriptions you don't use. Many households have two or three forgotten ones, easily twenty to forty dollars a
month. Two. Bank fees. Switching to a no fee account can save monthly maintenance and overdraft charges. Three. Your phone
plan. Many people pay for far more data than they use, and switching to a cheaper plan or carrier can save twenty dollars
or more a month.""",
   "Subscriptions on phone screen", "PLACES 1 TO 3")
sc("""Four. Insurance. Shopping your car and home insurance once a year can lower your premium. Five. Takeout and
delivery. Replacing just two delivery meals a month with home cooking can free up forty or fifty dollars. Six. Grocery
waste. Planning meals and using what you buy can cut spending noticeably. Seven. Brand names. Switching ten regular items
to store brands can save real money with no real difference.""",
   "Home cooked meal on table", "PLACES 4 TO 7")
sc("""Eight. Your tax refund. If you get a big refund every year, adjusting your withholding can add money to every
paycheck, money you could invest monthly instead of waiting a year. Nine. Selling things you don't use. A one time sale
can fund several months of investing. And ten. Your next raise. Commit now to investing part of it before you ever get
used to spending it.""",
   "Selling items online", "PLACES 8 TO 10")
sc("""You don't need all ten. Most people can find one hundred dollars with just three or four of these. The important
thing is to move the money automatically as soon as you find it, so it doesn't quietly get absorbed into other spending.""",
   "Automatic transfer notification", "MOVE IT AS SOON AS YOU FIND IT")

# ---------------- By age ----------------
ch("One hundred dollars a month at every age")
sc("""Here's what one hundred dollars a month, at a seven percent average yearly return, could become by age sixty five,
depending on when you start. Start at twenty, and it could be roughly three hundred eighty thousand dollars. Start at
thirty, roughly one hundred eighty thousand. Start at forty, roughly eighty one thousand. Start at fifty, roughly thirty
two thousand.""",
   "Ages timeline chart", "START AT 20, 30, 40 OR 50")
sc("""Look at the gap between twenty and thirty. Ten years of one hundred dollars, just twelve thousand dollars of
contributions, makes a difference of about two hundred thousand dollars by sixty five. That's the price of waiting a
decade. It's the most expensive decision many people never realize they made.""",
   "Two people different ages", "THE COST OF WAITING")
sc("""If you're older, don't be discouraged. The lesson is the same. Start now, and invest more than one hundred dollars if
you can, because you have fewer years for compounding. Many people in their forties and fifties are in their highest
earning years, and catch up contribution rules for people fifty and older allow them to put more into retirement
accounts.""",
   "Older professional at desk", "IF YOU'RE STARTING LATER")

# ---------------- Mistakes ----------------
ch("Five mistakes with small investments")
sc("""Mistake one. Stopping during a market drop. That's when your one hundred dollars buys the most shares. Mistake two.
Picking expensive funds. A high fee on a small balance still compounds against you for decades. Mistake three. Cashing
out early. Withdrawing from retirement accounts early can mean taxes and penalties, and it resets the compounding clock.""",
   "Person withdrawing money", "MISTAKES 1 TO 3")
sc("""Mistake four. Chasing hot tips with your monthly money. Small amounts are easy to gamble with, and that's exactly
why it's tempting. Keep your core plan boring. Mistake five. Never increasing the amount. One hundred dollars is a
wonderful start, but the people who end up with the most are the ones who raise it whenever they can.""",
   "Hot tip headline on phone", "MISTAKES 4 AND 5")

# ---------------- What it can do ----------------
ch("What fifty two thousand dollars can do")
sc("""So what can roughly fifty two thousand dollars actually do for you in twenty years? Option one. It can be the
backbone of your safety net. With that much invested, a job loss or a medical bill becomes a setback, not a crisis. That
kind of security changes how you negotiate at work, how you sleep at night, and how much risk you can take with your
career.""",
   "Calm person at home", "A SAFETY NET")
sc("""Option two. It can keep growing. If you stop contributing at year twenty and simply leave the fifty two thousand
invested at the same seven percent average return, it could roughly double again in about ten years, by the rule of
seventy two. Your one hundred dollars a month keeps working long after you stop paying in.""",
   "Plant continuing to grow", "IT KEEPS GROWING")
sc("""Option three. It can produce income. Using the four percent guideline many retirement planners mention, fifty two
thousand dollars could support roughly two thousand dollars of withdrawals a year. That's not a full income, but it's a
meaningful supplement, and it came from money most people never noticed spending.""",
   "Retired couple on porch", "A LITTLE INCOME")
sc("""And option four, the most important one. It can prove to you that this works. Once you've watched one hundred dollars
a month turn into tens of thousands, you'll never look at small money the same way again. That belief is often worth more
than the money itself.""",
   "Person smiling at phone balance", "PROOF IT WORKS")

# ---------------- Story ----------------
ch("Three people, one hundred dollars")
pr("""Let me show you how this plays out with three people.""")
short("Waiting ten years can cut your result in half.")
sc("""Alex starts investing one hundred dollars a month at twenty five and never increases it. At sixty five, at a seven
percent average yearly return, that could grow to roughly two hundred sixty thousand dollars. Not bad for money that
felt too small to matter.""",
   "Young adult with laptop", "ALEX: $100 FROM 25")
sc("""Jamie waits until thirty five to start, also with one hundred dollars a month. At sixty five, that could be
roughly one hundred twenty two thousand dollars. Waiting ten years cut the result by more than half.""",
   "Thirty something person thinking", "JAMIE: STARTS AT 35")
sc("""Morgan starts at twenty five with one hundred dollars a month, and increases the contribution a little every year.
By the end, Morgan could have far more than both of them. Same starting amount. The difference was starting early and
growing the habit.""",
   "Person celebrating milestone", "MORGAN: STARTS AND GROWS")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. Is one hundred dollars a month really worth it? Yes. It builds the habit, gets compounding started
and grows into a meaningful amount over decades. And it usually becomes more than one hundred dollars as your income grows.""",
   "Coins and question mark", "IS IT WORTH IT?")
sc("""Question two. What if I can only invest fifty dollars? Start with fifty. Many brokerages allow small amounts and
fractional shares. The habit matters more than the amount.""",
   "Fifty dollar bill", "WHAT ABOUT $50?")
sc("""Question three. What if the market crashes right after I start? Then you're buying at lower prices. For a twenty year
plan, early drops can actually help, as long as you keep investing.""",
   "Market crash headline", "WHAT IF IT CRASHES?")
sc("""Question four. Should I invest or pay off my student loans? It depends on the interest rate. High interest debt
usually comes first. For low interest debt, many people do both, especially to get an employer match.""",
   "Student loan statement", "LOANS OR INVEST?")
sc("""Question five. Should I invest my one hundred dollars all at once each year, or monthly? Research on lump sum
versus monthly investing suggests that investing sooner has historically done better more often, because markets have
tended to rise over time. But for most people, money arrives monthly with each paycheck, so investing monthly is the
natural and practical choice. The important thing is that it happens consistently.""",
   "Calendar months and coins", "MONTHLY OR YEARLY?")
sc("""Question six. Can I lose all my money? With a single stock, yes, a company can fail. With a broad index fund holding
hundreds or thousands of companies, losing everything would require nearly the entire market to collapse permanently.
Values can still drop sharply for a time, which is why money you need soon shouldn't be in stocks.""",
   "Diversified basket of eggs", "CAN I LOSE IT ALL?")

# ---------------- Recap ----------------
ch("Recap")
sc("""Quick recap. Angle one, the numbers. Time is the main ingredient, the rate changes everything, fees eat growth,
inflation shrinks the number, the right account matters, raising the amount changes everything, and bad years are part
of it.""",
   "Checklist on clipboard", "THE NUMBERS: 1 TO 7")
sc("""Angle two, the psychology. It feels too small, there's no perfect time, present bias, checking too often, comparing,
fear of losing, and fading motivation.""",
   "Person thinking at window", "THE PSYCHOLOGY: 8 TO 14")
sc("""Angle three, the playbook. Emergency fund, high interest debt, employer match, Roth IRA, simple low cost funds, and
automate and increase.""",
   "Notebook with plan", "THE PLAYBOOK: 15 TO 20")

# ---------------- Close ----------------
ch("What to do next")
pr("""One hundred dollars a month won't change your life this month. But in twenty years, it can change everything. Set it
up today. If you want the full plan, it's in my playbook, linked in the description. Tell me in the comments how many years
you have to invest. I'm Ryan Rover. See you in the next one.""")

save("video31", "What $100 a Month Becomes in 20 Years", [
    "Growth examples: monthly compounding at stated average yearly returns of 4%, 7% and 10% (illustrations, not promises)",
    "S&P Dow Jones Indices, S&P 500 total returns (2008 about -37%, 2022 about -18%); SPIVA scorecards on active vs index funds",
    "Aswath Damodaran, NYU Stern, historical returns on stocks, bonds and bills",
    "Federal Reserve, 2% longer-run inflation goal; US Bureau of Labor Statistics, CPI",
    "IRS, Roth IRA and 401(k) rules and limits",
    "Stango and Zinman (2009), exponential growth bias; Benartzi and Thaler (1995), myopic loss aversion",
    "J.P. Morgan Asset Management, Guide to Retirement (missing the best days)",
    "Madrian and Shea (2001), automatic enrollment",
], "what $100 a month becomes in 20 years, from 3 angles: numbers, psychology, playbook")
