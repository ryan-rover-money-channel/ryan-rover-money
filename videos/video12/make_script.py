import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short


def biz(n, title, sub, card_text, how, start, q1, c1, q2, c2):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"IDEA {n}")
    sc(how, q1, c1)
    sc(start, q2, c2)

# ---------------- Intro ----------------
ch("Intro")
short("You don't need a fortune to start a business. Here are twenty you can start with under five thousand dollars.")
pr("""Hi, I'm Ryan Rover. One of the biggest myths about starting a business is that you need a lot of money. A loan, investors, a
storefront, expensive equipment. For some businesses, sure. But for many of the most reliable small businesses in America, you can
start with less than five thousand dollars. Sometimes much less. Today, twenty of them.""")
card("""Twenty businesses you can start with under five thousand dollars. Real services people pay for, that you can test while
keeping your job.""",
     {"type": "stat", "label": "start-up budget", "big": "< $5,000", "sub": "20 businesses you can start in 2027"})
sc("""Here's the idea. Instead of betting your savings on one big idea, you start small, test whether people will pay, and grow only
when the customers are real. It's the opposite of the startup movie. Less glamour, much less risk. And many of the boring
businesses that quietly make millionaires started exactly this way: one person, a few tools, and a first customer.""",
   "Small business storefront", "START SMALL, TEST FAST")
sc("""For each business, we'll look at how it makes money and how to start cheaply. Then we'll look at the whole thing from three
angles: the numbers of starting small, the psychology of your first customers, and a simple ninety day playbook to go from idea to
paid. Let's start with the sources.""",
   "Notebook with financial notes", "20 IDEAS, 3 ANGLES")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Business application data comes from the U.S. Census Bureau's Business Formation Statistics. Pet spending data comes from the
American Pet Products Association. Self employment tax rules come from the IRS. Business survival data comes from the Bureau of Labor
Statistics. Start up costs in this video are rough estimates for a lean start, and they vary by city, licensing rules and the tools
you already own. This is education, not legal, tax or business advice.""",
   "Bureau of Labor Statistics building", "OUR SOURCES")

# ---------------- Angle 1: numbers ----------------
ch("Angle 1: The numbers")
pr("""Angle one. The numbers. Americans are starting businesses at a remarkable pace.""")
card("""The Census Bureau has recorded more than five million new business applications in each of the last several years, a big
jump from the years before twenty twenty.""",
     {"type": "stat", "label": "new business applications per year", "big": "5M+", "sub": "U.S. Census Bureau, Business Formation Statistics"})
sc("""Not every application becomes a real, lasting business. But it shows something important: starting a business has never been
easier. You can register online, take card payments on your phone, and find customers through local groups and free listings. The
barriers that used to keep people out, like storefronts and big ad budgets, are much lower for service businesses.""",
   "Online banking smartphone app", "EASIER THAN EVER")
sc("""Here's why starting under five thousand dollars matters so much. Remember, Bureau of Labor Statistics data shows about half of new
businesses are gone within five years. If you put fifty thousand dollars into a business that fails, you've lost years of savings. If
you put three thousand dollars into a business that fails, you've paid for an education. Small starts make failure survivable, and
survivable failure is how most successful owners learned.""",
   "Calculator with financial charts", "MAKE FAILURE SURVIVABLE")
card("""And remember taxes. Self employed people in the U.S. generally pay self employment tax of fifteen point three percent for Social
Security and Medicare, on top of income tax. Many new owners set aside twenty five to thirty percent of profit for taxes.""",
     {"type": "compare", "left": {"label": "Self-employment tax", "big": "15.3%", "sub": "Social Security + Medicare"},
      "right": {"label": "Set aside", "big": "25-30%", "sub": "of profit, rule of thumb"},
      "note": "IRS; your actual tax depends on your situation"})
sc("""That surprises a lot of people in their first year. They earn twenty thousand dollars on the side, spend it, and then get a big tax
bill in April. The fix is simple: open a separate account for taxes, and move a share of every payment into it the day it arrives.
Talk to a tax professional once, early, so you know what to expect.""",
   "Tax forms on desk", "THE APRIL SURPRISE")
sc("""Before the list, four questions to help you choose. Question one: what do you already have? A truck, a camera, a pressure washer,
a skill from your job? Starting with what you own is the cheapest start of all. Question two: how much time do you really have? Evenings,
weekends, or a few full days a week? Some businesses need daytime hours, others fit around a job.""",
   "Person standing at crossroads", "WHAT DO YOU HAVE?")
sc("""Question three: do you prefer physical work or screen work? Lawn care, cleaning and junk hauling are physical and outdoors.
Bookkeeping, social media and virtual assistance happen at a desk. Neither is better, but choosing the wrong one for your personality is a
fast way to burn out. And question four: do you want a side income, or a company? If you want to build something that can grow past you,
favor services with recurring customers that can be done by a team.""",
   "Notebook with financial notes", "WHAT DO YOU WANT?")
sc("""Keep your answers in mind as we go through the twenty. By the end, you'll probably have two or three that fit you much better than the
rest. That short list is where you start.""",
   "Person writing list notebook", "MAKE A SHORT LIST")
pr("""Okay. Twenty businesses under five thousand dollars. We'll start with services for homes, because every neighborhood needs them.""")

