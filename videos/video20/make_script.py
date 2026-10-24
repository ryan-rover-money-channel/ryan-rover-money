import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short


def edge(n, title, sub, a, b, c, q1, c1, q2, c2, q3, c3):
    ch(f"Advantage {n}. {title}")
    card(f"Advantage {n}. {title}. {sub}", {"type": "list", "n": n, "title": title, "sub": sub}, f"ADVANTAGE {n}")
    sc(a, q1, c1)
    sc(b, q2, c2)
    sc(c, q3, c3)
    t, q, cap = EX[n]
    sc("In real life. " + t, q, cap)


EX = {
    1: ("""Picture a journeyman electrician in a mid sized city earning around thirty five dollars an hour, which is roughly seventy thousand
dollars a year at full time hours, before overtime. Across town, a friend with a business degree works as a marketing coordinator earning
fifty five thousand. Both are doing fine, but the electrician is ahead, and started earning four years earlier.""", "Electrician working on panel", "TWO FRIENDS, TWO PAYCHECKS"),
    2: ("""A nineteen year old plumbing apprentice might earn around eighteen to twenty dollars an hour in the first year, depending on the
area, with raises each year. By the fourth year, the wage may be in the high twenties or more. Meanwhile, the apprentice's classroom
hours are often covered by the program.""", "Young worker on job site", "AN APPRENTICE'S PAYCHECK"),
    3: ("""Two twenty three year olds go apartment hunting. One is a new journeyman electrician with no loans. The other is a recent graduate
with a three hundred dollar monthly student loan payment. Same rent, same car, but one has three hundred extra dollars every month to save,
invest or use as a cushion.""", "Apartment building", "THE $300 DIFFERENCE"),
    4: ("""Picture the day a college senior walks across the stage at graduation. A friend who started an apprenticeship right after high school
is in the audience, already earning a solid wage, with a car paid off and a growing retirement account. Same age, very different starting
lines.""", "College graduation", "GRADUATION DAY"),
    5: ("""After a big storm, an electrician works long shifts restoring power and repairing damaged panels. In two weeks of storm work at
overtime rates, they might earn what would normally take a month or more. It's exhausting, but it's also how many tradespeople build their
savings or pay off a truck.""", "Storm damage on house", "STORM SEASON"),
    6: ("""A plumber helps a neighbor replace a water heater on a Saturday, properly permitted, and does such a good job that the neighbor tells
three friends. A year later, the plumber has a steady stream of weekend customers and starts thinking seriously about running a company.""", "Plumber working on pipes", "ONE SATURDAY JOB"),
}

# ---------------- Intro ----------------
ch("Intro")
short("The plumber who fixed your sink might have a higher net worth than the manager in the corner office.")
pr("""Hi, I'm Ryan Rover. For decades, the advice was simple. Go to college, get an office job, and you'll do better than the people who
work with their hands. For many people, that advice worked. But something quiet has been happening. Many plumbers and electricians now earn
more than the median worker, start earning years earlier, carry little or no student debt, and often end up owning businesses. Today, we're
going to look at twelve quiet advantages that help tradespeople out earn many office workers over a lifetime, and the honest downsides too.""")
card("""Plumbers and electricians versus office workers. Twelve quiet advantages, and the real tradeoffs.""",
     {"type": "stat", "label": "trades vs office", "big": "12", "sub": "quiet advantages over a lifetime"})
sc("""Let's be fair from the start. This isn't a video saying college is bad or office jobs are a mistake. Many office careers pay very well,
and many people are happier at a desk than in a crawl space. The point is that the old story, where hands on work automatically means less
money, is no longer true for a lot of people. And for some, the trades may be the faster path to wealth.""",
   "Person at office desk", "NOT TRADES VS COLLEGE, BUT CLEAR THINKING")
sc("""We'll use government data where we can, mainly from the Bureau of Labor Statistics. Where we use examples, they're simplified
illustrations to explain the ideas, not promises. Pay varies enormously by state, city, specialty, union membership and experience, and
your results will depend on your choices.""",
   "Calculator and pen on financial papers", "DATA AND ILLUSTRATIONS")
sc("""We'll go through the twelve advantages, then look at the whole picture from three angles. The numbers, meaning a lifetime comparison of
two people. The psychology, meaning why so many people overlook the trades. And the playbook, meaning how someone actually gets started, at
eighteen or at forty.""",
   "Notebook with financial notes", "12 ADVANTAGES, 3 ANGLES")
