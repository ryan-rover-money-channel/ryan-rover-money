import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

def item(n, title, sub, card_text, paras, label="WAY"):
    """paras: list of (text, query, caption)"""
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"{label} {n}")
    for t, q, c in paras:
        sc(t, q, c)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. You walk into a bank, or open its app, and everything is free. Free checking, a free
debit card, free online transfers. And yet banks are some of the most profitable businesses in the world.
So here's the question. If it's all free, where does the money come from? Today, we're going inside the
business of banking, and I'll show you exactly how banks make money, including the parts they don't
advertise.""")
short("Your bank makes money from your savings. Here's how.")
card("""Banks make money in two main ways. They earn a spread between what they pay you on deposits and what
they charge on loans. And they charge fees for services, some obvious, some quiet.""",
     {"type": "compare", "left": {"label": "The spread", "big": "Interest", "sub": "loans minus deposits"},
      "right": {"label": "The extras", "big": "Fees", "sub": "services, penalties, products"},
      "note": "The two engines of bank profit"})
sc("""None of this is secret, and banks provide real value. They keep your money safe, move it around the
world in seconds, and make it possible for millions of people to buy homes and start businesses. But
understanding how they profit tells you exactly where you might be overpaying, and where your money could
be working much harder for you instead of for the bank.""",
   "Bank building columns", "REAL VALUE, REAL PROFIT")
sc("""We'll look at it from three angles. First, the numbers: the eight main ways banks earn money from
customers like you. Second, the psychology: why we stay with banks that pay us little and charge us a lot.
And third, the playbook: ten moves to make sure your bank works for you.""",
   "Bank vault door open", "THREE ANGLES")
pr("""By the end, you might want to look at your savings account rate. Many people are shocked by it. Let's
start with the numbers.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Every number here comes from a named source. Industry data comes from the Federal Deposit Insurance
Corporation, the FDIC, which publishes reports on bank earnings and national average deposit rates.
Overdraft data comes from the Consumer Financial Protection Bureau. Rules on debit card fees come from the
Federal Reserve. Interest rates change often, so treat any rate as a snapshot. This is education, not
financial advice.""",
   "FDIC sign building", "OUR SOURCES")

# ---------------- History ----------------
ch("A short history of banking")
pr("""Before the numbers, a quick bit of history. Because the way banks make money today is surprisingly
old.""")
sc("""Banking as we know it took shape centuries ago. In Renaissance Italy, families like the Medici of
Florence built banking empires by taking deposits, lending money and moving funds between cities with
letters of credit. Goldsmiths in seventeenth century London discovered something important. People left
gold with them for safekeeping, and only a fraction of it was ever withdrawn at once. So they could lend
out the rest.""",
   "Renaissance Florence painting", "THE MEDICI BANK")
sc("""That discovery is the heart of modern banking. Keep a portion of deposits available, lend or invest the
rest, and earn the difference. It works beautifully, as long as everyone doesn't ask for their money back
at the same time. When they do, it's called a bank run, and history is full of them.""",
   "Old goldsmith workshop", "LEND THE REST")
sc("""During the Great Depression, thousands of American banks failed, and many families lost their savings.
In response, Congress created the Federal Deposit Insurance Corporation in nineteen thirty three. Since
then, depositors at insured banks have been protected up to a limit, which today is two hundred fifty
thousand dollars. The FDIC says no depositor has lost a penny of insured funds since it began.""",
   "Great Depression bank run crowd", "1933: THE FDIC")
sc("""Banking has changed enormously since then, with ATMs, online banking and apps. But the basic model
hasn't. Take deposits, pay depositors less than you earn on loans and investments, and charge fees for
services. Understanding that old model is the key to making the modern one work for you.""",
   "Modern bank app phone", "THE SAME OLD MODEL")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The eight main ways banks make money. Let's follow your dollar after you deposit it.""")

item(1, "The spread", "borrow low, lend high",
"""Way number one. The spread.""",
[("""When you deposit money, the bank doesn't keep it in a vault with your name on it. It lends much of it out,
as mortgages, car loans, business loans and credit cards, or invests it in things like government bonds.
The bank pays you a low rate on your deposit, and earns a higher rate on the loans and investments. The
difference is called the net interest margin.""",
  "Bank teller counter", "BORROW LOW, LEND HIGH"),
 ("""According to the FDIC, the average net interest margin for American banks has been around three percent in
recent years. That sounds small. But apply three percent to trillions of dollars of deposits and loans, and
it becomes the largest source of profit in the banking industry.""",
  "Stacks of money vault", "AROUND 3%"),
 ("""Here's a simple way to picture it. You deposit ten thousand dollars and earn almost nothing. The bank
lends that money for a car loan at eight percent. That's about eight hundred dollars a year on your
money. Even after costs, losses and the interest they pay you, there's usually plenty left. That's the
core of the business.""",
  "Car loan contract", "YOUR $10,000 AT WORK")])

