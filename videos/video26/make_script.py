import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

body_hook = None  # set right before item() to start a Short at its first explained scene

def item(n, title, sub, card_text, body, example, fix, q1, c1, q2, c2, q3, c3):
    ch(f"Rule {n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"RULE {n}")
    global body_hook
    if body_hook:
        short(body_hook); body_hook = None
    sc(body, q1, c1)
    sc(example, q2, c2)
    sc(fix, q3, c3)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Here's a question that tells you a lot about money. Why do so many genuinely rich
people drive old, boring cars? You'd think the people who can most afford a brand new luxury car would be the
ones buying them. But again and again, researchers find millionaires driving ten year old sedans, while people
with far less money drive the shiny new SUVs. Today, we'll figure out why, through fifteen money rules from real
millionaires.""")
short('Why do so many millionaires drive old cars?')
card("""Here's the research that started it. In Stop Acting Rich, Thomas Stanley reported that the median
price millionaires paid for their most recent vehicle was about thirty one thousand dollars, based on surveys
in the late two thousands. Meanwhile, the average new car today sells for more than fifty thousand.""",
     {"type": "compare", "left": {"label": "Millionaires' median car", "big": "~$31,000", "sub": "Stanley, Stop Acting Rich"},
      "right": {"label": "Average new car today", "big": "$50,000+", "sub": "Kelley Blue Book, 2025"},
      "note": "Different years, so treat as a rough contrast"})
sc("""Those numbers come from different years, so they're not a perfect comparison. But the pattern is
striking. Stanley found that many millionaires bought used cars, kept them for years, and chose reliable
mainstream brands. He also found that a lot of the people driving luxury cars weren't millionaires at all.
They were high earners spending their income on looking wealthy. That gap between looking rich and being rich
is what this whole video is about.""",
   "Old reliable car parked in driveway", "LOOKING RICH VS BEING RICH")
sc("""We'll go through fifteen rules from three angles. First, the numbers. The car math that millionaires
understand and most people ignore. Second, the psychology. Why rich people don't need a car to feel successful.
And third, the playbook. The rules they apply not just to cars, but to everything they buy. By the end, you'll
see why an old car in a millionaire's driveway isn't a sign of being cheap. It's a sign of a strategy.""",
   "Road through countryside", "THREE ANGLES")
