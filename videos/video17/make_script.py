import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short


def hustle(n, name, sub, a, b, c, q1, c1, q2, c2, q3, c3):
    ch(f"{n}. {name}")
    card(f"Number {n}. {name}. {sub}", {"type": "list", "n": n, "title": name, "sub": sub}, f"SIDE HUSTLE {n}")
    sc("The hustle. " + a, q1, c1)
    sc("The business. " + b, q2, c2)
    sc("The watch out. " + c, q3, c3)
    if n in GROW:
        t, q, cap = GROW[n]
        sc("Growing it. " + t, q, cap)


GROW = {
    1: ("""A weekend pressure washer notices that a local burger chain's drive throughs look grimy. He offers a free first cleaning at one
location, then signs a monthly contract for all four. With that steady base, he buys a second rig, hires a part time operator, and starts
pitching gas stations and apartment complexes.""", "Restaurant exterior", "ONE CONTRACT CHANGES EVERYTHING"),
    2: ("""A lawn mower with thirty weekly clients raises prices slightly, drops the customers farthest away, and adds twenty more on the same
streets. Route density lets one crew do more lawns per day. He hires a crew leader, adds a second trailer, and books fall cleanups and snow
removal to keep the crew busy all year.""", "Landscaping crew", "DENSITY, THEN CREWS"),
    3: ("""A house cleaner fully booked with twelve weekly homes hires her first employee and trains her with a written checklist for every
room. After six months, she has two teams, a waiting list and enough income to stop cleaning herself, focusing on quality checks and new
clients.""", "Cleaning supplies", "CHECKLISTS AND TEAMS"),
    4: ("""A bookkeeper with eight monthly clients partners with a local tax preparer who refers small businesses after tax season. Within
two years, she has thirty clients and two part time bookkeepers, and the firm's recurring monthly revenue makes it a valuable asset.""", "Accountant meeting client", "PARTNER FOR REFERRALS"),
    5: ("""A mobile detailer signs a contract with a used car dealership to prepare every car before it goes on the lot. The steady weekday
volume justifies a second van and an employee, while weekends stay reserved for high priced ceramic coating jobs.""", "Car dealership lot", "DEALERSHIP VOLUME"),
    6: ("""A vending operator starts with three machines, tracks sales weekly and moves the weakest one to a busier location. Every few months,
profits buy another machine. After a few years, a route of dozens of machines produces steady income and could be sold to another operator.""", "Vending machine", "TRACK, MOVE, ADD"),
    7: ("""A handyman who gets regular calls from one property manager offers a monthly maintenance package for all of their units. That steady
work lets him hire a second handyman and turn scattered weekend jobs into a weekday business.""", "Home repair tools", "PACKAGES FOR MANAGERS"),
    8: ("""Picture a hauler who starts with a pickup on Saturdays. After a year of steady referrals from two real estate offices, he buys a
used box truck and hires a weekend helper. By year three, he runs the truck five days a week with a crew, while he handles quotes, marketing
and the agent relationships that keep the calendar full.""", "Moving truck", "FROM PICKUP TO CREW"),
    9: ("""A dog walker with fifteen weekly clients is near her limit. She hires two part time walkers, pays them a fair share of each walk,
and uses scheduling software to keep everything organized. Now she manages forty clients and spends her time on customer relationships and
adding boarding during holidays, when prices are highest.""", "Dog walker with dogs", "FROM WALKER TO MANAGER"),
    10: ("""A math tutor with a waiting list starts small group sessions for test prep, charging each student less than private lessons but
earning more per hour overall. Then she recruits two other tutors for reading and science. Her role shifts toward matching students with
tutors and talking to parents.""", "Small classroom", "FROM TUTOR TO CENTER"),
    11: ("""A reseller who keeps finding great deals on vintage denim decides to specialize. He builds his own online store, buys inventory
in bulk from wholesalers, and hires a part time helper to photograph and ship. Specializing raises his margins and builds a loyal customer
base that follows his new arrivals.""", "Packages ready to ship", "SPECIALIZE TO GROW"),
    12: ("""A social media manager with five restaurant clients creates a simple monthly package with photos, posts and a short report. She
hires a freelance photographer and a part time writer, then signs ten more restaurants using results from the first five as proof.""", "Team meeting with laptops", "PACKAGES AND PROOF"),
    13: ("""A weekend real estate photographer signs a deal to shoot every new listing for a local brokerage. The steady volume lets him hire a
second photographer, add video walkthroughs and floor plans, and turn sporadic gigs into predictable weekly revenue.""", "Real estate building", "ONE BIG CONTRACT"),
    14: ("""A baker who sells out every Saturday at the farmers market rents time in a shared commercial kitchen, gets licensed, and starts
supplying three local coffee shops. Wholesale orders create steady weekly revenue, and the market stall becomes the place to test new
products.""", "Commercial kitchen", "MARKET TO WHOLESALE"),
    15: ("""An event rental owner who started with twenty chairs and four tables reinvests every dollar of profit into inventory for two years.
Partnerships with three wedding venues and a party planner keep the calendar full every weekend, and a part time crew handles setup and
teardown.""", "Wedding reception", "REINVEST AND PARTNER"),
    16: ("""A mobile mechanic who services cars in office parking lots signs maintenance deals with two local companies that run small fleets
of vans. The fleet work fills weekdays, so he hires a second technician and buys another service van.""", "Service van", "FLEET WORK"),
    17: ("""Two friends offering labor only moving help on weekends save for a year, buy a used truck, register and insure properly, and start
offering full local moves. Five star reviews become their main source of customers.""", "Moving truck", "REVIEWS DRIVE GROWTH"),
    18: ("""A co host who manages two vacation rentals for neighbors builds a reliable cleaning team and a simple guest messaging system.
Owners talk, and within two years she manages fifteen properties, earning a percentage of booking revenue from each.""", "Vacation rental home", "WORD OF MOUTH"),
    19: ("""A window cleaner signs up a whole street of storefronts for monthly service, then adds holiday lighting installation in November
and December, when window work slows down. The two services together keep his crew busy year round.""", "Storefronts on street", "STACK THE SEASONS"),
    20: ("""A woman who teaches spreadsheet skills on social media sells templates, then a full course, then corporate training sessions. She
hires an editor and a support assistant, and her audience becomes a business that earns while she sleeps.""", "Person recording video", "AUDIENCE TO BUSINESS"),
}

