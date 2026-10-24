import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short


def biz(n, name, sub, a, b, c, q1, c1, q2, c2, q3, c3):
    ch(f"{n}. {name}")
    card(f"Number {n}. {name}. {sub}", {"type": "list", "n": n, "title": name, "sub": sub}, f"UGLY BUSINESS {n}")
    sc(a, q1, c1)
    sc(b, q2, c2)
    sc(c, q3, c3)

# ---------------- Intro ----------------
ch("Intro")
short("The businesses nobody wants are often the ones quietly making people rich.")
pr("""Hi, I'm Ryan Rover. Everybody wants to own a coffee shop, a clothing brand, or a cool app. Almost nobody dreams of owning a septic
pumping company, a dumpster rental yard, or a business that cleans up after hoarders. And that's exactly the point. Today we're going
through fifteen ugly businesses nobody wants, why they can make real money, and what it actually takes to run them. By the end, you'll
understand why the dirtiest jobs often have the cleanest profits.""")
card("""Fifteen ugly businesses nobody wants, and why they can print cash for the people willing to do them.""",
     {"type": "stat", "label": "ugly businesses", "big": "15", "sub": "dirty jobs, clean profits"})
sc("""Here's the simple idea behind this whole video. Profit lives where competition is weak. Glamorous businesses attract crowds of
competitors, which pushes prices down and costs up. Ugly businesses scare most people away. Fewer competitors means customers often
pay fair prices, stay loyal, and call you back, because there aren't many other options.""",
   "Garbage truck on street", "PROFIT LIVES WHERE COMPETITION IS WEAK")
sc("""An important warning before we start. Any numbers in this video are rough illustrations to explain how these businesses work, not
promises or industry averages. Results depend heavily on your location, pricing, licensing, competition and how well you run things.
Some of these businesses need permits, insurance, special training, or expensive equipment. Always do your homework.""",
   "Calculator and pen on financial papers", "ILLUSTRATIONS, NOT PROMISES")
sc("""We'll go through all fifteen, then look at them from three angles. The numbers, meaning what makes the money work. The psychology,
meaning why most people avoid these businesses and why that's an advantage. And the playbook, meaning how to choose one and get
started without betting everything you own.""",
   "Notebook with financial notes", "15 BUSINESSES, 3 ANGLES")
pr("""Put on your gloves. Let's get into it.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Employment and wage information comes from the Bureau of Labor Statistics Occupational Outlook Handbook. Small business lending
information comes from the U.S. Small Business Administration. Example prices and margins are simplified illustrations we built for
teaching, not quotes from real companies. This video is education, not financial, legal or business advice.""",
   "Government building", "SOURCES")

# ---------------- The 15 ----------------
biz(1, "Septic tank pumping", "a job nobody wants, a need nobody can skip",
    """Number one. Septic tank pumping. Millions of American homes, especially in rural and suburban areas, aren't connected to city sewer
lines. They rely on septic tanks, which need to be pumped every few years, plus inspections when homes are sold. Nobody looks forward
to that job, but nobody can skip it either.""",
    """Why it works. The demand is steady and built into how homes function. Many jobs are scheduled maintenance, which creates repeat
customers, and emergencies can command higher prices. Real estate transactions often require inspections, which adds another source of
work. And once a customer finds a reliable company, they rarely shop around.""",
    """The catch. You need a pump truck, which is expensive, plus licenses and a place to legally dispose of the waste, which may charge
fees. It's physical, smelly work in all kinds of weather. But for owners who build a route of recurring customers, it can be a very
steady business.""",
    "Truck on rural road", "STEADY, UNSKIPPABLE DEMAND",
    "House with yard", "REPEAT CUSTOMERS",
    "Truck on rural road", "TRUCK, LICENSES, DISPOSAL")

biz(2, "Dumpster rental", "renting a metal box, again and again",
    """Number two. Dumpster rental. Contractors, roofers, people renovating, people moving, people cleaning out a parent's house. They all
need somewhere to put a mountain of debris. A dumpster rental company drops off a roll off container, picks it up full, and hauls it to
a landfill or transfer station.""",
    """Why it works. A steel container can be rented over and over for many years. Each rental pays for delivery, pickup, and disposal, plus
a margin. Once the containers are paid off, much of the revenue goes toward fuel, disposal fees, labor and truck costs, with the rest as
profit. Contractors who like your service become repeat customers.""",
    """The catch. Roll off trucks and containers cost real money, landfill fees can rise, and you need to manage scheduling carefully so
containers aren't sitting idle. Weight limits and banned materials also cause disputes. But it's a simple business to understand, and
many owners start with a few containers and grow from there.""",
    "Construction site", "CONTAINERS RENTED AGAIN AND AGAIN",
    "Construction workers on site", "CONTRACTORS COME BACK",
    "Garbage truck on street", "WATCH FEES AND IDLE TIME")

