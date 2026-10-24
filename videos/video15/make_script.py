import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short


def biz(n, name, sub, a, b, q1, c1, q2, c2):
    ch(f"{n}. {name}")
    card(f"Number {n}. {name}. {sub}", {"type": "list", "n": n, "title": name, "sub": sub}, f"STILL HERE IN 2040: {n}")
    sc(a, q1, c1)
    sc(b, q2, c2)
    t, q, c = GET_IN[n]
    sc("How to get in. " + t, q, c)


GET_IN = {
    1: ("""The classic path is an apprenticeship, often paid, through a union or a contractor, followed by a journeyman license and eventually a
master license. Many owners work for others for years, then start their own shop or buy one from a retiring plumber. Plumbers who learn the
business side, pricing, marketing and hiring, are the ones who turn a trade into a company.""", "Older plumber with apprentice", "APPRENTICE, LICENSE, OWN"),
    2: ("""Like plumbing, electrical work usually starts with a paid apprenticeship lasting several years. Licensed electricians can later
become contractors, which typically requires additional exams and insurance. A smart niche, like EV chargers or generators, can help a new
company stand out against established competitors.""", "Electrician working on panel", "PICK A NICHE"),
    3: ("""Technicians often start through trade school or on the job training, then earn certifications, including the EPA certification needed
to handle refrigerants. Owners who focus early on selling maintenance agreements build the steadiest companies and the most valuable ones to
sell later.""", "Technician servicing furnace", "SELL AGREEMENTS EARLY"),
    4: ("""Many roofing owners start as crew members or salespeople, learning how to estimate jobs and work with insurance adjusters. Good
insurance coverage, safety training and a reputation for honest storm work matter more than anything. Avoid companies that chase storms and
disappear, because reputation is the real asset.""", "Roofers working on house", "REPUTATION IS THE ASSET"),
    5: ("""Technicians usually train at community colleges or trade schools and earn certifications. Opening a shop takes equipment and a
location, so many owners buy an existing garage with loyal customers. Adding EV and hybrid training is a smart way to stay relevant as the
fleet changes.""", "Mechanic working under car", "TRAIN FOR WHAT'S NEXT"),
    6: ("""Funeral directors need specialized education and a state license. Ownership often passes within families, but many owners have no
successor, which can create opportunities to buy. Related businesses, like monument makers, memorial planning or cremation services, can
have lower barriers.""", "Flowers at memorial", "NO SUCCESSOR, OPPORTUNITY"),
    7: ("""Non medical home care agencies, which help with daily tasks rather than medical treatment, can have lower startup costs than
facilities, though many states require licenses. Franchises exist that provide training and systems. The key challenge is recruiting and
keeping good caregivers.""", "Caregiver helping elderly person", "START NON MEDICAL"),
    8: ("""Dentistry requires dental school and a license, so most people enter as investors or through related services. Dentists who own
their practices often build significant wealth over a career, especially if they buy a practice from a retiring dentist with an established
patient base.""", "Dentist with patient", "BUY A RETIRING PRACTICE"),
    9: ("""Grooming, dog walking, pet sitting, boarding and training can start small, sometimes from home where rules allow. Building a list of
repeat clients is the goal. Grooming in particular can be done from a mobile van, which removes the need for a storefront.""", "Dog grooming", "START SMALL, MOBILE"),
    10: ("""Many providers start with a licensed home daycare, which has lower costs than a center. Licensing rules, staff ratios and
inspections vary by state, so contact your state licensing agency first. Waiting lists in your area are a strong sign of unmet demand.""", "Children playing in daycare", "HOME DAYCARE FIRST"),
    11: ("""You can start with a truck, a trailer and basic equipment, then move toward commercial contracts and specialties like irrigation or
tree care. Certified arborists can charge more for tree work. Pricing by the job, not by the hour, often improves profits as your crew gets
faster.""", "Landscaper mowing lawn", "MOVE TOWARD CONTRACTS"),
    12: ("""Technicians need state pesticide licenses, and companies need insurance. Many owners work for a larger company first to learn
treatments and pricing, then start their own with a focus on recurring residential plans.""", "Exterminator spraying", "LEARN, THEN LAUNCH"),
    13: ("""Start with residential or small office cleaning, build reliable systems and crews, then pursue larger commercial contracts. Bonding
and insurance help win trust. Clear checklists and quality inspections keep customers from switching.""", "Cleaning supplies", "SYSTEMS AND CHECKLISTS"),
    14: ("""Tax preparers need an IRS preparer tax identification number, and many become enrolled agents or CPAs for more credibility and
higher fees. Starting with seasonal tax work and adding year round bookkeeping clients is a common path.""", "Accountant meeting client", "SEASONAL TO YEAR ROUND"),
    15: ("""Agents need state licenses for the types of insurance they sell. Many start at an existing agency, build a book of clients, then open
their own independent agency or buy a retiring agent's book of business.""", "Insurance documents", "BUILD A BOOK"),
    16: ("""Most people enter storage as investors, buying a small existing facility or partnering with experienced operators. Study local
occupancy and competitor prices carefully before buying, because oversupplied markets can mean price wars.""", "Storage units", "STUDY OCCUPANCY"),
    17: ("""Barbers and stylists need state licenses through cosmetology or barber school. Many work at a shop for years, build a loyal client
list, then open their own shop and rent chairs to other licensed professionals.""", "Barber cutting hair", "BUILD A CLIENT LIST"),
    18: ("""Some states license locksmiths and others don't, so check your local rules. Training programs and working under an experienced
locksmith are common starting points. Adding smart lock, camera and access control installation expands what you can offer.""", "Locksmith working on door", "ADD SMART SECURITY"),
    19: ("""Local moving can start with a rented or used truck and a reliable crew. Interstate moves require federal registration with the
Department of Transportation. Proper insurance and transparent pricing build the reviews that drive growth.""", "Moving truck", "TRANSPARENT PRICING"),
    20: ("""Dumpster rental and junk removal are common entry points into waste, requiring less capital than a full hauling company. Specialty
niches, like construction debris or recycling for businesses, can also be good places to start.""", "Garbage truck on street", "ENTER THROUGH A NICHE"),
}

