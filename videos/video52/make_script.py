import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Charlie Munger, Warren Buffett's longtime business partner, famously said the first one
hundred thousand dollars is the hardest. Almost everyone who has built wealth agrees. But almost nobody explains
exactly how to get there, step by step, from zero. So today, that's what we'll do. The full plan to your first one
hundred thousand dollars, in order.""")
short("The first $100,000 is the hardest. Here's the plan.")
card("""The first one hundred thousand dollars is the hardest, because at the start, almost all the progress has to come
from you. After it, your money starts helping.""",
     {"type": "stat", "label": "the first milestone", "big": "$100,000", "sub": "the hardest one, and the most important"})
sc("""If you watched my video on what changes when you hit one hundred thousand dollars of net worth, you know why this
milestone matters. Compounding becomes visible, your money starts out earning your savings in good years, and your
options multiply. This video is the other side. Not what happens when you get there, but exactly how to get there.""",
   "Mountain trail path", "HOW TO GET THERE")
sc("""We'll break the journey into six stages, from zero to one hundred thousand, and look at them from three angles.
First, the numbers: how long each stage takes at different savings levels. Second, the psychology: why this journey
feels so slow, and the mental traps at each stage. And third, the playbook: exactly what to do at each stage, in
order.""",
   "Six steps staircase", "SIX STAGES, THREE ANGLES")
pr("""Wherever you are right now, at zero, at ten thousand or at seventy, you'll find your next step in this video. Let's
start with the numbers.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Every number here is either from a named source or simple stated math. Timelines assume a seven percent average
yearly return compounded monthly, which is an illustration, not a promise. Real returns vary, and some years are
negative. Net worth data comes from the Federal Reserve's Survey of Consumer Finances. Retirement account rules come
from the IRS. This is education, not financial advice.""",
   "Federal Reserve building", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. How long does it really take, and where does the time go?""")
sc("""The answer depends mostly on one number: how much you invest each month. Let's look at a few realistic levels, all
at a seven percent average yearly return. At two hundred fifty dollars a month, reaching one hundred thousand takes
about seventeen years. At five hundred dollars a month, about eleven years.""",
   "Calendar on desk", "$250 VS $500 A MONTH")
sc("""At seven hundred fifty dollars a month, about eight years. At one thousand dollars a month, about six and a half
years. At fifteen hundred, under five years. And at two thousand dollars a month, a bit under four years. Every
increase in your monthly amount cuts years off the journey.""",
   "Calendar pages flipping", "$750 TO $2,000 A MONTH")
card("""How long it takes to reach one hundred thousand dollars, at a seven percent average yearly return, compounded
monthly.""",
     {"type": "compare", "left": {"label": "$500 a month", "big": "~11 years", "sub": "to $100,000"},
      "right": {"label": "$1,000 a month", "big": "~6.7 years", "sub": "to $100,000"},
      "note": "Illustration. Returns are not guaranteed."})
sc("""Now here's the important pattern. Look at the five hundred dollar path. Going from zero to fifty thousand takes about
six and a half years. Going from fifty thousand to one hundred thousand takes only about four and a half more. The
second half is faster than the first, because your money is now doing part of the work.""",
   "Running track second lap", "THE SECOND HALF IS FASTER")
sc("""That's exactly why Munger called the first one hundred thousand the hardest. At the start, almost all the progress is
your own contributions. Growth is tiny. In year one, at five hundred a month, growth might add only a couple of hundred
dollars. By year ten, growth in an average year can add several thousand dollars. Same habit. Very different
results.""",
   "Small plant vs big tree", "WHY THE START IS HARDEST")
card("""Five hundred dollars a month at seven percent for eleven years. You'd put in sixty six thousand dollars. Watch how
the growth line pulls away from the contributions near the end.""",
     {"type": "growth", "monthly": 500, "rate": 0.07, "years": 11})
sc("""Let's also put one hundred thousand dollars in context. According to the Federal Reserve's Survey of Consumer
Finances, the median net worth of families under thirty five was about thirty nine thousand dollars in twenty twenty
two. For families thirty five to forty four, it was about one hundred thirty five thousand. So reaching one hundred
thousand in your twenties or early thirties puts you well ahead of most people your age.""",
   "Young professionals city", "WHERE $100,000 PUTS YOU")
