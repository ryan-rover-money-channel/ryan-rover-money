import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short


def decade(title, card_text, spec, typical, matters, behind, move, q1, c1, q2, c2, q3, c3, q4, c4):
    ch(title)
    card(card_text, spec, title.upper())
    sc(typical, q1, c1)
    sc(matters, q2, c2)
    sc(behind, q3, c3)
    sc(move, q4, c4)

# ---------------- Intro ----------------
ch("Intro")
short("Here's what your net worth should be at your age, according to the Federal Reserve.")
pr("""Hi, I'm Ryan Rover. What should your net worth be at your age? It's one of the most searched money questions
on the internet, and most of the answers you'll find are either scary or useless. So today, real numbers from the
Federal Reserve, decade by decade. And more importantly, what to do if you're behind. Because if you are, you're
far from alone.""")
card("""Net worth is simple. Everything you own, minus everything you owe. Savings, investments, retirement accounts,
the equity in your home, minus credit cards, car loans, student loans and your mortgage.""",
     {"type": "stat", "label": "net worth", "big": "OWN − OWE", "sub": "the number that tells the truth"})
sc("""Why does this one number matter so much? Because income can fool you. Plenty of people earn a lot and keep very
little. Net worth shows what you've actually kept. It's the scoreboard for every money decision you've ever made,
and the good news is that it can change faster than most people think, once you start paying attention to it.""",
   "Spreadsheet on laptop", "THE SCOREBOARD")
sc("""We'll look at it from three angles. First, the numbers: what typical Americans actually have at each age, and the
rules of thumb people use. Then the psychology: why comparing yourself can help or hurt. And finally the playbook:
exactly how to catch up, whatever your age. Grab your own number if you know it, or a rough guess, and let's see where
you stand.""",
   "Calculator with financial charts", "NUMBERS, PSYCHOLOGY, PLAYBOOK")
pr("""And stay until the end, because the catch up playbook in the last part of this video works at any age, whether you're
twenty five or sixty five. First, where the numbers come from, because there's a lot of bad data out there.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""The net worth figures in this video come from the Federal Reserve's Survey of Consumer Finances. It's the most
detailed survey of American household wealth, run every three years, and the latest full results cover twenty twenty
two. The numbers are grouped by the age of the head of the family. The salary multiples come from Fidelity
Investments' retirement guidelines, and the net worth formula comes from the book The Millionaire Next Door.""",
   "Federal Reserve Bank building columns", "OUR SOURCES")
sc("""Two important notes. These are survey numbers, so they're estimates. And they include home equity, which is a big
part of wealth for many families, but not money you can easily spend. Growth examples use a seven percent average
yearly return as an illustration, not a promise. This is education, not financial advice.""",
   "Calculator and pen on financial papers", "EDUCATION, NOT ADVICE")

# ---------------- Angle 1: the numbers ----------------
ch("Angle 1: The numbers")
pr("""Angle one. The numbers. Before we go decade by decade, you need to know the difference between two words that
change everything: median and average.""")
card("""In twenty twenty two, the median net worth of all American families was about one hundred ninety two thousand
seven hundred dollars. The average was about one million sixty thousand.""",
     {"type": "compare", "left": {"label": "Median family", "big": "$192,700", "sub": "half have more, half less"},
      "right": {"label": "Average family", "big": "$1.06M", "sub": "pulled up by the very top"},
      "note": "Federal Reserve, Survey of Consumer Finances 2022"})
sc("""Median means the family right in the middle. Half have more, half have less. The average adds everyone up and
divides, so a small number of extremely wealthy families pull it way up. That's why the average is more than five
times the median. When you see a headline saying the average American has some huge number, it's almost always the
average, and it doesn't describe a typical family at all. In this video, we focus on the median.""",
   "Suburban houses street United States", "MEDIAN, NOT AVERAGE")
sc("""Next, a popular rule of thumb from Fidelity Investments. They suggest aiming to have saved about one times your
salary by thirty, three times by forty, six times by fifty, eight times by sixty, and ten times by sixty seven. That's
retirement savings, not total net worth, and it's a guideline, not a law. But it gives you a target that grows with
your income.""",
   "Office workers meeting", "1X, 3X, 6X, 8X, 10X")
