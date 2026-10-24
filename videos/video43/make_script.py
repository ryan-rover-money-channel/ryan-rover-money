import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

def item(n, title, sub, card_text, body, example, extra, q1, c1, q2, c2, q3, c3):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"WAY {n}")
    sc(body, q1, c1)
    sc(example, q2, c2)
    sc(extra, q3, c3)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Here's a question most people never ask. Your credit card gives you rewards, a
free app, fraud protection, sometimes even airport lounges. So who's paying for all of that? Because the
card company isn't a charity. Today, we follow the money, and we find out exactly how credit card
companies make money from you.""")
short("Who really pays for your credit card rewards?")
card("""In twenty twenty two, according to the Consumer Financial Protection Bureau, credit card companies
charged Americans more than one hundred billion dollars in interest, plus around twenty five billion
dollars in fees.""",
     {"type": "compare", "left": {"label": "Interest", "big": "$100B+", "sub": "charged in 2022"},
      "right": {"label": "Fees", "big": "~$25B", "sub": "charged in 2022"},
      "note": "Source: Consumer Financial Protection Bureau"})
sc("""That's not a typo. More than one hundred billion dollars in a single year, just in interest. And that's
before we count the money merchants pay every time you swipe. Credit cards are one of the most
profitable products in banking. Once you understand how that profit is made, you can use cards for their
benefits while paying almost nothing.""",
   "Bank skyscraper city", "ONE OF BANKING'S BEST BUSINESSES")
sc("""We'll look at it from three angles. First, the numbers: the eight main ways card companies earn
money, and how much each one costs you. Second, the psychology: the design tricks that make you spend
more and pay longer. And third, the playbook: how to flip the deal so the card works for you, not the
other way around.""",
   "Magnifying glass over credit card", "FOLLOW THE MONEY")
pr("""By the end, you'll know whether your card is a tool or a trap. Let's start with the money.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Every number in this video comes from a named source. Interest and fee totals come from the Consumer
Financial Protection Bureau's reports on the credit card market. Interest rates come from the Federal
Reserve. Research on card payments comes from the Federal Reserve Bank of Boston. Where I show an example,
it's stated, simple math. Card terms vary, so always read your own agreement. This is education, not
financial advice.""",
   "Consumer Financial Protection Bureau building", "OUR SOURCES")

# ---------------- History ----------------
ch("How we got here")
pr("""Before the numbers, a quick story. Because to understand why cards work the way they do, it helps to
know how they started.""")
sc("""In nineteen fifty, a company called Diners Club launched a card that let members pay at a group of
restaurants in New York and settle up later. It was a charge card. You paid the full bill each month. The
business made money mainly from the restaurants, which paid a fee on every meal. That idea, that the
merchant pays to accept the card, is still at the center of the system today.""",
   "Vintage restaurant nineteen fifties", "1950: DINERS CLUB")
sc("""In the late nineteen fifties, Bank of America took the idea further. In Fresno, California, it mailed
tens of thousands of unsolicited credit cards to residents, a famous experiment known as the Fresno drop.
These cards let people carry a balance and pay over time, with interest. Losses from fraud and unpaid
balances were large at first, but the model eventually became BankAmericard, which later became Visa.""",
   "Fresno California historic", "THE FRESNO DROP")
sc("""Then came a turning point. In nineteen seventy eight, a Supreme Court decision known as the Marquette
case allowed national banks to charge the interest rate allowed in their home state to customers
nationwide. Some states soon loosened their interest rate limits to attract card businesses. That's a big
part of why so many card companies are based in states like South Dakota and Delaware, and why card rates
can be so high.""",
   "United States Supreme Court building", "1978: THE MARQUETTE CASE")
sc("""Fast forward to two thousand nine. After the financial crisis, Congress passed the Credit CARD Act. It
limited surprise rate increases on existing balances, required clearer statements, including the minimum
payment warning, and restricted certain fees. It made cards fairer. But it didn't change the core business.
Interest from people who carry balances, and fees from merchants on every swipe.""",
   "United States Capitol building", "2009: THE CARD ACT")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The eight main ways card companies make money. Some you know. A few you probably don't.""")