# ---------------- Businesses ----------------
biz(1, "House cleaning", "supplies and a good reputation",
"""Idea number one. Residential cleaning.""",
"""People are busy, and many will happily pay to come home to a clean house. Cleaning is one of the most recurring services there is:
weekly, every two weeks, or monthly. Once you have a list of regular clients, your income becomes predictable.""",
"""Lean start: cleaning supplies, a vacuum, basic insurance and maybe a simple website or listing. Often well under one thousand
dollars. Start with friends and neighbors, ask every happy client for a review and a referral, and offer a discount for recurring
bookings.""",
"House cleaning", "RECURRING CLIENTS",
"Cleaning supplies", "UNDER $1,000 TO START")

biz(2, "Pressure washing", "dramatic before and after",
"""Idea number two. Pressure washing.""",
"""Driveways, decks, fences, siding, storefronts. The before and after photos do your marketing for you. Homeowners book it once or
twice a year, and businesses like restaurants and property managers can book it on a regular schedule.""",
"""Lean start: a good pressure washer, surface cleaner, hoses, safety gear and insurance. A few thousand dollars can get you going.
Learn proper techniques first, because too much pressure can damage wood and siding. Post every before and after photo, with the
customer's permission.""",
"Pressure washing driveway", "BEFORE AND AFTER",
"Hose water spray", "LEARN TECHNIQUE FIRST")

biz(3, "Lawn care", "weekly routes",
"""Idea number three. Lawn care.""",
"""Mowing, edging, leaf cleanup, mulch. In the growing season, lawns need attention every week. A route of houses close together means
less driving and more jobs per day, which is how lawn businesses become profitable.""",
"""Lean start: a reliable mower, trimmer, blower and a way to haul them. If you already have a truck, you can start for a couple of
thousand dollars, or less with used equipment. Focus on one neighborhood at a time, and add snow removal or leaf cleanup to stay busy
in the off season.""",
"Lawn mower grass", "WEEKLY ROUTES",
"Snow plow truck", "ADD OFF-SEASON WORK")

biz(4, "Handyman services", "small jobs nobody else wants",
"""Idea number four. Handyman services.""",
"""Hanging shelves, fixing doors, patching drywall, assembling furniture, mounting TVs. Larger contractors often don't want small jobs,
which leaves a big gap for a reliable handyman. Real estate agents and landlords often need someone they can call regularly.""",
"""Lean start: tools you probably already have, plus insurance. Check your state's rules, because some types of work require a license
above a certain dollar amount. Be clear about what you do and don't do, and never take on electrical or plumbing work you're not
licensed for.""",
"Handyman tools", "THE SMALL JOBS GAP",
"Toolbox", "KNOW YOUR LIMITS")

biz(5, "Window and gutter cleaning", "ladders and repeat business",
"""Idea number five. Window and gutter cleaning.""",
"""Gutters need cleaning once or twice a year, and storefronts want clean windows weekly or monthly. It's simple work, and happy
customers rebook year after year.""",
"""Lean start: ladders, safety equipment, cleaning tools and insurance, often under two thousand dollars. Safety is critical, so get
proper training and never cut corners on ladders. Offer an annual plan, and book next year's visit before you leave.""",
"Window cleaning ladder", "REPEAT BUSINESS",
"Gutter cleaning house", "BOOK NEXT YEAR NOW")

biz(6, "Holiday light installation", "a seasonal cash burst",
"""Idea number six. Holiday light installation.""",
"""Many homeowners love holiday lights but hate climbing ladders in the cold. Installation services put them up, take them down and
store them. It's seasonal, but it can be a strong burst of income in the fall and winter, and it pairs well with gutter cleaning.""",
"""Lean start: ladders, clips, safety gear, insurance, and either customer lights or lights you rent to them. Market early, in
September and October. Offer removal and storage as part of the package, so customers come back automatically next year.""",
"Christmas lights on house", "SEASONAL BURST",
"Window cleaning ladder", "PAIR IT WITH GUTTERS")