card("""For someone earning sixty thousand dollars a year, Fidelity's guideline would mean about one hundred eighty
thousand dollars in retirement savings by forty, and about three hundred sixty thousand by fifty.""",
     {"type": "compare", "left": {"label": "By 40", "big": "$180,000", "sub": "3x a $60,000 salary"},
      "right": {"label": "By 50", "big": "$360,000", "sub": "6x a $60,000 salary"},
      "note": "Fidelity retirement savings guideline (a rule of thumb)"})
sc("""And there's an older formula from Thomas Stanley and William Danko's book, The Millionaire Next Door. Multiply your
age by your yearly pretax income, then divide by ten. That's what they called your expected net worth. A forty year
old earning seventy thousand dollars would have an expected net worth of two hundred eighty thousand. Above double that,
they called you a prodigious accumulator of wealth. Below half, an under accumulator.""",
   "Old books library", "THE MILLIONAIRE NEXT DOOR FORMULA")
sc("""These rules disagree a bit, and they're all rough. That's fine. The point isn't to hit an exact number. It's to know
roughly where you are, and whether you're moving in the right direction. Now, decade by decade, starting with the age
group where almost everyone feels behind.""",
   "Map and compass", "ROUGHLY WHERE YOU ARE")

# ---------------- Decades ----------------
decade("Under 35",
"""Families headed by someone under thirty five had a median net worth of about thirty nine thousand dollars in twenty
twenty two.""",
{"type": "stat", "label": "median net worth, under 35", "big": "$39,040", "sub": "Federal Reserve, SCF 2022"},
"""Thirty nine thousand dollars. If you're in your twenties or early thirties and you have less than that, don't panic.
Many people in this group are just starting careers, paying off student loans, and buying their first car. Plenty have a
negative net worth, especially right after college. This decade isn't about having a lot. It's about the direction.""",
"""What matters most in this decade is habits, not balances. Building an emergency fund. Getting the full employer match.
Avoiding high interest debt. Starting to invest, even small amounts. Because money invested in your twenties has decades
to grow. At a seven percent illustration, every dollar invested at twenty five could become roughly fifteen dollars by
sixty five.""",
"""If you're behind here, the fix is simpler than at any other age. You have the most valuable asset in finance: time.
Focus on raising your income, because early career raises compound for decades. Learn a skill, switch jobs if the pay is
better, and keep your fixed costs low. A modest apartment and an older car in your twenties can be worth hundreds of
thousands of dollars by retirement.""",
"""Your move this decade: get your net worth above zero, then above one times your salary by around thirty. Invest a fixed
percentage of every paycheck automatically, starting with at least the employer match, and raise it by one percent every
year. If you do just that, you'll likely end your thirties well ahead of the median.""",
"Young people graduation", "DON'T PANIC",
"Piggy bank coins", "HABITS OVER BALANCES",
"Person studying laptop at night", "TIME IS YOUR ASSET",
"Graph trending upward", "ABOVE ZERO, THEN 1X")

decade("Age 35 to 44",
"""For families headed by someone thirty five to forty four, the median net worth was about one hundred thirty five
thousand dollars.""",
{"type": "stat", "label": "median net worth, age 35 to 44", "big": "$135,300", "sub": "Federal Reserve, SCF 2022"},
"""Look at that jump. From about thirty nine thousand to about one hundred thirty five thousand, more than three times
higher, in just one decade. That's what happens when people's incomes rise, they pay down debt, they build home equity,
and their early investments start to grow. This is often the decade where wealth starts to show up.""",
"""What matters in this decade is protecting your savings rate while life gets more expensive. Kids, bigger homes,
childcare, cars. These are also the years of peak lifestyle creep. The families who come out of this decade strong are
usually the ones who let their lifestyle grow slower than their income, and kept investing through every raise.""",
"""If you're behind in your late thirties or early forties, you still have twenty five years or more before a traditional
retirement age. That's plenty of time for compounding to do serious work. The key is to increase what you invest, not
just maintain it. Look at your three biggest costs, housing, cars and childcare, because that's where the real money is.""",
"""Your move this decade: aim for around three times your salary in retirement savings by forty, if you can, and push your
savings rate toward fifteen percent or more. Make sure you have term life insurance if anyone depends on your income, and
a basic will. Those aren't exciting, but they protect everything you're building.""",
"Family relaxing at home", "WEALTH STARTS TO SHOW",
"Luxury car dealership", "PEAK LIFESTYLE CREEP",
"Calendar planning", "25 YEARS IS PLENTY",
"Lawyer office documents", "PROTECT WHAT YOU BUILD")