item(2, "Paying you almost nothing", "the national average rate",
"""Way number two. Paying depositors very little.""",
[("""The FDIC publishes a national average rate for savings accounts. In recent years, even when interest rates
in the economy were relatively high, that average stayed well under one percent. At the same time, many
online banks and credit unions were paying several percent on high yield savings accounts, sometimes
around four percent or more at various points.""",
  "Savings account app low rate", "UNDER 1% VS SEVERAL %"),
 ("""Why the gap? Many big banks don't need to compete hard for your deposits. They have huge customer bases,
lots of branches, and customers who rarely move their money. So they can pay less. Online banks, without
the cost of branches, often pay more to attract customers.""",
  "Big bank branch downtown", "WHY THE GAP?"),
 ("""Look at what that gap means in dollars. Twenty thousand dollars in an account paying a fraction of one
percent might earn under one hundred dollars in a year. The same amount at four percent would earn about
eight hundred dollars. Same safety, if both are FDIC insured. Seven hundred dollars of difference, just
for the choice of where your savings sit.""",
  "Calculator with savings", "$700 A YEAR DIFFERENCE")])
card("""Twenty thousand dollars in savings for one year. At a typical big bank rate, a fraction of one percent.
At a four percent high yield account, about eight hundred dollars.""",
     {"type": "compare", "left": {"label": "Low rate savings", "big": "<$100", "sub": "a year on $20,000"},
      "right": {"label": "4% high yield", "big": "~$800", "sub": "a year on $20,000"},
      "note": "Illustration. Rates change often."})

item(3, "Loans of every kind", "mortgages, cars, cards",
"""Way number three. Lending.""",
[("""Lending is where the spread is earned. Mortgages, home equity lines, auto loans, personal loans, business
loans and credit cards. Each carries a different rate depending on the risk. A mortgage backed by a house
might carry a lower rate. A credit card with nothing behind it carries a much higher one, often above twenty
percent.""",
  "House mortgage signing", "EVERY KIND OF LOAN"),
 ("""Banks also earn fees when they create loans. Origination fees, closing costs, application fees. And they
can sell many mortgages to other investors, collect a fee for servicing them, and use the money to lend
again. A single home loan can generate income in several different ways over its life.""",
  "Loan documents stack", "FEES ON TOP OF INTEREST"),
 ("""For you, the key is that loan pricing depends heavily on your credit score and your shopping. Two people
with similar finances can get very different rates, simply because one compared offers and the other
accepted the first one. On a mortgage, even a small rate difference can add up to thousands of dollars
over the years.""",
  "Comparing offers on laptop", "SHOP YOUR RATE")])

item(4, "Overdraft fees", "billions from small mistakes",
"""Way number four. Overdraft and insufficient funds fees.""",
[("""An overdraft happens when you spend more than you have in your checking account, and the bank covers the
difference, for a fee. For years, a typical fee was around thirty dollars or more, even if the purchase was
a small coffee. The Consumer Financial Protection Bureau found that banks once collected well over ten
billion dollars a year from these fees.""",
  "Bank overdraft notice", "A $35 COFFEE"),
 ("""The good news: under pressure from regulators and competition, many banks have cut or eliminated these
fees in recent years. The CFPB reported that overdraft and insufficient funds revenue fell to around six
billion dollars in twenty twenty three, roughly half of what it had been before the pandemic. Still, six
billion dollars is a lot of money, and it often comes from customers with the smallest balances.""",
  "Chart falling bars", "STILL BILLIONS"),
 ("""Overdraft protection is often presented as a service. And sometimes it is useful. But you can usually opt
out of overdraft coverage for debit card purchases and ATM withdrawals, so a transaction is simply declined
instead of costing you a fee. Try this: check your overdraft settings in your banking app today, and
consider linking a savings account as a backup instead.""",
  "Phone banking settings", "CHECK YOUR SETTINGS")])