# ---------------- Intro ----------------
ch("Intro")
short("Most side hustles stay side hustles forever. These 20 can actually become real businesses.")
pr("""Hi, I'm Ryan Rover. Almost everyone has heard the advice: start a side hustle. Drive for an app, sell stuff online, freelance on
weekends. And extra income is great. But most side hustles have a ceiling. You trade hours for dollars, and when you stop working, the
money stops. Today, we're looking at twenty side hustles that can do something more: grow into real businesses with employees, systems
and value you could one day sell.""")
card("""Twenty side hustles that can grow into real businesses. Start small, then build something bigger than your own hours.""",
     {"type": "stat", "label": "side hustle to business", "big": "20", "sub": "hustles with a path to a real company"})
sc("""Here's the difference between a side hustle and a business. A side hustle depends entirely on you. If you get sick or take a vacation,
the income stops. A business has customers, systems and people that keep working even when you're not there. The goal of today's video is
to show you which hustles have a clear path from the first category to the second, and what that path looks like step by step.""",
   "Person working on laptop at night", "HUSTLE VS BUSINESS")
sc("""For each one, we'll look at three things. The hustle, meaning how you can start it on nights and weekends with modest money. The
business, meaning what it can grow into once demand is proven. And the watch out, meaning the trap that keeps most people stuck. Any income
numbers are illustrations, not promises. Results depend on your skills, your market and your effort.""",
   "Notebook with financial notes", "HUSTLE, BUSINESS, WATCH OUT")
sc("""After the twenty, we'll look at the whole thing from three angles. The numbers, meaning when a hustle is big enough to become a
business. The psychology, meaning why most people never make the jump. And the playbook, meaning the exact steps to grow from your first
customer to your first employee.""",
   "Person thinking with notebook", "20 HUSTLES, 3 ANGLES")
sc("""One more thing before we start. A side hustle that becomes a business usually takes years, not months. The examples you'll hear today
are made up but realistic, and they compress a lot of hard work into a few sentences. Expect slow months, mistakes and moments when you want
to quit. Those are normal. The people who build real businesses are usually the ones who keep going after the excitement wears off.""",
   "Hourglass", "IT TAKES YEARS")
