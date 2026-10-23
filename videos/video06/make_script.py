import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short


def way(n, title, sub, card_text, body, example, q1, c1, q2, c2):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"WAY {n}")
    sc(body, q1, c1)
    sc(example, q2, c2)

# ---------------- Intro ----------------
ch("Intro")
short("The first ten thousand dollars is the hardest money you will ever save. Here are twenty ways.")
pr("""Hi, I'm Ryan Rover. The first ten thousand dollars is the hardest money you'll ever save. Harder than the
second ten thousand. Much harder than the tenth. Because at the beginning, you're doing everything with your
own hands. No growth, no momentum, no cushion. Just you, your paycheck, and a world that's very good at taking
your money.""")
card("""Ten thousand dollars. The first real milestone. It's the difference between one bad month ruining your
year, and one bad month being just a bad month.""",
     {"type": "stat", "label": "the first milestone", "big": "$10,000", "sub": "20 ways to get there"})
sc("""Here's why ten thousand matters so much. With ten thousand dollars saved, most surprises stop being
emergencies. The car repair, the vet bill, the urgent flight. You stop borrowing. You stop paying interest on
your bad luck. And for many people, it's the first time money feels like a tool instead of a threat.""",
   "Car repair garage mechanic", "BAD LUCK STOPS COSTING YOU")
sc("""In this video, twenty practical ways to get there. Some help you spend less, some help you earn more, and
some protect what you've saved. You don't need all twenty. Pick five that fit your life, and you can get to ten
thousand faster than you think. And we'll look at it from three angles: the numbers, the psychology, and a
simple playbook to put it all together.""",
   "Notebook with financial notes", "20 WAYS, PICK 5")
pr("""Before we start, a promise. Nothing in this video requires you to live on rice and beans, cancel every bit of fun,
or become a different person. These are practical, normal moves that real people use. Let's start with where the numbers
come from, then the math of the first ten thousand.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Savings data comes from the Federal Reserve's survey on the economic well being of U.S. households, and from
Bankrate's emergency savings research. Fee information comes from the Consumer Financial Protection Bureau. Car
payment data comes from Edmunds. Tax refund data comes from the IRS filing season statistics. When we show
interest, it's a simple illustration, and rates change all the time. This video is education, not financial
advice.""",
   "Federal Reserve Bank building columns", "OUR SOURCES")

# ---------------- Angle 1: numbers ----------------
ch("Angle 1: The numbers")
pr("""Angle one. The numbers. Ten thousand dollars sounds like a mountain. Let's break it into pieces.""")
card("""Ten thousand dollars in one year is about eight hundred thirty three dollars a month. Or about one hundred
ninety two dollars a week. Or about twenty seven dollars a day.""",
     {"type": "compare", "left": {"label": "Per month", "big": "~$833", "sub": "for 12 months"},
      "right": {"label": "Per day", "big": "~$27", "sub": "for 365 days"},
      "note": "$10,000 divided over one year"})
sc("""Twenty seven dollars a day. That's a delivery dinner. A couple of drinks out. A tank of gas. Nobody's saying
give all of those up forever. But it shows that ten thousand dollars is not one giant act. It's a few hundred
small decisions, made in your favor.""",
   "Coffee shop cup", "$27 A DAY")
card("""And if a year is too fast, stretch it. Four hundred dollars a month gets you there in about two years. Two
hundred dollars a month gets you there in a little over four years. Any of these is a real plan.""",
     {"type": "compare", "left": {"label": "$400 a month", "big": "~2 years", "sub": "to $10,000"},
      "right": {"label": "$200 a month", "big": "~4 years", "sub": "to $10,000"},
      "note": "Before any interest earned. Interest shortens it a little."})
sc("""Now compare that with where most people are. Bankrate's research has found that a large share of Americans
have less than three months of expenses saved, and roughly a quarter have no emergency savings at all. The Federal
Reserve found that about a third of adults wouldn't cover a surprise four hundred dollar bill with cash. So if you
reach ten thousand, you'll be ahead of a very large part of the country.""",
   "Empty wallet", "AHEAD OF MOST PEOPLE")
sc("""And here's the hidden math that makes the first ten thousand so valuable. If you don't have it, surprises go on a
credit card at over twenty percent interest. A two thousand dollar emergency, paid off slowly, can cost hundreds in
interest. Your savings don't just sit there. They prevent a cost you would otherwise pay again and again.""",
   "Credit card close up", "SAVINGS PREVENT INTEREST")