# ---------------- Intro ----------------
ch("Intro")
short("Robots, AI, self driving cars. And yet these 20 businesses will almost certainly still be here in 2040.")
pr("""Hi, I'm Ryan Rover. Everyone is worried about which jobs and businesses will disappear. AI writes, robots build, apps replace
whole industries. But some businesses have survived every wave of technology for a hundred years, and they'll very likely survive the
next one too. Today, we're going through twenty small businesses that will almost certainly still exist in 2040, why they're so hard to
replace, and how you could own one.""")
card("""Twenty small businesses built to last. Physical, local, trusted, and needed in good times and bad.""",
     {"type": "stat", "label": "built to last", "big": "2040", "sub": "20 businesses that survive the next wave"})
sc("""Here's the test we used. A business makes this list if it needs to happen in the physical world, close to the customer, if people
need it whether the economy is good or bad, and if trust matters more than price. Technology will change how these businesses work, but
it's very unlikely to remove the need for them.""",
   "Small town main street", "THE TEST: PHYSICAL, LOCAL, NEEDED, TRUSTED")
sc("""A quick warning. Nobody can predict the future perfectly. Some of these businesses will change a lot by 2040, and individual
companies will still succeed or fail based on how they're run. Any numbers we use are illustrations, not guarantees. The goal is to help
you think about durability, which is one of the most underrated parts of building wealth.""",
   "Calendar pages flying", "NOBODY KNOWS THE FUTURE FOR SURE")
sc("""We'll go through all twenty, then look at them from three angles. The numbers, meaning why durable businesses are worth more. The
psychology, meaning why people chase shiny trends instead. And the playbook, meaning how to pick a durable business and get started.""",
   "Notebook with financial notes", "20 BUSINESSES, 3 ANGLES")
pr("""Let's start with the most essential one of all.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Job outlook information comes from the Bureau of Labor Statistics Occupational Outlook Handbook, which projects employment by
occupation. Population aging data comes from the U.S. Census Bureau. Small business lending information comes from the U.S. Small
Business Administration. This video is education, not financial, legal or business advice.""",
   "Government building", "SOURCES")

# ---------------- The 20 ----------------
biz(1, "Plumbing", "water and waste will always need pipes",
    """Number one. Plumbing. Every home, office, hospital and restaurant depends on clean water coming in and waste going out. Pipes leak,
water heaters fail, drains clog. That will be just as true in 2040 as it is today. And every repair happens in a specific place, under a
specific sink, which software alone can't do.""",
    """Many experienced plumbers are approaching retirement, and the trade has struggled to attract enough young people, which could support
strong demand for those who stay. Plumbing companies can add maintenance plans, water heater installations and remodeling work to build
steady revenue. Licensing takes years, which also protects those who have it.""",
    "Plumber working on pipes", "WATER ALWAYS NEEDS PIPES",
    "Older plumber with apprentice", "AGING WORKFORCE, STEADY DEMAND")