pr("""Let's start with the paycheck itself, because that's where most people's assumptions are furthest from reality.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Pay data comes from the Bureau of Labor Statistics Occupational Outlook Handbook and its occupational employment and wage statistics.
For May 2023, the Bureau reported median annual pay of about sixty one thousand five hundred dollars for both plumbers and electricians,
compared with a median of about forty eight thousand dollars for all occupations. Student debt information comes from the Federal Reserve and
the Department of Education. This video is education, not financial or career advice.""",
   "Government building", "SOURCES")

# ---------------- The 12 ----------------
edge(1, "Pay above the median", "the middle plumber out earns the middle worker",
    """Advantage one. Higher pay than many people expect. According to the Bureau of Labor Statistics, the median plumber and the median
electrician each earned about sixty one thousand five hundred dollars in May 2023. The median for all occupations was about forty eight
thousand. So the typical plumber or electrician earned roughly twenty eight percent more than the typical American worker.""",
    """And that's just the middle. Experienced tradespeople in high cost cities, in specialized fields, or in strong unions often earn far
more, with the top ten percent of electricians earning over one hundred thousand dollars a year according to the same data. Overtime can push
pay even higher, which we'll get to.""",
    """Compare that to many entry level office jobs, like administrative assistants, customer service representatives or junior marketing
roles, which often pay less than the median trade wage. Some office careers pay much more, of course, like engineering or finance. But the
idea that hands on work always pays less simply isn't supported by the data.""",
    "Plumber working on pipes", "ABOVE THE MEDIAN",
    "Electrician working on panel", "TOP EARNERS PASS $100K",
    "Person at office desk", "MANY OFFICE JOBS PAY LESS")

edge(2, "Paid to learn", "apprentices earn while they train",
    """Advantage two. You get paid to learn. Most plumbers and electricians train through apprenticeships, which typically last four to five
years and combine classroom instruction with paid work on real job sites. Instead of paying tuition, apprentices earn a wage that usually
rises as they gain skills.""",
    """Many apprentices start at a percentage of a journeyman's wage, often somewhere around forty to fifty percent, and get raises every year
or so as they progress. By the end of the apprenticeship, they're earning a full wage, with years of experience already on their resume.""",
    """Compare that with a typical four year college student, who often pays tuition, may work part time for low wages, and graduates with no
guarantee of a job in their field. The apprentice finishes training with income, experience and usually far less debt.""",
    "Older plumber with apprentice", "PAID TO LEARN",
    "Calendar on desk", "RAISES AS YOU PROGRESS",
    "College graduation", "THE COLLEGE COMPARISON")

edge(3, "Little or no student debt", "starting at zero instead of below zero",
    """Advantage three. Little or no student debt. Millions of Americans carry student loans, and many college graduates leave school owing
tens of thousands of dollars. Those loan payments can last ten years or more, eating into the money they could save and invest.""",
    """Apprentices often pay little for their training, since many programs are sponsored by unions or employers. Some trade school courses
cost money, but usually far less than a four year degree. That means the tradesperson often starts their career at zero, while the graduate
starts below zero.""",
    """That difference matters more than it seems. A three hundred dollar monthly loan payment for ten years is thirty six thousand dollars that
could have gone into investments instead. Invested at an illustrative seven percent a year, that money could grow into far more over a
career.""",
    "Person stressed with bills", "THE DEBT BURDEN",
    "Older plumber with apprentice", "LOW COST TRAINING",
    "Stock market chart on screen", "WHAT DEBT REALLY COSTS")

edge(4, "A four year head start", "earning while others are still in school",
    """Advantage four. A head start. An eighteen year old apprentice starts earning right away. An eighteen year old college student usually
starts their career around twenty two. That's four years of earnings, raises and experience for the tradesperson before the graduate even
begins.""",
    """Four years of earning means four years of potential saving and investing. Money invested at nineteen has decades longer to compound than
money invested at twenty six. Time is the most powerful ingredient in compound growth, and the tradesperson gets more of it.""",
    """It also means four years of experience. By twenty two, an apprentice may be close to becoming a licensed journeyman, while the graduate
is starting at the bottom of a new career ladder. Experience is what raises pay in both paths.""",
    "Young worker on job site", "FOUR YEARS EARLIER",
    "Stock market chart on screen", "MORE TIME TO COMPOUND",
    "Electrician working on panel", "EXPERIENCE EARLY")

