import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short


EXTRA = {
1: ("""How do you know stage one is done? You've tracked a full month, every bill is on autopay for at least the minimum, and your total debt
went down instead of up. The most common mistake here is waiting for a perfect plan before starting. Start messy. Fix it as you go.""",
  "Checklist stage one done", "DONE WHEN: DEBT STOPS GROWING"),
2: ("""How do you know stage two is done? One thousand dollars sits in a separate account, and you've resisted using it for anything that isn't
a real emergency. The common mistake is keeping it in checking, where it slowly disappears. Separate it, name it, and protect it.""",
  "Separate savings account", "DONE WHEN: $1,000 SEPARATE"),
3: ("""How do you know stage three is done? No balances above about eight percent interest remain, and you're not adding new ones. The common
mistake is clearing the cards and then running them up again. Keep one card for small purchases you pay in full, and put the rest away.""",
  "Credit cards put away", "DONE WHEN: NO HIGH RATE DEBT"),
4: ("""How do you know stage four is done? Your essential expenses are covered for three to six months, and you have sinking funds for
predictable irregular costs. The common mistake is investing the emergency fund to earn more. Keep it safe. Its job is protection, not
growth.""",
  "Emergency fund safe", "DONE WHEN: 3 TO 6 MONTHS SAFE"),
5: ("""How do you know stage five is done? Ten thousand dollars invested, fifteen percent going in automatically, and low cost funds you
understand. The common mistake is constantly switching investments. Pick a simple, diversified mix and leave it alone.""",
  "Simple portfolio", "DONE WHEN: $10K AND 15%"),
6: ("""How do you know stage six is done? Your investments cross one hundred thousand dollars. Celebrate it. The common mistake here is lifestyle
creep, raising spending as income grows until the savings rate quietly falls. Watch your rate every year.""",
  "Celebration hundred thousand", "DONE WHEN: $100K"),
7: ("""How do you know stage seven is done? Five hundred thousand dollars invested. The common mistake in this stage is a big lifestyle decision
that permanently raises fixed costs, like an oversized house or two expensive car payments. One decision like that can add a decade to your
journey.""",
  "Oversized house warning", "DONE WHEN: $500K"),
8: ("""How do you know stage eight is done? You cross one million. The common mistakes here are taking big risks to get there faster, or panicking
in a downturn and selling near the bottom. At this stage, protecting what you've built matters as much as growing it.""",
  "Steady hands portfolio", "DONE WHEN: $1 MILLION"),
9: ("""And what's the common mistake after a million? Stopping all planning. A million dollars without a withdrawal plan, tax strategy and
healthcare plan can disappear faster than people expect. The playbook doesn't end. It changes from building to preserving and enjoying.""",
  "Planning documents retirement", "KEEP PLANNING"),
}

def stage(n, title, sub, paras):
    ch(f"Stage {n}. {title}")
    card(f"Stage {n}. {title}.", {"type": "list", "n": n, "title": title, "sub": sub}, f"STAGE {n}")
    for t, q, c in paras:
        sc(t, q, c)
    sc(*EXTRA[n])

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. This is the video I've been building toward. Everything this channel teaches, in one place. The complete playbook
from broke to one million dollars. Not through luck, not through a hot stock, and not through a six figure salary. Through nine stages that
ordinary people can follow, one step at a time.""")
short("The complete playbook from broke to $1 million")
sc("""Let's be clear about what broke means. Maybe you have zero in savings. Maybe you have credit card debt and a car loan. Maybe your net
worth is negative. That's where many people start. In fact, according to the Federal Reserve's Survey of Consumer Finances, a meaningful
share of American families have negative net worth, meaning they owe more than they own.""",
   "Empty wallet and bills", "WHAT BROKE MEANS")
sc("""And one million dollars? It's not a magic number. But it's a powerful milestone. Invested and withdrawn carefully, using the four percent
guideline, a million dollars could support around forty thousand dollars a year of spending, before Social Security. For many people, that's
financial freedom.""",
   "One million dollars milestone", "WHY $1 MILLION")
sc("""We'll look at the whole journey from three angles. First, the numbers: how long it really takes, and why it speeds up. Second, the
psychology: the mental challenges at each stage, and what keeps people going. And third, the playbook: nine stages, from broke to a million,
with the exact moves for each.""",
   "Three paths mountain", "THREE ANGLES")
pr("""Stay for the stage I call the long middle. It's where most people quit, and it's exactly where the magic starts. Let's start with the
numbers.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Household data comes from the Federal Reserve's Survey of Consumer Finances and Survey of Household Economics and Decisionmaking.
Retirement plan data comes from Fidelity and Vanguard reports. The four percent guideline comes from William Bengen's 1994 research. Growth
examples use stated math at a seven percent average yearly return, an illustration, not a promise. This is education, not financial
advice.""",
   "Research documents desk", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. How long does it take to go from zero to a million?""")
