import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short


def item(n, title, sub, card_text, body, example, q1, c1, q2, c2):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"TRUTH {n}")
    sc(body, q1, c1)
    sc(example, q2, c2)

# ---------------- Intro ----------------
ch("Intro")
short("Everyone wants a million dollars. Almost nobody knows what it buys.")
pr("""Hi, I'm Ryan Rover. One million dollars. For a hundred years it's been the number. The word millionaire
still means rich to most people. But here's a question almost nobody asks. What does one million dollars
actually buy you, in real life, in twenty twenty seven? Because the answer is very different from what most
people imagine.""")
card("""One million dollars. Seven figures. The number on the lottery ticket, the number in the movies. Today
we're going to take it apart, and see what's really inside.""",
     {"type": "stat", "label": "the magic number", "big": "$1,000,000", "sub": "what it really buys in 2027"})
sc("""Some people think a million dollars means never working again, a mansion, and a sports car. Others think
it's not much money anymore. The truth sits in between, and it depends on three things: how you hold the
money, where you live, and how you spend. Get those right, and a million dollars can buy you something more
valuable than any car. Get them wrong, and it can disappear in a few years.""",
   "Sports car luxury", "MANSION AND SPORTS CAR?")
sc("""So we'll look at it from three angles. First, the numbers: what a million is worth after inflation, taxes
and fees. Then the psychology: why a million feels so different from what people expect. And finally the
playbook: how to make a million dollars actually work for you. Along the way, fifteen hard truths about seven
figures.""",
   "Calculator with financial charts", "3 ANGLES, 15 TRUTHS")
pr("""Let's start with a quick word on where the numbers come from.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Inflation figures come from the Bureau of Labor Statistics consumer price index. Household spending comes
from the Bureau of Labor Statistics Consumer Expenditure Survey. Home prices come from the National Association
of Realtors. Social Security amounts come from the Social Security Administration, and health insurance costs
from KFF's employer health benefits survey.""",
   "Bureau of Labor Statistics building", "OUR SOURCES")
sc("""Whenever we show growth, we use a seven percent average yearly return as an illustration. Withdrawal
examples use the well known four percent rule of thumb, which is a starting point, not a guarantee. This video
is education, not financial advice. Your taxes, your health and your city all change the math.""",
   "Calculator and pen on financial papers", "EDUCATION, NOT ADVICE")

# ---------------- Angle 1: numbers ----------------
ch("Angle 1: The numbers")
pr("""Angle one. The numbers. Let's put one million dollars on the table and see what it really turns into.""")
card("""The most common way to think about it is the four percent rule of thumb. Withdraw four percent in the
first year, then adjust for inflation. On one million dollars, that's about forty thousand dollars a year, before
taxes.""",
     {"type": "compare", "left": {"label": "Invested", "big": "$1,000,000", "sub": "a balanced portfolio"},
      "right": {"label": "Yearly income", "big": "~$40,000", "sub": "4% rule of thumb, before tax"},
      "note": "Rule of thumb from Bengen (1994). Not a guarantee."})
sc("""Forty thousand dollars a year. Let that sink in. That's a real income, and you never have to go to work for
it. But it's also far less than most people imagine when they think of a millionaire. It's roughly what a
full time job paying about twenty dollars an hour earns. Comfortable in many places. Not a mansion, not a
yacht.""",
   "Office building at dusk", "ABOUT $40,000 A YEAR")
card("""Now compare that with what Americans actually spend. The Bureau of Labor Statistics found the average
household spent about seventy seven thousand dollars in twenty twenty three. At that spending, one million
dollars covers about thirteen years if it earned nothing at all.""",
     {"type": "compare", "left": {"label": "Average household", "big": "$77,280", "sub": "spent per year (BLS 2023)"},
      "right": {"label": "$1M covers", "big": "~13 years", "sub": "with zero growth"},
      "note": "Bureau of Labor Statistics, Consumer Expenditure Survey 2023"})
sc("""Of course, a million dollars that's invested doesn't sit still. That's the whole point. But this comparison
shows why a million isn't the endless pile of money it sounds like. Spend like the average household, and you'd
need closer to two million dollars invested to support that lifestyle with the four percent rule. That's why
your spending is just as important as your balance.""",
   "Suburban houses street United States", "SPENDING DECIDES")
