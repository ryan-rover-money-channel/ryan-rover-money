import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short


def reason(n, title, sub, a, b, c, q1, c1, q2, c2, q3, c3):
    ch(f"Reason {n}. {title}")
    card(f"Reason {n}. {title}. {sub}", {"type": "list", "n": n, "title": title, "sub": sub}, f"REASON {n}")
    sc(a, q1, c1)
    sc(b, q2, c2)
    sc(c, q3, c3)

# ---------------- Intro ----------------
ch("Intro")
short("Most people start a business from zero. The smart money often buys one that already works.")
pr("""Hi, I'm Ryan Rover. When most people dream about owning a business, they picture starting one from scratch: a new idea, a new
logo, a grand opening. But a lot of wealthy business owners did something far less romantic. They bought a business that already had
customers, employees and profits. Today, I'll give you fifteen real reasons why buying a business can beat starting one, and also the
risks nobody talks about, so you can decide which path fits you.""")
card("""Buying versus starting. Fifteen reasons buying an existing business can beat starting from zero.""",
     {"type": "stat", "label": "buy vs start", "big": "15", "sub": "reasons buying can win"})
sc("""Let's be clear from the start. Buying a business isn't automatically better, and it isn't easy. It usually takes more money up front,
careful research and professional help. But for many people, especially those who want income sooner and less guesswork, buying an
established business can dramatically improve the odds.""",
   "Business meeting handshake", "NOT EASY, BUT OFTEN SMARTER")
sc("""The numbers in this video are simplified illustrations to explain the concepts, not promises. Real deals vary enormously by industry,
location, price and the quality of the business. Always work with an accountant and a lawyer, and verify everything before you sign.""",
   "Calculator and pen on financial papers", "ILLUSTRATIONS, NOT PROMISES")
sc("""We'll go through all fifteen reasons, then look at the decision from three angles. The numbers, meaning how a purchase actually gets
paid for. The psychology, meaning why people overvalue starting from scratch. And the playbook, meaning the steps to find, evaluate and buy
a business safely.""",
   "Notebook with financial notes", "15 REASONS, 3 ANGLES")
pr("""Let's start with the biggest reason of all.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Business survival data comes from the Bureau of Labor Statistics Business Employment Dynamics program, which tracks how many new
businesses survive over time. Lending information comes from the U.S. Small Business Administration's seven a loan program. Deal examples are
simplified illustrations we built for teaching. This video is education, not financial, legal or business advice.""",
   "Government building", "SOURCES")

# ---------------- The 15 ----------------
reason(1, "Cash flow from day one", "you get paid starting the first month",
    """Reason one. Cash flow from day one. When you start a business, you often spend months or years before it pays you anything. Many
founders live on savings while they build. When you buy a profitable business, the customers, sales and profits are already there. In many
cases, the business can start paying you and the loan from the very first month.""",
    """That changes your life immediately. Instead of draining your savings while you wait for customers, the business supports you. And
instead of wondering whether anyone will ever buy what you sell, you already know they do, because they've been buying it for years.""",
    """Of course, cash flow from day one depends on buying a business that's actually profitable, and on not losing customers during the
transition. That's why due diligence and a smooth handover matter so much. But the potential to earn from the first month is one of the
biggest advantages of buying.""",
    "Cash register in store", "PAID FROM DAY ONE",
    "Online banking smartphone app", "NO WAITING FOR CUSTOMERS",
    "Business meeting handshake", "PROTECT THE HANDOVER")

reason(2, "Proven survival", "it already made it through the hardest years",
    """Reason two. Proven survival. According to Bureau of Labor Statistics data, roughly one in five new businesses fails in its first year,
and about half are gone within five years. The early years are the most dangerous time in a business's life.""",
    """An established business has already survived those years. It has found customers, figured out pricing, and made it through at least
some ups and downs. That doesn't guarantee its future, but it removes one of the biggest risks in business: whether the idea works at all.""",
    """Think of it this way. A startup is a bet that an idea will work. Buying an established business is a bet that something already working
will keep working, especially if you run it well. The second bet usually has much better odds.""",
    "Closed store sign", "THE DANGEROUS EARLY YEARS",
    "Established storefront", "ALREADY SURVIVED",
    "Dice on table", "BETTER ODDS")

