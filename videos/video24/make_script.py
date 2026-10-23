import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save

def item(n, title, sub, card_text, body, example, fix, q1, c1, q2, c2, q3, c3):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"{n} OF 20")
    sc(body, q1, c1)
    sc(example, q2, c2)
    sc(fix, q3, c3)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. When you imagine a millionaire's Tuesday, you probably imagine champagne, a private
jet, and a meeting on a yacht. But the research on real American millionaires paints a very different
picture. Their Tuesday looks a lot like yours. The alarm, the commute, the work, the dinner. The difference is
in a handful of small choices along the way. Today, we're going to walk through a normal Tuesday, hour by
hour, and find twenty of those choices.""")
card("""Here's a fact that changes how you picture millionaires. In Ramsey Solutions' National Study of
Millionaires, a survey of more than ten thousand American millionaires, seventy nine percent said they did
not receive any inheritance at all.""",
     {"type": "stat", "label": "millionaires who inherited nothing", "big": "79%", "sub": "Ramsey Solutions, National Study of Millionaires"})
sc("""In that same study, the most common careers among the millionaires were things like engineer,
accountant, teacher, manager and attorney. Ordinary professional jobs. Thomas Stanley found something similar
decades earlier in The Millionaire Next Door. Most millionaires were self made, many owned small businesses,
and many lived in normal neighborhoods. So when we look at a millionaire's Tuesday, we're mostly looking at
the Tuesday of a regular person who made a lot of good small decisions, for a long time.""",
   "Office workers commuting morning", "ORDINARY JOBS")
sc("""We'll look at this day from three angles. First, the numbers. The money decisions that happen
almost automatically, from the morning coffee to the commute. Second, the psychology. How millionaires think
during the day, at work and in conversations. And third, the playbook. The evening and night routines that
quietly build wealth while everyone else is scrolling. Along the way, I'll point out which parts you can copy
tomorrow, whatever your income.""",
   "Clock showing morning time", "THREE ANGLES")
pr("""Alright. It's six thirty in the morning, and the alarm just went off. Let's go.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our sources. Millionaire profiles come from Ramsey Solutions' National Study of Millionaires and from
Thomas Stanley's research. Time use data comes from the Bureau of Labor Statistics' American Time Use Survey.
Some habit statistics come from author Tom Corley's Rich Habits survey, which is small and self reported, so
treat those numbers as interesting, not as proof. Growth examples use a stated seven percent average yearly
return, which is an illustration, not a promise. This is education, not financial advice.""",
   "Library research books", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers (morning)")
pr("""Angle one. The numbers. The morning is where a lot of automatic money decisions happen, and
millionaires have quietly set most of them up in advance.""")

item(1, "The money moved before they woke up", "automatic investing",
"""Six thirty. Moment number one. Before the millionaire even opens their eyes, money has already moved.""",
"""On payday, a set amount goes straight from the paycheck into a retirement account, and another amount
into savings or a brokerage account. They don't decide to invest each month. It just happens. In Ramsey's
study, about eight in ten millionaires said they invested in their company's retirement plan. Automatic
investing is the single most common thread in how ordinary people become millionaires.""",
"""The reason automation works so well is that it removes the daily decision. If you had to choose to
invest every single month, you'd skip months. Life would get in the way. A car repair, a holiday, a sale. With
automation, the default is that you invest, and you'd have to actively stop it. Behavioral economists have
shown that defaults are incredibly powerful, which is why companies that automatically enroll employees in
retirement plans see much higher participation.""",
"""Copy it tomorrow. Log into your payroll or bank account and set one automatic transfer for the day after
payday. Start with whatever doesn't hurt, even one percent of your pay. Then put a reminder in your calendar
to raise it every six months. Within a few years, you'll be investing a meaningful share of your income
without ever feeling the decision.""",
"Sunrise through bedroom window", "MONEY MOVES FIRST",
"Payroll direct deposit screen", "THE DEFAULT IS INVEST",
"Calendar reminder on phone", "RAISE IT EVERY 6 MONTHS")

item(2, "Coffee at home, mostly", "small, not miserable",
"""Six forty five. Moment number two. Coffee. Usually at home.""",
"""Let's be honest. Coffee isn't going to make or break anyone's retirement on its own. Personal finance
writers have argued about the latte factor for years, and the truth is somewhere in the middle. But the
habit behind it matters. Millionaires in Stanley's research tended to be deliberate about everyday spending.
They didn't do everything on autopilot.""",
"""If a coffee shop drink costs around five or six dollars and you buy one every workday, that's well over
one thousand dollars a year. Some people decide that's worth it, and that's fine. The point is that it's a
decision. Many millionaires make coffee at home most days and enjoy the coffee shop as a treat, not a
default. The same mindset applies to lunch, snacks and every small daily purchase.""",
"""Copy it tomorrow. Pick one daily purchase and decide on purpose how often you want it. Maybe coffee out
on Fridays only. Put the money you save into your automatic investment, so you can see it grow. Spending
on purpose feels much better than spending by default.""",
"Coffee maker kitchen morning", "COFFEE AT HOME",
"Coffee shop counter", "A TREAT, NOT A DEFAULT",
"Jar with coins labeled coffee", "SPEND ON PURPOSE")