sc("""And here's a number that surprises people. In Charles Schwab's Modern Wealth Survey from twenty twenty four,
Americans said it takes about two and a half million dollars to be considered wealthy. So by the public's own
definition, a millionaire isn't wealthy anymore. A million dollars has quietly moved from rich to comfortable.""",
   "New York City skyline", "RICH OR COMFORTABLE?")
pr("""So now let's go through the fifteen hard truths about one million dollars. Some will surprise you, a few might
annoy you, and one or two could change the way you plan your whole financial life. Let's start with the one nobody
puts in the movies.""")

# ---------------- Items ----------------
item(1, "Inflation cut it in half", "a 1990s million is worth double",
"""Truth number one. Inflation has already cut the million dollars in half.""",
"""According to the consumer price index from the Bureau of Labor Statistics, prices have roughly doubled since
the mid nineteen nineties. That means one million dollars today buys about what five hundred thousand dollars
bought back then. When your parents dreamed of being millionaires, they were dreaming of something worth twice
as much as today's million.""",
"""And inflation doesn't stop. At an average of three percent a year, prices double again in about twenty four
years. So if you're thirty today and you reach one million at fifty five, that million might buy what about five
hundred thousand buys now. Try this: when you set a money goal for the far future, think in today's dollars.
It keeps you honest about what you'll really need.""",
"Old dollar bills vintage", "PRICES DOUBLED",
"Grocery store shelves prices", "THINK IN TODAY'S DOLLARS")

item(2, "It's about $40,000 a year", "the 4% rule of thumb",
"""Truth number two. As an income, a million dollars is about forty thousand dollars a year.""",
"""This comes from research by financial planner William Bengen, published in nineteen ninety four. He looked at
historical market returns and found that withdrawing about four percent in the first year, then adjusting for
inflation, lasted at least thirty years in every period he studied. It became famous as the four percent rule.""",
"""But it's a rule of thumb, not a law. If you retire right before a big crash, or if inflation runs hot, the
math gets tighter. And if you retire young, your money needs to last fifty years, not thirty, so many planners
suggest something closer to three or three and a half percent. At three and a half percent, one million dollars
supports about thirty five thousand dollars a year.""",
"Retired couple on porch", "$1M = ~$40K A YEAR",
"Stock market chart on screen", "NOT A LAW")

item(3, "A house, and then nothing", "two and a half median homes",
"""Truth number three. You could buy about two and a half typical homes, and then you'd have nothing to live on.""",
"""The National Association of Realtors reports the median price of an existing home sold in the United States
was a little over four hundred thousand dollars in twenty twenty five. So a million dollars could buy two typical
homes outright, with change left over. Sounds amazing. But a house doesn't pay your grocery bill. It costs money
every year: taxes, insurance, repairs.""",
"""Here's the trap. Put six hundred thousand into a house, and you have four hundred thousand left invested.
At the four percent rule, that's sixteen thousand dollars a year. And the house still costs maybe eight to twelve
thousand a year to own. Try this: if you ever get a large sum, decide how much income you need first, and only
then decide how much house you can afford.""",
"House with for sale sign", "~$400K MEDIAN HOME",
"House repair roof", "HOUSES COST MONEY")

item(4, "Location changes everything", "same million, different life",
"""Truth number four. Where you live can double or halve what your million buys.""",
"""Forty thousand dollars a year in a small town in the Midwest or the South is a comfortable life. The same forty
thousand in San Francisco, New York City or Boston barely covers rent. Housing is the biggest expense for most
households, and housing costs vary enormously between cities.""",
"""This is why some people retire to lower cost areas, or even abroad, and suddenly their million feels like two.
But moving has real costs too: leaving family, friends and a familiar doctor. Try this: look up the cost of living
in two or three places you'd actually enjoy living. Compare them with where you are now. The difference might be
the most powerful money move you have.""",
"Small town main street", "SAME MONEY, DIFFERENT LIFE",
"Map and compass", "CHOOSE YOUR CITY")

item(5, "Taxes take a slice", "not all millions are equal",
"""Truth number five. Not every million dollars is the same, because of taxes.""",
"""One million dollars in a traditional 401k or IRA has never been taxed. When you take money out, it's taxed as
regular income. One million in a Roth account has already been taxed, so qualified withdrawals are tax free. And
one million in a regular brokerage account is somewhere in between: you pay tax on the gains when you sell, often
at lower long term capital gains rates.""",
"""So a million in a traditional account might really be worth something like eight hundred thousand to eight
hundred fifty thousand after taxes, depending on your bracket. Try this: if you have retirement savings, look at
which type of account they're in. Having a mix of taxable, tax deferred and tax free money gives you a lot more
control later. Tax rules change, so check the current IRS limits each year.""",
"Tax forms on desk", "TAXES CHANGE THE NUMBER",
"Paperwork documents desk", "KNOW YOUR ACCOUNT TYPE")

