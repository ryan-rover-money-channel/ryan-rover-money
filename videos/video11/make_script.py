import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short


def biz(n, title, sub, card_text, how, watch, q1, c1, q2, c2):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"BUSINESS {n}")
    sc(how, q1, c1)
    sc(watch, q2, c2)

# ---------------- Intro ----------------
ch("Intro")
short("The most boring businesses in America quietly make millionaires. Here are twenty five.")
pr("""Hi, I'm Ryan Rover. When people imagine getting rich from a business, they picture tech startups, apps and venture capital.
But a lot of quiet millionaires in America made their money doing something much less exciting. Washing cars. Storing boxes.
Killing bugs. Pumping septic tanks. Boring businesses. And boring, it turns out, can be beautiful.""")
card("""Twenty five boring businesses. No apps, no hype, no viral videos. Just services people need, again and again, whether the
economy is booming or not.""",
     {"type": "stat", "label": "boring businesses", "big": "25", "sub": "that quietly make millionaires"})
sc("""Here's why boring works. Boring businesses usually solve a problem people can't or won't solve themselves. They often have
repeat customers. Many are local, so a giant tech company can't easily take them over. And because they're not glamorous, there's
often less competition from people chasing the next big thing.""",
   "Small business storefront", "WHY BORING WORKS")
sc("""Back in the nineteen nineties, Thomas Stanley and William Danko wrote The Millionaire Next Door. They found that many American
millionaires were self employed, and many of them ran what the authors called dull, normal businesses: contractors, pest control,
cleaning, welding, and more. Not famous. Not flashy. Just profitable for a long time.""",
   "Old books library", "THE MILLIONAIRE NEXT DOOR")
sc("""In this video, twenty five of those businesses: how they make money, and what to watch out for. Then we'll look at the whole
idea from three angles. The numbers behind small business. The psychology of the owners who succeed. And a playbook for starting or
buying one, without betting everything you have.""",
   "Notebook with financial notes", "25 BUSINESSES, 3 ANGLES")
pr("""One honest warning first. No business is guaranteed to make money, and many small businesses fail. This video is about
understanding the models, not about promises. Let's go.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Small business counts come from the U.S. Small Business Administration's Office of Advocacy. Business survival rates come
from the Bureau of Labor Statistics. Wage figures for skilled trades come from the Bureau of Labor Statistics Occupational Outlook
Handbook. Where we give example numbers for a business, they're simple illustrations, not industry averages, because results vary
enormously by location, management and luck. This is education, not financial or business advice.""",
   "Bureau of Labor Statistics building", "OUR SOURCES")

# ---------------- Angle 1: numbers ----------------
ch("Angle 1: The numbers")
pr("""Angle one. The numbers. Let's look at the reality of small business in America before we get excited.""")
card("""The SBA Office of Advocacy counts more than thirty three million small businesses in the United States. They employ nearly
half of all private sector workers.""",
     {"type": "stat", "label": "U.S. small businesses", "big": "33M+", "sub": "SBA Office of Advocacy"})
sc("""Thirty three million. That's a lot of businesses, and the vast majority have no employees at all. They're one person
operations: a consultant, a handyman, a freelance bookkeeper. Most small businesses aren't trying to become the next big company.
They're trying to give their owner a good living and, eventually, something valuable to sell.""",
   "Person working from home laptop", "MOSTLY ONE PERSON")
sc("""And that's the key mindset shift for this whole video. A boring business doesn't have to become huge to change your life. A single
well run location, route or service area that pays its owner a solid income and builds value over twenty years can be the difference
between retiring on a modest salary and retiring as a millionaire.""",
   "Small business owner smiling", "IT DOESN'T HAVE TO BE HUGE")
card("""But survival is hard. Bureau of Labor Statistics data shows roughly one in five new businesses close within their first year,
and about half are gone within five years.""",
     {"type": "compare", "left": {"label": "After 1 year", "big": "~80%", "sub": "still open"},
      "right": {"label": "After 5 years", "big": "~50%", "sub": "still open"},
      "note": "Bureau of Labor Statistics, Business Employment Dynamics (approximate)"})
sc("""So why talk about boring businesses at all? Because the failure rate isn't spread evenly. Businesses with proven demand,
simple operations and repeat customers tend to have better odds than brand new ideas that need to convince people they want
something. A plumber doesn't need to convince anyone that pipes break. Demand is already there.""",
   "Plumber fixing pipe", "PROVEN DEMAND")