biz(2, "Electrical contracting", "the world is getting more electric, not less",
    """Number two. Electrical work. Electric vehicles, heat pumps, solar panels, home batteries and data centers all mean more wiring, more
panel upgrades and more electrical work. The more the world electrifies, the more electricians it needs.""",
    """Electrical contractors serve homes, businesses and new construction. Like plumbing, it requires a license and years of training, which
limits competition. Specialties like EV charger installation, solar connections and generator installations can add higher value work to
a small company.""",
    "Electrician working on panel", "MORE ELECTRIC EVERY YEAR",
    "Electric car charging", "NEW SPECIALTIES")

biz(3, "HVAC", "heating and cooling never go out of style",
    """Number three. Heating, ventilation and air conditioning. When the air conditioning dies in July or the furnace fails in January,
homeowners call immediately. Extreme weather and the shift toward heat pumps keep this industry busy.""",
    """HVAC companies earn money from installations, repairs and especially maintenance agreements, where customers pay yearly for tune ups and
priority service. Those agreements create recurring revenue, and well run HVAC businesses with many service agreements often attract
buyers when owners retire.""",
    "Air conditioning unit outside house", "WHEN IT BREAKS, THEY CALL",
    "Technician servicing furnace", "MAINTENANCE AGREEMENTS")

biz(4, "Roofing", "every roof eventually wears out",
    """Number four. Roofing. Every roof has a lifespan. Storms, hail and age eventually mean repairs or replacement. A roof isn't something a
homeowner can skip or delay forever, because a leaking roof destroys everything underneath it.""",
    """Roofing jobs can be large, and insurance claims after storms create waves of demand. The work is physical, seasonal in some places,
and requires good crews and safety practices. Roofing companies with strong reputations and good insurance relationships can do very well.""",
    "Roofers working on house", "EVERY ROOF WEARS OUT",
    "Storm damage on house", "STORMS CREATE DEMAND")

biz(5, "Auto repair", "even electric cars need mechanics",
    """Number five. Auto repair. Hundreds of millions of vehicles are on American roads, and the average car is now more than twelve years old.
Older cars need more repairs. And even as electric vehicles spread, they still need tires, brakes, suspension, alignment and collision
repair.""",
    """The trade is changing, with more electronics and software, so successful shops will need to keep training. But the core business of
fixing vehicles near where people live isn't going anywhere. Independent shops that earn trust often keep customers for decades.""",
    "Mechanic working under car", "OLDER CARS, MORE REPAIRS",
    "Electric car in garage", "EVS STILL NEED SERVICE")

short("This boring business has survived every recession, and it'll likely survive the next one.")
biz(6, "Funeral services", "the most certain demand there is",
    """Number six. Funeral homes and related services. It's uncomfortable to talk about, but demand for funeral services is about as certain
as demand gets. And as the large baby boom generation ages, the number of deaths in America is projected to rise in the coming decades.""",
    """The industry is changing, with more cremations and more personalized services, but families still want help, dignity and guidance in
their hardest moments. Many funeral homes are family owned and have served the same community for generations. Licensing and trust create
high barriers to entry.""",
    "Flowers at memorial", "CERTAIN DEMAND",
    "Small town church", "TRUST ACROSS GENERATIONS")

biz(7, "Senior care", "America is getting older fast",
    """Number seven. Senior care. The Census Bureau projects that the number of Americans aged sixty five and older will keep growing in the
coming decades. Older adults need help with daily tasks, transportation, medication and companionship, and many want to stay in their homes
as long as possible.""",
    """Home care agencies, adult day centers and assisted living facilities all serve this growing need. It's a business built on people and
trust, with real responsibility and regulation. Done well, it's both meaningful and in strong demand.""",
    "Caregiver helping elderly person", "AN AGING NATION",
    "Elderly couple at home", "AGING IN PLACE")

biz(8, "Dentistry", "teeth don't fix themselves",
    """Number eight. Dental practices. People will still have teeth in 2040, and those teeth will still get cavities, crack and need cleaning.
Dentistry requires hands, tools and a person in the chair. Technology will improve the tools, but it won't replace the visit.""",
    """Becoming a dentist requires years of school and debt, but practice ownership has historically been a strong path to wealth. Many
practices are being bought by larger groups, yet independent practices with loyal patients remain valuable. Related businesses like dental
labs and specialized offices also benefit.""",
    "Dentist with patient", "TEETH STILL NEED HANDS",
    "Dental office", "PRACTICE OWNERSHIP")