item(6, "Fees can eat a quarter", "1% of $1M is $10,000",
"""Truth number six. Fees can eat a huge share of your income.""",
"""A one percent yearly advisory fee on one million dollars is ten thousand dollars a year. If your safe income is
forty thousand, that fee is a quarter of it. Add fund expenses on top, and some people pay one and a half percent
or more without realizing it.""",
"""That doesn't mean advice is never worth paying for. A good advisor can save you from expensive mistakes,
especially with taxes and big decisions. But you should know exactly what you're paying in dollars, and what you get
for it. Try this: ask for every fee in writing, as a yearly dollar amount. If someone can't give you that clearly, it
tells you something.""",
"Receipt and coins on table", "1% = $10,000 A YEAR",
"Business meeting handshake", "ASK IN DOLLARS")

short("Before sixty five, health insurance can eat half your million dollar income.")
item(7, "Health insurance is the hidden bill", "before Medicare at 65",
"""Truth number seven. If you stop working before sixty five, health insurance becomes a big bill.""",
"""Most Americans get health insurance through work. KFF's employer health benefits survey found the average total
yearly premium for family coverage was close to twenty seven thousand dollars in twenty twenty five, with employers
paying most of it. When you leave your job, you pay the whole thing, or buy a plan on the marketplace.""",
"""For an early retiree living on forty thousand a year, health insurance can be one of the largest costs. Marketplace
subsidies depend on your income, and the rules have changed several times. Try this: before you plan any early
retirement, get a real quote for health insurance at the income you'd have. It's the number that breaks more early
retirement plans than any market crash.""",
"Hospital building exterior", "THE HIDDEN BILL",
"Doctor with stethoscope", "GET A REAL QUOTE")

item(8, "Social Security helps a lot", "the second income",
"""Truth number eight. For most retirees, Social Security makes a million dollars go much further.""",
"""The Social Security Administration reported that the average retired worker received around two thousand
dollars a month in twenty twenty five. That's about twenty four thousand dollars a year, adjusted for inflation. For
a married couple where both worked, it can be close to double.""",
"""So picture a retired couple with one million dollars invested. Forty thousand from the four percent rule, plus
perhaps forty thousand or more from two Social Security checks. That's eighty thousand dollars a year, above what
the average household spends. Try this: create an account at ssa dot gov and look at your own estimated benefit. It
changes how much you really need to save.""",
"Social Security card", "~$2,000 A MONTH",
"Retired couple walking in park", "TWO INCOMES")

item(9, "Early retirement is harder", "a million at 35 is not a million at 65",
"""Truth number nine. One million dollars at sixty five and one million at thirty five are completely different.""",
"""At sixty five, your money needs to last maybe twenty five or thirty years. You're getting Social Security and
Medicare. At thirty five, your money might need to last fifty or sixty years, with no Social Security for decades,
paying for health insurance yourself, and maybe raising kids.""",
"""That's why the early retirement community often aims for twenty five to thirty three times their yearly
spending, and keeps their costs low. A thirty five year old spending thirty thousand dollars a year might do it with a
million. A thirty five year old spending sixty thousand would need much more. Try this: divide your investments by your
yearly spending. That number, your years of freedom, is what really matters.""",
"Young couple hiking mountains", "35 IS NOT 65",
"Hourglass sand timer", "YEARS OF FREEDOM")

pr("""Quick pause. If these hard truths are useful, I've got videos coming on every step from zero to one million.
Subscribe so you don't miss them. It's free, and it really helps the channel. Now, truth number ten.""")

item(10, "Investing makes it grow", "it doubles in about 10 years",
"""Truth number ten. If you don't touch it, a million dollars can grow surprisingly fast.""",
"""At a seven percent average yearly return, money roughly doubles every ten years. That's the rule of seventy two.
So one million dollars left alone could become about two million in a decade. Not guaranteed, because markets go up
and down, but historically, patient investors in broad markets have been rewarded over long periods.""",
"""This is why people who reach a million in their forties or early fifties often keep working a bit longer, even
part time. A few extra years without withdrawals can change everything. Try this: if you're close to a big
milestone, run the math on working two more years versus stopping now. The difference is often bigger than people
expect.""",
"Snowball rolling in snow", "DOUBLES IN ~10 YEARS",
"Calendar planning", "TWO MORE YEARS")