pr("""Let's begin with the numbers. Rule number one is the one that changes everything else.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our sources. Millionaire car data comes from Thomas Stanley's research. New car prices come from Kelley
Blue Book, loan and payment data from Edmunds, and the full cost of owning a car from AAA's Your Driving Costs
study. The average age of cars on American roads comes from S and P Global Mobility. Ideas on the psychology of
money come from Morgan Housel's book The Psychology of Money and from research by psychologist Thomas Gilovich.
Growth examples use a stated seven percent average yearly return, an illustration, not a promise. This is
education, not financial advice.""",
   "Stack of research books", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Five rules about the math of cars, and why millionaires take that math so
seriously.""")

body_hook = 'Your new car loses this much in year one.'
item(1, "Let someone else pay the depreciation", "buy a few years old",
"""Rule number one. Let someone else pay for the biggest drop in value.""",
"""A new car loses value fastest in its first few years. Sources like Carfax and Edmunds estimate that many
new cars lose around twenty percent of their value in the first year, and roughly half or more within five
years, depending on the model. That loss is called depreciation, and it's one of the biggest costs of owning
a car. It never shows up on a bill, so most people never think about it. But it's real money leaving your
pocket every single day.""",
"""Millionaires who understand this often buy cars that are two or three years old. By then, the first owner
has absorbed the steepest part of the drop. The car is often still reliable, may still have some warranty
left, and costs thousands of dollars less. On a fifty thousand dollar car, letting someone else take the first
year's hit could easily save ten thousand dollars or more. That's money that can be invested instead of
evaporating in a driveway.""",
"""Apply the rule. Before your next purchase, look up the price of the same model brand new and at two or
three years old. Compare the difference with what you'd actually lose in features or reliability. For many
reliable models, the slightly used version is the far better deal. Consider certified pre owned programs if you
want extra peace of mind.""",
"New car driving off dealership lot", "-20% IN YEAR ONE",
"Certified pre owned car lot", "LET SOMEONE ELSE PAY",
"Comparing car prices on laptop", "NEW VS 3 YEARS OLD")

item(2, "Keep it for ten years or more", "the cheapest car is the one you own",
"""Rule number two. Keep your car for a long, long time.""",
"""According to S and P Global Mobility, the average age of cars and light trucks on American roads has
climbed to a record of over twelve and a half years. Modern cars, with good maintenance, can often last well
over one hundred fifty thousand miles. Yet many people trade in every three to five years, starting a new cycle
of depreciation and a new loan each time.""",
"""Every time you trade in a car, you lose money. Depreciation, sales tax, dealer fees, higher insurance on
the newer car, and often a new loan with new interest. Keeping a car for ten years instead of five can cut your
lifetime car costs dramatically. Many millionaires drive a car until repairs genuinely cost more than
replacement. Not until they get bored.""",
"""Apply the rule. Set a goal to keep your current car at least five years past the final payment. Track
repair costs in a notebook. Replace the car when repairs become frequent, expensive and unreliable, not when a
new model comes out.""",
"Old car with high mileage odometer", "12.5 YEARS AVERAGE AGE",
"Car trade in at dealership", "EVERY TRADE COSTS MONEY",
"Odometer passing 150000 miles", "DRIVE IT LONGER")

item(3, "Know the full cost", "the payment is a lie",
"""Rule number three. Know the full cost of owning a car, not just the payment.""",
"""AAA's Your Driving Costs study estimated that owning and operating a new car costs more than twelve
thousand dollars a year on average when you add up depreciation, insurance, fuel, maintenance, financing,
registration and taxes. That's over a thousand dollars a month. Most people only think about the monthly
payment, which is just one piece of that total.""",
"""Millionaires tend to think in total cost. A cheaper, reliable car doesn't just have a smaller payment. It
usually has lower insurance, lower registration fees in many states, cheaper tires and parts, and less
depreciation. The full cost difference between a modest car and a luxury car can be many thousands of dollars a
year, every year.""",
"""Apply the rule. Add up what your car really costs you in a year. Payment, insurance, fuel, maintenance,
registration, parking and an estimate of depreciation. Divide by twelve. That's the real monthly price of your
car. Use that number, not the payment, when you decide on your next one.""",
"Gas station fuel pump", "$12,000+ A YEAR",
"Car insurance bill", "THE PAYMENT IS ONE PIECE",
"Notebook with car costs", "THE REAL MONTHLY PRICE")

item(4, "Pay cash, or keep the loan short", "interest makes it worse",
"""Rule number four. Pay cash for cars when you can, and keep any loan short.""",
"""Edmunds has reported that many new car loans now stretch to seventy two months or more, with average new
car payments above seven hundred dollars a month. Long loans mean more interest and more time owing more than the
car is worth. Many quiet millionaires either pay cash or use short loans they can pay off quickly.""",
"""There's a psychological benefit to cash too. When you have to hand over the full price, you feel it.
That feeling makes you choose more carefully. A forty thousand dollar car feels very different as one payment
from savings than as six hundred dollars a month. That's exactly why sellers push monthly payments.""",
"""Apply the rule. If you need a loan, aim for four years or less, and make a big down payment. Better yet,
start a car fund now. When your current car loan ends, keep making the same payment into savings. By the time
you need another car, you may be able to buy it outright.""",
"Cash payment for car", "PAY CASH",
"Car loan contract signing", "72+ MONTH LOANS",
"Savings jar labeled car fund", "START A CAR FUND")

item(5, "Invest the difference", "the car that becomes a fortune",
"""Rule number five. Invest the difference.""",
"""Here's where the numbers get exciting. Say one person drives a modest used car, and another has a seven
hundred dollar monthly payment on a new one. If the first person invests that seven hundred dollars every month
instead, at a seven percent average yearly return, after twenty years it could grow to over three hundred sixty
thousand dollars.""",
"""That's the secret behind the old car in the millionaire's driveway. It's not just about saving money on a
car. It's about what the saved money becomes. Over a career, the difference between a car payment lifestyle and
a paid off car lifestyle can easily reach hundreds of thousands of dollars, or more.""",
"""Apply the rule. Calculate the difference between what you spend on your car and what a reliable, modest
car would cost. Even if it's only two hundred dollars a month, set up an automatic investment for that amount.
Watch what it becomes.""",
"Stock market growth chart", "INVEST THE DIFFERENCE",
"Modest car next to growing money", "WHAT THE OLD CAR BUYS",
"Automatic investment setup", "AUTOMATE IT")