card("""According to the Consumer Financial Protection Bureau, banks collected around six billion dollars in
overdraft and insufficient funds fees in twenty twenty three, down from more than twelve billion before
the pandemic.""",
     {"type": "compare", "left": {"label": "2019", "big": "$12B+", "sub": "overdraft and NSF fees"},
      "right": {"label": "2023", "big": "~$6B", "sub": "overdraft and NSF fees"},
      "note": "Source: Consumer Financial Protection Bureau"})

item(5, "Account fees", "the price of free",
"""Way number five. Monthly and service fees.""",
[("""Free checking often comes with conditions. Keep a minimum balance, set up direct deposit, or make a number of
debit purchases each month. Miss the condition, and a monthly maintenance fee appears, often somewhere
around five to fifteen dollars. Twelve dollars a month is one hundred forty four dollars a year, for an
account that may pay you almost nothing in interest.""",
  "Bank statement monthly fee", "THE PRICE OF FREE"),
 ("""Then there are service fees. Wire transfers, which can cost twenty five dollars or more. Out of network
ATM fees, sometimes charged twice, once by your bank and once by the ATM owner. Paper statement fees,
foreign transaction fees on debit cards, and fees for cashier's checks or stop payments.""",
  "ATM machine fee screen", "SERVICE FEES ADD UP"),
 ("""Each fee is small. But fees are almost pure profit for a bank, because the service often costs very
little to provide. Try this: download your last three statements and search for the word fee. Add up
everything you find. Then ask your bank to waive them, or switch to a bank that doesn't charge them.""",
  "Search on bank statement", "SEARCH FOR THE WORD FEE")])

item(6, "Your debit card swipes", "fees from merchants",
"""Way number six. Your debit card swipes.""",
[("""Every time you use your debit card, the merchant pays a fee, and part of it goes to your bank. Since the
Durbin amendment, part of the Dodd Frank law in twenty ten, the Federal Reserve has capped these fees for
large banks at about twenty one cents plus a small percentage per transaction. Smaller banks and credit
unions are exempt from the cap.""",
  "Debit card terminal", "A FEW CENTS PER SWIPE"),
 ("""A few cents per swipe doesn't sound like much. But Americans make tens of billions of debit card payments
every year. That adds up to billions of dollars in revenue. This is one reason banks encourage you to use
your debit card instead of cash, and why some accounts require a certain number of card purchases to avoid
fees.""",
  "Crowded store checkout", "BILLIONS OF SWIPES"),
 ("""Should you avoid your debit card because of this? Not necessarily. The fee is paid by the merchant, not
you. But it's worth knowing that for everyday purchases, a credit card paid in full each month often gives
you more protection and rewards, while the debit card mainly benefits the bank. Use whichever keeps you
in control of your spending.""",
  "Wallet debit and credit cards", "WHICH CARD TO USE")])

item(7, "Selling you more products", "the cross sell",
"""Way number seven. Selling you more products.""",
[("""Once you're a customer, banks want to sell you more. A credit card, a mortgage, an investment account,
insurance, a personal loan. Inside the industry, this is called cross selling, and it's a big focus,
because a customer with five products is more profitable and less likely to leave than a customer with
one.""",
  "Bank advisor meeting", "THE CROSS SELL"),
 ("""Cross selling isn't bad on its own. But it can go very wrong. In twenty sixteen, regulators fined Wells
Fargo after it was revealed that employees, under heavy sales pressure, had opened millions of accounts
without customers' permission. The bank paid large penalties and settlements. It became one of the most
famous banking scandals of the decade.""",
  "Bank scandal newspaper", "WHEN SALES GOALS GO WRONG"),
 ("""The investment and advice side can also be expensive. Some bank investment products come with higher fees
than similar low cost options elsewhere. Try this: when your bank offers a new product, ask three
questions. What does it cost per year in dollars? How is the person recommending it paid? And can I get the
same thing cheaper somewhere else?""",
  "Investment brochure fees", "ASK THREE QUESTIONS")])

item(8, "Float and timing", "money in motion",
"""Way number eight. Float.""",
[("""When money moves between accounts or banks, there can be a delay. Deposits sometimes take a day or two to
become available, and some transfers take days. During that time, the money is sitting somewhere, and banks
can benefit from holding it. This is sometimes called float.""",
  "Money transfer arrows", "MONEY IN MOTION"),
 ("""Faster payment systems are shrinking float, which is good for customers. The Federal Reserve launched an
instant payment service called FedNow in twenty twenty three, and many banks now offer real time
transfers. But holds on deposits still exist, often for good reasons like fraud prevention. Knowing how
long your bank holds deposits helps you avoid bounced payments.""",
  "Instant payment phone", "FASTER PAYMENTS"),
 ("""Try this: check your bank's funds availability policy. It's usually on their website. If your paycheck
lands on Friday but isn't available until Monday, schedule your bills accordingly, or ask about early
direct deposit, which some banks and credit unions offer.""",
  "Paycheck direct deposit", "KNOW YOUR HOLD TIMES")])