sc("""Let's assume you've already cleared high interest debt and built your emergency fund, and now you're investing from zero. At a seven
percent average yearly return, investing five hundred dollars a month, you could reach one million dollars in about thirty six years. At one
thousand dollars a month, about twenty eight years.""",
   "Long road timeline", "$1,000 A MONTH = ~28 YEARS")
sc("""At fifteen hundred dollars a month, about twenty three years. And at two thousand dollars a month, about twenty years. Double your
monthly investment, and you cut the timeline by roughly eight years. That's why growing your income and savings rate matters so much.""",
   "Shorter road timeline", "$2,000 A MONTH = ~20 YEARS")
card("""Years to reach one million dollars from zero, at a seven percent average yearly return.""",
     {"type": "compare", "left": {"label": "$1,000 a month", "big": "~28 years", "sub": "$330K contributed"},
      "right": {"label": "$2,000 a month", "big": "~20 years", "sub": "$470K contributed"},
      "note": "Illustration at 7% a year. Returns are not guaranteed."})
sc("""Now here's the most important chart in this video. Investing one thousand dollars a month at seven percent, the first one hundred
thousand dollars takes about six point seven years. The second hundred thousand takes about four and a half years. The third, about three
and a half.""",
   "Bar chart shrinking", "EACH $100K COMES FASTER")
sc("""And the tenth hundred thousand, the one that takes you from nine hundred thousand to a million, takes only about sixteen months. Same
contribution every month. The difference is that your money is now doing most of the work. That's compounding.""",
   "Snowball growing huge", "THE LAST $100K: ~16 MONTHS")
card("""Investing one thousand dollars a month at seven percent a year for thirty years.""",
     {"type": "growth", "monthly": 1000, "rate": 0.07, "years": 30})
sc("""After thirty years at one thousand dollars a month, you could have about one point two two million dollars. You'd have contributed three
hundred sixty thousand. The other roughly eight hundred sixty thousand is growth. In the later years, your portfolio can grow by more in a
good year than you contribute in an entire decade.""",
   "Portfolio growth more than contributions", "~$860K OF GROWTH")
sc("""This is why Charlie Munger, Warren Buffett's longtime business partner, reportedly said the first hundred thousand is the hardest. At the
start, it's all you. By the end, it's mostly your money. The hardest part of becoming a millionaire is the beginning.""",
   "Charlie Munger portrait", "THE FIRST $100K IS THE HARDEST")
sc("""How common is it? Fidelity has reported hundreds of thousands of 401k accounts with balances of one million dollars or more in recent
years, and many of those savers had ordinary incomes and simply contributed for decades. Becoming a millionaire through steady investing is
far more common than most people think.""",
   "Fidelity report chart", "401K MILLIONAIRES")
sc("""One more number to keep in mind: inflation. A million dollars in thirty years won't buy what a million buys today. At three percent
inflation, it might buy what about four hundred thousand buys now. That's not a reason to give up. It's a reason to start sooner and keep
increasing your contributions over time.""",
   "Inflation shrinking dollar", "INFLATION MATTERS")
sc("""Let's put the milestones on a timeline. Investing one thousand dollars a month at seven percent, starting from zero: one hundred thousand
dollars after about six point seven years. Two hundred fifty thousand after about thirteen years. Five hundred thousand after about twenty
years. And one million after about twenty eight years.""",
   "Milestone timeline", "$100K, $250K, $500K, $1M")
sc("""Look at the gaps. It takes about thirteen years to reach the first quarter million. Then about seven years to double it to half a million.
Then about eight years to double it again to a million, while you're contributing the same amount every month. Each doubling takes less of
your own effort, because growth is carrying more of the load.""",
   "Doubling chart", "EACH DOUBLING TAKES LESS EFFORT")
sc("""And the stages before investing matter too. Clearing debt and building an emergency fund might take one to four years. Those years don't
show up on the million dollar chart, but they're what make the chart possible. Without them, one emergency or one high interest balance can
undo years of investing.""",
   "Foundation under building", "THE YEARS BEFORE THE CHART")