sc("""There's one more number worth knowing: your personal speed. Take the amount you can realistically save each month,
including the money you'll free up with the ideas in this video, and divide ten thousand by it. That's your number of
months. Write it down. If it's twelve, great. If it's forty, that's fine too. A forty month plan you finish beats a twelve
month plan you abandon in March.""",
   "Calculator with financial charts", "YOUR PERSONAL SPEED")
sc("""And remember that the speed isn't fixed. Every way you add from this list shortens the timeline. A subscription
sweep might take a month off. A paid off car loan might take six months off. A raise might take a year off. The plan you
start with is just your first draft. Every few months, recalculate, and watch the finish line move closer.""",
   "Road sign highway", "THE FINISH LINE MOVES")
pr("""Alright. Twenty ways to get to ten thousand dollars. The first five are about setting up the system, because a
good system beats good intentions every time.""")

# ---------------- Ways ----------------
way(1, "Name the goal", "a number and a date",
"""Way number one. Give the goal a name, a number and a date.""",
"""Saving more is a wish. Ten thousand dollars by next December is a plan. Research on goal setting has found that
specific goals with deadlines lead to better results than vague ones. And naming the account, something like Freedom
Fund or Never Broke Again, sounds silly, but it makes the money feel like it has a job.""",
"""Try this: write the number and the date on a sticky note, and put it where you'll see it every day. Your bathroom
mirror, your laptop, your fridge. Every time you see it, you'll make one or two decisions differently. Over a year,
that adds up to real money.""",
"Notebook with financial notes", "A NUMBER AND A DATE",
"Sticky notes on wall", "SEE IT EVERY DAY")

way(2, "A separate account", "out of sight, out of reach",
"""Way number two. Keep your savings in a separate account, ideally at a different bank.""",
"""When your savings sit in the same app as your checking, they get spent. Not on purpose. A little here, a little
there. Moving them to a different bank adds a small barrier, a transfer that takes a day or two. That's just enough
friction to stop impulse spending, and not enough to stop you in a real emergency.""",
"""Look for an account that's FDIC insured, with no monthly fees and no minimum balance. And don't connect a debit card
to it. The goal is a place where money goes in easily and comes out only when you really decide it should.""",
"Bank building United States", "A DIFFERENT BANK",
"Online banking smartphone app", "IN EASY, OUT HARD")

way(3, "Automate it on payday", "save first, spend what's left",
"""Way number three. Automate your saving, on payday.""",
"""Most people save what's left at the end of the month. And at the end of the month, there's usually nothing left.
Flip it. Set an automatic transfer for the day your paycheck lands. You'll adjust your spending to what remains,
usually without even noticing. It's the single most powerful habit in personal finance.""",
"""If your employer allows it, you can even split your direct deposit, so part of every paycheck goes straight to your
savings account and never touches checking. Start with an amount that feels a little uncomfortable, but not painful.
Then raise it every few months.""",
"Clock gears mechanism", "AUTOMATE IT",
"Office building at dusk", "SPLIT THE DEPOSIT")

way(4, "Save every windfall", "refunds, bonuses, gifts",
"""Way number four. Send every windfall straight to savings.""",
"""Tax refunds, bonuses, birthday money, rebates. IRS filing statistics show the average federal tax refund has been
around three thousand dollars in recent years. For a lot of people, that single refund is almost a third of the way
to ten thousand dollars.""",
"""The trick is deciding before the money arrives. Once it's in your checking account, it starts to feel like spending
money. Decide now: all windfalls go to the goal. Or if that's too strict, try an eighty twenty rule. Eighty percent
saved, twenty percent enjoyed.""",
"Tax forms on desk", "~$3,000 REFUND",
"Gift box present", "DECIDE BEFORE IT ARRIVES")

way(5, "Track it every week", "what gets measured grows",
"""Way number five. Check your progress once a week.""",
"""Not obsessively. Just once, same day every week. How much is in the account? How much did you spend? Seeing the
number grow is motivating, and noticing a bad week early lets you fix it before it becomes a bad month.""",
"""Some people use a simple chart on the fridge, with a box for every two hundred fifty dollars. Fifty boxes to ten
thousand. Coloring in a box feels surprisingly good. It turns saving from something abstract into something you can
see.""",
"Calendar planning", "ONCE A WEEK",
"Chart on paper", "COLOR IN THE BOXES")