biz(7, "Junk hauling and moving help", "strong backs and a truck",
"""Idea number seven. Junk hauling and moving help.""",
"""Moves, cleanouts, renovations. People pay to have things lifted, loaded and taken away. If you have a truck or can rent one, you
can start offering junk removal and moving labor quickly.""",
"""Lean start: if you own a pickup or can rent a truck, mainly insurance, straps, dollies and dump fees. Price carefully to cover fuel,
dump charges and your time. Relationships with real estate agents and property managers can bring steady work.""",
"Junk removal truck", "LIFT AND HAUL",
"Moving truck boxes", "PRICE FOR DUMP FEES")

pr("""Now, services for people and their pets.""")

short("Americans spend about one hundred fifty billion dollars a year on their pets. Here's how to get a piece.")
biz(8, "Pet sitting and dog walking", "a market of billions",
"""Idea number eight. Pet sitting and dog walking.""",
"""The American Pet Products Association reported that Americans spent about one hundred fifty billion dollars on their pets in twenty
twenty four. Busy owners need dogs walked, pets fed while they travel, and someone trustworthy to check in.""",
"""Lean start: almost nothing beyond insurance, a basic pet first aid course, and maybe a background check to build trust. Apps can
help you find first clients, then you can build your own direct client list. Reliability and great communication, like photos after
every visit, are what build loyal customers.""",
"Dog walker park", "~$150B ON PETS",
"Cat sitting home", "RELIABILITY WINS")

biz(9, "Mobile car detailing", "bring the car wash to them",
"""Idea number nine. Mobile car detailing.""",
"""Instead of customers driving to a car wash, you go to them, at home or at work, and clean their car inside and out. Busy people pay
for convenience, and a full interior detail can command a solid price.""",
"""Lean start: a vacuum, extractor, cleaning products, towels and a water source plan, often a couple of thousand dollars. Check local
rules on water runoff. Offer monthly maintenance packages for regular customers, and approach small businesses that own vehicle
fleets.""",
"Car detailing", "CONVENIENCE SELLS",
"Car interior cleaning", "MONTHLY PACKAGES")

biz(10, "Tutoring", "your knowledge is the product",
"""Idea number ten. Tutoring.""",
"""Parents spend money on test prep, math help, reading support and music lessons. If you're strong in a subject, tutoring can pay well
per hour, and online sessions mean you're not limited to your town.""",
"""Lean start: almost free if you already have a laptop and internet. A simple website, a few reviews from early students, and
relationships with local schools or parent groups can fill your schedule. Specializing, like SAT math or adult English learners, often
lets you charge more.""",
"Tutor teaching student", "KNOWLEDGE IS THE PRODUCT",
"Student studying laptop", "SPECIALIZE TO EARN MORE")

biz(11, "Personal training", "fitness, one client at a time",
"""Idea number eleven. Personal training.""",
"""People pay for accountability and expertise to get fit. Trainers work in clients' homes, in parks, online, or in gyms that allow
independent trainers.""",
"""Lean start: a recognized certification, insurance, and basic equipment like bands and weights. Often under two thousand dollars in
total. Start with small group sessions in a park to lower the price per person and raise your hourly earnings.""",
"Personal trainer gym", "ACCOUNTABILITY SELLS",
"Group workout park", "SMALL GROUPS")

pr("""Quick pause. If one of these businesses is speaking to you, tell me which one in the comments. And subscribe, because this series
keeps going with how to buy a business, the real numbers behind laundromats and car washes, and side hustles that turn into real
companies. Now, idea twelve. The next few you can run from a laptop.""")

biz(12, "Bookkeeping", "monthly clients, recurring revenue",
"""Idea number twelve. Bookkeeping.""",
"""Small businesses need their books kept, receipts categorized and accounts reconciled, every single month. Monthly bookkeeping clients
are recurring revenue, and once you've set up a client, the work becomes routine.""",
"""Lean start: accounting software training or certification, which some providers offer at low cost, and a laptop. Start with a few
small businesses you know personally. Be clear about where bookkeeping ends and tax advice begins, and partner with a tax professional
for the rest.""",
"Accountant desk calculator", "MONTHLY CLIENTS",
"Laptop spreadsheet", "PARTNER WITH A CPA")