item(1, "Interest", "the biggest money maker",
"""Way number one. Interest. By far the biggest money maker.""",
"""When you don't pay your full statement balance by the due date, the card charges interest on what's
left. According to the Federal Reserve, the average rate on card accounts that were charged interest has
been above twenty percent in recent years. That's higher than almost any other common type of consumer
loan.""",
"""Here's what that means. Carry a three thousand dollar balance all year at twenty two percent, and you
pay roughly six hundred sixty dollars in interest. That's six hundred sixty dollars that buys nothing.
Inside the industry, people who carry a balance are often called revolvers. They're the most profitable
customers a card company has.""",
"""There's a quiet detail most people miss. Card interest usually compounds daily. The card takes your
yearly rate, divides it by three hundred sixty five, and applies it to your balance each day. Interest
gets added to the balance, and tomorrow's interest is charged on that bigger number. It's the same
compounding that grows investments, but working against you. Try this: find the APR on your statement
right now. If you don't know it, that's the first problem.""",
"Credit card statement close up", "20%+ A YEAR",
"Calculator interest", "~$660 FOR NOTHING",
"Calendar daily pages", "COMPOUNDED DAILY")

item(2, "Swipe fees", "the merchant pays, then you do",
"""Way number two. Swipe fees, also called interchange fees.""",
"""Every time you pay with a card, the store pays a fee, often somewhere around two percent of the purchase,
sometimes more for premium rewards cards. Part goes to the bank that issued your card, part to the
network and the processor. Across the whole country, merchants pay well over one hundred billion dollars a
year in card processing fees.""",
"""You might think, great, the store pays, not me. But stores build those costs into their prices. That
means everyone pays a little more, including people who pay with cash or debit. Researchers at the
Federal Reserve Bank of Boston studied this and found that, on average, cash users end up subsidizing
card users, especially those with rewards cards.""",
"""This is how rewards are funded. That two percent cash back isn't free money from the bank. It's largely
recycled from swipe fees, which come from higher prices for everyone. If you pay in full, you can come out
ahead. If you carry a balance, the interest you pay can wipe out every reward many times over. Try this:
compare your rewards earned this year with the interest you paid. Be honest about which is bigger.""",
"Card payment terminal store", "~2% PER SWIPE",
"Cash register store checkout", "EVERYONE PAYS A LITTLE",
"Cash back rewards", "WHERE REWARDS COME FROM")

item(3, "Late fees", "billions a year",
"""Way number three. Late fees.""",
"""Miss a due date, even by a day, and many cards charge a late fee that can be around thirty dollars or
more. The Consumer Financial Protection Bureau estimated that card companies charged roughly fourteen
billion dollars in late fees in twenty twenty two alone. That's a lot of forgotten due dates.""",
"""Late fees often don't come alone. A late payment can trigger a higher penalty interest rate, cancel a
promotional rate, and, if it's thirty days late or more, show up on your credit report. One forgotten
payment can cost the fee, months of higher interest and a lower score.""",
"""Card companies don't need you to be irresponsible. They just need you to be human. Busy weeks, a
changed due date, a payment that didn't go through. The easiest defense is automation. Try this: set
autopay for at least the minimum on every card, so you're never late, then pay the rest manually or set
autopay to the full balance.""",
"Calendar missed due date", "~$14 BILLION IN LATE FEES",
"Stressed person with bills", "ONE MISS, MANY COSTS",
"Autopay settings phone", "NEVER BE LATE")

item(4, "Annual fees", "paying to pay",
"""Way number four. Annual fees.""",
"""Many basic cards have no annual fee. But premium travel and rewards cards can charge from under one
hundred dollars to several hundred dollars a year. In exchange, they offer bigger rewards, travel
credits and perks. For the card company, the annual fee is steady, predictable income, paid whether you
use the card or not.""",
"""The perks are real, but only if you actually use them. A five hundred dollar card with a three hundred
dollar travel credit is only worth it if you'd have spent that three hundred on travel anyway, and the
rest of the perks matter to you. Many people pay for benefits they forget to claim.""",
"""Card companies count on something called breakage, benefits that people are entitled to but never
use. Unused credits, expired points, lounge passes that sit in an app. Every unused perk is profit. Try
this: list every benefit of your fee card and what you actually used last year. If the total is less than
the fee, ask for a no fee version, or a retention offer, before your renewal date.""",
"Premium metal credit card", "PAYING TO PAY",
"Airport lounge", "PERKS YOU USE",
"Unused gift cards drawer", "BREAKAGE")