biz(3, "Grease trap cleaning", "restaurants are required to do it",
    """Number three. Grease trap cleaning. Restaurants produce fats, oils and grease that would clog city sewers. So many cities require
restaurants to install grease traps and have them cleaned on a regular schedule. That makes this a recurring service that customers are
often required to buy.""",
    """Why it works. Required maintenance on a schedule is one of the best business models there is. A route of restaurants that need
service every month or every few months creates predictable revenue. Some companies also collect used cooking oil, which can sometimes
be sold for recycling into biofuels.""",
    """The catch. The work is messy, often done at night after restaurants close, and you need the right truck, permits and disposal
arrangements. Restaurants also open and close frequently, so you need to keep finding new customers. But the recurring nature of the
work makes it a quietly attractive business.""",
    "Restaurant kitchen", "REQUIRED, RECURRING SERVICE",
    "Restaurant kitchen", "PREDICTABLE ROUTES",
    "City street at night", "NIGHT WORK, MESSY WORK")

short("This is the cleanup business that charges premium prices because nobody else will do it.")
biz(4, "Biohazard and trauma cleanup", "the hardest job on this list",
    """Number four. Biohazard and trauma cleanup. After a crime, an accident, an unattended death, or a hoarding situation, someone has to
clean and decontaminate the property. It's emotionally and physically demanding work that requires training, protective equipment and
careful disposal of hazardous materials.""",
    """Why it works. Very few people are willing to do this work, and those who need it are usually in a crisis, so they value speed,
discretion and compassion more than price. In some situations, insurance may cover part of the cost. That combination can support
premium pricing compared with normal cleaning.""",
    """The catch. This isn't just a business, it's a heavy emotional load. You need proper training, insurance, safety procedures and
compliance with health and environmental rules. Relationships with property managers and others who encounter these situations matter.
For the right person, it can be meaningful and well paid work, but it isn't for everyone.""",
    "Protective suit worker", "TRAINING AND PROTECTION REQUIRED",
    "Insurance documents", "PREMIUM PRICING",
    "Person standing at crossroads", "NOT FOR EVERYONE")

biz(5, "Pest control", "customers pay to make problems disappear",
    """Number five. Pest control. Termites, roaches, rodents, bed bugs, wasps. People will pay almost anything to make these problems
disappear, and quickly. Pest control is a huge industry with a mix of national brands and many local operators.""",
    """Why it works. Pest control often turns into recurring service plans, with technicians visiting quarterly or monthly. Recurring plans
make revenue predictable and raise the value of the business if you ever sell. Commercial customers like restaurants, warehouses and
apartment buildings may need regular service by contract.""",
    """The catch. You'll need licensing, training on chemicals and safety, and insurance. Customers expect results, and some pests are
stubborn. But compared with many businesses, the startup costs can be moderate, and a local company with great service can compete well
against bigger brands.""",
    "Exterminator spraying", "PROBLEMS PEOPLE PAY TO SOLVE",
    "Calendar on desk", "RECURRING SERVICE PLANS",
    "Person reading documents", "LICENSING AND TRAINING")

biz(6, "Portable toilet rental", "every event and job site needs one",
    """Number six. Portable toilet rental. Construction sites, outdoor weddings, festivals, sports events and disaster recovery sites all
need restrooms. A portable toilet company rents units, delivers them, and services them regularly.""",
    """Why it works. Each unit can be rented many times over its life. Construction sites often rent for months, with weekly service,
which creates recurring revenue. Events add higher priced bursts of demand, especially in summer. And once you own the units, trucks and
routes, your costs per service can fall as you grow.""",
    """The catch. You need service trucks, disposal arrangements, and enough units to meet demand at peak times. It's smelly work, and
events can be seasonal. Larger competitors may operate in your area. But the combination of construction contracts and events can make
this a surprisingly steady business.""",
    "Outdoor festival crowd", "EVENTS AND JOB SITES",
    "Construction site", "MONTHS LONG RENTALS",
    "Truck on rural road", "SERVICE ROUTES")