short("If you're forty five and behind on money, this is what to do.")
decade("Age 45 to 54",
"""For families headed by someone forty five to fifty four, the median net worth was about two hundred forty seven
thousand dollars.""",
{"type": "stat", "label": "median net worth, age 45 to 54", "big": "$246,700", "sub": "Federal Reserve, SCF 2022"},
"""Around two hundred forty seven thousand dollars. For many families, a big piece of this is home equity, since people in
this group have often owned their homes for years. Their retirement accounts have also had decades to grow. This is where
the gap between people who started early and people who didn't becomes very visible.""",
"""What matters most in this decade is that these are often your peak earning years. Kids may be getting older, the
mortgage may be shrinking, and your income may be the highest it will ever be. That creates a window, maybe fifteen years,
where you can save more than at any other time in your life. Use it.""",
"""If you're behind, here's the honest truth. You can't get back the years you lost, but you can make the next fifteen
count. Starting at age fifty, the IRS allows extra catch up contributions to retirement accounts on top of the normal
limits. Check the current amounts, because they change. Every dollar of catch up contribution is a dollar that grows tax
advantaged.""",
"""Your move this decade: aim to put twenty percent or more of your income toward retirement if you're behind. Pay off
any remaining high interest debt. Avoid taking on a new mortgage or big car loans now if you can. And get a clear
estimate of your Social Security benefit at ssa dot gov, because that number changes how much you really need.""",
"House with for sale sign", "HOME EQUITY GROWS",
"Office building at dusk", "PEAK EARNING YEARS",
"Paperwork documents desk", "CATCH UP CONTRIBUTIONS",
"Social Security card", "KNOW YOUR BENEFIT")

pr("""Quick pause. If you're finding your decade useful, subscribe. This channel goes step by step through every stage of
building wealth, and new videos come out every couple of days. It's free, and it helps more than you'd think. Now, the
decades closest to retirement.""")

decade("Age 55 to 64",
"""For families headed by someone fifty five to sixty four, the median net worth was about three hundred sixty four
thousand dollars.""",
{"type": "stat", "label": "median net worth, age 55 to 64", "big": "$364,500", "sub": "Federal Reserve, SCF 2022"},
"""Around three hundred sixty four thousand dollars, right before retirement for many people. That may sound like a lot,
but remember, it includes the home. The money available to live on is often much less. And with the four percent rule of
thumb, two hundred thousand dollars of investments supports only about eight thousand dollars a year.""",
"""What matters in this decade is the plan for the transition. When will you claim Social Security? How will you pay for
health insurance before Medicare starts at sixty five? Will you downsize? Will you work part time for a few years? These
decisions can matter as much as anything you saved before.""",
"""If you're behind at fifty five or sixty, you have real options. Working even two or three more years can make a huge
difference: more years of saving, fewer years of withdrawals, and a bigger Social Security check if you delay claiming.
The Social Security Administration explains that benefits grow for each year you delay past full retirement age, up to
age seventy.""",
"""Your move this decade: max out catch up contributions if you can, plan your health insurance bridge, and decide your
Social Security strategy carefully. Many people also reduce investment risk gradually in this decade, with more bonds and
cash, so a market crash right before retirement doesn't derail everything.""",
"Retired couple on porch", "IT INCLUDES THE HOUSE",
"Hospital building exterior", "PLAN THE TRANSITION",
"Calendar planning", "WORK A LITTLE LONGER?",
"Pie chart on paper", "REDUCE RISK GRADUALLY")