pr("""Now, the next seven ways are about spending less, without making your life miserable.""")

way(6, "Cancel what you don't use", "the subscription sweep",
"""Way number six. Do a subscription sweep.""",
"""Streaming services, apps, memberships, software, a gym you don't go to. Each one is small, so it slips under the
radar. Together, they can easily add up to one hundred dollars a month or more. And many renew automatically, so you
keep paying long after you stopped using them.""",
"""Go through the last two months of your bank and card statements, line by line. Cancel anything you didn't use in
the last thirty days. You can always sign up again later. Many people find fifty to one hundred dollars a month in an
hour. That's six hundred to twelve hundred dollars a year.""",
"Laptop streaming service", "THE SUBSCRIPTION SWEEP",
"Scissors cutting paper", "CANCEL, YOU CAN COME BACK")

way(7, "Negotiate your bills", "an hour of calls",
"""Way number seven. Negotiate your bills.""",
"""Phone, internet, car insurance, home or renters insurance. Companies often give their best prices to new customers,
which means loyal customers can end up paying more for the same thing. A few phone calls, or a few online quotes, can
lower these bills noticeably.""",
"""Try this: get two quotes from competitors first. Then call your current provider, tell them what you've been offered,
and ask if they can match it. If not, switch. An hour of calls could save fifty to one hundred fifty dollars a month,
every month, with zero change in your lifestyle.""",
"Phone call customer service", "CALL AND ASK",
"Car insurance documents", "GET TWO QUOTES")

way(8, "Cut the delivery markup", "same food, less money",
"""Way number eight. Cut back on food delivery.""",
"""Delivery apps add service fees, delivery fees, tips and often higher menu prices. A twenty dollar meal can easily
become thirty dollars or more by the time it reaches your door. You're paying a big premium for convenience.""",
"""You don't have to quit. Pick it up yourself, or set a limit, like twice a month instead of twice a week. Cooking a
few simple meals in bulk on Sunday can cover lunches for the week. Small change, real money. Many households save one
hundred to two hundred dollars a month here.""",
"Food delivery bicycle", "THE MARKUP",
"Cooking at home kitchen", "COOK ON SUNDAY")

short("A car payment can quietly steal your first ten thousand dollars. Here's the math.")
way(9, "Skip the car payment", "the biggest leak for many people",
"""Way number nine. Avoid a big car payment.""",
"""Edmunds has reported that the average monthly payment on a new car loan has been above seven hundred dollars. That's
over eight thousand dollars a year, almost your entire ten thousand dollar goal, going to a car that loses value every
month.""",
"""If your current car runs, keep it. If you need a car, consider a reliable used one, and keep the loan short. And when
you finally pay off a car loan, here's the best trick in personal finance: keep making the same payment, but to your
savings account. You're already used to living without that money.""",
"Car dealership lot", "OVER $700 A MONTH",
"Old car parked on street", "KEEP THE CAR")

way(10, "Rethink housing", "the biggest bill of all",
"""Way number ten. Rethink your housing costs.""",
"""Housing is the biggest expense for most households. That makes it the place where a single change saves the most.
A roommate, a slightly smaller apartment, or a place a bit further out can free up hundreds of dollars a month.""",
"""It's not for everyone, and it's not forever. But even one year with a roommate, saving four hundred dollars a month,
puts nearly five thousand dollars toward your goal. Half of your first ten thousand, from one decision.""",
"Apartment building", "THE BIGGEST BILL",
"Friends sharing apartment", "ONE YEAR, $4,800")

way(11, "Sell what you don't use", "your closet is a bank",
"""Way number eleven. Sell things you don't use.""",
"""Most homes have hundreds or even thousands of dollars of unused stuff. Old phones, electronics, furniture, tools,
sports gear, clothes with the tags still on. Online marketplaces make it easy to sell locally.""",
"""Try this: walk through your home with a box. Anything you haven't used in a year goes in the box. Sell what's worth
selling, donate the rest. Every dollar goes straight to savings. It's one of the fastest ways to build momentum in the
first month.""",
"Garage sale items", "YOUR CLOSET IS A BANK",
"Cardboard boxes moving", "ONE BOX, ONE WEEKEND")