biz(9, "Veterinary care and pet services", "people treat pets like family",
    """Number nine. Veterinary clinics and pet services. Americans spend enormous amounts on their pets, and that spending has grown for years.
Pets need checkups, vaccines, surgery, grooming, boarding and training, all of which happen in person.""",
    """Vet clinics require licensed veterinarians, but related businesses like grooming, boarding, dog training and pet sitting are easier to
start. Pet owners tend to be loyal and willing to pay for quality care, because to them, a pet is family.""",
    "Veterinarian with dog", "PETS ARE FAMILY",
    "Dog grooming", "GROOMING AND BOARDING")

biz(10, "Childcare", "parents will always need help",
    """Number ten. Childcare. As long as parents work, they need safe, reliable care for their children. In many parts of the country, there
aren't enough childcare spots, and waiting lists are common.""",
    """Childcare is heavily regulated and margins can be thin, because staffing is the biggest cost. But demand is strong, and parents are
loyal to providers they trust. Before and after school programs, summer camps and tutoring add related opportunities.""",
    "Children playing in daycare", "PARENTS NEED HELP",
    "Kids at summer camp", "RELATED PROGRAMS")

pr("""Quick pause. If you're getting value from this, subscribe to the channel. Every week, Ryan breaks down how money really works, from
saving your first ten thousand dollars to buying a business that lasts. Now, number eleven.""")

biz(11, "Landscaping and tree care", "grass grows and trees fall",
    """Number eleven. Landscaping and tree care. Grass keeps growing, trees keep falling, and businesses and homeowners keep wanting their
properties to look good. Commercial properties often need weekly service by contract.""",
    """Landscaping is easy to start but hard to scale well. The money often comes from commercial contracts, irrigation, hardscaping and tree
work, which requires specialized skill and insurance. Robotic mowers may change some tasks, but trimming, planting, removal and design
still need people.""",
    "Landscaper mowing lawn", "GRASS KEEPS GROWING",
    "Tree removal crew", "TREE WORK PAYS")

biz(12, "Pest control", "bugs don't read the news",
    """Number twelve. Pest control. Termites, ants, rodents and bed bugs have been around far longer than humans, and they're not leaving.
Warmer climates in some areas may even expand pest seasons.""",
    """Pest control companies earn recurring revenue through quarterly service plans, which makes them stable and valuable. Licensing and
safety training create some barriers to entry. Larger companies regularly buy local operators, which gives owners a possible exit.""",
    "Exterminator spraying", "BUGS AREN'T LEAVING",
    "Calendar on desk", "RECURRING PLANS")

short("Robots can vacuum a floor. They still can't do this job.")
biz(13, "Cleaning services", "dirt is permanent",
    """Number thirteen. Cleaning services. Offices, homes, hospitals, schools and vacation rentals all need cleaning, constantly. Robots can
vacuum floors, but they can't yet clean bathrooms, kitchens and offices the way a trained crew can.""",
    """Commercial cleaning companies work on recurring contracts, which helps stability. Specialized cleaning, like medical facilities or
post construction cleanup, can earn higher prices. The challenge is managing people well, but the demand itself is permanent.""",
    "Office cleaning at night", "DIRT IS PERMANENT",
    "Cleaning supplies", "RECURRING CONTRACTS")

biz(14, "Accounting and tax preparation", "taxes are forever",
    """Number fourteen. Accounting and tax preparation. Software can do simple returns, and AI is getting better at numbers. But small
businesses, landlords, families with complicated situations and people facing audits still want a trusted human who understands their
situation and takes responsibility for the advice.""",
    """The tax code changes constantly, which keeps demand for expertise strong. Firms that move from basic tax preparation toward advisory
work, like planning, bookkeeping and helping owners make decisions, may be best positioned. Recurring monthly clients make the business
more stable.""",
    "Tax forms on desk", "TAXES ARE FOREVER",
    "Accountant meeting client", "ADVICE OVER DATA ENTRY")

biz(15, "Insurance agencies", "risk never disappears",
    """Number fifteen. Independent insurance agencies. People and businesses will always need to protect homes, cars, health, lives and
companies. Online quotes have changed the industry, but complex situations still benefit from an advisor who shops multiple companies and
helps when there's a claim.""",
    """Agencies earn commissions that often renew every year as long as the customer stays, creating recurring revenue. That's why established
books of business can be valuable to buyers. Licensing is required, and relationships drive growth.""",
    "Insurance documents", "RISK NEVER DISAPPEARS",
    "Handshake with customer", "RENEWING COMMISSIONS")

