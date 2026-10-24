import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

def item(n, title, sub, card_text, paras):
    """paras: list of (text, query, caption)"""
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"FEE {n}")
    for t, q, c in paras:
        sc(t, q, c)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Here's one of the most unfair truths in money. It's expensive to be poor. Not just hard.
Expensive. People with the least money often pay the most for the same things. More fees, higher interest,
higher prices, and even more time. Today, twenty hidden costs of being poor, and how to escape each one.""")
short("It's expensive to be poor. Here's the proof.")
card("""Being poor comes with a hidden price list. Fees, interest and higher prices that people with savings simply
never pay.""",
     {"type": "stat", "label": "the hidden price list", "big": "20 COSTS", "sub": "that people with savings never pay"})
sc("""This isn't about blame. Most of these costs aren't caused by bad choices. They're built into a system that
charges more to people with less cushion, lower credit scores or fewer options. But knowing exactly where those
costs are hiding is powerful. Many of them can be avoided or reduced, sometimes with one phone call or one
new account.""",
   "Receipts and coins on table", "NOT ABOUT BLAME")
sc("""We'll look at it from three angles. First, the numbers: the eight costs of banking and borrowing without a
cushion. Second, the psychology and time costs: how scarcity drains not just money, but time and mental energy.
And third, the playbook: the last five costs, and a step by step way to escape the poverty premium.""",
   "Three paths walking", "THREE ANGLES")
pr("""Some of these costs add up to thousands of dollars a year. Let's start with the numbers.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Every number here comes from a named source. Banking data comes from the FDIC's National Survey of Unbanked
and Underbanked Households. Payday and title loan data comes from the Consumer Financial Protection Bureau.
Rules on credit union small loans come from the National Credit Union Administration. Medical debt data comes
from the CFPB. Fees vary widely by company and state, so treat examples as typical, not exact. This is
education, not financial advice.""",
   "FDIC building", "OUR SOURCES")

# ---------------- History ----------------
ch("The company store")
sc("""The idea that the poor pay more isn't new. In the late eighteen hundreds and early nineteen hundreds, many coal
mining and logging towns in America ran company stores. Workers were sometimes paid in scrip, a currency that
could only be spent at the company's own store. Prices there were often higher than elsewhere, and workers could
fall into debt to their employer.""",
   "Historic coal mining town", "THE COMPANY STORE")
sc("""The song Sixteen Tons, made famous by Tennessee Ernie Ford in the nineteen fifties, captured the feeling with one
line: I owe my soul to the company store. Workers earned, spent at the store, owed the store, and worked to pay it
back. The cycle was hard to escape.""",
   "Vintage record player", "I OWE MY SOUL")
sc("""Today's version is less obvious, but the structure is similar. When you have no cushion and few options, you
often end up paying more to the businesses that serve people in exactly that situation. Fees, high interest and
higher prices. Understanding that structure is the first step to stepping outside it.""",
   "Modern storefront payday loans", "TODAY'S VERSION")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. Eight costs of banking and borrowing when you don't have a cushion.""")

item(1, "Overdraft fees", "a $35 sandwich",
"""Cost number one. Overdraft fees.""",
[("""When your balance is low, a single small purchase can trigger an overdraft fee, historically often around
thirty five dollars at many banks. Buy a six dollar sandwich with eight dollars too little in your account, and
the sandwich can effectively cost forty one dollars. Several small purchases on the same day can mean several
fees.""",
  "Sandwich and receipt", "A $41 SANDWICH"),
 ("""People with healthy balances rarely pay these fees. People living paycheck to paycheck can pay them again and
again. The CFPB has found that a relatively small share of customers, usually those with low balances, pay the
majority of overdraft fees.""",
  "Bank fee notice", "A SMALL GROUP PAYS MOST"),
 ("""Many banks have reduced or eliminated overdraft fees in recent years, which is real progress. Try this: check
whether your bank still charges them. If it does, turn off overdraft coverage for debit purchases, or move to an
account that doesn't charge overdraft fees at all.""",
  "Phone banking settings", "TURN IT OFF")])