decade("Age 65 and up",
"""For families headed by someone sixty five to seventy four, the median net worth was about four hundred ten thousand
dollars, the highest of any age group. For seventy five and older, about three hundred thirty six thousand.""",
{"type": "compare", "left": {"label": "Age 65 to 74", "big": "$409,900", "sub": "median net worth"},
 "right": {"label": "Age 75+", "big": "$335,600", "sub": "median net worth"},
 "note": "Federal Reserve, Survey of Consumer Finances 2022"},
"""Net worth usually peaks in the late sixties and early seventies, then slowly declines as people spend their savings in
retirement. That's not failure. That's exactly what the money was for. The goal in this stage isn't to keep growing. It's
to make the money last, and to enjoy it.""",
"""What matters in this decade is managing withdrawals, taxes and health costs. Required minimum distributions from many
retirement accounts start in your seventies, and the rules have changed in recent years, so check the current IRS age.
Long term care is another big unknown, and planning for it early gives you more choices.""",
"""If you're behind in retirement, focus on what you can control. Reduce big fixed costs, like housing, if you can. Look
into every benefit you may qualify for. Consider part time work you enjoy. And be extremely careful with scams, which
target retirees heavily. The FBI's Internet Crime Complaint Center reports billions of dollars in losses among people
over sixty.""",
"""Your move in this stage: write a simple yearly spending plan, keep one to two years of spending in safe accounts, and
review beneficiaries and your will. And if you have more than you need, decide while you can how you want to help family
or causes you care about.""",
"Elderly couple travel airport", "THE PEAK",
"Tax forms on desk", "WITHDRAWALS AND TAXES",
"Computer hacker keyboard", "WATCH FOR SCAMS",
"Family walking on beach", "ENJOY IT")

# ---------------- Levers ----------------
ch("What really moves net worth")
pr("""Before the psychology, let's look at what actually builds net worth in American households. Because when you look
at the Federal Reserve data, the same few things show up again and again.""")
sc("""The first is the home. For the middle class, home equity is often the largest single asset. Every mortgage payment
pays down a bit of the loan, and over long periods home prices have tended to rise, though not always and not everywhere.
That's why net worth often jumps for people in their forties and fifties. It's not that they suddenly became great
investors. Their house quietly turned into savings.""",
   "House with for sale sign", "LEVER 1: THE HOME")
sc("""But the home is a slow, illiquid lever. You can't sell a bedroom to pay for groceries. And a house that's too
expensive can drain your savings through taxes, insurance and repairs. The best version of this lever is a home you can
comfortably afford, kept for a long time, with a mortgage you'll pay off before or around retirement.""",
   "House repair roof", "AFFORDABLE AND LONG TERM")
sc("""The second lever is retirement accounts. Workplace plans like a 401k, plus IRAs, let money grow without yearly taxes,
and many employers add matching contributions. For many families, these accounts and the home together make up most of
their wealth. The secret here is automation: contributions taken from every paycheck, invested, and left alone for
decades.""",
   "Office workers meeting", "LEVER 2: RETIREMENT ACCOUNTS")
sc("""The third lever is business ownership. In the Federal Reserve's data, families that own a business tend to have much
higher net worth than those that don't, though business is also riskier and many small businesses fail. You don't have to
start a company to benefit. Owning broad stock index funds makes you a part owner of thousands of businesses.""",
   "Small business storefront", "LEVER 3: OWNERSHIP")
sc("""And the fourth lever works in reverse: debt. High interest debt pulls net worth down every single month. A thirty
thousand dollar car loan, a twenty thousand dollar credit card balance, and a large student loan can keep someone's net
worth near zero for years, even on a good income. Paying down expensive debt is one of the most reliable ways to raise
your net worth, because every dollar repaid is a dollar of net worth gained.""",
   "Credit card bills on table", "LEVER 4: DEBT IN REVERSE")
sc("""So if you want to move your number, focus on these four. An affordable home kept long term. Automatic retirement
investing with every matching dollar. Ownership, through funds or a business. And getting rid of expensive debt. Almost
everything else is detail.""",
   "Notebook with financial notes", "FOUR LEVERS")

# ---------------- Example people ----------------
short("Five people, five ages, five net worths. Which one are you?")
ch("Five people, five decades")
pr("""Let's meet five example people, one for each decade. They're made up, but each one is built from the typical patterns
in the data. See if you recognize yourself.""")
sc("""Jasmine is twenty eight. She has eighteen thousand dollars in savings and a 401k, a car worth eight thousand, and
twenty two thousand in student loans. Her net worth is about plus four thousand dollars. Below the median for her age
group, but moving fast, because she just started contributing ten percent of her salary with a match. In five years, if
she keeps going, she'll likely be well above the median.""",
   "Young woman working on laptop", "JASMINE, 28: +$4,000")