pr("""So the math works, and it accelerates. The hard part is staying in the game long enough. That's angle two.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
pr("""Angle two. The psychology. What it feels like at each part of the journey, and how to keep going.""")
short("Why the journey to $1 million feels slow, then sudden")
sc("""At the beginning, the journey feels hopeless. You're paying off debt and saving small amounts. Your net worth might be negative. It's
easy to think, this will never work for someone like me. The key here is quick wins: a first five hundred dollars, a first card paid off.
Small wins prove the system works.""",
   "Person at bottom of mountain", "THE BEGINNING: HOPELESS")
sc("""In the early building years, the problem is boredom. You're investing every month, but the balance barely moves. A market drop can wipe
out a year of contributions. This is where the urge to do something exciting, like chasing a hot stock or crypto, is strongest. Resist it.""",
   "Bored person watching chart", "EARLY YEARS: BORING")
sc("""Then comes the long middle, roughly from one hundred thousand to five hundred thousand. Progress is real but slow. Life gets expensive:
kids, homes, career changes. Lifestyle creep pulls hard. This is where most people stall. Not because they fail, but because they slowly
stop increasing their savings.""",
   "Long flat road", "THE LONG MIDDLE")
sc("""And finally, the acceleration. After five hundred thousand, your money starts to grow faster than you can save. Good years can add more
than your annual contributions. The challenge here is different: fear of losing what you've built, and the temptation to take big risks or
stop too early.""",
   "Rocket accelerating", "THE ACCELERATION")

sc("""Notice that the hardest feelings come at the wrong times. Hopelessness hits when you've barely started, and that's when the system needs
patience. Boredom hits when compounding is still small, and that's when it needs consistency. Fear hits when you have the most to lose, and
that's when it needs calm. Knowing these feelings are coming makes them much easier to handle.""",
   "Emotional journey map", "THE FEELINGS ARE PREDICTABLE")
sc("""Research in behavioral finance, including work by Daniel Kahneman and Amos Tversky on loss aversion, suggests that losses can feel roughly
twice as painful as equal gains feel good. That's why market drops feel so much bigger than market rises. It's normal. The trick is not to
let that feeling make your decisions.""",
   "Loss aversion scale", "LOSSES FEEL TWICE AS BIG")
sc("""So build rules for yourself in advance. When the market drops, I keep investing. When I get a raise, half goes to my future. When I feel
like quitting, I read my why. Rules made in calm moments protect you in emotional ones.""",
   "Written rules card", "RULES MADE IN CALM MOMENTS")

ch("Five mindset rules for the journey")
sc("""Mindset one. Focus on the system, not the number. You can't control the market. You can control your savings rate, your fees, your
behavior and your income growth. Put your energy there.""",
   "Control dashboard", "MINDSET 1: THE SYSTEM")
sc("""Mindset two. Measure yearly, not daily. Checking your balance every day makes market noise feel like a crisis. Check once a quarter.
Measure progress once a year.""",
   "Yearly calendar", "MINDSET 2: YEARLY")
sc("""Mindset three. Celebrate milestones. Your first ten thousand. Your first hundred thousand. The year your portfolio grew more than you
contributed. Celebrating keeps the journey meaningful.""",
   "Celebration milestone", "MINDSET 3: CELEBRATE")
sc("""Mindset four. Never interrupt compounding unnecessarily. Cashing out a retirement account when changing jobs, or selling everything in a
crash, can set you back years. Protect the snowball.""",
   "Snowball rolling", "MINDSET 4: PROTECT THE SNOWBALL")
sc("""And mindset five. Remember why. A million dollars isn't the goal. Freedom is. Security for your family. Time for what matters. Write down
your why and read it when the journey feels long.""",
   "Handwritten why note", "MINDSET 5: REMEMBER WHY")

ch("Where the millionaire next door came from")
sc("""In 1996, researchers Thomas Stanley and William Danko published The Millionaire Next Door. After surveying wealthy Americans, they found
something surprising. Many millionaires didn't look rich. They lived in ordinary neighborhoods, drove ordinary cars, and had built their
wealth slowly by spending less than they earned and investing the difference.""",
   "Ordinary suburban house", "THE MILLIONAIRE NEXT DOOR")
sc("""Since then, the tools for ordinary people have improved enormously. The 401k became widespread in the 1980s. Low cost index funds became
easy to buy. Automatic enrollment became more common after the Pension Protection Act of 2006. Today, a regular worker can build a
diversified portfolio for a tiny fraction of a percent in yearly fees.""",
   "Timeline of investing tools", "BETTER TOOLS THAN EVER")
