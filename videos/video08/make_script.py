import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short


def thing(n, title, sub, card_text, body, example, q1, c1, q2, c2):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"CHANGE {n}")
    sc(body, q1, c1)
    sc(example, q2, c2)

# ---------------- Intro ----------------
ch("Intro")
short("Here's what happens when you finally stop living paycheck to paycheck.")
pr("""Hi, I'm Ryan Rover. Living paycheck to paycheck is exhausting. Counting days until payday. Checking your balance
before buying groceries. Feeling your stomach drop when an unexpected bill shows up. And it's incredibly common. But here's
what almost nobody talks about: what actually changes when you finally break out of it. Because it's a lot more than just
having some money in the bank.""")
card("""Paycheck to paycheck means that when the next paycheck arrives, the last one is already gone. No buffer. No cushion.
Every dollar spoken for.""",
     {"type": "stat", "label": "paycheck to paycheck", "big": "$0", "sub": "left when the next paycheck lands"})
sc("""Surveys by groups like LendingClub and PYMNTS have repeatedly found that a majority of Americans say they live paycheck
to paycheck, including many people earning six figures. It's not only a low income problem. It's a gap problem. When
spending rises to meet income, any income can feel too small.""",
   "Empty wallet", "A MAJORITY OF AMERICANS")
sc("""Today, twenty five things that change when you stop living paycheck to paycheck. Some are about money. Some are about
your health, your relationships and the way you think. And we'll look at the whole thing from three angles. The numbers,
meaning what living on the edge actually costs. The psychology, meaning what it does to your brain. And the playbook,
meaning exactly how to get out.""",
   "Calculator with financial charts", "25 CHANGES, 3 ANGLES")
pr("""If you're living paycheck to paycheck right now, this video is a picture of what's waiting on the other side. And if
you've already escaped, it's a reminder of why it's worth staying out. Let's
start with the sources.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our numbers come from named sources. Household savings data comes from the Federal Reserve's survey on the economic
well being of U.S. households. Payday loan and overdraft information comes from the Consumer Financial Protection Bureau.
Credit score information comes from FICO. And the research on how money stress affects thinking comes from economist Sendhil
Mullainathan and psychologist Eldar Shafir. This video is education, not financial advice.""",
   "Federal Reserve Bank building columns", "OUR SOURCES")

# ---------------- Angle 1: numbers ----------------
ch("Angle 1: The numbers")
pr("""Angle one. The numbers. Living paycheck to paycheck isn't just stressful. It's expensive. Being broke costs money.
Here's how.""")
card("""The Consumer Financial Protection Bureau has reported that overdraft fees have typically been around thirty five
dollars. And a typical payday loan fee of fifteen dollars per one hundred borrowed works out to an annual rate of almost four
hundred percent.""",
     {"type": "compare", "left": {"label": "Overdraft fee", "big": "~$35", "sub": "each time"},
      "right": {"label": "Payday loan", "big": "~400%", "sub": "APR at $15 per $100"},
      "note": "Consumer Financial Protection Bureau"})
sc("""Think about what that means. A twenty dollar purchase that overdraws your account can end up costing fifty five
dollars. A three hundred dollar payday loan for two weeks can cost forty five dollars in fees, and if you roll it over, much
more. These costs fall hardest on people with the least room. That's the cruel math of living on the edge.""",
   "ATM machine", "BROKE IS EXPENSIVE")
sc("""Then there's the credit card. When there's no cushion, every surprise goes on a card, often at interest rates above
twenty percent, according to the Federal Reserve. A one thousand dollar emergency, paid off slowly with minimum payments, can
cost hundreds of dollars in interest and take years to clear. Meanwhile, the next surprise is already on its way.""",
   "Credit card close up", "THE CARD BECOMES THE CUSHION")
sc("""And there are hidden costs too. Late fees on bills. Higher insurance premiums when you can only afford to pay monthly.
Buying small packages at higher unit prices because you can't afford the bulk size. Reconnection fees. Each one is small.
Together, they can add up to hundreds or even thousands of dollars a year, a tax on not having a buffer.""",
   "Receipt and coins on table", "THE TAX ON NO BUFFER")
card("""The Federal Reserve found that sixty three percent of adults would cover a surprise four hundred dollar expense with
cash or its equivalent. Which means more than a third would have to borrow, sell something, or couldn't cover it at all.""",
     {"type": "stat", "label": "would cover $400 with cash", "big": "63%", "sub": "Federal Reserve, 2025 survey"})