sc("""So that's how your dollar earns money for the bank. The spread on loans, the low rate on deposits, the
loans themselves, overdraft fees, account and service fees, debit card swipes, cross selling, and float.
Most of these are reasonable. A few are expensive. And almost all of them can be reduced if you know
where to look.""",
   "Bank building at night", "EIGHT ENGINES")
sc("""One more thing worth knowing about the spread. When interest rates in the economy rise, banks often raise
the rates they charge on loans quickly, but raise the rates they pay on savings slowly. When rates fall,
the reverse often happens. Savings rates drop fast, and loan rates drift down more slowly. Economists call
this deposit rate stickiness. For savers, the lesson is simple. Don't wait for your bank to give you a
raise. Go where the rate already is.""",
   "Interest rate chart arrows", "STICKY RATES")
pr("""So if the numbers are this clear, why do so many people stay with a bank that pays them so little? That's
angle two.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
pr("""Angle two. The psychology. Six reasons we keep our money where it earns the least.""")
short("Why you're probably still with the wrong bank")

item(9, "Inertia", "the bank you opened at 18",
"""Reason number nine. Inertia.""",
[("""Many people still bank where their parents opened their first account, or where they signed up in
college. Switching feels like a hassle. Moving direct deposits, updating automatic payments, learning a new
app. Economists call the tendency to stick with the default status quo bias. Banks know that once you're
in, you're unlikely to leave.""",
  "Teenager opening bank account", "THE FIRST BANK"),
 ("""And inertia is profitable. It's why banks can pay loyal customers less than new ones. Some banks even
offer better rates to new customers than to existing ones. Loyalty, in banking, is often rewarded with
lower interest.""",
  "Loyalty card concept", "LOYALTY PAYS LESS"),
 ("""Try this: you don't have to leave your bank. Keep your checking account where it is for convenience, and
open a high yield savings account elsewhere for your emergency fund and savings goals. Link them. It
takes about fifteen minutes and can earn you hundreds of dollars a year.""",
  "Two bank accounts linked", "KEEP CHECKING, MOVE SAVINGS")])

item(10, "Free feels good", "the zero price effect",
"""Reason number ten. Free feels good.""",
[("""Researchers have found that people react to a price of zero very differently from any other price. Free
checking, free transfers, free debit cards. It feels like a great deal. And it makes us less likely to
ask what we're giving up. In banking, free often means paid for in other ways, like low deposit rates or
fees when you slip.""",
  "Free sign in window", "THE ZERO PRICE EFFECT"),
 ("""Try this: look at your bank as a total cost. Add up fees paid, then subtract interest earned. If the number
is a cost to you, your free account isn't free. Compare it with what a high yield account and a no fee
checking account would give you.""",
  "Balance sheet simple", "TOTAL COST, NOT FREE"),
 ("""Free also shapes how we judge new options. A high yield account that pays four percent might ask you to
open a new login, wait a day for transfers, or link accounts. Those small hassles feel bigger than the
hundreds of dollars of interest you'd earn, because the hassle is immediate and the interest arrives
slowly. Recognize that bias, and do the fifteen minutes of setup anyway.""",
  "Laptop new account setup", "SMALL HASSLE, BIG REWARD")])

item(11, "Trust and fear", "big feels safe",
"""Reason number eleven. Big feels safe.""",
[("""Many people believe a big bank with a famous name is safer than a smaller or online bank. But for most
savers, the key protection is FDIC insurance. Deposits at insured banks are protected up to two hundred
fifty thousand dollars per depositor, per insured bank, for each account ownership category. Credit unions
have similar protection through the National Credit Union Administration.""",
  "FDIC insured sticker", "$250,000 PROTECTION"),
 ("""In March twenty twenty three, Silicon Valley Bank collapsed after customers rushed to withdraw their money,
in one of the fastest bank runs in history. Many of its customers had balances far above the insured limit.
The lesson for ordinary savers isn't that banks are unsafe. It's that the insurance limit matters, and that
you should know which bank is actually holding your money.""",
  "Bank closed sign", "WHY THE LIMIT MATTERS"),
 ("""Try this: confirm that any bank you use is FDIC insured, or any credit union is NCUA insured, using the
official government websites. And if you ever have more than the insured limit in one place, ask about
how to structure your accounts to stay protected.""",
  "Government website on laptop", "CONFIRM THE INSURANCE")])