sc("""That's why this playbook works. It's not a secret. It's the same pattern Stanley and Danko found decades ago, made easier by modern tools.
Spend less than you earn. Avoid expensive debt. Invest steadily in low cost funds. And give it time.""",
   "Simple pattern diagram", "THE SAME PATTERN")

# ---------------- Mid ----------------
ch("A quick favor")
pr("""Quick pause. If you're on this journey, or ready to start, subscribe to the channel. It's free, and it's the best way to follow the
whole playbook with me. Now, the nine stages.""")

ch("Which stage are you in?")
pr("""Before the stages, here's a quick way to find where you are. Answer these questions in order. The first no is your stage.""")
sc("""Question one. In the last month, did your total debt go down rather than up, and are all your bills on autopay? If no, you're in stage
one. Question two. Do you have at least one thousand dollars in a separate savings account? If no, you're in stage two.""",
   "Quiz checklist", "QUESTIONS 1 AND 2")
sc("""Question three. Are you free of debt above about eight percent interest? If no, stage three. Question four. Do you have three to six months
of essential expenses saved? If no, stage four. Question five. Are you investing at least fifteen percent, with at least ten thousand dollars
invested? If no, stage five.""",
   "Quiz checklist continued", "QUESTIONS 3 TO 5")
sc("""After that, your stage is simply your invested balance. Under one hundred thousand, stage six. One hundred to five hundred thousand, stage
seven. Five hundred thousand to one million, stage eight. Over a million, stage nine. Pause the video and find yours.""",
   "Balance ranges chart", "THEN IT'S YOUR BALANCE")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
pr("""Angle three. The playbook. Nine stages from broke to one million dollars. Each stage has one main goal.""")
short("The 9 stages from broke to $1 million")

stage(1, "Stop the bleeding", "from negative to stable", [
("""Stage one. Stop the bleeding. The goal is to stop going further behind. Track your spending for one month. Find the leaks: overdraft
fees, unused subscriptions, late payments, high interest borrowing. Set up autopay for minimum payments so you never miss one.""",
 "Plugging a leak", "STOP GOING BACKWARD"),
("""If you're using payday loans or carrying overdrafts, getting out of those comes first. The Consumer Financial Protection Bureau has
reported that typical payday loans can carry annual percentage rates of almost four hundred percent. Escaping that cycle is the first big
win.""",
 "Payday loan sign", "ESCAPE THE WORST DEBT"),
("""You don't need perfection at this stage. You need a month where you don't add new debt. That's the turning point.""",
 "Calendar turning point", "ONE MONTH WITH NO NEW DEBT"),
])

stage(2, "Build a $1,000 starter fund", "the first shield", [
("""Stage two. Build a starter emergency fund of one thousand dollars in a separate high yield savings account. Sell things you don't use,
pick up an extra shift, or use a tax refund. Automate a transfer every payday.""",
 "Emergency fund jar", "$1,000 SHIELD"),
("""This small cushion means the next car repair or medical bill doesn't go on a credit card. It breaks the cycle of every surprise becoming
new debt.""",
 "Car repair paid cash", "BREAK THE CYCLE"),
("""At the same time, if your employer offers a retirement match, contribute enough to get it, even now. The match is too valuable to skip.""",
 "401k match form", "AND GET THE MATCH"),
])

stage(3, "Kill high interest debt", "free your income", [
("""Stage three. Pay off all high interest debt, usually anything above about eight percent. Credit cards, personal loans, store cards. List them
by interest rate and attack the highest first, or by balance if you need quick wins.""",
 "Debt list ranked", "HIGHEST RATE FIRST"),
("""Every debt you pay off frees up its payment. Roll that payment into the next debt. By the end, you might be sending several hundred dollars
a month at the last one.""",
 "Snowball rolling payments", "ROLL THE PAYMENTS"),
("""When this stage ends, something powerful happens. All those payments become money you can save and invest. Your income finally works for
you.""",
 "Money freed up", "YOUR INCOME IS FREE"),
])

stage(4, "Build the full emergency fund", "three to six months", [
("""Stage four. Grow your emergency fund to three to six months of essential expenses. Send your old debt payments here first. This fund protects
everything you'll build next.""",
 "Full emergency fund", "3 TO 6 MONTHS"),
("""With this in place, a job loss or a big repair won't force you to sell investments at a bad time or borrow again. It's your foundation.""",
 "Strong foundation", "THE FOUNDATION"),
("""At the end of stage four, your net worth may still be small. But your financial life is stable. That's a huge achievement that many people
never reach.""",
 "Stable calm person", "STABILITY"),
])