sc("""And remember that net worth counts everything: retirement accounts, savings, investments, and home equity, minus
debts. In this video, we'll focus mainly on invested money and savings, because that's the part that compounds. But
paying off debt also raises your net worth, dollar for dollar.""",
   "Balance sheet simple", "WHAT COUNTS")

sc("""Here's another way to see it. In year one of the five hundred dollar path, you contribute six thousand dollars, and
growth adds maybe two hundred. In year eleven, you still contribute six thousand, but growth in an average year can add
around six thousand more. Your effort stays the same. The result doubles. That's the shift every person on this
journey eventually feels.""",
   "Two bars comparison", "SAME EFFORT, DOUBLE RESULT")
sc("""And here's the honest reality check. Most people never get there, not because the math is hard, but because life keeps
interrupting. A car, a move, a wedding, a job change, a scary headline. The plan in this video is designed to survive those
interruptions. It doesn't require a perfect decade. It requires a decade where you mostly keep going.""",
   "Life events calendar busy", "A DECADE OF MOSTLY KEEPING GOING")
sc("""Think of the journey in seasons, not days. Some seasons you'll save a lot. Some seasons, like a new baby or a job loss,
you'll save very little, and that's okay. The people who make it aren't the ones with perfect seasons. They're the ones who
always come back to the plan when the season ends.""",
   "Four seasons tree", "SEASONS, NOT DAYS")

ch("The six stages")
pr("""Here are the six stages of the journey. Each one has a different job, and a different danger.""")
card("""Stage one, zero to one thousand. Stage two, one thousand to ten thousand. Stage three, ten to twenty five thousand.
Stage four, twenty five to fifty. Stage five, fifty to seventy five. And stage six, seventy five to one hundred
thousand.""",
     {"type": "stat", "label": "the journey", "big": "6 STAGES", "sub": "$0 → $1K → $10K → $25K → $50K → $75K → $100K"})
sc("""Stage one, zero to one thousand dollars, is about breaking the paycheck to paycheck loop. Stage two, one thousand to
ten thousand, is about clearing high interest debt and building a real emergency fund. Stage three, ten to twenty five
thousand, is where serious investing begins.""",
   "First steps path", "STAGES 1 TO 3")
sc("""Stage four, twenty five to fifty thousand, is the long, boring middle, where most people stall. Stage five, fifty to
seventy five thousand, is where compounding becomes noticeable. And stage six, seventy five to one hundred thousand, is
the final push, which usually goes faster than you expect.""",
   "Mountain switchback trail", "STAGES 4 TO 6")
pr("""Now, why does this journey feel so hard, even when you know the math? That's angle two.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
pr("""Angle two. The psychology. The mental trap at each stage, and how to get past it.""")
short("The stage where most people quit on the way to $100K")
sc("""Stage one trap: it feels pointless. One thousand dollars feels like nothing compared with the goal. People think,
what's the point of saving fifty dollars a week when I need one hundred thousand? But the first thousand isn't about
the amount. It's about proving to yourself that you can keep money. It's the most important thousand of the whole
journey.""",
   "Small savings jar coins", "STAGE 1: IT FEELS POINTLESS")
sc("""The fix: celebrate the first thousand like a real milestone, because it is. Many people never reach it. Researchers
have found that people are more motivated by goals that feel close and achievable. So don't stare at one hundred
thousand yet. Stare at one thousand.""",
   "Celebration small cake", "CELEBRATE THE FIRST $1,000")
sc("""Stage two trap: debt fatigue. Paying off credit cards and building an emergency fund is slow, and it doesn't feel
like getting richer. Your balance might be negative for a while. Many people give up here and go back to spending,
because the progress is invisible.""",
   "Credit card bills tired", "STAGE 2: DEBT FATIGUE")
sc("""The fix: track debt paid off as progress, not just savings. Make a simple chart and color in every five hundred
dollars of debt you clear. Seeing the chart fill up gives your brain the visible progress it craves. And remember,
every dollar of high interest debt you pay off is a guaranteed return.""",
   "Debt payoff chart colored", "COLOR THE CHART")
sc("""Stage three trap: fear of investing. You finally have money to invest, and suddenly it feels risky. What if the market
crashes right after I start? So people keep everything in cash for years, waiting for the right moment, while
inflation quietly eats it.""",
   "Nervous person laptop", "STAGE 3: FEAR OF INVESTING")
sc("""The fix: start with automatic monthly investing into diversified, low cost funds. Investing the same amount every
month means you never have to pick the perfect day. And if the market drops early, you're buying at lower prices,
which helps you over the long run.""",
   "Automatic investing app", "AUTOMATE THE START")
sc("""Stage four trap: the boring middle. From twenty five to fifty thousand, there are no exciting milestones. The
emergency fund is done, the debt is gone, and now it's just year after year of steady contributions. This is where
lifestyle creep, comparison and boredom pull the most people off the path.""",
   "Long flat road", "STAGE 4: THE BORING MIDDLE")
sc("""The fix: create mini milestones every five thousand dollars, and raise your contribution with every raise. Find one
friend or online community on the same path. And keep a simple yearly snapshot of your net worth, so you can see the
middle is moving, even when it doesn't feel like it.""",
   "Milestone markers road", "MINI MILESTONES")
