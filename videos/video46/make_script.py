import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

def item(n, title, sub, card_text, paras, label="TRAP"):
    """paras: list of (text, query, caption)"""
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"{label} {n}")
    for t, q, c in paras:
        sc(t, q, c)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Pay in four. Zero interest. No impact on your credit, in many cases. Just split it.
Buy now, pay later has spread from sneakers and electronics to concert tickets, plane tickets, groceries
and even takeout. It looks like the friendliest kind of debt ever invented. Today, let's find out whether
it really is, or whether it's the quietest debt trap of this decade.""")
short("Buy now, pay later is the quietest debt trap of this decade")
card("""Buy now, pay later lets you split a purchase into smaller payments, often four payments over six
weeks, frequently with no interest if you pay on time.""",
     {"type": "stat", "label": "buy now, pay later", "big": "PAY IN 4", "sub": "often every two weeks, often no interest"})
sc("""Here's the thing. On paper, a zero interest loan paid on time is a pretty good deal. It costs nothing
extra. So why are regulators, economists and consumer groups paying such close attention? Because the
product is designed to make spending feel smaller than it is, to be used again and again, and to be easy
to stack. And debt that feels small is the easiest kind to accumulate.""",
   "Phone checkout screen", "DEBT THAT FEELS SMALL")
sc("""We'll look at buy now, pay later from three angles. First, the numbers: how big it's become, how the
companies make money, and what happens when payments slip. Second, the psychology: why splitting a price
into four changes how much we spend. And third, the playbook: clear rules for when it's fine, when it's
risky, and how to get out if you're juggling too many plans.""",
   "Three arrows target", "THREE ANGLES")
pr("""If you've ever had three or four of these running at the same time, this video is for you. Let's start
with the numbers.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Every number here comes from a named source. Market data comes from reports by the Consumer Financial
Protection Bureau, which has studied buy now, pay later lenders and their customers. Household data comes
from the Federal Reserve's yearly survey of household well being. This market changes quickly, and rules
and products differ by company, so always read the terms of any plan you use. This is education, not
financial advice.""",
   "Government report documents", "OUR SOURCES")

# ---------------- History ----------------
ch("Paying later is not new")
pr("""Before the numbers, a little history. Because paying later isn't new at all. It's one of the oldest
tricks in retail.""")
sc("""In the eighteen fifties, the Singer company faced a problem. Its sewing machines were life changing,
but too expensive for many families to buy outright. So it offered an installment plan. A small payment
down, then regular payments over time. Sales took off. Many historians point to it as one of the early
examples of consumer installment buying in America.""",
   "Antique Singer sewing machine", "1850s: SINGER'S PLAN")
sc("""In the twentieth century, installment plans spread to furniture, radios, appliances and cars.
Department stores offered layaway, where you paid in small amounts before taking the item home. Notice
the difference. With layaway, you paid first and got the item last. With buy now, pay later, you get the
item first and pay last. That small flip changes everything about how it feels.""",
   "Vintage department store", "LAYAWAY: PAY FIRST")
sc("""Then came credit cards, which made paying later universal. And now, buy now, pay later combines the old
installment plan with modern technology. Instant approval, phone apps and one tap checkout. The idea is
over a century old. What's new is the speed, and how easy it is to have many plans at once.""",
   "Smartphone app shopping", "THE OLD IDEA, FASTER")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. How big this has become, and how it actually works.""")

item(1, "Explosive growth", "from niche to everywhere",
"""Number one. Explosive growth.""",
[("""Buy now, pay later existed in different forms for years, but it exploded around twenty twenty. A report
by the Consumer Financial Protection Bureau found that loans from five major providers grew from about two
billion dollars in twenty nineteen to more than twenty four billion dollars in twenty twenty one. That's
more than ten times larger in just two years.""",
  "Graph rising sharply", "ABOUT 10X IN TWO YEARS"),
 ("""And it kept growing after that. Today, buy now, pay later buttons appear at checkout on major retail sites,
in phone wallets, inside banking apps, and even at physical stores. Some plans now cover everyday
spending, like groceries and food delivery. What started as a way to buy a pair of sneakers has become a
general way to pay for almost anything.""",
  "Online store checkout options", "EVERYWHERE AT CHECKOUT"),
 ("""Why did it grow so fast? Partly because shopping moved online during the pandemic. Partly because many