stage(5, "Invest 15% and reach $10,000", "the engine starts", [
("""Stage five. Raise your retirement investing to at least fifteen percent of your income, including the match. Use low cost index funds or a
target date fund. Open a Roth IRA if you qualify.""",
 "Index funds screen", "15% INVESTED"),
("""Your first goal is ten thousand dollars invested. It might take a year or two. It will feel slow. But this is where the engine starts.""",
 "Ten thousand milestone", "FIRST $10,000"),
("""Turn on automatic contribution increases if your plan offers them, so your rate rises by one percent each year without any effort.""",
 "Automatic increase setting", "AUTO INCREASES"),
])

stage(6, "Reach $100,000", "the hardest milestone", [
("""Stage six. Reach one hundred thousand dollars invested. At one thousand dollars a month, it takes about six to seven years from zero. This
is the hardest milestone, because most of it comes from your own contributions.""",
 "Hundred thousand milestone", "$100,000"),
("""Speed it up with income growth. Ask for raises, build skills, change jobs when it makes sense. Use the raise rule: half of every raise goes to
investing.""",
 "Career growth", "GROW YOUR INCOME"),
("""Avoid the big mistakes that reset progress: cashing out old 401k accounts, buying a car you can't afford, or panic selling in a downturn.""",
 "Warning signs", "AVOID THE RESETS"),
])

stage(7, "The long middle: $100K to $500K", "where most people stall", [
("""Stage seven. The long middle. From one hundred thousand to five hundred thousand. At one thousand a month, it takes roughly thirteen more
years. Life gets busy and expensive. This is where discipline matters most.""",
 "Long road middle", "THE LONG MIDDLE"),
("""Keep fixed costs under control as income rises. Buy a home you can comfortably afford, not the maximum the bank offers. Keep cars longer.
Protect your savings rate from lifestyle creep.""",
 "Modest home", "PROTECT YOUR SAVINGS RATE"),
("""And protect your family: term life insurance if people depend on you, disability insurance, a will, and updated beneficiaries. You now have
something worth protecting.""",
 "Family insurance", "PROTECT WHAT YOU'VE BUILT"),
])

stage(8, "The acceleration: $500K to $1M", "your money does the work", [
("""Stage eight. The acceleration. From five hundred thousand to a million. At one thousand a month and seven percent, this stage might take
about eight years, less time than the long middle, even though the dollar gap is bigger.""",
 "Rocket rising", "THE ACCELERATION"),
("""Now, investment growth can exceed your contributions. A seven percent year on six hundred thousand dollars is forty two thousand dollars of
growth. Keep contributing, but let the money do the heavy lifting.""",
 "Growth exceeds contributions", "GROWTH > CONTRIBUTIONS"),
("""As you get closer, review your investment mix. Many people gradually add more stable assets, like bonds, as they approach the point where
they'll need the money. A good plan reduces the risk of a big drop right before your goal.""",
 "Balanced portfolio", "REVIEW YOUR MIX"),
])

stage(9, "Reach $1 million and protect it", "freedom", [
("""Stage nine. One million dollars. Using the four percent guideline, it could support around forty thousand dollars a year of spending, more
with Social Security. You may be able to work by choice, cut back, or retire.""",
 "One million celebration", "$1,000,000"),
("""Now the focus shifts to protection and planning. A sustainable withdrawal strategy, tax planning, healthcare, and estate planning. Many people
benefit from a fee only fiduciary advisor at this stage.""",
 "Advisor meeting", "PROTECT AND PLAN"),
("""And think about what the money is for. Freedom, family, giving, experiences. Reaching a million isn't the end of the journey. It's the
beginning of a life with more choices.""",
 "Family generations", "WHAT IT'S FOR"),
])

# ---------------- Stories ----------------
ch("Three paths to a million")
short("Three ordinary people, three paths to $1 million")
sc("""Let's look at three paths. First, the early starter. Mia starts at twenty three with debt from college. She clears it by twenty six,
builds her emergency fund, and invests fifteen percent of a modest salary, increasing it with each raise. By her late fifties, she could reach
a million dollars on an ordinary career.""",
   "Young woman graduate", "MIA: THE EARLY STARTER")
sc("""Second, the late starter. Andre is broke at thirty eight after a divorce. He rebuilds stage by stage, and by forty two he's investing
two thousand dollars a month, about twenty five percent of his income. If he keeps it up, he could reach a million around sixty two, with his
highest earning years doing the heavy lifting.""",
   "Man in his forties rebuilding", "ANDRE: THE LATE STARTER")