biz(16, "Storage", "people always have more stuff than space",
    """Number sixteen. Self storage. Life changes like moving, divorce, downsizing and inheritance push belongings into storage. The need for
extra space has grown for decades, and smaller homes and apartments in cities may keep it going.""",
    """Storage facilities need capital, but they can run with small staffs and steady occupancy. Some markets have overbuilt, so location and
pricing matter. It's closer to real estate than to a typical small business, and it's a classic boring wealth builder for investors.""",
    "Storage units", "MORE STUFF THAN SPACE",
    "Real estate building", "BORING REAL ESTATE")

biz(17, "Barbershops and salons", "you can't download a haircut",
    """Number seventeen. Barbershops and hair salons. Hair keeps growing, and people want to look good. A haircut can't be shipped, streamed or
automated in any practical way. That's why barbers have been around for thousands of years.""",
    """Shops can earn money from services, product sales and renting chairs to independent stylists. Loyal clients who come back every few
weeks create predictable revenue. The best shops also become community gathering places, which makes them hard to replace.""",
    "Barber cutting hair", "YOU CAN'T DOWNLOAD A HAIRCUT",
    "Barbershop interior", "COMMUNITY PLACES")

biz(18, "Locksmiths and security", "people will always get locked out",
    """Number eighteen. Locksmiths and security installation. Smart locks and cameras are changing the business, but someone still needs to
install, repair and secure them. And people will always lock themselves out of homes and cars.""",
    """Locksmith work includes emergencies, rekeying, commercial access systems and safes. Adding smart lock and camera installation helps
locksmiths grow with technology instead of being replaced by it. Trust is crucial, which favors established local operators.""",
    "Locksmith working on door", "LOCKED OUT FOREVER",
    "Smart lock on door", "GROW WITH THE TECH")

biz(19, "Moving companies", "Americans move millions of times a year",
    """Number nineteen. Moving companies. Americans move millions of times every year for jobs, families, retirement and new homes. Every move
involves heavy things that need to go from one place to another, carefully.""",
    """Moving businesses can start with one truck and a small crew, then grow into packing, storage and long distance moves. Reviews matter
enormously, because customers fear damaged belongings and scams. Companies known for honesty and care stand out quickly.""",
    "Moving truck", "MILLIONS OF MOVES",
    "Workers lifting boxes", "HONESTY STANDS OUT")

biz(20, "Waste management and recycling", "trash is forever",
    """And number twenty. Waste management. Every person and business produces trash, and someone has to collect, sort, haul and dispose of
it. Large national companies dominate city contracts, but there's still room for local haulers, dumpster rentals, recycling and specialty
waste services.""",
    """Waste businesses require trucks, permits and disposal arrangements, which create high barriers to entry. Customers often sign long
contracts. It's not glamorous, but it's about as durable as a business gets.""",
    "Garbage truck on street", "TRASH IS FOREVER",
    "Recycling center", "LONG CONTRACTS")

# ---------------- At risk ----------------
ch("Five businesses that may look very different by 2040")
pr("""To make the point clearer, let's look at the other side. Here are five businesses that may look very different by 2040. Not
necessarily gone, but changed enough that owners should be careful.""")
sc("""One. Basic data entry and simple bookkeeping. Software and AI can already categorize transactions and fill in forms. Firms that only do
data entry may struggle, while those that offer advice may thrive. Two. Simple translation and transcription. Automated tools have improved
quickly, though specialized legal and medical work still needs experts.""",
   "Laptop with business software", "DATA ENTRY AND TRANSLATION")
sc("""Three. Traditional travel agencies for simple trips. Booking apps handle most basic travel, though complex trips and luxury travel still
use advisors. Four. Print shops focused on basic printing. Demand for paper has fallen for years, though specialized printing, signs and
packaging remain. Five. Video rental and similar media stores. That one already happened, and it's a reminder that any business built on a
physical product that becomes digital is at risk.""",
   "Empty store", "TRAVEL, PRINT, MEDIA")
sc("""Notice the pattern. The businesses at risk are those where the product can become digital, the customer doesn't need to be nearby, and
the work is repetitive. The businesses on our list are the opposite: physical, local and personal. That's the difference that matters.""",
   "Person thinking with notebook", "THE PATTERN")

# ---------------- Example owners ----------------
ch("Two owners, twenty years")
sc("""Imagine two people in 2020 with the same savings. One opens a trendy business riding a popular fad. It booms for two years, then
customers move on, and by 2025 it closes. The other buys a small HVAC company from a retiring owner. Growth is slow, but every summer and
every winter, the phones ring.""",
   "Two paths diverging", "TWO OWNERS")