card("""Here's what that looks like. One million dollars, nothing added, at a seven percent illustration, grows to
roughly two million dollars in ten years.""",
     {"type": "compare", "left": {"label": "Today", "big": "$1,000,000", "sub": "nothing added"},
      "right": {"label": "10 years", "big": "~$2,000,000", "sub": "at 7% a year"},
      "note": "Illustration. Returns are not guaranteed."})

item(11, "Spending is the real dial", "cut $10,000, need $250,000 less",
"""Truth number eleven. Your spending is the most powerful dial you have.""",
"""Here's a quick trick from the four percent rule. Every ten thousand dollars a year you don't need to spend means
you need about two hundred fifty thousand dollars less invested. Cut your yearly costs by twenty thousand, and your
finish line moves half a million dollars closer.""",
"""That's why people who reach financial independence on ordinary salaries obsess over a few big costs: housing,
cars and food. Small savings help, but the big three move the number. Try this: take your yearly spending and
multiply by twenty five. That's your personal number. Then see how it changes if you cut your biggest expense by
ten percent.""",
"Luxury car dealership", "-$10K SPENDING = -$250K NEEDED",
"Spreadsheet on laptop", "YOUR NUMBER = SPENDING x 25")

item(12, "It buys choices", "the real value of a million",
"""Truth number twelve. What a million really buys is choices.""",
"""Ask people who have reached a million what changed, and they rarely say stuff. They say options. They could turn
down a bad job. They could take a lower paying job they love. They could take care of a parent, start a business, or
take a year off without panic. The money became a kind of shield.""",
"""Even before you reach a million, you get pieces of this. One hundred thousand buys some choices. Five hundred
thousand buys more. That's why the journey matters as much as the destination. Try this: write down three choices
you wish you could make right now. Those are the real reasons you're saving.""",
"Person standing at crossroads", "MONEY BUYS OPTIONS",
"Notebook with financial notes", "WRITE YOUR REASONS")

item(13, "Lifestyle can burn it fast", "big upgrades eat seven figures",
"""Truth number thirteen. A million dollars can disappear faster than you think.""",
"""Studies of athletes and sudden windfalls have found that a big pile of money doesn't automatically protect people
from financial trouble. A study published by the National Bureau of Economic Research found that a significant share of
former NFL players faced bankruptcy within about a dozen years of retiring, despite earning millions.""",
"""The pattern is usually the same. Big house, several cars, generous gifts, risky investments with friends. Each one
feels fine on its own. Together, they burn through seven figures. Try this: if you ever receive a large sum, park it
in a safe account for six months before making any big decision. Time is the best protection against emotional
spending.""",
"American football stadium", "WINDFALLS DISAPPEAR",
"Bank vault door", "WAIT SIX MONTHS")

item(14, "Most millionaires look ordinary", "the quiet millionaire",
"""Truth number fourteen. Most millionaires don't look like millionaires.""",
"""UBS estimates there are more than twenty million millionaires in the United States. Most are not famous. Many
are people in their fifties and sixties who owned a home for decades, saved in workplace retirement plans, and kept
their spending under control. The classic book The Millionaire Next Door, by Thomas Stanley and William Danko, found
the same thing back in the nineteen nineties.""",
"""In other words, the people who look rich are often spending their wealth, and the people who are actually rich
are often keeping it. Try this: next time you see a fancy car, remember you're seeing what someone spent, not what
they have. It makes comparison a lot less powerful.""",
"Suburban houses street United States", "QUIET MILLIONAIRES",
"Old car parked on street", "SPENT VS KEPT")

item(15, "It's reachable", "the math of an ordinary million",
"""Truth number fifteen. A million dollars is more reachable than most people believe.""",
"""One thousand dollars a month, invested for thirty years at a seven percent average yearly return, grows to roughly
one point two million dollars. You'd put in three hundred sixty thousand. The rest is growth. For a couple putting a
combined fifteen percent of a hundred thousand dollar income into retirement accounts, that's not a fantasy. It's a
plan.""",
"""And employer matches make it faster. If your employer matches part of your contributions, that's free money added
every month. Try this: find out exactly what your workplace plan matches, and make sure you get every dollar of it. It's
the easiest raise you'll ever get.""",
"Graph trending upward", "$1,000 A MONTH x 30 YEARS",
"Office workers meeting", "GET THE FULL MATCH")