sc("""Third, the high saver. Grace and Luis, both thirty, share one paid off car, rent modestly, and invest forty percent of their combined
income, about two thousand five hundred a month. At that pace, they could reach a million in under twenty years, by around fifty.""",
   "Young couple modest apartment", "GRACE AND LUIS: HIGH SAVERS")
sc("""Mia's biggest advantage was time. Starting in her twenties, even modest contributions had decades to compound. Her biggest challenge was
patience. In her thirties, her balance felt small compared to friends' lifestyles. But by her late forties, her investments were growing by more
each year than she contributed.""",
   "Woman reviewing growing balance", "MIA: TIME AND PATIENCE")
sc("""Andre's biggest advantage was income. Starting later, he used his peak earning years and catch up contributions after fifty to save
aggressively. His biggest challenge was avoiding the urge to catch up with risky bets. He stuck to the plan, and the plan worked.""",
   "Man calm investing", "ANDRE: INCOME AND DISCIPLINE")
sc("""Grace and Luis's biggest advantage was their savings rate. Their biggest challenge was social pressure from friends who didn't understand
why they lived modestly. Their answer was simple: we're buying our freedom early. By fifty, they may be able to work only on what they love.""",
   "Couple confident", "GRACE AND LUIS: FREEDOM EARLY")
sc("""Different starting points. Different timelines. The same playbook. These are illustrations, not promises, and real returns will vary. But
they show that a million dollars is reachable from very different lives.""",
   "Three paths converge", "THE SAME PLAYBOOK")

# ---------------- Accelerators ----------------
ch("The four accelerators")
pr("""There are four things that can speed up the journey at every stage. Let's go through them.""")
sc("""Accelerator one: income growth. Every raise, promotion or job change that increases your pay, combined with the raise rule, adds fuel.
Going from one thousand to two thousand dollars a month invested cuts the journey to a million from about twenty eight years to about
twenty.""",
   "Career promotion", "1: INCOME GROWTH")
sc("""Accelerator two: the big three. Housing, transportation and food make up most of a typical budget. A cheaper home, longer lasting cars and
more home cooking can free up hundreds of dollars a month, every month, for decades.""",
   "House car groceries", "2: THE BIG THREE")
sc("""Accelerator three: tax advantages. Using 401k plans, IRAs and health savings accounts lets more of your money compound. Over thirty years,
the difference between taxed and tax advantaged growth can be very large.""",
   "Tax advantaged accounts", "3: TAX ADVANTAGES")
sc("""And accelerator four: low fees. A one percent difference in yearly fees can cost tens of thousands of dollars, sometimes more than a
hundred thousand, over a long investing life. Low cost index funds keep more of the growth in your pocket.""",
   "Low fee fund", "4: LOW FEES")

sc("""Put all four accelerators together, and the effect is dramatic. A household that raises its income over time, keeps the big three
modest, uses every tax advantaged account available, and pays low fees can often reach a million years earlier than one doing only one of
those things. You don't need all four at once. Add one at a time, and let them stack.""",
   "Four arrows stacking", "LET THEM STACK")

ch("Surviving the long middle")
sc("""Let's spend a moment on the long middle, because it's where the journey is won or lost. Between one hundred and five hundred thousand
dollars, the progress is real, but it rarely feels exciting. Life is busy. The finish line is far away. And it's tempting to coast.""",
   "Long road fatigue", "WHERE IT'S WON OR LOST")
sc("""Three habits help. First, raise your contribution every year, even by one percent. Second, track your net worth once a year and write it
down, so you can see the progress you'd otherwise miss. Third, find people on the same path, a friend, a partner, or an online community, to
keep you motivated.""",
   "Friends talking money", "THREE HABITS")
sc("""And give yourself rewards along the way. A trip when you hit two hundred fifty thousand. A nice dinner at three hundred thousand. The
journey should include joy. That's what makes it sustainable.""",
   "Couple on trip", "REWARDS ALONG THE WAY")

ch("Taxes and the road to a million")
sc("""Where you hold your investments matters as you approach a million. Traditional 401k and IRA withdrawals are generally taxed as income.
Roth withdrawals can be tax free if the rules are met. Taxable brokerage accounts are taxed on dividends and gains, often at lower long term
rates.""",
   "Tax buckets", "THREE TAX BUCKETS")
sc("""Many people build a mix of all three, which gives flexibility later. In low income years, like early retirement or a career break, some
people convert traditional money to Roth at a lower tax rate. A tax professional can help you plan this, especially in stages eight and
nine.""",
   "Tax professional", "BUILD A MIX")