sc("""Here's the good news hidden in all of that. Because being broke is so expensive, getting even slightly ahead saves you
money immediately. The first one thousand dollars you keep doesn't just sit there. It stops the fees, the interest and the
penalties. In a real sense, a small emergency fund can earn a better return than almost any investment, because of all the
costs it prevents.""",
   "Piggy bank coins", "THE FIRST $1,000 PAYS YOU")
pr("""So, twenty five things that change when you break the cycle. The first few show up within weeks.""")

# ---------------- Items ----------------
thing(1, "Groceries stop being scary", "no more balance checks at the register",
"""Change number one. You stop checking your balance before buying groceries.""",
"""This is the first thing many people notice. The little calculation in your head at the checkout disappears. You stop
putting items back. You stop praying the card goes through. It sounds small, but it's a daily stress that quietly drains
your energy, and when it's gone, you feel lighter.""",
"""People who've made this shift often describe it as the first moment they realized something had changed. Not a big
purchase. Not a celebration. Just a normal Tuesday at the store, and no fear. That's what a cushion feels like in real life.""",
"Grocery store shelves prices", "NO MORE FEAR AT CHECKOUT",
"Person smiling grocery shopping", "A NORMAL TUESDAY")

thing(2, "Overdraft fees disappear", "around $35 each, gone",
"""Change number two. Overdraft fees disappear.""",
"""When there's always a buffer in your checking account, you stop overdrawing. Every overdraft fee you don't pay is money
back in your pocket. For people who used to overdraw a few times a month, that can mean over a thousand dollars a year
saved.""",
"""Try this: keep a minimum buffer in checking, like one hundred or two hundred dollars, that you treat as zero. Set a low
balance alert just above it. And if your bank allows it, turn off overdraft coverage entirely, so a purchase gets declined
instead of costing thirty five dollars.""",
"ATM machine", "NO MORE OVERDRAFTS",
"Online banking smartphone app", "A BUFFER YOU TREAT AS ZERO")

thing(3, "Late fees vanish", "bills paid on time, every time",
"""Change number three. Late fees vanish.""",
"""When money is tight, bills get paid in the order they scream. Some end up late. Late fees on credit cards, utilities,
rent and phone bills can each cost twenty five to forty dollars or more. With a cushion, you can pay everything on time,
regardless of when your paycheck lands.""",
"""Once you're ahead, put every bill on autopay. Because the money is there, autopay stops being risky and becomes a time
saver. You don't have to remember due dates anymore. The system just runs.""",
"Paperwork documents desk", "NO MORE LATE FEES",
"Clock gears mechanism", "AUTOPAY EVERYTHING")

thing(4, "No more payday loans", "the 400% trap closes",
"""Change number four. You never need a payday loan or a cash advance again.""",
"""Payday loans are designed for people with no buffer. The fees are high, and the Consumer Financial Protection Bureau has
found that many borrowers roll their loans over again and again, paying fees each time. A small emergency fund closes that
trap permanently.""",
"""If you're currently stuck in payday loans, the way out is to build a small fund while paying them down, even a few
hundred dollars. Some credit unions also offer small, lower cost loans as an alternative. Every step away from those fees is
money you keep.""",
"Pawn shop sign", "THE TRAP CLOSES",
"Bank building United States", "CREDIT UNIONS CAN HELP")

thing(5, "Your credit score climbs", "on-time payments matter most",
"""Change number five. Your credit score starts to climb.""",
"""According to FICO, payment history is the biggest factor in a FICO score, about thirty five percent. When you pay every
bill on time and stop maxing out credit cards, your score tends to rise. Lower credit card balances relative to your limits
also help.""",
"""A higher score means lower interest rates on car loans, mortgages and credit cards. On a large mortgage, a better rate can
save tens of thousands of dollars over the life of the loan. So getting off the paycheck to paycheck treadmill doesn't just
save fees. It makes every future loan cheaper.""",
"Credit report document", "PAYMENT HISTORY: ~35%",
"House with for sale sign", "CHEAPER LOANS")

thing(6, "You sleep better", "money stress is real stress",
"""Change number six. You sleep better.""",
"""The American Psychological Association's Stress in America surveys have consistently found money to be one of the most
common sources of stress for Americans. Money worries follow people to bed. They lie awake running numbers. With a cushion,
that late night math stops.""",
"""People who build their first emergency fund often say the biggest change wasn't financial. It was sleep. It was not
feeling anxious every time the phone rang. You can't put a price on that, but it may be the most valuable thing on this whole
list.""",
"Person sleeping peacefully", "BETTER SLEEP",
"Bedroom night", "NO MORE MIDNIGHT MATH")