sc("""And the reward can be big. The Federal Reserve's Survey of Consumer Finances has consistently found that families who own a
business tend to have a much higher median net worth than families who don't. Business ownership is one of the main paths to
wealth in America, alongside real estate and long term investing. It's riskier, but it's also one of the few paths where your
upside isn't capped by a salary.""",
   "Federal Reserve Bank building columns", "OWNERS HAVE MORE WEALTH")
sc("""So what makes a boring business good? Look for five traits. One, demand that doesn't depend on trends. People need clean clothes,
working pipes and no termites in any decade. Two, recurring revenue: customers who pay every week, month or season instead of once.
Three, a local moat, meaning the work happens in a physical place, so a website on the other side of the world can't easily take your
customers.""",
   "Map and compass", "TRAITS 1 TO 3")
sc("""Four, a reason most people avoid it. Dirty, smelly, physical, or simply unglamorous work keeps competition lower than in businesses
everyone dreams about. And five, a path to systems. The best boring businesses can eventually run with a manager and a team, so the owner
earns from the business instead of being the business. When you look at each of the twenty five businesses in this video, check how many
of these five traits it has.""",
   "Notebook with financial notes", "TRAITS 4 AND 5")
sc("""And here's one more number worth knowing. Many owners of established service businesses say the hardest part isn't finding
customers. It's finding and keeping good workers. In the skilled trades especially, demand for qualified people has been strong. That's a
challenge if you're an owner, but it's also an opportunity if you're thinking about learning a trade first, getting paid while you learn
how the business really works.""",
   "Construction workers", "THE REAL BOTTLENECK")
pr("""Okay. Twenty five boring businesses. We'll start with the ones that run on machines, because machines don't call in sick.""")

# ---------------- Businesses ----------------
biz(1, "Laundromats", "quarters, every single week",
"""Business number one. Laundromats.""",
"""Millions of Americans don't have a washer and dryer at home, especially renters in apartments. They need to wash clothes every
week, no matter what the economy is doing. A laundromat sells machine time, plus extras like wash and fold service, vending, and
sometimes pickup and delivery. Many owners run them with few or no full time staff.""",
"""What to watch: machines are expensive, and a lease, water and utility costs can eat profits. Location is everything, ideally near
dense apartment housing. Many people buy an existing laundromat rather than build one, and look closely at the age of the machines
and the remaining years on the lease before signing anything.""",
"Laundromat washing machines", "WEEKLY DEMAND",
"Apartment building", "LOCATION AND LEASE")

biz(2, "Car washes", "dirty cars never go out of style",
"""Business number two. Car washes.""",
"""Car washes range from self serve bays to fully automated tunnels. A big trend in recent years has been monthly memberships:
customers pay a flat fee for unlimited washes, which creates predictable, recurring revenue. Automated washes can serve a lot of cars
per hour with a small team.""",
"""What to watch: building a modern tunnel wash can cost millions, and competition has grown as investors have poured into the
industry. Water, equipment repairs and weather all affect results. Smaller self serve washes cost less to buy, but usually earn less
too. Study local competition carefully.""",
"Car wash", "MONTHLY MEMBERSHIPS",
"Car wash bay", "WATCH THE COMPETITION")

biz(3, "Self storage", "people's stuff, paying rent",
"""Business number three. Self storage.""",
"""Americans have a lot of stuff, and they move, downsize, divorce, renovate and inherit. Self storage rents small spaces month by
month. Once a facility is full, costs are relatively low: some staff, security, maintenance and marketing. Many customers stay much
longer than they planned.""",
"""What to watch: building a facility takes land and serious capital, and new supply in an area can push prices down. Large public
companies dominate in many cities. Smaller investors often look at buying existing facilities in growing towns, or converting old
buildings.""",
"Self storage units", "STUFF PAYS RENT",
"Construction site", "CAPITAL AND COMPETITION")

biz(4, "Vending machines", "small sales, many locations",
"""Business number four. Vending machines.""",
"""Vending is one of the easiest businesses to start small. You buy a machine, place it in a location like an office, a gym or a
factory, often sharing a cut with the location owner, and restock it regularly. Modern machines accept cards and phones, and some
send sales data so you only restock when needed.""",
"""What to watch: profits per machine are often modest, so the business only becomes meaningful with many machines and efficient
routes. Good locations are competitive. Machines can be damaged or stolen. Treat online claims of huge passive income from one machine
with a lot of skepticism.""",
"Vending machine", "START SMALL",
"Delivery van driving", "ROUTES MATTER")