short("Here's the overtime math that quietly pushes many electricians past six figures.")
edge(5, "Overtime and emergency pay", "when the lights go out, rates go up",
    """Advantage five. Overtime and emergency pay. Pipes burst at night, power fails during storms, and construction projects run on deadlines.
Many tradespeople earn time and a half or more for overtime, nights and weekends. Office workers on salary often work extra hours for no
extra pay.""",
    """Here's a simple illustration. An electrician earning forty dollars an hour works five extra hours a week at time and a half, sixty dollars
an hour. That's three hundred dollars a week, or about fifteen thousand dollars a year, on top of regular pay. Some tradespeople work far more
overtime during busy seasons.""",
    """Overtime isn't free, of course. It costs time with family and can wear you out. But it gives tradespeople a lever many salaried office
workers don't have: when they want to earn more, they can often choose to work more and get paid for it.""",
    "Electrician at night", "OVERTIME AND EMERGENCIES",
    "Calculator and coins", "THE OVERTIME MATH",
    "Family dinner", "THE TRADEOFF")

edge(6, "Side work", "skills you can sell on weekends",
    """Advantage six. Side work. A licensed electrician or plumber has skills that neighbors, friends and small businesses need constantly.
Many tradespeople earn extra income doing side jobs, where permitted by their employer and local rules, on weekends.""",
    """Side work can be a path to starting a business. Many owners began by building a list of loyal customers on the side, then left their job
once the side work could support them. It's a way to test the business before taking the leap.""",
    """Important caution. Licensing, permits, insurance and employer agreements apply to side work, and unlicensed or unpermitted work can lead
to fines and liability. Done properly, though, side work turns a skill into a second income stream.""",
    "Home repair tools", "SKILLS ON WEEKENDS",
    "Small business owner smiling", "A PATH TO OWNERSHIP",
    "Person reading documents", "DO IT LEGALLY")

pr("""Quick pause. If this is changing how you think about careers and money, subscribe to the channel. Every week, Ryan breaks down how real
people build wealth, with real numbers and no hype. Now, advantage seven.""")

EX.update({
    7: ("""A master plumber starts a company at thirty with one truck. By forty, she runs five trucks with technicians, a dispatcher and
hundreds of maintenance agreements. She works on the business, not under sinks, and earns far more than she did as an employee. At sixty, she
sells the company to a younger plumber who once worked for her.""", "Work truck", "ONE TRUCK TO FIVE"),
    8: ("""During years when many companies cut office staff or moved jobs offshore, local electricians kept getting calls, because houses
still needed rewiring and panels still failed. The work followed the buildings, and the buildings stayed where they were.""", "Electrician working on panel", "THE WORK STAYS LOCAL"),
    9: ("""In many areas, homeowners wait days or even weeks for a plumber or electrician to be available. That backlog is a signal: demand
exceeds supply. For a skilled worker, a backlog means pricing power and steady work.""", "Phone ringing on desk", "THE BACKLOG SIGNAL"),
    10: ("""A union electrician who works thirty years might retire with a pension paying a monthly income, plus savings in an annuity or
retirement account, plus Social Security. Three income streams, two of which many office workers don't have.""", "Elderly couple at home", "THREE INCOME STREAMS"),
    11: ("""Compare a downtown office worker who spends a few hundred dollars a month on parking, transit, lunches out and work clothes, with a
tradesperson who drives a company truck and packs lunch. Over thirty years, that difference alone could add up to tens of thousands of
dollars.""", "Packed lunch", "THE COMMUTE MATH"),
    12: ("""An electrician buys a dated house, rewires it, updates the kitchen with a plumber friend in exchange for electrical work on his
house, and sells or rents it a year later. Their skills turn a fixer upper into real equity, with labor costs far below what a typical buyer
would pay.""", "Kitchen remodel", "SWEAT EQUITY"),
})
edge(7, "A clear path to ownership", "from apprentice to boss",
    """Advantage seven. A clear path to owning a business. In many office careers, owning the company isn't really an option. In the trades,
it's common. A master plumber or licensed electrical contractor can start a company with a truck, tools, insurance and a phone.""",
    """Business owners in the trades can earn far more than employees, because they keep the profit from their crews' work. A contractor with
several crews might earn well into six figures, depending on the market and how well the business is run.""",
    """Ownership also creates an asset. A plumbing or electrical company with steady customers, maintenance agreements and trained employees
can be sold when the owner retires, often for a multiple of its yearly profit. That sale can be the biggest payday of a career.""",
    "Truck on rural road", "FROM APPRENTICE TO BOSS",
    "Team of workers", "PROFIT FROM CREWS",
    "Business meeting handshake", "A BUSINESS YOU CAN SELL")