item(5, "Balance transfer fees", "0% isn't free",
"""Way number five. Balance transfer fees.""",
"""Balance transfer offers sound like a gift. Move your debt to a new card at zero percent interest for a
year or more. But most charge a fee, commonly around three to five percent of the amount you move. Move
ten thousand dollars at a three percent fee, and you pay three hundred dollars up front.""",
"""That can still be a great deal compared with paying twenty two percent interest. The trap is what
happens next. If the balance isn't paid off when the promotion ends, the regular rate kicks in. And many
people, relieved by the zero percent, keep using the old card too. Now they have two balances.""",
"""Card companies know a share of people won't finish in time. That's part of why the offers exist. Used
with a plan, a balance transfer can save you a lot. Used as relief, it just delays the problem. Try this:
before transferring, divide the balance by the number of promotional months. If you can't pay that
amount every month, the offer probably won't solve your problem.""",
"Bank transfer arrows", "3-5% UP FRONT",
"Two credit cards side by side", "NOW TWO BALANCES",
"Calendar countdown", "DIVIDE BY THE MONTHS")

item(6, "Cash advances", "the most expensive cash",
"""Way number six. Cash advances.""",
"""Using your credit card to get cash from an ATM is called a cash advance, and it's usually one of the most
expensive ways to borrow. There's often an upfront fee, commonly around five percent or a minimum dollar
amount. The interest rate is often higher than your purchase rate. And there's usually no grace period,
so interest starts the day you take the cash.""",
"""Take five hundred dollars in a cash advance, and you might pay a twenty five dollar fee right away,
plus interest at a higher rate from day one. Some things also count as cash advances without looking like
one, like some money transfers, buying certain gambling chips, or some purchases that are treated like cash.
Check your card's terms.""",
"""People usually take cash advances when they're already stressed, which is why they're so profitable.
The real fix is upstream: a small emergency fund so you never need one. Try this: ask your bank to lower
or turn off the cash advance limit on your card. It removes the option on your worst day.""",
"ATM machine cash withdrawal", "THE MOST EXPENSIVE CASH",
"Casino chips table", "HIDDEN CASH ADVANCES",
"Emergency fund jar", "TURN IT OFF")

item(7, "Foreign transaction fees", "a tax on travel",
"""Way number seven. Foreign transaction fees.""",
"""Many cards charge a fee, often around three percent, on purchases made in another currency or processed
by a foreign bank. That includes buying something online from an overseas store, even if you never leave
home. Spend two thousand dollars on a trip abroad, and that's about sixty dollars in fees.""",
"""There's a related trap at the register abroad. Sometimes the card machine asks if you want to pay in
dollars instead of the local currency. It sounds convenient. But that conversion, called dynamic currency
conversion, often uses a worse exchange rate set by the merchant's processor.""",
"""Many cards, especially travel cards, don't charge foreign transaction fees at all. So this one is easy to
avoid if you check before you go. Try this: before your next trip or international online order, look up
your card's foreign fee. And at foreign terminals, generally choose to pay in the local currency.""",
"Airport departures board", "~3% ON FOREIGN PURCHASES",
"Card terminal currency choice", "PAY IN LOCAL CURRENCY",
"Passport and credit card", "CHECK BEFORE YOU GO")

item(8, "Penalty rates", "one slip, higher rate",
"""Way number eight. Penalty APRs.""",
"""Many cards have a penalty rate, a much higher interest rate that can apply after you pay late, often if
you're sixty days or more behind. Penalty rates on some cards approach thirty percent. Federal rules
under the Credit CARD Act of two thousand nine limit when and how these can be applied, and require the
issuer to review it later, but it can still be very expensive while it lasts.""",
"""Picture a five thousand dollar balance moving from twenty two percent to nearly thirty percent. That's
roughly four hundred dollars more in interest per year, on top of late fees. It's the card company's way
of charging more to customers it now considers riskier. And riskier customers who keep paying are very
profitable.""",
"""The good news: penalty rates are entirely avoidable. Pay at least the minimum, on time, every month. If
you're struggling, call the issuer before you miss a payment. Many have hardship programs that can lower
your rate or payment temporarily. Try this: save your card issuer's phone number in your contacts, under
call before I'm late.""",
"Warning sign red", "UP TO ~30%",
"Phone call customer service", "CALL BEFORE YOU'RE LATE",
"Contacts list on phone", "SAVE THE NUMBER")