biz(5, "ATMs", "a fee every time",
"""Business number five. ATM machines.""",
"""Independent ATM owners place machines in bars, convenience stores, events and other spots where people need cash. Each withdrawal
earns a surcharge fee, often split with the location. Once a machine is installed, the main jobs are keeping it filled with cash and
running.""",
"""What to watch: cash use has been declining as cards and phones take over, which is a real long term risk. You need cash to load the
machines, and security matters. Like vending, this business usually only works at scale, with many machines in busy locations.""",
"ATM machine", "A FEE EVERY TIME",
"Credit card close up", "CASH IS DECLINING")

pr("""Next, the trades and home services. These are the businesses Stanley and Danko kept finding among quiet millionaires.""")

biz(6, "Plumbing", "pipes always break",
"""Business number six. Plumbing.""",
"""When a pipe bursts, nobody shops for the cheapest option. They call someone who can come now. Plumbing combines emergency work,
renovations and new construction. The Bureau of Labor Statistics reported a median pay for plumbers of around sixty three thousand
dollars a year in twenty twenty four, and owners who build a team can earn much more.""",
"""What to watch: it takes years of training and licensing, which is also what protects good plumbers from competition. Growing
beyond yourself means hiring, managing and finding skilled workers, which many trades owners say is the hardest part of the business.""",
"Plumber fixing pipe", "PIPES ALWAYS BREAK",
"Construction workers", "HIRING IS THE HARD PART")

biz(7, "HVAC", "heat and air, every season",
"""Business number seven. Heating, ventilation and air conditioning.""",
"""Every home and commercial building needs heating and cooling, and systems break, age out and need regular maintenance. Many HVAC
companies sell maintenance plans, which create recurring revenue and steady customers. Demand spikes in heat waves and cold snaps.""",
"""What to watch: like plumbing, HVAC needs licensed technicians and training, and the busy seasons can be exhausting. Equipment costs
and changing efficiency regulations matter. Owners who build strong maintenance plan programs often have the most stable businesses.""",
"Air conditioner unit", "EVERY SEASON",
"Technician repairing", "MAINTENANCE PLANS")

biz(8, "Electrical contracting", "the grid inside every building",
"""Business number eight. Electrical contracting.""",
"""Electricians wire new homes, upgrade old panels, install EV chargers and solar systems, and fix problems. The Bureau of Labor
Statistics reported a median pay for electricians of around sixty two thousand dollars in twenty twenty four, and projects demand for
the trade to keep growing as buildings electrify.""",
"""What to watch: licensing takes years, and the work carries real safety risk. Contracting businesses depend on construction cycles,
so a housing slowdown can hurt. Many electrical contractors balance new construction with service work to smooth out the ups and
downs.""",
"Electrician working", "ELECTRIFICATION",
"House construction", "BALANCE THE CYCLES")

biz(9, "Pest control", "bugs don't take recessions off",
"""Business number nine. Pest control.""",
"""Termites, ants, roaches, rodents. Pest control is a classic boring business, and one of the most recurring. Many customers sign up
for quarterly or monthly service. Real estate transactions often require termite inspections, which adds steady demand.""",
"""What to watch: you need state licensing to apply many chemicals, and safety and regulations matter. Big national brands compete in
many markets. Smaller operators often win on service and local reputation, and some build routes that they eventually sell to larger
companies.""",
"Pest control spraying", "RECURRING SERVICE",
"Suburban houses street United States", "LOCAL REPUTATION")

biz(10, "Landscaping and lawn care", "grass keeps growing",
"""Business number ten. Landscaping and lawn care.""",
"""Lawns grow every week in the season, and many homeowners and businesses would rather pay someone than mow. You can start with a
mower and a trailer. Over time, businesses add services like design, irrigation, tree work and snow removal in winter.""",
"""What to watch: the barrier to entry is low, so competition is high and prices can be pressured. It's physical work, and it's
seasonal in many places. The owners who do well often focus on commercial contracts and recurring residential routes, not one time
jobs.""",
"Lawn mower grass", "GRASS KEEPS GROWING",
"Snow plow truck", "ADD WINTER WORK")

short("Nobody wants to pump septic tanks. That's exactly why it can pay so well.")
biz(11, "Septic services", "the job nobody wants",
"""Business number eleven. Septic pumping and portable toilets.""",
"""Around one in five American homes uses a septic system, according to the Environmental Protection Agency, and tanks need regular
pumping. Portable toilets are needed at every construction site, festival and outdoor event. These businesses are the definition of
unglamorous, which keeps a lot of people away.""",
"""What to watch: trucks and equipment are expensive, and there are environmental regulations on disposal. But demand is steady and
recurring, and many owners say that the very thing that makes it unappealing, the smell, is what protects them from competition.""",
"Septic truck", "1 IN 5 HOMES",
"Portable toilets construction site", "UNGLAMOROUS = LESS COMPETITION")

