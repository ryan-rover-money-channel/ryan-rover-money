import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short


def lesson(n, title, sub, card_text, a, b, c, q1, c1, q2, c2, q3, c3):
    ch(f"Lesson {n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"LESSON {n}")
    sc(a, q1, c1)
    sc(b, q2, c2)
    sc(c, q3, c3)

# ---------------- Intro ----------------
ch("Intro")
short("A laundromat looks boring. The math behind it is fascinating.")
pr("""Hi, I'm Ryan Rover. Walk past a laundromat and it looks like the most boring business on earth. Rows of machines, a change
machine, a folding table. But behind that boring front is a money machine that teaches you almost everything about how small
businesses really make money. Today we're going to open the books, step by step, using a simple example. And by the end, you'll
be able to look at any boring business and see the math behind it.""")
card("""The laundromat math. Revenue, costs, profit, what the business is worth, and how buyers actually pay for it.""",
     {"type": "stat", "label": "the laundromat math", "big": "$ IN − $ OUT", "sub": "how boring businesses really make money"})
sc("""Why a laundromat? Because it's simple enough to understand in one video, and it has all the pieces that matter: steady demand,
expensive equipment, a lease, utility bills, a little labor, and a sale price based on profit. Once you understand these pieces,
you can apply the same thinking to car washes, storage units, vending routes, cleaning companies and almost any small business.""",
   "Laundromat washing machines", "ONE BUSINESS, EVERY LESSON")
sc("""One important warning. The numbers in this video are an illustration we built to teach the concepts, not industry averages or a
real business. Real laundromats vary enormously depending on location, size, prices, competition and management. Some do much
better than our example. Some lose money. Always look at real records before making any decision.""",
   "Calculator and pen on financial papers", "AN ILLUSTRATION, NOT A PROMISE")
sc("""We'll go through twelve lessons, then look at the whole thing from three angles. The numbers, meaning the actual math. The
psychology, meaning why people misjudge these businesses. And the playbook, meaning a checklist for evaluating any boring business
before you put a dollar into it.""",
   "Notebook with financial notes", "12 LESSONS, 3 ANGLES")
pr("""Let's open the books.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our example business is a simplified illustration. Lending rules come from the U.S. Small Business Administration, which
describes its seven a loan program and its requirements on its website. Business survival data comes from the Bureau of Labor
Statistics. Market return comparisons use a stated seven percent average yearly return as an illustration, not a promise. This
video is education, not financial, legal or business advice.""",
   "Bureau of Labor Statistics building", "OUR SOURCES")

# ---------------- Angle 1: the example P&L ----------------
ch("Angle 1: The numbers")
pr("""Angle one. The numbers. Here's our example laundromat, in a busy neighborhood full of apartments, where many renters don't have
their own washers and dryers.""")
card("""Our example laundromat brings in about three hundred thousand dollars a year: two hundred twenty thousand from washers and dryers,
sixty thousand from wash and fold service, and twenty thousand from vending and extras.""",
     {"type": "compare", "left": {"label": "Self-service machines", "big": "$220,000", "sub": "per year"},
      "right": {"label": "Wash & fold + extras", "big": "$80,000", "sub": "per year"},
      "note": "Illustration only, not an industry average"})
card("""Now the costs. Rent of about sixty thousand a year, utilities of about sixty thousand, labor of forty five thousand, repairs of
fifteen thousand, and about twenty thousand for insurance, supplies and everything else. Total costs: about two hundred thousand.""",
     {"type": "compare", "left": {"label": "Revenue", "big": "$300,000", "sub": "per year"},
      "right": {"label": "Costs", "big": "$200,000", "sub": "rent, utilities, labor, repairs, other"},
      "note": "Illustration only, not an industry average"})
card("""That leaves about one hundred thousand dollars a year for the owner, before loan payments, depreciation and income taxes. In the
small business world, this is often called seller's discretionary earnings.""",
     {"type": "stat", "label": "owner earnings (illustration)", "big": "$100,000", "sub": "before debt payments and taxes"})
sc("""One hundred thousand dollars a year sounds great, and in our example it is. But notice how fragile it is. If revenue falls by ten
percent, that's thirty thousand dollars less, while most costs stay the same. Owner earnings drop from one hundred thousand to seventy
thousand, a thirty percent fall from a ten percent drop in sales. That's called operating leverage, and it works in both directions.""",
   "Stock market chart falling on screen", "10% LESS SALES = 30% LESS PROFIT")
sc("""The good news is that it works upward too. If the owner adds pickup and delivery and grows revenue by ten percent, most costs barely
change, so owner earnings could jump by close to thirty thousand. That's why the best laundromat owners obsess over adding revenue
without adding much cost: wash and fold, commercial accounts like gyms and salons, longer hours, and card payments that make customers
spend a little more.""",
   "Graph trending upward", "10% MORE SALES = BIG PROFIT JUMP")
pr("""Now let's go through the twelve lessons hidden inside those numbers.""")

# ---------------- Lessons ----------------
lesson(1, "Demand comes first", "who needs this, every week?",
"""Lesson one. Demand comes before everything.""",
"""A laundromat works because a specific group of people needs it every single week: renters without washers, people in older apartment
buildings, and families with big loads. Before looking at machines or prices, the smart question is, who exactly needs this, how often,
and how many of them live within a short drive?""",
"""That's why location is everything. A laundromat surrounded by single family homes with washers and dryers will struggle. One near dense
apartments, with parking and good visibility, has a built in customer base. Many experienced buyers look at local population density,
the share of renters, and the number of competing laundromats within a few miles.""",
"""The same lesson applies to every boring business. A septic company needs homes on septic systems. A pest control company needs warm
weather and bugs. A storage facility needs people moving in and out. Find the demand first, then the business. Never the other way
around.""",
"Apartment building", "WHO NEEDS IT WEEKLY?",
"Map and compass", "LOCATION IS DEMAND",
"Suburban houses street United States", "DEMAND FIRST, ALWAYS")

lesson(2, "Revenue has layers", "machines, services, extras",
"""Lesson two. Revenue has layers.""",
"""In our example, self service machines bring in most of the money. But the services layered on top, like wash and fold, pickup and
delivery, and commercial laundry for gyms, salons and small hotels, can grow revenue without needing more floor space.""",
"""Services often earn more per pound of laundry, and they keep machines busy during quiet hours. A laundromat that's packed on Saturday
morning but empty on Tuesday afternoon can fill those slow hours with wash and fold work. That's using the same expensive equipment more
of the time.""",
"""The lesson for any business is to ask: what else could my existing customers and equipment do for me? A lawn care company adds snow
removal. A pressure washing company adds gutters. A cleaning company adds move out cleans. Layers of revenue on the same base are how
small businesses grow profit without growing risk.""",
"Laundromat washing machines", "LAYERS OF REVENUE",
"Folded laundry", "FILL THE QUIET HOURS",
"Snow plow truck", "SAME BASE, MORE SERVICES")

short("The most important document in a laundromat isn't the books. It's the lease.")
lesson(3, "Rent is the silent partner", "the lease decides your fate",
"""Lesson three. The lease is your silent partner.""",
"""In our example, rent is sixty thousand dollars a year, one of the two biggest costs. And unlike repairs or supplies, it's fixed. It's due
whether you have a great month or a terrible one. That's why the lease is one of the most important documents in the whole business.""",
"""Experienced buyers look closely at how many years remain on the lease, whether there are options to renew, and how much rent can
increase. A laundromat with expensive machines and only two years left on its lease is a big risk, because if the landlord won't renew,
moving those machines is costly and you lose your location.""",
"""The lesson: in any location based business, the lease can matter as much as the business itself. Read it carefully, ideally with a
lawyer, and try to negotiate long terms with renewal options. A great business in a location you can lose is not a great business.""",
"Small business storefront", "RENT IS FIXED",
"Lawyer office documents", "READ THE LEASE",
"Paperwork documents desk", "LONG TERMS, RENEWALS")

lesson(4, "Utilities move with volume", "water, gas, electricity",
"""Lesson four. Some costs move with sales.""",
"""Utilities are the other big cost in our example: water, gas for the dryers, and electricity. Unlike rent, utilities rise and fall with
how much the machines run. More customers means a bigger utility bill, but also more revenue.""",
"""This is the difference between fixed costs and variable costs. Fixed costs, like rent and insurance, stay the same no matter what.
Variable costs, like utilities and supplies, grow with sales. A business with mostly fixed costs has big operating leverage: profits swing
a lot with sales. A business with mostly variable costs is steadier, but grows profit more slowly.""",
"""Owners can lower utility costs with efficient machines, which use less water and energy per load. That's often a big part of the math
when deciding whether to replace old equipment. Lower variable costs per customer mean more profit on every load, forever.""",
"Electric meter", "VARIABLE COSTS",
"Washing machine close up", "EFFICIENT MACHINES",
"Calculator with financial charts", "FIXED VS VARIABLE")

lesson(5, "Equipment wears out", "the cost you don't see every month",
"""Lesson five. Equipment wears out, and that's a real cost.""",
"""Commercial washers and dryers are expensive and they last many years, but not forever. In our example, we listed fifteen thousand a year
in repairs. But there's a bigger cost that doesn't show up as a monthly bill: one day, all those machines will need to be replaced.""",
"""Accountants call this depreciation. Smart owners think of it as a replacement fund. If machines will cost a few hundred thousand dollars
to replace in ten to fifteen years, part of each year's profit really belongs to that future bill. A business that looks profitable but
never saves for equipment replacement is borrowing from its future.""",
"""This is one of the most common traps when buying any equipment heavy business. A seller may show strong profits, but if the machines are
near the end of their life, the buyer will face a big bill soon after closing. Always ask the age of every major piece of equipment, and
factor replacement into your math.""",
"Washing machine close up", "MACHINES WEAR OUT",
"Piggy bank coins", "A REPLACEMENT FUND",
"Paperwork documents desk", "ASK THE AGE OF EVERYTHING")

lesson(6, "Labor is a choice", "owner time has a price",
"""Lesson six. Labor is a choice, and your time has a price.""",
"""Many laundromats can run with few employees, which is part of their appeal. In our example, labor is forty five thousand a year, mostly for
wash and fold and keeping the place clean. But someone also has to handle repairs, collections, customer issues and the books.""",
"""If the owner does all of that personally, the business looks more profitable on paper. But the owner is really being paid for their time.
When evaluating a business, many buyers subtract a fair salary for a manager. If the business is still profitable after paying someone else
to run it, it's a true investment. If not, it's a job you're buying.""",
"""The lesson applies everywhere. A cleaning company that only makes money because the owner cleans sixty hours a week isn't the same as one
that makes money with a team and a manager. Both can be good choices, but you should know which one you're getting.""",
"Office cleaning janitor", "WHO DOES THE WORK?",
"Business meeting handshake", "PAY A FAIR SALARY",
"Construction workers", "JOB OR INVESTMENT?")

pr("""Quick pause. If you're enjoying this kind of business breakdown, subscribe to the channel. More of these deep dives are coming, on car
washes, storage units, vending machines and buying a business instead of starting one. Now, lesson seven, which is where the real money in
boring businesses is made.""")

short("Here's how a business that earns one hundred thousand dollars a year gets valued.")
lesson(7, "Value is a multiple", "what the business is worth",
"""Lesson seven. A business is valued as a multiple of its earnings.""",
"""Small businesses are often priced as a multiple of their owner earnings. For a business like our example, buyers and brokers might talk
about something like three to five times earnings, depending on the location, the lease, the age of the equipment, and how much the business
depends on the owner. These are rough ranges, and every deal is negotiated.""",
"""So our example laundromat, earning one hundred thousand a year, might be valued somewhere around three hundred to five hundred thousand
dollars. A newer laundromat with a long lease and modern machines would be at the high end. An older one with a short lease and tired
equipment would be at the low end, or even lower.""",
"""Here's why this matters. Every extra ten thousand dollars of steady yearly profit could add thirty to fifty thousand dollars to what the
business is worth when you sell. That's the hidden engine of wealth in boring businesses. You earn the profit every year, and you build
value every time profit grows.""",
"Business meeting handshake", "3X TO 5X EARNINGS",
"Laundromat washing machines", "~$300K TO $500K",
"Graph trending upward", "PROFIT BUILDS VALUE")

card("""On screen: owner earnings of one hundred thousand dollars a year, valued at three to five times earnings, gives a value of roughly three
hundred thousand to five hundred thousand dollars.""",
     {"type": "compare", "left": {"label": "Owner earnings", "big": "$100,000", "sub": "per year (illustration)"},
      "right": {"label": "Value at 3x to 5x", "big": "$300K-$500K", "sub": "depends on lease, equipment, risk"},
      "note": "Rough illustration; real deals vary widely"})

lesson(8, "Most buyers use debt", "how people actually pay",
"""Lesson eight. Most buyers don't pay cash.""",
"""Many small businesses are bought with a loan. The U.S. Small Business Administration's seven a program guarantees loans made by banks
to small businesses, including loans to buy an existing business. Buyers are usually required to put in some of their own money, and lenders
look closely at whether the business's cash flow can cover the loan payments.""",
"""Let's say our buyer pays three hundred thousand dollars, puts down thirty thousand of their own money, and borrows two hundred seventy
thousand over ten years at an illustrative interest rate of ten and a half percent. The monthly payment would be about three thousand six
hundred fifty dollars, or roughly forty four thousand dollars a year.""",
"""So out of one hundred thousand of owner earnings, about forty four thousand goes to the loan in the early years, leaving around fifty six
thousand for the owner before income taxes and the equipment fund. Still a solid return on a thirty thousand dollar down payment, but with
real risk, because if revenue drops, the loan payment doesn't.""",
"Bank building United States", "SBA 7(a) LOANS",
"Calculator with financial charts", "~$3,650 A MONTH",
"Spreadsheet on laptop", "~$56K LEFT FOR THE OWNER")

card("""On screen: two hundred seventy thousand dollars borrowed over ten years at an illustrative ten and a half percent costs about forty four
thousand dollars a year in payments.""",
     {"type": "compare", "left": {"label": "Owner earnings", "big": "$100,000", "sub": "per year"},
      "right": {"label": "Loan payments", "big": "~$44,000", "sub": "per year, 10 years"},
      "note": "Illustration; rates and terms vary"})

lesson(9, "Leverage cuts both ways", "debt magnifies everything",
"""Lesson nine. Debt magnifies results, good and bad.""",
"""With thirty thousand dollars down, our example owner might earn over fifty thousand a year after loan payments. That's a huge return on
the cash they put in. That's the magic of leverage, and it's why buying a business with a loan can build wealth so fast.""",
"""But leverage cuts both ways. Remember operating leverage from earlier: a ten percent drop in revenue cut owner earnings by thirty thousand.
Now add a fixed loan payment of forty four thousand on top. A bad year could leave the owner with very little, or even force them to put more
money in. Two kinds of leverage stacked together create big swings.""",
"""This is why lenders and experienced buyers look for a cushion: business earnings well above the loan payments, plus cash reserves. Never
buy a business where the plan only works if everything goes right. Always ask, what happens to me if revenue drops twenty percent?""",
"Graph trending upward", "LEVERAGE MAGNIFIES",
"Stock market chart falling on screen", "IT CUTS BOTH WAYS",
"Road sign curve ahead", "WHAT IF SALES DROP 20%?")

lesson(10, "Compare to the boring alternative", "would an index fund be easier?",
"""Lesson ten. Always compare to the boring alternative.""",
"""Every business decision should be compared with the simplest alternative: putting the same money into a diversified index fund and doing
nothing. At a seven percent illustration, three hundred thousand dollars would earn around twenty one thousand dollars in an average year, with
no lease, no broken machines and no customers to manage.""",
"""So the real question about our laundromat isn't whether it makes money. It's whether it makes enough extra money to justify the risk, the
time and the stress, compared with the easy option. For many owners, the answer is yes, because they enjoy running a business and the returns
can be much higher. For others, the index fund is the better choice.""",
"""This comparison protects you from falling in love with a business. If the numbers only beat an index fund by a small amount, after paying
yourself a fair salary for your time, the business probably isn't worth the risk. If they beat it by a lot, it might be.""",
"New York Stock Exchange trading floor", "THE BORING ALTERNATIVE",
"Person thinking by window", "EXTRA RETURN FOR EXTRA RISK",
"Calculator and pen on financial papers", "DON'T FALL IN LOVE")

lesson(11, "Records tell the truth", "trust, but verify everything",
"""Lesson eleven. Records tell the truth, and claims don't.""",
"""When you look at a business for sale, the seller will show you numbers. But numbers on a sales sheet aren't the same as numbers on tax
returns and bank statements. In cash heavy businesses especially, buyers should check that reported revenue matches deposits, utility bills
and machine counters.""",
"""Utility bills are a clever check for laundromats. Water use is tied to how much the machines run. If a seller claims high revenue but the
water bills are low, something doesn't add up. Similar checks exist in other businesses: fuel for delivery routes, supplies for cleaning
companies, or chemicals for pool services.""",
"""The lesson is simple. Trust, but verify everything. Use an accountant who knows small business deals, and walk away from any seller who
won't show real records. The best deals are often with owners who kept clean books for years.""",
"Tax forms on desk", "TAX RETURNS, NOT CLAIMS",
"Electric meter", "UTILITY BILLS DON'T LIE",
"Accountant desk calculator", "VERIFY EVERYTHING")

lesson(12, "Improve, then sell or hold", "the owner's real job",
"""Lesson twelve. The owner's real job is to improve the business.""",
"""Once you own a business, the biggest wealth comes from improving it. Adding services, upgrading to efficient machines, extending hours,
improving reviews, signing commercial accounts, and building systems so it runs without you. Each improvement raises profit, and every dollar
of profit raises the value.""",
"""Imagine our owner grows owner earnings from one hundred thousand to one hundred forty thousand over five years, while paying down the loan.
At a similar multiple, the business might now be worth well over four hundred thousand dollars, with much less debt. That's how a thirty
thousand dollar down payment can turn into a large amount of wealth, if things go well.""",
"""Then the owner has a choice: keep it for the cash flow, or sell it and use the money to buy a bigger business, invest, or retire. Either way,
the wealth came from buying a decent business, improving it patiently, and managing risk carefully.""",
"Laundromat washing machines", "IMPROVE IT",
"Graph trending upward", "MORE PROFIT, MORE VALUE",
"Person standing at crossroads", "HOLD OR SELL")

# ---------------- Other businesses ----------------
ch("The same math, everywhere")
pr("""Now here's the payoff. The same twelve lessons work for almost every boring business. Let's apply them quickly to a few others.""")
sc("""A car wash. Demand comes from cars in the area and how dirty they get. Revenue has layers: single washes, monthly memberships, detailing.
Costs include rent or land, water, chemicals, electricity and equipment. Equipment is expensive and wears out. Memberships create recurring
revenue, which buyers usually value highly. Same math, different machine.""",
   "Car wash", "CAR WASH")
sc("""Self storage. Demand comes from people moving, downsizing and running out of space. Revenue is monthly rent per unit. Costs are mostly
fixed: property taxes, insurance, maintenance, staff and marketing. That means huge operating leverage: once the facility is full, extra
revenue drops almost straight to profit. But a half empty facility can lose money.""",
   "Self storage units", "SELF STORAGE")
sc("""A vending route. Demand comes from busy locations with hungry people. Revenue is sales per machine. Costs are products, commissions to the
location owner, and your time driving and restocking. Each machine is a tiny business, and the route is a portfolio of them. Efficiency in
routing is the difference between profit and a low paying job.""",
   "Vending machine", "VENDING ROUTE")
sc("""And a cleaning company. Demand comes from busy households and offices. Revenue is recurring contracts. The biggest cost is labor, which is
mostly variable, so operating leverage is lower but risk is lower too. Value comes from recurring clients and systems that work without the
owner. Every business is different, but the questions are always the same.""",
   "Office cleaning janitor", "CLEANING COMPANY")

# ---------------- Three owners ----------------
ch("Three owners, three outcomes")
pr("""Let's run our example forward with three different owners who buy the exact same laundromat for three hundred thousand dollars. Same
machines, same lease, same neighborhood. Made up, but realistic.""")
sc("""Owner one, the improver. She keeps the place spotless, adds pickup and delivery, signs contracts with two gyms and a small hotel, and
installs card readers. Over five years, revenue grows and owner earnings rise to around one hundred forty thousand dollars. She's paid down
much of the loan, and the business is worth considerably more than she paid. Her thirty thousand dollar down payment has turned into a large
amount of equity and a strong income.""",
   "Small business owner smiling", "THE IMPROVER")
sc("""Owner two, the absentee. He thought it was passive income, so he visits once a month. Machines stay broken for weeks, the floor gets
dirty, and online reviews drop. Customers drift to a competitor two miles away. Revenue falls fifteen percent, which, thanks to operating
leverage and the loan payment, cuts his take home income by more than half. Five years later, he sells for less than he paid.""",
   "Person relaxing on couch", "THE ABSENTEE")
sc("""Owner three, the unlucky one. He runs it well, but two years in, a big new apartment complex nearby includes in unit washers, and the
landlord raises rent sharply at renewal. Revenue falls while costs rise. He survives because he kept a cash reserve and didn't overpay, but
his returns are modest. Not a disaster, but not the dream either.""",
   "Apartment building", "THE UNLUCKY ONE")
sc("""Same business, three outcomes. The improver won because of effort and smart additions. The absentee lost because he believed the passive
income story. And the unlucky owner survived because he protected himself from the downside. That's small business in one picture: effort
matters, luck matters, and risk management decides whether bad luck is a setback or a catastrophe.""",
   "Three people silhouettes", "EFFORT, LUCK, PROTECTION")

# ---------------- Five profit levers ----------------
ch("Five ways to raise profit without raising risk")
pr("""So what does the improver actually do? Here are five ways to raise profit in almost any boring business, without taking on much more risk.""")
sc("""Lever one. Raise prices carefully. Many small business owners haven't raised prices in years. A modest increase, explained well, often
loses very few customers and drops straight to profit. Lever two. Fill the slow hours. Discounts for quiet times, commercial work, or services
that use idle equipment turn dead time into revenue.""",
   "Receipt and coins on table", "LEVERS 1 AND 2")
sc("""Lever three. Add recurring revenue. Memberships, subscriptions, maintenance plans and commercial contracts make income more predictable,
which also raises the business's value. Lever four. Cut waste, not quality. Efficient machines, better energy contracts and smarter
scheduling lower costs without making customers unhappy.""",
   "Online banking smartphone app", "LEVERS 3 AND 4")
sc("""And lever five. Improve reputation. In local businesses, reviews are a form of marketing that compounds. A clean, safe, friendly business
with fast fixes and a responsive owner earns better reviews, which bring more customers, which fund more improvements. Of the five levers, this
one is the cheapest and often the most powerful.""",
   "Business meeting handshake", "LEVER 5: REPUTATION")

# ---------------- The exit ----------------
ch("The exit: what happens when you sell")
pr("""Finally, the part most people forget to plan: selling.""")
sc("""When an owner sells, the buyer looks at the same things we discussed: earnings, the lease, equipment, records and how much the business
depends on the owner. A business with clean books, a long lease, newer machines and a manager in place can command a higher multiple. A messy
one sells for less, or doesn't sell at all.""",
   "Business meeting handshake", "WHAT BUYERS LOOK FOR")
sc("""Taxes matter at the exit too. The sale of a business can create taxable gains, and how the price is split between equipment, goodwill and
other assets affects the tax bill. That's another reason to work with an accountant years before a sale, not weeks before. Planning ahead can
make a meaningful difference in what you keep.""",
   "Tax forms on desk", "PLAN THE TAXES EARLY")
sc("""The best time to prepare for a sale is the day you buy. Keep clean records, document how everything works, build relationships that don't
depend only on you, and keep the equipment in good shape. Even if you never sell, a business that's ready to sell is a business that's easier
to own.""",
   "Notebook with financial notes", "READY TO SELL FROM DAY ONE")

# ---------------- Angle 2: psychology ----------------
short("Why do people overpay for boring businesses? It's not the math, it's the dream.")
# ---------------- Red flags ----------------
ch("Ten red flags when buying a small business")
pr("""Before we get into the psychology, let's protect your money. Here are ten red flags I'd look for before buying any laundromat, car wash,
vending route, or other boring business. Any one of them isn't automatically a deal breaker, but each one deserves hard questions.""")
sc("""Red flag one. The seller can't or won't show tax returns. If the business earns what they say, the returns should roughly match. Big gaps
usually mean the real numbers are lower, or the seller is hiding cash income, which is a problem either way. Red flag two. The lease is short,
or the landlord won't commit to a renewal. Without a secure lease, you're buying a business that could be evicted.""",
   "Tax forms on desk", "RED FLAGS 1 AND 2")
sc("""Red flag three. The equipment is old and the price assumes it isn't. Ask the age of every major machine and what replacements cost. Red
flag four. Revenue jumped right before the sale. Sometimes owners push prices, cut maintenance, or stop paying themselves to make the last year
look great. Look at three to five years, not one.""",
   "Laundromat washing machines", "RED FLAGS 3 AND 4")
sc("""Red flag five. One customer or one contract is a huge share of revenue. If that customer leaves, the business changes overnight. Red flag
six. The owner is the business. If every relationship, skill and decision lives in the seller's head, what you're buying may walk out the door
on closing day. Ask how long they'll stay to train you.""",
   "Business meeting handshake", "RED FLAGS 5 AND 6")
sc("""Red flag seven. A new competitor is coming, or the neighborhood is changing in a way that hurts demand. Drive the area, talk to nearby
businesses, and check city planning records. Red flag eight. The seller is in a hurry and pressures you to skip inspections. A good deal
survives due diligence. A bad deal needs you to rush.""",
   "City street with small shops", "RED FLAGS 7 AND 8")
sc("""Red flag nine. Unpaid bills, liens, or legal disputes. A lawyer can search for these, and the purchase agreement should protect you from
the seller's old debts. And red flag ten. The numbers only work if everything goes perfectly. If one broken machine, one rent increase, or one
slow month makes the loan payment impossible, the deal is too tight. Walk away, or negotiate a lower price.""",
   "Notebook with financial notes", "RED FLAGS 9 AND 10")
sc("""Here's a simple rule many experienced buyers use: assume revenue comes in ten to fifteen percent lower than the seller says and costs come
in ten percent higher. If the business still pays the loan, covers your living costs and leaves a cushion, you may have a real opportunity. If
it doesn't, you've just saved yourself from a very expensive lesson.""",
   "Calculator and coins", "STRESS TEST THE DEAL")
pr("""Due diligence feels slow and expensive. A few thousand dollars for an accountant, a lawyer and an equipment inspection can feel like a lot.
But compared with a three hundred thousand dollar mistake, it's the cheapest insurance you'll ever buy.""")

ch("Angle 2: The psychology")
pr("""Angle two. The psychology. Why do smart people make bad decisions when buying boring businesses?""")
sc("""The first trap is the passive income dream. Laundromats, vending and storage are often sold online as passive income. People imagine
collecting money while doing nothing. Then they discover broken machines at midnight, unhappy customers and tricky landlords. Expecting
passive income leads people to underestimate the work, and to overpay for a business they don't really want to run.""",
   "Person relaxing on couch", "THE PASSIVE INCOME DREAM")
sc("""The second trap is anchoring on revenue. Three hundred thousand dollars of revenue sounds impressive. But revenue isn't profit. Buyers who
focus on the big top line number often forget to subtract every cost, a fair salary for their own time, loan payments and an equipment
fund. Always work down to the money that's actually left.""",
   "Calculator and pen on financial papers", "REVENUE IS NOT PROFIT")
sc("""The third trap is deal fever. After months of searching, buyers want the search to be over. They start ignoring red flags, like a short
lease or missing records, because they're emotionally invested. The best protection is a written checklist of deal breakers, made before you
start looking, and a willingness to walk away.""",
   "Person stressed looking at bills", "DEAL FEVER")
sc("""And the fourth trap is overconfidence in improvements. Every buyer believes they'll increase revenue and cut costs. Some do. But a price
based on the improvements you plan to make means you're paying the seller for your own future work. Smart buyers pay for the business as it
is today, and keep the upside of improvements for themselves.""",
   "Chess game", "DON'T PAY FOR YOUR OWN WORK")

# ---------------- Angle 3: playbook ----------------
short("Use this ten point checklist before you buy any small business.")
ch("Angle 3: The playbook")
pr("""Angle three. The playbook. Here's a checklist you can use to evaluate any boring business.""")
sc("""One. Demand: who needs this, how often, and how many of them are nearby? Two. Revenue: what are the layers, and how much is recurring?
Three. Costs: which are fixed and which are variable? What does a ten or twenty percent drop in sales do to profit? Four. Location: how long is
the lease, what are the renewal options, and how can rent change?""",
   "Notebook with financial notes", "CHECKLIST 1 TO 4")
sc("""Five. Equipment: how old is it, and what will replacement cost? Six. Labor: what's left after paying a fair salary to whoever runs it?
Seven. Records: do tax returns, bank deposits and utility bills match the seller's numbers? Eight. Debt: can the business comfortably cover the
loan payments, even in a bad year?""",
   "Paperwork documents desk", "CHECKLIST 5 TO 8")
sc("""Nine. Alternative: does this beat an index fund by enough to justify the time and the risk? And ten. You: do you actually want to run this
business, or at least manage the person who does? A great business you hate owning is a bad investment for you.""",
   "Person standing at crossroads", "CHECKLIST 9 AND 10")
sc("""And before any of this, protect your foundation. Keep an emergency fund outside the business, keep your retirement savings separate, and
never put in money you can't afford to lose. Buy with the help of an accountant and a lawyer who know small business deals. Their fees are
small compared with the cost of a bad purchase.""",
   "Piggy bank coins", "PROTECT YOUR FOUNDATION")

# ---------------- Questions ----------------
ch("Questions people ask")
pr("""Let me answer the questions people ask most about the laundromat math.""")
sc("""Question one. Is a laundromat a good first business? It can be, especially for people who are handy, organized and comfortable with
equipment. But it requires capital, a good lease and careful due diligence. Question two. Is it better to build or buy? Buying an existing
laundromat with records removes guesswork about demand, but you pay for the established customer base. Building lets you choose a great
location and new machines, but you start from zero customers.""",
   "Laundromat washing machines", "FIRST BUSINESS? BUILD OR BUY?")
sc("""Question three. What about cash and card payments? Many laundromats now use card systems or apps, which can increase spending, reduce
theft and make records cleaner. Question four. How long until I make my money back? In our illustration, with thirty thousand down and around
fifty thousand a year after loan payments, the down payment could come back within a year or so. But that ignores risk, taxes and the
equipment fund. Real results vary widely.""",
   "Credit card close up", "CARDS? PAYBACK?")
sc("""Question five. Do I need to be there every day? Not necessarily. Many owners hire attendants and visit regularly, using cameras and card
systems to monitor the business. But someone needs to handle problems quickly, and absentee owners often find that service quality slips
without attention.""",
   "Security camera", "THERE EVERY DAY?")
sc("""Question six. What happens if a big machine breaks right after I buy? That's exactly why the equipment fund and the cash reserve exist.
Before closing, get the machines inspected and ask for a price reduction or a repair credit for anything near the end of its life. After
closing, set aside money every month so a repair is an expense, not an emergency.""",
   "Laundromat washing machines", "WHAT IF A MACHINE BREAKS?")
sc("""Question seven. Can I buy a business with no money at all? Some deals use seller financing, where the seller lets you pay part of the price
over time, often combined with a bank loan. That can reduce the cash you need, but you still need reserves, good credit and a deal that works
on paper. Be careful with anyone selling a course promising no money down riches. The math still has to work.""",
   "Contract signing pen", "NO MONEY DOWN?")
sc("""Question eight. Is a boring business better than real estate or stocks? It's different. Stocks are passive and diversified. Real estate
offers leverage and tangible assets. A small business can offer higher returns, but it demands your time and concentrates your risk in one
place. Many wealthy people own all three, but they usually build the foundation with steady investing first.""",
   "Stock market chart on screen", "BUSINESS VS STOCKS VS REAL ESTATE")
sc("""Question nine. How do I learn this before risking money? Work in or near the industry, talk to owners who aren't selling, and study real
listings on business for sale websites, running the numbers on each one the way we did today. After analyzing twenty or thirty listings,
you'll start to see what a good deal looks like and which numbers sellers like to inflate.""",
   "Person reading book", "LEARN BEFORE YOU BUY")

# ---------------- Recap ----------------
ch("Recap: the laundromat math")
sc("""Let's recap the twelve lessons. Demand comes first. Revenue has layers. The lease is your silent partner. Some costs move with sales. Equipment
wears out. Labor is a choice, and your time has a price.""",
   "Notebook with financial notes", "LESSONS 1 TO 6")
sc("""A business is valued as a multiple of its earnings. Most buyers use debt. Leverage cuts both ways. Always compare to the boring alternative.
Records tell the truth. And the owner's real job is to improve the business, then hold it or sell it.""",
   "Mountain climber reaching summit", "LESSONS 7 TO 12")
sc("""And the three angles. The numbers: three hundred thousand of revenue can become one hundred thousand of owner earnings, and a value of three
to five times that, in our illustration. The psychology: beware the passive income dream, revenue anchoring, deal fever and paying for your own
improvements. And the playbook: a ten point checklist, and a protected foundation.""",
   "Map and compass", "NUMBERS, PSYCHOLOGY, PLAYBOOK")

# ---------------- Close ----------------
ch("What to do next")
pr("""So here's your homework. Pick any small business in your neighborhood, and try to sketch its math. Who are the customers? What are the
big costs? What might it be worth? Doing that for a few businesses will train your eye faster than anything else. If you want the full plan for
building wealth, it's in my playbook, link in the description. I'm Ryan Rover. See you in the next one.""")

save("video13", "The Laundromat Math: How Boring Businesses Really Make Money", [
    "Example laundromat figures: simplified illustration built for teaching, not an industry average or a real business",
    "U.S. Small Business Administration, 7(a) loan program (guaranteed loans, including for business acquisitions; equity injection requirements)",
    "Bureau of Labor Statistics, Business Employment Dynamics (business survival rates)",
    "Loan payment example: $270,000 over 10 years at an illustrative 10.5% interest rate",
    "Market comparison: stated illustrative 7% average yearly return",
], "the laundromat math")