item(12, "Convenience", "everything in one place",
"""Reason number twelve. Convenience.""",
[("""Having everything in one place feels simple. Checking, savings, credit card, mortgage, all in one app.
Banks encourage this with relationship discounts and bundled benefits. Sometimes the bundle is a good
deal. But often, convenience is the price you pay for not shopping around.""",
  "Banking app dashboard", "ALL IN ONE APP"),
 ("""The best rate on a savings account is rarely at the same place as the best mortgage rate, or the best credit
card for you. Splitting your banking across two or three institutions takes a little more effort, but
it can mean better rates on almost everything. Modern apps make linking accounts easy.""",
  "Multiple apps phone", "BEST IN EACH CATEGORY"),
 ("""A simple setup works for most people. One checking account for bills and spending, wherever is most
convenient. One high yield savings account for the emergency fund and goals. And one investment account,
at a low cost brokerage, for long term money. Three accounts, three jobs, each at the place that does
that job best.""",
  "Three folders organized desk", "THREE ACCOUNTS, THREE JOBS")])

item(13, "Complexity", "fine print fatigue",
"""Reason number thirteen. Complexity.""",
[("""Bank accounts come with long fee schedules, terms and conditions, and disclosures. Few people read them.
That's not because people are lazy. It's because the documents are long and confusing. And when something is
confusing, we stick with what we have. Complexity protects the status quo.""",
  "Long fine print document", "FINE PRINT FATIGUE"),
 ("""Try this: you only need to find five things in any account's terms. The interest rate. The monthly fee and
how to avoid it. The overdraft policy. The ATM fees. And the funds availability policy. Five numbers. Ten
minutes. That's all it takes to compare almost any two accounts.""",
  "Highlighter on document", "FIND FIVE NUMBERS"),
 ("""Banks are required to disclose fees and rates, and many publish simple summary sheets. Some even offer
a one page fee table. Ask for it, or search the bank's site for account disclosures. Once you have it,
the comparison takes minutes, and the complexity barrier disappears.""",
  "One page summary document", "ASK FOR THE SUMMARY")])

item(14, "Not seeing the cost", "the invisible opportunity",
"""Reason number fourteen. You never see what you didn't earn.""",
[("""Fees show up on your statement. But the interest you could have earned somewhere else never shows up
anywhere. There's no line that says you missed seven hundred dollars this year. Because the cost is
invisible, it doesn't feel real. Economists call it opportunity cost, and it's one of the hardest costs for
humans to notice.""",
  "Empty space on statement", "THE INVISIBLE COST"),
 ("""Try this: make it visible. Write down your savings balance and your current rate. Then calculate what you'd
earn at a competitive high yield rate. The difference is your yearly loyalty cost. Seeing that number is
often enough to make the switch.""",
  "Writing numbers notebook", "YOUR LOYALTY COST"),
 ("""Do the same for loans. If you have a car loan or credit card at your main bank, check what other
lenders would offer you today. If your credit has improved, a refinance or a balance transfer might lower
your rate. Your bank won't call you to suggest it. Their best outcome is that you never ask.""",
  "Refinance offer letter", "CHECK YOUR LOANS TOO")])

# ---------------- Follow one dollar ----------------
ch("Follow one paycheck")
sc("""Let's follow one paycheck through the system. Your employer sends three thousand dollars by direct deposit.
Within seconds, it's in your checking account, earning little or nothing. Your bank now has three thousand
more dollars of deposits it can use to fund loans and investments.""",
   "Direct deposit notification", "THE PAYCHECK ARRIVES")
sc("""Over the next two weeks, you pay rent, buy groceries with your debit card and pay a few bills. Each debit
purchase sends a few cents to the bank. If your balance dips too low on the wrong day, a fee might
appear. Meanwhile, the money you haven't spent yet is helping the bank earn interest elsewhere.""",
   "Grocery debit card payment", "THE MONEY MOVES")