sc("""Stage five trap: market drops feel bigger. At sixty thousand dollars invested, a twenty percent market drop is twelve
thousand dollars. That might be more than you saved all year. For the first time, a bad year can wipe out a year of
effort, at least on paper. This is when panic selling becomes tempting.""",
   "Stock market falling red", "STAGE 5: DROPS FEEL BIGGER")
sc("""The fix: write a note to your future self now, before the drop. When my portfolio falls twenty percent, I will keep
investing and I will not sell. And check your mix. If drops truly keep you up at night, a slightly more conservative
mix that you can stick with is better than an aggressive one you abandon.""",
   "Handwritten note pen", "A NOTE BEFORE THE DROP")
sc("""Stage six trap: the finish line feeling. You're close, and it's tempting to ease off, reward yourself, or start
spending ahead of reaching the goal. Or the opposite, taking bigger risks to get there faster. Both can delay you by
years.""",
   "Runner near finish line", "STAGE 6: THE FINISH LINE")
sc("""The fix: keep the exact same habits for the final stretch. Remember, at this stage your money is doing a big share of
the work. Don't change the system that got you here. And plan your celebration in advance, a modest one, so it doesn't
turn into a lifestyle reset.""",
   "Same routine calendar", "DON'T CHANGE THE SYSTEM")

# ---------------- Mid ----------------
ch("A quick favor")
pr("""Quick pause. If you're on this journey right now, subscribe to the channel. It's free, and I'll be here with you
for every stage. Now, the playbook. Exactly what to do at each stage.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
pr("""Angle three. The playbook. Six stages, with the exact moves for each.""")
short("Exactly what to do at every stage from $0 to $100K")

sc("""If you want the whole plan in one sentence, here it is. Build a small cushion, get the match, kill high interest debt,
build a real emergency fund, invest ten to fifteen percent automatically in low cost funds, grow your income, and don't
interrupt it. Everything else is detail. Now let's go stage by stage.""",
   "One sentence on paper", "THE ONE SENTENCE PLAN")

ch("Stage 1: $0 to $1,000")
sc("""Stage one, zero to one thousand dollars. The goal is a starter cushion that breaks the loop of every surprise
becoming debt. Open a separate high yield savings account, ideally at a different bank from your checking, so the
money isn't staring at you every day.""",
   "Opening savings account", "STAGE 1: THE CUSHION")
sc("""Set an automatic transfer on payday, even twenty five dollars. Cancel two subscriptions you don't use, and send that
money to savings. Sell a few things you don't need. And put any windfall, like a tax refund, straight in. Most people
can finish this stage in two to six months.""",
   "Selling items online", "STAGE 1: FAST WINS")

sc("""The common mistake in stage one is waiting for the perfect budget before starting. You don't need one. You need a
transfer. A real example: Kayla, twenty three, set up a twenty dollar weekly transfer and sold an old game console. She hit
one thousand dollars in about four months, and said it was the first time in her life she didn't panic when her car
needed new tires.""",
   "Young woman car tires shop", "STAGE 1 IN REAL LIFE")
ch("Stage 2: $1,000 to $10,000")
sc("""Stage two, one thousand to ten thousand. Two jobs here. First, make sure you're getting any employer retirement match,
because that's part of your pay. Contribute at least enough to get it, even while paying off debt.""",
   "Employer benefits form", "STAGE 2: GET THE MATCH")