way(12, "Use a thirty day rule", "for every want",
"""Way number twelve. Use a thirty day rule for wants.""",
"""When you want something that isn't a need, write it down with the date, and wait thirty days. If you still want it
after thirty days, and it fits your budget, buy it guilt free. You'll be surprised how often the urge simply fades.""",
"""This works because a lot of spending is emotional. A bad day, a clever ad, a friend's post. The thirty day rule puts
time between the feeling and the purchase. People who try it often find that a large share of their wish list
disappears on its own.""",
"Shopping bags mall", "WAIT 30 DAYS",
"Calendar planning", "THE URGE FADES")

pr("""Quick pause. If these ideas are helping, subscribe to the channel. Every week I break down another step on the road
from zero to financial freedom, and subscribing is the easiest way to keep going with me. Now, the next five ways are
about earning more, because cutting has a limit, and earning doesn't.""")

way(13, "Ask for a raise", "the best hourly rate you'll ever earn",
"""Way number thirteen. Ask for a raise.""",
"""Many people never ask. But a conversation of thirty minutes can be worth thousands of dollars a year, for every year
you stay. And raises compound, because future raises are usually a percentage of your current pay.""",
"""Prepare. Look up salary data for your role and city. Write down what you've achieved, with numbers if you can. Then
ask for a specific amount. If the answer is no, ask what it would take to get there in six months, and get it in
writing. Send every dollar of the raise to your goal for the first few months.""",
"Business meeting handshake", "ASK",
"Person writing list notebook", "PREPARE YOUR CASE")

way(14, "Take the extra hours", "overtime and extra shifts",
"""Way number fourteen. Take extra hours, for a limited time.""",
"""If your job offers overtime or extra shifts, a few months of extra work can speed up your goal dramatically. Overtime
is often paid at a higher rate, and it goes straight into money you're not used to having yet.""",
"""The key is a time limit. Burning out isn't a plan. Try a sprint: three months of extra hours, every extra dollar to
savings, then back to normal. A short sprint can cover a big chunk of the way to ten thousand.""",
"Night shift worker", "A SHORT SPRINT",
"Calendar planning", "THREE MONTHS ONLY")

way(15, "Sell a skill", "side income that fits your life",
"""Way number fifteen. Turn a skill into side income.""",
"""Tutoring, pet sitting, handyman work, cleaning, editing, design, translation, lawn care. If you have a skill people
pay for, a few hours a week can add a few hundred dollars a month. You don't need a business plan. You need one
customer, then another.""",
"""Start with people who already know you. Tell friends, family and neighbors what you offer. Price it fairly, do great
work, and ask for referrals. And remember taxes: side income is usually taxable, so set aside a part of every payment.""",
"Person working from home laptop", "SELL A SKILL",
"Dog walker park", "ONE CUSTOMER AT A TIME")

way(16, "Consider switching jobs", "the biggest raises often come from moving",
"""Way number sixteen. Consider switching jobs.""",
"""Wage tracking by the Federal Reserve Bank of Atlanta has often shown that people who change jobs see faster pay growth
than people who stay. Loyalty is nice, but the market often pays more for the same skills.""",
"""You don't have to leave. But you should know what you're worth. Update your resume, look at listings, and talk to one
or two recruiters each year. Either you find a better offer, or you get the information you need to ask for more where
you are.""",
"Job interview handshake", "MOVERS EARN MORE",
"Person studying laptop at night", "KNOW YOUR WORTH")

way(17, "Use rewards the right way", "only if you pay in full",
"""Way number seventeen. Use cash back the right way, or not at all.""",
"""Cash back cards can give you one to two percent or more back on spending. But only if you pay the full balance every
month. Carry a balance at over twenty percent interest, and the rewards are wiped out many times over.""",
"""If you trust yourself, use one simple cash back card for normal spending, pay it off in full automatically, and send
the rewards to savings every few months. If you don't trust yourself with credit cards yet, skip this one entirely.
That's a smart decision, not a weak one.""",
"Credit card close up", "ONLY IF PAID IN FULL",
"Coins in jar", "REWARDS TO SAVINGS")

pr("""And the last three ways are about protecting what you save, so it keeps growing instead of leaking away.""")