biz(7, "Junk removal", "people pay you to take their stuff away",
    """Number seven. Junk removal. People move, downsize, renovate, or inherit a house full of belongings. Junk removal companies show up
with a truck and a crew, load everything, and haul it away. Customers pay to make the problem vanish.""",
    """Why it works. The startup costs can be lower than many businesses on this list: a truck or trailer, labor, insurance and marketing.
Some items can be donated, recycled or resold, which can add revenue or reduce disposal costs. Real estate agents and property managers
can become steady referral sources.""",
    """The catch. It's heavy physical work, disposal fees add up, and competition can be strong in some cities. Pricing by volume takes
experience, and you need to watch out for items that require special disposal. But it's a classic example of a simple business with
clear demand.""",
    "Moving boxes and furniture", "TAKE IT ALL AWAY",
    "Thrift store shelves", "DONATE, RECYCLE, RESELL",
    "Workers lifting boxes", "HEAVY WORK")

pr("""Quick pause. If you like learning how real businesses make money, subscribe to the channel. Every week Ryan breaks down a new part
of money, from your first ten thousand dollars to buying a business. Now, number eight.""")

biz(8, "Pressure washing and exterior cleaning", "dirt grows back, so customers come back",
    """Number eight. Pressure washing and exterior cleaning. Driveways, siding, decks, gas stations, parking lots, dumpster pads and
restaurant drive throughs all get dirty. Pressure washing companies clean them, often with equipment that costs far less than a truck
based business.""",
    """Why it works. Dirt comes back, so customers come back. Commercial clients may sign recurring contracts for regular cleaning. Before
and after photos sell the service better than any ad, which makes marketing easier on social media. And startup costs can be relatively
modest for residential work.""",
    """The catch. Competition can be stiff because it's easy to start. You need to learn proper techniques to avoid damaging surfaces, and
some areas have rules about wastewater. Winter can slow things down in cold climates. Commercial contracts are often where the steadier
money is.""",
    "Pressure washing driveway", "DIRT COMES BACK",
    "Smartphone camera photo", "BEFORE AND AFTER SELLS",
    "Snowy street", "SEASONS AND RULES")

short("Somebody has to clean the bins. That somebody can build a subscription business.")
biz(9, "Trash can cleaning", "a subscription for the grossest chore",
    """Number nine. Trash can cleaning. Garbage bins get disgusting, especially in summer. Some companies follow the garbage truck route
and clean the bins right after they've been emptied, using trucks or trailers with water tanks and washing equipment.""",
    """Why it works. It's naturally a subscription business, with customers paying monthly or quarterly. Once you have many customers in one
neighborhood, you can clean lots of bins on the same street in a short time, which improves profit per hour. Homeowner associations and
apartment complexes can add volume.""",
    """The catch. Equipment costs can be meaningful, demand can be seasonal in some regions, and you need to handle wastewater properly.
Customer density is everything, because driving between scattered customers kills profit. But it's a great example of turning a gross
chore into recurring revenue.""",
    "Garbage bins on street", "THE GROSSEST CHORE",
    "Suburban street houses", "DENSITY IS EVERYTHING",
    "Online banking smartphone app", "MONTHLY SUBSCRIPTIONS")

biz(10, "Commercial cleaning", "offices, gyms and clinics every single night",
    """Number ten. Commercial cleaning. Offices, gyms, medical clinics, schools and warehouses all need to be cleaned, often every night.
Commercial cleaning companies sign contracts to handle it, usually after hours.""",
    """Why it works. Contracts create recurring monthly revenue, and the work doesn't require a lot of expensive equipment. Many owners start
by cleaning themselves, then hire crews as they win more contracts. Specialized cleaning, like medical facilities or post construction
cleanup, can command higher prices.""",
    """The catch. Margins can be thin, labor turnover is high, and customers may switch companies to save money. Your success depends on
managing people, quality and scheduling well. But a cleaning company with reliable crews and strong relationships can grow steadily.""",
    "Office cleaning at night", "NIGHTLY CONTRACTS",
    "Cleaning supplies", "LOW EQUIPMENT COSTS",
    "Team of workers", "PEOPLE AND QUALITY")