item(3, "A paid off car in the driveway", "no payment, no problem",
"""Seven fifteen. Moment number three. They walk out to a car that's probably several years old, and
probably paid off.""",
"""In Stop Acting Rich, Stanley found that the median price millionaires paid for their most recent car was
about thirty one thousand dollars, in a survey from the late two thousands. Ramsey's study also found that
many millionaires drive mainstream brands like Toyota, Honda and Ford, and keep them for years. Meanwhile,
Edmunds has reported average new car payments above seven hundred dollars a month.""",
"""Think about what no car payment means. Seven hundred dollars a month, invested at a seven percent average
yearly return for ten years, grows to over one hundred twenty thousand dollars. That's the hidden power of
driving a paid off car. It isn't glamorous, but each month without a payment is a month the money can work
for you instead of the bank.""",
"""Copy it tomorrow. If you have a car loan, don't sell the car in a panic. Instead, plan to keep it for
years after the last payment. When it's paid off, keep making the same payment, but to your own savings
account. That fund becomes the cash for your next car.""",
"Older Toyota in driveway", "PAID OFF",
"Car payment bill", "$700 A MONTH",
"Savings account car fund", "PAY YOURSELF THE PAYMENT")

card("""Here's that math on screen. A seven hundred dollar monthly payment, invested instead at a seven
percent average yearly return, grows to roughly one hundred twenty one thousand dollars in ten years.""",
     {"type": "growth", "monthly": 700, "rate": 0.07, "years": 10})

item(4, "The commute is a classroom", "audiobooks and podcasts",
"""Seven thirty. Moment number four. The commute. Many millionaires turn it into a classroom.""",
"""The Bureau of Labor Statistics' American Time Use Survey and Census data show that many Americans spend
close to an hour a day commuting. That's around two hundred fifty hours a year for a full time worker. Many
successful people use at least part of that time for audiobooks, podcasts or language lessons.""",
"""Tom Corley's Rich Habits survey reported that most of the wealthy people he interviewed read for self
improvement regularly, and that many listened to educational audio while driving. Remember, that's a small
self reported survey. But the idea is sound. Two hundred fifty hours a year is like a semester of college,
every year, for free.""",
"""Copy it tomorrow. Pick one book about money, your career or a skill you want, and listen to it during
your commute this month. If you don't commute, use the time you spend doing chores or walking. One book a
month is twelve books a year.""",
"Car dashboard with podcast", "AN HOUR A DAY",
"Headphones and audiobook", "A SEMESTER A YEAR",
"Stack of books on desk", "12 BOOKS A YEAR")

item(5, "Lunch from home, most days", "the quiet thousand",
"""Twelve noon. Moment number five. Lunch. Often brought from home.""",
"""Buying lunch every workday can easily cost a hundred dollars or more a week in many cities. Bringing
lunch most days can save thousands of dollars a year. Many millionaires do this not because they need to,
but because it's how they built their wealth in the first place, and the habit stuck.""",
"""There's a bonus. Many people who bring lunch also eat healthier, and health is one of the biggest
financial assets you have. Medical costs and lost work time from health problems are expensive. A simple
habit like packing lunch quietly pays off in two ways.""",
"""Copy it tomorrow. Cook a little extra at dinner tonight and pack it for lunch. Aim for three days a week
at first. Track what you save for a month. When you see the total, it gets much easier to keep going.""",
"Packed lunch container", "LUNCH FROM HOME",
"Healthy salad meal prep", "HEALTH IS WEALTH",
"Kitchen preparing food", "THREE DAYS A WEEK")