ch("Couples and families on the journey")
sc("""For couples, the journey works best as a team. Share the goal, agree on the savings rate, and hold a short monthly money meeting. When
both people understand the plan, it's much easier to stay on track during expensive years.""",
   "Couple planning together", "A TEAM GOAL")
sc("""For families with kids, the timeline often stretches during the childcare years. That's normal. Keep at least the match going, protect the
emergency fund, and raise contributions again when childcare costs fall. And put retirement before college savings, since kids can borrow
for school and you can't borrow for retirement.""",
   "Family with kids", "FAMILIES")
sc("""And involve your kids in age appropriate ways. Show them the plan. Let them see you save and invest. Teaching them the playbook early may
be the greatest financial gift you can give.""",
   "Parent teaching child", "TEACH THE NEXT GENERATION")

ch("The biggest mistakes on the road to a million")
sc("""Mistake one: cashing out retirement accounts when changing jobs. Taxes, penalties and lost compounding can cost far more than the check
you receive. Roll it over instead.""",
   "Rollover form", "MISTAKE 1: CASHING OUT")
sc("""Mistake two: panic selling in a crash. Selling after a big drop locks in losses and often means missing the recovery.""",
   "Panic selling", "MISTAKE 2: PANIC SELLING")
sc("""Mistake three: chasing get rich quick schemes. Hot tips, leveraged bets and too good to be true promises have derailed more journeys than
bad markets.""",
   "Get rich quick ad", "MISTAKE 3: GET RICH QUICK")
sc("""Mistake four: lifestyle creep. Letting spending rise as fast as income keeps the savings rate flat and the finish line far away.""",
   "Spending creeping", "MISTAKE 4: LIFESTYLE CREEP")
sc("""And mistake five: never starting. Waiting for the perfect time, the perfect income or the perfect knowledge. The best time to start was
years ago. The second best time is this week.""",
   "Calendar today", "MISTAKE 5: NEVER STARTING")

ch("Your first week on the playbook")
sc("""Here's your first week. Day one: calculate your net worth and find your stage. Day two: set up autopay for every minimum payment. Day
three: open a separate high yield savings account and automate a transfer.""",
   "Checklist first days", "DAYS 1 TO 3")
sc("""Day four: check that you're getting your full employer match. Day five: list your debts by interest rate. Day six: cancel one subscription
and redirect the money. Day seven: write your why on a card and put it somewhere you'll see it every day.""",
   "Card with written why", "DAYS 4 TO 7")

ch("What a million dollars actually buys")
sc("""So what does a million dollars actually look like in retirement? Using the four percent guideline, it could support about forty thousand
dollars a year of withdrawals, adjusted for inflation. Add Social Security, which for many retirees provides a significant share of income, and
the total could support a comfortable middle class retirement in many parts of the country.""",
   "Retired couple at home", "~$40,000 A YEAR + SOCIAL SECURITY")
sc("""For someone who retires early, a million might support a leaner lifestyle, or a combination of withdrawals and part time work. For someone
in a high cost city, it might be a milestone on the way to a larger number. That's why your own number, twenty five times your spending,
matters more than the round million.""",
   "City versus small town", "YOUR NUMBER MATTERS MORE")
sc("""And there's something money can't fully measure. People who reach financial independence often describe the biggest change as freedom
from worry. The freedom to say no, to help family, to give, and to spend time on what matters. That's the real return on the playbook.""",
   "Grandparents with grandchildren", "FREEDOM FROM WORRY")

ch("But Ryan, what about...")
sc("""Objection one. A million dollars is impossible for someone like me. It might take longer than you'd like. But the math shows that steady
investing on an ordinary income can get there over a career. And even if you reach half a million instead, you'll be far more secure than if
you never started.""",
   "Determined ordinary worker", "IMPOSSIBLE FOR ME")
sc("""Objection two. The economy is different now. Housing and education are more expensive than they were for earlier generations. That's true.
But investing is cheaper and easier than ever, with low cost funds and automatic contributions. Focus on what you control.""",
   "Modern economy chart", "THE ECONOMY IS DIFFERENT")
sc("""And objection three. I'd rather enjoy my money now. You can do both. The playbook includes fun money at every stage. It's not about
sacrificing your life. It's about making sure your future self gets a good life too.""",
   "Friends enjoying dinner", "ENJOY IT NOW")

# ---------------- FAQ ----------------
ch("Questions people ask")
pr("""Let me answer the questions I hear most about the journey to a million.""")
sc("""Question one. Can I really do this on an average salary? Yes, although it takes time. Many 401k millionaires have earned ordinary salaries
and contributed steadily for decades. Your savings rate and time in the market matter more than your income.""",
   "Ordinary worker", "ON AN AVERAGE SALARY?")