reason(3, "Banks lend on history", "lenders like businesses with track records",
    """Reason three. Banks prefer history. It's very hard to get a loan to start a brand new business, because there's no track record. But
lenders can look at years of tax returns and financial statements from an existing business and see whether it can repay a loan.""",
    """The Small Business Administration's seven a loan program is often used to buy existing businesses. Typically, the buyer puts in a
portion of the price, often around ten percent depending on the deal and the lender, and the loan covers much of the rest. The business's
own cash flow then repays the loan over time.""",
    """That means a buyer with a relatively small amount of cash can sometimes acquire a business worth many times that amount. Leverage
cuts both ways, and a loan has to be repaid even in bad months, but used carefully, it's one of the most powerful tools in small business.""",
    "Bank building", "BANKS LIKE HISTORY",
    "Contract signing pen", "SBA FINANCING",
    "Calculator and coins", "LEVERAGE, CAREFULLY")

reason(4, "Seller financing", "the seller can become your lender",
    """Reason four. Seller financing. In many small business sales, the seller agrees to receive part of the price over time, like a loan, instead
of all of it at closing. That can reduce how much cash and bank financing a buyer needs.""",
    """Seller financing also sends a signal. If the seller is willing to be paid over several years, it suggests they believe the business will
keep producing enough cash to pay them. A seller who refuses any financing and wants everything up front may deserve a few extra questions.""",
    """Many deals combine an SBA loan, a buyer's down payment and some seller financing. The exact structure depends on the lender and the
negotiation, and it should always be reviewed by a lawyer and an accountant. But it's a tool most people don't even know exists.""",
    "Handshake with customer", "THE SELLER AS LENDER",
    "Person thinking with notebook", "A SIGNAL OF CONFIDENCE",
    "Contract signing pen", "COMBINED STRUCTURES")

short("When you buy a business, you're not just buying profit. You're buying the team that makes it.")
reason(5, "Trained employees", "the team already knows how to do the work",
    """Reason five. Trained employees. Hiring and training a team from scratch is slow, expensive and risky. An established business usually
comes with employees who already know the customers, the equipment and the routines.""",
    """Experienced employees are often the reason customers stay. Keeping them through the transition, and treating them well, is one of the
most important things a new owner can do. Many buyers meet key employees before closing, and some offer retention bonuses to keep them.""",
    """There's a flip side. If key employees leave after the sale, or if the team has problems the seller hid, the business can suffer. So meet
the team, understand their pay and roles, and plan how you'll keep the people who matter most.""",
    "Team of workers", "A TEAM THAT KNOWS THE WORK",
    "Business meeting", "KEEP THE KEY PEOPLE",
    "Person thinking with notebook", "MEET THE TEAM FIRST")

reason(6, "Existing customers", "the hardest part of business is already done",
    """Reason six. Existing customers. Ask any founder what the hardest part of starting a business was, and many will say finding customers.
Marketing is expensive, and earning trust takes time. When you buy a business, you buy its customer base.""",
    """Some of those customers may be on contracts or recurring plans, which makes revenue more predictable. Others are loyal because of habit,
location or reputation. Either way, you start with people who already pay for what the business sells.""",
    """Your job is to keep them. Customers can leave when ownership changes, especially if service slips or prices jump. Smart buyers keep
things steady at first, introduce themselves personally, and only make changes after they understand why customers stay.""",
    "Customers in store", "CUSTOMERS INCLUDED",
    "Calendar on desk", "RECURRING REVENUE",
    "Handshake with customer", "KEEP THEM CLOSE")

reason(7, "Systems and suppliers", "years of trial and error, already paid for",
    """Reason seven. Systems and suppliers. An established business has already figured out a thousand small things: which suppliers are
reliable, how to schedule staff, what to charge, how to handle complaints, which software to use. Those lessons cost the previous owner
years of trial and error.""",
    """When you buy, you inherit those systems and relationships. Supplier accounts, payment terms and processes are already in place. That
frees you to focus on improving the business instead of building every piece from zero.""",
    """Not every business has great systems, of course. Some are messy and depend on the owner's memory. Those can be bought at a lower price
and improved, but you need to know what you're getting. Ask how everything works before you buy.""",
    "Warehouse shelves organized", "YEARS OF LESSONS",
    "Laptop with business software", "SYSTEMS IN PLACE",
    "Notebook with financial notes", "KNOW WHAT YOU'RE GETTING")