item(6, "They know their numbers", "the five minute check",
"""Twelve thirty. Moment number six. A quick look at the numbers.""",
"""Many wealthy people check their spending and accounts regularly. Not obsessively, but often enough to
know where they stand. Stanley found that the millionaires he studied were far more likely than others to
know exactly how much they spent each year on food, clothing and housing.""",
"""Knowing your numbers changes your decisions. When you know your savings rate is twenty percent, you
think twice before signing up for a new monthly payment. When you know what you spent on dining out last
month, you naturally adjust. Awareness does a lot of the work that willpower can't.""",
"""Copy it tomorrow. Put a five minute weekly money check on your calendar. Look at your balance, your
spending since last week, and any upcoming bills. That's it. Five minutes a week is enough to stay in
control.""",
"Person checking phone at lunch", "A QUICK LOOK",
"Spreadsheet budget categories", "KNOW WHAT YOU SPEND",
"Weekly calendar note", "5 MINUTES A WEEK")

item(7, "No impulse buys at work", "the online cart test",
"""One fifteen. Moment number seven. The online shopping temptation.""",
"""Office breaks are prime time for online shopping. A quick scroll, a flash sale, one click and it's on the
way. Retailers know this, and many sales and emails are timed for exactly these moments.""",
"""Millionaires are just as tempted, but many use a simple rule. They don't buy non essentials on impulse.
They wait. A day for small items, a month for big ones. Most of the time, the urge passes. When it doesn't,
they buy it without guilt, because they know they really want it.""",
"""Copy it tomorrow. Remove your saved card from your favorite shopping sites, and turn off one click
buying. That small bit of friction gives your brain a moment to ask, do I actually need this? Then add the
twenty four hour rule for anything that isn't essential.""",
"Online shopping cart on laptop", "THE FLASH SALE",
"Hourglass timer", "WAIT A DAY",
"Credit card form on screen", "ADD FRICTION")

pr("""That's angle one. The money moved automatically, coffee and lunch on purpose, a paid off car, a commute
that teaches, a quick look at the numbers, and no impulse buys. None of these require a big salary. Now angle
two. The psychology. How millionaires think during the workday.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology (workday)")
sc("""The middle of the day is where mindset shows up. How you handle your boss, your career, your
coworkers, a sales pitch, or a bad day at the office. Millionaires aren't immune to stress or temptation.
But research suggests they tend to think about time, risk and value a little differently.""",
   "Office meeting room", "THE MINDSET")

item(8, "They think like owners", "not just employees",
"""Two o'clock. Moment number eight. They think like owners, even when they're employees.""",
"""Stanley found that a large share of millionaires were business owners, and many of the rest thought like
owners at work. They asked how they could make themselves more valuable, not just how they could get through
the day. Over a career, that mindset tends to lead to raises, promotions and opportunities.""",
"""Thinking like an owner also changes how you see your own money. An owner asks, what will this purchase
return? An employee mindset asks, can I afford the payment? Owners buy assets that grow. That simple shift
in question changes thousands of decisions over a lifetime.""",
"""Copy it tomorrow. At work, ask yourself one question. What's one thing I could do this week that would
make me noticeably more valuable here? Do it. And with your money, ask what a purchase will return before
you ask about the payment.""",
"Small business owner in shop", "THINK LIKE AN OWNER",
"Business plan on desk", "WHAT WILL IT RETURN?",
"Person working focused at desk", "BE MORE VALUABLE")

item(9, "Income is their biggest tool", "investing in earning power",
"""Two thirty. Moment number nine. They treat their income as their most important tool.""",
"""Early in life, your ability to earn is usually worth far more than your savings. Raising your income by
ten or twenty percent through skills or a new role can do more for your wealth than years of cutting coupons.
Many self made millionaires focused hard on growing their income in their twenties and thirties.""",
"""The trick is what they did with the higher income. Instead of upgrading everything, they kept their
lifestyle relatively steady and invested the difference. That gap between income and spending is where
wealth comes from. Earning more only helps if you keep a good part of it.""",
"""Copy it tomorrow. Look up the salary range for your role and the next role up. Identify one skill or
certification that would help you get there. Spend thirty minutes a week on it. And when your next raise
comes, save at least half of it.""",
"Person studying certification", "GROW THE INCOME",
"Graph of income and spending gap", "KEEP THE GAP",
"Laptop online course", "30 MINUTES A WEEK")

item(10, "They say no to most pitches", "if it sounds too good",
"""Three o'clock. Moment number ten. Someone pitches them an investment. They say no.""",
"""Wealthy people get a lot of pitches. Hot stocks, crypto tips, business deals, insurance products, rental
schemes. Most of them are bad, some are scams. The Federal Trade Commission receives reports of billions of
dollars lost to fraud every year, and investment scams are among the costliest categories.""",
"""Many millionaires follow a version of Warren Buffett's rule: only invest in what you understand. If they
can't explain how the investment makes money, what it costs and how to get out, they pass. Saying no to
most opportunities protects the wealth they've built.""",
"""Copy it tomorrow. Write these three questions on a card and keep it in your wallet. How do you make
money? What are all the fees? How do I get my money out? If anyone can't answer clearly, walk away.""",
"Salesperson pitching in office", "THE PITCH",
"Warning sign scam alert", "BILLIONS LOST TO FRAUD",
"Index card with questions", "THREE QUESTIONS")