card("""On screen: one thousand dollars a month for thirty years at a seven percent illustration. About one point two
million dollars at the end, from three hundred sixty thousand of contributions.""",
     {"type": "growth", "monthly": 1000, "rate": 0.07, "years": 30})

# ---------------- Price of a million by age ----------------
ch("The price of a million at every age")
pr("""So what does it cost to build one million dollars by sixty five? The answer depends almost entirely on when
you start. Watch how fast the price goes up.""")
card("""Start at twenty five, and you have forty years. At a seven percent illustration, about three hundred eighty
dollars a month gets you to one million by sixty five. That's less than many car payments.""",
     {"type": "compare", "left": {"label": "Start at 25", "big": "~$380/mo", "sub": "40 years to $1M"},
      "right": {"label": "Start at 35", "big": "~$820/mo", "sub": "30 years to $1M"},
      "note": "Illustration at 7% a year, compounded monthly. Not guaranteed."})
sc("""Wait ten years and start at thirty five, and the monthly price more than doubles, to about eight hundred
twenty dollars. That's the cost of waiting a decade. Not ten percent more. More than double. Every year you wait,
the mountain gets steeper, because you lose the years when compounding does its best work.""",
   "Wall clock office", "THE COST OF WAITING")
card("""Start at forty five, with twenty years to go, and it's about nineteen hundred twenty dollars a month. Start at
fifty, with fifteen years, and it's over three thousand a month.""",
     {"type": "compare", "left": {"label": "Start at 45", "big": "~$1,920/mo", "sub": "20 years to $1M"},
      "right": {"label": "Start at 50", "big": "~$3,160/mo", "sub": "15 years to $1M"},
      "note": "Illustration at 7% a year, compounded monthly. Not guaranteed."})
sc("""Now, don't let that discourage you if you're older. People in their forties and fifties usually earn more than
they did at twenty five, their kids may be grown, and the mortgage may be shrinking. And employer matches and catch up
contributions, which the IRS allows for people fifty and over, can carry part of the load. The point isn't that it's
too late. The point is that the best day to start is always today.""",
   "Older man reading financial newspaper", "NEVER TOO LATE")
sc("""And if you're young, this is the most valuable thing you'll hear all year. Three hundred eighty dollars a
month, starting at twenty five, can do what three thousand a month does starting at fifty. Your biggest financial
asset isn't your salary. It's your time. Spend it wisely.""",
   "Young people graduation", "YOUR TIME IS YOUR ASSET")

# ---------------- Three millionaires ----------------
short("Three people have one million dollars. Only one of them is free.")
ch("Three people, one million each")
pr("""To make all of this real, let's meet three example people who each have exactly one million dollars. They're
made up, but the math is real, and you'll probably recognize someone you know.""")
sc("""Person one. Linda is sixty six and lives in a paid off house in a mid sized city in Ohio. Her one million is
invested in a mix of stock and bond index funds. She withdraws about forty thousand a year, and she and her late
husband's Social Security records give her around thirty thousand more. Her total costs are about fifty five thousand.
Linda has a surplus every year. She travels, helps her grandkids, and never checks the market.""",
   "Retired woman gardening", "LINDA: FREE")
sc("""Person two. Kevin is forty one, lives in San Diego, and has one million dollars, but six hundred thousand of it
is the equity in his house. He has four hundred thousand invested and a mortgage payment of four thousand dollars a
month. On paper he's a millionaire. In practice, his investments could support about sixteen thousand dollars a year,
and his costs are over ninety thousand. Kevin has to keep working, and he feels it.""",
   "San Diego skyline", "KEVIN: HOUSE RICH")
sc("""Kevin isn't doing anything wrong. He has a valuable home and good savings. But his million is mostly locked in a
place he lives, and his costs are set by an expensive city. His most powerful options are to keep investing, pay down
the mortgage over time, or one day move somewhere cheaper and unlock that equity. Many millionaires on paper are in
exactly his position.""",
   "Suburban houses street United States", "MILLIONAIRE ON PAPER")
sc("""Person three. Priya is thirty four, rents a modest apartment, and has one million dollars invested across a
401k, a Roth IRA and a brokerage account. She spends thirty five thousand dollars a year. Using a more cautious three
and a half percent, her investments could support about thirty five thousand a year. She's technically financially
independent, at thirty four.""",
   "Young woman working on laptop", "PRIYA: INDEPENDENT AT 34")