biz(12, "Junk removal", "people pay you to take their stuff",
"""Business number twelve. Junk removal.""",
"""Moving, renovations, estate cleanouts, office clear outs. People pay to make things disappear. A truck, a couple of strong workers
and good reviews can get you started. Some items can be donated, recycled or resold, which adds a bit of extra income.""",
"""What to watch: dump fees, fuel and labor are the big costs. Franchises compete in many cities. Success often comes from great
reviews, fast scheduling, and relationships with real estate agents and property managers who need cleanouts regularly.""",
"Junk removal truck", "TAKE IT AWAY",
"Moving truck boxes", "REAL ESTATE RELATIONSHIPS")

biz(13, "Commercial cleaning", "offices need cleaning every night",
"""Business number thirteen. Commercial cleaning.""",
"""Offices, clinics, gyms and schools need cleaning, often every night. Commercial contracts can be monthly and recurring, which makes
revenue predictable. Many owners start by cleaning themselves, then hire teams as they win more contracts.""",
"""What to watch: margins depend on managing labor well, and staff turnover can be high. Winning contracts takes bidding and
relationships. The owners who succeed usually build reliable systems and quality checks, so clients never have a reason to switch.""",
"Office cleaning janitor", "RECURRING CONTRACTS",
"Office building at dusk", "SYSTEMS AND QUALITY")

biz(14, "Pressure washing", "low start up, high visual impact",
"""Business number fourteen. Pressure washing.""",
"""Driveways, decks, siding, storefronts, parking lots. The results are dramatic, which makes marketing easy: before and after photos
sell themselves. Start up costs are relatively low compared with many businesses.""",
"""What to watch: low barriers mean lots of competition. Damage to property is a real risk if you don't know what you're doing, so
training and insurance matter. Commercial clients, like restaurants and property managers, can provide steadier recurring work than
one time homeowners.""",
"Pressure washing driveway", "BEFORE AND AFTER",
"Parking lot", "COMMERCIAL CLIENTS")

biz(15, "Pool service", "weekly visits, all season",
"""Business number fifteen. Pool cleaning and maintenance.""",
"""Pool owners in warm states need weekly cleaning, chemical balancing and equipment repairs. A route of regular customers creates
recurring monthly income. Repairs and equipment replacements add higher value jobs on top.""",
"""What to watch: it's seasonal in colder areas, and chemicals require care and knowledge. Some owners build routes and later sell
them to larger operators. Good communication with customers is what keeps routes from shrinking.""",
"Swimming pool backyard", "A ROUTE OF REGULARS",
"Pool cleaning", "ROUTES CAN BE SOLD")

pr("""Quick pause. If you'd like a deeper video on any of these businesses, tell me which one in the comments. And subscribe, because
the next videos in this series go into the real numbers: laundromats, car washes, storage units, and how to buy a business instead of
starting one. Now, business sixteen.""")

biz(16, "Auto repair", "cars keep getting older",
"""Business number sixteen. Auto repair.""",
"""Americans are keeping their cars longer, and S and P Global Mobility has reported the average age of cars and light trucks on U.S.
roads at a record of more than twelve and a half years. Older cars need more repairs. Independent shops that earn trust can keep
customers for decades.""",
"""What to watch: cars are getting more complex, with electronics and electric vehicles requiring new tools and training. Finding good
technicians is a challenge. Shops that invest in diagnostics and build a reputation for honesty tend to thrive.""",
"Car repair garage mechanic", "OLDER CARS, MORE REPAIRS",
"Mechanic computer diagnostics", "TRUST IS EVERYTHING")

biz(17, "Towing", "someone always needs a tow",
"""Business number seventeen. Towing.""",
"""Breakdowns, accidents, illegally parked cars, repossessions. Towing companies often have contracts with police departments,
property managers and roadside assistance programs, which create steady volume.""",
"""What to watch: trucks are expensive, insurance is costly, and the work can be dangerous and around the clock. Regulations vary by
city. Strong contracts with clubs, insurers and local businesses often matter more than random calls.""",
"Tow truck", "CONTRACTS MATTER",
"Car with flat tire on road", "24/7 WORK")

biz(18, "Dumpster rental", "every project makes trash",
"""Business number eighteen. Dumpster rental.""",
"""Contractors, roofers, renovators and homeowners cleaning out a house all need roll off dumpsters. You drop it off, pick it up, and
dispose of the contents. Repeat contractor customers can provide steady volume.""",
"""What to watch: trucks and containers require capital, and landfill fees and fuel are major costs. Local relationships with
contractors are the core of the business. Pricing carefully for weight and distance protects profits.""",
"Dumpster construction site", "EVERY PROJECT MAKES TRASH",
"Garbage truck", "WATCH LANDFILL FEES")