sc("""By 2040, the HVAC owner has twenty years of profits, a team of technicians, hundreds of maintenance agreements, and a business that
could sell for several times its yearly profit. The trendy owner had a great two years and then had to start over. Same starting point,
very different endings. Durability made the difference.""",
   "Technician servicing furnace", "TWENTY YEARS LATER")

# ---------------- Mistakes ----------------
ch("Six mistakes that kill durable businesses")
pr("""Even a business with permanent demand can fail. Here are six mistakes that kill durable businesses.""")
sc("""Mistake one. Competing only on price. In trusted local services, the cheapest company often attracts the worst customers and can't
afford good workers. Mistake two. Ignoring reviews and reputation. One bad year of service can undo a decade of trust, especially online.""",
   "Handshake with customer", "MISTAKES 1 AND 2")
sc("""Mistake three. Refusing to adapt. A locksmith who ignores smart locks, or an auto shop that refuses to learn electric vehicles, can lose
customers even in a durable industry. Mistake four. The owner doing everything. If the business can't run for two weeks without the owner,
it's fragile, and it's worth much less when it's time to sell.""",
   "Mechanic working under car", "MISTAKES 3 AND 4")
sc("""Mistake five. Too much debt. Borrowing heavily for trucks, buildings or expansion can turn a slow season into a crisis. Mistake six.
No succession plan. Many good businesses simply close when the owner retires, because nobody was trained to take over and no buyer was
found in time. Planning the exit years ahead protects everything you built.""",
   "Older business owner", "MISTAKES 5 AND 6")

# ---------------- Angle 1 ----------------
ch("Angle 1: The numbers")
pr("""Now, three angles. First, the numbers. Why does durability matter so much for money?""")
card("""A business that earns one hundred thousand dollars a year for twenty years is worth far more than one that earns two hundred thousand
dollars for three years and then disappears.""",
     {"type": "compare", "left": {"label": "Durable", "big": "$2M", "sub": "$100K a year for 20 years"},
      "right": {"label": "Trendy", "big": "$600K", "sub": "$200K a year for 3 years"}}, "DURABILITY WINS")
sc("""Look at this simple comparison. A trendy business earning two hundred thousand dollars a year for three years produces six hundred
thousand dollars, then fades. A durable business earning one hundred thousand dollars a year for twenty years produces two million dollars.
Half the yearly profit, more than three times the total. Durability is a multiplier.""",
   "Calculator and coins", "DURABILITY IS A MULTIPLIER")
sc("""Durability also affects what a business is worth when you sell it. Buyers pay more for businesses they believe will keep earning for
many years. A business with steady demand, recurring customers and a long history usually sells for a higher multiple of its profit than one
that depends on a fad.""",
   "Business meeting handshake", "BUYERS PAY FOR DURABILITY")
sc("""And durable businesses are easier to finance. Banks and SBA lenders look at history and stability when deciding whether to lend. A
plumbing company with ten years of steady records is far easier to finance than a brand new trendy concept. Easier financing means more
people can buy these businesses, which supports their value.""",
   "Bank building", "EASIER TO FINANCE")
sc("""Finally, durability lets compounding work. When a business keeps producing cash for decades, the owner can invest that cash year after
year. Steady profits invested steadily are how many quiet millionaires are made: not one big win, but many good years in a row.""",
   "Stock market chart on screen", "LET COMPOUNDING WORK")

# ---------------- Example P&L ----------------
ch("Inside a durable business: an example")
pr("""Let's open the books of a made up but realistic durable business, so you can see where the money comes from.""")
card("""Example: a small HVAC company. Revenue one million dollars. Owner's earnings about one hundred fifty thousand dollars.""",
     {"type": "stat", "label": "example HVAC company", "big": "$1M → $150K", "sub": "illustration: revenue to owner earnings"}, "EXAMPLE BOOKS")
sc("""Say this HVAC company brings in one million dollars a year. Equipment and parts cost around four hundred thousand. Technician wages
and benefits take about three hundred thousand. Trucks, fuel, insurance, rent, software and marketing take another one hundred fifty
thousand. That leaves around one hundred fifty thousand dollars for the owner, before taxes. These are illustrative numbers, but the shape is
common.""",
   "Calculator and pen on financial papers", "WHERE THE MONEY GOES")