way(18, "Stop paying fees", "overdrafts, ATMs, late fees",
"""Way number eighteen. Stop paying bank fees.""",
"""The Consumer Financial Protection Bureau has reported that overdraft fees have typically been around thirty five
dollars each. A few overdrafts, some out of network ATM fees, and a late payment fee can easily cost a hundred dollars
or more in a single month.""",
"""Turn off overdraft coverage if you can. Set up low balance alerts. Put every bill on autopay for at least the
minimum. And use your own bank's ATMs. These are boring fixes, but every fee you stop paying is money that goes to your
goal instead of the bank.""",
"ATM machine", "~$35 PER OVERDRAFT",
"Online banking smartphone app", "ALERTS AND AUTOPAY")

way(19, "Earn interest on it", "a high yield savings account",
"""Way number nineteen. Make your savings earn interest.""",
"""Many big banks pay almost nothing on savings. Online banks and some credit unions often pay much more on high yield
savings accounts. Rates change with the economy, but the difference can be significant, and it costs nothing to switch.""",
"""On ten thousand dollars, the difference between almost zero and a few percent could be a few hundred dollars a year.
It won't make you rich, but it's free money for your emergency fund, and it helps it keep up with inflation. Just make
sure the account is FDIC or NCUA insured.""",
"Bank building United States", "HIGH YIELD",
"Piggy bank coins", "FREE MONEY")

way(20, "Save your raises", "the painless way to save more",
"""Way number twenty. Save your raises.""",
"""When your income goes up, your spending usually follows. That's lifestyle creep. The easiest way to beat it is to
decide in advance: at least half of every raise goes to savings. Your life still gets better, and your savings rate
climbs automatically.""",
"""Say you get a three thousand dollar raise. You keep fifteen hundred to enjoy, and fifteen hundred goes to your goal.
That's one hundred twenty five dollars a month you never had to cut from anything. Do this with every raise, and you'll
reach ten thousand, and then the next ten thousand, almost without trying.""",
"Graph trending upward", "HALF OF EVERY RAISE",
"Person smiling at laptop", "PAINLESS")

# ---------------- Three savers ----------------
short("Three people saved their first ten thousand dollars in three very different ways.")
ch("Three ways people get there")
pr("""Let's make this concrete with three example savers. They're made up, but each one uses a different mix of the
twenty ways, and the math is simple enough to check on your phone.""")
sc("""Saver one. Dani is twenty three, works retail, and earns about thirty two thousand dollars a year. There isn't
much room to cut. So Dani focuses on systems and windfalls. An automatic transfer of one hundred fifty dollars every
month. A tax refund of about one thousand five hundred, saved in full. Birthday and holiday money, saved. A box of old
electronics sold online for four hundred dollars. And a cash back card, paid in full every month, with the rewards
swept into savings.""",
   "Young woman working retail store", "DANI: SYSTEMS AND WINDFALLS")
sc("""In the first year, Dani saves around four thousand dollars. In the second year, a raise and a promotion push the
monthly transfer to two hundred fifty, and the refund grows a bit. By the end of year three, Dani crosses ten thousand
dollars. Three years sounds slow. But Dani is twenty six with ten thousand dollars, no debt, and a habit that will
last a lifetime. That's a better start than most people ever get.""",
   "Calendar planning", "THREE YEARS, NO DEBT")
sc("""Saver two. Marcus is thirty one, a warehouse supervisor earning fifty five thousand dollars. Marcus focuses on the
big leaks. He keeps his paid off truck instead of buying a new one, avoiding a payment of about seven hundred dollars.
He takes a roommate for one year, saving four hundred a month. And he cuts delivery food from three times a week to
twice a month.""",
   "Young man working warehouse", "MARCUS: THE BIG LEAKS")
sc("""Together, those changes free up more than eight hundred dollars a month, without touching his social life or his
hobbies. Marcus reaches ten thousand dollars in just over a year. Then, instead of buying the new truck, he keeps the
transfer running and starts investing. Two years later, the truck still runs fine, and Marcus has more than twenty
thousand dollars set aside.""",
   "Pickup truck parked", "KEEP THE TRUCK")