biz(13, "Social media management", "local businesses need help",
"""Idea number thirteen. Social media management for local businesses.""",
"""Restaurants, salons, contractors and shops know they should post online, but they're too busy. Managing their accounts for a monthly
fee creates recurring revenue.""",
"""Lean start: a phone, a laptop and free or cheap design tools. Build a portfolio by helping one or two businesses at a low rate, and
show real results, like more bookings or more calls. Focus on one industry, like restaurants, so you become the expert.""",
"Social media smartphone", "BUSY OWNERS NEED HELP",
"Restaurant owner", "PICK ONE INDUSTRY")

biz(14, "Virtual assistant", "admin work, from anywhere",
"""Idea number fourteen. Virtual assistant services.""",
"""Email, scheduling, customer service, data entry, research. Busy professionals and small business owners pay for help with tasks that
eat their time. You can do this from anywhere with internet.""",
"""Lean start: a laptop, internet and a professional profile. Start with hourly work, then move to monthly retainers once clients trust
you. Specializing, like assisting real estate agents or podcasters, can raise your rates.""",
"Person working from home laptop", "TIME IS WHAT YOU SELL",
"Calendar planning", "RETAINERS OVER HOURS")

biz(15, "Resume and career services", "help people get hired",
"""Idea number fifteen. Resume writing and career coaching.""",
"""People pay for help when they're changing careers, applying for promotions or coming back after a gap. A strong resume and interview
practice can change someone's income, which makes the service easy to value.""",
"""Lean start: a laptop and examples of your work. If you have experience in hiring or in a specific industry, lead with that.
Testimonials from clients who got hired are your best marketing.""",
"Job interview handshake", "HELP PEOPLE GET HIRED",
"Person writing list notebook", "TESTIMONIALS SELL")

biz(16, "Photography", "events, families, businesses",
"""Idea number sixteen. Photography.""",
"""Families, graduations, real estate listings, small business products, local events. If you already own a decent camera and know how
to use it, you can start booking paid work.""",
"""Lean start: if you own a camera and lens, mainly editing software and insurance. Real estate photography can be especially steady,
because agents need photos for every listing. Build a portfolio with a few free or discounted shoots, then raise prices as demand
grows.""",
"Photographer camera", "STEADY REAL ESTATE WORK",
"House with for sale sign", "AGENTS NEED PHOTOS")

pr("""And the last four: buying, selling and specialty services.""")

biz(17, "Reselling and flipping", "buy low, sell online",
"""Idea number seventeen. Reselling.""",
"""Some people make real income buying underpriced items at thrift stores, garage sales and estate sales, and reselling them online.
Furniture, tools, vintage clothing, electronics. The skill is knowing what sells and for how much.""",
"""Lean start: a few hundred dollars of inventory and a phone for photos. Start with a category you know well. Track every purchase and
sale, because profit is what's left after fees, shipping and your time. Reinvest profits into inventory to grow.""",
"Garage sale items", "BUY LOW, SELL HIGH",
"Cardboard boxes moving", "KNOW YOUR CATEGORY")

biz(18, "Furniture flipping", "sanding, paint, profit",
"""Idea number eighteen. Furniture flipping.""",
"""Old solid wood dressers, tables and chairs can be bought cheaply, refinished, and sold for much more. People love unique, sturdy
furniture, and a good flip can sell quickly online.""",
"""Lean start: sanders, paint, hardware and a place to work, like a garage. Start with one piece, document the transformation, and post
it. Many flippers find their before and after posts become their best advertising.""",
"Furniture restoration", "SAND, PAINT, PROFIT",
"Wooden dresser", "DOCUMENT IT")

biz(19, "Notary and loan signing", "paperwork that has to be signed",
"""Idea number nineteen. Mobile notary and loan signing agent.""",
"""Mortgages, refinances, real estate deals and legal documents need a notary. Mobile notaries travel to clients, and loan signing agents
guide borrowers through closing documents for title and escrow companies.""",
"""Lean start: your state's notary commission, training, a bond and errors and omissions insurance where required. Costs are often a few
hundred dollars. Requirements vary a lot by state, so check your state's rules first. Building relationships with title companies is the
key to steady work.""",
"Signing documents", "PAPERWORK MUST BE SIGNED",
"Lawyer office documents", "TITLE COMPANY RELATIONSHIPS")

biz(20, "Errand and delivery services", "time is what people buy",
"""Idea number twenty. Errand and senior assistance services.""",
"""Groceries, prescriptions, dry cleaning, rides to appointments. Older adults and busy families often need help with errands. A trusted
local errand service can build loyal, recurring clients.""",
"""Lean start: a reliable car, insurance that covers business use, and a background check to build trust. Partner with senior centers or
local churches to find clients. Reliability and kindness are the whole business.""",
"Grocery bags delivery", "TIME IS WHAT PEOPLE BUY",
"Senior woman smiling", "TRUST AND KINDNESS")