biz(19, "Bookkeeping and tax prep", "every business needs it",
"""Business number nineteen. Bookkeeping and tax preparation.""",
"""Every small business needs bookkeeping, and millions of households pay someone to do their taxes. Monthly bookkeeping clients
create recurring revenue. Tax season brings a big wave of work every year.""",
"""What to watch: you need skills and accuracy, and certain services require credentials. Software has automated parts of the work, so
the best firms focus on advice and service, not just data entry. Busy season can mean very long hours.""",
"Accountant desk calculator", "MONTHLY CLIENTS",
"Tax forms on desk", "TAX SEASON")

biz(20, "Funeral services", "the oldest recurring demand",
"""Business number twenty. Funeral homes.""",
"""It's a hard topic, but demand is certain. Funeral homes are often family owned for generations, and trust and reputation in a
community are everything. Services include planning, preparation, cremation and pre need contracts.""",
"""What to watch: licensing is required, buildings and vehicles are expensive, and the shift toward cremation has changed revenue for
many funeral homes. The emotional side of the work is demanding. Consolidators buy independent funeral homes in many markets.""",
"Funeral home building", "CERTAIN DEMAND",
"Cemetery", "TRUST AND REPUTATION")

biz(21, "Mobile home and RV parks", "renting the land underneath",
"""Business number twenty one. Mobile home parks and RV parks.""",
"""In many mobile home parks, residents own their homes but rent the land underneath. Moving a manufactured home is expensive, so
residents tend to stay for many years. RV parks earn from travelers and long term stays.""",
"""What to watch: these businesses have faced criticism over rising lot rents, and some states have strengthened tenant protections.
Infrastructure like water and sewer can be costly to maintain. Investors who do this well treat residents fairly and keep parks safe
and well run.""",
"Mobile home park", "RENT THE LAND",
"RV camping park", "TREAT RESIDENTS FAIRLY")

biz(22, "Parking lots", "a lot that earns while it sits",
"""Business number twenty two. Parking lots.""",
"""In busy downtowns, near stadiums, airports and hospitals, parking is in demand. A lot can earn steady income with simple operations,
especially with automated payment systems.""",
"""What to watch: land in good locations is expensive. Remote work and ride sharing have changed demand in some cities. Many lot owners
see the land itself as a long term investment, with parking income paying the bills while they wait.""",
"Parking lot", "LAND THAT EARNS",
"City downtown street", "LOCATION, LOCATION")

biz(23, "Window and gutter cleaning", "ladders and repeat customers",
"""Business number twenty three. Window and gutter cleaning.""",
"""Homes need gutters cleaned once or twice a year. Storefronts want clean windows every week or month. It's simple work with low start
up costs, and customers who are happy tend to book again and again.""",
"""What to watch: ladder work has real safety risks, so training and insurance are essential. It's seasonal in some areas. Offering
maintenance plans and bundling services like pressure washing can smooth out revenue.""",
"Window cleaning ladder", "REPEAT CUSTOMERS",
"Gutter cleaning house", "SAFETY FIRST")

biz(24, "Tire shops", "rubber wears out",
"""Business number twenty four. Tire shops.""",
"""Every car needs new tires every few years, plus rotations, balancing and repairs. Tire shops often add oil changes, alignments and
brakes. With older cars on the road, demand for maintenance stays steady.""",
"""What to watch: inventory takes capital and space, and big chains compete on price. Local shops win on service and speed. Building
relationships with fleets, like delivery companies and contractors, can provide steady volume.""",
"Tire shop", "RUBBER WEARS OUT",
"Delivery van driving", "FLEET CUSTOMERS")

biz(25, "Sign and print shops", "every business needs to be seen",
"""Business number twenty five. Sign and print shops.""",
"""Every new business needs a sign, banners, vehicle wraps, menus and business cards. Real estate agents need yard signs. Events need
banners. It's a steady, local, business to business service.""",
"""What to watch: equipment is an investment, and online printers compete on simple products. Local shops win on custom work,
installation and speed. Relationships with contractors, agents and new businesses are the lifeblood.""",
"Print shop", "EVERY BUSINESS NEEDS SIGNS",
"Small business storefront", "LOCAL RELATIONSHIPS")