short('What a car payment could become instead.')
card("""Here's the math on screen. Seven hundred dollars a month, invested for twenty years at a seven percent
average yearly return, grows to roughly three hundred sixty five thousand dollars. You'd put in one hundred
sixty eight thousand.""",
     {"type": "growth", "monthly": 700, "rate": 0.07, "years": 20})

ch("New every 5 years vs keep it for 10")
sc("""Let's compare two drivers over twenty years. Driver one buys a new fifty thousand dollar car every five
years, trading in the old one each time. That's four new cars. Each time, they lose a big chunk to
depreciation, pay sales tax again, and usually start a new loan with new interest. They're never without a car
payment.""",
   "New car dealership row of cars", "DRIVER 1: NEW EVERY 5 YEARS")
sc("""Driver two buys a reliable three year old car for around thirty thousand dollars and keeps it ten years.
Then they do it again. That's two cars in twenty years. They pay much less depreciation, much less sales tax, and
spend many of those years with no payment at all. They also pay less for insurance and registration along the
way.""",
   "Used car in good condition", "DRIVER 2: USED, KEEP 10 YEARS")
sc("""The exact numbers depend on the cars, the loans and the market. But it's easy for the difference to
reach well over one hundred thousand dollars in total costs over twenty years. Invested along the way, that
difference could become several hundred thousand. Same need, getting from home to work. Completely different
financial outcome.""",
   "Two roads splitting", "SAME NEED, DIFFERENT OUTCOME")

pr("""That's angle one. Let someone else pay the depreciation, keep it ten years, know the full cost, pay cash
or keep loans short, and invest the difference. Now angle two. The psychology. Because the numbers are easy.
The hard part is not caring what other people think.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
sc("""For many people, a car isn't just transportation. It's a statement. It says who you are, how
successful you are, what kind of person you want to be seen as. Car companies spend enormous amounts on
advertising that connects their cars with status, freedom and identity. Millionaires who drive old cars have
learned to separate those feelings from the purchase.""",
   "Luxury car commercial style", "A CAR AS A STATEMENT")

item(6, "A car is transportation, not identity", "who you are isn't parked outside",
"""Rule number six. Your car is a tool, not your identity.""",
"""Stanley found that many millionaires simply didn't care much about cars. They saw a car as a tool to get
from one place to another, safely and reliably. Many found satisfaction elsewhere, in their families, their
businesses, their communities and their financial independence. Their identity wasn't parked in the driveway.""",
"""When your car is part of your identity, every few years you feel pressure to upgrade it, because the old
one no longer matches who you think you are. When your car is just a tool, you replace it when it stops
working. That one shift in thinking can save a fortune over a lifetime.""",
"""Apply the rule. Ask yourself honestly what you want your car to say about you. Then ask whether there's a
cheaper way to be that person. Usually, the things we want to be known for, like being successful, reliable or
interesting, have nothing to do with what we drive.""",
"Toolbox with tools", "A TOOL",
"Family enjoying time together", "IDENTITY LIVES ELSEWHERE",
"Person reflecting by window", "WHAT DO YOU WANT IT TO SAY?")

body_hook = 'Nobody is watching you as much as you think.'
item(7, "Nobody is watching as much as you think", "the spotlight effect",
"""Rule number seven. Nobody is watching you as closely as you think.""",
"""Psychologist Thomas Gilovich and his colleagues studied something called the spotlight effect. In one
famous experiment, students wore an embarrassing T shirt into a room, and they greatly overestimated how many
people noticed it. We all tend to believe others are paying much more attention to us than they really are.""",
"""That applies to cars too. You might think people judge you for your old sedan. In reality, most people are
too busy thinking about themselves to notice. Millionaires who drive old cars seem to understand this
intuitively. They don't spend money performing for an audience that isn't really there.""",
"""Apply the rule. Next time you feel embarrassed about your car, ask yourself when you last noticed what a
coworker or neighbor drove, and whether you thought less of them for it. Probably never. They're not thinking
about yours either.""",
"Spotlight on stage", "THE SPOTLIGHT EFFECT",
"People walking busy street", "EVERYONE IS BUSY WITH THEMSELVES",
"Parking lot full of cars", "NOBODY NOTICES")