pr("""Let's start with one of the simplest hustles there is.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Data on self employment and small business comes from the Bureau of Labor Statistics and the U.S. Small Business Administration's
Office of Advocacy, which reports that the large majority of small businesses have no employees. Tax information comes from the IRS. Example
earnings are simplified illustrations. This video is education, not financial, legal or tax advice.""",
   "Government building", "SOURCES")

# ---------------- The 20 ----------------
hustle(1, "Pressure washing", "from weekend driveways to commercial contracts",
    """Buy a quality pressure washer and surface cleaner, and start with driveways, decks and fences in your neighborhood on weekends.
Before and after photos on social media and neighborhood groups do much of the marketing for you. Many people book their first jobs
within weeks.""",
    """The growth path is commercial work: restaurants, gas stations, apartment complexes, parking garages and storefronts that need regular
cleaning. Monthly contracts turn one time jobs into recurring revenue. Then you hire a crew, add a second rig, and move from washing to
selling and managing.""",
    """Easy to start means easy for others to start too. Residential prices get competitive. The ones who build businesses chase recurring
commercial contracts, get properly insured, and learn soft washing techniques that prevent damage to roofs and siding.""",
    "Pressure washing driveway", "WEEKEND DRIVEWAYS",
    "Restaurant exterior", "COMMERCIAL CONTRACTS",
    "Insurance documents", "INSURANCE AND TECHNIQUE")

hustle(2, "Lawn care", "from one mower to a landscaping company",
    """Mow lawns for neighbors after work and on weekends. A good mower, trimmer and blower, plus a trailer or truck, can be enough to start.
Reliability is rare in this industry, so simply showing up on time every week wins customers.""",
    """Once your weekly route is full, the next step is a second crew. Then add higher value services like mulching, planting, irrigation,
seasonal cleanups and snow removal in winter. Commercial properties and homeowner associations can provide large, steady contracts.""",
    """Pricing too low to win customers is the classic trap. So is a route spread across town, which kills profit with driving time. Pack
your customers close together, price for profit, and learn to say no to jobs that don't fit.""",
    "Landscaper mowing lawn", "ONE MOWER",
    "Landscaping crew", "CREWS AND SERVICES",
    "Map with pins", "ROUTE DENSITY")

hustle(3, "House cleaning", "from your own two hands to cleaning teams",
    """Clean homes on weekends or evenings for a few regular clients. Startup costs are mostly supplies and transportation. Many people find
their first clients through friends, neighbors and local social media groups.""",
    """Hire and train cleaners, create checklists so every home gets the same quality, and focus on recurring weekly or biweekly clients.
Add move out cleaning, vacation rental turnovers and small offices. Your job becomes hiring, scheduling and quality control.""",
    """The challenge is people. Finding reliable cleaners and keeping quality consistent is hard. Clear systems, fair pay and insurance or
bonding make the difference between a hustle that burns you out and a business that grows.""",
    "Cleaning supplies", "WEEKEND CLEANING",
    "Team of workers", "CLEANING TEAMS",
    "Notebook with financial notes", "SYSTEMS AND PEOPLE")

hustle(4, "Bookkeeping", "from one client to a small firm",
    """If you're organized and comfortable with numbers, small business owners need help keeping their books up to date. Many bookkeepers
start with one or two clients in the evenings, using common accounting software. Certifications can help build trust.""",
    """Monthly bookkeeping is naturally recurring revenue. As you add clients, you can hire other bookkeepers, add payroll services, and
partner with tax preparers. A small firm with dozens of monthly clients can become a valuable, sellable business.""",
    """Bookkeeping is a responsibility, and mistakes can cost clients money. Know your limits, avoid giving tax advice you're not qualified
to give, and consider professional liability insurance as you grow.""",
    "Accountant meeting client", "EVENING CLIENTS",
    "Calendar on desk", "MONTHLY RECURRING",
    "Person reading documents", "KNOW YOUR LIMITS")

hustle(5, "Mobile car detailing", "from your driveway to a fleet of vans",
    """Detail cars at customers' homes or workplaces on weekends. A pressure washer, vacuum, polisher and quality products are enough to
start. Customers love the convenience of not driving anywhere.""",
    """Add maintenance plans for regular washes, ceramic coatings, and fleet contracts with dealerships, rental companies or businesses with
company vehicles. Then add vans and trained detailers. Some owners eventually open a fixed location.""",
    """Weather and water restrictions can disrupt mobile work, and pricing is competitive for basic washes. The money is in premium services
and recurring fleet contracts, not one time cheap washes.""",
    "Car detailing", "DETAILING AT YOUR DOOR",
    "Car dealership lot", "FLEET CONTRACTS",
    "Rain on window", "WEATHER AND PRICING")