sc("""But Priya's money has to last fifty years or more, she pays for her own health insurance if she stops working,
and she can't touch most of her retirement accounts without penalties until fifty nine and a half, except through
specific IRS rules. So she chooses a middle path. She keeps working, but part time, at a job she enjoys. Her million
bought her the freedom to choose.""",
   "Person working from home laptop", "FREEDOM TO CHOOSE")
sc("""Same number, three completely different lives. Linda is free. Kevin is house rich and cash tight. Priya has
options. What made the difference wasn't the million. It was where it was held, how much they spent, and how many
years it had to last. That's the whole video in three people.""",
   "Three people silhouettes", "SAME NUMBER, 3 LIVES")

# ---------------- How it disappears ----------------
ch("Five ways a million disappears")
pr("""Now the scary part. Here are five common ways a million dollars quietly disappears. Avoid these, and you're ahead of
most people who ever reach seven figures.""")
sc("""One. Withdrawing too much, too early. Taking eight or ten percent a year can feel fine for a while, especially in a
rising market. But at that rate, a long bad stretch can drain the money in a couple of decades or less. The early years
matter most, because losses then hit a bigger balance and leave less time to recover. Planners call this sequence of
returns risk.""",
   "Stock market crash newspaper", "1. WITHDRAWING TOO MUCH")
sc("""Two. Panic selling in a crash. Broad stock markets have fallen by a third or more several times in the last
hundred years, and recovered every time so far, though the past is no guarantee. People who sold at the bottom locked in
the loss. People who held on, or kept buying, usually came out ahead. Three. Concentration. Putting a big share into one
stock, one property or one business. If it fails, you fall several levels at once.""",
   "Stock market chart falling on screen", "2. PANIC  3. CONCENTRATION")
sc("""Four. Lending and gifting without limits. When people learn you have money, requests arrive. Family, friends,
business ideas. Helping people you love can be wonderful, but set a yearly amount you can give without hurting your own
plan, and stick to it. A no today can protect your ability to say yes for decades.""",
   "Family dinner table", "4. LENDING WITHOUT LIMITS")
sc("""Five. Scams and too good to be true investments. Fake crypto platforms, romance scams, guaranteed returns, urgent
calls pretending to be your bank. The FBI's Internet Crime Complaint Center reports billions of dollars in losses every
year, and older Americans report some of the largest losses. If anyone pressures you to act fast, or promises high
returns with no risk, stop and hang up.""",
   "Computer hacker keyboard", "5. SCAMS")

# ---------------- Angle 2: psychology ----------------
short("Why does a million dollars feel like less than you expected?")
ch("Angle 2: The psychology")
pr("""Angle two. The psychology. Because the strangest thing about one million dollars is how it feels when you
actually get there.""")
sc("""Many people expect reaching a million to feel like crossing a finish line. Fireworks. Relief. Instead, a lot
of people say it feels oddly normal. They check the number, smile, and go back to work the next day. Psychologists
call this hedonic adaptation. We get used to new situations quickly, good and bad. The thrill fades, and the new
level becomes the baseline.""",
   "Person looking at laptop calm", "IT FEELS NORMAL")
sc("""That's why the million should never be the goal on its own. If it's just a number, it disappoints. If it's
connected to something you want, like time with your kids, a business, or leaving a job you hate, then hitting it
means something. The number is just a vehicle. The destination is the life it buys.""",
   "Family walking on beach", "A VEHICLE, NOT A DESTINATION")
sc("""There's another trap called moving the goalposts. At five hundred thousand, people say they'll feel safe at a
million. At a million, they say two million. The Schwab survey we mentioned shows the same thing at the level of the
whole country. The definition of wealthy keeps rising. Without a clear personal number, enough never arrives.""",
   "Soccer goal on field", "MOVING THE GOALPOSTS")
sc("""The opposite also happens. Some people feel a million is so far away that they never start. It seems
impossible, so why bother? This is where the math is your friend. Nobody saves a million dollars. They save a few
hundred dollars, over and over, and let time do the heavy lifting. Break it down, and the mountain becomes a
staircase.""",
   "Staircase steps", "A MOUNTAIN OR A STAIRCASE")