thing(7, "Fewer money fights", "calmer relationships",
"""Change number seven. You fight less about money.""",
"""Money is one of the most common sources of conflict for couples, and stress makes every disagreement sharper. When every
dollar is tight, every purchase becomes a negotiation. With a buffer, small spending decisions stop feeling like threats.""",
"""Try this: once you have some breathing room, set up a monthly money date with your partner. Twenty minutes. Look at the
numbers together, celebrate progress, and agree on the next goal. Couples who talk about money regularly tend to fight about
it less.""",
"Couple cooking together kitchen", "FEWER FIGHTS",
"Calendar planning", "A MONTHLY MONEY DATE")

thing(8, "Payday stops mattering", "bills on your schedule, not the calendar's",
"""Change number eight. Payday stops being the most important day of the month.""",
"""When you live paycheck to paycheck, your whole life revolves around payday. Bills get timed around it. Plans get timed
around it. Once you're a full month ahead, payday is just a day. Your paycheck refills the tank, but you're never running on
empty.""",
"""Many people aim to get one full month ahead, so this month's spending is paid from last month's income. It's one of the
most freeing setups in personal finance. Start by building a buffer of a few hundred dollars, and grow it until it equals a
full month of spending.""",
"Calendar planning", "PAYDAY IS JUST A DAY",
"Online banking smartphone app", "ONE MONTH AHEAD")

thing(9, "You buy at better prices", "bulk, sales and timing",
"""Change number nine. You start paying lower prices for the same things.""",
"""With a buffer, you can buy the big pack instead of the small one, stock up when prices drop, and wait for a sale instead
of buying the moment something runs out. Unit prices on bigger packages are often noticeably lower.""",
"""This works for more than groceries. You can buy a reliable used car with cash instead of financing a worse one. You can
replace a broken appliance with a durable one, instead of the cheapest option available today. Having money lets you make
decisions based on value, not desperation.""",
"Warehouse store aisles", "BETTER PRICES",
"Store sale sign", "VALUE, NOT DESPERATION")

thing(10, "Insurance gets cheaper", "pay yearly, raise deductibles",
"""Change number ten. Your insurance can get cheaper.""",
"""Many insurers charge less if you pay your premium in full upfront, rather than monthly. And with an emergency fund, you
can choose a higher deductible on car or home insurance, which usually lowers your premium. You're taking on a bit more risk
yourself, because now you can afford to.""",
"""Try this: ask your insurer how much you'd save by paying annually and by raising your deductible. Make sure your emergency
fund can comfortably cover the deductible. For many people, these two changes together save a meaningful amount every
year.""",
"Car insurance documents", "CHEAPER INSURANCE",
"Phone call customer service", "ASK YOUR INSURER")

short("A car repair can be a crisis or a minor annoyance. The difference is one thing.")
thing(11, "Car trouble is just annoying", "not a financial emergency",
"""Change number eleven. A car breakdown becomes an annoyance, not a crisis.""",
"""When you live paycheck to paycheck, a six hundred dollar car repair can set off a chain reaction. You can't get to work,
you put the repair on a card, you fall behind on another bill. With a cushion, you pay the mechanic, refill the fund, and
move on.""",
"""This is exactly what an emergency fund is for. It doesn't prevent bad luck. It stops bad luck from turning into debt.
Every surprise you handle with cash instead of credit is a small victory that keeps your progress intact.""",
"Car repair garage mechanic", "AN ANNOYANCE",
"Car with flat tire on road", "NO CHAIN REACTION")

thing(12, "You can say no", "to bad jobs and bad deals",
"""Change number twelve. You can say no.""",
"""No to a boss who treats you badly. No to a high pressure sales pitch. No to a friend's loan request you can't afford. When
you have nothing saved, you often can't afford to say no. Savings give you the power to walk away.""",
"""Some people call this a freedom fund. Even a few months of expenses saved can change how you show up at work. You can
negotiate more confidently, because you're not terrified of losing everything. That confidence alone can lead to better pay.""",
"Person standing at crossroads", "THE POWER OF NO",
"Business meeting handshake", "NEGOTIATE WITH CONFIDENCE")