sc("""Second, attack high interest debt. List every debt by interest rate, and pay extra on the highest rate first, while
making minimum payments on the rest. Once high interest debt is gone, build your emergency fund to three to six months
of essential expenses. This stage often takes one to three years, depending on your debt.""",
   "Debt list notebook", "STAGE 2: DEBT, THEN CUSHION")
sc("""A tip for this stage. When a debt is paid off, don't let that payment disappear into spending. Roll it into the next
debt, then into the emergency fund. You're already used to living without that money. Keep it working.""",
   "Rolling snowball", "ROLL THE PAYMENT")

sc("""The common mistake in stage two is skipping the match to pay off debt faster. That's usually a bad trade, because the
match is an instant return that debt payoff can't beat. Another mistake is closing every credit card the moment it's paid.
Sometimes keeping an old, no fee card open helps your credit history. Just don't use it to rebuild a balance.""",
   "Credit card in drawer", "STAGE 2 MISTAKES")
ch("Stage 3: $10,000 to $25,000")
sc("""Stage three, ten to twenty five thousand. Now investing begins in earnest. If you haven't already, open a retirement
account like an IRA, or raise your workplace plan contributions above the match. Choose simple, diversified, low cost
funds, like broad index funds or a target date fund.""",
   "Index fund selection", "STAGE 3: START INVESTING")
sc("""Aim for a savings rate of at least ten to fifteen percent of your gross income, including any employer match. If that
feels impossible, start where you can and add one percent every few months. Turn on automatic contribution increases if
your plan offers them.""",
   "Percentage increase arrow", "STAGE 3: 10 TO 15%")

sc("""The common mistake in stage three is overcomplicating it. People read about dozens of funds and strategies and end up
frozen. A single broad, low cost fund, or a target date fund, is a perfectly reasonable starting point. You can always
adjust later. Another mistake is checking the balance every day. Weekly is plenty. Monthly is better.""",
   "Simple investing app", "STAGE 3 MISTAKES")
ch("Stage 4: $25,000 to $50,000")
sc("""Stage four, twenty five to fifty thousand, the boring middle. Your main job is to protect the habit and grow your
income. Apply a raise rule: at least half of every raise goes to investing. Make one career move per year, a skill, a
certification, a negotiation, or a better role.""",
   "Professional career growth", "STAGE 4: GROW INCOME")
sc("""Also check your fees. Find the expense ratio of every fund you own. And avoid big new fixed costs, like a large car
payment or a much bigger apartment, that would force you to cut your savings rate. This stage is mostly about not
breaking what works.""",
   "Fee comparison laptop", "STAGE 4: PROTECT IT")

sc("""The common mistake in stage four is the big upgrade. A new car loan or a much bigger apartment that quietly cuts the
monthly investment in half. Another is jumping between strategies, selling one fund for another after reading a scary or
exciting headline. Every switch can mean taxes, fees and lost time. Boring consistency wins this stage.""",
   "New car dealership tempting", "STAGE 4 MISTAKES")
ch("Stage 5: $50,000 to $75,000")
sc("""Stage five, fifty to seventy five thousand. Compounding becomes noticeable. In a good year, your investments might
grow by several thousand dollars. This is the stage to get your financial paperwork in order. Check the beneficiaries
on every account. If people depend on your income, consider term life insurance. And make sure your emergency fund
has kept up with your expenses.""",
   "Signing beneficiary forms", "STAGE 5: PAPERWORK")
sc("""It's also a good time to think about taxes. Are you using tax advantaged accounts, like a 401k, an IRA, or a health
savings account if you're eligible, as much as makes sense? The rules and limits change, so check the IRS website for
current numbers each year.""",
   "Tax advantaged accounts", "STAGE 5: TAX ACCOUNTS")

sc("""The common mistake in stage five is panic during a market drop. Someone at sixty thousand watches it fall to fifty
thousand, sells, and waits for things to feel safe again. By the time it feels safe, prices have often recovered. Another
mistake is taking on too much risk because the balance feels big enough to gamble a part of it.""",
   "Panic selling screen", "STAGE 5 MISTAKES")