sc("""And finally, there's fear of spending. People who spent decades saving often find it painful to withdraw, even
when they can clearly afford it. Research on retirees has found many spend less than they safely could. If that's
you someday, remember that the money was always meant to be used. Saved money that's never enjoyed is a kind of
failure too.""",
   "Elderly couple travel airport", "LET YOURSELF SPEND")
sc("""So the psychological lesson of a million dollars is simple. Define enough before you get there. Connect the
money to a purpose. And give yourself permission to enjoy it when the time comes. People who do those three things
tend to be much happier with their money, whatever the final number is.""",
   "Sunrise over mountains", "DEFINE ENOUGH")

# ---------------- Angle 3: playbook ----------------
short("Here's how to make one million dollars last for the rest of your life.")
ch("Angle 3: The playbook")
pr("""Angle three. The playbook. If you have a million dollars, or you're on your way, here's how to make it
actually work for you.""")
sc("""Step one. Know your number. Add up what you spend in a year, not what you think you spend, what you actually
spend. Look at a full year of bank and card statements. Multiply by twenty five for a traditional retirement, or by
about thirty if you want extra safety or plan to retire early. That's your target, and it might be more or less than
a million.""",
   "Spreadsheet on laptop", "STEP 1: KNOW YOUR NUMBER")
sc("""Step two. Keep it diversified and low cost. Many long term investors use broad index funds that hold
thousands of companies, plus some bonds as they get closer to needing the money. You don't need to pick winners. You
need to own the market cheaply and stay invested. Check your fees once a year.""",
   "New York Stock Exchange trading floor", "STEP 2: LOW COST, DIVERSIFIED")
sc("""Step three. Keep a cash buffer. Many retirees keep one to two years of spending in cash or very safe
investments. When markets fall, they spend from the buffer instead of selling investments at low prices. It's one of
the simplest ways to make the four percent rule safer.""",
   "Piggy bank coins", "STEP 3: A CASH BUFFER")
sc("""Step four. Be flexible. The people whose money lasts the longest usually spend a little less in bad years and a
little more in good years. Skipping one big trip during a downturn can make a real difference over thirty years.
Step five. Plan your taxes. Decide which accounts to draw from first. A tax professional can be worth the fee here,
especially in the first years.""",
   "Tax forms on desk", "STEPS 4 AND 5")
sc("""Step six. Protect it. Make sure you have the right insurance, a will, and beneficiaries named on every account.
Be extremely careful with anyone who promises guaranteed high returns. The Federal Reserve found that about one in five
adults experienced fraud or a scam in a single year. People with money are bigger targets, not smaller ones.""",
   "Lawyer office documents", "STEP 6: PROTECT IT")
sc("""And if you're still on your way to a million, the playbook is even simpler. Spend less than you earn. Invest
the difference automatically in low cost, diversified funds. Get every dollar of employer match. Avoid high interest
debt. And don't interrupt the process. That's genuinely most of it.""",
   "Graph trending upward", "THE ROAD TO A MILLION")

# ---------------- Questions ----------------
ch("Questions people ask")
pr("""Let me answer the questions people ask me most about a million dollars.""")
sc("""Question one. Is a million enough to retire? For many people, combined with Social Security and a paid off
home, yes. For people in very expensive cities, or retiring very young, maybe not. It comes back to your spending.
Question two. Should I pay off my house first? It's a personal choice. A paid off house lowers the income you need,
but it ties up money you can't easily spend.""",
   "House with for sale sign", "IS IT ENOUGH?")
sc("""Question three. What if I inherit a million? Slow down. Put it somewhere safe and boring, pay off high interest
debt, and talk to a fee only financial planner before doing anything big. Question four. Can I live off interest alone?
If safe bonds pay around four percent, one million earns around forty thousand a year, before taxes, without touching
the principal. But interest rates change, and inflation slowly eats away at a fixed income.""",
   "Bank building United States", "INHERITANCE AND INTEREST")
sc("""Question five. How long does it take to save a million? It depends almost entirely on how much you invest each
month. At a seven percent illustration, two thousand dollars a month gets there in about twenty years. One thousand
a month takes around twenty eight. Five hundred a month takes around thirty six. Start earlier, and time does more of the
work.""",
   "Calendar planning", "HOW LONG DOES IT TAKE?")
sc("""Question six. Does a million make you happy? Research on income and happiness, including well known work by
Daniel Kahneman and Angus Deaton, and later work by Matthew Killingsworth, suggests money is linked to well being,
especially in removing stress. But the biggest gains come from escaping money worries, not from luxury. A million
dollars can buy you calm. It can't buy you purpose. You have to bring that yourself.""",
   "Person relaxing on couch", "DOES IT MAKE YOU HAPPY?")