short("Here's a side hustle that can turn into a business you could sell for real money.")
hustle(6, "Vending machines", "from one machine to a route",
    """Buy a used snack or drink machine and place it in a business with steady foot traffic, like an auto shop, a gym or a small office.
You stock it weekly and share a small commission with the location owner, if needed.""",
    """Add machines one by one until you have a route. A route of many well placed machines can produce steady income and can be sold to
another operator. Some owners add healthy vending, micro markets in offices, or specialty machines.""",
    """Location is everything. A machine in a bad spot barely covers its costs. And machines break, get vandalized and need restocking,
which takes time. Track sales per machine and move the weak ones.""",
    "Vending machine", "ONE MACHINE",
    "Office break room", "A ROUTE OF MACHINES",
    "Person thinking with notebook", "LOCATION IS EVERYTHING")

hustle(7, "Handyman services", "from fixing things to a home services company",
    """If you're handy, neighbors always need small repairs: mounting TVs, fixing doors, assembling furniture, patching drywall. Many people
start with tools they already own and book jobs through word of mouth and local apps.""",
    """Hire other handymen, focus on property managers and real estate agents who need repairs constantly, and expand into small remodeling
projects. Some states require contractor licenses above certain job sizes, so check your rules as you grow.""",
    """Handyman work can become scattered small jobs with lots of driving. Grouping jobs by area, setting minimum charges and building
relationships with property managers turns chaos into a business.""",
    "Home repair tools", "SMALL REPAIRS",
    "Real estate agent with house", "PROPERTY MANAGERS",
    "Map with pins", "MINIMUMS AND ROUTES")

pr("""Quick pause. If you're enjoying this, subscribe to the channel. Every week, Ryan breaks down a new part of money, from side hustles to
buying businesses, with real numbers and no hype. Now, number eight.""")

hustle(8, "Junk removal", "from a pickup truck to a hauling company",
    """With a pickup truck or a trailer, you can haul away old furniture, appliances and yard waste on weekends. People happily pay to make
their junk disappear. Donating or reselling some items can add income.""",
    """Upgrade to a box truck or dump trailer, hire a helper, and build relationships with real estate agents, estate sale companies and
property managers. Add cleanouts, light demolition and dumpster rentals.""",
    """Dump fees and fuel add up quickly, so price by volume and know your costs. Heavy lifting can wear you down, which is why hiring help
early matters.""",
    "Pickup truck loaded", "A PICKUP TRUCK",
    "Moving boxes and furniture", "CLEANOUTS AND REFERRALS",
    "Calculator and coins", "KNOW YOUR COSTS")

hustle(9, "Pet care", "from dog walking to a pet services company",
    """Walk dogs, pet sit or offer drop in visits for neighbors. Apps can help you find clients, but building your own client list gives you
more control and better pay.""",
    """Hire other walkers and sitters, add grooming, training or boarding, and focus on recurring weekly clients. Some owners eventually open a
dog daycare facility.""",
    """Insurance and bonding are important, because you're responsible for people's pets and homes. Reliability and trust are the whole
business.""",
    "Dog walker with dogs", "DOG WALKING",
    "Dog grooming", "GROOMING AND DAYCARE",
    "Insurance documents", "TRUST AND INSURANCE")

hustle(10, "Tutoring", "from one student to a tutoring center",
    """Tutor students in subjects you know well, test prep, music or languages, in person or online. Parents are often willing to pay for
help that improves grades or scores.""",
    """Hire other tutors, create programs and packages, and consider a small learning center or online platform. Group classes increase how
much you earn per hour.""",
    """Tutoring is seasonal around school calendars and exams. Packages and recurring sessions smooth out income. Results and parent
referrals drive growth.""",
    "Tutor with student", "ONE STUDENT",
    "Small classroom", "A TUTORING CENTER",
    "Calendar on desk", "SEASONAL DEMAND")

hustle(11, "Reselling", "from flipping finds to an online store",
    """Buy underpriced items at thrift stores, garage sales and clearance aisles, then resell them online for more. Many people start with
items they already own.""",
    """Specialize in a category you know, like sneakers, vintage clothing, electronics or tools. Build your own store, buy inventory in bulk,
and eventually hire help for photos, listing and shipping.""",
    """It's easy to spend hours for little profit. Track your time, focus on higher margin items, and watch out for inventory that never
sells.""",
    "Thrift store shelves", "FLIPPING FINDS",
    "Packages ready to ship", "AN ONLINE STORE",
    "Calculator and coins", "TRACK YOUR TIME")