item(2, "Check cashing fees", "paying to get paid",
"""Cost number two. Paying to cash your own paycheck.""",
[("""According to the FDIC, millions of American households don't have a bank account. They're called unbanked. In
the FDIC's twenty twenty three survey, about four percent of households were unbanked, roughly five and a half
million households. Many of them use check cashing stores to turn their paychecks into cash.""",
  "Check cashing store sign", "MILLIONS UNBANKED"),
 ("""Check cashing stores charge a fee, often a percentage of the check. Pay a few percent on every paycheck, and
over a year it can add up to hundreds of dollars, just to access money you already earned. Add money orders to
pay bills, and the cost of handling money grows further.""",
  "Money order counter", "HUNDREDS A YEAR TO GET PAID"),
 ("""Why do people stay unbanked? The FDIC survey found common reasons included not having enough money to meet
minimum balance requirements, not trusting banks, and high or unpredictable fees. Those are fair concerns,
and there are solutions.""",
  "Person thinking at counter", "WHY PEOPLE STAY UNBANKED"),
 ("""Try this: look for a Bank On certified account. These are low cost accounts offered by many banks and credit
unions, meeting national standards, usually with low or no monthly fees and no overdraft fees. You can find
them at the Bank On website.""",
  "Credit union branch", "BANK ON ACCOUNTS")])
card("""According to the FDIC, about four percent of American households, roughly five and a half million, had no bank
account in twenty twenty three.""",
     {"type": "stat", "label": "unbanked households", "big": "~5.6 MILLION", "size": 160, "sub": "FDIC National Survey, 2023"})

item(3, "Payday loans", "400% a year",
"""Cost number three. Payday loans.""",
[("""A payday loan is a small, short term loan, usually due on your next payday. According to the CFPB, a typical
two week payday loan charges a fee of around fifteen dollars for every one hundred dollars borrowed. That
sounds small. But as an annual percentage rate, it's almost four hundred percent.""",
  "Payday loan store", "~400% APR"),
 ("""The real trap is the rollover. Many borrowers can't repay the full amount in two weeks, so they pay the fee
and borrow again. The CFPB has found that most payday loan fees come from borrowers stuck in long sequences of
loans. A four hundred dollar loan can turn into hundreds of dollars in fees over a few months.""",
  "Calendar repeating payments", "THE ROLLOVER TRAP"),
 ("""Payday lending rules vary a lot by state. Some states ban high cost payday loans, others allow them. But
everywhere, they're one of the most expensive forms of credit available.""",
  "United States map", "RULES VARY BY STATE"),
 ("""Try this: if you're a member of a federal credit union, ask about a payday alternative loan. These small loans
are regulated by the National Credit Union Administration, with interest rates capped at twenty eight percent.
Still not cheap, but a fraction of a payday loan.""",
  "Credit union loan officer", "PAYDAY ALTERNATIVE LOANS")])
card("""A typical payday loan costs fifteen dollars per one hundred borrowed for two weeks. That's close to four hundred
percent a year. A federal credit union payday alternative loan is capped at twenty eight percent.""",
     {"type": "compare", "left": {"label": "Payday loan", "big": "~400%", "sub": "APR, typical (CFPB)"},
      "right": {"label": "Credit union PAL", "big": "≤28%", "sub": "APR cap (NCUA)"},
      "note": "Sources: CFPB, National Credit Union Administration"})

item(4, "Rent to own", "paying double for a sofa",
"""Cost number four. Rent to own.""",
[("""Rent to own stores let you take home furniture, appliances or electronics with no credit check, for weekly or
monthly payments. If you keep paying long enough, you own it. It sounds accessible. But the total cost can be
two or even three times the regular retail price.""",
  "Rent to own store", "NO CREDIT CHECK"),
 ("""Imagine a TV that costs five hundred dollars at a regular store. On a rent to own plan, the total payments to
own it could be over one thousand dollars. And if you miss payments, the store can take it back, and you keep
none of what you've paid.""",
  "Television living room", "$500 TV, $1,000+ COST"),
 ("""Rent to own contracts are also often structured so that the weekly payment looks tiny. Twenty or
thirty dollars a week feels manageable. But multiply by the number of weeks in the contract, and the total
tells a very different story. It's the same partitioned price trick we see with buy now, pay later, just older.""",
  "Weekly payment calendar", "THE WEEKLY PAYMENT TRICK"),
 ("""Try this: for things you truly need, look for used options, community buy nothing groups, or save for a few
weeks and buy outright. For a temporary need, renting can make sense. For owning, it's one of the most expensive
paths there is.""",
  "Used furniture marketplace", "USED OR SAVE FIRST")])