body_hook = "Nobody admires you for your car. Here's why."
item(8, "Wealth is what you don't see", "the man in the car paradox",
"""Rule number eight. Real wealth is invisible.""",
"""In The Psychology of Money, Morgan Housel describes what he calls the man in the car paradox. When you
see someone driving a nice car, you rarely think, wow, that driver is cool. You think, wow, if I had that car,
people would think I'm cool. The irony is that people who buy expensive things to earn admiration often don't get
it, because observers are imagining themselves in the car.""",
"""Housel also points out that wealth is what you don't see. It's the cars not bought, the upgrades not made,
the money left invested. A big house or a fancy car might mean someone is rich, or it might mean they're deeply in
debt. You can't tell from the outside. Real wealth is the money still in the account.""",
"""Apply the rule. Next time you're tempted to buy something to impress, remember the paradox. People won't
admire you. They'll imagine themselves with it. If you want respect, kindness and generosity work far better,
and cost much less.""",
"Sports car on highway", "THE MAN IN THE CAR PARADOX",
"Bank vault door", "WEALTH IS INVISIBLE",
"Person helping neighbor", "RESPECT COSTS LESS")

item(9, "Delay gratification", "the marshmallow mindset",
"""Rule number nine. Be willing to wait.""",
"""In the famous Stanford marshmallow studies, children who could wait for a second treat instead of eating
one right away were followed into adulthood. Later research has questioned how much those results really
predict, and found that family background matters a lot. But the basic idea still resonates with how many
millionaires behave. They're willing to wait.""",
"""Driving an old car now so you can have financial freedom later is a form of delayed gratification. The new
car feels good immediately. The investments feel good much later. People who build wealth have usually learned
to enjoy the waiting, or at least to see it as a fair trade.""",
"""Apply the rule. When you want a big purchase, set a waiting period. Thirty days for anything over a few
hundred dollars, six months for a car. Use the time to save for it in cash. If you still want it after the
wait, buy it with no regrets.""",
"Marshmallow on plate", "THE MARSHMALLOW TEST",
"Calendar countdown", "WILLING TO WAIT",
"Savings growing in jar", "SAVE WHILE YOU WAIT")

pr("""Let's take a quick break. If you're enjoying these rules, subscribe to Ryan Rover Money. It's free and it
helps the channel grow, so we can keep making long, honest videos about money. Now, rule number ten, which
explains why the new car feeling never lasts.""")

item(10, "Escape the hedonic treadmill", "the new car smell fades",
"""Rule number ten. Get off the hedonic treadmill.""",
"""Psychologists use the term hedonic adaptation, often called the hedonic treadmill, to describe how we
quickly get used to new things. The thrill of a new car fades within months. It becomes just your car. Then you
start wanting the next upgrade to feel that thrill again, and the cycle repeats.""",
"""People who understand this stop chasing the thrill through things. Instead, they find longer lasting
satisfaction in experiences, relationships, health and the security of having money saved. Research on
happiness has often suggested that experiences and time with people we love bring more lasting joy than
possessions.""",
"""Apply the rule. Think about the last big purchase that excited you. How long did the excitement last?
Use that answer the next time you're tempted. And consider spending that money on an experience you'll
remember instead.""",
"Treadmill at gym", "THE HEDONIC TREADMILL",
"Friends on road trip", "EXPERIENCES LAST LONGER",
"Old photos of a trip", "WHAT DO YOU REMEMBER?")

ch("Why rich people care less about status")
sc("""There's one more psychological reason rich people often drive old cars. Once you have real financial
security, you need less external proof of success. You know you're doing well, because your accounts tell you
so. People who don't yet have that security often feel more pressure to show success through things.""",
   "Calm confident person", "SECURITY BEATS STATUS")
sc("""This creates a strange loop. The people who most need to save are often the ones who feel the most
pressure to spend on status. And the people who've already saved feel the least pressure. Breaking that loop
early, by caring less about what others see, is one of the most powerful money moves anyone can make.""",
   "Loop arrow circle", "BREAK THE LOOP")
sc("""Many millionaires describe a quiet satisfaction in knowing that they could buy the luxury car, and
choosing not to. That feeling of freedom, of having options, is often worth more to them than the car itself.
Financial independence is the ultimate status symbol, and it's one nobody else can see.""",
   "Person relaxing in hammock", "THE ULTIMATE STATUS SYMBOL")