short("This side hustle has almost no startup cost, and it can grow into an agency.")
hustle(12, "Social media management", "from one client to a marketing agency",
    """Manage social media accounts for local businesses that don't have time to post. Restaurants, gyms, salons and contractors often need
help. Start with one or two clients and build a portfolio.""",
    """Offer packages with content creation, ads management and reporting. Hire freelancers or employees and become a small agency serving
dozens of clients on monthly retainers.""",
    """Clients may leave if they don't see results. Track and report results clearly, and focus on industries where you understand the
customer.""",
    "Smartphone social media", "ONE CLIENT",
    "Team meeting with laptops", "AN AGENCY",
    "Stock market chart on screen", "SHOW RESULTS")

hustle(13, "Photography and video", "from weekend shoots to a production company",
    """Shoot portraits, events, real estate or products on weekends. Real estate photography in particular can bring steady work from agents
who list homes regularly.""",
    """Hire other photographers, add video, drone footage and virtual tours, and sign contracts with real estate brokerages or businesses that
need regular content.""",
    """Equipment can get expensive, and creative work can be hard to price. Focus on niches with steady demand rather than one time events
only.""",
    "Photographer with camera", "WEEKEND SHOOTS",
    "Real estate building", "REAL ESTATE CONTRACTS",
    "Calculator and coins", "PRICE THE NICHE")

hustle(14, "Food from a home kitchen", "from farmers markets to a food brand",
    """Many states have cottage food laws that let you sell certain homemade foods, like baked goods or jams, with limited licensing. Farmers
markets and local events are great places to test recipes and prices.""",
    """Move into a commercial kitchen, get the required licenses, and sell to local stores, cafes or online. Some food businesses grow into
regional brands.""",
    """Food has thin margins and strict rules. Know your state's laws and calculate costs carefully, including ingredients, packaging and your
time.""",
    "Farmers market stall", "FARMERS MARKETS",
    "Commercial kitchen", "A FOOD BRAND",
    "Person reading documents", "KNOW THE RULES")

hustle(15, "Event rentals", "from a few tables to a rental company",
    """Rent out tables, chairs, tents, bounce houses or photo booths for parties and events on weekends. Your equipment earns money every time
it's rented.""",
    """Add more inventory, delivery and setup services, and partnerships with event planners and venues. Weddings and corporate events can be
very profitable.""",
    """Storage space, transportation and wear and tear are real costs. Insurance is important, especially for inflatables.""",
    "Outdoor event tent", "A FEW TABLES",
    "Wedding reception", "WEDDINGS AND EVENTS",
    "Storage units", "STORAGE AND INSURANCE")

hustle(16, "Mobile mechanic", "from driveway repairs to a service company",
    """If you have mechanical skills, do basic repairs like brakes, batteries and oil changes at customers' homes. Convenience is the selling
point.""",
    """Hire technicians, add vans, and serve fleets and businesses with regular maintenance contracts. Some mobile mechanics eventually open a
shop.""",
    """You need proper tools, insurance and the ability to say no to jobs that require a full shop. Environmental rules on disposing of fluids
apply.""",
    "Mechanic working under car", "DRIVEWAY REPAIRS",
    "Service van", "FLEETS AND VANS",
    "Home repair tools", "KNOW YOUR LIMITS")

hustle(17, "Moving help", "from helping friends to a moving company",
    """Offer labor only moving help, loading and unloading trucks that customers rent. All you need at first is strength, a helper and some
basic equipment.""",
    """Buy a truck, get the needed registration and insurance, and offer full service local moves. Then add packing, storage and long distance
moves.""",
    """Damage claims and injuries are real risks. Insurance, careful training and clear pricing protect you and your customers.""",
    "Workers lifting boxes", "LABOR ONLY",
    "Moving truck", "A MOVING COMPANY",
    "Insurance documents", "INSURANCE MATTERS")