sc("""Saver three. Aisha is thirty eight, a nurse, and a single parent earning seventy thousand dollars. Aisha's budget is
tight because of childcare, so she focuses on earning more. She picks up two extra shifts a month for six months,
negotiates a raise when she takes on a training role, and sends the whole raise to savings for the first year.""",
   "Nurse in hospital corridor", "AISHA: EARN MORE")
sc("""Her extra shifts add around six thousand dollars before tax over the sprint. The raise adds about three thousand
more over the year. With a small automatic transfer on top, Aisha passes ten thousand dollars in about fourteen months,
while her daily life barely changes. And because the extra shifts had an end date, she didn't burn out.""",
   "Mother and child walking", "A SPRINT WITH AN END DATE")
sc("""Three people, three incomes, three completely different strategies. Dani used systems and windfalls. Marcus closed
the big leaks. Aisha earned more for a limited time. What they had in common was a named goal, a separate account, and
an automatic transfer that never stopped. Those three things are the skeleton. The other ways are the muscle you add.""",
   "Three people silhouettes", "THE SKELETON AND THE MUSCLE")

# ---------------- After 10K ----------------
ch("What to do once you have $10,000")
pr("""So you've reached ten thousand dollars. Congratulations. Now what? Here's what most people do next, in a sensible
order.""")
sc("""First, decide what the ten thousand is for. If it's your emergency fund, it stays in safe, boring savings. Don't
invest it in stocks, don't lend it to a friend, don't use it for a vacation. Its job is to sit there, quietly, until
life throws something at you. And if you use it, the next job is to refill it.""",
   "Bank vault door", "GIVE IT A JOB")
sc("""Second, if you still have any high interest debt, this is the moment to attack it hard. Your cushion means you won't
need the credit card for emergencies anymore, so you can throw your monthly transfer at the balance. A card at over
twenty percent costs you more than almost any investment could reasonably earn.""",
   "Scissors cutting credit card", "ATTACK THE DEBT")
sc("""Third, start investing for the long term. If your employer offers a match on retirement contributions, make sure
you're getting all of it. Then consider an IRA, invested in low cost, broad index funds. Now the same automatic transfer
that built your cushion starts building your future. At a seven percent illustration, five hundred dollars a month for
twenty years grows to roughly two hundred sixty thousand dollars.""",
   "New York Stock Exchange trading floor", "START INVESTING")
sc("""And fourth, grow the cushion over time. Ten thousand is a great start. As your life gets bigger, with a family, a
home, or more responsibilities, many people grow their emergency fund to three to six months of essential costs. But
don't let that stop you from investing. You can do both at the same time, with part of your monthly transfer going to
each.""",
   "Family relaxing at home", "GROW THE CUSHION")

# ---------------- Traps ----------------
ch("Five traps that drain your savings")
pr("""Finally, five traps that drain savings right after people build them. Know them in advance, and you can walk right
past them.""")
sc("""Trap one. The reward splurge. You hit your goal and celebrate with a purchase that eats a big chunk of it. Celebrate,
absolutely, but with something small. Trap two. The fake emergency. A sale, a concert, a new phone. Before you touch the
fund, ask: is this unexpected, necessary, and urgent? If not all three, it's not an emergency.""",
   "Shopping bags mall", "TRAPS 1 AND 2")
sc("""Trap three. The friend in need. Lending money to people you love can strain both your savings and the relationship.
If you want to help, consider giving an amount you can afford to lose, rather than lending. Trap four. The hot tip.
Someone tells you how to double your ten thousand quickly. The faster the promise, the bigger the risk, and some of
these are outright scams.""",
   "Friends talking coffee", "TRAPS 3 AND 4")
sc("""And trap five. Stopping the transfer. You reached the goal, so you turn off the automatic savings. A few months
later, the extra money has quietly disappeared into everyday spending. Instead, redirect it. The transfer that built your
first ten thousand should keep running for the rest of your life. Just point it at the next goal.""",
   "Clock gears mechanism", "TRAP 5: STOPPING")

# ---------------- Angle 2: psychology ----------------
short("You're not bad with money. Your brain is doing exactly what it was built to do.")
ch("Angle 2: The psychology")
pr("""Angle two. The psychology. Because if saving ten thousand dollars were just about knowing these twenty ways,
everybody would do it. The hard part is in your head.""")
sc("""Behavioral economists have a name for one of the biggest obstacles: present bias. We value rewards now much more
than rewards later. A dinner tonight feels real. Ten thousand dollars next year feels abstract. That's not a personal
failing. It's how human brains work. Which is exactly why automation works so well. It takes the decision away from
the version of you standing in the store.""",
   "Person thinking by window", "PRESENT BIAS")