sc("""David is thirty nine. He and his wife own a home with ninety thousand dollars of equity and have sixty thousand in
retirement accounts. They also have a twenty eight thousand dollar car loan and eight thousand on a credit card. Their net
worth is around one hundred fourteen thousand dollars, a little below the median for their age. Paying off the card and
not replacing the car for a few years would move them above it.""",
   "Family relaxing at home", "DAVID, 39: ~$114,000")
sc("""Lisa is forty nine and single. She rents, has no home equity, and has about one hundred forty thousand dollars in her
retirement accounts. Her net worth is about one hundred thirty five thousand. Below the median for her age, mostly because
she doesn't own a home. But her money is liquid and invested, and with catch up contributions starting next year, she can
put away a lot in her peak earning years.""",
   "Woman in office", "LISA, 49: ~$135,000")
sc("""Mike is fifty eight. His house is almost paid off, with three hundred twenty thousand dollars of equity, and he has
two hundred ten thousand in a 401k. Net worth, about five hundred thirty thousand. Comfortably above the median. But his
investable money, the part that will pay for retirement, is only two hundred ten thousand. Mike's real question isn't his
net worth. It's whether to downsize, work a few more years, or delay Social Security.""",
   "Older man reading financial newspaper", "MIKE, 58: ~$530,000")
sc("""And Rosa is seventy one. Her net worth is about four hundred thousand dollars, mostly her paid off home plus one
hundred thousand in savings. With Social Security covering most of her bills, she withdraws a little each year for travel
and her grandchildren. Her net worth is slowly declining, and that's exactly the plan. Her money is doing its job.""",
   "Retired woman gardening", "ROSA, 71: ~$400,000")
sc("""Notice that the net worth number alone doesn't tell you who's in good shape. Jasmine's small number is healthy because
of her direction. Mike's big number hides a retirement question. Rosa's falling number is a success. That's why the
playbook matters more than the comparison.""",
   "Three people silhouettes", "THE NUMBER ISN'T THE STORY")

# ---------------- Angle 2: psychology ----------------
short("Comparing your net worth to others can make you richer, or much poorer.")
ch("Angle 2: The psychology")
pr("""Angle two. The psychology. Because looking at these numbers does something to people. Some feel proud. Some feel
crushed. And how you react matters more than the number itself.""")
sc("""The first trap is comparing yourself to the average instead of the median. People see a headline that the average
American in their forties has nearly a million dollars, and they feel like failures. But that average is pulled up by a
small number of very wealthy families. Compare yourself to the median, and most people discover they're much closer to
normal than they thought.""",
   "Newspaper headlines", "THE AVERAGE MAKES YOU FEEL POOR")
sc("""The second trap is comparing yourself to the people around you. Your neighbor's new truck, your friend's vacation,
your coworker's renovation. You see their spending, but not their debt. Some of the people who look the richest have the
lowest net worth, because they spend everything they earn. Stanley and Danko found exactly this in their research. Many
true millionaires lived in modest homes and drove ordinary cars.""",
   "Pickup truck parked", "YOU SEE SPENDING, NOT DEBT")
sc("""The third trap is shame. When people feel far behind, they often stop looking. They avoid opening statements, they
don't check balances, and the problem grows in the dark. Research on financial stress has found that worry about money
can make it harder to think clearly about long term decisions. The fix is to look anyway, and turn a scary number into a
plan.""",
   "Person stressed looking at bills", "SHAME MAKES PEOPLE LOOK AWAY")
sc("""The fourth trap is the opposite: complacency. Some people discover they're above the median and relax. But the median
isn't a finish line. A median sixty year old with three hundred sixty thousand dollars, mostly in home equity, may not have
enough to retire comfortably. Being normal isn't the same as being ready. Your target is your own number, not the
country's.""",
   "Person relaxing on couch", "NORMAL IS NOT READY")
sc("""So here's the healthy way to use these numbers. Look at them once. Find your decade. Notice whether you're above or
below the median. Then put them away, because staring at other people's numbers every week helps nobody. Focus on the only comparison that really matters: you this year versus you last
year. If your net worth is going up every year, you're winning, whatever anyone else is doing.""",
   "Person running on road", "YOU VS LAST YEAR")