thing(13, "You can chase better opportunities", "a move, a course, a new job",
"""Change number thirteen. You can take a chance on something better.""",
"""A better job in another city. A training course that pays off next year. A new role with a short gap between jobs.
Opportunities often require a little money upfront, or a short period without income. Without savings, people stay stuck.
With them, they can take the leap.""",
"""Think of your savings as an opportunity fund, not just an emergency fund. Some of the biggest income jumps people make
happen because they had enough cushion to take a risk that others couldn't afford.""",
"Moving truck boxes", "TAKE THE LEAP",
"Graduation cap diploma", "AN OPPORTUNITY FUND")

thing(14, "Credit cards become a tool", "not a lifeline",
"""Change number fourteen. Credit cards stop being your emergency fund.""",
"""When a card is your only backup, every emergency adds debt at high interest. Once you have savings, you can use a card for
convenience and rewards, and pay it in full every month. The card goes from a trap to a tool.""",
"""If you're carrying credit card debt right now, the path is to build a small cushion first, then attack the card balance,
highest interest rate first. When the balance hits zero, keep paying it in full every month, and never let it carry over
again.""",
"Credit card close up", "FROM TRAP TO TOOL",
"Scissors cutting credit card", "PAY IN FULL")

thing(15, "Interest starts working for you", "instead of against you",
"""Change number fifteen. Interest starts working for you instead of against you.""",
"""When you live paycheck to paycheck, you pay interest: on cards, on loans, on cash advances. Once you have savings, you can
earn interest instead. A high yield savings account at an online bank or credit union often pays far more than a traditional
savings account, though rates change over time.""",
"""It's a complete reversal. Instead of paying twenty percent to a credit card company, you're earning a few percent from a
bank. On a ten thousand dollar emergency fund, that can mean a few hundred dollars a year. Not life changing, but it's the
first time money is paying you.""",
"Bank building United States", "INTEREST FOR YOU",
"Coins in jar", "MONEY THAT PAYS YOU")

pr("""Quick pause. If you're living paycheck to paycheck right now, or you just got out, I'd love to hear your story in the
comments. And if this video is helping, subscribe. I make videos like this every couple of days, and subscribing is the best
way not to miss the next one. Now, change number sixteen.""")

thing(16, "You start investing", "the next level unlocks",
"""Change number sixteen. You can finally start investing.""",
"""Investing money you might need next month is risky, because markets can fall right when you need the cash. But once you
have a real emergency fund, you can invest for the long term without that fear. That's when wealth building really begins.""",
"""At a seven percent illustration, investing two hundred dollars a month for thirty years could grow to roughly two hundred
forty four thousand dollars. That's what becomes possible when you're no longer living on the edge. The cushion is the
foundation. Investing is what you build on top.""",
"New York Stock Exchange trading floor", "INVESTING UNLOCKS",
"Graph trending upward", "$200 A MONTH x 30 YEARS")

thing(17, "You get the full employer match", "free money you used to miss",
"""Change number seventeen. You can grab the full employer match.""",
"""Many people living paycheck to paycheck skip their workplace retirement plan, or contribute less than the match, because
they need every dollar now. Once you have breathing room, you can contribute enough to get every matching dollar. That's an
instant return on your money.""",
"""A common formula is fifty cents for every dollar you contribute, up to six percent of your pay. On a fifty thousand dollar
salary, that's fifteen hundred dollars a year of extra money from your employer. Missing it for years is one of the hidden
costs of living paycheck to paycheck.""",
"Office workers meeting", "FREE MONEY",
"Paperwork documents desk", "$1,500 A YEAR")

thing(18, "Your decisions get better", "scarcity steals brainpower",
"""Change number eighteen. You start making better decisions.""",
"""In their book Scarcity, Sendhil Mullainathan and Eldar Shafir describe how not having enough narrows your focus onto the
urgent problem in front of you, and leaves less mental bandwidth for everything else. In one study they discuss, simply
thinking about a big financial problem lowered people's performance on reasoning tests.""",
"""This means that getting out of paycheck to paycheck doesn't just give you more money. It gives you back mental space.
People make better long term choices when they're not constantly putting out fires. It's one of the most powerful and least
discussed benefits on this list.""",
"Person thinking by window", "SCARCITY STEALS BANDWIDTH",
"Chess game", "BETTER DECISIONS")