item(5, "The low credit tax", "higher rates on everything",
"""Cost number five. The low credit score tax.""",
[("""A lower credit score raises the price of almost everything you borrow. Car loans, credit cards, personal loans
and mortgages all cost more. The difference between a high score and a low score can be the difference between
a car loan at around seven percent and one at fifteen percent or more.""",
  "Credit score gauge low", "HIGHER RATES"),
 ("""Low credit also affects things that aren't loans at all. Some landlords check credit before renting.
Some employers review credit information for certain jobs, where allowed by law. And in many states, insurers use
credit based scores. A low score quietly raises the cost of living in many directions at once.""",
  "Rental application form", "IT REACHES EVERYWHERE"),
 ("""On a twenty thousand dollar car loan over five years, going from seven percent to fifteen percent adds roughly
four thousand eight hundred dollars in extra interest. Same car. Same price. Thousands more, because of a
number on a report.""",
  "Car loan document", "+$4,800 FOR THE SAME CAR"),
 ("""Try this: get your free credit reports at annual credit report dot com and dispute any errors. Pay every bill on
time, even if it's just the minimum. And keep card balances low. Scores can improve faster than many people
think, often within months.""",
  "Credit report review", "FIX ERRORS, PAY ON TIME")])

item(6, "Deposits everywhere", "paying upfront for trust",
"""Cost number six. Security deposits.""",
[("""Without good credit, many companies ask for deposits. A bigger security deposit on an apartment. Deposits for
electricity, gas, internet and phone service. Some landlords ask for extra months up front. That money is locked
away, often when you can least afford it.""",
  "Apartment keys and lease", "PAY UPFRONT"),
 ("""These deposits can add up to hundreds or even thousands of dollars, making it harder to move to a better or
cheaper place. Someone with good credit simply signs and moves in.""",
  "Moving boxes apartment", "HARDER TO MOVE"),
 ("""Try this: ask utilities whether they'll waive the deposit if you set up autopay, or after a period of on time
payments. And ask landlords if they accept a letter showing on time rent history. Many have flexibility they
don't advertise.""",
  "Utility bill and phone", "ASK FOR A WAIVER")])

item(7, "Prepaid card fees", "fees to use your own money",
"""Cost number seven. Prepaid card fees.""",
[("""Prepaid debit cards are popular with people who don't have bank accounts. But many have fees. Fees to buy the
card, monthly fees, reload fees, ATM fees and even fees for checking your balance on some cards. Each one is small.
Together, they can easily cost more than a basic bank account.""",
  "Prepaid card rack store", "FEES TO USE YOUR MONEY"),
 ("""Since twenty nineteen, the CFPB's prepaid rule requires clear fee disclosures on prepaid cards, which makes
comparison easier. Look for the short form disclosure on the package.""",
  "Prepaid card packaging", "READ THE FEE BOX"),
 ("""Try this: compare your yearly prepaid card fees with a Bank On certified account or a free online checking
account. For many people, switching saves money right away.""",
  "Comparison chart", "COMPARE AND SWITCH")])

item(8, "Title loans", "risking the car you need",
"""Cost number eight. Car title loans.""",
[("""A car title loan lets you borrow against your car, using the title as collateral. Interest rates are often
extremely high, and the loans are short. The CFPB found that about one in five single payment title loan
sequences ended with the borrower's car being repossessed.""",
  "Car title document", "1 IN 5 LOSE THE CAR"),
 ("""Losing the car can mean losing the ability to get to work, which makes everything worse. A loan meant to solve
a short term problem can create a much bigger one.""",
  "Person waiting at bus stop", "NO CAR, NO JOB?"),
 ("""Try this: before a title loan, call your creditors and ask for a payment plan, check local assistance programs
by dialing two one one, and ask a credit union about small loans. Almost any alternative is safer than risking
your car.""",
  "Phone dialing 211", "TRY 211 FIRST")])
pr("""That's eight costs of banking and borrowing. Now the hidden costs that don't show up on any statement.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
pr("""Angle two. Seven costs of time, energy and buying small.""")
short("The boots theory: why cheap things cost more")

item(9, "Buying small", "the unit price penalty",
"""Cost number nine. Buying in small quantities.""",
[("""Buying in bulk is usually cheaper per unit. The big pack of toilet paper, the large bag of rice, the family
size detergent. But bulk buying requires extra cash today, storage space, and often a car to get to a warehouse
store. Without those, people buy small, and pay more per unit.""",
  "Bulk products warehouse store", "BULK IS CHEAPER"),
 ("""Small differences per item add up across a whole year of groceries and household supplies. It's a quiet tax on
not having extra cash or space.""",
  "Small grocery bag", "A QUIET TAX"),
 ("""Location matters too. In some low income neighborhoods, there are fewer full size grocery stores, so people
shop at convenience stores where prices are often higher and choices are fewer. Researchers call these areas
food deserts. The same groceries can cost more simply because of where you live.""",
  "Corner convenience store", "WHERE YOU LIVE MATTERS"),
 ("""Try this: check unit prices on shelf tags, which show the price per ounce or per count. Team up with a friend or
neighbor to split bulk packs. And buy bulk only for things you use often and that don't spoil.""",
  "Unit price label shelf", "CHECK UNIT PRICES")])