pr("""That's angle two. A car is a tool, nobody's watching, wealth is invisible, be willing to wait, and get off
the treadmill. Now angle three, the playbook. Five rules millionaires apply not just to cars, but to
everything.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
sc("""The old car isn't really about cars. It's a symptom of a whole way of handling money. The same rules
show up in how millionaires buy houses, clothes, electronics and almost everything else. Here are the five
that matter most.""",
   "Blueprint plans on table", "BEYOND CARS")

item(11, "Maintenance beats replacement", "take care of what you own",
"""Rule number eleven. Take care of what you already own.""",
"""Regular oil changes, tire rotations and following the maintenance schedule can help a car last far longer.
The same applies to homes, appliances and clothes. Small maintenance costs today often prevent big replacement
costs tomorrow. Many millionaires are meticulous about maintenance for exactly this reason.""",
"""Skipping maintenance is a false saving. A neglected car can need expensive repairs years earlier than a
maintained one. A neglected roof can damage the whole house. Taking care of what you own is one of the most
reliable ways to spend less over time.""",
"""Apply the rule. Find your car's maintenance schedule in the owner's manual and follow it. Do the same for
your home, with a simple yearly checklist. Fix small problems early, before they turn into big ones.""",
"Mechanic changing oil", "MAINTENANCE",
"Home roof repair", "SMALL COSTS PREVENT BIG ONES",
"Owner's manual maintenance schedule", "FOLLOW THE SCHEDULE")

item(12, "Borrow only for things that grow", "or not at all",
"""Rule number twelve. Don't borrow for things that lose value.""",
"""Many financially careful people follow a simple principle. Borrowing might make sense for things that can
grow in value or income, like a reasonable mortgage, an education with a clear payoff, or a business. But
borrowing for things that lose value, like cars, vacations and electronics, makes you poorer twice. You pay
interest on something that's shrinking.""",
"""Car loans are the most common example. You pay interest every month on an asset that's losing value every
month. That's why so many millionaires prefer to pay cash for cars, or at least keep loans short, even when they
could easily afford the payments.""",
"""Apply the rule. Look at every loan you have. Is it for something that grows, or something that shrinks?
Prioritize paying off the loans on shrinking things first, especially if they have high interest rates.""",
"Home with growing value chart", "BORROW FOR GROWTH",
"Car losing value chart", "INTEREST ON A SHRINKING ASSET",
"List of loans on paper", "PAY OFF THE SHRINKERS")

item(13, "Insure smart", "protect against disasters",
"""Rule number thirteen. Insure against disasters, not inconveniences.""",
"""Older cars often don't need the same insurance as new ones. Once a car's value drops, some owners decide
that collision coverage costs more than it's worth, especially if they have the savings to replace the car.
Raising deductibles, when you have an emergency fund, can also lower premiums.""",
"""The bigger principle is that wealthy people insure against losses they couldn't handle, like liability in
a serious accident, while self insuring small losses. That's why liability coverage stays important even on an
old car. A serious accident can lead to costs far bigger than the car itself.""",
"""Apply the rule. Check your car insurance this year. Compare what you pay for collision coverage with what
the car is actually worth. Make sure your liability limits are high enough. And shop around for quotes at least
once a year.""",
"Car insurance policy documents", "INSURE SMART",
"Car accident scene", "LIABILITY MATTERS",
"Comparing insurance quotes", "SHOP EVERY YEAR")

item(14, "Automate the good choices", "make wealth the default",
"""Rule number fourteen. Make good decisions automatic.""",
"""Millionaires who drive old cars aren't superhuman. Many have simply set up systems so the right choices
happen without effort. Automatic transfers to retirement accounts, automatic payments into a car fund, automatic
bill payments so late fees never happen.""",
"""Automation protects you from your own worst moments. If money is moved to investments on payday, there's
less sitting in checking to be tempted by a new car ad. The default becomes saving, and spending becomes the
active choice.""",
"""Apply the rule. This week, set up three automatic transfers. One to retirement, one to an emergency fund,
and one to a car fund. Start small. You can always increase them later.""",
"Automatic payment settings screen", "AUTOMATE IT",
"Paycheck splitting into accounts", "SAVING BY DEFAULT",
"Three savings accounts on app", "THREE TRANSFERS")