edge(8, "Hard to outsource or automate", "you can't fix a pipe from overseas",
    """Advantage eight. Job security against outsourcing and automation. Many office tasks can be done remotely, outsourced to other countries,
or increasingly handled by AI. You can't fix a leak in Ohio from overseas, and robots that can rewire an old house aren't anywhere close.""",
    """That doesn't mean the trades are immune to change. Tools, codes and technology keep evolving. But the core of the work, solving physical
problems in unpredictable buildings, is among the hardest things to automate.""",
    """Meanwhile, the shift to electric vehicles, heat pumps, solar panels and home batteries means more electrical work, not less. The trades
may be one of the safest places to be as technology advances.""",
    "Robot and human hands", "HARD TO AUTOMATE",
    "Electrician working on panel", "TOOLS CHANGE, WORK REMAINS",
    "Electric car charging", "ELECTRIFICATION BOOM")

edge(9, "A retirement wave creating demand", "experienced workers are leaving",
    """Advantage nine. Demand from retirements. Many experienced plumbers and electricians are nearing retirement, and the trades have struggled
for years to attract enough young workers. The Bureau of Labor Statistics projects tens of thousands of openings for these trades each year,
many from workers who retire or leave.""",
    """When fewer people enter a field and many leave, the remaining workers often gain bargaining power. That can show up as higher wages,
better benefits and more opportunities to move up quickly.""",
    """For people who want to own a business, retirements also create a chance to buy existing companies from owners who have no successor. A
young electrician who earns an owner's trust might buy the company over time.""",
    "Older plumber with apprentice", "A RETIREMENT WAVE",
    "Help wanted sign", "BARGAINING POWER",
    "Business meeting handshake", "BUY FROM RETIREES")

edge(10, "Union benefits and pensions", "some trades still offer pensions",
    """Advantage ten. Union benefits. Many electricians and plumbers belong to unions, which negotiate wages, health insurance and, in many
cases, pensions. Pensions have become rare in office jobs, where most workers rely only on their own retirement accounts.""",
    """A pension that pays a monthly income for life can be worth hundreds of thousands of dollars in retirement value. Combined with personal
retirement savings, it can provide a very strong foundation.""",
    """Not every tradesperson is in a union, and union benefits vary widely by local and region. But for those who are, the benefits can be a
major hidden advantage over many office jobs.""",
    "Construction workers on site", "UNION BENEFITS",
    "Elderly couple at home", "A PENSION FOR LIFE",
    "Person reading documents", "BENEFITS VARY")

edge(11, "Lower cost of working", "no commute wardrobe, often a company truck",
    """Advantage eleven. Lower costs of working, in some cases. Many tradespeople drive company trucks, wear work clothes instead of expensive
office wardrobes, and don't pay for downtown parking or train passes. Small costs, but they add up over a career.""",
    """Some tradespeople also live in areas with lower housing costs, since the work exists everywhere, not only in expensive big cities where
many high paying office jobs are concentrated. Lower living costs can mean a higher savings rate on the same income.""",
    """Of course, tradespeople often buy their own tools, and those can be expensive. But overall, the cost of going to work can be lower than
for many office workers in big cities.""",
    "Work truck", "LOWER COSTS OF WORKING",
    "Small town main street", "WORK EXISTS EVERYWHERE",
    "Home repair tools", "TOOLS COST MONEY")

edge(12, "Skills that save money at home", "you never pay a plumber",
    """Advantage twelve. Skills that save money in your own life. A plumber never pays a plumber. An electrician wires their own garage. Over
a lifetime, the money saved on home repairs, renovations and maintenance can be significant.""",
    """Those skills also make real estate investing easier. Many tradespeople buy fixer upper homes or rental properties, do much of the work
themselves, and build equity faster than investors who must hire everything out.""",
    """It's a quiet advantage that doesn't show up in salary data, but it can add up to tens of thousands of dollars over a career, and even
more if it opens the door to real estate.""",
    "Home repair tools", "NEVER PAY A PLUMBER",
    "Real estate building", "FIXER UPPERS",
    "Piggy bank coins", "THE QUIET SAVINGS")