sc("""So that's the money side. Interest, swipe fees, late fees, annual fees, balance transfer fees, cash
advances, foreign fees and penalty rates. Notice something. Almost every one of them is avoidable. People
who pay in full, on time, at home, pay close to nothing, and still collect rewards. People who carry a
balance and slip up now and then fund the whole system.""",
   "Two paths diverging road", "WHO FUNDS THE SYSTEM")
card("""Here's the contrast in a single picture. A cardholder who pays in full can earn rewards and pay no
interest. A cardholder who carries three thousand dollars at twenty two percent pays roughly six hundred
sixty dollars a year.""",
     {"type": "compare", "left": {"label": "Carries $3,000", "big": "-$660", "sub": "interest a year at 22%"},
      "right": {"label": "Pays in full", "big": "$0", "sub": "interest, plus rewards"},
      "note": "Illustration. Your card's terms will differ."})
pr("""Now the part the card companies really don't advertise. How the product is designed to change your
behavior.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
pr("""Angle two. The psychology. Five design tricks that keep you spending more and paying longer.""")
short("The minimum payment is designed to keep you in debt")

item(9, "The minimum payment anchor", "the smallest number wins",
"""Way number nine. The minimum payment anchor.""",
"""Your statement shows several numbers: the full balance, and a much smaller minimum payment. Research by
psychologist Neil Stewart found that showing the minimum payment can act as an anchor, a number your brain
latches onto. In his experiments, people who saw a minimum payment tended to choose to repay less than
people who didn't see one.""",
"""The minimum is often calculated as a small percent of the balance plus interest. It's designed to keep
your account in good standing, not to get you out of debt. At the minimum, a balance of a few thousand
dollars can take many years to clear, and the total interest can approach or even exceed what you
originally spent.""",
"""Since the Credit CARD Act, statements must show how long it would take to pay off your balance making
only minimum payments, and how much you'd pay in total. Most people skip that box. Try this: find it on
your next statement and read it out loud. Then choose a fixed monthly payment that clears the balance in
the time you want, and set it as your autopay.""",
"Price tag anchor", "THE ANCHOR",
"Long road to horizon", "YEARS AT THE MINIMUM",
"Statement warning box", "READ THE BOX")

item(10, "Rewards that make you spend", "points feel like free money",
"""Way number ten. Rewards that change how you spend.""",
"""Points, miles and cash back feel like free money. And that feeling changes behavior. People may choose a
card purchase over cash to earn points, spend a bit more to hit a bonus, or book a hotel they didn't need
to keep a status level. The reward is small. The extra spending can be large.""",
"""Sign up bonuses are the clearest example. Spend four thousand dollars in three months, get a big bonus.
If you were going to spend that anyway, great. If the bonus makes you buy things to reach the target,
the card company just turned a reward into new spending, and possibly new interest.""",
"""Rewards also use gamification. Progress bars, status tiers, limited time offers, all designed to keep you
engaged. Try this: treat rewards as a discount on spending you already planned, never as a reason to
spend. And if you ever carry a balance, forget rewards completely and focus on the interest rate.""",
"Airline miles rewards", "POINTS FEEL FREE",
"Shopping bags spree", "SPENDING FOR THE BONUS",
"Progress bar on phone app", "GAMIFIED SPENDING")

item(11, "Deferred interest", "the zero percent trap",
"""Way number eleven. Deferred interest promotions.""",
"""You've seen it at furniture and electronics stores. No interest if paid in full in twelve months. That
wording matters. With many of these store card offers, if you don't pay the entire balance by the deadline,
interest is charged back to the original purchase date, on the full amount, not just what's left.""",
"""Say you buy a two thousand dollar couch on a twelve month deferred interest plan at twenty six percent,
and you've paid it down to two hundred dollars when the year ends. On many of these plans, you could be
charged roughly a year of interest on the full two thousand, potentially hundreds of dollars, all at once.
The Consumer Financial Protection Bureau has warned consumers about exactly this.""",
"""This is different from a true zero percent APR card, where interest only starts on the remaining balance
after the promotion. The words if paid in full are the warning sign. Try this: if you use a deferred
interest offer, divide the price by the months, minus one, and pay that amount every month so you finish
early.""",
"Furniture store showroom", "IF PAID IN FULL",
"Couch living room", "INTEREST FROM DAY ONE",
"Fine print magnifying glass", "READ THE WORDS")