item(15, "Spend big on what you love", "and cut ruthlessly on the rest",
"""And rule number fifteen. Spend lavishly on what you love, and cut ruthlessly on what you don't.""",
"""Personal finance author Ramit Sethi calls this conscious spending. The idea is that being good with money
doesn't mean cutting everything. It means deciding what you truly value, spending freely on that, and cutting
costs mercilessly on things you don't care about.""",
"""That's exactly why so many millionaires drive old cars. They don't care about cars, so they spend as little
as possible on them. But many spend generously on things they value, like travel, their kids' education,
charity or a hobby. Their spending isn't small. It's focused. And because it's focused, it actually makes them happier than spending
a little bit on everything ever could.""",
"""Apply the rule. Write down three things you truly love spending money on. Then write down three things you
spend on but don't really care about. Cut the second list, and feel free to enjoy the first. That's not being
cheap. It's being intentional.""",
"Person enjoying hobby painting", "SPEND ON WHAT YOU LOVE",
"Family traveling abroad", "FOCUSED, NOT SMALL",
"Two lists on notebook", "LOVE IT OR CUT IT")

# ---------------- How to buy ----------------
ch("How to buy a car the millionaire way")
pr("""Now let's make this practical. Here's how to buy your next car the way a quiet millionaire would, step by
step.""")
sc("""Step one. Decide your budget before you shop, based on the full cost of ownership, not the payment. A rule
of thumb many personal finance writers use is to keep your total vehicle costs, including payment, insurance and
fuel, to a modest share of your take home pay, often suggested as around ten to fifteen percent. Write the
number down before you ever set foot on a lot, because dealerships are designed to make you forget it.""",
   "Budget notebook and pen", "STEP 1: SET THE BUDGET")
sc("""Step two. Pick models known for reliability. Look at reliability ratings from sources like Consumer
Reports, and check crash safety ratings from the Insurance Institute for Highway Safety. Reliable mainstream
models tend to hold their value reasonably well and cost less to repair. A boring car with a great reliability
record is often the smartest purchase on the lot.""",
   "Car reliability ratings magazine", "STEP 2: CHOOSE RELIABLE")
sc("""Step three. Check the history and get an inspection. Run a vehicle history report to check for accidents,
flood damage and title problems. Then pay an independent mechanic to inspect the car before you buy. It usually
costs a modest fee and can save you from a very expensive mistake. Sellers who refuse an inspection are telling
you something.""",
   "Mechanic inspecting car underside", "STEP 3: INSPECT IT")
sc("""Step four. Arrange financing before you shop, if you need it. Credit unions and banks often offer better
rates than dealer financing. With a pre approval in hand, you can negotiate on the total price, not the monthly
payment. Step five. Negotiate the out the door price, which includes taxes and fees. And be ready to walk away.
There are always more cars.""",
   "Credit union branch", "STEPS 4 AND 5: FINANCE AND NEGOTIATE")
sc("""Step six. Say no to the extras in the finance office. Extended warranties, paint protection, fabric
protection, and other add ons are often heavily marked up. If you want a warranty, you can research options
separately and take your time. And step seven. Once you drive home, start your car fund immediately, so the next
car is paid for before you need it.""",
   "Finance office paperwork", "STEPS 6 AND 7: NO EXTRAS, START THE FUND")

# ---------------- Life stage ----------------
ch("Your car plan at every stage")
sc("""In your twenties, the car rule matters most, because every dollar not spent on a car can compound for
forty years. A reliable used car, paid in cash or with a short loan, is one of the best financial decisions a
young person can make. Many people who become millionaires look back on driving a cheap car in their twenties as
a turning point.""",
   "Young driver with old car", "IN YOUR 20s")
sc("""In your thirties and forties, family needs often grow. Safety and space matter more. That's fine. The
same rules apply. Buy a few years old, choose reliability, keep it long, and avoid long loans. A minivan you keep
for twelve years can be a fantastic financial decision. Two car households can also stagger purchases so they're
never replacing both cars at once.""",
   "Family minivan in driveway", "IN YOUR 30s AND 40s")
sc("""In your fifties and beyond, many people finally have the financial room to buy a nicer car. If your
retirement is on track, a car you truly enjoy might be part of your conscious spending. Just remember that every
car is still a depreciating asset, and that money spent on cars close to retirement has fewer years to recover.""",
   "Older couple with car on road trip", "IN YOUR 50s AND BEYOND")