# ---------------- Three starters ----------------
short("Three people started a business with less than three thousand dollars. Here's what happened.")
ch("Three example starters")
pr("""Let's see how this works in practice. Three example people, made up but realistic, each starting with less than three thousand
dollars.""")
sc("""Brianna, twenty six, works as a receptionist. She starts cleaning houses on Saturdays with six hundred dollars of supplies. Her
first three clients are her coworkers' parents. She asks every client for a review, and within six months she has eight recurring
clients, about two Saturdays a week. She sets aside thirty percent for taxes and invests a big part of the rest. After a year, she
hires a helper and starts thinking about leaving her job.""",
   "House cleaning", "BRIANNA: CLEANING")
sc("""Tom, forty one, is an accountant at a mid sized company. He starts bookkeeping for three small businesses in the evenings, using
software he already knows. Each client pays a monthly fee. After two years, he has a dozen clients, and his side income rivals a good
part of his salary. He's in no rush to quit. The extra income goes straight into his retirement accounts and his kids' college fund.""",
   "Accountant desk calculator", "TOM: BOOKKEEPING")
sc("""Rosa, fifty five, recently retired from teaching. She becomes a mobile notary and loan signing agent, spending a few hundred dollars
on her commission, training and insurance. She builds relationships with two local title companies and works three or four days a week
on her own schedule. The extra income lets her delay Social Security, which raises her future monthly benefit.""",
   "Signing documents", "ROSA: NOTARY")
sc("""Three different people, three different reasons. Brianna wants to build a company. Tom wants to accelerate his wealth. Rosa wants
flexible income in early retirement. None of them risked their savings. All of them started with what they already had: skills,
relationships and a few hundred to a few thousand dollars.""",
   "Three people silhouettes", "START WITH WHAT YOU HAVE")
sc("""Notice also what they did with the money. Brianna invested a big share. Tom sent it to retirement and college savings. Rosa used it to
delay Social Security. A side business is most powerful when its income has a job. Without a plan, side income tends to disappear into
everyday spending, and a year later there's nothing to show for all those extra hours. Decide before the first payment arrives where the
money will go.""",
   "Piggy bank coins", "GIVE THE MONEY A JOB")

# ---------------- Pricing ----------------
short("Most new business owners charge too little. Here's how to price your service.")
ch("How to price your service")
pr("""Before the psychology, let's talk about the one decision that makes or breaks small service businesses: price.""")
sc("""Start with what competitors charge. Call three local businesses offering the same service and ask for a quote, or look at their
websites and reviews. That gives you a range. As a beginner, you might start slightly below the middle of that range, but almost never
at the bottom. The cheapest price attracts the customers who complain most and pay slowest.""",
   "Phone call customer service", "KNOW THE MARKET")
sc("""Then do your own math. Add up your real costs per job: supplies, fuel, insurance spread across your jobs, equipment wear, payment
processing fees, and taxes. Then decide what you want to earn per hour of your time, including driving and admin. If the market price
doesn't cover that, either the business doesn't work for you, or you need to work more efficiently, for example with tighter routes.""",
   "Calculator and pen on financial papers", "DO YOUR OWN MATH")
sc("""Next, think in packages, not hours. Customers understand a clear price for a clear result: a full house clean, a driveway and
sidewalk wash, a monthly bookkeeping package. Packages also reward you for getting faster. If you charge by the hour, getting better at
your job lowers your income. If you charge by the result, getting better raises it.""",
   "Notebook with financial notes", "PACKAGES, NOT HOURS")
sc("""And finally, raise prices regularly. Many owners raise prices for new customers first, then for existing customers once a year, with
plenty of notice. If nobody ever pushes back on your price, it's probably too low. A few lost price sensitive customers are often
replaced by better ones who value quality.""",
   "Graph trending upward", "RAISE PRICES REGULARLY")

# ---------------- Free marketing ----------------
ch("Eight free ways to get customers")
pr("""You don't need an advertising budget to get your first fifty customers. Here are eight free or nearly free ways local service
businesses find clients.""")
sc("""One. Tell everyone you know. Friends, family, coworkers, your gym, your church. Most first customers come from people who already
trust you. Two. Free business listings. Set up a free business profile on major map and search services so people searching nearby can
find you. Three. Local community groups online, where neighbors ask for recommendations every day.""",
   "Social media smartphone", "WAYS 1 TO 3")