biz(11, "Roadkill and dead animal removal", "a public service most people never think about",
    """Number eleven. Dead animal removal. Wildlife dies under porches, in attics, in crawl spaces, and on roads. Homeowners, property
managers and sometimes local governments pay someone to remove it safely, and sometimes to fix the entry point so it doesn't happen again.""",
    """Why it works. Almost nobody wants to do it, so the people who do can charge fair prices. It often pairs with wildlife control,
exclusion work and repairs, which raise the value of each job. Government contracts in some areas can add steady volume.""",
    """The catch. You'll need to follow local and state rules, use protective equipment, and dispose of remains properly. Some jobs are
emotionally unpleasant. But as an add on to wildlife control or pest control, it can be a profitable niche.""",
    "Raccoon in attic", "NOBODY WANTS TO DO IT",
    "Home repair tools", "PAIR IT WITH REPAIRS",
    "Government building", "FOLLOW THE RULES")

biz(12, "Self storage", "renting empty space to people with too much stuff",
    """Number twelve. Self storage. Storage facilities rent small rooms to people who have more stuff than space, often during life
changes like moving, divorce, downsizing or a death in the family. It's not dirty work, but it's often seen as boring and unglamorous.""",
    """Why it works. Once built or bought, a storage facility can have relatively low staffing needs compared with many businesses. Many
tenants stay longer than they planned, and moving out is a hassle, which can make occupancy fairly stable. Small rent increases over time
can add up across hundreds of units.""",
    """The catch. Buying or building a facility takes a lot of capital, and some markets have too many facilities, which leads to price
competition. It's closer to real estate than a typical small business. But for investors with capital, it's a classic boring wealth
builder.""",
    "Storage units", "RENTING EMPTY SPACE",
    "Moving boxes and furniture", "TENANTS STAY",
    "Real estate building", "CLOSER TO REAL ESTATE")

biz(13, "Mobile home park ownership", "one of the most unloved investments in America",
    """Number thirteen. Mobile home parks. In many parks, residents own their homes but rent the land underneath. The park owner maintains
roads, utilities and common areas, and collects lot rent.""",
    """Why it works. Moving a manufactured home is expensive, so residents tend to stay a long time. New parks are hard to build in many
places because of zoning, which limits new competition. That's why some investors have found these properties attractive despite their
image.""",
    """The catch. Parks can come with aging water and sewer systems, deferred maintenance and complex local rules. Raising rents too
aggressively hurts residents who often have limited means, can damage your reputation and invite regulation. The best owners treat
residents fairly and invest in the property. It's real estate with real responsibility.""",
    "Mobile home park", "OWN THE LAND",
    "Neighborhood street", "RESIDENTS STAY",
    "Water pipes infrastructure", "OLD PIPES, REAL RESPONSIBILITY")

biz(14, "Sewer and drain cleaning", "when the drain backs up, price matters less",
    """Number fourteen. Sewer and drain cleaning. Clogged drains and sewer backups are emergencies. When wastewater is coming up through
the floor, people want someone there fast. Drain companies use snakes, jetters and cameras to clear and inspect lines.""",
    """Why it works. Emergencies tend to make customers less sensitive to price. Camera inspections can lead to larger repair jobs, and
commercial clients like restaurants and apartment buildings may need regular maintenance. Equipment costs can be manageable compared
with many trades.""",
    """The catch. Licensing rules vary by state and city, and sewer work is dirty and sometimes dangerous. Customers can feel pressured in
emergencies, so honesty matters for your reputation. A company known for fair prices and fast response can earn loyal customers for
life.""",
    "Plumber working on pipes", "EMERGENCIES",
    "Plumber with camera inspection", "INSPECTIONS LEAD TO REPAIRS",
    "Handshake with customer", "HONESTY BUILDS LOYALTY")

biz(15, "Scrap metal and recycling", "turning trash into a commodity",
    """Number fifteen. Scrap metal and recycling. Old appliances, copper wire, car parts, aluminum, steel. Scrap businesses collect, sort and
sell metal to processors. Some people start small by picking up scrap from homes and businesses, others run full scrap yards.""",
    """Why it works. Metal has real value, and many people and businesses would rather give it away than haul it themselves. Collecting it
for free or a low price, sorting it carefully and selling it in bulk can create a margin. Contracts with contractors and manufacturers can
supply steady volume.""",
    """The catch. Scrap prices go up and down with commodity markets, sometimes sharply. Yards need permits, environmental compliance and
space. Theft prevention and record keeping rules apply in many states. It's a business where knowing your metals and your buyers makes all
the difference.""",
    "Scrap metal yard", "TRASH INTO COMMODITY",
    "Copper wire pile", "SORTING CREATES MARGIN",
    "Stock market chart on screen", "PRICES SWING")