# ---------------- Where the millions come from ----------------
short("Most business owners don't get rich from profits. They get rich when they sell.")
ch("Where the millions really come from")
pr("""Here's something most people don't understand about boring businesses. The biggest payday usually isn't the yearly profit. It's
what the business is worth when you sell it.""")
sc("""Small businesses are often valued as a multiple of their yearly profit, sometimes called seller's discretionary earnings. A
small service business might sell for something like two to four times its yearly earnings, depending on the industry, how stable it
is, and how much it depends on the owner. These are rough ranges, and every deal is different.""",
   "Business meeting handshake", "A MULTIPLE OF PROFIT")
sc("""So imagine a pest control company that earns two hundred thousand dollars a year for its owner. At three times earnings, it might
sell for around six hundred thousand dollars. Now imagine the owner spends five years building recurring contracts, training a manager,
and documenting everything, and profit grows to three hundred fifty thousand. At a higher multiple, because it no longer depends on the
owner, the business might be worth well over a million.""",
   "Pest control spraying", "FROM $600K TO $1M+")
sc("""That's the hidden math of boring businesses. Every dollar of steady, recurring profit can add several dollars to what the business
is worth. And the things that raise the multiple are the same things we talked about: recurring customers, systems, clean records, and
an owner who isn't doing every job personally.""",
   "Graph trending upward", "EVERY $1 OF PROFIT = SEVERAL $ OF VALUE")
sc("""This is why many owners in these industries say the goal is to build something you could sell, even if you never do. A business
that depends entirely on you is really a job you own. A business that runs on systems is an asset, and assets are what create
millionaires.""",
   "Factory machine gears", "A JOB OR AN ASSET?")

# ---------------- Three owners ----------------
ch("Three example owners")
pr("""Let's make it concrete with three example owners. They're made up, but their paths are common in these industries.""")
sc("""Owner one, Luis. Luis started pressure washing on weekends with about three thousand dollars of equipment. After a year, he had
enough repeat customers to quit his warehouse job. He added gutter cleaning and window washing, hired two workers, and focused on
restaurants and property managers who needed regular service. Eight years later, his small company gives him a solid income, and he
works mostly on sales and scheduling, not on the ladder.""",
   "Pressure washing driveway", "LUIS: STARTED SMALL")
sc("""Owner two, Karen. Karen spent twenty years in corporate accounting. Instead of starting from scratch, she used savings and a small
business loan to buy an existing laundromat with good records and a long lease. She replaced the oldest machines, added wash and fold
and pickup service, and raised revenue steadily. She kept her emergency fund and retirement accounts untouched, so the business was a
calculated risk, not a bet on everything.""",
   "Laundromat washing machines", "KAREN: BOUGHT PROVEN")
sc("""Owner three, Darnell. Darnell trained as an HVAC technician, worked for a larger company for six years, and learned how the
business really ran: pricing, scheduling, maintenance plans, hiring. When he started his own company, he already had skills, customers
who trusted him, and a plan. Within a decade, he had several technicians and hundreds of maintenance plan customers.""",
   "Air conditioner unit", "DARNELL: LEARNED FIRST")
sc("""Three different paths. Luis started small with almost no money. Karen bought a proven business with her savings. Darnell learned
the trade and the business first, then went out on his own. What they share is patience, careful money management, and a focus on
recurring customers. None of them got rich fast. All of them built something real.""",
   "Three people silhouettes", "THREE PATHS")

# ---------------- Red flags ----------------
ch("Red flags before you jump in")
pr("""Before you start or buy any business, watch for these red flags.""")
sc("""Red flag one. Someone selling a course or a business opportunity that promises passive income with little work. Many online
pitches for vending, ATMs or car washes make money mostly by selling the dream, not by running the business. Red flag two. A seller who
can't show clean financial records and tax returns. If the numbers aren't documented, assume they're not real.""",
   "Computer hacker keyboard", "RED FLAGS 1 AND 2")
sc("""Red flag three. A business where all the customers are tied to the owner personally. When the owner leaves, the customers might
too. Red flag four. A short lease, or a landlord who won't commit to renewing. Your location could disappear. Red flag five. Old
equipment that will need expensive replacement soon after you buy.""",
   "Paperwork documents desk", "RED FLAGS 3 TO 5")
sc("""And red flag six. Your own plan requires everything to go right. If the business only works with perfect revenue, no repairs and no
slow months, it's too fragile. Build in room for things to go wrong, because they will. The owners who survive are the ones who planned
for bad months while things were good.""",
   "Road sign curve ahead", "RED FLAG 6: NO ROOM FOR ERROR")