younger shoppers were wary of credit cards. And partly because merchants discovered that offering it can
increase sales. When something helps both the lender and the store sell more, you can expect to see it
everywhere.""",
  "Young shopper with phone", "WHY IT GREW")])
card("""According to the Consumer Financial Protection Bureau, buy now, pay later loans from five large
lenders grew from about two billion dollars in twenty nineteen to over twenty four billion in twenty twenty
one.""",
     {"type": "compare", "left": {"label": "2019", "big": "~$2B", "sub": "in BNPL loans"},
      "right": {"label": "2021", "big": "$24B+", "sub": "in BNPL loans"},
      "note": "Source: CFPB, five large BNPL lenders"})

item(2, "Who really pays", "the merchant, at first",
"""Number two. If it's zero interest, who pays?""",
[("""With the classic pay in four plan, the main payer is the merchant. Stores typically pay the buy now, pay
later company a fee on each sale, and those fees are often higher than what they'd pay for a regular card
transaction. Why would a store pay more? Because offering split payments can make shoppers more likely to
complete a purchase, and to spend more per order.""",
  "Store owner looking at sales", "THE STORE PAYS"),
 ("""Think about what that means. The merchant is paying extra because the product changes your behavior in a
way that's good for the store. More completed purchases. Bigger carts. That's not a conspiracy. It's the
business model, written right on the lenders' marketing to merchants: offer us at checkout, and sell
more.""",
  "Full shopping cart online", "BIGGER CARTS"),
 ("""There's also a newer twist. Some buy now, pay later companies run their own shopping apps, with
deals, rewards and personalized offers. That means the lender isn't just financing your purchase. It's
also showing you what to buy next. When the company that profits from your spending also curates your
shopping feed, it's worth being extra careful.""",
  "Shopping app deals screen", "THE LENDER IS THE STORE")])

item(3, "Late fees and interest", "where the cost appears",
"""Number three. Late fees, and the loans that do charge interest.""",
[("""If you miss a payment, many providers charge a late fee. The amounts and rules vary by company and by
state, and some providers have dropped late fees altogether. But a late fee on a small payment can be a
big percentage of what you owed. A seven dollar late fee on a twenty five dollar installment is a twenty
eight percent charge for being a few days late.""",
  "Late payment notification phone", "A FEE ON A SMALL PAYMENT"),
 ("""And not every buy now, pay later plan is zero interest. Many providers also offer longer plans, over six,
twelve, or even more months, especially for bigger purchases. These often charge interest, and the rates
can be high, sometimes comparable to credit cards, depending on your credit and the store's deal with the
lender.""",
  "Big screen television store", "LONGER PLANS, REAL INTEREST"),
 ("""So the name buy now, pay later covers two very different things. A short, zero interest plan that costs
nothing if you're always on time. And a longer installment loan that can cost real money. Many shoppers
don't notice which one they picked, because the checkout screens look similar. Try this: before you tap,
look for the letters APR. If you see a number above zero, it's a loan with interest.""",
  "Fine print on screen", "LOOK FOR THE APR")])

item(4, "Stacking", "many loans at once",
"""Number four. Loan stacking.""",
[("""Here's where things get risky. Because each loan is small and approval is fast, many people take out
several at once. A CFPB study of buy now, pay later borrowers found that around sixty three percent took
out more than one loan at the same time at some point during the year, and about a third used more than one
buy now, pay later company.""",
  "Multiple apps on phone screen", "63% STACKED LOANS"),
 ("""Each loan alone might be manageable. Twenty five dollars here, forty dollars there. But six loans across
three apps, with payments every two weeks on different dates, can add up to hundreds of dollars a month,
and become very hard to track. Missing one isn't about being careless. It's about juggling too many small
bills.""",
  "Calendar many due dates", "SMALL LOANS, BIG TOTAL"),
 ("""Picture it. Eighty dollars of shoes. A two hundred dollar jacket. A three hundred twenty dollar
phone. Groceries split twice. Concert tickets. Individually, the payments look like twenty, fifty, eighty
dollars. Together, they can easily reach two hundred to three hundred dollars every two weeks. That's more
than many people's car payment, spread across apps they rarely open.""",
  "Shopping bags many", "IT ADDS UP")])