# ---------------- Mistakes ----------------
ch("The five most expensive car mistakes")
sc("""Let's look at the car mistakes that cost people the most. Mistake one. Rolling negative equity into a new
loan. If you owe more than your car is worth and trade it in, the dealer may add the leftover balance to your new
loan. You start the new car already underwater, paying interest on a car you no longer own.""",
   "Underwater car concept", "MISTAKE 1: ROLLING NEGATIVE EQUITY")
sc("""Mistake two. Shopping by monthly payment. When the only question is what payment you can handle, a
seller can stretch the loan, add extras and raise the price, all while keeping the payment the same. Mistake
three. Leasing forever. Leasing can make sense in some situations, but leasing one car after another means you
always have a payment and never own anything.""",
   "Lease agreement document", "MISTAKES 2 AND 3")
sc("""Mistake four. Buying more car than your life needs. A large truck or SUV for a solo commute costs more in
fuel, insurance and depreciation. Buy for the life you actually live, not the one in the commercial. And mistake
five. Skipping maintenance to save money, which often turns a cheap fix into an expensive repair, and shortens
the life of the car.""",
   "Large truck in city traffic", "MISTAKES 4 AND 5")

# ---------------- Beyond cars ----------------
ch("The old car rule for everything else")
sc("""Here's the bigger lesson. The old car rule works for almost everything you buy. Houses. Buy what you
need, take care of it, and stay long enough to avoid the costs of moving again and again. Phones. Keep them until
they genuinely stop working well. Clothes. Buy quality where it matters, wear it for years, and skip the trends.""",
   "Well kept old house", "THE RULE FOR EVERYTHING")
sc("""The pattern is always the same. Buy something good enough, often slightly used. Take care of it. Keep it
much longer than most people do. And invest the money you didn't spend on upgrades. Do that across your whole
life, and the results can be enormous, because you're not just saving on one car. You're saving on hundreds of
purchases over decades.""",
   "Quality leather boots worn", "GOOD ENOUGH, KEPT LONG")
sc("""That's really why rich people drive old cars. It's not one decision. It's a philosophy that shows up
everywhere in their lives. The car is just the most visible example, because it's sitting right there in the
driveway for everyone to see.""",
   "Driveway with older sedan", "THE VISIBLE EXAMPLE")

# ---------------- Real examples ----------------
ch("Real people, old cars")
pr("""Let me give you a few real examples of wealthy people who are famous for modest cars.""")
sc("""Warren Buffett, one of the richest people in the world, has been known for years for driving ordinary
cars and keeping them a long time. He has joked in interviews that he only drives a few thousand miles a year,
so he doesn't need a new car very often. For a man worth well over one hundred billion dollars, the car simply
isn't important.""",
   "Omaha Nebraska street", "WARREN BUFFETT")
sc("""And then there are the quiet millionaires you'll never hear about. The retired teacher with a paid off
house and a twelve year old Camry. The plumber who owns his business and drives a work truck with two hundred
thousand miles on it. The engineer who bought a three year old minivan and drove it until her kids went to
college. Stanley's research is full of people like them.""",
   "Pickup truck work site", "THE QUIET MILLIONAIRES")
sc("""None of them are depriving themselves. They still enjoy road trips, family vacations and nice dinners. They just decided, long
ago, that the car wasn't where they wanted their money to go. Over decades, that one decision freed up a fortune. And that fortune bought them something no
car can buy, which is freedom.""",
   "Couple watching sunset", "FREEDOM")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. Aren't old cars unsafe? Safety has improved a lot over the years, so it's worth checking
crash test ratings from the Insurance Institute for Highway Safety and the government's NHTSA before you buy. But
many cars that are a few years old have excellent safety features. Driving a modest car doesn't mean driving an
unsafe one.""",
   "Car crash test dummy", "ARE OLD CARS SAFE?")
sc("""Question two. Don't repairs on an old car cost more than a payment? Sometimes, but often not. Even a
major repair costing a couple thousand dollars is usually far less than a year of new car payments. The key is to
budget for repairs in advance with a car fund, so they don't become emergencies.""",
   "Auto repair shop", "REPAIRS VS PAYMENTS")