sc("""Now look at what makes it durable. Say six hundred customers pay about two hundred dollars a year for maintenance agreements. That's
one hundred twenty thousand dollars of recurring revenue before a single emergency call. Those customers also call this company first when
something breaks, which feeds the repair and replacement business. The agreements are the foundation everything else is built on.""",
   "Technician servicing furnace", "THE RECURRING FOUNDATION")
sc("""And when the owner eventually sells, a buyer looks at that steady history, the agreements and the team. A business like this might sell
for a few times its yearly owner earnings, depending on the market and how dependent it is on the owner. That sale price is the reward for
twenty years of boring consistency.""",
   "Business meeting handshake", "THE PAYOFF AT SALE")

# ---------------- Angle 2 ----------------
short("Why smart people keep chasing trends that die, while boring businesses quietly last for decades.")
ch("Angle 2: The psychology")
pr("""Second angle. The psychology. If durable businesses are so good, why do so many people chase trends instead?""")
sc("""The first reason is novelty bias. New things grab our attention. A new app or a hot new food trend feels exciting, while a plumbing
company feels like background noise. But what's exciting to talk about and what makes money for decades are often very different things.""",
   "Person scrolling smartphone", "NOVELTY BIAS")
sc("""The second reason is fear of missing out. When people see others getting rich quickly from a trend, they want in, often right before
the trend fades. Durable businesses never trigger that feeling, because they grow slowly and steadily. Nobody brags at a party about their
pest control company's renewal rate.""",
   "Crowd of people", "FEAR OF MISSING OUT")
sc("""The third reason is fear of technology. Many people assume every business will be replaced by AI or robots, so they think nothing
is safe. But the businesses on this list involve physical work, local presence and personal trust, which are the hardest things for
technology to replace. Smart owners use technology to run better, not as a reason to give up.""",
   "Robot and human hands", "FEAR OF TECHNOLOGY")
sc("""The fourth reason is status. Telling people you run a startup sounds more impressive than saying you own a pest control company.
But status doesn't pay the mortgage. Many of the wealthiest people in small towns own exactly the kind of businesses on this list, and
most of them stopped caring long ago what the business sounds like.""",
   "People at party talking", "STATUS")
sc("""The fifth reason is impatience. Durable businesses reward people who think in decades. Trendy businesses promise results in months.
Most people choose months, which leaves the decades to those patient enough to wait for them.""",
   "Hourglass", "IMPATIENCE")
pr("""The takeaway. Boring and durable usually beats exciting and fragile, especially when you measure over twenty years instead of two.""")

# ---------------- Angle 3 ----------------
short("Use these five questions to know if a business will still exist in 2040.")
ch("Angle 3: The playbook")
pr("""Third angle. The playbook. How do you pick a durable business and get started?""")
card("""The 2040 test. Physical? Local? Needed in recessions? Built on trust? Hard to enter?""",
     {"type": "list", "n": 5, "title": "the 2040 test", "sub": "five questions for durability"}, "THE 2040 TEST")
sc("""Ask five questions about any business. Does it require physical work in a specific place? Does it serve local customers who can't
easily buy from far away? Do people need it even in a recession? Does it depend on trust and relationships? And are there barriers like
licenses, equipment or skills that keep competitors out? The more yes answers, the more durable the business.""",
   "Notebook with financial notes", "FIVE QUESTIONS")
sc("""Next, choose your path. You can learn a trade and start your own company, which takes years but can be powerful. You can buy an
existing business from a retiring owner, often with SBA financing. Or you can invest in businesses as a silent partner, though that requires
trusting the operator.""",
   "Person standing at crossroads", "CHOOSE YOUR PATH")
sc("""Whichever path you choose, start with a test. Work a season in the industry, shadow an owner, or run the business part time before
going all in. A few months of real experience will tell you more about whether you can do this for twenty years than any amount of research.""",
   "Workers on job site", "TEST BEFORE YOU COMMIT")
sc("""Then, use technology as a tool. Online booking, digital marketing, scheduling software and automated invoicing can make a traditional
business far more efficient. The owners who thrive in 2040 will run timeless businesses with modern tools.""",
   "Laptop with business software", "TIMELESS BUSINESS, MODERN TOOLS")
sc("""Here are a few examples. A plumber who offers online booking and text updates wins customers who hate waiting by the phone. An HVAC
company that uses software to remind customers about tune ups sells more maintenance agreements. A barbershop with an app for appointments
fills empty chairs. A cleaning company that uses route planning saves hours of driving every week. The business stays timeless. The tools
make it faster, friendlier and more profitable.""",
   "Smartphone booking app", "EXAMPLES")