hustle(18, "Airbnb co-hosting", "from one listing to a management company",
    """Help property owners manage their short term rentals: listings, guest messages, cleaning schedules and check ins. Many co hosts earn a
percentage of booking revenue.""",
    """Manage more properties, hire cleaners and assistants, and form a property management company. Some managers handle dozens of units.""",
    """Local short term rental rules are changing in many cities, and some places have banned or restricted them. Know your local laws
before you build.""",
    "Vacation rental home", "ONE LISTING",
    "Keys on table", "MANAGING MANY UNITS",
    "Government building", "LOCAL RULES")

hustle(19, "Window and gutter cleaning", "from a ladder to recurring routes",
    """With ladders, poles and basic tools, you can clean windows and gutters for homes and small storefronts. Many homeowners want this done
once or twice a year.""",
    """Build recurring routes for storefronts that need windows cleaned weekly or monthly, add holiday light installation in winter, and hire
crews.""",
    """Ladder work is dangerous. Safety training, the right equipment and insurance are not optional.""",
    "Window cleaning", "A LADDER",
    "Storefronts on street", "STOREFRONT ROUTES",
    "Safety equipment", "SAFETY FIRST")

hustle(20, "Online courses and digital products", "from one product to a content business",
    """Teach a skill you know through a course, templates, guides or a paid newsletter. Startup costs are low, mainly your time and simple
tools.""",
    """Build an audience, add more products, offer coaching or memberships, and eventually hire help with editing, support and marketing.""",
    """Many digital products never sell, because there's no audience. Build an audience first, and validate demand before spending months
creating.""",
    "Person recording video", "ONE PRODUCT",
    "Laptop with business software", "A CONTENT BUSINESS",
    "Person thinking with notebook", "AUDIENCE FIRST")

# ---------------- Which one fits ----------------
ch("How to choose the right hustle for you")
pr("""With twenty options, how do you choose? Ask yourself four questions.""")
sc("""Question one. What do I already know how to do? Your existing skills cut months off the learning curve. A mechanic should look at
mobile repair, an accountant at bookkeeping, a teacher at tutoring. Question two. How much money can I risk? Some hustles start with a few
hundred dollars, others need a truck or inventory.""",
   "Person thinking with notebook", "SKILLS AND MONEY")
sc("""Question three. Do I prefer physical work or computer work? Lawn care and junk removal keep you moving. Bookkeeping and social media keep
you at a desk. Pick what you can sustain. Question four. Does it have recurring demand in my area? Search for providers nearby, read their
reviews, and look for gaps in service, availability or quality.""",
   "Landscaper mowing lawn", "WORK STYLE AND DEMAND")
sc("""There's no perfect choice, and you can always switch. Many successful owners tried two or three hustles before finding the one that
fit. The important thing is to start, learn from real customers, and keep moving toward recurring revenue and a team.""",
   "Person standing at crossroads", "JUST START")

# ---------------- The ladder ----------------
ch("The five rungs from hustle to business")
pr("""Every hustle on this list grows through the same five rungs. Knowing where you are tells you what to do next.""")
sc("""Rung one. You do everything. You find customers, do the work, send invoices and answer every call. That's normal at the start, and
it's where you learn how the business really works. Rung two. You raise prices and fill your schedule. Once demand exceeds your time, you're
ready for the next step.""",
   "Person working on laptop at night", "RUNGS 1 AND 2")
sc("""Rung three. You hire your first helper. This is the scariest jump, because your profit per job drops at first and you have to trust
someone else. Rung four. You build systems: checklists, scheduling software, pricing sheets and training, so others can do the work your
way.""",
   "Team of workers", "RUNGS 3 AND 4")
sc("""Rung five. You become the owner, not the worker. You focus on sales, hiring, finances and growth while the team does the work. At this
point, the business can run without you for a week or two, and it starts to have real value that someone else might pay for.""",
   "Business meeting", "RUNG 5: OWNER")

# ---------------- Mistakes ----------------
ch("Five mistakes that keep hustles small")
sc("""Mistake one. Charging too little for too long. Low prices fill your calendar but leave no money to hire or grow. Mistake two. Mixing
personal and business money. Open a separate bank account early, and set aside money for taxes, because self employment tax surprises many
new hustlers.""",
   "Tax forms on desk", "MISTAKES 1 AND 2")
sc("""Mistake three. Saying yes to everything. Chasing every kind of job spreads you thin. Focus on the work that pays best and recurs.
Mistake four. Never hiring. If you refuse to let anyone else do the work, your income will always be limited to your own hours.""",
   "Person stressed with bills", "MISTAKES 3 AND 4")