sc("""There's one more psychological effect worth knowing about. When people start tracking their net worth regularly, they
tend to make better decisions without even trying. A purchase stops being just a purchase. It becomes a small dent in a
number you care about. Economists sometimes call this salience: what you pay attention to, you manage. That's why the
single most useful habit from this whole video is simply writing your number down, regularly.""",
   "Notebook with financial notes", "WHAT YOU WATCH, YOU MANAGE")
sc("""And finally, be kind to yourself about the past. Many people who are behind got there through things they couldn't
control: a layoff, an illness, a divorce, caring for family, or starting adult life in a recession. Your number reflects
your history, not your worth as a person. What matters now is the next decision, and the one after that.""",
   "Person thinking by window", "YOUR PAST IS NOT YOUR WORTH")

# ---------------- Angle 3: playbook ----------------
short("Here's a catch up plan if you're behind on money at any age.")
ch("Angle 3: The catch up playbook")
pr("""Angle three. The playbook. If you're behind for your age, here's a catch up plan that works at any age. Five moves,
in order.""")
sc("""Move one. Find your real number. Write down everything you own and everything you owe, today. Then calculate two
versions: your total net worth, and your net worth without your home. The second one tells you how much money is
actually working for you. Do this once a quarter. It takes less than an hour, and watching the number change is one of the
best motivators there is.""",
   "Spreadsheet on laptop", "MOVE 1: YOUR REAL NUMBER")
sc("""Move two. Stop the leaks. High interest debt is the biggest one. Credit cards at over twenty percent interest are
compounding against you every day. Then the big fixed costs: a car payment that's too large, a home that eats too much of
your income, subscriptions you forgot about. Every leak you plug becomes money you can invest.""",
   "Credit card bills on table", "MOVE 2: STOP THE LEAKS")
sc("""Move three. Raise your savings rate, aggressively but sustainably. If you're behind, ten percent probably isn't
enough. Aim for fifteen, then twenty. Use raises, bonuses and paid off loans to get there without cutting your lifestyle
all at once. And use every tax advantaged account you have access to: workplace plans, IRAs, and catch up contributions
once you're fifty.""",
   "Graph trending upward", "MOVE 3: RAISE THE RATE")
sc("""Move four. Grow your income. At any age, more income is the fastest way to catch up. In your twenties and thirties,
it's skills, job changes and promotions. In your forties and fifties, it might be a raise you've been afraid to ask for,
consulting on the side, or turning a hobby into income. Even a few hundred extra dollars a month, invested, changes the
math.""",
   "Job interview handshake", "MOVE 4: EARN MORE")
sc("""Move five. Let time and consistency work. Invest automatically, in low cost, diversified funds, and don't stop when
markets fall. At a seven percent illustration, someone who starts investing one thousand dollars a month at forty five
could have roughly five hundred twenty thousand dollars by sixty five. That alone would put them well above the median for
their age.""",
   "Snowball rolling in snow", "MOVE 5: LET TIME WORK")
card("""On screen: one thousand dollars a month, starting at forty five, for twenty years, at a seven percent illustration.
Roughly five hundred twenty thousand dollars at sixty five.""",
     {"type": "growth", "monthly": 1000, "rate": 0.07, "years": 20})

# ---------------- Mistakes by decade ----------------
ch("The biggest mistake in each decade")
pr("""Every decade has one mistake that costs people more than any other. Here they are, so you can skip them.""")
sc("""In your twenties, the biggest mistake is waiting to start. People think they'll invest once they earn more. But the
money invested in your twenties is the most powerful money you'll ever invest, because it has the most time to grow. At a
seven percent illustration, a dollar invested at twenty five can grow roughly sixteen times by sixty five. A dollar
invested at forty five grows about four times. Same dollar. Very different result.""",
   "Young people graduation", "20s: WAITING TO START")
sc("""In your thirties, the biggest mistake is lifestyle inflation. Income finally rises, and so does everything else. The
house, the cars, the vacations, the restaurants. It all feels deserved. But the thirties are when the gap between savers
and spenders opens up. Keep your lifestyle growing slower than your income, and your forties will look completely
different.""",
   "Luxury car dealership", "30s: LIFESTYLE INFLATION")