thing(19, "You plan in months, not days", "a longer horizon",
"""Change number nineteen. You start planning months ahead instead of days.""",
"""When money is tight, your planning horizon shrinks to the next paycheck. Once you have a buffer, you can think about next
quarter, next year, even the next decade. You can plan for holidays, car replacements and annual bills before they arrive.""",
"""Try sinking funds. Small separate savings for predictable but irregular costs, like car maintenance, gifts, annual
subscriptions or vacations. Divide the yearly cost by twelve and save that amount each month. When the bill comes, the money
is already waiting.""",
"Calendar planning", "A LONGER HORIZON",
"Jars with labels", "SINKING FUNDS")

thing(20, "Gaps in income stop being scary", "between jobs, slow months",
"""Change number twenty. Gaps in income stop being terrifying.""",
"""A layoff, a slow season, a few weeks between jobs, a reduction in hours. When you live paycheck to paycheck, any gap is
an emergency. With three to six months of essential expenses saved, a gap becomes a hard time instead of a disaster.""",
"""This matters most for people with irregular income, like freelancers, gig workers and anyone paid on commission. For
them, a bigger cushion turns unpredictable income into predictable spending. Many pay themselves a steady salary from a
separate account, and let the cushion absorb the ups and downs.""",
"Person working from home laptop", "GAPS ARE OKAY",
"Online banking smartphone app", "PAY YOURSELF A SALARY")

thing(21, "You can help people", "without hurting yourself",
"""Change number twenty one. You can help others without putting yourself at risk.""",
"""When someone you love needs help, it hurts to say no. When you're living on the edge, saying yes can sink you too. With a
cushion, you can decide how much you're able to give and give it freely, without wrecking your own plan.""",
"""Many people set a yearly giving budget once they're stable. Family, friends, charity. Knowing the number in advance makes
generosity easier, because you're not deciding under pressure. You're following a plan you made when you were calm.""",
"Family dinner table", "HELP WITHOUT RISK",
"Gift box present", "A GIVING BUDGET")

thing(22, "You see where your money goes", "patterns become visible",
"""Change number twenty two. You finally see where your money goes.""",
"""When you're scrambling, money disappears and you're not sure where. Once you're ahead, you have the calm to actually look.
And when people look, they often find surprises: subscriptions, fees, habits that quietly cost hundreds a month.""",
"""Try a once a month review. Look at your spending by category and ask one question about each: did this make my life better?
Keep what does. Cut what doesn't. That simple question often frees more money than any strict budget.""",
"Spreadsheet on laptop", "PATTERNS BECOME VISIBLE",
"Notebook with financial notes", "DID THIS MAKE LIFE BETTER?")

thing(23, "Your health can improve", "you stop delaying care",
"""Change number twenty three. You stop putting off things that matter for your health.""",
"""When money is tight, people often delay the dentist, skip a doctor's visit, or stretch out a prescription. Surveys by
groups like KFF have found that many adults skip or delay care because of cost. Small problems can become big ones.""",
"""With savings, you can handle the copay, the deductible, or the dental bill when it's needed, instead of waiting until it's
an emergency. Some people also use a health savings account, if their insurance plan allows it, to save for medical costs
with tax advantages.""",
"Doctor with stethoscope", "STOP DELAYING CARE",
"Hospital building exterior", "SAVE FOR HEALTH")

thing(24, "Your identity changes", "from broke to someone who keeps money",
"""Change number twenty four. You start seeing yourself differently.""",
"""People who break the paycheck to paycheck cycle often describe an identity shift. They stop thinking of themselves as bad
with money. They start thinking of themselves as someone who keeps money. And identity drives behavior. When you believe you're
a saver, you act like one.""",
"""This is why small wins matter so much early on. Every month you end with money left over is evidence. Evidence that you can
do it. Collect enough evidence, and the old story, I'm just bad with money, quietly stops being true.""",
"Person looking in mirror", "A NEW IDENTITY",
"Person smiling at laptop", "COLLECT EVIDENCE")

thing(25, "You get your time back", "the real prize",
"""Change number twenty five. The biggest one. You get your time and your attention back.""",
"""Living paycheck to paycheck takes constant mental energy. Juggling due dates, moving money around, worrying, calculating.
When that stops, you get hours of attention back every week. Attention you can spend on your family, your health, your work, or
building something new.""",
"""That's the real reason to break the cycle. Not to get rich. Not to buy more things. To get your life back from constant
money worry. And once you've done it, you can start aiming higher: not just out of paycheck to paycheck, but toward real
financial freedom.""",
"Family walking on beach", "YOUR TIME BACK",
"Sunrise over mountains", "THE REAL PRIZE")