ch("Stage 6: $75,000 to $100,000")
sc("""Stage six, seventy five to one hundred thousand, the final push. Keep everything the same. Same automatic
contributions, same raise rule, same low cost funds. If you get a bonus, put a large share toward investing. And when you
cross one hundred thousand, celebrate modestly, then raise your automatic contribution by a little, instead of
lowering it.""",
   "Crossing finish line", "STAGE 6: THE FINAL PUSH")
sc("""Why raise it at the finish line? Because the next one hundred thousand comes faster than the first, and the habits you
keep now decide how fast. One hundred thousand isn't the end of the road. It's the point where the road starts going
downhill in your favor.""",
   "Road going downhill sunset", "THE ROAD TILTS YOUR WAY")
card("""The second one hundred thousand usually comes much faster than the first, because your money is now doing part of the
work. At five hundred dollars a month and seven percent, roughly eleven years for the first, and only about six more for the
second.""",
     {"type": "compare", "left": {"label": "First $100K", "big": "~11 years", "sub": "at $500 a month"},
      "right": {"label": "Second $100K", "big": "~6 years", "sub": "at $500 a month"},
      "note": "Illustration at 7% average yearly return."})

ch("Where to keep the money at each stage")
sc("""A quick guide to where money usually belongs at each stage. Your starter cushion and emergency fund belong in safe,
easy to reach places, like an FDIC insured high yield savings account. Not in stocks, because you might need it during a
market drop, exactly when stocks are down.""",
   "High yield savings app", "CUSHION: SAFE AND LIQUID")
sc("""Money for goals within a few years, like a down payment or a car, also usually belongs somewhere stable, like savings
accounts, certificates of deposit, or Treasury bills. Money for retirement and goals ten or more years away is where
diversified stock investments make the most sense, because there's time to recover from drops.""",
   "Treasury bills document", "GOALS: MATCH THE TIMELINE")
sc("""And the order of accounts many people follow is: employer plan up to the match, then an IRA, then more in the employer
plan, then a regular brokerage account. If you're eligible for a health savings account, it can be a powerful addition.
The right order depends on your situation, and limits change each year.""",
   "Retirement accounts order", "THE ACCOUNT ORDER")

sc("""The common mistake in stage six is changing the plan right before the finish. Some people move everything to cash to
protect the milestone, then miss the growth that would have carried them past it. Others get impatient and take a big risk
to get there faster. The milestone doesn't need protecting. The habit does.""",
   "Runner stumbling near finish", "STAGE 6 MISTAKES")

# ---------------- Accelerators ----------------
ch("Five ways to get there faster")
sc("""Want to speed it up? Here are five accelerators. Accelerator one. Raise your income early. A higher income in your
twenties or early thirties has the most years to compound. Accelerator two. Cut one big expense, like housing or a car,
instead of many small ones. One big win can free up hundreds of dollars a month.""",
   "Downsizing apartment", "ACCELERATORS 1 AND 2")
sc("""Accelerator three. Capture every dollar of employer match, and use tax advantaged accounts. Accelerator four. Live
on one income if you're a two income household, and invest most of the other, even for a few years. And accelerator
five. Send windfalls, like bonuses and refunds, mostly to investing.""",
   "Couple planning finances", "ACCELERATORS 3 TO 5")

ch("Finding $500 a month")
pr("""Five hundred dollars a month sounds like a lot to many people. So let's find it, on an ordinary budget.""")
sc("""Start with the big three: housing, transportation and food. Moving to a slightly cheaper apartment at renewal, or
getting a roommate for a while, might free two hundred dollars. Keeping your current car instead of upgrading, or
refinancing an expensive car loan, might free one hundred fifty.""",
   "Roommates apartment", "THE BIG THREE")
sc("""Then the smaller leaks. Cancel unused subscriptions, maybe forty dollars. Cook a few more dinners at home each week,
maybe eighty dollars. Shop your phone plan and insurance, maybe forty more. Add it up, and you're near five hundred, without
changing your life dramatically.""",
   "Home cooked dinner family", "THE SMALLER LEAKS")
sc("""And if the budget truly has no slack, the money has to come from income. A raise, a better paying job, overtime, or a
side income for a set period. Many people use a combination: cut two hundred, earn three hundred more. Five hundred dollars
a month isn't one big sacrifice. It's usually five or six small decisions.""",
   "Side job delivery", "OR EARN IT")