sc("""In your forties, the biggest mistake is putting everyone else first. Kids' activities, college savings, helping
parents. All of it comes from love. But a common piece of advice from planners is that you can borrow for college, but you
can't borrow for retirement. Keep funding your own future, even while you help the people you love.""",
   "Family dinner table", "40s: EVERYONE ELSE FIRST")
sc("""In your fifties, the biggest mistake is panic. Either panic that it's too late, which leads people to give up, or
panic that leads them to chase risky investments to catch up quickly. Both are expensive. The fifties reward steady,
boring, high savings, using every catch up contribution available.""",
   "Stock market chart falling on screen", "50s: PANIC")
sc("""In your sixties, the biggest mistake is claiming Social Security without a plan, or retiring without knowing your
health insurance costs. These decisions are mostly permanent, so they deserve real time and research. And in your seventies
and beyond, the biggest mistake is falling for scams, or never letting yourself enjoy the money you worked so hard for.""",
   "Social Security card", "60s AND BEYOND")

# ---------------- Ten year challenge ----------------
ch("The ten year challenge")
pr("""Here's a challenge I want to give you. Forget the medians for a moment. Ask yourself one question: where could my net
worth be in ten years?""")
sc("""Start with today's number. Then add what you'll invest each year, and a conservative growth estimate. At a seven
percent illustration, five hundred dollars a month for ten years grows to roughly eighty seven thousand dollars. One
thousand dollars a month, roughly one hundred seventy three thousand. Add debt you'll pay off, and equity you'll build in a
home, and most people are surprised how much can change in a decade.""",
   "Calculator with financial charts", "WHERE IN TEN YEARS?")
sc("""Ten years is long enough for compounding to start showing up, and short enough to feel real. It's also roughly the gap
between the age groups in the Federal Reserve data. So your challenge is this: in ten years, be above the median for the
age group you'll be in. If you're thirty two today, aim to beat the forty two year old median. If you're fifty, aim to beat
the median at sixty.""",
   "Calendar planning", "BEAT YOUR FUTURE MEDIAN")
sc("""Write your ten year target on a piece of paper, along with the monthly amount it takes to get there. Then check it once
a year, on the same date. Some years you'll be ahead, some behind. Markets will move. Life will happen. But having a clear
target turns net worth from a scary judgment into a game you can win.""",
   "Notebook with financial notes", "A GAME YOU CAN WIN")
sc("""And here's what people often find after a few years of this. The number starts to grow faster than they expected,
because growth begins to add to their contributions. The habits get easier. And the question changes from, am I behind?
to, how far ahead can I get? That shift, from fear to curiosity, is one of the best things that can happen to your
financial life.""",
   "Sunrise over mountains", "FROM FEAR TO CURIOSITY")

# ---------------- Questions ----------------
ch("Questions people ask")
pr("""Let me answer the questions people ask me most about net worth by age.""")
sc("""Question one. Should I count my house? For your total net worth, yes. But also track your net worth without the house,
because you can't buy groceries with home equity unless you sell or borrow against it. Question two. Should I count my
car? Technically yes, at what you could sell it for today, not what you paid. Cars lose value quickly, so for many people
the car is a small number, or even negative if the loan is bigger than the value.""",
   "Car dealership lot", "HOUSE? CAR?")
sc("""Question three. What about a pension? A pension is valuable, even if it's not easy to put a number on it. If you have
one, your savings target can be lower, because part of your retirement income is already covered. Question four. What
about student loans? They count as debt. A negative net worth in your twenties because of student loans is extremely
common, and it doesn't mean you're failing. It means you're early.""",
   "Graduation cap diploma", "PENSION? STUDENT LOANS?")
sc("""Question five. How often should I calculate my net worth? Once a quarter or once a year is enough for most people.
Daily checking just makes you react to market noise. Question six. What's a good net worth to retire? There's no single
number. A common rule of thumb is to have about twenty five times your expected yearly spending invested, minus what Social
Security and any pension will cover. That's your personal target.""",
   "Calendar planning", "HOW OFTEN? HOW MUCH?")
sc("""Question seven. Is it too late to start at fifty five? No. You may not reach the same number as someone who started at
twenty five, but ten years of focused saving, catch up contributions, a later Social Security claim and lower costs can
make a big difference to your retirement. The worst choice is deciding it's too late and doing nothing.""",
   "Older man reading financial newspaper", "TOO LATE AT 55?")