pr("""Let me take a short break here. If you're enjoying this walk through a millionaire's Tuesday, please
subscribe to Ryan Rover Money. It's free, and it tells me to make more videos like this one. Okay, it's three
thirty in the afternoon. Back to the office.""")

item(11, "They don't keep up with coworkers", "status at work",
"""Three thirty. Moment number eleven. A coworker shows off a new car. The millionaire doesn't care.""",
"""Workplaces are full of quiet status competition. Cars in the parking lot, watches, vacations, clothes.
Stanley described how many high earners felt pressure to look successful, which kept them from building real
wealth. Many quiet millionaires simply opted out of that game.""",
"""Opting out isn't about judging anyone. It's about knowing your own goals. Every dollar spent on looking
successful is a dollar that can't buy freedom later. Millionaires often care more about owning their time
than about impressing the people in the next cubicle.""",
"""Copy it tomorrow. Next time you feel the pull to match someone else's purchase, ask: does this move me
toward my own goals? If not, let it go. You're running your own race.""",
"Office parking lot luxury cars", "THE PARKING LOT",
"Person walking alone confidently", "OPT OUT",
"Running track lane", "RUN YOUR OWN RACE")

item(12, "They think in decades", "long term thinking",
"""Four o'clock. Moment number twelve. A market headline says stocks dropped. They barely react.""",
"""Market drops are normal. Broad stock markets have fallen significantly many times in history, and have
historically recovered over long periods, though there are no guarantees and recovery can take years.
Millionaires who built wealth through investing usually learned to ignore daily noise.""",
"""Their mindset is measured in decades, not days. A bad Tuesday on the market is a footnote in a thirty
year plan. Many keep investing through drops, which means they buy more shares when prices are lower. That
patience is one of the biggest advantages ordinary investors have.""",
"""Copy it tomorrow. Turn off stock price notifications on your phone. Check your investments once a month
or once a quarter, not once a day. And decide now what you'll do in a crash, which for most long term
investors is: keep investing.""",
"Stock market red screen", "STOCKS DROPPED",
"Calendar decades concept", "THINK IN DECADES",
"Phone notifications off", "TURN OFF THE NOISE")

item(13, "They protect their health", "the walk after work",
"""Five thirty. Moment number thirteen. A walk, a run or the gym.""",
"""Corley's survey reported that most of the wealthy people he interviewed exercised regularly. Again,
a small survey. But the link between health and wealth shows up elsewhere too. Good health means fewer
medical bills, fewer missed workdays, and more years of earning and enjoying your money.""",
"""Exercise also helps with stress, and stress is expensive. Stressed people tend to make more impulsive
money decisions. A daily walk is one of the cheapest investments you can make, with returns in energy, mood
and focus.""",
"""Copy it tomorrow. Take a twenty minute walk after work. No equipment, no gym membership needed. If you
like company, invite a friend or family member. Health is a form of wealth that money can't buy back.""",
"Person jogging in park evening", "THE DAILY WALK",
"Doctor checkup clinic", "FEWER MEDICAL BILLS",
"Two friends walking together", "20 MINUTES")