# ---------------- Three stories ----------------
short("Three people broke the paycheck to paycheck cycle. Here's exactly how.")
ch("Three ways out")
pr("""Let's look at three example people who broke the cycle in three different ways. They're made up, but their numbers are
realistic, and you might see yourself in one of them.""")
sc("""Tanya earns thirty eight thousand dollars a year as a medical assistant. Every month ended at zero, plus two or three
overdraft fees. She turned off overdraft coverage, cancelled four subscriptions she wasn't using, and switched to a cheaper
phone plan. That freed about one hundred sixty dollars a month, plus the hundred dollars a month she'd been losing to fees.
Within four months, she had over one thousand dollars saved. For the first time in years, she ended a month with money
left.""",
   "Nurse in hospital corridor", "TANYA: STOP THE FEES")
sc("""Chris earns eighty five thousand dollars, and was still living paycheck to paycheck. A new truck payment, a big apartment,
and a lot of eating out. Chris didn't need more income. Chris needed a smaller gap. He moved to a cheaper apartment when his
lease ended and refinanced the truck loan. Together, those two decisions freed up about seven hundred dollars a month. A year
later, Chris had a full emergency fund and was investing for the first time.""",
   "Pickup truck parked", "CHRIS: CLOSE THE GAP")
sc("""Maya and Jordan, a couple with two kids and a combined income of sixty five thousand, had almost nothing left to cut. So
they focused on income. Jordan picked up weekend shifts for three months. Maya asked for a raise, with a list of what she'd
achieved, and got a modest one. They sent every extra dollar to a separate account. After six months, they had two thousand
five hundred dollars, and a plan to reach one month ahead by the end of the year.""",
   "Family relaxing at home", "MAYA AND JORDAN: EARN MORE")
sc("""Three different paths. Tanya stopped the fees. Chris closed the gap. Maya and Jordan earned more. But they all did three
things the same way: a separate account, an automatic transfer, and a rule that the transfer never stops. That's the core of
breaking the cycle. Everything else is choosing which path fits your life.""",
   "Three people silhouettes", "THREE PATHS, ONE CORE")

# ---------------- Myths ----------------
ch("Five myths about paycheck to paycheck")
pr("""Before the psychology, let's clear up five myths that keep people stuck.""")
sc("""Myth one. It only happens to people with low incomes. False. Surveys consistently find a meaningful share of six figure
earners say they live paycheck to paycheck. Spending rises to meet income. Myth two. You need a big raise to escape. Usually
not. Most people escape by closing the gap a little at a time, not by a single big jump in pay.""",
   "Office building at dusk", "MYTHS 1 AND 2")
sc("""Myth three. You have to give up everything fun. No. You need to choose your fun on purpose. Keep the things that really
matter to you, and cut the ones you barely notice. Myth four. Budgeting apps fix it. Apps can help you see your money, but
they don't move it. The automatic transfer is what actually changes the outcome.""",
   "Friends at restaurant", "MYTHS 3 AND 4")
sc("""And myth five. Once you're out, you're out forever. Not quite. Lifestyle creep can pull people right back in after a raise
or a big purchase. The protection is simple: keep the transfer running, send half of every raise to savings, and think twice
before adding any new monthly payment. Staying out is easier than getting out, but it still takes attention.""",
   "Luxury car dealership", "MYTH 5: OUT FOREVER")

# ---------------- Angle 2: psychology ----------------
short("Living paycheck to paycheck changes how your brain works. Here's the science.")
ch("Angle 2: The psychology")
pr("""Angle two. The psychology. Why is it so hard to break out, even when people know what to do? Because living on the edge
changes how you think.""")
sc("""Remember scarcity. When you're short on money, your brain focuses intensely on the immediate problem: this bill, this
week, this paycheck. Mullainathan and Shafir call it tunneling. It helps you survive the short term, but it pushes long term
decisions out of view. That's why saving feels impossible when you're broke. Your brain is busy putting out fires.""",
   "Tunnel light", "TUNNELING")
sc("""The second trap is the reward cycle. When life feels hard, small purchases feel like relief. A treat after a hard day.
A delivery dinner because you're exhausted. Each one is understandable, and each one makes the next paycheck tighter. The
fix isn't to never treat yourself. It's to choose your treats on purpose, and plan for them.""",
   "Food delivery bicycle", "THE REWARD CYCLE")