pr("""Quick pause. If you're finding this useful, subscribe to the channel. Every week, Ryan breaks down how money and business really
work, in plain English, with real numbers. Now, reason number eight.""")

reason(8, "Brand and reputation", "trust that took years to earn",
    """Reason eight. Brand and reputation. A business that has served its community for years has something you can't buy with advertising:
trust. People recognize the name, know where it is, and have friends who use it. Online, it may have hundreds of reviews.""",
    """Building that kind of reputation from scratch can take years. When you buy, you start with it. A strong reputation brings in new
customers through word of mouth and makes marketing far more effective.""",
    """But reputation is fragile. Check reviews carefully before buying, because a bad reputation is hard to fix. And after buying, protect the
reputation by keeping quality high. Customers don't care that the owner changed. They care whether the service is still good.""",
    "Established storefront", "TRUST TAKES YEARS",
    "Smartphone reviews app", "REVIEWS AND WORD OF MOUTH",
    "Person thinking with notebook", "PROTECT IT")

reason(9, "Real data to decide with", "you can see the numbers before you commit",
    """Reason nine. Real data. A startup runs on predictions. You guess how many customers you'll get and what they'll pay. When you buy a
business, you can look at real numbers: years of sales, costs, profits, customer counts and seasonal patterns.""",
    """That data helps you decide whether the price makes sense, whether the business can support a loan, and where it could improve. It
replaces hope with evidence. Lenders use it too, which is why financing is easier.""",
    """The key is to verify the data. Compare the profit and loss statements with tax returns and bank statements. Have an accountant review
everything. Sellers sometimes present their numbers in the best possible light, so trust, but verify.""",
    "Calculator and pen on financial papers", "EVIDENCE OVER HOPE",
    "Tax forms on desk", "VERIFY EVERYTHING",
    "Accountant meeting client", "TRUST BUT VERIFY")

reason(10, "Baby boomer retirements", "a generation of owners is getting ready to sell",
    """Reason ten. Timing. A large share of small business owners in America are baby boomers approaching or past retirement age. Many of
them don't have children who want to take over. That means many profitable businesses may be looking for buyers in the coming years.""",
    """For buyers, that can mean more choice and, in some cases, more motivated sellers. A retiring owner who has spent thirty years building
a business often cares about who takes it over, about protecting employees and customers, not just about getting the highest price.""",
    """This doesn't mean bargains are everywhere. Good businesses still sell for fair prices, and competition from investors is growing. But
the wave of retirements is one reason many people believe this decade is a strong time to buy a small business.""",
    "Older business owner", "A WAVE OF RETIREMENTS",
    "Business meeting handshake", "OWNERS WHO CARE",
    "Calendar pages flying", "THE TIMING")

short("Buying a business can be cheaper than starting one. Here's the math that surprises people.")
reason(11, "Lower total cost of risk", "starting can cost more than it looks",
    """Reason eleven. The true cost of starting is often higher than it looks. Startups spend on equipment, buildout, marketing and
inventory, then often lose money for months while they find customers. Add the cost of the founder's unpaid time, and the real price of
starting can be surprisingly high.""",
    """Buying looks more expensive up front because you pay for the profits. But you're paying for something proven. When you compare the
total cost, including the money lost while a startup ramps up and the risk that it never works at all, buying can be the cheaper path to a
given level of income.""",
    """Here's a simple illustration. A startup might need one hundred fifty thousand dollars and two years of little or no income before it
earns one hundred thousand a year, if it works. An existing business earning one hundred thousand might cost three hundred thousand, but
pay from month one, with a much higher chance of success. Different paths, very different risks.""",
    "Calculator and coins", "THE HIDDEN COST OF STARTING",
    "Cash register in store", "PAYING FOR PROOF",
    "Notebook with financial notes", "AN ILLUSTRATION")

reason(12, "Room to improve", "many small businesses are under-managed",
    """Reason twelve. Room to improve. Many small businesses are run the same way for decades. Prices haven't been raised in years. Marketing
is word of mouth only. Nobody answers the phone after five. The website looks like it's from 2005.""",
    """For a buyer with fresh energy, that can be an opportunity. Modest improvements, like better pricing, online booking, a few marketing
efforts, or a new service, can raise profits meaningfully. And because businesses are often valued as a multiple of profit, higher profit
can also raise what the business is worth.""",
    """Be careful not to change too much too fast. Customers and employees may resist. The best buyers learn the business first, keep what
works, and make improvements gradually. But the upside of improving an under managed business is one of the most exciting parts of buying.""",
    "Old fashioned storefront", "UNDER MANAGED",
    "Laptop with business software", "MODEST IMPROVEMENTS",
    "Person thinking with notebook", "CHANGE GRADUALLY")