sc("""Now imagine you also carry a credit card balance at the same bank, and you have a car loan there. The bank
is earning on your deposits, on your card balance at over twenty percent, on your car loan, and on your
swipes. You might be one of its most profitable customers, while earning almost nothing on your own money.""",
   "Bank customer profile illustration", "A VERY PROFITABLE CUSTOMER")
sc("""Flip that picture. Savings in a high yield account, earning a competitive rate. Credit card paid in full
every month. Car loan from the cheapest lender you could find. Debit or credit card used thoughtfully.
Now the bank still makes some money from you, which is fair, but much more of the value flows back to you.
That's the goal.""",
   "Balanced scale coins", "FLIP THE PICTURE")

# ---------------- Mid ----------------
ch("A quick favor")
pr("""Quick pause. If you're about to go check your savings rate, good. Do it. And if this video is helping,
subscribe to the channel. It's free, and it helps me keep making these videos for you. Now, the playbook.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
pr("""Angle three. Ten moves to make your bank work for you, not the other way around.""")
short("10 moves to make your bank work for you")
sc("""Move one. Move your savings to a high yield account. Keep checking wherever is convenient, but put your
emergency fund and savings goals somewhere that pays a competitive rate, and make sure it's FDIC or NCUA
insured. This single move often earns people hundreds of dollars a year for fifteen minutes of work.""",
   "High yield savings app", "MOVE 1: HIGH YIELD SAVINGS")
sc("""Move two. Turn off overdraft coverage for debit card purchases if you don't need it, or link a savings
account as a backup. Move three. Avoid monthly fees. Meet the conditions, ask for a fee waiver, or switch to
a no fee account. Many online banks and credit unions charge no monthly fees at all.""",
   "Settings toggles phone", "MOVES 2 AND 3")
sc("""Move four. Use in network ATMs, or choose a bank that reimburses ATM fees. Move five. Set up alerts. Low
balance alerts, large transaction alerts and deposit alerts. They're free, and they prevent most overdrafts
and catch fraud quickly.""",
   "Phone notification alert", "MOVES 4 AND 5")
sc("""Move six. Shop every loan. Before a mortgage, car loan or personal loan, get quotes from at least three
lenders, including a credit union. Compare the APR, not just the monthly payment. On big loans, a small
rate difference can mean thousands of dollars.""",
   "Credit union sign", "MOVE 6: SHOP EVERY LOAN")
sc("""Move seven. Say no to products you don't understand. If the person recommending a product can't explain
its costs clearly, that's your answer. Move eight. Keep your investments low cost. Compare any bank
investment product with low cost index funds at a brokerage, and look at the fees in dollars.""",
   "Person declining offer politely", "MOVES 7 AND 8")
sc("""Move nine. Review your bank once a year. Same day every year, check your rates, fees and accounts. Ask
your bank to match competitors. If they won't, move. And move ten. Use the bank's business model in your
favor. Take advantage of sign up bonuses when they make sense, pay credit cards in full, and keep your
money where it earns the most.""",
   "Calendar yearly review", "MOVES 9 AND 10")
card("""Moving twenty thousand dollars from a low rate account to a four percent account, and adding two hundred
dollars a month, for ten years. Here's roughly where it could grow.""",
     {"type": "growth", "start": 20000, "monthly": 200, "rate": 0.04, "years": 10})
sc("""That's an illustration, with rates that will change over time. But notice that this growth comes with
no stock market risk at all, just a better rate on safe money. Banks count on most people never making
this move. You can be the exception.""",
   "Person smiling at phone", "SAFE MONEY, BETTER RATE")

# ---------------- Stories ----------------
ch("Two savers")
short("Same savings, one moved banks. Here's the difference.")
sc("""Let's compare two savers. Patricia has thirty thousand dollars in savings at the big bank she's used
for twenty years. The rate is a fraction of one percent. She pays a twelve dollar monthly fee on her
checking because her balance sometimes dips below the minimum, and she's been charged two overdraft fees
this year.""",
   "Woman at big bank branch", "PATRICIA: TWENTY YEARS")
sc("""In a year, Patricia earns maybe one hundred dollars in interest and pays about two hundred twenty dollars in
fees. Her bank relationship costs her money. She doesn't notice, because the fees are small and the missing
interest is invisible.""",
   "Bank statement fees highlighted", "A COST SHE DOESN'T SEE")
sc("""Kevin has the same thirty thousand. His checking account is at a credit union with no monthly fee, and
his savings are in an FDIC insured high yield account paying around four percent. He turned off overdraft
coverage and set low balance alerts. He spent one afternoon setting it up.""",
   "Man with laptop setting accounts", "KEVIN: ONE AFTERNOON")