sc("""Question eight. My partner and I have very different numbers. Does that matter? For couples who share their finances,
what matters is the combined picture and the shared plan. But it's worth talking openly about debts and savings each of
you brings, because surprises are what cause money fights. Many couples find a monthly money date, twenty minutes with the
numbers, helps more than any budgeting app.""",
   "Couple cooking together kitchen", "COUPLES WITH DIFFERENT NUMBERS")
sc("""Question nine. Should I pay off my mortgage early to raise my net worth? Paying off a mortgage does raise your net worth,
dollar for dollar, and it lowers the income you need in retirement. Investing instead may grow faster over long periods,
but with more risk. Many people do a bit of both, especially as retirement gets closer. There's no single right answer, but
high interest debt should always come first.""",
   "House with for sale sign", "PAY OFF THE MORTGAGE?")
sc("""Question ten. Do I need a high income to have a high net worth? It helps, but it's not required. Stanley and Danko found
many millionaires with ordinary jobs, like teachers, small business owners and tradespeople, who simply spent less than
they earned for decades. And many high earners have low net worth because they spend almost everything. The gap between
income and spending matters more than income alone.""",
   "Small business storefront", "DO I NEED A HIGH INCOME?")

# ---------------- Recap ----------------
ch("Recap: net worth by age")
sc("""Let's recap the medians from the Federal Reserve, twenty twenty two. Under thirty five, about thirty nine thousand
dollars. Thirty five to forty four, about one hundred thirty five thousand. Forty five to fifty four, about two hundred
forty seven thousand.""",
   "Staircase steps", "UNDER 35 TO 54")
sc("""Fifty five to sixty four, about three hundred sixty four thousand. Sixty five to seventy four, about four hundred ten
thousand, the peak. And seventy five and up, about three hundred thirty six thousand, as people spend in retirement.""",
   "Mountain climber reaching summit", "55 AND UP")
sc("""And the three angles. The numbers: use the median, not the average, and rules of thumb like Fidelity's salary
multiples. The psychology: don't compare yourself to the average or your neighbors, compare yourself to last year. And the
playbook: find your real number, stop the leaks, raise your rate, earn more, and let time work.""",
   "Map and compass", "NUMBERS, PSYCHOLOGY, PLAYBOOK")
sc("""And remember the four levers that really move net worth: an affordable home kept for the long term, automatic
retirement investing with every matching dollar, ownership through funds or a business, and getting rid of expensive debt.
Pull those four levers steadily, decade after decade, and the medians in this video stop being a judgment. They become
numbers you pass on the way to your own goal. Wherever you are today, the next ten years can look completely different from
the last ten, and that's not a slogan. It's just how compounding works when you give it time.""",
   "Factory machine gears", "PULL THE FOUR LEVERS")

# ---------------- Close ----------------
ch("What to do next")
pr("""So here's your homework. Calculate your net worth tonight, both with and without your home. Find your decade. And then
write down one move from the catch up playbook that you'll start this week. Just one. Small moves, repeated, are what
change the number. If you want the full plan with worksheets,
it's in my playbook, link in the description. I'm Ryan Rover. See you in the next one.""")

save("video07", "What Your Net Worth Should Be at Every Age (And What to Do If It Isn't)", [
    "Federal Reserve, Changes in U.S. Family Finances from 2019 to 2022: Evidence from the Survey of Consumer Finances (median net worth all families $192,700, mean $1,063,700; by age of head: under 35 $39,040; 35-44 $135,300; 45-54 $246,700; 55-64 $364,500; 65-74 $409,900; 75+ $335,600)",
    "Fidelity Investments, How much do I need to save for retirement? (1x salary by 30, 3x by 40, 6x by 50, 8x by 60, 10x by 67)",
    "Thomas J. Stanley and William D. Danko, The Millionaire Next Door (1996) (expected net worth = age x pretax income / 10)",
    "IRS, catch-up contributions and required minimum distributions (check current-year rules)",
    "Social Security Administration, delayed retirement credits (benefits grow for each year of delay up to age 70)",
    "FBI Internet Crime Complaint Center, Elder Fraud Report",
    "Compound growth: stated illustrative math at 7% average yearly return, compounded monthly",
], "net worth by age")