sc("""Four. Before and after photos, posted everywhere, with permission. They show your work better than any description. Five. Door
hangers or flyers in the exact neighborhood where you just did a job. Neighbors see your work, and they're nearby, so your routes get
tighter. Six. Partnerships. Real estate agents, property managers, contractors and other small businesses can send you steady work, and
you can send work back to them.""",
   "Pressure washing driveway", "WAYS 4 TO 6")
sc("""Seven. Ask for reviews, every time. Make it easy with a direct link. Reviews compound: each one makes the next customer more likely to
choose you. And eight. Ask for referrals, and reward them. A small discount for both the customer and the friend they refer can turn
every happy client into a salesperson.""",
   "Business meeting handshake", "WAYS 7 AND 8")
sc("""The pattern is simple. Do great work, make it visible, and ask for the next customer. It's not glamorous, but it's how most local
service businesses grow, especially in the first year, before they ever spend a dollar on ads.""",
   "Small business owner smiling", "GREAT WORK, MADE VISIBLE")

# ---------------- Stages ----------------
ch("From side hustle to real business")
pr("""Most of these businesses go through the same five stages. Knowing them helps you see where you are and what comes next.""")
sc("""Stage one. The test. You're doing the work yourself, a few hours a week, and finding out whether people will pay. The goal is
proof, not profit. Stage two. The side income. You have regular customers, and the business pays a few hundred to a few thousand dollars a
month. You're still working your job, and the extra money goes toward savings and investing.""",
   "Person working from home laptop", "STAGES 1 AND 2")
sc("""Stage three. The decision. The business has grown to the point where it competes with your job for time. This is where many owners
either stay part time on purpose, or plan a careful leap, with an emergency fund and several months of steady business income. Stage four.
The first hire. You bring in a helper or an employee, and your role starts shifting from doing the work to managing it.""",
   "Construction workers", "STAGES 3 AND 4")
sc("""And stage five. The asset. The business runs on systems and a team, with recurring customers and clean records. At this point, it's
not just income. It's something with real value that could be sold one day. Not every business needs to reach stage five. But knowing it
exists changes how you build from day one.""",
   "Factory machine gears", "STAGE 5: THE ASSET")

# ---------------- Angle 2: psychology ----------------
ch("Angle 2: The psychology")
pr("""Angle two. The psychology. The hardest part of starting a small business usually isn't money. It's in your head.""")
sc("""The first obstacle is waiting until you feel ready. People spend months on logos, websites and business plans before they've ever
talked to a customer. But you learn more from your first paying customer than from any amount of planning. Start with the smallest
version of your service, and improve it as you go.""",
   "Person thinking by window", "YOU'LL NEVER FEEL READY")
sc("""The second is fear of asking. Asking friends, neighbors or local businesses for work feels awkward. But most people are glad to help
someone they know, and word of mouth is still the most powerful marketing for local services. Try a simple message: I'm starting a
pressure washing service. If you know anyone who needs it, I'd really appreciate a referral.""",
   "Friends talking coffee", "JUST ASK")
sc("""The third is underpricing. New owners often charge too little because they feel like beginners. But low prices attract the most
difficult customers and leave no room for taxes, insurance and equipment. Price for the value you deliver, and raise prices as your
reviews grow.""",
   "Receipt and coins on table", "DON'T UNDERPRICE")
sc("""And the fourth is quitting too early. The first few months are often slow. Many people give up right before word of mouth starts to
work. Give a new service business at least six months of consistent effort before deciding whether it works. Track what brings in
customers, and do more of that.""",
   "Long road desert", "GIVE IT SIX MONTHS")
sc("""And the fifth obstacle is comparison with people online. Social media is full of young entrepreneurs claiming they made ten thousand
dollars in their first month. Some are real. Many are selling courses. Comparing your quiet, steady progress to someone's highlight reel is
a fast way to feel like a failure while you're actually doing fine. The only comparison that matters is your business this month versus
your business three months ago. If that line is going up, you're winning.""",
   "Social media smartphone", "IGNORE THE HIGHLIGHT REELS")
sc("""Underneath all of these obstacles is one simple truth: action beats thinking. The people who build successful small businesses aren't
always the smartest or the most talented. They're the ones who started before they felt ready, asked for work even when it was awkward,
charged fair prices, and kept going through the slow months.""",
   "Person running on road", "ACTION BEATS THINKING")