ch("The same plan at three incomes")
sc("""Let's see the plan at three incomes. At forty thousand dollars a year, investing two hundred fifty dollars a month is about
seven and a half percent of gross pay. Adding a three percent employer match helps. The journey might take fifteen years or
more, but income growth along the way usually shortens it.""",
   "Retail worker store", "AT $40,000")
sc("""At sixty thousand, five hundred a month is ten percent of gross pay. With a match, maybe thirteen percent. That's the
eleven year path, often shorter with raises. And at one hundred thousand, one thousand a month is twelve percent of gross
pay, about six and a half years. Higher incomes make it faster, but only if lifestyle doesn't rise to match.""",
   "Office professional laptop", "AT $60,000 AND $100,000")
sc("""Notice the percentages are similar. Around ten to fifteen percent. The plan scales with your income. What doesn't scale
is the habit. That has to be built at whatever income you have today.""",
   "Scales with income", "THE HABIT DOESN'T SCALE")

ch("Mistakes that cost years")
sc("""Before the stories, four mistakes that can add years to the journey. Mistake one. Cashing out a retirement account when
changing jobs. Taxes, possible penalties, and lost compounding can set you back years. Roll it over instead. Mistake two.
Taking a big loan for a depreciating asset, like an expensive car, in the middle of the journey.""",
   "Job change moving boxes", "MISTAKES 1 AND 2")
sc("""Mistake three. Chasing hot investments with a large share of your savings. One big loss can erase years of progress.
And mistake four. Stopping contributions for a long period during a downturn. Early dollars have the most time to grow, and
dollars invested during downturns often grow the most. If you need to, reduce contributions, but try not to stop.""",
   "Hot stock tip phone", "MISTAKES 3 AND 4")

ch("Your one page tracker")
pr("""Here's a simple tool that makes the whole journey easier. A one page tracker. You can do it in a notebook or a spreadsheet.""")
sc("""At the top, write your goal, one hundred thousand dollars, and the date you started. Below it, draw six boxes, one for
each stage. Each time you finish a stage, write the date in the box. It sounds almost childish. But seeing the boxes fill
up over the years is surprisingly motivating.""",
   "Notebook with boxes", "SIX BOXES")
sc("""Under the boxes, keep four numbers that you update once a month: your total invested, your emergency fund, your total
debt, and your savings rate. Once a year, add one more: your net worth. That's the whole tracker. Five minutes a month.""",
   "Spreadsheet simple", "FOUR NUMBERS A MONTH")
sc("""Why does this help? Because progress you can see keeps you going during the long middle. And because writing numbers down
regularly catches problems early, like a savings rate that slipped, or debt that crept back. What gets measured gets
managed, as the saying goes.""",
   "Pen writing numbers", "WHAT GETS MEASURED")

ch("Irregular income")
sc("""What if your income isn't steady? Freelancers, gig workers, people on commission and seasonal workers face a harder version
of this journey. The plan still works, with two changes. First, a bigger emergency fund, often six months or more, because
income can drop without warning.""",
   "Freelancer working cafe", "A BIGGER CUSHION")
sc("""Second, save a percentage, not a fixed amount. Every time money comes in, move a set share, say fifteen percent, to
savings and investing right away. In good months, you save more. In slow months, less. And set aside money for taxes if
they're not withheld. Many freelancers keep a separate account just for taxes.""",
   "Separate tax account", "SAVE A PERCENTAGE")
sc("""Some people with irregular income also pay themselves a steady salary from a holding account. All income goes into one
account, and a fixed amount moves to checking every two weeks. It turns a bumpy income into a smooth one, which makes every
other part of the plan easier.""",
   "Two bank accounts flow", "PAY YOURSELF A SALARY")

ch("Doing it as a couple")
sc("""If you're in a couple, the journey can go much faster, or much slower, depending on how you work together. Start with one
honest conversation about goals, debts and spending. Many couples avoid it for years, and lose time.""",
   "Couple talking kitchen", "ONE HONEST TALK")
sc("""Then decide on a system. Some couples combine everything. Some keep separate accounts and share a joint account for bills
and goals. Both can work. What matters is a shared target, shared automatic contributions, and a monthly fifteen minute check
in. Celebrate each stage together.""",
   "Couple high five", "A SHARED SYSTEM")