reason(13, "Training from the seller", "the previous owner can teach you",
    """Reason thirteen. Training from the seller. Many purchase agreements include a transition period where the seller stays for weeks or
months to train the buyer, introduce key customers and suppliers, and answer questions.""",
    """That's like getting a private apprenticeship from the person who knows the business better than anyone. When a seller is also
financing part of the deal, they have an extra reason to help you succeed, because they want to get paid.""",
    """Negotiate the training period clearly in the contract: how long, how many hours, and what it includes. Some deals also include a
non compete agreement, which prevents the seller from opening a competing business nearby.""",
    "Older plumber with apprentice", "A PRIVATE APPRENTICESHIP",
    "Handshake with customer", "THE SELLER WANTS YOU TO WIN",
    "Contract signing pen", "PUT IT IN WRITING")

reason(14, "Faster path to scale", "build on something instead of from nothing",
    """Reason fourteen. A faster path to scale. Once you own one profitable business and understand it, you can grow by improving it, adding
locations, or buying similar businesses nearby. Some owners eventually combine several small businesses into a larger company.""",
    """Larger, combined businesses can sometimes sell for higher multiples than small ones, because buyers see them as less risky and less
dependent on one owner. That's one reason investors buy small businesses and grow them.""",
    """This is an advanced strategy that requires management skill and careful financing. But it shows how buying one business can become the
foundation for much bigger wealth over time.""",
    "Map with pins", "ADD LOCATIONS",
    "Business meeting", "BIGGER CAN BE WORTH MORE",
    "Stock market chart on screen", "A FOUNDATION FOR GROWTH")

reason(15, "Ownership without inventing", "you don't need a brilliant idea",
    """And reason fifteen. You don't need a brilliant idea. Many people never become business owners because they're waiting for the perfect
idea. Buying removes that barrier. You don't need to invent anything. You need to run something well.""",
    """That opens ownership to people who are good at operations, management, sales or customer service, but who aren't inventors. Some of
the most successful small business owners are simply excellent operators of ordinary businesses.""",
    """Ordinary businesses, run well, can produce extraordinary results over time. A plumbing company, an accounting firm, a car wash. None of
these require genius. They require consistency, good people and careful money management.""",
    "Person thinking with notebook", "NO BRILLIANT IDEA NEEDED",
    "Team of workers", "OPERATORS WIN",
    "Small town main street", "ORDINARY CAN BE EXTRAORDINARY")

# ---------------- Risks ----------------
ch("The risks nobody talks about")
pr("""Now, to be fair, buying a business has real risks. Let's go through the biggest ones.""")
sc("""Risk one. Overpaying. If you pay too much, the business may not produce enough cash to repay the loan and pay you. Risk two. Hidden
problems: declining sales, unpaid taxes, legal disputes or equipment about to fail. Risk three. Customer or employee loss after the sale,
especially if the business depended heavily on the seller's relationships.""",
   "Person stressed with bills", "RISKS 1 TO 3")
sc("""Risk four. Debt. A loan has to be paid even in bad months, and many SBA loans require a personal guarantee, which can put personal
assets at risk if the business fails. Risk five. You might not enjoy it. Owning a business is demanding, and buying one doesn't make that
easier. Know what daily life looks like before you buy.""",
   "Contract signing pen", "RISKS 4 AND 5")

# ---------------- When starting wins ----------------
ch("When starting from scratch is the better choice")
pr("""To be fair, starting a business is sometimes the better choice. Here's when.""")
sc("""Starting makes sense when you have very little capital and the business can begin small, like a service you can do yourself with
basic tools. It makes sense when you have a genuinely new idea or a market that no existing business serves. And it makes sense when you
want to build something with your own culture and methods from day one, without inheriting someone else's habits.""",
   "Garage workshop", "WHEN STARTING WINS")