pr("""That's angle two. Owners, not just employees. Income as a tool. No to most pitches. No status games.
Decades, not days. And health as wealth. Now angle three. The playbook. The evening and night, where a lot of
the real wealth building happens.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook (evening)")
sc("""The evening is when most people are tired and on autopilot. That's exactly why it's such a powerful
time to build better habits. A few small routines between six p.m. and bedtime can add up to a
completely different financial life over ten or twenty years.""",
   "City at dusk lights coming on", "THE EVENING")

item(14, "Dinner at home with family", "cheap and valuable",
"""Six thirty. Moment number fourteen. Dinner at home, with family.""",
"""Restaurant meals and delivery add up fast. Many millionaires eat most dinners at home. Not because
they can't afford restaurants, but because home dinners are cheaper, healthier, and give them time with
the people they care about.""",
"""Dinner is also when many families talk about money. Stanley found that millionaires often taught their
kids about money early, including saving, budgeting and the value of work. Those conversations can shape
a child's financial habits for life.""",
"""Copy it tomorrow. Plan four home dinners this week. Keep them simple. And at one of them, ask a money
question. What would you do with a hundred dollars? How do you think people get rich? It's a great way to
start the conversation.""",
"Family dinner at kitchen table", "DINNER AT HOME",
"Parent and child counting coins", "TEACHING KIDS",
"Simple home meal", "FOUR DINNERS A WEEK")

item(15, "Screens off, books on", "the TV gap",
"""Seven thirty. Moment number fifteen. The TV gap.""",
"""According to the Bureau of Labor Statistics' American Time Use Survey, watching TV is the top leisure
activity for Americans, at close to three hours a day on average. That's around twenty hours a week. Add
social media and phones, and many evenings simply disappear.""",
"""Warren Buffett has said he spends a large part of each day reading. Bill Gates is famous for reading
dozens of books a year. You don't need to match them. But swapping even thirty minutes of TV for reading or
learning, five nights a week, adds up to more than one hundred twenty hours a year.""",
"""Copy it tomorrow. Set a simple rule. Thirty minutes of reading or learning before any TV. Keep a book on
the couch where the remote usually sits. It's a small change with a surprisingly big payoff over the years.""",
"Family watching television", "3 HOURS OF TV A DAY",
"Person reading book on couch", "READ FIRST",
"Book next to TV remote", "30 MINUTES")

item(16, "A side project", "building something",
"""Eight fifteen. Moment number sixteen. Working on something of their own.""",
"""Many millionaires built their wealth through a business, and many started that business on the side,
in the evenings. A side project can be a small online store, freelance work, a skill they're developing,
or a rental property they manage.""",
"""Not every side project becomes a business. But even small ones build skills, create a second income
stream, and give you options if your main job changes. And the income from a side project can go straight
into investments, speeding everything up.""",
"""Copy it tomorrow. Pick one evening a week for a side project. Start with something low cost that uses
a skill you already have. Track every dollar you earn from it and invest most of it.""",
"Person working laptop at night", "SOMETHING OF YOUR OWN",
"Small online shop packages", "A SECOND STREAM",
"Notebook with business ideas", "ONE EVENING A WEEK")

item(17, "Money talk with their partner", "on the same team",
"""Nine o'clock. Moment number seventeen. A quick money conversation with their partner.""",
"""Money is one of the most common sources of conflict in relationships. Couples who talk about money
regularly, set shared goals and make big decisions together tend to have fewer fights about it. Stanley found
that many millionaires described their spouse as a key partner in building wealth.""",
"""It doesn't have to be a big meeting. A few minutes to check in. Any big expenses coming up? Are we on
track with savings? Anything we want to change? Small regular conversations prevent big blowups.""",
"""Copy it tomorrow. Pick one evening a week for a ten minute money check in with your partner. Keep it
positive. Start with a win, then talk about what's coming up. If you're single, do it with yourself, in a
notebook.""",
"Couple talking on couch", "ON THE SAME TEAM",
"Couple planning with laptop", "SHARED GOALS",
"Notebook money check in", "10 MINUTES A WEEK")