# ---------------- Angle 3: playbook ----------------
short("Here's a ninety day plan to go from business idea to paying customers.")
ch("Angle 3: The 90 day playbook")
pr("""Angle three. The playbook. Here's a simple ninety day plan to go from idea to paying customers, while keeping your job.""")
sc("""Days one to fifteen. Pick one business from this list that matches your skills, your schedule and your budget. Check licensing and
insurance requirements in your city and state. Set up a separate bank account. And write down your price list, based on what local
competitors charge.""",
   "Notebook with financial notes", "DAYS 1 TO 15: PICK AND PREPARE")
sc("""Days sixteen to thirty. Get your first three customers. Ask friends, family and neighbors. Post in local community groups. Offer a
small launch discount in exchange for an honest review. Do outstanding work, take before and after photos, and ask each customer who
else might need your service.""",
   "Business meeting handshake", "DAYS 16 TO 30: FIRST 3 CUSTOMERS")
sc("""Days thirty one to sixty. Build systems. A simple booking method, a template for quotes and invoices, a checklist for every job, and
a way to collect reviews. Move a share of every payment into your tax account automatically. And track where each customer came from.""",
   "Clock gears mechanism", "DAYS 31 TO 60: SYSTEMS")
sc("""Days sixty one to ninety. Grow what works. If referrals bring the most customers, ask for more referrals. If one neighborhood books
the most, focus there. Raise prices slightly for new customers. And decide on your goal for the next six months: more income, more
recurring clients, or your first helper.""",
   "Graph trending upward", "DAYS 61 TO 90: GROW")
sc("""And one rule throughout: protect your foundation. Keep your emergency fund, keep contributing to retirement, and don't take on debt
to grow a business that hasn't proven itself yet. The beauty of starting under five thousand dollars is that you never have to bet your
family's security on it.""",
   "Piggy bank coins", "PROTECT YOUR FOUNDATION")

# ---------------- Mistakes ----------------
ch("Six mistakes new owners make")
pr("""Starting cheap protects you from big losses. But there are still mistakes that can sink a small business in its first year. Here
are six of the most common.""")
sc("""Mistake one. Skipping insurance. One damaged driveway, one dropped TV, one injured dog, and a single claim could wipe out a year of
profit or more. General liability insurance is often affordable for small service businesses, and some clients require it. Mistake two.
Mixing business and personal money. It makes taxes painful and hides whether you're actually profitable.""",
   "Paperwork documents desk", "MISTAKES 1 AND 2")
sc("""Mistake three. Buying too much equipment too early. The top of the line mower, the van with custom graphics, the expensive camera.
Start with what you need to do good work, and upgrade only when customers are paying for it. Mistake four. Saying yes to every job. Jobs
far away, jobs outside your skills, or jobs from customers who haggle aggressively often cost more than they pay.""",
   "Lawn mower grass", "MISTAKES 3 AND 4")
sc("""Mistake five. Forgetting about taxes until April. We talked about this, but it bears repeating. Set aside a share of every payment,
and consider paying estimated taxes during the year, as the IRS generally expects from self employed people. And mistake six. Not
tracking anything. Without knowing your revenue, costs and where customers come from, you can't tell what's working.""",
   "Tax forms on desk", "MISTAKES 5 AND 6")
sc("""Every one of these mistakes is cheap to avoid and expensive to make. Insurance, a separate account, modest equipment, clear rules
about which jobs you take, a tax account, and a simple spreadsheet. That's the whole defensive playbook, and it costs less than a
weekend away.""",
   "Spreadsheet on laptop", "CHEAP TO AVOID")

# ---------------- Tools ----------------
ch("Simple tools that keep costs low")
pr("""You don't need expensive software to run a small business. Here's a lean toolkit many owners use.""")
sc("""For money: a separate business checking account, a separate savings account for taxes, and a simple way to take card payments on your
phone. For bookkeeping, a spreadsheet works at the start, and low cost accounting software makes sense once you have regular clients. For
scheduling, a shared calendar or a basic booking tool is plenty.""",
   "Online banking smartphone app", "MONEY AND SCHEDULING")
sc("""For marketing: a free business profile on map and search services, a simple one page website, and a phone full of before and after
photos. For customer communication, templates for quotes, reminders and thank you messages save hours every week. And for learning, free
online courses and videos from experienced owners in your industry.""",
   "Laptop online banking", "MARKETING AND LEARNING")
sc("""The point is to keep fixed costs close to zero until revenue is real. Every subscription and every monthly fee raises the amount you
need to earn before you make a single dollar of profit. Lean businesses survive slow months. Bloated ones don't.""",
   "Receipt and coins on table", "KEEP FIXED COSTS LOW")