item(12, "Credit limit increases", "more room to spend",
"""Way number twelve. Automatic credit limit increases.""",
"""Card companies often raise your limit over time, sometimes without you asking. It feels like a
compliment. You've been trusted with more. And a higher limit can actually help your score, by lowering how
much of your available credit you're using.""",
"""But for some people, a higher limit simply becomes more room to spend. Research on consumer behavior has
suggested that people often treat available credit as part of what they can afford. If you were already
carrying a balance, a higher limit can mean a higher balance, and more interest.""",
"""The key is knowing which type of person you are. If you pay in full every month, a higher limit is
mostly a benefit. If you carry a balance, it's a risk. Try this: if limit increases tempt you, call and
ask to keep your limit where it is, or set your own spending alert well below it.""",
"Credit limit increase notification", "MORE ROOM",
"Shopping cart full", "AVAILABLE CREDIT ISN'T INCOME",
"Spending alert phone", "SET YOUR OWN LIMIT")

item(13, "Painless payments", "no friction, more spending",
"""Way number thirteen. Making payment painless.""",
"""Paying with cash makes you feel the money leave. Researchers call that the pain of paying. Cards reduce
that pain, and studies have suggested people may spend more when paying by card. Tap to pay, phone wallets
and one click checkouts reduce it even further. Less pain, more spending.""",
"""Card companies and retailers work hard to remove friction. Saved cards in every app. Approval in a
second. No signature. Each step makes buying easier, which is great for convenience, and great for
spending. Convenience is the product, and your spending is the result.""",
"""You don't have to give up convenience. You just need to add one deliberate pause. Try this: remove saved
cards from shopping sites and apps you use for impulse buys. Keep them only for bills and essentials.
That small pause is often enough to ask, do I actually want this?""",
"Phone tap to pay terminal", "NO PAIN, MORE SPENDING",
"One click checkout button", "FRICTION REMOVED",
"Hand pausing over button", "ADD ONE PAUSE")

# ---------------- Life cycle ----------------
ch("The customer journey they plan for")
pr("""Here's something worth knowing. Card companies think about you as a journey, from the first offer to
the last payment. Let me walk you through it.""")
sc("""It starts with acquisition. Mail offers, app pop ups, and sign up bonuses at checkout. Card companies
spend heavily to win new customers, because a good customer can be profitable for many years. That's why
so many offers arrive in your mailbox, and why the bonus is so big. They expect to earn it back.""",
   "Mailbox full of letters", "STAGE 1: THE OFFER")
sc("""Next comes activation and habit. The goal is to make the card your default. Put it in your phone
wallet. Save it in your favorite apps. Earn extra points in your most common category. Once a card is the
one you reach for without thinking, it tends to stay there for years.""",
   "Phone wallet with cards", "STAGE 2: THE HABIT")
sc("""Then the profitable stage. If you carry a balance, interest flows every month. If you pay in full,
swipe fees still flow. Limit increases, balance transfer offers and new promotions keep you engaged. And
finally, retention. If you call to cancel, many issuers will offer bonus points, a waived fee or a lower
rate to keep you. Which tells you something useful. Your business is worth more to them than you think.""",
   "Customer service call center", "STAGES 3 AND 4: PROFIT AND RETENTION")
sc("""Knowing this journey gives you leverage. You can take the sign up bonus on spending you'd do anyway.
You can choose which card becomes your default. You can call before your annual fee posts and ask for a
retention offer. And you can walk away if the deal stops working for you. You're the customer. Act like
one.""",
   "Confident person walking city", "USE YOUR LEVERAGE")