item(18, "Tomorrow planned tonight", "a calm start",
"""Nine thirty. Moment number eighteen. Planning tomorrow.""",
"""Many successful people spend a few minutes each evening planning the next day. What are the three most
important things? What's for lunch? What's on the calendar? This simple habit reduces stress and helps
avoid expensive last minute decisions.""",
"""Last minute decisions are often expensive ones. The rushed breakfast bought on the way to work, the
forgotten bill that becomes a late fee, the unplanned dinner that turns into delivery. A little planning
the night before prevents a lot of small, costly mistakes.""",
"""Copy it tomorrow. Before bed, write down three priorities for tomorrow and pack your lunch. Five minutes.
You'll wake up with a plan instead of a scramble.""",
"To do list on desk at night", "PLAN TOMORROW",
"Rushed person grabbing breakfast", "LAST MINUTE COSTS",
"Notebook with three priorities", "THREE PRIORITIES")

item(19, "Gratitude, not envy", "enough is a number",
"""Ten o'clock. Moment number nineteen. A moment of gratitude.""",
"""Many wealthy people talk about the idea of enough. Knowing what's enough for you protects you from
endless spending, because there's always a bigger house or a newer car. Researchers who study well being
have found that gratitude is linked with greater life satisfaction.""",
"""Gratitude also fights the envy that drives so much spending. When you appreciate what you have, you
need less to feel good. That's not just good for your mood. It's good for your bank account.""",
"""Copy it tomorrow. Before bed, write down three things you're grateful for that don't cost money. It
takes two minutes, and over time it changes how you think about wanting more.""",
"Person writing in journal at night", "GRATITUDE",
"Peaceful home evening", "WHAT IS ENOUGH?",
"Journal with three lines", "THREE THINGS")

item(20, "Sleep", "the most underrated asset",
"""Ten thirty. Moment number twenty. Lights out.""",
"""Sleep sounds like it has nothing to do with money. But tired people make worse decisions, including
financial ones. Research has linked sleep deprivation with poorer judgment and more impulsive choices. The
Centers for Disease Control and Prevention says about a third of American adults don't get enough sleep.""",
"""A good night's sleep helps you focus at work, resist late night online shopping, and handle stress
without spending to cope. Many successful people protect their sleep as carefully as their savings.""",
"""Copy it tomorrow. Set a consistent bedtime and put your phone away thirty minutes before it. Late night
scrolling is when a lot of impulse shopping happens. Protect your sleep, and you protect your wallet.""",
"Bedroom at night lamp off", "LIGHTS OUT",
"Tired person at desk", "TIRED DECISIONS",
"Phone charging away from bed", "PHONE AWAY")

# ---------------- Day math ----------------
ch("What one Tuesday adds up to")
pr("""So what does one Tuesday really add up to? On its own, not much. That's the secret.""")
sc("""One Tuesday of packing lunch saves a few dollars. One evening of reading teaches you a few pages. One
automatic transfer moves a small amount. On their own, these moments look meaningless. But a year has fifty
two Tuesdays, and a career has about two thousand of them. Repeat those small choices two thousand times, and
the result is a completely different life.""",
   "Calendar pages flying", "2,000 TUESDAYS")
card("""Here's the money side. If these habits free up five hundred dollars a month, and you invest it at
a seven percent average yearly return, after thirty years that's roughly six hundred ten thousand
dollars.""",
     {"type": "growth", "monthly": 500, "rate": 0.07, "years": 30})
sc("""And that's just the money you saved. Add the raises from the skills you built in all those commutes,
the side income from those evenings, and the health from those walks, and it's easy to see how ordinary people
end up as quiet millionaires. Not through one big moment. Through thousands of small ones.""",
   "Mountain path with footprints", "THOUSANDS OF SMALL MOMENTS")

# ---------------- Real people ----------------
ch("Real quiet millionaires")
pr("""Does this kind of Tuesday really make millionaires? Let me tell you about a few real people.""")
sc("""Ronald Read worked as a gas station attendant and later as a janitor in Brattleboro, Vermont. He
lived simply, drove an old car and was known for his modest habits. When he died in twenty fourteen, people
discovered he had built a fortune of around eight million dollars, mostly by buying shares of well known
companies and holding them for decades. He left millions to his local hospital and library.""",
   "Small town Vermont main street", "RONALD READ")
sc("""Grace Groner was a secretary at Abbott Laboratories near Chicago. In nineteen thirty five, she bought
three shares of Abbott stock for one hundred eighty dollars. She never sold. She reinvested the dividends,
lived in a small one bedroom house, and bought her clothes at rummage sales. When she died in twenty ten, her
stock was worth about seven million dollars, which she left to her college, Lake Forest College.""",
   "Lake Forest College campus", "GRACE GRONER")