item(10, "The boots theory", "cheap things cost more",
"""Cost number ten. The boots theory.""",
[("""The author Terry Pratchett described it through a character named Sam Vimes. A rich man buys good boots for fifty
dollars that last ten years. A poor man can only afford ten dollar boots that last a season. Over ten years, the
poor man spends far more on boots, and still has wet feet.""",
  "Worn out boots", "THE BOOTS THEORY"),
 ("""It's fiction, but it describes something real. Cheaper versions of shoes, appliances, tools and cars often wear
out faster. Without the cash to buy quality up front, people end up buying again and again.""",
  "Broken cheap appliance", "BUYING AGAIN AND AGAIN"),
 ("""Try this: for things you use daily, like shoes, a mattress or tools, look for quality used versions, which can
offer durability at a lower price. And save in a sinking fund so the next replacement can be a better one.""",
  "Quality used shoes", "QUALITY USED")])

item(11, "The time tax", "hours instead of dollars",
"""Cost number eleven. The time tax.""",
[("""Without a car, a trip to the grocery store, a job interview or a doctor's appointment can take hours by public
transit. Without paid leave, a sick day means lost wages. Without a washer, laundry means hours at a
laundromat. Being poor often costs time, and time is money you can't earn back.""",
  "Long bus commute", "HOURS, NOT DOLLARS"),
 ("""There's also the paperwork. Applying for benefits, proving eligibility, waiting on hold, renewing documents.
Researchers sometimes call this administrative burden. It falls hardest on the people with the least time and
flexibility.""",
  "Waiting room line", "ADMINISTRATIVE BURDEN"),
 ("""Try this: batch errands, use online services when possible, and ask employers about flexible scheduling. Small
time savings free up energy for the bigger moves that change your situation.""",
  "Phone online appointment", "BATCH AND MOVE ONLINE")])

item(12, "The bandwidth tax", "scarcity drains the mind",
"""Cost number twelve. The bandwidth tax.""",
[("""Researchers Sendhil Mullainathan and Eldar Shafir described how scarcity uses up mental bandwidth. In one
well known study, people facing money worries performed worse on cognitive tests, as if they had lost a
night's sleep. Not because they were less capable, but because worry was taking up mental space.""",
  "Stressed person thinking", "WORRY TAKES SPACE"),
 ("""That's important, because managing money with little cushion requires the most planning, comparing and
remembering. The situation demands more bandwidth and leaves less of it. It's one of the cruelest parts of
being poor.""",
  "Juggling balls", "MORE DEMAND, LESS BANDWIDTH"),
 ("""Try this: reduce the number of decisions you have to make. Automate bill payments when you can, set reminders
for due dates, and use simple rules. Systems save bandwidth for the decisions that matter.""",
  "Phone reminders calendar", "SYSTEMS SAVE BANDWIDTH")])

item(13, "Late fee cascades", "one late bill becomes three",
"""Cost number thirteen. Late fee cascades.""",
[("""When money is tight, one late bill can trigger others. A late rent payment means a late fee. Paying that fee makes
the phone bill late. The phone bill late fee makes the card payment late. Each fee makes the next payment
harder. Within a month, a small shortfall can become a pile of fees.""",
  "Stack of overdue bills", "ONE BECOMES THREE"),
 ("""Late payments can also be reported to credit bureaus once they're thirty days or more past due, which
lowers your score, which raises your future borrowing costs. So a single tight month can echo for years,
through higher interest on the next car loan or credit card.""",
  "Credit report late mark", "IT ECHOES FOR YEARS"),
 ("""Late fees on rent, utilities, credit cards and loans can each be twenty five to fifty dollars or more. Three or
four in one month can cost over one hundred dollars, often more than the original shortfall.""",
  "Calculator fees", "$100+ IN A MONTH"),
 ("""Try this: when you know a payment will be late, call before the due date. Many landlords, utilities and lenders
will waive a fee or agree to a short delay if you ask early. Calling after it's late is much harder.""",
  "Person calling landlord", "CALL BEFORE IT'S LATE")])