# ---------------- Angle 1 ----------------
ch("Angle 1: The numbers")
pr("""Now let's step back and look at these fifteen businesses through three angles. First, the numbers. What actually makes ugly
businesses profitable?""")
card("""What the money machines have in common. Required demand, recurring revenue, weak competition, and assets used again and again.""",
     {"type": "list", "n": 4, "title": "the money pattern", "sub": "required, recurring, rare, reusable"}, "THE PATTERN")
sc("""Pattern one. Required demand. Septic pumping, grease traps and drain cleaning aren't optional. When a service is required by law,
by health, or by basic function, customers buy it in good times and bad. That makes revenue more resilient during recessions than
businesses that sell nice to haves.""",
   "Plumber working on pipes", "REQUIRED DEMAND")
sc("""Pattern two. Recurring revenue. Pest control plans, grease trap schedules, portable toilet service, trash can subscriptions and
commercial cleaning contracts all repeat. Recurring revenue means you don't start every month at zero. It also tends to make a business
more valuable when you sell, because buyers pay more for predictable income.""",
   "Calendar on desk", "RECURRING REVENUE")
sc("""Pattern three. Weak competition. When fewer people are willing to do the work, the ones who do can often charge fair prices and keep
customers longer. That doesn't mean there's no competition, but the competition is usually smaller and less aggressive than in popular
industries.""",
   "Empty city street", "WEAK COMPETITION")
sc("""Pattern four. Reusable assets. A dumpster, a portable toilet, a storage unit, a pump truck. Each one gets used again and again for
years. Every additional rental or job on the same asset spreads the purchase cost wider, which is how margins improve as you grow.""",
   "Construction site", "REUSABLE ASSETS")
card("""An illustration. A dumpster bought for six thousand dollars, rented twice a month at a contribution of two hundred dollars after
disposal and fuel, earns about four thousand eight hundred dollars a year before overhead.""",
     {"type": "stat", "label": "one dumpster, illustrated", "big": "$4,800/yr",
      "sub": "two rentals a month at $200 each, before overhead"}, "ONE BOX, MANY RENTALS")
sc("""Here's a simple illustration. Say a dumpster costs six thousand dollars. Say it's rented about twice a month, and after disposal fees,
fuel and driver time, each rental leaves two hundred dollars. That's about four thousand eight hundred dollars a year from one box, before
overhead like insurance, office costs and the truck payment. The box could pay for itself in a little over a year and keep working for
many years after.""",
   "Calculator and coins", "THE MATH ON ONE BOX")
sc("""But notice the assumption: twice a month. If that dumpster sits idle half the time, the math falls apart. That's the big lesson of
asset based businesses. Owning the equipment isn't the hard part. Keeping it busy is. Utilization, meaning the share of time your assets
are earning, is the number that decides whether these businesses make money.""",
   "Empty parking lot", "UTILIZATION DECIDES")
sc("""Labor businesses, like junk removal, commercial cleaning and pressure washing, have a different math. They need less equipment, but
profit depends on pricing, crew efficiency and route density. A crew that finishes four jobs a day close together earns far more than a
crew that drives across town for two.""",
   "Workers lifting boxes", "LABOR MATH")

# ---------------- Three owners ----------------
ch("Three owners, three paths")
pr("""Let's make this real with three made up but realistic owners, each starting a different ugly business.""")
sc("""Owner one starts a junk removal company with a used box truck and a friend as his first employee. The first year is hard. He learns
that he underpriced big jobs, that dump fees eat more than expected, and that reviews are everything. In year two, he raises prices,
builds relationships with three real estate offices and two property managers, and starts getting steady referrals. By year three, he
runs two crews and spends most of his time on sales and scheduling.""",
   "Moving boxes and furniture", "THE JUNK HAULER")
sc("""Owner two buys an existing pest control company from a retiring owner, using an SBA loan and some seller financing. She inherits
several hundred customers on service plans. Her first year is about not losing anyone: she calls every customer, keeps the old
technicians, and improves scheduling. Her second year is about growth: she adds commercial contracts and a termite inspection service for
home sales.""",
   "Business meeting handshake", "THE BUYER")