# ---------------- Downsides ----------------
ch("The honest downsides")
pr("""Now, to be fair, the trades have real downsides. Any honest comparison has to include them, so let's go through the biggest ones.""")
sc("""Downside one. It's physically demanding. Crawl spaces, attics, ladders, heat, cold and heavy lifting take a toll on the body over
decades. Injuries happen, and many tradespeople plan for less physical roles later in their careers, like estimating, inspection, teaching or
running a business.""",
   "Construction worker tired", "PHYSICALLY DEMANDING")
sc("""Downside two. Work can be cyclical. Construction slows during recessions, and some areas have seasonal swings. Service and repair work
tends to be steadier than new construction. Downside three. Early mornings, emergencies and travel can disrupt family life.""",
   "Construction site", "CYCLES AND SCHEDULES")
sc("""Downside four. Pay varies a lot. A plumber in a rural, low cost area may earn much less than one in a big city, though living costs differ
too. And downside five. Not everyone enjoys this kind of work. The money only matters if you can do the job for years without burning out.""",
   "Map with pins", "PAY VARIES")

# ---------------- Specialties ----------------
short("These are the trade specialties where the money gets really interesting.")
ch("Specialties where pay climbs higher")
pr("""Within the trades, some specialties tend to pay more. Here are a few worth knowing.""")
sc("""For electricians, industrial and commercial work, controls and automation, and specialties tied to growing industries like solar,
battery storage, EV charging and data centers can pay more than basic residential work. Linemen, who work on power lines, are often among the
highest paid, though the work is dangerous and demanding.""",
   "Power line workers", "ELECTRICAL SPECIALTIES")
sc("""For plumbers, specialties like medical gas systems in hospitals, commercial and industrial pipefitting, steamfitting and backflow
testing can raise pay. Service plumbers who handle emergencies and work on commission in some companies can also earn well above average.""",
   "Plumber working on pipes", "PLUMBING SPECIALTIES")
sc("""Specialties usually require extra training and certifications, but they often come with higher pay, more stable demand and less
competition. A tradesperson who adds one valuable certification every few years keeps raising their earning power.""",
   "Person reading documents", "KEEP ADDING CERTIFICATIONS")

# ---------------- Three paths ----------------
ch("Three tradespeople, three paths")
sc("""Let's imagine three electricians who finished their apprenticeships together. The first stays a union journeyman for his whole career,
works steady hours with occasional overtime, invests in his retirement plan and pension, and retires comfortably at sixty two. No drama, just
consistency.""",
   "Construction workers on site", "THE STEADY JOURNEYMAN")
sc("""The second moves into industrial controls, earns several certifications, and becomes a supervisor. Her pay climbs well above the
median, and she manages crews on large projects. She doesn't own a company, but her specialty makes her hard to replace.""",
   "Electrician with tablet", "THE SPECIALIST")
sc("""The third starts a small residential electrical company at thirty two. The first years are stressful, with long hours and uneven
income. But by forty five, he has eight employees, a steady stream of customers and a business worth a meaningful amount. He took the most
risk, and he has the highest potential reward.""",
   "Work truck", "THE OWNER")
sc("""Three different paths, all solid. That's one of the best things about the trades: you can choose stability, specialization or
ownership, and each can lead to a comfortable financial life if you manage your money well.""",
   "Two paths diverging", "CHOOSE YOUR PATH")

# ---------------- Money mistakes ----------------
ch("Money mistakes tradespeople make")
pr("""Earning well doesn't automatically mean building wealth. Here are common money mistakes in the trades, and how to avoid them.""")
sc("""Mistake one. The big truck payment. It's common to see young tradespeople with expensive new trucks and big monthly payments. A truck
you need for work is one thing. A luxury truck financed for seven years can drain money that could have been invested.""",
   "Pickup truck loaded", "THE BIG TRUCK PAYMENT")
sc("""Mistake two. Spending overtime as if it's permanent. Overtime comes and goes with busy seasons and economic cycles. Smart tradespeople
build their lifestyle on base pay and save or invest the overtime. Mistake three. Not planning for the body. Physical work gets harder with
age, so save aggressively in your twenties and thirties and plan for a less physical role later.""",
   "Calculator and coins", "OVERTIME AND THE BODY")
sc("""Mistake four. Ignoring retirement accounts. If your employer or union offers a retirement plan with matching contributions, take full
advantage. And if you're self employed, look into retirement accounts designed for business owners. Mistake five. No emergency fund, which
matters even more in work that can be seasonal or cyclical.""",
   "Piggy bank coins", "RETIREMENT AND EMERGENCIES")