item(14, "Higher insurance costs", "credit and coverage",
"""Cost number fourteen. Higher insurance costs.""",
[("""In many states, insurers use credit based insurance scores to help set car and home insurance prices. That
means people with lower credit can pay more for the same coverage. And to keep premiums affordable, many people
choose high deductibles, which can be hard to pay when something actually happens.""",
  "Car insurance documents", "CREDIT AFFECTS PREMIUMS"),
 ("""Then there's being uninsured. Without health insurance, a single emergency room visit can cost thousands of
dollars. Without renter's insurance, a fire or theft can mean losing everything.""",
  "Emergency room entrance", "THE COST OF NO COVERAGE"),
 ("""Try this: shop insurance every year, ask about discounts, and check if you qualify for subsidized health
coverage through the official marketplace at health care dot gov, or Medicaid in your state. Renter's insurance is
often surprisingly cheap.""",
  "Healthcare marketplace website", "SHOP AND CHECK SUBSIDIES")])

item(15, "Account and ATM fees", "small balances, big fees",
"""Cost number fifteen. Monthly account and ATM fees.""",
[("""Many accounts waive monthly fees if you keep a minimum balance. People with low balances pay those fees, and
people with high balances don't. And without a nearby in network ATM, withdrawing cash can cost several dollars
each time.""",
  "ATM fee screen", "FEES FOR LOW BALANCES"),
 ("""Try this: look for accounts with no monthly fees and no minimum balance, including many online banks and credit
unions. Use in network ATMs, or get cash back at stores when buying something you already need.""",
  "Cash back at register", "NO FEE ACCOUNTS"),
 ("""Some employers also offer pay cards instead of direct deposit. By law, they generally have to give you
at least one way to get your full pay without a fee. Ask your employer or the card provider how to avoid fees,
or ask to switch to direct deposit into your own account.""",
  "Pay card employer", "ASK ABOUT PAY CARDS")])

# ---------------- Mid ----------------
ch("A quick favor")
pr("""Quick pause. If this video might help someone you know, please share it with them. And subscribe to the
channel if it's helping you. It's free, and it helps me keep making these videos. Now, the last five costs,
and how to escape them all.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
pr("""Angle three. The last five costs, and then the escape plan.""")
short("How to escape the poverty premium, step by step")

item(16, "Fines that grow", "tickets become debts",
"""Cost number sixteen. Fines and fees that grow.""",
[("""A parking ticket or traffic fine might be manageable at first. But if it isn't paid on time, many places add late
fees, collection fees, and in some cases suspend driver's licenses. A one hundred dollar ticket can grow into
several hundred dollars, and a suspended license can make it harder to work.""",
  "Parking ticket windshield", "TICKETS GROW"),
 ("""Try this: contact the court or agency early. Many offer payment plans, reduced fines based on income, or
community service options. Some jurisdictions run amnesty programs. Ignoring it is the most expensive choice.""",
  "Courthouse building", "ASK FOR A PLAN"),
 ("""Also check whether a fine has turned into a license suspension without you knowing. Driving on a
suspended license can lead to much bigger penalties. Many states have online tools to check your license status,
and some have programs to restore licenses suspended only for unpaid fines.""",
  "Driver license card", "CHECK YOUR LICENSE")])

item(17, "Buy here, pay here cars", "the most expensive cars",
"""Cost number seventeen. Buy here, pay here car lots.""",
[("""Buy here, pay here dealers sell used cars with in house financing, often without a credit check. For people with
poor credit, they may seem like the only option. But interest rates can be very high, cars may be priced above
their value, and some dealers repossess quickly when a payment is missed.""",
  "Used car lot small", "BUY HERE, PAY HERE"),
 ("""Try this: before visiting one, check with a credit union, even with imperfect credit. Some offer loans designed for
rebuilding credit. And consider a cheaper car bought partly with savings, with an independent mechanic's
inspection.""",
  "Mechanic inspecting car", "CREDIT UNION FIRST"),
 ("""And read the contract carefully. Look for the APR, the total of payments, and what happens if you're late.
Some contracts allow the dealer to install devices that disable the car if a payment is missed. Know exactly what
you're agreeing to before you sign.""",
  "Car loan contract", "READ THE TOTAL OF PAYMENTS")])

item(18, "Medical debt", "the bill you didn't choose",
"""Cost number eighteen. Medical debt.""",
[("""Medical debt is one of the most common kinds of debt in collections. The CFPB has estimated that medical bills on
credit reports totaled around eighty eight billion dollars. People with less savings and less insurance are hit
hardest, and medical debt can then damage their credit, raising the cost of everything else.""",
  "Hospital bill paper", "$88 BILLION ON REPORTS"),
 ("""There's been some progress. The major credit bureaus stopped reporting paid medical collections, and medical
collections under five hundred dollars, in recent years. And many nonprofit hospitals are required to have
financial assistance policies.""",
  "Hospital building", "SOME PROGRESS"),
 ("""Try this: always ask for an itemized bill and check for errors. Ask the hospital about financial assistance or
charity care, which you may qualify for even with a job. And ask for a payment plan with no interest before the
bill goes to collections.""",
  "Itemized medical bill review", "ASK FOR ASSISTANCE")])