sc("""Owner three starts a pressure washing business on weekends while keeping his job. He buys modest equipment, posts before and after
photos, and books driveways and decks. After a season, he notices that restaurants and gas stations pay for regular cleaning. He
pitches a dozen local businesses, lands four monthly contracts, and that recurring revenue gives him the confidence to go full time the
next spring.""",
   "Pressure washing driveway", "THE SIDE HUSTLER")
sc("""Three different paths, but the same lessons. Price for profit, not just to win jobs. Chase recurring revenue. Build relationships
with people who send you customers. And keep risk small until the business proves itself. None of them got rich overnight, but each one
built something that pays far more than the work looks like it should.""",
   "Three people silhouettes", "SAME LESSONS")

# ---------------- Mistakes ----------------
ch("Eight mistakes that sink ugly businesses")
pr("""Ugly businesses can make good money, but plenty of them fail. Here are eight mistakes that sink them.""")
sc("""Mistake one. Underpricing. New owners often charge too little to win jobs, then discover they can't cover fuel, disposal fees,
insurance and repairs. Know your full cost per job before you set prices. Mistake two. Skipping the paperwork. Operating without the right
licenses, permits or insurance can bring fines, lawsuits, or a shutdown that wipes out everything you built.""",
   "Calculator and pen on financial papers", "MISTAKES 1 AND 2")
sc("""Mistake three. Buying too much equipment too soon. A shiny new truck with a big loan payment can sink a business that hasn't found
enough customers yet. Mistake four. Ignoring utilization. Idle dumpsters, empty storage units and parked trucks still cost money every
month. Track how busy your assets are, and don't buy more until the ones you have are working.""",
   "Truck on rural road", "MISTAKES 3 AND 4")
sc("""Mistake five. Poor communication. In service businesses, showing up on time and answering the phone wins more customers than any
advertisement. Missed calls are missed money. Mistake six. Neglecting reviews. In local businesses, online reviews often decide who gets
the call. Ask happy customers for reviews and respond politely to the unhappy ones.""",
   "Phone ringing on desk", "MISTAKES 5 AND 6")
sc("""Mistake seven. Doing everything yourself forever. Owners who never hire or train anyone hit a ceiling and burn out. Build simple
systems early, so someone else can do the work the way you would. And mistake eight. Mixing personal and business money. Separate bank
accounts, clean records and money set aside for taxes keep a good business from turning into a financial mess.""",
   "Team of workers", "MISTAKES 7 AND 8")

# ---------------- Startup cost tiers ----------------
ch("What it really costs to start")
pr("""Let's sort these fifteen businesses by how much money it roughly takes to get started. These are broad tiers, not quotes, and real
costs depend on your area and whether you buy new or used.""")
sc("""Tier one, lower startup costs. Junk removal with a trailer, pressure washing, commercial cleaning, and trash can cleaning with modest
equipment. Many people start these for thousands to tens of thousands of dollars, often while keeping a job. The tradeoff is more
competition, because the door is open to everyone.""",
   "Cleaning supplies", "TIER 1: LOWER COST")
sc("""Tier two, moderate startup costs. Pest control, dead animal removal, drain cleaning, and biohazard cleanup. These need training,
licenses, insurance and specialized equipment, but not necessarily heavy trucks. The licensing and training requirements also keep some
competitors out.""",
   "Exterminator spraying", "TIER 2: MODERATE COST")
sc("""Tier three, higher startup costs. Septic pumping, grease trap cleaning, dumpster rental and portable toilets need trucks, containers
or units, plus disposal arrangements. And tier four, the most capital: self storage, mobile home parks and scrap yards, which are closer to
real estate investing. Higher capital requirements usually mean fewer competitors, but more risk if things go wrong.""",
   "Storage units", "TIERS 3 AND 4: HEAVY CAPITAL")

# ---------------- Angle 2 ----------------
short("The reason you don't want this business is the same reason it's profitable.")
ch("Angle 2: The psychology")
pr("""Second angle. The psychology. Why do so many people avoid these businesses, and why is that an advantage for those who don't?""")
sc("""The first reason is status. Many people care what others think of their job. Saying you own a tech startup sounds impressive. Saying
you own a septic company gets a laugh at a party. But the bank doesn't care how your business sounds. It cares about cash flow. Willing to
give up status can mean gaining money.""",
   "People at party talking", "STATUS COSTS MONEY")