sc("""And mistake five. Quitting your job too early. Many successful owners keep their job until the side business reliably earns enough to
replace their income, with savings as a cushion. Patience protects you while the business proves itself.""",
   "Person at office desk", "MISTAKE 5")

# ---------------- Angle 1 ----------------
ch("Angle 1: The numbers")
pr("""Now, three angles. First, the numbers. When is a side hustle big enough to become a business?""")
card("""An illustration. Doing jobs yourself at one hundred dollars of profit per job, twenty jobs a month earns two thousand dollars. Two crews
earning forty dollars of profit per job, doing one hundred twenty jobs a month, earn four thousand eight hundred dollars, without your hours.""",
     {"type": "compare", "left": {"label": "You alone", "big": "$2,000", "sub": "20 jobs × $100 profit"},
      "right": {"label": "Two crews", "big": "$4,800", "sub": "120 jobs × $40 profit"}}, "HOURS VS SYSTEMS")
sc("""Here's the key math. When you do every job yourself, you keep most of the money from each job, but you can only do so many. When you
hire, your profit per job drops, because you pay the worker, but the number of jobs can multiply. In this illustration, you earn more with
crews, and your own time is freed for sales and growth.""",
   "Calculator and coins", "PROFIT PER JOB VS NUMBER OF JOBS")
sc("""A simple signal that it's time to grow: you're turning away work, your prices are already fair or high, and you've had steady demand
for at least six months. Before hiring, make sure your price leaves enough room to pay a worker, cover insurance and payroll taxes, and still
make a profit on every job. A common mistake is hiring as soon as you feel busy, before the numbers support it. Run the math
first: what you'll pay per job, what insurance and payroll taxes add, and how many jobs the new person needs to do each week to cover the
cost. If the math works with a cushion, hire. If not, raise prices first.""",
   "Calendar on desk", "SIGNS IT'S TIME")
sc("""Taxes matter too. Side hustle income is generally taxable, and self employment tax applies to net earnings above a small threshold. As
income grows, many owners form an LLC for liability protection and talk with an accountant about the best tax setup. Planning for taxes from
the start avoids a painful surprise in April.""",
   "Tax forms on desk", "PLAN FOR TAXES")
sc("""Finally, value. A hustle that depends on you is worth little to a buyer. A business with recurring customers, trained staff and
documented systems can sell for a multiple of its yearly profit. That's the real prize of making the jump: you're building an asset, not
just an income.""",
   "Business meeting handshake", "BUILDING AN ASSET")

# ---------------- Angle 2 ----------------
short("Why most people never turn their side hustle into a real business, and how to be different.")
ch("Angle 2: The psychology")
pr("""Second angle. The psychology. Why do so few side hustles become businesses?""")
sc("""The first reason is the comfort of control. Doing everything yourself feels safe. You know the work is done right. Hiring means letting
go, accepting mistakes and trusting others. But without letting go, growth is impossible.""",
   "Person thinking with notebook", "THE COMFORT OF CONTROL")
sc("""The second reason is fear of losing the paycheck. Many people stay stuck between a job and a hustle for years, too busy to grow and too
scared to leap. The answer isn't to quit recklessly, but to set clear milestones: when the business earns a specific amount for a specific
number of months, with savings in place, you make the move.""",
   "Person at office desk", "FEAR OF THE LEAP")
sc("""The third reason is identity. Many hustlers see themselves as a cleaner, a photographer or a mechanic, not as a business owner. That
identity keeps them working in the business instead of on it. Thinking of yourself as the owner, even when you're still doing the work, can
change the decisions you make.""",
   "Person looking in mirror", "OWNER IDENTITY")
pr("""The takeaway. The skills that start a hustle aren't the same skills that build a business. The jump requires letting go, planning the
leap and seeing yourself as the owner.""")

# ---------------- Angle 3 ----------------
short("Here's the step by step plan to go from side hustle to your first employee.")
ch("Angle 3: The playbook")
pr("""Third angle. The playbook. Here's how to go from first customer to first employee.""")
sc("""Step one. Pick a hustle with recurring demand and a clear growth path, like the ones on this list. Step two. Start small and keep your
job. Get your first ten paying customers and learn what they actually value.""",
   "Notebook with financial notes", "STEPS 1 AND 2")