sc("""In a year, Kevin earns roughly twelve hundred dollars in interest and pays nothing in fees. The gap between
Patricia and Kevin is more than thirteen hundred dollars a year, with exactly the same amount of money and
exactly the same level of safety. Over ten years, that's well over thirteen thousand dollars, before
counting any interest on the difference.""",
   "Two paths split", "$1,300 A YEAR DIFFERENCE")
card("""Same thirty thousand dollars. Same safety. Very different results in a single year.""",
     {"type": "compare", "left": {"label": "Patricia", "big": "-$120", "sub": "interest minus fees"},
      "right": {"label": "Kevin", "big": "+$1,200", "sub": "interest, no fees"},
      "note": "Illustration. Rates and fees vary."})

# ---------------- Fair view ----------------
ch("What banks do well")
sc("""To be fair, let's talk about what banks do well, because this isn't a story about villains. Banks make it
possible to get paid electronically, pay bills in seconds, and keep money safe from theft and fire. They
fund mortgages that let families own homes, and loans that help businesses grow and hire. Without banks,
modern economic life would barely function.""",
   "Small business owner shop", "WHAT BANKS DO WELL")
sc("""Banks also carry real risks and costs. Some loans aren't repaid. Fraud costs them billions. Regulation
requires them to hold capital, follow strict rules and run expensive compliance programs. Branches, staff and
technology all cost money. Profit is how they cover those costs and pay their shareholders.""",
   "Bank security guard", "REAL COSTS, REAL RISKS")
sc("""So the goal isn't to hate your bank. It's to be an informed customer. Use the services that give you real
value, avoid the products and fees that don't, and make sure your own money earns a fair return. Banks
respond to customers who shop around. That's how competition works.""",
   "Customer shaking hands with banker", "AN INFORMED CUSTOMER")

# ---------------- Apps ----------------
ch("What about banking apps?")
sc("""In recent years, many financial apps have appeared that look like banks, but aren't. Some are technology
companies that partner with a licensed bank behind the scenes. They can offer great features, like
early paydays, budgeting tools and higher savings rates. But it's important to know who actually holds
your money.""",
   "Fintech app on phone", "APPS THAT LOOK LIKE BANKS")
sc("""In twenty twenty four, a company called Synapse, which connected several popular apps to partner banks, went
bankrupt. Many customers of those apps found their money frozen for months, and some reported missing
funds. The lesson isn't to avoid apps. It's to read the fine print. Check which bank holds your deposits,
whether it's FDIC insured, and whether your balance is held in your name.""",
   "Frozen account message screen", "KNOW WHO HOLDS YOUR MONEY")

ch("What to say when you call your bank")
pr("""Here's a short script you can use when you call your bank. It works more often than people think.""")
sc("""Start friendly. Hi, I've been a customer for a long time, and I'm reviewing my accounts. Then be specific.
I've been charged a monthly fee and an overdraft fee this year. Could you waive them? Many banks have the
power to refund fees, especially for long time customers, and they'd rather keep you happy than lose
you.""",
   "Person calling bank smiling", "ASK FOR A WAIVER")
sc("""Then ask about rates. My savings account pays much less than insured online banks. Do you have a better
savings option for me? If they offer something, compare it. If they don't, thank them and move your
savings. And on loans, ask whether you qualify for a lower rate given your payment history.""",
   "Notes during phone call", "ASK FOR A BETTER RATE")
sc("""Stay polite, keep it short, and don't be afraid of a no. The worst outcome is that nothing changes, and you
move your money anyway. The best outcome is that a ten minute call saves you hundreds of dollars a year.""",
   "Phone call ending happy", "TEN MINUTES, REAL MONEY")

# ---------------- Red flags ----------------
ch("Five red flags in your bank account")
sc("""Before the questions, five red flags that your bank account is costing you too much. One. Your savings
rate is a tiny fraction of what insured online banks are paying. Two. You've paid a monthly maintenance fee
in the last three months. Three. You've paid an overdraft or insufficient funds fee this year.""",
   "Red flag warning", "RED FLAGS 1 TO 3")
sc("""Four. You regularly pay out of network ATM fees. And five. You've bought an investment or insurance product
from your bank without comparing it elsewhere. If you see two or more of these, block out one afternoon and
run the playbook. It's one of the highest paying afternoons you'll ever spend.""",
   "Afternoon desk work", "RED FLAGS 4 AND 5")