sc("""The second reason is disgust. Our brains are wired to avoid dirt, waste and decay. That instinct kept our ancestors alive, but it also
creates a barrier to entry in modern business. Every person who says that's gross is one less competitor. The disgust barrier is a moat
that protects these businesses.""",
   "Garbage bins on street", "THE DISGUST MOAT")
sc("""The third reason is the passion trap. People are told to follow their passion, so they open businesses in crowded industries they
love, like restaurants or fashion, where competition is fierce. Many successful ugly business owners say the passion came later, from
building something that works, serving customers well and seeing the profits grow.""",
   "Person at crossroads", "PASSION CAN COME LATER")
sc("""The fourth reason is invisibility. Nobody posts their septic company on social media. You don't see these businesses in movies.
So young people rarely even consider them. Meanwhile, many owners of these companies are approaching retirement, which may create
opportunities to buy established businesses in the coming years.""",
   "Older business owner", "INVISIBLE OPPORTUNITIES")
pr("""Here's the takeaway. The feeling of not wanting to do a job is real, but it's also information. It tells you most other people feel
the same way, which is exactly why the job can pay well.""")

# ---------------- Angle 3 ----------------
short("Here's how to choose an ugly business and start it without betting everything.")
ch("Angle 3: The playbook")
pr("""Third angle. The playbook. How do you choose one of these businesses and get started without risking everything?""")
sc("""Step one. Be honest about what you can tolerate. Smell, blood, heavy lifting, night work, emergencies. Each business has its own
version of ugly. Pick the one you can do for years without burning out. Step two. Study your local market. Search for providers in your
area, read their reviews, and look for gaps, like slow response times, bad service or no one covering certain neighborhoods.""",
   "Person thinking with notebook", "STEPS 1 AND 2")
sc("""Step three. Learn the rules. Licenses, permits, insurance, disposal requirements and safety training vary by state and city. Call
your local licensing office and talk to an insurance agent before spending money on equipment. Step four. Work in the industry first if you
can. A few months on someone else's crew teaches you pricing, problems and customers faster than any course.""",
   "Person reading documents", "STEPS 3 AND 4")
sc("""Step five. Start small. Many of these businesses can start with one truck, one trailer, a few containers or a single crew. Test demand
before borrowing big. Step six. Chase recurring revenue. Service plans, contracts and subscriptions turn one time customers into
predictable income, which is what makes a business valuable.""",
   "Small truck", "STEPS 5 AND 6")
sc("""Step seven. Consider buying instead of starting. Many established businesses in these industries are owned by people nearing
retirement. Buying one can give you customers, equipment and cash flow from day one. The Small Business Administration has loan programs
that can be used to buy businesses, though they come with requirements and personal guarantees.""",
   "Business meeting handshake", "STEP 7: BUY ONE")
sc("""And step eight. Keep your foundation solid. Keep an emergency fund, don't put all your savings into one truck, and keep investing for
retirement even while you build. A business is a powerful wealth builder, but your safety net should never depend entirely on it.""",
   "Piggy bank coins", "STEP 8: PROTECT YOUR FOUNDATION")

ch("The five question ugly business test")
pr("""Before you commit to any of these, run it through a simple five question test. If the answer to most of them is yes, you may have
found a good opportunity.""")
sc("""Question one. Is the service required, not optional? Question two. Will customers need it again, ideally on a schedule? Question
three. Are there few good providers in my area, judging by search results and reviews? Question four. Can I start small and test it before
borrowing big? And question five. Can I picture myself doing or managing this work for at least five years?""",
   "Notebook with financial notes", "THE 5 QUESTION TEST")
sc("""Septic pumping scores high on required and recurring demand. Junk removal scores high on starting small. Self storage scores high on
low labor but fails the start small test for most people. There's no perfect business, only the best fit for your money, your skills, your
location and your stomach. Score two or three options honestly, and the right one usually stands out.""",
   "Person thinking with notebook", "FIND YOUR FIT")
sc("""And remember, the goal isn't to own an ugly business forever. Many owners build the company, hire a manager, and eventually sell it.
A business with recurring revenue, clean books and a team that runs without the owner can sell for several times its yearly profit. That
sale can be the moment the dirty work turns into real wealth.""",
   "Business meeting handshake", "BUILD IT, THEN SELL IT")