sc("""And then there's Warren Buffett, one of the richest people in the world, who still lives in the Omaha
house he bought in nineteen fifty eight. In the documentary Becoming Warren Buffett, he described stopping at
McDonald's on his drive to work and choosing breakfast based on how the market was doing that day, spending
just a few dollars.""",
   "Omaha Nebraska skyline", "WARREN BUFFETT")
sc("""None of these people had a glamorous Tuesday. They had a patient one. They spent less than they earned,
invested the difference in things they understood, and gave time the chance to work. Their stories are
extreme, but the habits behind them are available to anyone.""",
   "Old photo album pages", "A PATIENT TUESDAY")

# ---------------- Contrast ----------------
ch("The other Tuesday")
sc("""Now picture the other Tuesday. The alarm goes off late. No time for breakfast, so it's a drive through
on the way to work in a car with a seven hundred dollar payment. Lunch is bought. A flash sale gets a quick
click. The evening is three hours of TV and scrolling, a delivery dinner, and a late night of online shopping.
The paycheck is gone before the next one arrives.""",
   "Fast food drive through morning", "THE OTHER TUESDAY")
sc("""Nobody on that Tuesday is doing anything terrible. That's what makes it so common. Each choice is
reasonable on its own. But two thousand of those Tuesdays lead to a very different place than two thousand of
the millionaire's Tuesdays. The difference was never one big decision. It was always the small ones.""",
   "Two roads diverging", "TWO DIFFERENT PLACES")
sc("""The good news is you don't have to switch everything at once. Try changing just three moments. One from
the morning, one from the workday, one from the evening. Next month, add three more. Within a year, your
Tuesday can look a lot like the millionaire's, whatever your income is today.""",
   "Person smiling morning coffee", "THREE MOMENTS AT A TIME")

# ---------------- Monthly ----------------
ch("Bonus: the once a month moments")
pr("""A normal Tuesday is built on daily habits. But millionaires also have a few moments that happen once a
month or once a year. Here are the big ones.""")
sc("""Once a month, many wealthy people do a money review. They look at net worth, savings rate and any
changes in spending. It takes maybe half an hour. They ask simple questions. Did we spend what we planned?
Did anything surprise us? Is there a subscription or fee we can cut? Is our savings rate going up or
down?""",
   "Monthly calendar review", "THE MONTHLY REVIEW")
sc("""Once a year, they do a bigger checkup. Insurance policies, beneficiaries on retirement accounts, the
investment mix, and goals for the next year. Many also review their tax situation before the year ends,
looking for things like maxing out retirement contributions. These annual reviews catch problems before they
become expensive.""",
   "Annual planning documents", "THE YEARLY CHECKUP")
sc("""And whenever they get a raise, they follow a simple rule. Before any lifestyle upgrade, they increase
their automatic saving. Many save at least half of every raise. That single habit is one of the most
powerful ways to build wealth, because your lifestyle never catches up with your income, and the gap keeps
growing year after year.""",
   "Salary increase letter", "SAVE HALF THE RAISE")
sc("""Finally, many give. Studies of wealthy households, and Stanley's research, found that many
millionaires give regularly to charity, their church, or causes they care about. Giving keeps money in
perspective. It's a reminder that money is a tool for a good life, not the goal itself.""",
   "Volunteers at food bank", "GIVING")

# ---------------- Mistakes ----------------
ch("Mistakes when copying the routine")
sc("""A word of warning. When people see a routine like this, they often try to copy everything on day one.
Up at five, no coffee out, no TV, side project every night, reading an hour a day. By Friday, they've quit.
Big overnight changes rarely last. Small changes that stack up over months usually do.""",
   "Exhausted person at desk", "DON'T COPY EVERYTHING AT ONCE")
sc("""The second mistake is copying the look instead of the habit. Buying a fancy planner, an expensive
water bottle and a gym membership feels like progress, but it's just more spending. The habits on this list
are almost all free. Start with the free ones.""",
   "Expensive planner and gadgets", "COPY THE HABIT, NOT THE LOOK")
sc("""And the third mistake is comparing your chapter one with someone else's chapter twenty. A fifty five
year old millionaire's Tuesday is the result of thirty years of habits. Yours is just getting started. Judge
your progress against last year's version of you, not against someone further down the road.""",
   "Book with chapters open", "YOUR CHAPTER ONE")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. Do all millionaires live like this? No. Some are flashy, some inherited their money, and