sc("""Question seven. Should I tell people I have a million? Many quiet millionaires don't. Not out of secrecy, but
because it changes how people treat you, and it makes you a target for sales pitches and scams. Share it with your
partner, your planner and the people who need to know for your estate. Beyond that, your net worth is your business.
Question eight. Is a million still worth chasing? Absolutely. Just know what you're chasing: not a rich lifestyle,
but a life where money stops making your decisions for you.""",
   "Person thinking by window", "KEEP IT QUIET?")

# ---------------- Recap ----------------
ch("Recap: 15 hard truths")
sc("""Let's recap the fifteen truths. One, inflation has cut the million in half since the nineties. Two, as an income
it's about forty thousand dollars a year. Three, a house alone would eat it. Four, location changes everything. Five,
taxes take a slice. Six, fees can eat a quarter of your income. Seven, health insurance is the hidden bill before
sixty five. Eight, Social Security helps a lot.""",
   "Notebook with financial notes", "TRUTHS 1 TO 8")
sc("""Nine, early retirement is much harder. Ten, investing makes it grow. Eleven, spending is the real dial. Twelve,
it buys choices. Thirteen, lifestyle can burn it fast. Fourteen, most millionaires look ordinary. And fifteen, a million
is more reachable than most people believe, with time and consistency.""",
   "Mountain climber reaching summit", "TRUTHS 9 TO 15")
sc("""And the three angles. The numbers say a million is comfortable, not rich, and your spending decides how far it
goes. The psychology says define enough before you get there. And the playbook says keep it simple, low cost,
diversified, protected, and flexible.""",
   "Map and compass", "NUMBERS, PSYCHOLOGY, PLAYBOOK")
sc("""And one last thought before you go. When people picture a million dollars, they picture a pile of cash, and
what they could buy with it. But the people who handle money best picture something else. They picture a machine,
quietly producing income month after month, year after year, so that their time belongs to them. A pile of cash
gets spent. A machine keeps working. Whether your million becomes a pile or a machine is the most important money
decision you'll ever make, and it's a decision you can start making today, long before you reach seven figures.""",
   "Factory machine gears", "A PILE OR A MACHINE?")

# ---------------- Close ----------------
ch("What to do next")
pr("""So here's your homework. Work out your own number: your yearly spending times twenty five. Then compare it with a
million. You might find your finish line is closer than you thought. Or you might find it's further away,
and that's useful too, because now you know exactly what you're aiming at. Either way, write the number down
somewhere you'll see it every month. If you want the full step by step plan, it's in my
playbook, link in the description. I'm Ryan Rover. See you in the next one.""")

save("video04", "What $1 Million Actually Buys You in 2027", [
    "Bureau of Labor Statistics, Consumer Price Index (prices roughly doubled since the mid-1990s)",
    "Bureau of Labor Statistics, Consumer Expenditure Survey 2023 (average household spending $77,280)",
    "National Association of Realtors, existing-home sales (2025 median price a little over $400,000)",
    "Social Security Administration, monthly statistical snapshot 2025 (average retired worker benefit about $2,000 a month)",
    "KFF, Employer Health Benefits Survey 2025 (average family premium close to $27,000)",
    "Charles Schwab, Modern Wealth Survey 2024 (about $2.5 million to be considered wealthy)",
    "UBS Global Wealth Report 2025 (more than 20 million U.S. millionaires)",
    "Carlson, Kim, Lusardi and Camerer, Bankruptcy Rates among NFL Players with Short-Lived Income Spikes, NBER (2015)",
    "Kahneman and Deaton, High income improves evaluation of life but not emotional well-being, PNAS (2010); Killingsworth, PNAS (2021)",
    "Thomas J. Stanley and William D. Danko, The Millionaire Next Door (1996)",
    "William P. Bengen, Determining Withdrawal Rates Using Historical Data, Journal of Financial Planning (1994)",
    "Federal Reserve, Economic Well-Being of U.S. Households in 2025 (about 1 in 5 experienced fraud or scams)",
    "FBI Internet Crime Complaint Center, annual Internet Crime Report (billions in reported losses; large losses among people over 60)",
    "Compound growth: stated illustrative math at 7% average yearly return, compounded monthly",
], "what $1 million buys in 2027")