sc("""The second obstacle is the what the heck effect. You've been saving well, then one weekend you overspend. And your
brain says, well, I already blew it, might as well keep going. Researchers have described this pattern with diets, and
it shows up with money too. The fix is to treat a bad day as a bad day, not a broken plan. The next day, you just
continue.""",
   "Person stressed looking at bills", "THE WHAT THE HECK EFFECT")
sc("""The third is social pressure. Friends invite you out, coworkers order lunch, family expects gifts. Saying no feels
awkward. One approach that works for many people is to be honest, but positive. Instead of, I can't afford it, try, I'm
saving for something big this year. Most people respect a goal. Some even join you.""",
   "Friends at restaurant", "SOCIAL PRESSURE")
sc("""And the fourth is the long middle. The first thousand dollars feels exciting. The last thousand feels exciting. But
somewhere around four or five thousand, it gets boring. This is where people quit. Plan for it. Set small milestones
every thousand or two, and celebrate each one with something small and cheap that you genuinely enjoy.""",
   "Long road desert", "THE LONG MIDDLE")
sc("""Here's the most encouraging thing. When people reach ten thousand dollars, they often say they feel calmer, sleep
better, and fight less about money at home. The Federal Reserve's surveys consistently show that people who can handle
a surprise expense report higher financial well being. The money matters. But the calm matters even more.""",
   "Person sleeping peacefully", "THE CALM IS THE PRIZE")

# ---------------- Angle 3: playbook ----------------
short("Here's a simple twelve month plan to save your first ten thousand dollars.")
ch("Angle 3: The playbook")
pr("""Angle three. The playbook. Here's a simple twelve month plan, using a handful of the twenty ways. This is an
example, so adjust it to your own life.""")
sc("""Month one. Name the goal, open a separate account, and set an automatic transfer of two hundred fifty dollars a
month. Do the subscription sweep and negotiate two bills. Say that frees one hundred fifty dollars a month, which also
goes into the automatic transfer. Sell one box of stuff. You might start the year with five hundred dollars and four
hundred a month flowing in.""",
   "Calendar planning", "MONTH 1: SET UP")
sc("""Months two and three. Cut delivery to twice a month, adding about one hundred dollars more. Now you're saving five
hundred a month. In March or April, your tax refund arrives. Say it's two thousand five hundred dollars, and you save
eighty percent, two thousand. By the end of month three, you could be past three and a half thousand dollars.""",
   "Tax forms on desk", "MONTHS 2 AND 3")
sc("""Months four to six. Do a three month sprint of extra hours or a small side income, adding about three hundred
dollars a month. That's eight hundred a month going in. By the end of month six, you could be above six thousand. This
is the long middle, so celebrate every thousand.""",
   "Night shift worker", "MONTHS 4 TO 6: SPRINT")
sc("""Months seven to twelve. The sprint ends, so you're back to about five hundred a month. But your annual raise
arrives, and half of it goes to savings, adding maybe one hundred dollars more. Add interest from a high yield account,
and by month twelve, you're at or near ten thousand dollars. No lottery. No extreme frugality. Just a handful of good
decisions, stacked on top of each other.""",
   "Mountain climber reaching summit", "MONTHS 7 TO 12")
sc("""And what happens next is the best part. Don't stop the automatic transfer. Keep it running, and send it to the next
goal: investing for the long term, or paying off any remaining debt. You already know how to live without that money.
That's the real gift of the first ten thousand. It builds the habit that builds everything after it.""",
   "Graph trending upward", "KEEP THE TRANSFER RUNNING")

# ---------------- Questions ----------------
ch("Questions people ask")
pr("""Let me answer the questions I get most about the first ten thousand dollars.""")
sc("""Question one. Should I save ten thousand before paying off credit cards? Many people build a small cushion first,
around one thousand to two thousand dollars, then attack high interest debt, then come back to finish the ten thousand.
That keeps you from adding new debt while you pay off the old. Question two. Should I invest it instead? For an
emergency fund, most people keep it in savings, not stocks, because emergencies often arrive when markets are down.""",
   "Credit card bills on table", "DEBT OR SAVINGS FIRST?")