# ---------------- Angle 2: psychology ----------------
short("The people who get rich from boring businesses share these five traits.")
ch("Angle 2: The psychology")
pr("""Angle two. The psychology. Because the business is only half the story. The other half is the owner. What do people who succeed
with boring businesses have in common?""")
sc("""First, they don't need the business to be exciting. They get their excitement from results, from a growing customer list and a
healthy bank account, not from telling people at parties what they do. If you need your business to impress strangers, boring
businesses will feel painful. If you care about profits and freedom, they can feel wonderful.""",
   "Small business owner smiling", "RESULTS OVER IMAGE")
sc("""Second, they think in systems. The owners who build real wealth don't do every job forever. They write down how the work is done,
train people, and build routines so the business can run without them on site every hour. That's what turns a job into an asset someone
might want to buy one day.""",
   "Clock gears mechanism", "SYSTEMS")
sc("""Third, they're patient. Many boring businesses take years to build a customer base and a reputation. There's no overnight
success. But the reward for patience is a business with loyal customers and steady cash flow, which is exactly what makes it valuable.""",
   "Hourglass sand timer", "PATIENCE")
sc("""Patience also shows up in how they grow. Instead of borrowing heavily to expand fast, many successful owners add one truck, one
route, or one location at a time, funded mostly by profits. It's slower, but it means one bad year doesn't sink the whole company.
Growing at the speed of your cash flow is one of the oldest and safest rules in small business, and boring business owners tend to
follow it closely.""",
   "Delivery van driving", "GROW AT THE SPEED OF CASH")
sc("""Fourth, they're careful with money. Successful owners tend to reinvest profits, avoid unnecessary debt, and keep a cash cushion for
slow months. Stanley and Danko noticed that many of the business owner millionaires they studied lived well below their means, even
after they became wealthy.""",
   "Calculator and pen on financial papers", "CAREFUL WITH MONEY")
sc("""And fifth, they obsess over customers. In local service businesses, reputation is everything. Online reviews, word of mouth,
showing up on time. The owners who win treat every customer like they'll be telling ten friends, because they often do.""",
   "Business meeting handshake", "CUSTOMERS FIRST")

# ---------------- Angle 3: playbook ----------------
short("Here's how to get into a boring business without betting your life savings.")
ch("Angle 3: The playbook")
pr("""Angle three. The playbook. If one of these businesses interests you, here's how to explore it without risking everything.""")
sc("""Step one. Keep your foundation. Before you put money into any business, have an emergency fund, no high interest debt, and your
retirement savings going. A business is a risk, and risk should never threaten your family's basic security.""",
   "Piggy bank coins", "STEP 1: KEEP YOUR FOUNDATION")
sc("""Step two. Learn the business from the inside. Work in it, even part time, before you own it. Talk to owners in other cities who
won't see you as competition. Ask what surprised them, what their biggest costs are, and what they'd do differently. Most owners love
talking about their business.""",
   "Construction workers", "STEP 2: LEARN FROM INSIDE")
sc("""Step three. Start small or buy proven. You can start with low cost services, like pressure washing, cleaning or lawn care, and test
demand with almost no risk. Or you can buy an existing business with real customers and records. Both are usually safer than building
something big from scratch.""",
   "Small business storefront", "STEP 3: SMALL OR PROVEN")
sc("""Step four. Do the math honestly. Revenue isn't profit. List every cost: equipment, insurance, fuel, labor, rent, licenses, taxes,
and your own time. If the business only works when you work eighty hours a week for free, it's not a business yet. It's a hard job.""",
   "Spreadsheet on laptop", "STEP 4: HONEST MATH")
sc("""Step five. Protect yourself. Form the right legal structure, get proper insurance, and keep business and personal money completely
separate. A good accountant and, when buying, a lawyer, are worth their fees many times over.""",
   "Lawyer office documents", "STEP 5: PROTECT YOURSELF")
sc("""And step six. Build to sell, even if you never sell. Keep clean records, build systems, train people, and grow recurring revenue.
Those are the things that make a business valuable to a buyer, and they're also the things that let you take a vacation without
everything falling apart.""",
   "Notebook with financial notes", "STEP 6: BUILD TO SELL")

# ---------------- Questions ----------------
ch("Questions people ask")
pr("""Let me answer the questions people ask most about boring businesses.""")
sc("""Question one. Which one is the best? There's no single best. The best business for you depends on your skills, your money, your
location and what you can tolerate. Someone who loves physical work might thrive in landscaping. Someone who likes numbers might prefer
bookkeeping or vending routes.""",
   "Person standing at crossroads", "WHICH ONE IS BEST?")
sc("""Question two. Are these businesses really passive? Mostly no. Vending, laundromats and storage are often called passive, but they
still need management, repairs and attention. Passive usually means you've hired someone else to do the active part. Question three.
How much money do I need? Some services start with a few thousand dollars of equipment. Others, like car washes or storage, can cost
millions.""",
   "Vending machine", "IS IT PASSIVE?")