sc("""Starting can also be a great way to learn. Many people start a small side business to discover what they're good at, then later buy a
larger business in the same field. The two paths aren't enemies. For many owners, starting small teaches the skills, and buying later
provides the scale.""",
   "Person thinking with notebook", "START TO LEARN, BUY TO SCALE")
sc("""The honest answer is this. If you have the capital, the credit and the temperament to manage people, buying often offers better odds
and faster income. If you have little money but plenty of time and energy, starting small may be the realistic path. Know which one
describes you.""",
   "Person standing at crossroads", "KNOW WHICH ONE YOU ARE")

# ---------------- Three buyers ----------------
ch("Three buyers, three stories")
pr("""Let's make this concrete with three made up but realistic buyers.""")
sc("""Buyer one is a forty year old operations manager tired of corporate life. She has eighty thousand dollars saved and strong credit. She
spends six months looking at listings and buys a commercial cleaning company earning about one hundred ten thousand dollars a year, with an
SBA loan, seller financing and a three month training period. Her management experience turns out to be exactly what the business needed.""",
   "Office cleaning at night", "THE CORPORATE ESCAPEE")
sc("""Buyer two is a thirty two year old HVAC technician. He knows the trade inside and out but has never run a company. When his boss
announces plans to retire, the two of them agree on a sale with significant seller financing, paid over seven years. The customers already
know him, the employees trust him, and the transition is smooth.""",
   "Technician servicing furnace", "THE EMPLOYEE WHO BUYS")
sc("""Buyer three makes the classic mistake. He falls in love with a restaurant, skips a full review of the books, and pays based on the
seller's claims. After closing, he discovers sales were declining and the lease renewal includes a large rent increase. Within two years,
he's struggling to make the loan payments. The business wasn't the problem. Skipping due diligence was.""",
   "Empty restaurant", "THE BUYER WHO SKIPPED HOMEWORK")
sc("""The lessons. Match the business to your skills. Look for sellers willing to help with financing and training. And never, ever skip due
diligence, no matter how much you love the business.""",
   "Notebook with financial notes", "THE LESSONS")

# ---------------- Where to find ----------------
ch("Where to find businesses for sale")
sc("""Source one. Online marketplaces for businesses for sale, which list thousands of small businesses with asking prices and basic
financials. They're great for learning what businesses cost in your area. Source two. Business brokers, who represent sellers and often
have listings that aren't advertised widely.""",
   "Laptop searching listings", "MARKETPLACES AND BROKERS")
sc("""Source three. Your own network. Accountants, lawyers, bankers and insurance agents often know which business owners are thinking about
retirement. Source four. Direct outreach. Some buyers write letters or call owners of businesses they admire to ask if they've ever
considered selling. Many great deals never get listed at all.""",
   "Phone ringing on desk", "NETWORK AND DIRECT OUTREACH")
sc("""Source five. Your current employer. If you work for a small business with an owner nearing retirement, you may be the most natural
buyer of all. You already know the customers, the team and the work, and owners often prefer selling to someone they trust.""",
   "Older business owner", "YOUR OWN EMPLOYER")

# ---------------- Due diligence ----------------
ch("Ten questions to ask before you buy")
sc("""Question one. Why is the owner selling? Retirement is common and reasonable, but listen for problems they might be escaping. Question
two. Do the tax returns match the profit and loss statements? Question three. Are sales growing, steady or shrinking over the last three to
five years?""",
   "Tax forms on desk", "QUESTIONS 1 TO 3")
sc("""Question four. How much revenue comes from the top few customers? Question five. How long is the lease, and what are the renewal terms?
Question six. How old is the equipment, and what will it cost to replace? Question seven. Which employees are essential, and will they stay?""",
   "Person reading documents", "QUESTIONS 4 TO 7")
sc("""Question eight. How much of the business depends on the owner personally? Question nine. Are there any lawsuits, liens, unpaid taxes or
license issues? And question ten. Will the seller train me, sign a non compete and carry part of the financing? The answers to these ten
questions tell you most of what you need to know.""",
   "Contract signing pen", "QUESTIONS 8 TO 10")

# ---------------- Mistakes ----------------
ch("Five mistakes first time buyers make")
sc("""Mistake one. Falling in love with the business before checking the numbers. Mistake two. Using all their savings for the down payment,
leaving no cash reserve for surprises. A business can need money in the first months for repairs, inventory or slow seasons.""",
   "Person stressed with bills", "MISTAKES 1 AND 2")