card("""Six small plans running at the same time, each split into four payments, can add up to hundreds of
dollars every two weeks.""",
     {"type": "compare", "left": {"label": "One plan", "big": "$25", "sub": "every two weeks"},
      "right": {"label": "Six plans", "big": "$250+", "sub": "every two weeks"},
      "note": "Illustration. Totals depend on your purchases."})

item(5, "Phantom debt", "invisible to everyone",
"""Number five. Phantom debt.""",
[("""For years, many buy now, pay later loans didn't show up on traditional credit reports. That sounds like a
benefit. But it creates what some economists call phantom debt. Other lenders can't see it. Sometimes even
you lose track of it. A credit card company approving a new card, or a lender approving a car loan, might
have no idea that you already owe several hundred dollars in installments.""",
  "Invisible ghost illustration", "PHANTOM DEBT"),
 ("""This is starting to change. Some lenders have begun reporting these loans to credit bureaus, and credit
scoring companies have announced ways to include them. That's good for transparency. But it also means
missed payments may increasingly show up where it hurts. The safe assumption today is simple: treat every
buy now, pay later plan as real debt, because it is.""",
  "Credit report document", "IT'S REAL DEBT"),
 ("""The phantom debt problem also affects households. Couples can be surprised to find their partner has
several plans running. Parents may not realize a young adult child is juggling them. Because these loans
are small and live inside apps, they're easy to hide, even without meaning to.""",
  "Couple surprised looking at phone", "HIDDEN IN THE APPS")])

item(6, "Who uses it most", "often those with the least room",
"""Number six. Who uses it most.""",
[("""The CFPB found that buy now, pay later borrowers were, on average, more likely to have high levels of
other debt, like credit cards, and more likely to carry balances on those cards, than people who didn't
use it. Many were younger, and many had lower credit scores. In other words, the product is often used by
people who already have the least room in their budgets.""",
  "Young adults in city", "LEAST ROOM, MOST USE"),
 ("""That doesn't mean everyone who uses it is in trouble. Plenty of people use it for convenience and pay
everything on time. But it does mean that for a large group of users, buy now, pay later isn't replacing
credit cards. It's adding to them. More debt, spread across more places.""",
  "Credit cards and phone", "ADDING, NOT REPLACING"),
 ("""And the Federal Reserve's household survey has found that a meaningful share of buy now, pay later users
reported paying late at least once. When people who already carry other debts start missing small
payments, it's often a sign of a bigger squeeze in the household budget. The small late payment is the
warning light, not the real problem.""",
  "Dashboard warning light", "THE WARNING LIGHT")])
sc("""Regulators have noticed. The CFPB has published several reports on buy now, pay later, and the rules
that apply to it have been debated and changed more than once in recent years. Other countries have also
moved to regulate it more closely. For you, the practical lesson is that protections can vary by provider
and change over time. Don't assume a buy now, pay later loan gives you the same rights as a credit card.
Read the dispute and refund terms.""",
   "Government building columns", "THE RULES ARE CHANGING")
pr("""So the numbers show a product that's huge, growing, and used most heavily by people with the least
slack. Now let's look at why it changes how we spend.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
pr("""Angle two. The psychology. Seven reasons splitting a price makes us spend more.""")
short("Why 4 payments of $50 feels cheaper than $200")

item(7, "The smaller number", "$50 feels cheaper than $200",
"""Reason number seven. The smaller number wins.""",
[("""When a two hundred dollar jacket is shown as four payments of fifty dollars, your brain anchors on fifty.
Fifty feels affordable. Two hundred might make you pause. It's the same jacket and the same total, but the
number you see first changes the decision. Marketers have known this for a long time. It's the same reason
gym memberships are priced per day and cars are priced per month.""",
  "Price tag fifty dollars", "THE SMALLER NUMBER"),
 ("""Researchers who study pricing call this partitioning. When a price is broken into parts, people often
underestimate the total. With buy now, pay later, the partition is right there on the button. Pay four
interest free payments of fifty dollars. The two hundred is technically shown, but it's not what sticks.""",
  "Checkout button four payments", "PARTITIONED PRICES"),
 ("""Try this: before using a split payment, say the full price out loud. Not four payments of fifty. Two
hundred dollars. Then ask whether you'd buy it at that price, paid today. If the answer is yes, the split
is just convenience. If the answer is no, the split is doing the persuading.""",
  "Person thinking at laptop", "SAY THE FULL PRICE")])