sc("""The same goes for AI. Owners can use it to answer common questions, write estimates faster, plan schedules and understand their
numbers. Used well, it frees up time for the work only people can do: showing up, fixing the problem and earning the customer's trust.""",
   "Robot and human hands", "AI AS AN ASSISTANT")
sc("""And protect your foundation while you build. Keep an emergency fund, keep investing for retirement, and don't bet everything on one
business. Even durable businesses face bad years, bad partners and bad luck. A strong personal financial base lets you survive them.""",
   "Piggy bank coins", "PROTECT YOUR FOUNDATION")

# ---------------- Questions ----------------
ch("Questions people ask")
sc("""Question one. Won't AI eventually replace these too? AI will change how they're run, from scheduling to diagnosis to marketing. But
fixing a pipe, cutting hair or caring for an elderly parent requires physical presence and human trust. Those are likely to be among the
last things to be fully automated. Question two. Do I need a license? Many of these do, especially plumbing, electrical, HVAC, insurance,
pest control and childcare. Check your state's requirements early.""",
   "Robot and human hands", "AI? LICENSES?")
sc("""Question three. What's the best one to start with little money? Cleaning, landscaping, pet services and moving often have lower
startup costs. Question four. What about buying instead of starting? Many owners of durable businesses are nearing retirement, which may
create buying opportunities. Always review several years of financial records with an accountant before buying.""",
   "Calculator and coins", "LITTLE MONEY? BUYING?")
sc("""Question five. Is it too late to learn a trade if I'm thirty or forty? No. Many people switch into trades later in life, and
apprenticeships often pay while you learn. Maturity, reliability and customer skills can make older apprentices valuable. Question six.
Should I franchise? Franchises in areas like senior care, cleaning and pest control offer training and brand recognition in exchange for fees
and royalties. Compare the total cost carefully against starting independently.""",
   "Older plumber with apprentice", "TOO LATE? FRANCHISE?")
sc("""Question seven. How do I know my local market isn't already saturated? Search for providers near you, count them, read their reviews,
and notice how long it takes to get an appointment. Long wait times and mediocre reviews usually mean room for a better competitor. Question
eight. What's the biggest risk in durable businesses? Usually not demand, but people: finding and keeping good workers. Owners who treat
employees well have a real advantage.""",
   "Phone ringing on desk", "SATURATED? BIGGEST RISK?")

# ---------------- Recap ----------------
ch("Recap")
sc("""Let's recap the twenty. Plumbing. Electrical. HVAC. Roofing. Auto repair. Funeral services. Senior care. Dentistry. Veterinary and pet
services. Childcare. Landscaping. Pest control. Cleaning. Accounting. Insurance. Storage. Barbershops. Locksmiths. Moving. And waste
management.""",
   "Notebook with financial notes", "THE 20")
sc("""And the lesson behind them. Physical, local, needed and trusted businesses tend to outlast every trend. Durability multiplies profits,
raises business value, makes financing easier and gives compounding time to work.""",
   "Calculator and pen on financial papers", "THE LESSON")
sc("""Think about your own town in 2040. The phones will be smarter, the cars may drive themselves, and AI will be everywhere. But somewhere a
pipe will burst at two in the morning, a dog will need surgery, a family will need a funeral, and an older couple will need help staying in
their home. The people who own the businesses that answer those calls will still be earning, year after year.""",
   "Small town main street", "YOUR TOWN IN 2040")
sc("""You don't need to predict the next big trend to build wealth. You need to find a need that won't go away, serve it better than anyone
nearby, and keep doing it for a long time. That's not exciting advice. But it's the advice that has worked for generations of quiet
millionaires, and it will very likely still work in 2040.""",
   "Notebook with financial notes", "THE QUIET MILLIONAIRE ADVICE")

ch("What to do next")
pr("""Pick one business from this list that fits your skills and your town. This week, look up how many companies offer it nearby, read
their reviews, and call one owner to ask how they got started. I'm Ryan Rover. Build something that lasts, and I'll see you in the next
video.""")

save("video15", "20 Small Businesses That Will Still Exist in 2040", [
    "Bureau of Labor Statistics, Occupational Outlook Handbook (employment projections for trades and services)",
    "U.S. Census Bureau, population projections (growth of the 65 and older population)",
    "S&P Global Mobility, average age of light vehicles in the U.S. (over 12 years)",
    "U.S. Small Business Administration, 7(a) loan program (business acquisition loans)",
    "Durability comparison: simplified illustration ($100,000 a year for 20 years vs $200,000 a year for 3 years)",
], "built to last")