# ---------------- Apprentice money plan ----------------
ch("A money plan for a new apprentice")
sc("""If you're starting an apprenticeship, here's a simple money plan. First, build a starter emergency fund of one thousand dollars, then
work toward three to six months of expenses. Second, contribute enough to any retirement plan to get the full employer or union match.""",
   "Piggy bank coins", "EMERGENCY FUND AND MATCH")
sc("""Third, avoid big debt early, especially a car or truck payment you don't need. Buy reliable and used if you can. Fourth, every time you
get a raise, save at least half of it. Your lifestyle grows a little, and your savings grow a lot.""",
   "Online banking smartphone app", "AVOID DEBT, SAVE RAISES")
sc("""Fifth, invest consistently in low cost index funds through a retirement account. Starting at nineteen or twenty gives compounding
decades to work. Follow this plan through a four year apprenticeship, and you could finish with a solid emergency fund, a growing retirement
account and no debt, before many of your friends even start their careers.""",
   "Stock market chart on screen", "INVEST EARLY")
sc("""Here's what that could look like in numbers. Say an apprentice invests three hundred dollars a month from age nineteen to twenty three,
about fourteen thousand dollars in total. Then they never add another dollar. At an illustrative seven percent a year, that money could grow to
more than two hundred thousand dollars by age sixty two. Four years of discipline during an apprenticeship can quietly fund a big piece of
retirement.""",
   "Calculator and coins", "FOUR YEARS OF DISCIPLINE")
sc("""And if they keep investing a modest amount for their whole career, the total could be far larger, especially with an employer match or a
pension on top. The trades provide the income and the head start. The money habits turn that head start into real wealth.""",
   "Piggy bank coins", "KEEP GOING")

# ---------------- Angle 1 ----------------
ch("Angle 1: The numbers")
pr("""Now, three angles. First, the numbers. Let's compare two people over a lifetime, using simplified illustrations.""")
card("""Two eighteen year olds. One apprentice, one college student. By twenty two, the apprentice has earned and saved while the student
has borrowed.""",
     {"type": "compare", "left": {"label": "Apprentice at 22", "big": "+$25K", "sub": "saved and invested"},
      "right": {"label": "Graduate at 22", "big": "−$30K", "sub": "student loans"}}, "TWO PATHS AT 22")
sc("""Meet two eighteen year olds. Alex becomes an electrical apprentice, earning a modest wage that rises each year. Sam goes to college and
graduates at twenty two with thirty thousand dollars in student loans. Over four years, Alex earns well over one hundred thousand dollars in
total and, living with family and saving carefully, invests twenty five thousand dollars.""",
   "Young worker on job site", "ALEX AND SAM")
sc("""At twenty two, Alex has about twenty five thousand dollars invested and a nearly finished license. Sam has a degree, a new job and
thirty thousand dollars of debt. That's a fifty five thousand dollar gap in net worth before Sam's career even begins.""",
   "Calculator and coins", "THE GAP AT 22")
sc("""Now let compounding work. If Alex's twenty five thousand dollars grows at an illustrative seven percent a year until age sixty two, it
could become around three hundred seventy thousand dollars, without adding another dollar. Meanwhile, Sam spends years paying off the loan
before investing seriously.""",
   "Stock market chart on screen", "COMPOUNDING THE HEAD START")
sc("""Of course, Sam's career might eventually pay more, especially in a high paying field. Many college graduates do catch up and pass
tradespeople over time. The point isn't that one path always wins. It's that the trades offer a head start that's easy to underestimate, and
if Alex later owns a business, the gap could grow much larger.""",
   "Two paths diverging", "IT DEPENDS ON THE CHOICES")
sc("""Now add ownership to Alex's story. Say at thirty five, Alex starts an electrical contracting company and grows it to earn, in our
illustration, around one hundred fifty thousand dollars a year in owner earnings by forty five. Twenty years later, Alex sells the company for
a few times its yearly profit. That sale alone could be worth more than many office workers save in a lifetime.""",
   "Business meeting handshake", "ADD OWNERSHIP")
sc("""And what about Sam? If Sam becomes an engineer, a nurse practitioner or a successful manager, Sam may earn more than Alex for much of
their career. Many college paths pay off very well. The real lesson is that both paths can build wealth, and the trades deserve to be
considered seriously, not dismissed as a fallback.""",
   "Person at office desk", "SAM CAN WIN TOO")