item(19, "Missing the match", "the benefits gap",
"""Cost number nineteen. Missing out on employer benefits.""",
[("""When every dollar is needed for this week, saving for retirement can feel impossible. So many lower income workers
don't contribute enough to get their employer's retirement match, which is essentially part of their pay left on
the table. Some jobs don't offer retirement plans at all.""",
  "Retirement plan enrollment form", "LEAVING THE MATCH"),
 ("""There's also the Saver's Credit, a federal tax credit for low and moderate income workers who contribute to
retirement accounts. Many eligible people don't know it exists. The IRS has information on who qualifies.""",
  "IRS tax credit form", "THE SAVER'S CREDIT"),
 ("""Try this: if your employer offers a match, try to contribute at least one percent, then increase it as you can.
And check whether you qualify for the Saver's Credit when you file taxes.""",
  "Paycheck with deduction", "START WITH 1%")])

item(20, "No cushion", "the cost behind all costs",
"""Cost number twenty. Having no cushion at all.""",
[("""This is the cost behind almost every other cost on this list. Without even a small emergency fund, every
surprise turns into a fee, a high interest loan or a late payment. The cushion is what separates an inconvenience
from a crisis.""",
  "Empty savings jar", "THE COST BEHIND ALL COSTS"),
 ("""Even a few hundred dollars can make a huge difference. It can stop an overdraft, avoid a payday loan, or cover a
car repair. It's not a lot of money, but it breaks the chain of fees.""",
  "Small savings envelope", "A FEW HUNDRED DOLLARS"),
 ("""Research supports this. Studies of emergency savings have found that even small amounts of liquid savings are
linked to fewer missed bill payments and less use of high cost credit. A small cushion isn't just
comforting. It changes outcomes.""",
  "Research report document", "SMALL SAVINGS, BIG EFFECT"),
 ("""Try this: start with a goal of five hundred dollars. Save small amounts automatically, and put any windfalls, like
tax refunds, straight into it. Keep it in a separate account so it doesn't get spent by accident.""",
  "Separate savings account app", "START WITH $500")])

ch("The escape plan")
sc("""It's worth saying clearly. None of the twenty costs we've covered requires a bad decision. A low balance, an
old car, a medical emergency or a gap between jobs can happen to anyone. That's why the escape plan focuses on
building systems, a safe account, a small cushion and better credit, instead of on willpower. Systems keep
working on the hard weeks, when willpower runs out.""",
   "Gears working together", "SYSTEMS OVER WILLPOWER")
pr("""So how do you escape the poverty premium? Here's a step by step plan. It starts small, on purpose.""")
sc("""Step one. Get a safe, low cost account. A Bank On certified account or a credit union account with no
overdraft fees. This alone can save hundreds of dollars a year in check cashing, prepaid card and overdraft
fees.""",
   "Opening bank account", "STEP 1: A SAFE ACCOUNT")
sc("""Step two. Build a starter cushion of five hundred dollars. Even ten or twenty dollars a week adds up. This is the
wall that stops the cascade of fees. Step three. Replace the most expensive debt first. If you have a payday or
title loan, look for a credit union alternative to pay it off.""",
   "Savings jar growing", "STEPS 2 AND 3")
sc("""Step four. Start building credit. A secured credit card, used for one small bill each month and paid in full,
can build a score over time. Credit builder loans from credit unions are another option. Better credit lowers
the cost of almost everything else.""",
   "Secured credit card", "STEP 4: BUILD CREDIT")
sc("""Step five. Claim what you're owed. Check eligibility for the Earned Income Tax Credit, the Saver's Credit,
health insurance subsidies, and local assistance programs. Many eligible people never claim them. The IRS says
about one in five eligible workers don't claim the Earned Income Tax Credit.""",
   "Tax refund credit form", "STEP 5: CLAIM WHAT YOU'RE OWED")
sc("""And step six. Grow income. A certification, a trade skill, a better paying role, or a side income with a clear
goal. Cutting costs has limits. Raising income doesn't. And every dollar of new income, once the cushion is in
place, can go toward the future instead of fees.""",
   "Trade school training", "STEP 6: GROW INCOME")
card("""The Earned Income Tax Credit can be worth thousands of dollars for working families. But according to the IRS,
about one in five eligible workers don't claim it.""",
     {"type": "stat", "label": "earned income tax credit", "big": "1 IN 5", "sub": "eligible workers don't claim it (IRS)"})