sc("""One more tip. If one partner earns more, contributions can be proportional to income, rather than equal. That keeps things
fair, and avoids resentment, which can derail a plan faster than any market crash.""",
   "Balanced scale", "PROPORTIONAL, NOT EQUAL")

ch("What about inflation?")
sc("""One more honest point. Because of inflation, one hundred thousand dollars ten years from now will buy less than it does
today. At three percent inflation, it would buy roughly what seventy four thousand buys now. So the milestone is a little
less impressive in real terms by the time you reach it.""",
   "Grocery prices rising", "INFLATION SHRINKS IT")
sc("""But that's another reason to invest rather than just save. Investments have historically grown faster than inflation over long
periods, while cash often hasn't. And it's a reason to raise your contributions over time, roughly in line with your income.
That keeps your plan growing in real terms, not just on paper.""",
   "Growing investment chart", "RAISE IT OVER TIME")

# ---------------- Stories ----------------
ch("Three paths to $100,000")
short("Three people, three paths to their first $100,000")
sc("""Let's look at three paths. Jordan, twenty six, a junior software tester. Starts at zero, invests four hundred dollars a
month, and raises it with every raise. After five years, he's investing twelve hundred a month. He reaches one hundred
thousand in about seven and a half years. His accelerator was income growth.""",
   "Young tech worker desk", "JORDAN: INCOME GROWTH")
sc("""Teresa, thirty three, a nurse with sixteen thousand dollars of credit card and car debt. She spends her first two and a
half years in stages one and two, clearing debt and building an emergency fund. Then she redirects those payments,
about one thousand dollars a month, into investing. She reaches one hundred thousand around nine and a half years after
starting. Her accelerator was the rolled debt payment.""",
   "Nurse hospital hallway", "TERESA: ROLLED PAYMENTS")
sc("""And Sam and Priya, a couple in their thirties, each earning about sixty thousand dollars. They decide to live on one
income for four years and invest most of the other. Investing about two thousand five hundred dollars a month, they reach one
hundred thousand in about three years, then relax their savings rate a little. Their accelerator was a high savings
rate for a short period.""",
   "Couple cooking at home", "SAM AND PRIYA: ONE INCOME")
sc("""Three very different paths. One focused on income, one on debt first, one on an intense savings rate. All three used
automation, avoided big new fixed costs, and kept investing through market drops. The details differ. The stages and the
habits are the same.""",
   "Three paths converge", "SAME STAGES, SAME HABITS")

ch("What it feels like to get there")
sc("""People who reach their first one hundred thousand often say the same thing. It didn't feel like a big moment. There was no
fireworks day. The balance just quietly crossed a line on a random Tuesday. What changed wasn't the day. It was everything
around it.""",
   "Ordinary Tuesday office", "A QUIET TUESDAY")
sc("""Money stopped feeling like an emergency. A surprise bill became a minor annoyance. Job decisions became choices instead of
necessities. And for many, the biggest change was internal. They had proof that they could set a long goal and reach it.
That proof makes every next goal easier.""",
   "Calm confident person", "PROOF YOU CAN DO IT")
sc("""And many say the same regret. I wish I'd started sooner, even with smaller amounts. If you're at the very beginning right now,
this is the part of the story you're in. It's the part everyone wishes they'd started earlier.""",
   "Sunrise new start", "START SOONER")

sc("""Notice also what none of them did. None of them found a secret investment. None of them timed the market. None of them
earned a huge salary at the start. They followed the stages in order, adjusted when life got in the way, and kept the
automatic transfers running. That's the whole secret, and it's available to almost anyone with a steady income and a little
patience.""",
   "Ordinary people walking city", "NO SECRET INVESTMENT")
sc("""And each of them says the same thing about the moment they crossed one hundred thousand. It wasn't the money that felt
best. It was knowing the hardest part was behind them.""",
   "Person looking at view", "THE HARDEST PART IS BEHIND")

# ---------------- FAQ ----------------
ch("Questions people ask")
pr("""Let me answer the questions people ask me most about the first one hundred thousand.""")
sc("""Question one. Does home equity count? For net worth, yes. But in this plan, I focus on invested money and savings,
because home equity doesn't compound the same way and can't easily be used. A paid down mortgage is valuable. It's just a
different kind of progress.""",
   "House with equity concept", "DOES HOME EQUITY COUNT?")