sc("""Question three. What about electric cars? Many electric cars cost less to fuel and maintain, which can
help the total cost. The same rules still apply. Consider buying used, check the battery warranty and condition,
keep it a long time, and calculate the full cost of ownership.""",
   "Electric car charging", "WHAT ABOUT EVs?")
sc("""Question four. Can I ever buy my dream car? Absolutely. If you love cars, it can be part of your conscious
spending. The millionaire way is to buy it after you've built a strong financial base, pay cash or keep the loan
short, and cut costs elsewhere to make room for it.""",
   "Classic sports car at show", "THE DREAM CAR")
sc("""Question five. What if I need a reliable car for work? Then reliability is exactly what you should pay
for. Choose models with strong reliability ratings, have a trusted mechanic inspect any used car before buying,
and keep an emergency fund so a breakdown doesn't threaten your job.""",
   "Mechanic inspecting used car", "RELIABILITY FOR WORK")
sc("""Question six. Should I lease or buy? For most people who want to minimize lifetime car costs, buying a
reliable car and keeping it for many years tends to be cheaper than leasing one car after another. Leasing can
make sense for some business owners or people who drive very few miles and want a new car every few years, but
it means a permanent payment. Read every lease term carefully, especially mileage limits and wear charges.""",
   "Car keys and lease document", "LEASE OR BUY?")
sc("""Question seven. How do I start a car fund if I still have a car loan? Start small now, even fifty dollars a
month, while you finish the loan. When the loan is paid off, add the full old payment to the fund. In a few years,
you'll have enough to buy your next car in cash, and you'll never need a car loan again. That one cycle change
can save you thousands in interest over your lifetime.""",
   "Piggy bank with car keys", "STARTING A CAR FUND")

# ---------------- Recap ----------------
ch("Recap: all 15 rules")
sc("""Quick recap. Angle one, the numbers. Let someone else pay the depreciation, keep it ten years or more,
know the full cost, pay cash or keep loans short, and invest the difference.""",
   "Checklist on clipboard", "THE NUMBERS: 1 TO 5")
sc("""Angle two, the psychology. A car is transportation, not identity. Nobody is watching as much as you
think. Wealth is what you don't see. Delay gratification. And escape the hedonic treadmill.""",
   "Person thinking at window", "THE PSYCHOLOGY: 6 TO 10")
sc("""Angle three, the playbook. Maintenance beats replacement, borrow only for things that grow, insure smart,
automate the good choices, and spend big on what you love while cutting ruthlessly on the rest.""",
   "Notebook with plan", "THE PLAYBOOK: 11 TO 15")

# ---------------- Close ----------------
ch("What to do next")
pr("""Here's the big idea one more time. A car is one of the largest purchases most people make, over and over,
for their entire lives. Getting that one decision right, again and again, can be worth more than almost any
investment tip you'll ever hear. Buy reliable, buy slightly used, keep it long, and invest the difference. So
next time you see an old car in a nice neighborhood, don't assume the owner is struggling. They might be
the richest person on the street. If you want the full plan for building that kind of quiet wealth, it's in my
playbook, linked in the description. Tell me in the comments how old your car is. I'm Ryan Rover. See you in the
next one.""")

save("video26", "Why Rich People Drive Old Cars: 15 Money Rules From Real Millionaires", [
    "Thomas J. Stanley, Stop Acting Rich (2009): median price millionaires paid for most recent vehicle about $31,000; The Millionaire Next Door (1996)",
    "Kelley Blue Book, average new-vehicle transaction price above $50,000 (2025); Edmunds, loan terms and monthly payments",
    "Carfax and Edmunds, depreciation estimates",
    "S&P Global Mobility, average age of US light vehicles (record above 12.5 years)",
    "AAA, Your Driving Costs (more than $12,000 a year to own and operate a new vehicle)",
    "Morgan Housel, The Psychology of Money (2020): the man in the car paradox",
    "Gilovich, Medvec and Savitsky, The Spotlight Effect in Social Judgment (1999); Mischel, Stanford marshmallow studies, and later replication by Watts, Duncan and Quan (2018)",
    "Ramit Sethi, I Will Teach You to Be Rich (conscious spending)",
    "Growth example: monthly compounding at 7% average yearly return (illustration, not a promise)",
], "why rich people drive old cars, 15 rules from 3 angles: numbers, psychology, playbook")