# ---------------- A year of costs ----------------
ch("What the poverty premium costs in a year")
sc("""Let's add up a realistic year for someone without a cushion, using modest numbers. Check cashing on paychecks,
perhaps two hundred to three hundred dollars. A few overdraft fees, around one hundred dollars. Three late fees,
about one hundred dollars. One payday loan rolled over twice, around one hundred eighty dollars in fees.""",
   "Calculator and receipts", "ADDING IT UP")
sc("""Add higher interest on a car loan because of a lower credit score, maybe eight hundred to one thousand dollars a
year. A higher insurance premium, a few hundred dollars. Prepaid card fees, rent to own markups, and buying small.
Quickly, the total can reach two thousand to three thousand dollars a year, depending on the person.""",
   "Bills stacked high", "$2,000 TO $3,000 A YEAR")
card("""Fees, interest and higher prices can add up to two to three thousand dollars a year for a household without a
cushion. That money could have been the cushion.""",
     {"type": "compare", "left": {"label": "Poverty premium", "big": "$2-3K", "sub": "a year, rough estimate"},
      "right": {"label": "Could become", "big": "A cushion", "sub": "in a single year"},
      "note": "Illustration. Actual costs vary widely."})
sc("""Here's the cruel irony. Two to three thousand dollars a year is more than enough to build a solid starter emergency
fund. The money that's lost to the poverty premium is often exactly the money that could end it. That's why
the first steps of the escape plan focus on stopping fees, not on cutting groceries.""",
   "Broken chain", "THE MONEY THAT COULD END IT")

# ---------------- Biggest wins ----------------
ch("The five biggest quick wins")
pr("""If you only do five things from this video, do these. They usually save the most money for the least effort.""")
sc("""Win one. Move to a no overdraft, low fee account. Win two. Never roll over a payday loan, and replace it with a
credit union alternative if you can. Win three. Call before any bill is late, and ask for a fee waiver or a short
delay.""",
   "Checklist phone", "WINS 1 TO 3")
sc("""Win four. File your taxes, even if your income is low, and check for the Earned Income Tax Credit. It can be worth
thousands of dollars, and many eligible people miss it. Free help is available through the IRS's VITA program.
And win five. Automate a tiny weekly savings transfer, even ten dollars, into a separate account. That's the
seed of your cushion.""",
   "Tax forms and coins", "WINS 4 AND 5")

# ---------------- Stories ----------------
ch("Two neighbors, same income")
short("Same income, $2,000 a year difference. Here's why.")
sc("""Let's see how much the poverty premium can cost in a year, with two neighbors earning the same income. Tanya
cashes her paychecks at a check cashing store, uses a prepaid card, and has no savings. When her car broke down,
she took a payday loan and rolled it over twice. She paid several overdraft and late fees during the year.""",
   "Woman at check cashing store", "TANYA: NO CUSHION")
sc("""Add it up, and Tanya paid easily over one thousand dollars in fees and interest that year, possibly closer to
two thousand. Not because she was careless. Because every surprise cost her extra, and she had no other
options she knew about.""",
   "Pile of receipts fees", "$1,000 TO $2,000 IN FEES")
sc("""Her neighbor Maria earns the same. But a friend told her about a credit union with a free account and no overdraft
fees. Maria set up automatic savings of fifteen dollars a week, and built a cushion of about seven hundred
dollars over the year. When her car broke down, she paid from savings and a small credit union loan.""",
   "Woman at credit union counter", "MARIA: THE CREDIT UNION")
sc("""Maria paid almost nothing in fees. Same income, same city, same kind of emergency. But a gap of over a thousand
dollars a year. Over five years, that gap could be enough to build a real emergency fund, or start investing.
The poverty premium is real. And for many people, small changes can cut it dramatically.""",
   "Two paths split", "SAME INCOME, DIFFERENT COSTS")

sc("""Fast forward three years. Maria's cushion has grown to a full month of expenses. Her credit score is good
enough for a normal car loan rate. She contributes to her employer's retirement plan and gets the match. Tanya,
still paying the premium, is in a similar place to where she started, through no lack of effort. Then a coworker
tells Tanya about the credit union. Within a year, her fees drop to almost nothing, and her own cushion begins.""",
   "Two women talking at work", "THREE YEARS LATER")
sc("""The lesson isn't that one neighbor was smarter. It's that information is one of the most valuable things in
personal finance. Maria heard about a better option first. That's why sharing what you learn matters. Someone
you know might be paying the poverty premium right now, simply because nobody told them there's another way.""",
   "Friends sharing information", "SHARE WHAT YOU LEARN")