sc("""Question three. What if I can only save fifty dollars a month? Start anyway. Fifty dollars a month is six hundred a
year, plus whatever windfalls you add. The habit matters more than the amount at first, and your amount will grow when
your income grows. Question four. Is ten thousand enough? For many people, it's a great first emergency fund. Later,
you might aim for three to six months of essential expenses.""",
   "Coins in jar", "ONLY $50 A MONTH?")
sc("""Question five. Should my partner and I save together? If you share expenses, a shared goal can be very powerful,
and talking about it openly reduces money fights. Some couples keep a joint savings account for shared goals and
separate accounts for personal spending. The best system is the one both of you understand and agree on.""",
   "Couple cooking together kitchen", "SAVING AS A COUPLE")
sc("""Question six. Should I pause retirement contributions to reach ten thousand faster? Usually not if your employer
offers a match, because a match is an instant return you can't get back later. Keep contributing at least enough for the
full match, and build your cushion with everything else. If there's no match, some people do pause briefly to build a
starter cushion, then restart.""",
   "Office workers meeting", "PAUSE RETIREMENT?")
sc("""Question seven. What if an emergency wipes out my savings halfway? Then the savings did exactly what they were
supposed to do. Without them, that emergency would be on a credit card right now. Take a breath, restart the transfer,
and rebuild. Most people find the second time is faster, because the habit and the systems are already in place.""",
   "Car with flat tire on road", "WHAT IF IT GETS WIPED OUT?")

# ---------------- Recap ----------------
ch("Recap: 20 ways")
sc("""Let's recap. Setting up the system: name the goal, a separate account, automate on payday, save every windfall,
and track weekly. Spending less: cancel what you don't use, negotiate bills, cut the delivery markup, skip the car
payment, rethink housing, sell what you don't use, and the thirty day rule.""",
   "Notebook with financial notes", "WAYS 1 TO 12")
sc("""Earning more: ask for a raise, take extra hours for a limited time, sell a skill, consider switching jobs, and use
rewards only if you pay in full. And protecting it: stop paying fees, earn interest on your savings, and save at least
half of every raise.""",
   "Mountain climber reaching summit", "WAYS 13 TO 20")
sc("""And the three angles. The numbers: twenty seven dollars a day, or eight hundred thirty three a month, gets you there
in a year. The psychology: present bias, the what the heck effect, social pressure, and the long middle. And the
playbook: stack a handful of these ways, and let automation do the heavy lifting.""",
   "Map and compass", "NUMBERS, PSYCHOLOGY, PLAYBOOK")
sc("""And here's the thing I want you to remember most. The first ten thousand dollars is the hardest because it's the one
that changes you. You learn that you can say no. You learn that you can wait. You learn that small, boring decisions add
up to something real. Once you've learned those things, the money that comes after is easier, faster and calmer. You're
not just saving ten thousand dollars. You're becoming the kind of person who keeps money, and that person never really
goes back to living paycheck to paycheck.""",
   "Sunrise over mountains", "IT CHANGES YOU")

# ---------------- Close ----------------
ch("What to do next")
pr("""So here's your homework. Pick five of the twenty ways. Write them down. Do the first one today, even if it's just
opening the account. Then add one more way every week for the next month. By the end of the month, you'll have a system
that runs on its own. If you want the full step by step plan, it's in my playbook, link in the description. And when you
hit ten thousand, come tell me in the comments. I'm Ryan Rover. See you in the next one.""")

save("video06", "The First $10,000 Is the Hardest: 20 Ways to Get There", [
    "Federal Reserve, Economic Well-Being of U.S. Households in 2025 (63% would cover a $400 expense with cash or its equivalent)",
    "Bankrate, Emergency Savings Report 2026 (share of Americans with no emergency savings or less than three months)",
    "Consumer Financial Protection Bureau, overdraft and NSF fee research (overdraft fees typically around $35)",
    "Edmunds, new vehicle financing data (average new car payment above $700 a month)",
    "IRS, filing season statistics (average federal refund around $3,000 in recent years)",
    "Federal Reserve Bank of Atlanta, Wage Growth Tracker (job switchers vs job stayers)",
    "Locke and Latham, goal-setting research (specific goals with deadlines improve results)",
], "the first $10,000 is the hardest")