some got lucky. But research like Stanley's and Ramsey's suggests that the typical American millionaire is
self made and lives below their means, much like the Tuesday we just walked through.""",
   "Diverse group of professionals", "ALL MILLIONAIRES?")
sc("""Question two. I work nights or shifts. Does this still apply? Absolutely. The clock times don't matter.
What matters are the moments. Automatic saving, food on purpose, learning while you travel, a daily walk, time
with family, and protecting your sleep. Fit them into your own schedule.""",
   "Night shift worker hospital", "SHIFT WORK?")
sc("""Question three. How long does it take to become a millionaire this way? It depends on your income,
your savings rate and market returns, which aren't guaranteed. Ramsey's study reported that the average age
at which those millionaires reached a million dollars was around forty nine. For most, it was a long, steady
journey, not a sprint.""",
   "Hourglass and coins", "HOW LONG IT TAKES")
sc("""Question four. Should I wake up at five like some successful people? Only if it suits you. There's no
magic in the hour itself. What matters is having some time each day that you control, whether that's early
morning, lunch, or late evening. Use that time for things that grow, like learning, exercise, or a side
project.""",
   "Alarm clock early morning", "UP AT FIVE?")
sc("""Question five. What if my partner doesn't want to change? Start with yourself and share results, not
lectures. Bring lunch, track what you save, and show the number after a month. Progress is persuasive. And
when you do talk, focus on goals you both want, like a vacation, a house, or less stress.""",
   "Couple cooking together", "IF YOUR PARTNER WON'T CHANGE")
sc("""Question six. Which single moment matters most? If you only copy one, copy the first one. Money
moved automatically before you wake up. It's the habit behind almost every quiet millionaire story, it takes
ten minutes to set up, and after that it works every single Tuesday without asking anything of you. Every
other moment on this list makes it stronger, but that one is the foundation.""",
   "Foundation of house construction", "THE ONE THAT MATTERS MOST")

# ---------------- Recap ----------------
ch("Recap: the 20 moments")
sc("""Quick recap. Angle one, the numbers, the morning. Money moved automatically, coffee at home, a paid off
car, a commute that teaches, lunch from home, knowing their numbers, and no impulse buys.""",
   "Morning sunrise city", "THE MORNING: 1 TO 7")
sc("""Angle two, the psychology, the workday. Thinking like owners, treating income as a tool, saying no to
most pitches, ignoring status games, thinking in decades, and protecting their health.""",
   "Office building afternoon", "THE WORKDAY: 8 TO 13")
sc("""Angle three, the playbook, the evening. Dinner at home, screens off and books on, a side project, money
talk with their partner, planning tomorrow, gratitude, and sleep.""",
   "City lights at night", "THE EVENING: 14 TO 20")

# ---------------- Close ----------------
ch("What to do next")
pr("""Here's the thing I love about this. You don't need a lucky break, a rich family or a genius idea to
live a millionaire's Tuesday. You just need a few good defaults, repeated for a long time, with the patience to let them work while
everybody else is chasing something faster. Tomorrow is a
normal day for you, too. Pick three moments from this video and try them. If you want the
full plan for turning ordinary days into real wealth, it's in my playbook, linked in the description. Tell me
in the comments which moment you're starting with. I'm Ryan Rover. See you in the next one.""")

save("video24", "How Millionaires Spend a Normal Tuesday", [
    "Ramsey Solutions, National Study of Millionaires (79% received no inheritance; most common careers; about 8 in 10 invested in their company retirement plan; average age reaching $1M about 49)",
    "Thomas J. Stanley and William D. Danko, The Millionaire Next Door (1996); Thomas J. Stanley, Stop Acting Rich (2009): median vehicle price about $31,000",
    "US Bureau of Labor Statistics, American Time Use Survey (TV is the top leisure activity, close to 3 hours a day)",
    "Edmunds, average new-vehicle monthly payment (above $700)",
    "Tom Corley, Rich Habits survey (small, self-reported sample)",
    "Federal Trade Commission, Consumer Sentinel fraud reports (investment scams among the costliest)",
    "Centers for Disease Control and Prevention, about 1 in 3 US adults don't get enough sleep",
    "Growth examples: monthly compounding at 7% average yearly return (illustration, not a promise)",
], "a millionaire's normal Tuesday, from 3 angles: numbers (morning), psychology (workday), playbook (evening)")