item(8, "It doesn't feel like debt", "no card, no loan, just a plan",
"""Reason number eight. It doesn't feel like debt.""",
[("""Most people know credit cards are debt. But buy now, pay later feels different. There's no plastic card,
often no hard credit check, and the language is friendly. Plans, installments, splitting. Many users don't
think of themselves as borrowers at all. And if you don't think it's debt, you don't treat it with the same
caution.""",
  "Friendly app design", "A PLAN, NOT A LOAN?"),
 ("""But legally and practically, it's a loan. You receive something now and promise to pay for it later. If
you don't pay, there are consequences: fees, collections, and possibly credit damage. The friendly
language doesn't change the obligation. It just makes it easier to say yes.""",
  "Signature on agreement", "IT'S STILL A LOAN"),
 ("""Try this: rename it in your head. Every time you see the button, read it as take out a loan. Take out a
loan for these headphones. Take out a loan for this dinner. It sounds dramatic, but it's simply accurate.
And it brings back the caution that the friendly language removes.""",
  "Loan word on screen", "CALL IT A LOAN")])

item(9, "Less pain of paying", "you barely feel it",
"""Reason number nine. Less pain of paying.""",
[("""Paying hurts a little. That small pain is actually useful. It makes you think. Researchers have shown
that people often spend more when the pain of paying is reduced, for example by paying with cards instead of
cash. Buy now, pay later reduces it even further. You pay only a quarter today, and the rest happens
automatically later, when the excitement of buying has moved on.""",
  "Happy shopper with bags", "PAY LATER, FEEL LATER"),
 ("""This also separates the joy from the cost. You enjoy the purchase now. The payments arrive in two, four
and six weeks, when you might be enjoying something else, also bought with a split plan. The cost and the
pleasure never meet, so the cost never feels as big as it is.""",
  "Calendar with payments marked", "JOY NOW, COST LATER"),
 ("""Try this: if you do use a split plan, put every future payment date in your calendar with the item name.
Payment three of four, jacket, forty five dollars. When the reminder appears, you reconnect the cost with
the purchase. It's a small habit, and it makes the real price visible again.""",
  "Calendar reminder phone", "NAME EVERY PAYMENT")])

item(10, "Bigger carts", "the plan makes it fit",
"""Reason number ten. Bigger carts.""",
[("""When the total is split, a more expensive option starts to look reachable. The one hundred fifty dollar
shoes feel like they cost the same as the one hundred dollar ones, because the split payments are only a
little different. Merchants report larger average orders when split payments are offered. That's one of
the main reasons they pay the fees.""",
  "Comparing two shoes in store", "THE UPGRADE FEELS SMALL"),
 ("""Try this: when you see a split payment option, decide what you were going to buy before you saw the
button. Then stick to that item and that price. The button can change how you pay. It shouldn't change
what you buy.""",
  "Shopping list on phone", "DECIDE BEFORE THE BUTTON"),
 ("""This works for subscriptions and memberships too. Many offers now show a monthly price for things you
used to pay for once. The smaller number always looks friendlier. Always convert it back to the yearly or
total price, and decide based on that.""",
  "Monthly price tag", "CONVERT TO THE TOTAL")])

item(11, "Instant approval", "no time to think",
"""Reason number eleven. Instant approval.""",
[("""Traditional loans have friction. Applications, waiting, maybe a call from the bank. That friction gives
you time to reconsider. Buy now, pay later approval often takes seconds, right at checkout. There's no pause
between I want this and it's mine. Speed is great for convenience, and dangerous for impulse purchases.""",
  "Approved checkmark screen", "APPROVED IN SECONDS"),
 ("""Late night shopping makes it worse. Tired, scrolling, a little bored, and one tap away from a new plan.
Many impulse purchases happen exactly in those moments. Try this: create a personal rule. No split payment
purchases after nine p.m. If you still want it in the morning, go ahead.""",
  "Person shopping phone at night", "NO PLANS AFTER 9 PM"),
 ("""You can also add your own friction. Use a separate debit card with a set weekly amount for online
shopping, so you physically can't spend more than you planned. Or log out of shopping apps after each use.
The few extra seconds it takes to log back in are often enough for your better judgment to catch up.""",
  "Logging out of app", "ADD YOUR OWN FRICTION")])