# ---------------- Questions ----------------
ch("Questions people ask")
pr("""Let me answer the questions people ask most about starting small.""")
sc("""Question one. Do I need an LLC? Not always to start, but many owners form one for liability protection and simpler separation of
finances. Rules and fees vary by state. Insurance is often just as important as the legal structure. Question two. How do I find my first
customers? People you know, local online groups, neighborhood apps, and simple flyers still work for local services.""",
   "Paperwork documents desk", "LLC? FIRST CUSTOMERS?")
sc("""Question three. What if my employer has a policy about side businesses? Read your employment agreement, especially if your business
is related to your job. Keep your business completely separate from work time and work equipment. Question four. When should I quit my job?
Many people wait until the business has replaced a large share of their salary for several months in a row, and they have a solid
emergency fund.""",
   "Office building at dusk", "EMPLOYER RULES? WHEN TO QUIT?")
sc("""Question five. Which one makes the most money? The ones that can grow beyond your own hours, through recurring clients, routes and
eventually employees, tend to have the highest ceiling: cleaning, lawn care, pressure washing, bookkeeping. Services where you sell only
your time, like tutoring or virtual assistance, are easier to start but harder to scale.""",
   "Graph trending upward", "WHICH MAKES THE MOST?")
sc("""Question six. Can I do this with no experience? For many of these, yes, with some learning first. Cleaning, lawn care, pet sitting and
reselling have low skill barriers, though quality and reliability still matter. Others, like bookkeeping, tutoring and personal training,
need real knowledge or a certification. Be honest with customers about your experience, and price accordingly while you learn.""",
   "Person studying laptop at night", "NO EXPERIENCE?")
sc("""Question seven. How much can I realistically earn? It varies enormously by city, service and effort, so be skeptical of anyone who
promises a specific number. A realistic first goal for most people is a few hundred dollars a month in the first few months, growing as
reviews and referrals build. The businesses that grow biggest are the ones whose owners keep showing up for years, not months.""",
   "Calculator with financial charts", "HOW MUCH CAN I EARN?")

# ---------------- Recap ----------------
ch("Recap: 20 businesses under $5,000")
sc("""Let's recap. Home services: house cleaning, pressure washing, lawn care, handyman, window and gutter cleaning, holiday lights, and junk
hauling. People and pets: pet sitting, mobile car detailing, tutoring and personal training.""",
   "Notebook with financial notes", "IDEAS 1 TO 11")
sc("""Laptop businesses: bookkeeping, social media management, virtual assistance, resume services and photography. And buying, selling and
specialty services: reselling, furniture flipping, mobile notary, and errand services.""",
   "Small business storefront", "IDEAS 12 TO 20")
sc("""And the three angles. The numbers: over five million business applications a year, about half of businesses gone in five years, so
start small to make failure survivable, and set aside money for taxes. The psychology: you'll never feel ready, ask for work, don't
underprice, and give it six months. And the playbook: ninety days from idea to paying customers, while protecting your foundation.""",
   "Map and compass", "NUMBERS, PSYCHOLOGY, PLAYBOOK")
sc("""And here's the bigger picture. A small business you start for under five thousand dollars might stay small forever, and that's
fine. Even a few hundred dollars a month, invested over twenty years, can grow into a meaningful sum. Or it might grow into something much
bigger. Either way, you'll learn skills no job teaches: selling, pricing, managing money and solving problems on your own. Those skills
stay with you, whatever you do next.""",
   "Sunrise over mountains", "SKILLS THAT STAY")

# ---------------- Close ----------------
ch("What to do next")
pr("""So here's your homework. Pick one idea. Just one. And this week, tell three people you're offering it. That's it. Your first
customer is closer than you think. If you want the full plan for building wealth, it's in my playbook, link in the description. I'm
Ryan Rover. See you in the next one.""")

save("video12", "20 Businesses You Can Start With Under $5,000 in 2027", [
    "U.S. Census Bureau, Business Formation Statistics (more than 5 million business applications a year in recent years)",
    "Bureau of Labor Statistics, Business Employment Dynamics (about half of new establishments survive five years)",
    "IRS, Self-Employment Tax (15.3% for Social Security and Medicare)",
    "American Pet Products Association, U.S. pet industry spending 2024 (about $150 billion)",
    "Social Security Administration, delayed retirement credits",
    "Start-up costs: rough estimates for a lean start; they vary by location and licensing",
], "20 businesses under $5,000")