sc("""Question two. Should I pay off my mortgage or invest? Once high interest debt is gone and your emergency fund is full, it depends on your
mortgage rate and your peace of mind. Many people do some of both. Investing has historically offered higher long term returns than low
mortgage rates, but a paid off home has real emotional value.""",
   "Mortgage and investments", "MORTGAGE OR INVEST?")
sc("""Question three. What about real estate or a business? Both can build wealth, and many millionaires own them. But they also carry more
risk, more work and less diversification. Many people build the core of their wealth through steady investing first, then add other assets
if they want.""",
   "Rental property and shop", "REAL ESTATE OR BUSINESS?")
sc("""Question four. What if the market crashes on the way? It probably will, several times. Historically, broad markets have recovered from
every major crash, though some took years. Keep contributing. Falling prices mean you're buying more shares for the same money.""",
   "Market crash recovery", "WHAT IF IT CRASHES?")
sc("""Question five. Is a million enough? It depends on your spending, where you live, and when you retire. For some people, it's more than
enough. For others, it's a milestone on the way to a bigger number. Calculate your own number: about twenty five times your yearly
spending.""",
   "Calculator personal number", "IS $1M ENOUGH?")

sc("""Question six. How long should each stage take? It varies widely. Stages one through four might take one to four years, depending on
debt and income. Stage five might take one or two. Stages six to nine take most of the journey, often twenty to thirty years in total. Faster
with higher savings rates.""",
   "Timeline chart stages", "HOW LONG EACH STAGE?")
sc("""Question seven. Do I need a financial advisor? Many people follow this playbook on their own with simple index funds. Others prefer help,
especially later. If you hire one, look for a fee only fiduciary who is legally required to act in your best interest.""",
   "Advisor meeting", "AN ADVISOR?")
sc("""And question eight. What if I'm already past some stages? Great. Start at your current stage and keep going. And double check the earlier
ones occasionally. Make sure your emergency fund is still sized right and no high interest debt has crept back.""",
   "Person climbing stairs midway", "ALREADY PAST SOME STAGES?")

# ---------------- Recap ----------------
ch("Recap: the 9 stages")
short("Broke to $1 million: the 60-second playbook")
sc("""Quick recap. At one thousand dollars a month and seven percent, a million takes about twenty eight years, and each hundred thousand comes
faster than the last. The journey feels hopeless, then boring, then long, then sudden. Focus on the system, measure yearly, celebrate
milestones, protect the snowball, and remember why.""",
   "Checklist clipboard", "THE NUMBERS AND MINDSET")
sc("""The nine stages. One: stop the bleeding. Two: build a one thousand dollar starter fund. Three: kill high interest debt. Four: build the full
emergency fund. Five: invest fifteen percent and reach ten thousand. Six: reach one hundred thousand. Seven: the long middle. Eight: the
acceleration. And nine: reach a million, and protect it.""",
   "Nine stage staircase", "THE 9 STAGES")

sc("""Before we finish, one last thought from me. When this channel started, the goal was simple: to make money less confusing and less
scary for ordinary people. Every video has been one piece of this playbook. The numbers, the psychology, and the steps. Now you have the
whole map.""",
   "Map unfolded on table", "THE WHOLE MAP")
sc("""You don't need to be perfect. You don't need to be rich to start. You need to know which stage you're in, and take the next step. Then the
next one. That's how ordinary people become millionaires. Slowly, then suddenly.""",
   "Path to sunrise", "SLOWLY, THEN SUDDENLY")

# ---------------- Close ----------------
ch("What to do next")
pr("""Figure out which stage you're in today. Then do one thing from that stage this week. That's how every millionaire's journey starts. Thank
you for watching this channel and following the playbook with me. I'm Ryan Rover. See you in the next one.""")

save("video60", "The Ryan Rover Money Playbook: From Broke to $1 Million", [
    "Federal Reserve, Survey of Consumer Finances (net worth distribution)",
    "Federal Reserve, Economic Well-Being of U.S. Households (SHED)",
    "Consumer Financial Protection Bureau, payday loan research",
    "Fidelity, quarterly retirement analysis (401(k) millionaires)",
    "Vanguard, How America Saves",
    "William P. Bengen, Determining Withdrawal Rates Using Historical Data (1994)",
    "Growth and milestone timelines: stated illustrative math at a 7% average yearly return",
], "broke to $1 million: numbers, psychology, playbook")