sc("""Mistake three. Changing too much too fast, which scares away employees and customers. Mistake four. Not budgeting for their own salary.
Remember that owner earnings must cover the loan, your living expenses, taxes and reinvestment. And mistake five. Going it alone without an
accountant and a lawyer who know small business deals.""",
   "Accountant meeting client", "MISTAKES 3 TO 5")

# ---------------- Valuation ----------------
ch("How small businesses are priced")
pr("""Before you can judge a deal, you need to understand how small businesses are usually priced.""")
sc("""Most small businesses are priced as a multiple of their earnings. For very small owner operated businesses, brokers often use something
called seller's discretionary earnings, which is the profit plus the owner's salary and certain personal expenses run through the business.
It shows how much cash one full time owner could take out.""",
   "Calculator and pen on financial papers", "SELLER'S DISCRETIONARY EARNINGS")
sc("""Multiples vary widely. A tiny business that depends entirely on its owner might sell for one to two times earnings. A larger, well run
business with recurring revenue, a manager in place and steady growth might sell for three, four or more times. The safer and more
transferable the earnings, the higher the multiple.""",
   "Stock market chart on screen", "WHAT DRIVES THE MULTIPLE")
sc("""Watch out for add backs, which are expenses the seller says won't continue under a new owner, like personal car payments or family
members on payroll. Some add backs are legitimate. Others are wishful thinking that inflates the earnings and the price. Your accountant
should check every one.""",
   "Accountant meeting client", "CHECK THE ADD BACKS")
sc("""And remember the simple test. After paying the loan, can the business pay you a reasonable salary and still leave a cushion? If the
answer is no at the asking price, the price is too high, no matter what multiple the broker quotes.""",
   "Online banking smartphone app", "THE SIMPLE TEST")

# ---------------- First 100 days ----------------
ch("Your first 100 days as an owner")
sc("""Days one to thirty. Listen. Meet every employee one on one. Call or visit the most important customers and introduce yourself. Learn
how everything works before changing anything. Make sure payroll, suppliers and bills keep running smoothly. Stability is the goal.""",
   "Business meeting", "DAYS 1 TO 30: LISTEN")
sc("""Days thirty to sixty. Learn the numbers deeply. Track weekly sales, costs and cash. Identify the quick wins, like unanswered calls,
outdated prices or a broken website. Start building your relationships with the bank, the landlord and key suppliers.""",
   "Calculator and coins", "DAYS 30 TO 60: LEARN")
sc("""Days sixty to one hundred. Start improving, carefully. Make one or two changes at a time and measure the results. Share your plans
with the team so they feel part of the future. By day one hundred, you should know the business well enough to make a twelve month plan.""",
   "Notebook with financial notes", "DAYS 60 TO 100: IMPROVE")

# ---------------- Angle 1 ----------------
ch("Angle 1: The numbers")
pr("""Let's look at the whole decision through three angles. First, the numbers. How does a purchase actually get paid for?""")
card("""Example deal. Business earns one hundred twenty thousand dollars a year for the owner. Price three hundred sixty thousand dollars,
three times earnings.""",
     {"type": "stat", "label": "example deal", "big": "3× earnings", "sub": "$120K a year, price $360K (illustration)"}, "AN EXAMPLE DEAL")
sc("""Say a business produces one hundred twenty thousand dollars a year in owner earnings, after all expenses but before the owner's pay and
loan payments. Small businesses often sell for a multiple of that number, perhaps two to four times depending on the industry, size and
risk. At three times, the price is three hundred sixty thousand dollars.""",
   "Calculator and pen on financial papers", "THE PRICE")
sc("""Now the financing. Say the buyer puts down thirty six thousand dollars, ten percent. An SBA loan covers the remaining three hundred
twenty four thousand over ten years. At an illustrative interest rate around ten and a half percent, the monthly payment would be roughly
four thousand four hundred dollars, about fifty three thousand dollars a year.""",
   "Bank building", "THE FINANCING")
sc("""Subtract that from the one hundred twenty thousand of earnings, and about sixty seven thousand dollars a year remains for the owner,
before taxes, while the loan is being paid off. After ten years, the loan is gone, and the full earnings belong to the owner. All for a cash
investment of thirty six thousand dollars, plus a lot of work.""",
   "Online banking smartphone app", "WHAT'S LEFT FOR YOU")