sc("""Question four. Should I buy a franchise? Franchises offer a proven system and brand, but come with fees and rules. Read the
franchise disclosure document carefully, and talk to current and former franchise owners before signing. Question five. Will AI replace
these businesses? Many of them involve physical work in specific places, which is much harder to automate than office work. That's part
of their appeal.""",
   "Paperwork documents desk", "FRANCHISE? AI?")
sc("""Question six. Can I run one of these while keeping my job? Some, yes. Vending routes, small cleaning contracts, pressure washing on
weekends, or a laundromat with a good manager can be started alongside a job. It's often the smartest way to test a business, because
your salary covers your life while the business proves itself. Just be honest about your time and energy, and check your employment
contract for conflicts.""",
   "Person working from home laptop", "KEEP YOUR JOB?")
sc("""Question seven. Should I use my retirement savings to buy a business? Be very careful. There are complex arrangements that allow it,
but they carry real risks and rules, and if the business fails you could lose both your business and your retirement. Most people are
better off using savings outside retirement accounts, a small business loan, or seller financing, where the seller lets you pay part of
the price over time.""",
   "Bank building United States", "USE RETIREMENT MONEY?")

# ---------------- Recap ----------------
ch("Recap: 25 boring businesses")
sc("""Let's recap. The machine businesses: laundromats, car washes, self storage, vending machines and ATMs. The trades: plumbing, HVAC,
electrical, pest control and landscaping. The jobs nobody wants: septic, junk removal, commercial cleaning, pressure washing and pool
service.""",
   "Notebook with financial notes", "BUSINESSES 1 TO 15")
sc("""Then auto repair, towing, dumpster rental, bookkeeping and tax prep, and funeral services. And the land and local businesses: mobile
home and RV parks, parking lots, window and gutter cleaning, tire shops, and sign and print shops.""",
   "Small business storefront", "BUSINESSES 16 TO 25")
sc("""And the three angles. The numbers: tens of millions of small businesses, about half survive five years, but owners tend to build
much more wealth. The psychology: results over image, systems, patience, careful money and obsession with customers. And the playbook:
keep your foundation, learn from the inside, start small or buy proven, do honest math, protect yourself, and build to sell.""",
   "Map and compass", "NUMBERS, PSYCHOLOGY, PLAYBOOK")
sc("""And here's the bigger lesson behind all twenty five businesses. Wealth often hides in plain sight, in the services everybody uses
and nobody thinks about. The laundromat on the corner. The pest control truck in your neighbor's driveway. The company that pumps the
septic tank at the edge of town. Behind many of them is an owner who saw a boring, steady need, served it well for years, and quietly
built something worth far more than a salary. You don't need a brilliant idea. You need a real need, a lot of patience, and the
discipline to run it well.""",
   "Small business storefront", "WEALTH IN PLAIN SIGHT")
sc("""And if owning a business isn't for you, that's completely fine too. You can still benefit from the same idea. Broad index funds
make you a part owner of thousands of businesses, boring and exciting alike. Owning, in one form or another, is how most wealth gets
built. The question is just which form fits your life.""",
   "New York Stock Exchange trading floor", "OWNERSHIP, ANY FORM")

# ---------------- Close ----------------
ch("What to do next")
pr("""So here's your homework. Pick two businesses from this list that fit your skills and your budget. This week, call one owner and
ask them about their business. That one conversation will teach you more than a hundred videos, including this one. Ask what they love about it,
what they hate about it, and what they wish they'd known on day one. If you want the full plan for building
wealth, it's in my playbook, link in the description. I'm Ryan Rover. See you in the next one.""")

save("video11", "25 Boring Businesses That Quietly Make Millionaires", [
    "U.S. Small Business Administration, Office of Advocacy, Frequently Asked Questions (more than 33 million small businesses; nearly half of private-sector employment)",
    "Bureau of Labor Statistics, Business Employment Dynamics, establishment survival (about 1 in 5 close in year one, about half by year five)",
    "Federal Reserve, Survey of Consumer Finances (business-owning families have higher median net worth)",
    "Bureau of Labor Statistics, Occupational Outlook Handbook (plumbers and electricians median pay, 2024)",
    "U.S. Environmental Protection Agency, Septic Systems Overview (about one in five U.S. homes)",
    "S&P Global Mobility, average age of light vehicles in operation (record above 12.5 years)",
    "Thomas J. Stanley and William D. Danko, The Millionaire Next Door (1996)",
], "25 boring businesses")