sc("""Step three. Make it official. Separate bank account, basic bookkeeping, any required licenses, and insurance. Step four. Raise prices
until you're earning a healthy profit per job. Step five. Write down how you do the work, step by step, so you can teach it.""",
   "Person reading documents", "STEPS 3 TO 5")
sc("""Step six. Hire your first helper, maybe part time, and train them using your written steps. Step seven. Shift your time toward sales,
recurring contracts and customer relationships. Step eight. When the business reliably replaces your income and you have savings, decide
whether to go full time.""",
   "Team of workers", "STEPS 6 TO 8")
sc("""Throughout all of it, keep investing for retirement and keep an emergency fund. A growing business is exciting, but your personal
financial foundation should never depend on it alone.""",
   "Piggy bank coins", "PROTECT YOUR FOUNDATION")

# ---------------- Questions ----------------
ch("Questions people ask")
sc("""Question one. How much money do I need to start? Many of these hustles start with a few hundred to a few thousand dollars in
equipment. Start with the minimum, and upgrade with profits. Question two. Do I need an LLC? Not always at the very start, but as income and
risk grow, an LLC and insurance can protect your personal assets. Ask a local professional.""",
   "Calculator and coins", "HOW MUCH? LLC?")
sc("""Question three. How do I find my first customers? Friends, neighbors, local social media groups, online listings and simply asking
satisfied customers for referrals. Question four. Which hustle grows into the most valuable business? Those with recurring revenue, like
bookkeeping, cleaning contracts, lawn care routes and vending routes, tend to be the most valuable when you sell.""",
   "Smartphone social media", "FIRST CUSTOMERS? MOST VALUABLE?")
sc("""Question five. Should I use gig apps or find my own customers? Apps can be a great way to get started quickly, but they take a cut and
control the relationship. The goal is to move customers to your own business over time, where you set the prices and keep the relationship.
Question six. How many hours a week does it take? Many people start with ten to fifteen hours on evenings and weekends, then increase as
demand grows.""",
   "Smartphone booking app", "APPS? HOURS?")
sc("""Question seven. What if I fail? Most side hustles cost little to start, so the downside is usually small: some money and some time. And
even a failed hustle teaches sales, pricing and customer service, skills that make the next attempt far more likely to work.""",
   "Person standing at crossroads", "WHAT IF I FAIL?")

# ---------------- Recap ----------------
ch("Recap")
sc("""Let's recap the twenty. Pressure washing. Lawn care. House cleaning. Bookkeeping. Mobile detailing. Vending. Handyman services. Junk
removal. Pet care. Tutoring. Reselling. Social media management. Photography. Home kitchen food. Event rentals. Mobile mechanic. Moving help.
Airbnb co hosting. Window and gutter cleaning. And digital products.""",
   "Notebook with financial notes", "THE 20")
sc("""And the path. Do everything, fill your schedule, hire your first helper, build systems, then become the owner. Price for profit,
chase recurring revenue, keep your job until the business proves itself, and protect your foundation the whole way.""",
   "Calculator and pen on financial papers", "THE PATH")
sc("""Remember, every large service company you see today, the cleaning company with fifty employees, the landscaping firm with a fleet of
trucks, the agency with dozens of clients, started with one person and one customer. The difference between them and the millions of hustles
that stayed small wasn't luck. It was a decision, made at some point, to stop being the worker and start being the owner. That decision is
available to you too, whenever your hustle is ready for it.""",
   "Small business owner smiling", "ONE PERSON, ONE CUSTOMER")

ch("What to do next")
pr("""Pick one hustle from this list that matches your skills. This week, get your first paying customer, even if it's a neighbor. Then
start writing down how you do the work. That list is the first page of your future business. Then keep going: ten customers, then twenty, then the day you realize you
have more work than hours. When that day comes, don't just work harder. Hire, train and build. That's the moment a side hustle starts
becoming a company. And if you start one of these, tell me in the comments which one you picked. I read them, and your story might help
someone else take their first step. I'm Ryan Rover. Start small, think big, and
I'll see you in the next video.""")

save("video17", "20 Side Hustles That Actually Turn Into Businesses", [
    "U.S. Small Business Administration, Office of Advocacy, small business profiles (most small businesses have no employees)",
    "IRS, self-employment tax (applies to net earnings of $400 or more)",
    "Bureau of Labor Statistics, self-employment data",
    "Crew math: simplified illustration (20 jobs at $100 profit vs 120 jobs at $40 profit)",
], "side hustle to business")