item(12, "Everyone is doing it", "influencers and checkouts",
"""Reason number twelve. It's normal now.""",
[("""Social media is full of hauls and outfits, sometimes bought with split payments, and the option appears on
so many stores that it starts to feel like the default way to pay. When something is everywhere, we assume
it's safe. When friends use it casually, it feels responsible enough.""",
  "Influencer filming haul video", "IT FEELS NORMAL"),
 ("""But being normal doesn't make something right for your budget. Remember, the CFPB found many users already
had high levels of other debt. Normal can mean that many people are stretched. Try this: follow your own
numbers, not the feed. If your monthly split payments ever exceed what you'd put in savings, something is
off.""",
  "Person putting phone down", "YOUR NUMBERS, NOT THE FEED"),
 ("""It's also worth remembering that some creators earn commissions on what they recommend, and promoted
posts don't always look like ads. That's not wrong, but it means the person telling you to buy may benefit
when you do. Enjoy the content. Make your own decisions.""",
  "Affiliate link phone", "WHO BENEFITS?")])

item(13, "Mental accounting chaos", "four apps, no total",
"""Reason number thirteen. Losing track.""",
[("""When debts live in one place, like a single credit card statement, you can see the total. Buy now, pay
later spreads debt across different apps, each with its own schedule. Your brain counts each one as small.
Nobody adds them up. And if payments come out automatically from your debit card, they can pull money you
needed for rent or bills.""",
  "Multiple phone apps icons", "NO SINGLE TOTAL"),
 ("""This can trigger overdraft fees at your bank, on top of any late fees from the lender. Two fees for one
small payment. Try this: once a week, open every buy now, pay later app you use and write down the total you
owe and every due date in one place, a note on your phone or a simple calendar. One total. One list.""",
  "Phone note with list", "ONE TOTAL, ONE LIST"),
 ("""When you write the total down, compare it with your monthly savings. If you owe more in split payments than
you save each month, that's a clear signal to pause new plans until the list is empty. Most people who do
this exercise once say it changes how they use the button forever.""",
  "Comparing two numbers notepad", "COMPARE WITH SAVINGS")])

# ---------------- Self test ----------------
ch("Are you in the trap? A quick test")
sc("""Before the playbook, a quick self test. One. Do you have more than one buy now, pay later plan running
right now? Two. Have you used it for food, groceries or takeout in the last month? Three. Do you know the
total you owe across all apps, without looking?""",
   "Questionnaire pen paper", "THE TEST: 1 TO 3")
sc("""Four. Have you ever moved money between accounts to cover an installment? Five. Have you paid a late fee or
an overdraft fee because of a plan? And six. Would you have bought the last thing you split if you had to
pay the full price today? If you answered yes to the first five, or no to the last one, more than once, the
playbook that follows is for you.""",
   "Person thinking honestly", "THE TEST: 4 TO 6")