# ---------------- Questions ----------------
ch("Questions people ask")
pr("""Let me answer a few common questions about ugly businesses.""")
sc("""Question one. Which one is the easiest to start? Businesses with low equipment costs, like junk removal, pressure washing and
commercial cleaning, are often easier to start. But easy to start also means easy for competitors to start, so service quality becomes
your edge. Question two. Which ones need the most money? Self storage, mobile home parks, scrap yards and truck based businesses like
septic pumping usually need the most capital.""",
   "Calculator and coins", "EASIEST? MOST EXPENSIVE?")
sc("""Question three. Can I run one without doing the dirty work myself? Eventually, many owners hire crews and focus on sales, scheduling
and management. But most successful owners did the work at the beginning, which taught them how to price jobs, train people and spot
problems. Question four. Are these businesses recession proof? Nothing is fully recession proof, but required services tend to hold up
better than optional ones.""",
   "Team of workers", "HANDS OFF? RECESSION PROOF?")
sc("""Question five. How do I find customers? Local search listings, online reviews, relationships with real estate agents, property
managers, contractors and restaurant owners, and simply being the company that answers the phone and shows up on time. In many of these
industries, being reliable is a competitive advantage by itself.""",
   "Phone ringing on desk", "FINDING CUSTOMERS")
sc("""Question six. Do I need a college degree? For most of these businesses, no. What you need is training, licensing where required,
business skills like pricing and bookkeeping, and a willingness to learn. Many owners take short courses, certifications, or learn on the
job. Question seven. What about taxes? Business owners pay income tax plus self employment tax on profits, and often need to make quarterly
estimated payments. A good accountant usually pays for themselves.""",
   "Person reading book", "DEGREE? TAXES?")
sc("""Question eight. What if I start and hate it? That's why starting small matters. If you test the business on weekends or work for
someone else first, the cost of changing your mind is small. Used equipment can often be sold. The bigger danger is borrowing heavily
before you know whether you can stand the work for years.""",
   "Person standing at crossroads", "WHAT IF I HATE IT?")
sc("""Question nine. Is it better to pick one business or combine a few? Many owners combine related services, like pest control with
dead animal removal, or junk removal with light demolition and cleanouts. Combining services lets you sell more to the same customer
using the same truck and crew. But start with one service and master it before you add another.""",
   "Home repair tools", "ONE OR SEVERAL?")
sc("""Question ten. How do I know if a business is worth buying? Look at at least three years of tax returns, the percentage of recurring
revenue, the age of the equipment, how dependent the business is on the owner, and the customer reviews. Then have an accountant and a
lawyer review the deal before you sign anything.""",
   "Tax forms on desk", "WORTH BUYING?")

# ---------------- Recap ----------------
ch("Recap")
sc("""Let's recap the fifteen. Septic pumping. Dumpster rental. Grease trap cleaning. Biohazard cleanup. Pest control. Portable toilets. Junk
removal. Pressure washing. Trash can cleaning. Commercial cleaning. Dead animal removal. Self storage. Mobile home parks. Drain cleaning.
And scrap metal.""",
   "Notebook with financial notes", "THE 15")
sc("""And the pattern behind them. Required demand. Recurring revenue. Weak competition. Reusable assets that stay busy. Plus one
psychological edge: the work most people avoid is often the work that pays.""",
   "Calculator and pen on financial papers", "THE PATTERN")
sc("""One last thought. Every town in America has people quietly earning a great living from work that nobody notices. The septic truck
on your street, the crew cleaning offices at midnight, the person who hauled away your old couch. Behind many of those trucks is an owner
who decided that the money mattered more than the image. That choice is available to anyone willing to make it, and the competition for it
is smaller than you think.""",
   "Truck on rural road", "THE QUIET MONEY")

ch("What to do next")
pr("""If one of these businesses made you curious instead of disgusted, that's a sign worth paying attention to. Pick one, study your local
market this week, and talk to someone who already does it. I'm Ryan Rover. Stay boring, stay profitable, and I'll see you in the next
video.""")

save("video14", '15 "Ugly" Businesses Nobody Wants (That Print Cash)', [
    "Bureau of Labor Statistics, Occupational Outlook Handbook (trades and service occupations)",
    "U.S. Small Business Administration, 7(a) loan program (business acquisition loans)",
    "U.S. EPA, septic systems overview (homes relying on septic systems; pumping intervals)",
    "Dumpster contribution example: simplified illustration ($6,000 container, about $200 per rental after direct costs, two rentals a month)",
], "ugly businesses")