# ---------------- Mid ----------------
ch("A quick favor")
pr("""Quick pause. If you just realized your card has been making money off you, subscribe to the channel.
It's free, and it helps me make more videos like this one. Now, let's flip the deal.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
pr("""Angle three. The playbook. Ten rules that make your card company earn almost nothing from you, while you
keep the benefits.""")
short("10 rules so your credit card makes $0 from you")
sc("""Rule one. Pay the full statement balance every month. This single habit removes the biggest source of
card profit, interest. Most cards give you a grace period, so if you pay the full statement balance by the
due date, new purchases don't get charged interest at all.""",
   "Paid in full stamp", "RULE 1: PAY IN FULL")
sc("""Rule two. Turn on autopay. At least the minimum, ideally the full balance. You'll never pay a late fee or
trigger a penalty rate again. Rule three. Know your APR. Write it down. If you ever carry a balance, that's
the number that matters, not the rewards.""",
   "Autopay toggle smartphone", "RULES 2 AND 3")
sc("""Rule four. If you carry a balance, attack it before anything else except a small emergency fund. Paying
off a card at twenty two percent is a guaranteed twenty two percent return. Few investments can match that
reliably. Rule five. Use balance transfers only with a written plan to finish before the promotion ends.""",
   "Debt payoff chart", "RULES 4 AND 5")
card("""Here's why rule four matters. A three thousand dollar balance at twenty two percent. Paying only around
the minimum can take many years. Paying a fixed three hundred dollars a month clears it in about twelve
months.""",
     {"type": "compare", "left": {"label": "Near minimum", "big": "Years", "sub": "interest keeps piling up"},
      "right": {"label": "$300 a month", "big": "~12 months", "sub": "about $350 interest"},
      "note": "Illustration at 22% APR, compounded monthly."})
sc("""Rule six. Never take a cash advance. Ask your issuer to lower or remove the cash limit if you can. Rule
seven. Avoid deferred interest offers unless you'll pay them off early, with a fixed monthly amount set from
day one.""",
   "Store credit card offer", "RULES 6 AND 7")
sc("""Rule eight. Match the card to your life. If you don't travel, you may not need a travel card with an
annual fee. If you travel abroad, pick a card with no foreign transaction fee. A simple no fee card with
flat cash back is the right answer for many people.""",
   "Choosing between cards", "RULE 8: MATCH YOUR LIFE")
sc("""Rule nine. Treat rewards as a discount, not a goal. Never spend to earn points. And once a year, add up
what you earned and what you paid in fees and interest. If the second number is bigger, the card is
winning. Rule ten. Read your statement every month. It takes five minutes, catches fraud and errors, and
keeps you out of the ostrich effect.""",
   "Reading statement with coffee", "RULES 9 AND 10")
pr("""Do these ten things, and you become what the industry sometimes calls a transactor. Someone who uses the
card for convenience and pays in full. You still get the protection and rewards. And the card company
earns mostly from the swipe fees, not from you directly.""")

# ---------------- Statement ----------------
ch("Reading your statement like an insider")
pr("""Now, let's read a credit card statement the way the card company does. Five numbers matter.""")
sc("""Number one, the statement balance. That's what you owe for the last billing cycle. Pay this full
amount by the due date, and on most cards you won't pay interest on purchases. Number two, the current
balance. That includes new purchases made after the statement closed. You don't have to pay those yet to
avoid interest, but you can.""",
   "Credit card statement document", "STATEMENT VS CURRENT")
sc("""Number three, the minimum payment. As we saw, this is the anchor. Paying only this keeps your account in
good standing, but keeps the interest flowing. Number four, the due date. Miss it, and fees and possibly a
penalty rate follow. Number five, the APR. Often there are several: one for purchases, one for balance
transfers, one for cash advances, and a penalty rate.""",
   "Highlighted numbers on paper", "MINIMUM, DUE DATE, APR")
sc("""And then there's the box most people skip, the minimum payment warning. It shows how long it would take
to pay off your balance with minimum payments only, and the total cost. It also shows what you'd need to
pay each month to clear it in three years. That second number is often a much better target than the
minimum. Try this: use the three year number as your new minimum.""",
   "Warning box on statement", "THE THREE YEAR NUMBER")
sc("""One more line worth checking every month is the interest charged. If that line shows anything other
than zero, you're paying for the privilege of borrowing. Seeing that number in black and white, month
after month, is often what finally pushes people to change. Circle it. Write it on a sticky note. Make
it visible until it reaches zero.""",
   "Sticky note on monitor", "CIRCLE THE INTEREST LINE")