# ---------------- Mid ----------------
ch("A quick favor")
pr("""Quick pause. If you just counted how many plans you have running right now, you're not alone.
Subscribe to the channel if this is helping. It's free, and it helps me keep making these videos for you.
Now the playbook.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
pr("""Angle three. The playbook. When buy now, pay later is fine, when it's dangerous, and how to get out.""")
short("The one rule for using buy now, pay later safely")
sc("""Rule one, the golden rule. Only use buy now, pay later for something you could pay for in full today,
with money you already have. If you can afford it now, splitting it is just a timing choice. If you can't,
the plan is a loan you may not be able to repay. This one rule eliminates most of the risk.""",
   "Gold star rule", "RULE 1: COULD I PAY TODAY?")
sc("""Rule two. One plan at a time. Never stack. If you have a plan running, finish it before starting another.
This keeps the total visible and the schedule simple. Rule three. Never for consumables. Food, takeout,
groceries, and everyday items are gone long before the payments end. Paying later for a meal you ate weeks
ago is a sign the budget needs attention, not a payment plan.""",
   "Takeout food containers", "RULES 2 AND 3")
sc("""Rule four. Know the type of plan. Pay in four with no interest is very different from a twelve month
installment loan with interest. Read the APR before you tap. Rule five. Pay from the right account. If
payments come from a debit card, make sure the money will be there on each due date. Many people prefer to
set reminders and pay manually, or pay off early.""",
   "Reading terms on screen", "RULES 4 AND 5")
sc("""Rule six. Turn off the button. Some apps and browsers let you hide or disable payment options, and you
can remove saved accounts. Less temptation at checkout. Rule seven. Keep one list. Every plan, every due
date, every amount, in one place. Review it weekly.""",
   "Settings toggle off", "RULES 6 AND 7")
sc("""Rule eight. If you use it, use it for planned purchases only. Something you budgeted for, at a price you
decided ahead of time. A new fridge when the old one dies, paid in four with no interest, from money you
already set aside, is a reasonable use. An impulse outfit at midnight is not.""",
   "New refrigerator kitchen", "RULE 8: PLANNED ONLY")
card("""The golden rule of buy now, pay later. Only split what you could pay for in full today.""",
     {"type": "stat", "label": "the golden rule", "big": "PAY TODAY?", "size": 190, "sub": "if you couldn't, don't split it"})

ch("How to get out")
pr("""And if you're already juggling several plans, here's how to get out, step by step.""")
sc("""Step one. Stop adding. No new plans until all current ones are finished. Remove saved payment methods
from your shopping apps for now. Step two. Make the list. Open every app, write every remaining payment and
date in one place, and add it up. Knowing the real total is uncomfortable, but it's the turning point.""",
   "Writing list on paper", "STEPS 1 AND 2")
sc("""Step three. Protect the essentials. Rent, utilities, food and transportation come first. If a payment
date clashes with rent, contact the lender before the due date and ask about rescheduling. Many providers
let you move a payment date or offer hardship options. Ask early, not after you've missed it.""",
   "Calling customer support", "STEP 3: PROTECT ESSENTIALS")
sc("""Step four. Clear the smallest plans first, if the costs are similar. Finishing a plan entirely reduces the
number of due dates, which lowers your risk of a missed payment. Any plan that charges interest should move
to the top of the list. Step five. Build a small cushion, even two or three hundred dollars, so a surprise
doesn't push you back to splitting everyday costs.""",
   "Small savings jar", "STEPS 4 AND 5")
sc("""And step six. Look at the bigger picture. If you've been using split payments to cover regular expenses,
the real issue is the gap between income and spending. Use the same tools from my video on why most people
stay broke: find your real number, cut the leaks, and build a starter cushion. The plans are a symptom. The
budget is the cure.""",
   "Notebook budget plan", "STEP 6: THE BIGGER PICTURE")

# ---------------- A month ----------------
ch("One paycheck, many plans")
pr("""Let's walk through one month in the life of someone using several plans, so you can see how quickly it
builds.""")
sc("""Day one. Paycheck arrives, two thousand dollars after taxes for two weeks. Rent comes out, plus the car
payment and the phone bill. About seven hundred dollars is left for everything else. Day three. A forty
dollar installment for sneakers bought last month. Day five. A sixty dollar installment for a jacket. Day
seven. A thirty dollar installment for groceries split two weeks ago.""",
   "Calendar with marked days", "WEEK ONE")
sc("""Day ten. A ninety dollar installment for a new phone accessory bundle and earbuds. Day twelve. A
seventy five dollar installment for concert tickets. Nothing seems big on its own. But by the end of two
weeks, close to three hundred dollars has gone to past purchases. That's three hundred dollars that can't be
used for this week's groceries, gas or savings.""",
   "Phone notifications payments", "WEEK TWO")
sc("""So what happens next? The person splits this week's groceries too, because the account is low. And now
next month has another plan. This is how the loop forms. Past spending crowds out present needs, which
creates new plans, which crowd out future needs. It's the paycheck to paycheck loop, just broken into
smaller pieces.""",
   "Circular arrows loop", "THE LOOP IN SMALL PIECES")
sc("""The way out is the same as any debt loop. Stop the new plans, let the old ones finish, and build even a
small cushion so the next week doesn't depend on splitting. It might take one or two tight months. Then the
money that went to installments is yours again.""",
   "Sunrise over calm water", "BREAKING THE LOOP")

# ---------------- Better options ----------------
ch("Better ways to pay later")
sc("""If what you love about buy now, pay later is spreading out a cost, there are better ways to do it.
The best one is old fashioned: save first. Create a savings bucket for the thing you want and add to it
every payday. When it's full, buy it. You get the same small, regular payments, just before the purchase
instead of after it.""",
   "Savings goal app progress bar", "PAY FIRST, BUY LATER")
sc("""Saving first has three advantages. No risk of late fees or credit damage. Time to change your mind,
because many things you want today, you won't want in six weeks. And sometimes, while you save, the price
drops, or a better option appears. Saving first turns impulse purchases into planned ones.""",
   "Price drop tag", "TIME TO CHANGE YOUR MIND")
sc("""For bigger necessary costs, plan with sinking funds, like we covered in other videos. A little each month
for car repairs, holidays, appliances and medical costs. When the expense comes, it's already paid. And if
you truly need to borrow, compare the total cost of a buy now, pay later plan with options like a credit
union loan, and pick the cheapest one you can comfortably repay.""",
   "Labeled envelopes savings", "SINKING FUNDS")

# ---------------- Stories ----------------
ch("Two shoppers")
short("Same shopping habits, very different endings")
sc("""Let's see two shoppers. Emma, twenty four, used buy now, pay later for almost everything. Shoes, a
jacket, a phone, a weekend trip, even groceries a few times. Each plan seemed small. Then one month,
her hours at work were cut. Suddenly she had about four hundred dollars of installments due within two
weeks, and not enough in her account.""",
   "Young woman stressed looking at phone", "EMMA: THE STACK")
sc("""One payment bounced, leading to a late fee from the lender and an overdraft fee from her bank. She
started using her credit card to cover the next installments, which added interest. It took her about five
months, a second job on weekends, and a lot of stress to get out. Looking back, no single purchase was the
problem. The stack was.""",
   "Woman working weekend cafe job", "THE STACK WAS THE PROBLEM")
sc("""Now Chris, twenty nine. He uses buy now, pay later once or twice a year, only for planned purchases he
could pay for in full, like a new laptop for work. He chooses zero interest plans, pays from an account
with a cushion, and often pays off early. For him, it's a free short term loan, and the merchant pays the
cost.""",
   "Man working on new laptop", "CHRIS: THE PLANNER")
sc("""Same product. Two completely different outcomes. Chris uses buy now, pay later as a tool. Emma used it as
a budget. The difference wasn't income, or intelligence. It was one rule. Only split what you could pay
for today.""",
   "Two paths in park", "A TOOL, NOT A BUDGET")

# ---------------- FAQ ----------------
ch("Questions people ask")
pr("""Let me answer the questions people ask me most about buy now, pay later.""")
sc("""Question one. Does buy now, pay later affect my credit score? It depends on the provider and the plan.
Some don't report short plans at all, some report certain loans, and some report missed payments or send
them to collections. And reporting practices are changing, as credit bureaus and scoring companies add
these loans. The safest approach is to assume a missed payment can hurt your credit.""",
   "Credit score dial", "DOES IT AFFECT CREDIT?")
sc("""Question two. Is it better than a credit card? If you'd otherwise carry a credit card balance at twenty
percent, a true zero interest plan that you pay on time can cost less. But credit cards offer a single
statement, a clear total, and often stronger purchase protections. And a card paid in full each month is
also interest free. For people who pay cards in full, buy now, pay later adds little.""",
   "Credit card and phone side by side", "BETTER THAN A CARD?")
sc("""Question three. What about returns? Returns can get complicated. If you return an item, you usually need
to make sure the store processes the refund and the lender updates the plan. Until that happens, payments
may continue. Keep receipts and check the app to make sure the plan is canceled or adjusted.""",
   "Returning package to store", "WHAT ABOUT RETURNS?")
sc("""Question four. Is it okay for big necessary purchases? Sometimes. If your washing machine breaks and you
have the money but want to keep your cushion intact a bit longer, a zero interest plan can be reasonable. If
the plan charges interest, compare it with other options, like a credit union loan, and choose the
cheapest.""",
   "Broken washing machine", "FOR BIG NECESSITIES?")
sc("""Question five. What's the biggest warning sign? Using buy now, pay later for everyday spending like
groceries, gas or takeout. When basic costs need to be split, the budget is already under strain. That's
the moment to pause new plans and look at the bigger picture.""",
   "Grocery checkout line", "THE BIGGEST WARNING SIGN")
sc("""Question seven. Can buy now, pay later help build credit? Possibly, as more lenders report on time
payments and scoring models start counting them. But it's a slow and uncertain way to build credit, and
missed payments can hurt. A simpler path for most people is a basic credit card used for a small regular
bill, paid in full every month on autopay.""",
   "Credit building concept", "CAN IT BUILD CREDIT?")
sc("""Question eight. What if a payment fails because my account is empty? Contact the provider right away.
Many will let you retry or reschedule the payment, and acting quickly can reduce fees and keep it from
being reported. Then move the remaining due dates into your calendar, and make sure the money is there
for each one before you buy anything else.""",
   "Bank account low balance", "WHAT IF A PAYMENT FAILS?")
sc("""And question six. How do I talk to my teenager or young adult about it? Show them the math with real
examples. Add up a typical month of split payments. Explain that it's a loan, even if the app looks
friendly. And share the golden rule. Many young people have never had anyone explain it, and a ten minute
conversation can save them years of stress.""",
   "Parent and teenager talking", "TALKING TO YOUNG ADULTS")

sc("""One last thought before the recap. Buy now, pay later isn't evil, and the people who use it aren't
foolish. It's a well designed product that solves a real problem, wanting something now and paying
gradually. The danger is that it solves that problem by borrowing from your future self, a little at a
time, in a way that's easy to miss. Your future self deserves a say. Give them one by checking the total
before you tap.""",
   "Person looking in mirror", "ASK YOUR FUTURE SELF")

# ---------------- Recap ----------------
ch("Recap")
short("Buy now, pay later: what nobody tells you")
sc("""Quick recap. The numbers: buy now, pay later grew more than tenfold in two years, merchants pay because it
makes people spend more, late fees and longer interest bearing plans add real costs, many users stack loans
across several apps, and the debt is often invisible to other lenders.""",
   "Checklist clipboard", "THE NUMBERS")
sc("""The psychology: the smaller number wins, it doesn't feel like debt, less pain of paying, bigger carts,
instant approval, social normalization and losing track across apps.""",
   "Brain thinking illustration", "THE PSYCHOLOGY")
sc("""And the playbook: only split what you could pay today, one plan at a time, never for consumables, know
the plan type, pay from the right account, turn off the button, keep one list, and use it only for planned
purchases. If you're stacked, stop adding, list everything, protect essentials, clear plans one by one,
and fix the bigger budget.""",
   "Organized desk planner", "THE PLAYBOOK")

# ---------------- Close ----------------
ch("What to do next")
pr("""If you want the full plan for getting out of every kind of debt, and building wealth after, it's in my
playbook. The link is in the description. And watch my video on how credit card companies make money from
you. It's the other half of this story. I'm Ryan Rover. See you in the next one.""")

save("video46", "Buy Now, Pay Later: The Quiet Debt Trap Nobody Talks About", [
    "Consumer Financial Protection Bureau, Buy Now, Pay Later: Market Trends and Consumer Impacts (2022): loans from five lenders grew from about $2 billion (2019) to over $24 billion (2021)",
    "Consumer Financial Protection Bureau, Consumer Use of Buy Now, Pay Later and Other Unsecured Debt (2025): about 63% of borrowers had multiple simultaneous loans; about a third used multiple lenders; users more likely to carry other debt",
    "Federal Reserve, Economic Well-Being of U.S. Households (SHED): BNPL use and late payments",
    "Research on partitioned pricing and the pain of paying",
    "Payment totals: stated illustrative math",
], "buy now pay later: numbers, psychology, playbook")