sc("""Now the stress test. If earnings fall twenty percent to ninety six thousand, the owner keeps about forty three thousand a year. Still
positive, but tight. If earnings fall by half, the business can barely cover the loan. That's why buyers need cash reserves, conservative
assumptions and a price that leaves room for bad years.""",
   "Stock market chart falling", "THE STRESS TEST")

# ---------------- The exit ----------------
ch("The other end: selling someday")
sc("""Here's one more reason buying can build wealth: the exit. If you buy a business at three times earnings, improve it, pay down the loan,
and grow earnings over ten years, you may eventually sell it for more than you paid, while having earned an income the whole time. That
combination of income plus a sale is how many small business owners build their largest asset.""",
   "Business meeting handshake", "INCOME PLUS A SALE")
sc("""Let's continue our example. Say you grow earnings from one hundred twenty thousand to one hundred sixty thousand dollars over ten years,
and the loan is fully paid. If a buyer pays three times earnings, the business sells for around four hundred eighty thousand dollars. Your
original cash investment was thirty six thousand. Taxes and fees will take a share, and nothing is guaranteed, but you can see the power of
the model.""",
   "Calculator and coins", "THE EXAMPLE, TEN YEARS LATER")
sc("""To get there, run the business from day one as if you'll sell it. Keep clean books, document how things work, build a team that doesn't
depend on you, and grow recurring revenue. The same habits that make a business easier to own also make it worth more to the next buyer.""",
   "Notebook with financial notes", "RUN IT LIKE YOU'LL SELL IT")

# ---------------- Angle 2 ----------------
short("Why most people would rather start a business that might fail than buy one that already works.")
ch("Angle 2: The psychology")
pr("""Second angle. The psychology. Why do so many people choose to start from scratch, even when buying might be smarter?""")
sc("""The first reason is the founder myth. Our culture celebrates founders who started in a garage. Buying a business doesn't make for an
exciting story. But a business's bank account doesn't care about the story. Many successful owners are buyers, not founders.""",
   "Garage workshop", "THE FOUNDER MYTH")
sc("""The second reason is sticker shock. A price of three hundred thousand dollars feels huge, while starting with fifty thousand feels
manageable. But that comparison ignores the risk and the years of lost income in a startup. People compare prices instead of comparing
outcomes.""",
   "Person stressed with bills", "STICKER SHOCK")
sc("""The third reason is not knowing it's possible. Most people have never heard of SBA acquisition loans, seller financing or business
brokers. They simply don't know that buying a business is an option for regular people. Now you do.""",
   "Person reading book", "NOT KNOWING IT'S POSSIBLE")
sc("""The fourth reason is fear of debt. Borrowing hundreds of thousands of dollars feels terrifying, and caution is healthy. But there's a
difference between debt used for a car that loses value and debt used to buy an asset that produces cash and repays the loan itself. The
question isn't whether debt is scary. It's whether the business can comfortably carry it, even in a bad year.""",
   "Contract signing pen", "FEAR OF DEBT")
sc("""The fifth reason is ego. Some people want the business to be entirely theirs, built their way, from the ground up. That's a valid
choice. But it's worth asking honestly whether you want to build something, or whether you want the income and freedom that ownership can
bring. If it's the second, buying may get you there years sooner.""",
   "Person thinking with notebook", "EGO")
pr("""The takeaway. Starting is more romantic. Buying is often more rational. Choose based on the outcome you want, not the story you want to
tell.""")

# ---------------- Angle 3 ----------------
short("Here are the eight steps to buy your first small business without getting burned.")
ch("Angle 3: The playbook")
pr("""Third angle. The playbook. How do you actually buy a business?""")
sc("""Step one. Get your finances ready. Know your credit score, savings and how much you could put down while keeping an emergency fund.
Step two. Choose industries that fit your skills and interests. Step three. Search for businesses through brokers, business for sale
websites, your local network and even by contacting owners directly.""",
   "Laptop searching listings", "STEPS 1 TO 3")
sc("""Step four. Analyze the numbers. Ask for at least three years of tax returns, profit and loss statements and bank statements. Step five.
Make an offer, usually a letter of intent, that sets the price and terms subject to due diligence. Step six. Do the due diligence with an
accountant and lawyer: verify financials, review leases and contracts, inspect equipment, and talk to key employees.""",
   "Tax forms on desk", "STEPS 4 TO 6")