# ---------------- FAQ ----------------
ch("Questions people ask")
pr("""Let me answer the questions people ask me most about banks.""")
sc("""Question one. Are online banks safe? If they're FDIC insured, deposits are protected up to the limits,
just like at a big bank. Check the FDIC's official BankFind tool. Some apps are not banks themselves but
partner with banks, so make sure you understand which bank actually holds your money and whether it's
insured.""",
   "FDIC BankFind website", "ARE ONLINE BANKS SAFE?")
sc("""Question two. Is a credit union better than a bank? Credit unions are member owned nonprofits, and they
often offer lower fees and better loan rates, especially on auto loans. Banks may offer more branches and
technology. Many people use both. A credit union for loans and checking, and an online bank for high yield
savings.""",
   "Credit union branch building", "CREDIT UNION OR BANK?")
sc("""Question three. Should I keep money in a CD? A certificate of deposit locks your money for a set time at a
fixed rate. It can make sense for money you won't need until a specific date, especially if rates are
expected to fall. But early withdrawals usually come with a penalty, so don't put your emergency fund in
one.""",
   "Certificate of deposit document", "WHAT ABOUT CDs?")
sc("""Question four. How do I switch banks without chaos? Open the new account first. Move your direct deposit.
Then move automatic payments one by one over a month or two. Keep the old account open, with a small
balance, until you're sure everything has moved. Then close it. It's a project, not a crisis.""",
   "Checklist moving accounts", "HOW TO SWITCH")
sc("""Question five. Do banks really lend out my money? Yes. That's the business. Banks hold some cash and
reserves, and lend or invest much of the rest. This system is why deposit insurance and regulation exist,
to protect depositors if a bank fails.""",
   "Bank lending illustration", "DO THEY LEND MY MONEY?")
sc("""Question seven. Is it worth chasing bank sign up bonuses? Sometimes. Some banks pay a few hundred dollars
for opening an account and setting up direct deposit. If the requirements are easy and there are no fees,
it can be worth it. But read the conditions carefully, and don't open so many accounts that you lose
track.""",
   "Bonus offer card", "SIGN UP BONUSES?")
sc("""And question six. What's the one thing I should do today? Look up the interest rate on your savings
account. Then look up the rate on a few FDIC insured high yield accounts. If the difference is large, you've
just found free money waiting to be collected.""",
   "Person checking phone rate", "THE ONE THING TODAY")

# ---------------- Recap ----------------
ch("Recap")
short("How banks really make money")
sc("""Quick recap. Banks make money from the spread, paying you little and lending at more, from all kinds of
loans, from overdraft fees, from monthly and service fees, from debit card swipes, from selling you more
products, and from float.""",
   "Checklist clipboard", "THE EIGHT WAYS")
sc("""We stay because of inertia, the appeal of free, the feeling that big is safe, convenience, complexity, and
the invisible cost of interest we never earned.""",
   "Brain thinking illustration", "WHY WE STAY")
sc("""And the playbook: high yield savings, overdraft settings, no monthly fees, in network ATMs, alerts, shop
every loan, skip products you don't understand, keep investments low cost, review once a year, and use the
system in your favor.""",
   "Thumbs up phone bank", "THE PLAYBOOK")

# ---------------- Close ----------------
ch("What to do next")
pr("""If you want the full plan for making every dollar work harder, it's in my playbook. The link is in the
description. And watch my video on how credit card companies make money from you. It's the other half of
the banking business. I'm Ryan Rover. See you in the next one.""")

save("video47", "How Banks Really Make Money (And What They Don't Tell You)", [
    "FDIC, Quarterly Banking Profile (industry net interest margin around 3%)",
    "FDIC, National Rates and Rate Caps (national average savings rate)",
    "Consumer Financial Protection Bureau, overdraft and NSF fee revenue (about $5.8 billion in 2023, down from over $12 billion in 2019)",
    "Federal Reserve, Regulation II debit card interchange fee cap (Durbin amendment, Dodd-Frank Act)",
    "Federal Reserve, FedNow Service (launched 2023)",
    "FDIC deposit insurance ($250,000 per depositor, per insured bank, per ownership category); NCUA share insurance",
    "Wells Fargo unauthorized accounts enforcement actions (2016); Silicon Valley Bank failure (March 2023)",
    "Interest and growth figures: stated illustrative math",
], "how banks make money: numbers, psychology, playbook")