sc("""The biggest variable in both stories isn't the career. It's what each person does with the money. A plumber who spends everything ends
up with nothing, and so does a lawyer. A tradesperson who invests early and avoids debt can end up wealthier than many high earners who don't.""",
   "Calculator and coins", "WHAT YOU DO WITH THE MONEY")

# ---------------- Lessons for office workers ----------------
ch("What office workers can learn from the trades")
sc("""Even if you love your office job, the trades teach some valuable money lessons. Lesson one. Avoid debt for credentials when there's a
cheaper path to the same skills. Certifications, employer paid training and community colleges can sometimes deliver similar results for far
less money.""",
   "Person at office desk", "LESSON 1: CHEAPER CREDENTIALS")
sc("""Lesson two. Build skills that are hard to replace. The trades are protected because the work is physical and local. In office jobs,
the equivalent is judgment, relationships and expertise that AI and outsourcing struggle to copy. Lesson three. Look for a path to ownership.
Many office workers can eventually start consulting practices or buy small businesses in their field.""",
   "Handshake with customer", "LESSONS 2 AND 3")
sc("""And lesson four. Get paid for extra effort. Tradespeople earn overtime. Office workers can look for bonuses, commissions, side
consulting or roles where extra results translate into extra pay. Effort that isn't rewarded is a donation to your employer.""",
   "Calculator and coins", "LESSON 4: GET PAID FOR EFFORT")

# ---------------- Angle 2 ----------------
short("Why parents push kids away from the trades, even when the money says otherwise.")
ch("Angle 2: The psychology")
pr("""Second angle. The psychology. Why do so many people overlook the trades?""")
sc("""The first reason is status. For decades, schools and parents pushed college as the respectable path and treated the trades as a backup
plan. That stigma is fading, but slowly. Many people still feel a blue collar job is a step down, even when it pays more.""",
   "College graduation", "THE STATUS STORY")
sc("""The second reason is invisibility. Office success is visible: titles, offices, LinkedIn posts. A plumber with a growing business and a
paid off house doesn't announce it. The wealth in the trades is quiet, so people don't see it.""",
   "Plumber working on pipes", "QUIET WEALTH")
sc("""The third reason is outdated information. Many parents' views of the trades are based on how things were decades ago. Today's trades
involve technology, problem solving and, in many cases, strong pay and ownership opportunities.""",
   "Electrician with tablet", "OUTDATED VIEWS")
sc("""The fourth reason is the comfort of a clear script. College is a familiar path: apply, attend, graduate. The trades can feel less
clear, with apprenticeship applications, union locals and licensing steps that many families have never navigated. Unfamiliar feels risky,
even when it isn't.""",
   "Person standing at crossroads", "THE FAMILIAR SCRIPT")
sc("""And the fifth reason is underestimating the brain work. People picture the trades as purely physical. In reality, diagnosing an
electrical fault or designing a plumbing system requires knowledge of codes, math, physics and problem solving. Many tradespeople are some of
the sharpest problem solvers you'll ever meet.""",
   "Electrician with tablet", "IT'S BRAIN WORK TOO")
pr("""The takeaway. The trades aren't a backup plan. For many people, they're a front door to solid income, little debt and business ownership.""")

# ---------------- Angle 3 ----------------
short("Here's exactly how to get into the trades, whether you're eighteen or forty.")
ch("Angle 3: The playbook")
pr("""Third angle. The playbook. How does someone actually get started?""")
sc("""Step one. Explore. Talk to plumbers and electricians, visit a job site if you can, and try some basic projects to see if you enjoy the
work. Step two. Look for apprenticeships through union locals, contractor associations and employers. Many list openings online and accept
applications at specific times of year.""",
   "Person reading documents", "STEPS 1 AND 2")
sc("""Step three. Consider a pre apprenticeship or trade school program if you need basic skills first. Step four. Complete the
apprenticeship and earn your journeyman license. Step five. Keep learning: specialties like solar, EV chargers, controls or medical gas
can raise your value.""",
   "Older plumber with apprentice", "STEPS 3 TO 5")
sc("""Step six. Manage your money from day one. Save and invest part of every paycheck, especially during the apprenticeship when habits form.
Step seven. If you want ownership, learn the business side: estimating, sales, bookkeeping and managing people. Many owners start with side
work or buy a company from a retiring owner.""",
   "Piggy bank coins", "STEPS 6 AND 7")