sc("""The third is comparison. Social media is full of vacations, new cars and renovations. It makes spending look normal and
saving look strange. But you're only seeing the purchases, not the debt behind them. Many of the people you're comparing
yourself to are living paycheck to paycheck too, just with nicer pictures.""",
   "Social media smartphone", "COMPARISON")
sc("""The fourth is hopelessness. When the gap feels too big, people stop trying. Why save twenty dollars when you need two
thousand? But this is where the math is on your side. Twenty dollars a week is over a thousand dollars a year. Small amounts,
repeated, break the cycle. Not overnight, but steadily.""",
   "Long road desert", "HOPELESSNESS")
sc("""And the fifth is the way out, and it's surprisingly simple. Make the right choice automatic, so your tired, stressed brain
doesn't have to make it. An automatic transfer on payday, before you see the money. A separate account you don't look at. Bills
on autopay. Systems beat willpower, especially when willpower is running low.""",
   "Clock gears mechanism", "SYSTEMS BEAT WILLPOWER")
sc("""And here's something hopeful from the same research on scarcity. The effects aren't permanent. When people get some slack,
some breathing room, their decision making tends to improve too. In other words, building a small cushion doesn't just protect
your wallet. It protects your mind, which then helps you make even better money decisions. It's a cycle, and once it starts
turning in your favor, it tends to keep going.""",
   "Sunrise over mountains", "SLACK HELPS THE MIND")

# ---------------- Angle 3: playbook ----------------
short("Here's a ninety day plan to stop living paycheck to paycheck.")
ch("Angle 3: The 90 day playbook")
pr("""Angle three. The playbook. Here's a simple ninety day plan to break the paycheck to paycheck cycle. It's an example, so
adjust the numbers to your life.""")
sc("""Days one to seven. Look at the last two months of your bank and card statements. Write down every regular bill and every
spending category. Cancel two or three subscriptions you don't use. Call one provider, like your phone or internet company, and
ask for a better rate. Open a separate savings account at a different bank. Set an automatic transfer on payday, even twenty
five dollars.""",
   "Person writing list notebook", "WEEK 1: SEE IT")
sc("""Days eight to thirty. Find your three biggest leaks. For many people, it's food delivery and eating out, impulse
shopping, and fees. Set a simple rule for each, like delivery twice a month, a thirty day wait on wants, and overdraft
protection turned off. Sell a few things you don't use. Every dollar you free up goes into the automatic transfer.""",
   "Garage sale items", "MONTH 1: PLUG THE LEAKS")
sc("""Days thirty one to sixty. Aim for your first five hundred dollars in the separate account. Put every bill on autopay
for at least the minimum, timed after payday. Start building a small buffer in checking that you treat as zero. If you have a
tax refund or bonus coming, decide now that most of it goes to the cushion.""",
   "Piggy bank coins", "MONTH 2: FIRST $500")
sc("""Days sixty one to ninety. Push toward one thousand dollars. Look for one income boost: a few extra hours, a small side
job, or a raise conversation. And when you reach one thousand, don't stop the transfer. Keep it running toward one full month
of expenses. That's the point where payday stops controlling your life.""",
   "Mountain climber reaching summit", "MONTH 3: $1,000")
sc("""Ninety days won't make you rich. But it can get you out of the danger zone, and give you a system that keeps working
long after the ninety days end. The most important thing isn't how fast you go. It's that the transfer never stops.""",
   "Sunrise over mountains", "THE TRANSFER NEVER STOPS")

# ---------------- Questions ----------------
ch("Questions people ask")
pr("""Let me answer the questions I hear most from people trying to break the cycle.""")
sc("""Question one. What if my income really is too low? Then the plan focuses more on earning and on protecting what you
have. Look into benefits you may qualify for, like tax credits for working families. Avoid high cost debt at all costs. And
look for ways to raise income, even slowly. Small cushions still matter, because they prevent fees that hit low incomes hardest.""",
   "Person studying laptop at night", "INCOME TOO LOW?")
sc("""Question two. Should I pay off debt or build savings first? Most people do both in stages: a small cushion first, around
five hundred to one thousand dollars, then attack high interest debt, then build the cushion further. Without that first
cushion, every surprise adds new debt and you never get ahead.""",
   "Credit card bills on table", "DEBT OR SAVINGS FIRST?")