sc("""Step seven. Arrange financing with an SBA lender or bank, and negotiate seller financing if possible. Step eight. Close, then manage the
transition carefully. Keep employees and customers informed, learn before you change, and use the seller's training period well.""",
   "Contract signing pen", "STEPS 7 AND 8")
sc("""Throughout all eight steps, build your team of advisors early: an accountant who understands small business acquisitions, a lawyer who
has handled purchase agreements, and a lender experienced with SBA deals. Their fees are small compared with the price of the business, and
the mistakes they help you avoid can be worth far more than they cost.""",
   "Accountant meeting client", "BUILD YOUR ADVISOR TEAM")
sc("""And give yourself permission to walk away. Most serious buyers look at dozens of businesses and make offers on several before one
works out. Walking away from a bad deal isn't failure. It's the most important skill a buyer can have.""",
   "Person standing at crossroads", "PERMISSION TO WALK AWAY")

# ---------------- Questions ----------------
ch("Questions people ask")
sc("""Question one. How much money do I need? It depends on the price, but SBA deals often require a down payment around ten percent, plus
closing costs and working capital. Many buyers also keep personal reserves. Question two. Should I use a business broker? Brokers can help
find deals, but they usually represent the seller. Your own accountant and lawyer represent you.""",
   "Calculator and coins", "HOW MUCH? BROKERS?")
sc("""Question three. What's a good first business to buy? Many first time buyers look for simple, steady businesses with recurring customers
and low dependence on the owner, like service companies. Question four. Can I keep my job while buying? Some people buy businesses with
managers in place, but most small businesses need an active owner, especially in the first year.""",
   "Person thinking with notebook", "FIRST BUSINESS? KEEP MY JOB?")
sc("""Question five. What if my credit isn't great? SBA lenders look at credit, experience and the business's cash flow. Improving your
credit and building savings for a year before buying can make a big difference. Seller financing can also help fill gaps. Question six. What
if the seller won't show tax returns? Walk away. Without verified numbers, you can't know what you're buying.""",
   "Person reading documents", "CREDIT? NO TAX RETURNS?")
sc("""Question seven. How long does buying a business take? From the first search to closing, many buyers take six months to a year or more.
Finding the right business takes time, and due diligence and financing can take several months. Patience is part of the process, and rushing
is how mistakes happen.""",
   "Calendar on desk", "HOW LONG DOES IT TAKE?")

# ---------------- Recap ----------------
ch("Recap")
sc("""Let's recap the fifteen reasons. Cash flow from day one. Proven survival. Banks lend on history. Seller financing. Trained employees.
Existing customers. Systems and suppliers. Brand and reputation. Real data. Retirements creating opportunities. Lower total cost of risk.
Room to improve. Training from the seller. A faster path to scale. And ownership without needing a brilliant idea.""",
   "Notebook with financial notes", "THE 15 REASONS")
sc("""And remember the risks. Overpaying, hidden problems, losing customers or employees, debt with personal guarantees, and simply not enjoying
ownership. The buyers who succeed are the ones who respect those risks: they verify the numbers, keep reserves, negotiate help from the seller
and take the first year slowly.""",
   "Person reading documents", "RESPECT THE RISKS")
sc("""Buying a business isn't a shortcut. It's a different path, one that trades a bigger check at the start for a much better chance of
success. For the right person, with the right business at the right price, it can be one of the fastest ways to go from earning a salary to
owning an asset that pays you for decades.""",
   "Established storefront", "A DIFFERENT PATH")

ch("What to do next")
pr("""If buying a business sounds interesting, start small. This week, browse a business for sale website for your area and run the numbers on
three listings, the way we did today. You'll learn more in an hour than most people learn in years. I'm Ryan Rover. Buy smart, and I'll see
you in the next video.""")

save("video16", "Why Buying a Business Beats Starting One: 15 Real Reasons", [
    "Bureau of Labor Statistics, Business Employment Dynamics (survival rates of new establishments: about 1 in 5 fail in year one, about half by year five)",
    "U.S. Small Business Administration, 7(a) loan program (business acquisitions, equity injection, personal guarantees)",
    "Example deal: simplified illustration ($120,000 owner earnings, 3x multiple, 10% down, 10-year loan at an illustrative 10.5% rate)",
], "buy vs start")