# ---------------- FAQ ----------------
ch("Questions people ask")
pr("""Let me answer a few questions people ask about the cost of being poor.""")
sc("""Question one. I've been rejected by banks before. What can I do? Ask about second chance checking accounts,
designed for people with past banking problems. Many banks and credit unions offer them. You can also request
your ChexSystems report, a record banks use, to see why you were rejected and dispute errors.""",
   "Bank rejection letter", "REJECTED BEFORE?")
sc("""Question two. Are payday loans ever okay? They're one of the most expensive options available. Before using one,
call creditors, ask your employer about a paycheck advance, look for credit union alternatives, and check local
assistance through two one one. If you do use one, have a clear plan to repay it on the first due date, without
rolling it over.""",
   "Payday loan sign", "ARE PAYDAY LOANS OKAY?")
sc("""Question three. How long does it take to build credit? With a secured card or credit builder loan and on time
payments, many people see a score within about six months, and improvement over a year or two. Consistency
matters more than anything else.""",
   "Credit score rising", "HOW LONG FOR CREDIT?")
sc("""Question four. Where can I get free help? Nonprofit credit counseling agencies, local credit unions, community
action agencies and free tax preparation programs, like the IRS's VITA program, can all help. Dial two one one to
find local services.""",
   "Community center help desk", "FREE HELP")
sc("""Question five. What if I'm already behind on several bills? Make a list of everything you owe and when. Protect
housing, utilities, food and transportation to work first. Then call each creditor, explain your situation and
ask for a plan. A nonprofit credit counselor can help you prioritize and sometimes negotiate on your behalf, often
for free or a small fee.""",
   "List of bills on table", "ALREADY BEHIND?")
sc("""And question six. Isn't this a system problem, not a personal one? Yes, a lot of it is. The poverty premium is
built into how many products are priced. That's worth changing, and regulators and advocates are working on it.
But while the system changes slowly, knowing these costs and the alternatives can put real money back in your
pocket today.""",
   "Capitol building", "A SYSTEM PROBLEM?")

sc("""One more thought before the recap. If you're living with the poverty premium right now, you're dealing with
a harder version of personal finance than most money advice assumes. The fact that you're watching a thirty
minute video about it says a lot about your determination. Small steps count more here than anywhere else,
because each fee you stop is money that stays with you, every single month.""",
   "Determined person walking sunrise", "SMALL STEPS COUNT MORE")

# ---------------- Recap ----------------
ch("Recap: all 20 costs")
short("20 hidden costs of being poor")
sc("""Quick recap. The banking and borrowing costs: overdraft fees, check cashing, payday loans, rent to own, the low
credit tax, deposits, prepaid card fees and title loans. The time and energy costs: buying small, the boots
theory, the time tax, the bandwidth tax, late fee cascades, higher insurance costs, and account fees.""",
   "Checklist clipboard", "THE FIRST 15")
sc("""And the last five: fines that grow, buy here pay here cars, medical debt, missing employer benefits, and the cost
behind all costs, having no cushion. The escape plan: a safe account, a five hundred dollar cushion, replace the
worst debt, build credit, claim what you're owed, and grow your income.""",
   "Stairs going up", "THE LAST 5 AND THE ESCAPE")

# ---------------- Close ----------------
ch("What to do next")
pr("""If you want the full plan from zero to a real emergency fund and beyond, it's in my playbook. The link is in the
description. And watch my video on why most people stay broke, and how to escape. It's the perfect next step
after this one. I'm Ryan Rover. See you in the next one.""")

save("video50", "The Real Cost of Being Poor: 20 Hidden Fees", [
    "FDIC, National Survey of Unbanked and Underbanked Households (2023): about 4.2% of households unbanked, about 5.6 million",
    "Consumer Financial Protection Bureau, payday loan research (typical $15 per $100 for two weeks, nearly 400% APR); single-payment auto title loans (about 1 in 5 sequences end in repossession); overdraft research; medical debt on credit reports (about $88 billion); prepaid accounts rule",
    "National Credit Union Administration, Payday Alternative Loans (28% APR cap)",
    "IRS, Earned Income Tax Credit participation (about 4 in 5 eligible claim it); Saver's Credit; VITA free tax help",
    "Mani, Mullainathan, Shafir and Zhao, Poverty Impedes Cognitive Function, Science (2013)",
    "Terry Pratchett, Men at Arms (1993): the Sam Vimes boots theory",
    "Bank On national account standards (Cities for Financial Empowerment Fund)",
    "Loan and fee figures: stated illustrative math",
], "the cost of being poor: numbers, psychology, playbook")