sc("""Question two. Should I pay off student loans first? It depends on the rate. High interest loans are often worth paying
down aggressively. Lower rate loans can usually be paid on schedule while you invest, especially to capture an employer
match. Check whether you qualify for any federal repayment programs first.""",
   "Student loan statement", "STUDENT LOANS FIRST?")
sc("""Question three. What if I'm forty and just starting? You can still get there. You'll need a higher monthly amount,
which is often possible because income tends to be higher in your forties. At one thousand dollars a month, it takes
roughly six and a half years at seven percent. And from age fifty, catch up contributions let you save more in
retirement accounts.""",
   "Middle aged man planning", "STARTING AT 40?")
sc("""Question four. Should I pick individual stocks to get there faster? It's tempting. But individual stocks add risk,
and most people who try to beat the market don't succeed over the long run. Many people keep the core of their money in
diversified funds, and if they want to pick stocks, use only a small slice they can afford to lose.""",
   "Stock picking screen", "PICK STOCKS?")
sc("""Question five. Should I use a robo advisor? Many robo advisors offer simple, diversified portfolios with automatic
rebalancing for a modest fee. They can be a good fit if you want things handled for you. Compare their total cost with a
target date fund, which can do something similar inside a single fund.""",
   "Robo advisor app", "ROBO ADVISOR?")
sc("""Question six. How often should I check my progress? Once a month for contributions, and once or twice a year for the
big picture. Checking daily tends to increase anxiety and the temptation to react to short term moves.""",
   "Monthly calendar check", "HOW OFTEN TO CHECK?")
sc("""Question seven. What about kids? Should I save for their college first? Generally, many planners suggest securing your
own retirement path first, at least the employer match, because kids can borrow for college but you can't borrow for
retirement. Once your plan is on track, a 529 college savings plan can be a good tool for education goals.""",
   "Family with kids planning", "WHAT ABOUT KIDS?")
sc("""And question eight. What if the market crashes right before I hit one hundred thousand? It might. Your balance could fall
back to eighty, or even seventy thousand for a while. That's normal and temporary in most historical cases, though not
guaranteed. Keep investing. Many people reach the milestone faster after a crash, because they bought cheap shares on
the way down.""",
   "Market recovery chart", "A CRASH NEAR THE GOAL?")

sc("""If you're starting from zero today, here's your homework for this week. Open a separate savings account. Set up an
automatic transfer for payday, any amount. And write the six stage boxes on a piece of paper. That's stage one, started.
The rest of the journey is just repeating that first week, with slightly bigger numbers, for a few years.""",
   "Notebook first page", "YOUR HOMEWORK THIS WEEK")

# ---------------- Recap ----------------
ch("Recap")
short("The 6 stages from $0 to $100,000")
sc("""Quick recap. The numbers: at five hundred dollars a month and seven percent, about eleven years. At one thousand, about
six and a half. The second half always goes faster than the first. The six stages: zero to one thousand, one to ten, ten to
twenty five, twenty five to fifty, fifty to seventy five, and seventy five to one hundred thousand.""",
   "Checklist clipboard", "THE NUMBERS AND STAGES")
sc("""The traps: it feels pointless, debt fatigue, fear of investing, the boring middle, bigger drops and the finish line
feeling. And the playbook: a starter cushion, the match and debt, start investing, grow income, paperwork and tax accounts,
and the final push. Keep the system running, and let the road tilt your way.""",
   "Road downhill", "THE TRAPS AND THE PLAYBOOK")

# ---------------- Close ----------------
ch("What to do next")
pr("""If you want this plan in more detail, with worksheets for every stage, it's in my playbook. The link is in the description.
And watch my video on what changes when you hit one hundred thousand dollars. It's the reward at the end of this road. I'm
Ryan Rover. See you in the next one.""")

save("video52", "The First $100K Is the Hardest: Here's the Plan", [
    "Charlie Munger: the first $100,000 is the hardest (widely quoted)",
    "Federal Reserve, Survey of Consumer Finances 2022 (median net worth under 35: $39,040; 35-44: $135,300)",
    "IRS, retirement plan, IRA and HSA rules and catch-up contributions (check current limits)",
    "Timeline and growth figures: stated illustrative math at a 7% average yearly return, compounded monthly",
], "the first $100k plan: numbers, psychology, playbook")