# ---------------- Stories ----------------
ch("Two cardholders, same card")
short("Same credit card, two very different results")
sc("""Let's make it real with two people holding the exact same rewards card, with two percent cash back and
a twenty two percent APR. Alex spends about two thousand dollars a month on the card, and pays it off
completely every month on autopay.""",
   "Young man with phone and card", "ALEX: THE TRANSACTOR")
sc("""Over a year, Alex earns roughly four hundred eighty dollars in cash back. He pays no interest, no late
fees, and no annual fee. The card company still makes money from Alex, through swipe fees paid by
merchants, but Alex comes out ahead. For him, the card is a tool.""",
   "Cash back reward notification", "+$480 A YEAR")
sc("""Now Jordan. Same card, same spending. But Jordan pays only part of each bill, and carries an average
balance of around six thousand dollars. Twice a year, Jordan forgets a payment and gets a late fee.""",
   "Woman stressed with bills at desk", "JORDAN: THE REVOLVER")
sc("""Jordan also earns around four hundred eighty dollars in cash back. But on a six thousand dollar average
balance at twenty two percent, Jordan pays roughly thirteen hundred dollars a year in interest, plus about
sixty dollars in late fees. Net result, Jordan loses roughly nine hundred dollars a year. Same card. Same
rewards. Opposite outcomes.""",
   "Money flying away illustration", "-$900 A YEAR")
card("""Same card, same spending, same rewards. The only difference is paying in full.""",
     {"type": "compare", "left": {"label": "Jordan, revolver", "big": "-$900", "sub": "a year, after rewards"},
      "right": {"label": "Alex, transactor", "big": "+$480", "sub": "a year in cash back"},
      "note": "Illustration at 22% APR and 2% cash back."})
sc("""And here's the twist. Jordan's interest helps pay for the system that funds Alex's rewards. That's the
quiet truth of credit cards. The people who pay in full are, in a way, subsidized by the people who don't.
The goal of this video is to move you from Jordan's side to Alex's.""",
   "Seesaw balance playground", "WHO SUBSIDIZES WHOM")

# ---------------- Premium math ----------------
ch("When a fancy card is worth it")
sc("""Let's do the honest math on premium cards, because they're everywhere. Imagine a card with a five
hundred fifty dollar annual fee. It offers a three hundred dollar travel credit, airport lounge access, and
three points per dollar on travel and dining. Is it worth it? It depends entirely on how you live.""",
   "Premium travel credit card", "THE $550 QUESTION")
sc("""If you travel several times a year, use the full travel credit on trips you'd take anyway, and value
the lounge, the math can work. Say you spend ten thousand dollars a year on travel and dining. At three
points per dollar, that's thirty thousand points. Depending on how you redeem them, that might be worth
around three hundred to four hundred fifty dollars. Add the credit, and you may come out ahead.""",
   "Traveler at airport gate", "WHEN IT WORKS")
sc("""But if you travel once a year, forget to use the credit, and rarely visit lounges, the same card can
cost you hundreds of dollars a year for benefits you never touch. A simple no fee card with two percent
cash back might leave you better off. The card company is betting you'll be the second person, and many
people are.""",
   "Empty airport lounge chairs", "WHEN IT DOESN'T")
sc("""A simple rule. Only pay an annual fee if the benefits you actually used last year, in dollars, clearly
beat the fee. And never, ever, pay an annual fee on a card where you carry a balance. At that point, you're
paying twice. Once for the card, and once for the interest.""",
   "Calculator comparing numbers", "BENEFITS USED VS FEE")

# ---------------- FAQ ----------------
ch("Questions people ask")
pr("""Let me answer the questions people ask me most about credit cards.""")
sc("""Question one. Should I just cut up all my cards? If cards consistently lead you into debt, using debit
or cash for a while can be a smart reset. But if you can pay in full, cards offer real advantages, like
stronger fraud protection than many debit cards, and building credit history. The card isn't the enemy.
Carrying a balance is.""",
   "Scissors and credit card", "CUT THEM UP?")
sc("""Question two. Can I negotiate my interest rate? Often, yes, especially if you've paid on time for a
while. Call, ask politely for a lower APR, and mention competing offers if you have them. It doesn't always
work, but it costs a five minute call. Even a few percentage points can save real money on a balance.""",
   "Person on phone call smiling", "NEGOTIATE YOUR RATE")