sc("""Question three. I earn good money but I'm still living paycheck to paycheck. Why? Usually it's fixed costs: housing, cars,
and subscriptions that grew with your income. The fix is the same. Track spending, cut one big fixed cost, automate saving, and
send half of every raise to savings. Income doesn't fix a spending gap. Only the gap fixes the gap.""",
   "Luxury car dealership", "HIGH INCOME, STILL BROKE?")
sc("""Question four. How long does it take? It depends on your income and expenses, but many people can build a one thousand
dollar cushion in one to three months, and get one month ahead within a year. The first step is the hardest. After that, each
step gets easier, because the fees and interest you stop paying become money you can save.""",
   "Calendar planning", "HOW LONG DOES IT TAKE?")
sc("""Question five. Should I use a budgeting method like fifty thirty twenty? It can help as a starting point: roughly half of
your take home pay for needs, thirty percent for wants, and twenty percent for savings and debt. But if your needs take more
than half, which is common in expensive cities, don't feel like a failure. Start with whatever percentage you can save, and
grow it over time.""",
   "Pie chart on paper", "50/30/20?")
sc("""Question six. What if my partner doesn't want to change? Start with what you control, like your own spending and your own
transfer, and share your progress. Seeing a growing balance is often more persuasive than any argument. And frame it around
shared goals, like less stress, a trip together or a safer future for your kids, rather than cutting back.""",
   "Couple talking at table", "A PARTNER WHO RESISTS?")

# ---------------- Recap ----------------
ch("Recap: 25 changes")
sc("""Let's recap. The first changes show up fast: groceries stop being scary, overdraft fees disappear, late fees vanish, no
more payday loans, and your credit score climbs. Then the life changes: better sleep, fewer money fights, payday stops mattering,
better prices, cheaper insurance, and car trouble becomes just an annoyance.""",
   "Notebook with financial notes", "CHANGES 1 TO 11")
sc("""Then the power changes: you can say no, chase better opportunities, credit cards become a tool, interest works for you, you
start investing, and you get the full match. And finally the deep changes: better decisions, longer planning, calm during income
gaps, helping others, seeing where money goes, better health, a new identity, and your time back.""",
   "Mountain climber reaching summit", "CHANGES 12 TO 25")
sc("""And the three angles. The numbers: being broke is expensive, so the first thousand dollars pays you back immediately. The
psychology: scarcity narrows your focus, so make good choices automatic. And the playbook: ninety days, one transfer that never
stops.""",
   "Map and compass", "NUMBERS, PSYCHOLOGY, PLAYBOOK")
sc("""If you take one thing from this video, let it be this. Living paycheck to paycheck isn't a personal failure, and it isn't
permanent. It's a gap, and gaps can be closed. Sometimes by spending less, sometimes by earning more, usually by a bit of both.
Every one of the twenty five changes in this video starts with the same tiny step: keeping a little money that you don't spend.
Do it once, and you've started. Do it every payday, and one day you'll realize you haven't checked your balance at the grocery
store in months. That's the day you'll know you're out.""",
   "Grocery store shelves prices", "THE DAY YOU KNOW YOU'RE OUT")

# ---------------- Close ----------------
ch("What to do next")
pr("""So here's your homework. Open the separate account and set up the automatic transfer today. Even twenty five dollars. That
one step starts everything else on this list. Then pick one leak from this video, just one, and plug it this week. Next
week, pick another. In a few months, you won't recognize your bank account. If you want the full plan, it's in my playbook, link in the description. And
watch my video on the first ten thousand dollars next. I'm Ryan Rover. See you in the next one.""")

save("video08", "25 Things That Happen When You Stop Living Paycheck to Paycheck", [
    "Federal Reserve, Economic Well-Being of U.S. Households in 2025 (63% would cover a $400 expense with cash or its equivalent)",
    "Consumer Financial Protection Bureau, overdraft research (fees typically around $35) and What is a payday loan ($15 per $100 equals almost 400% APR)",
    "Federal Reserve G.19 Consumer Credit (credit card interest rates above 20%)",
    "FICO, What's in my FICO Scores (payment history about 35%)",
    "American Psychological Association, Stress in America surveys (money as a common source of stress)",
    "LendingClub and PYMNTS, paycheck-to-paycheck reports (a majority of U.S. consumers)",
    "KFF, polling on cost-related delays in health care",
    "Mullainathan and Shafir, Scarcity: Why Having Too Little Means So Much (2013)",
    "Compound growth: stated illustrative math at 7% average yearly return, compounded monthly",
], "25 things when you stop living paycheck to paycheck")