sc("""And if you're older, it's not too late. Many people switch into the trades in their thirties or forties. Maturity and reliability are
valued, and apprenticeships pay while you learn. The physical demands are real, so consider your health, but don't assume the door is closed.""",
   "Older worker on job site", "IT'S NOT TOO LATE")
sc("""How do you choose between plumbing and electrical? Electrical work tends to involve more problem solving with circuits, codes and
technology, and less mess. Plumbing involves water, drains and gas, can be messier, and often has a big emergency service component. Both
pay similarly at the median. Try a day shadowing each, and choose the one you can imagine doing for decades.""",
   "Electrician working on panel", "PLUMBING OR ELECTRICAL?")
sc("""And don't forget related trades with similar advantages: HVAC technicians, elevator installers, welders, pipefitters and lineworkers.
Some of these, like elevator installation, have even higher median pay according to the Bureau of Labor Statistics, though openings can be
more limited.""",
   "Construction workers on site", "RELATED TRADES")

# ---------------- Questions ----------------
ch("Questions people ask")
sc("""Question one. Do plumbers or electricians earn more? Median pay is very similar nationally, but it varies by region, specialty and union
status. Question two. How long does it take to get licensed? Typically four to five years of apprenticeship, then a licensing exam, though
requirements vary by state.""",
   "Plumber working on pipes", "WHO EARNS MORE? HOW LONG?")
sc("""Question three. Is college a waste of money? No. Many careers require it and pay well. The point is to compare paths honestly, including
cost, debt and time. Question four. Can women succeed in the trades? Absolutely. Women are a growing part of the trades, and many programs
actively recruit them.""",
   "College graduation", "COLLEGE? WOMEN IN TRADES?")
sc("""Question five. What about the physical toll as I age? Many tradespeople move into estimating, project management, inspection,
teaching or business ownership in their forties and fifties. Planning for that shift, and saving aggressively early, makes the transition
easier. Question six. Do I need to be good at math? Basic math helps, especially for electricians, but apprenticeships teach what you need.""",
   "Older plumber with apprentice", "AGING? MATH?")
sc("""Question seven. Can I start a trade business without being a master? Most states require a master or contractor license to run a
plumbing or electrical company, or to employ someone who holds one. Check your state's rules early, because licensing determines when
ownership becomes possible.""",
   "Person reading documents", "LICENSE TO OWN")

# ---------------- Recap ----------------
ch("Recap")
sc("""Let's recap the twelve advantages. Pay above the median. Paid to learn. Little or no student debt. A four year head start. Overtime and
emergency pay. Side work. A clear path to ownership. Hard to automate or outsource. Demand from retirements. Union benefits. Lower costs of
working. And skills that save money at home.""",
   "Notebook with financial notes", "THE 12 ADVANTAGES")
sc("""And the honest tradeoffs: physical demands, cycles, schedules and variation in pay. The trades aren't for everyone, but for the right
person, they can be one of the most reliable paths to wealth in America.""",
   "Construction workers on site", "THE TRADEOFFS")
sc("""So next time you see a plumber's van or an electrician's truck in your neighborhood, remember what might be behind it. Maybe a person
who started earning at eighteen, never had student loans, invested early, and is quietly building a business and a net worth that would
surprise most people driving past. Quiet wealth is still wealth, and in many ways, it's the most durable kind.""",
   "Work truck", "QUIET WEALTH")

ch("What to do next")
pr("""If you or someone you know is choosing a path, share this video with them. And this week, look up the apprenticeship programs near you,
just to see what's possible. Many programs hold information sessions, and some accept applications only once or twice a year, so
knowing the dates early can save you months. And if you're already in the trades, tell me in the comments what you wish someone had told you
about money when you started. Your answer could help someone who's just beginning. I'm Ryan Rover. Respect the trades, build your wealth, and I'll see you in the next video.""")

save("video20", "How Plumbers and Electricians Quietly Out-Earn Office Workers", [
    "Bureau of Labor Statistics, Occupational Outlook Handbook: plumbers, pipefitters and steamfitters; electricians (median pay May 2023 about $61,550 and $61,590; job outlook)",
    "Bureau of Labor Statistics, Occupational Employment and Wage Statistics, May 2023 (median for all occupations about $48,060; top 10% of electricians above $100,000)",
    "Federal Reserve, Economic Well-Being of U.S. Households (student loans)",
    "Lifetime comparison: simplified illustration ($25,000 invested by age 22 at an illustrative 7% a year; $30,000 student loan)",
], "trades vs office")