sc("""Question three. Does paying in full hurt my credit because the bank doesn't make money? No. Your credit
score is based on things like paying on time and how much of your limit you use, not on how much interest
you pay. Paying in full every month is one of the best things you can do for your score.""",
   "Credit score gauge", "DOES PAYING IN FULL HURT?")
sc("""Question four. When is the best time to pay? At minimum, by the due date. But your balance on the
statement closing date is often what's reported to the credit bureaus. If you want a lower reported
balance, paying before the statement closes can help. Either way, never pay late.""",
   "Calendar with dates circled", "WHEN TO PAY")
sc("""Question five. Are store cards ever worth it? Sometimes, if you shop at that store often and pay in
full. But store cards often have higher interest rates and deferred interest promotions. For most people,
a general card with simple rewards works better.""",
   "Department store entrance", "STORE CARDS?")
sc("""Question seven. Do card companies make money even if I pay in full? Yes, mainly through swipe fees
paid by merchants, and sometimes through annual fees. That's why they're still happy to have you. But
they make far less from you than from someone who carries a balance, and that's exactly the position you
want to be in.""",
   "Store owner at register", "IF I PAY IN FULL?")
sc("""And question six. What if I'm already deep in card debt? Start with a small emergency fund so new
surprises don't add debt. Stop using the cards for now. List every balance and rate, and choose a payoff
method. Call your issuers and ask about lower rates or hardship programs. And if you feel overwhelmed, look
for a nonprofit credit counseling agency. Many offer free or low cost help.""",
   "Person planning with notebook", "ALREADY IN DEBT?")

ch("Five warning signs")
sc("""Before we go, five warning signs that your card is using you, instead of the other way around. One.
You don't know your APR. Two. You've paid interest in three or more of the last twelve months. Three. You
use one card to pay another, or take cash advances to cover bills.""",
   "Warning road sign", "WARNING SIGNS 1 TO 3")
sc("""Four. You pick purchases to earn points or hit a bonus. And five. You feel a little relief when the
minimum payment is small. If two or more of these sound familiar, it's time to run the playbook. Start with
rule one this month: aim to pay the full statement balance, and if you can't yet, pick a fixed payment that
clears it on a date you choose. Then put that date on your calendar and celebrate it when it comes.""",
   "Calendar with goal date circled", "WARNING SIGNS 4 AND 5")

# ---------------- Recap ----------------
ch("Recap")
short("8 ways credit card companies make money from you")
sc("""Quick recap. Credit card companies make money through interest, swipe fees, late fees, annual fees,
balance transfer fees, cash advances, foreign transaction fees and penalty rates. More than one hundred
billion dollars in interest alone in a single year.""",
   "Checklist clipboard", "THE EIGHT WAYS")
sc("""They keep it flowing with design: the minimum payment anchor, rewards that make you spend, deferred
interest promotions, rising credit limits and painless payments. And you flip the deal with ten rules,
starting with the most important one. Pay in full, every month, on autopay.""",
   "Thumbs up person with card", "FLIP THE DEAL")

# ---------------- Close ----------------
ch("What to do next")
pr("""If you want the full plan, from paying off cards to building real wealth, it's in my playbook. The link
is in the description. And if credit card debt is part of a bigger loop, watch my video on why most people
stay broke, and how to escape. I'm Ryan Rover. See you in the next one.""")

save("video43", "How Credit Card Companies Make Money From You", [
    "Consumer Financial Protection Bureau, credit card market reports (more than $100 billion in interest and about $25 billion in fees in 2022; about $14 billion in late fees)",
    "Federal Reserve, G.19 Consumer Credit (average APR on accounts assessed interest above 20%)",
    "Schuh, Shy and Stavins, Who Gains and Who Loses from Credit Card Payments? Federal Reserve Bank of Boston (2010)",
    "Neil Stewart, The Cost of Anchoring on Credit-Card Minimum Repayments, Psychological Science (2009)",
    "Credit CARD Act of 2009 (minimum payment disclosure, penalty rate rules)",
    "CFPB consumer guidance on deferred interest promotions",
    "Payoff and interest figures: stated illustrative math",
], "how credit card companies make money: numbers, psychology, playbook")
