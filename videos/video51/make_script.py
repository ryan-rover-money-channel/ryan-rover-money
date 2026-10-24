import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. In Ernest Hemingway's novel The Sun Also Rises, one character asks another how he went
bankrupt. The answer: two ways. Gradually, then suddenly. Here's the good news. Wealth works exactly the same way.
Slowly, then suddenly. Today, the three money habits that build wealth that way, and why most people quit right
before the suddenly part.""")
short("Wealth comes slowly, then suddenly. Here's why.")
card("""Three habits. Spend less than you earn and automate the gap. Invest that gap consistently, for a very long time.
And keep growing what you earn. That's it.""",
     {"type": "stat", "label": "the three habits", "big": "SAVE · INVEST · GROW", "size": 120, "sub": "slowly, then suddenly"})
sc("""I know. That sounds too simple. Where's the secret? The hot stock, the side hustle, the clever trick? Here's
the truth. There isn't one. The people who build real wealth on ordinary incomes almost always do some version of
these three things. What separates them from everyone else isn't knowledge. It's that they keep doing them for
years, especially during the long, boring stretch when nothing seems to happen.""",
   "Simple notebook three items", "TOO SIMPLE?")
sc("""We'll look at these three habits from three angles. First, the numbers: the math that turns small, boring
habits into a sudden jump in wealth. Second, the psychology: why these habits are so hard to keep, and what
habit science says about making them stick. And third, the playbook: a thirty day setup for each habit, so they
run on autopilot.""",
   "Three stones balanced", "THREE ANGLES")
pr("""Stay for the chart in the numbers section. It shows exactly where the suddenly happens, and it's usually much
later than people expect. Let's start.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Every number here is either from a named source or stated, simple math. Growth examples use a seven percent
average yearly return, which is an illustration, not a promise. Markets go up and down, and some years are
negative. Research on habits comes from published studies, including work at University College London.
Retirement rules come from the IRS. This is education, not financial advice.""",
   "University library", "OUR SOURCES")

# ---------------- History ----------------
ch("Slowly, then suddenly")
sc("""Hemingway's line was about going broke, but it describes almost every big change. A forest grows slowly for
decades, then seems to fill the hillside. A skill improves slowly for years, then suddenly you're the expert people
call. In money, the slow part can last ten or fifteen years. The sudden part is when compounding finally becomes
visible, and the growth starts to dwarf what you put in.""",
   "Forest growing hillside", "SLOWLY, THEN SUDDENLY")
sc("""Warren Buffett is the most famous example. Most of his enormous wealth was built after his fiftieth birthday,
not because he got smarter later in life, but because he started very young and never stopped compounding. The
habits were in place for decades before the results became dramatic.""",
   "Omaha Nebraska skyline", "BUFFETT'S LATE WEALTH")
sc("""You don't need to be Buffett for this to work. The same math applies to a teacher saving four hundred dollars a
month, or a nurse investing ten percent of each paycheck. The scale is different. The shape of the curve is the
same. A long, flat start, then a steep climb.""",
   "Teacher in classroom", "THE SAME CURVE FOR EVERYONE")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Let's look at the math behind each habit, starting with the one that makes everything
else possible.""")

ch("Habit 1: Spend less and automate the gap")
card("""Habit one. Spend less than you earn, and automate the difference. The gap between income and spending is the raw
material of all wealth.""",
     {"type": "list", "n": 1, "title": "Save the gap", "sub": "spend less than you earn, automatically"}, "HABIT 1")
sc("""The most important number in personal finance isn't your income or your investment return. It's your savings
rate, the percentage of your income you keep. Someone earning sixty thousand dollars who saves fifteen percent
is building wealth faster than someone earning one hundred fifty thousand who saves two percent.""",
   "Percentage sign coins", "YOUR SAVINGS RATE")
sc("""Here's why savings rate is so powerful. It works on both sides of the equation. When you save more, you have
more money growing. And you're also living on less, which means you need less to eventually support your
lifestyle. A higher savings rate shortens the journey from both ends at once.""",
   "Two arrows meeting", "IT WORKS BOTH WAYS")
sc("""Let's put numbers on that. Using a simple illustration, with investments growing at five percent a year after
inflation, and a goal of having twenty five times your yearly spending, here's roughly how many years it takes to
reach financial independence at different savings rates. At five percent saved, around sixty five years. At
fifteen percent, around forty three years.""",
   "Calendar years", "5% VS 15%")
sc("""At twenty percent, around thirty seven years. At thirty percent, about twenty eight years. At fifty percent,
around seventeen years. Notice how the time drops sharply as the savings rate rises. Going from five to fifteen
percent cuts more than two decades off the journey. That's the power of habit one.""",
   "Stairs going down", "20%, 30%, 50%")
card("""Years to financial independence, as an illustration, assuming five percent yearly growth after inflation and a goal
of twenty five times yearly spending.""",
     {"type": "compare", "left": {"label": "Save 10%", "big": "~52 years", "sub": "to independence"},
      "right": {"label": "Save 30%", "big": "~28 years", "sub": "to independence"},
      "note": "Illustration only. Real returns vary."})
sc("""The second half of habit one is automation. Researchers studying retirement savings have found that automatic
enrollment dramatically increases participation in workplace plans. When saving is the default, most people stick
with it. When it requires action, many never start. Automation turns a decision you'd have to make every month into
one you make once.""",
   "Automatic payment settings", "AUTOMATION WINS")

ch("Habit 2: Invest consistently and don't interrupt")
card("""Habit two. Invest the gap consistently, in diversified, low cost investments, and don't interrupt the
compounding.""",
     {"type": "list", "n": 2, "title": "Invest and wait", "sub": "consistently, cheaply, for decades"}, "HABIT 2")
sc("""This is where slowly, then suddenly becomes visible. Imagine investing five hundred dollars a month at a seven percent
average yearly return. After ten years, you'd have put in sixty thousand dollars, and the balance might be around
eighty six thousand. Nice, but not life changing. This is the slow part, and it's where many people give up.""",
   "Slow growth plant", "YEAR 10: ~$86,000")
sc("""After twenty years, you'd have put in one hundred twenty thousand dollars, and the balance could be around two
hundred sixty thousand. Now growth is doing more than half the work. After thirty years, about six hundred ten
thousand. And after forty years, roughly one point three million dollars, from two hundred forty thousand
contributed.""",
   "Tall tree", "YEAR 40: ~$1.3 MILLION")
card("""Five hundred dollars a month, at a seven percent average yearly return, for forty years. You'd put in two hundred
forty thousand dollars. Look at the shape of the curve.""",
     {"type": "growth", "monthly": 500, "rate": 0.07, "years": 40})
sc("""Look at the last ten years on that chart. The balance more than doubles, from about six hundred thousand to one
point three million, while you only add sixty thousand dollars of your own money. That's the suddenly. And here's
the critical point. You only get those last ten years if you didn't quit during the first twenty.""",
   "Mountain summit view", "THE LAST TEN YEARS")
sc("""That's why the second half of habit two matters so much: don't interrupt. The biggest threats to compounding
are not bad markets. They're people pulling money out early, stopping contributions during a downturn, or cashing
out a retirement account when changing jobs. Each interruption resets part of the curve back to the slow part.""",
   "Broken chain link", "DON'T INTERRUPT")
sc("""And keep it cheap. A one percent difference in yearly fees might sound small. But over forty years, it can reduce
the final balance by a large amount, often well over twenty percent. Low cost index funds became popular for exactly
this reason. You can't control the market. You can control what you pay.""",
   "Fee comparison chart", "KEEP IT CHEAP")

ch("The crossover point")
sc("""There's a specific moment in the curve worth knowing about. I call it the crossover point. It's the year when
your investments earn more in a typical year than you contribute. In our example, five hundred dollars a month at
seven percent, that moment arrives around year ten. From then on, in an average year, your money is adding more
than you are.""",
   "Two lines crossing chart", "THE CROSSOVER POINT")
sc("""Before the crossover, you're the engine. Every dollar of progress comes mostly from your paycheck. After the
crossover, you have two engines, and the second one keeps getting stronger. By year twenty, growth in an average
year can be two or three times your contributions. By year thirty, it can be many times larger.""",
   "Airplane two engines", "TWO ENGINES")
sc("""Of course, real markets don't deliver average years. Some years the growth is huge, and some years it's negative.
But over long periods, the shape tends to hold. And knowing that the crossover is coming makes the slow years easier
to accept. You're not failing. You're building the first engine.""",
   "Construction site building", "BUILDING THE FIRST ENGINE")

ch("The cost of a pause")
sc("""Now let's see what happens if the habit is interrupted. Same example, five hundred dollars a month for forty years.
But this time, the person stops investing for five years, from year six to year ten, because life got busy, or the
market felt scary. They skip thirty thousand dollars of contributions.""",
   "Pause button", "A FIVE YEAR PAUSE")
sc("""The result after forty years? Instead of about one point three million dollars, roughly one point zero two million.
Skipping thirty thousand dollars of contributions early on cost nearly three hundred thousand dollars at the end.
Early dollars are the most valuable dollars, because they have the most time to compound.""",
   "Money disappearing illustration", "$30,000 SKIPPED, ~$290,000 LOST")
card("""Five hundred dollars a month for forty years at seven percent. A five year pause early on skips thirty thousand
dollars of contributions, but can reduce the ending balance by nearly three hundred thousand.""",
     {"type": "compare", "left": {"label": "Never paused", "big": "~$1.31M", "sub": "after 40 years"},
      "right": {"label": "Paused years 6 to 10", "big": "~$1.02M", "sub": "after 40 years"},
      "note": "Illustration at 7% average yearly return."})
sc("""This is why habit two says don't interrupt. If money gets tight, reduce the contribution instead of stopping
completely. Even fifty dollars a month keeps the habit alive and the account growing. A smaller contribution is
almost always better than none.""",
   "Small steady stream water", "REDUCE, DON'T STOP")

ch("What everyday millionaires have in common")
sc("""Let's look at what research and data say about everyday millionaires. Fidelity, one of the largest retirement plan
providers in America, regularly reports how many of its 401k savers have balances of one million dollars or more. In
recent years, that number has been in the hundreds of thousands. Many of them aren't executives. They're people who
contributed steadily for decades.""",
   "Office workers retirement", "401(k) MILLIONAIRES")
sc("""Fidelity has noted that many of these savers contributed a meaningful share of their pay, including employer
contributions, for a long time, often more than twenty years. That's habit one and habit two, in real life. Steady
saving, steady investing, and no big interruptions.""",
   "Long road calendar years", "STEADY, FOR DECADES")
sc("""Thomas Stanley's research on millionaires found a similar pattern. Many lived below their means, avoided debt,
bought used cars, and invested regularly. Their income was often good, but not extraordinary. Their habits were
what made the difference.""",
   "Modest suburban house", "LIVING BELOW THEIR MEANS")
sc("""And here's what's notably absent from these stories. Lucky stock picks. Perfect market timing. Secret strategies.
The common thread is boring consistency, applied for a very long time. That's encouraging, because consistency is
something almost anyone can learn.""",
   "Steady clock ticking", "BORING CONSISTENCY")

ch("The habits in a bad decade")
sc("""What about bad decades? They happen. From two thousand to two thousand nine, a period that included the dot com
crash and the financial crisis, the S and P five hundred ended the decade lower than it started, even with dividends
roughly flat. People called it the lost decade.""",
   "Financial crisis headlines 2008", "THE LOST DECADE")
sc("""But someone who kept investing every month through that decade was buying shares at lower and lower prices, during
the crashes. When markets recovered in the following decade, those cheap shares grew significantly. The habit didn't
avoid the bad decade. It turned the bad decade into a buying opportunity.""",
   "Market recovery chart", "BUYING THROUGH IT")
sc("""This is the deepest reason habit two works. You don't need to know what the next decade will bring. You just need
to keep buying, keep costs low, stay diversified, and give it enough time. Past performance never guarantees future
results. But consistent buying has historically been rewarded over long periods.""",
   "Patient investor reading", "KEEP BUYING")

ch("Habit 3: Keep growing what you earn")
card("""Habit three. Keep growing your income, through skills, career moves and value, and send a share of every increase
to habits one and two.""",
     {"type": "list", "n": 3, "title": "Grow your income", "sub": "and feed the first two habits"}, "HABIT 3")
sc("""Saving and investing have a limit set by your income. You can only cut so much. But income can grow for decades.
A new skill, a certification, a job change, a promotion, a side business. For most people early in their careers,
growing income is the single biggest lever for building wealth.""",
   "Professional training class", "THE BIGGEST LEVER")
sc("""Here's how it connects to the other habits. Say your income grows by three to five percent a year over your
career, and every time it grows, you send half of the raise to your savings. Your savings rate climbs year after
year without your lifestyle ever going backward. Habit three feeds habit one, which feeds habit two.""",
   "Gears connected", "THE HABITS FEED EACH OTHER")
sc("""And early raises matter more than late ones, for the same reason early investing matters more. A ten thousand
dollar raise at twenty eight, partly invested, has nearly forty years to compound. The same raise at fifty eight has
less than ten. Investing in your skills early is one of the highest return investments available.""",
   "Young professional studying", "EARLY RAISES COMPOUND")
sc("""Here's a simple way to think about it. Every year, ask yourself one question. What could I learn or do this
year that would make me more valuable to an employer or a customer next year? Then do one thing about it. Over a
decade, those yearly answers add up to a very different career, and a very different income.""",
   "Person learning online course", "ONE QUESTION A YEAR")
sc("""And don't ignore negotiation. Many people accept the first salary offer. Research and surveys have suggested that
people who negotiate often receive higher starting pay, and starting pay sets the base for every future raise. One
uncomfortable ten minute conversation can be worth tens of thousands of dollars over a career.""",
   "Salary negotiation meeting", "NEGOTIATE THE START")
sc("""One more thought on the slow part. Many people quit because they compare their year three with someone else's year
twenty. That's like comparing a seedling with an oak tree and deciding the seedling is broken. Every large balance
you've ever seen online started as a small balance that somebody kept feeding. Give your seedling the same
patience.""",
   "Seedling next to oak tree", "SEEDLING VS OAK")
sc("""And if you need a reminder, write down three numbers today: your savings rate, your monthly investment and your
net worth. Put the note away and look at it again in a year. Most people are surprised by how much the habits
changed in twelve months, even when the balance still feels small.""",
   "Note in envelope", "THREE NUMBERS, ONE YEAR")
pr("""So that's the math. Three habits, each simple, each powerful, and together, explosive. So why does almost nobody
stick with them? That's angle two.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
pr("""Angle two. The psychology. Eight reasons these habits are so hard, and what habit science says about fixing
each one.""")
short("Why most people quit right before the money gets good")
sc("""Reason one. The slow part is boring. For years, your balance grows by amounts that feel meaningless compared
with your paycheck. Your brain craves visible progress. When it doesn't get any, it looks for something more
exciting, like a hot stock, a new car, or a different strategy. Boredom is the silent killer of wealth.""",
   "Bored person waiting", "REASON 1: BOREDOM")
sc("""The fix: track the right number. Instead of watching the balance, track your savings rate and your monthly
contribution. Those are things you control, and they improve faster. Celebrate the habit, not the result. The
result will catch up.""",
   "Habit tracker calendar", "TRACK THE HABIT")
sc("""Reason two. Present bias. Your brain values a reward today much more than a bigger reward in the future. Every
month, the money you could save competes with something you could enjoy now. The present makes a strong argument,
every single time.""",
   "Ice cream cone now", "REASON 2: PRESENT BIAS")
sc("""The fix: remove the monthly decision. Automate saving on payday so the present never gets a vote. Behavioral
economists Richard Thaler and Shlomo Benartzi designed a program called Save More Tomorrow, where workers commit in
advance to save part of future raises. In the original study, participants' savings rates rose substantially over
a few years.""",
   "Calendar future date", "SAVE MORE TOMORROW")
sc("""Reason three. Market fear. When markets drop, every instinct says sell, stop, protect what's left. But selling
after a drop locks in the loss, and stopping contributions means missing the chance to buy at lower prices. Many
of the worst investment decisions happen during the scariest weeks.""",
   "Stock market red screen", "REASON 3: FEAR")
sc("""The fix: write your plan before the drop. A simple note. When the market falls twenty percent, I will keep
investing as usual, and I won't sell. Read it when it happens. Decisions made calmly in advance are much better than
decisions made in panic.""",
   "Handwritten note", "A NOTE TO YOUR FUTURE SELF")
sc("""Reason four. Comparison. Your friend made a fortune on a meme stock, or your neighbor bought a lake house. Slow
and steady feels like losing. Social comparison pulls people off their plan, toward riskier bets or bigger
spending.""",
   "Neighbor new boat", "REASON 4: COMPARISON")
sc("""The fix: remember you only see wins, not losses, and you only see spending, not debt. Compare yourself with your
own progress last year. Did your savings rate go up? Did your net worth go up? That's the only scoreboard that
matters.""",
   "Personal progress chart", "YOUR OWN SCOREBOARD")
sc("""Reason five. All or nothing thinking. People decide to save thirty percent starting tomorrow, cut every expense,
and invest perfectly. Then a hard month comes, they miss the goal, and quit entirely. Perfection is fragile.""",
   "Broken glass", "REASON 5: ALL OR NOTHING")
sc("""The fix: start smaller than you think. Researchers at Stanford, including BJ Fogg, have written about tiny habits:
behaviors so small they're almost impossible to skip. Save one percent. Invest twenty five dollars. Then grow it. A
small habit kept for a decade beats a big habit kept for a month.""",
   "Tiny seedling", "START TINY")
sc("""Reason six. It takes longer than you think to form a habit. A study by Phillippa Lally and colleagues at University
College London found that forming a new habit took anywhere from about eighteen to over two hundred fifty days, with
an average of around sixty six days. Most people expect it to feel automatic after a week or two. When it doesn't,
they assume they've failed.""",
   "University College London", "REASON 6: ~66 DAYS")
sc("""The fix: give yourself at least three months. Expect the first weeks to feel effortful. That's normal. And
missing a single day or a single month doesn't erase the habit. The same study found that missing one occasion
didn't significantly hurt the long term result. Just restart.""",
   "Calendar three months", "GIVE IT THREE MONTHS")
sc("""Reason seven. Lifestyle creep. As income grows, spending grows with it, and habit three stops feeding habits one and
two. We covered this in my lifestyle inflation video. The fix: decide before the raise arrives what share goes to
savings. Half is a great rule.""",
   "Upscale shopping bags", "REASON 7: LIFESTYLE CREEP")
sc("""And reason eight. Identity. Many people don't see themselves as investors or savers. They think wealth is for
other kinds of people. Writer James Clear, in his book Atomic Habits, argues that lasting habits often come from
identity. Every small action is a vote for the type of person you want to become.""",
   "Person in mirror confident", "REASON 8: IDENTITY")
sc("""The fix: start saying I'm someone who saves and invests. Then prove it with a tiny action, today. Each automatic
transfer is a vote. After a few hundred votes, it's simply who you are.""",
   "Ballot vote box", "EVERY TRANSFER IS A VOTE")

# ---------------- Mid ----------------
ch("A quick favor")
pr("""Quick pause. If this is helping you think about money differently, subscribe to the channel. It's free, and it
helps me keep making these videos for you. Now, let's set up all three habits in thirty days.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
pr("""Angle three. The playbook. Here's how to set up each habit so it runs without willpower.""")
short("Set up 3 wealth habits in 30 days")
sc("""Week one, habit one. Find your real numbers. Add up your take home pay and your spending from the last two or three
months. Calculate your current savings rate. Don't judge it. Just know it. Then pick a starting target slightly
above it. If you save nothing today, start with one percent, or twenty five dollars a paycheck.""",
   "Calculator and statements", "WEEK 1: YOUR NUMBERS")
sc("""Then automate it. Set an automatic transfer from checking to a separate savings account on the day your paycheck
arrives. If you don't have an emergency fund yet, that's where this money goes first, until you have at least one
month of expenses, then three to six.""",
   "Payday automatic transfer", "WEEK 1: AUTOMATE")
sc("""Week two, habit two. Open or review your investment accounts. If your employer offers a retirement plan with a
match, make sure you're contributing at least enough to get the full match. If you're already doing that, turn on the
automatic increase feature if your plan has one, so your contribution rises a little each year.""",
   "401k benefits website", "WEEK 2: GET THE MATCH")
sc("""Then choose simple, diversified, low cost investments. Many people use broad index funds or target date funds,
which automatically adjust over time. Check the expense ratio of each fund. Lower is generally better. And set up
automatic monthly contributions, so investing happens whether you think about it or not.""",
   "Index fund expense ratio", "WEEK 2: KEEP IT SIMPLE")
sc("""Week three, habit three. Pick one income move for the next twelve months. Ask for a raise with clear evidence of
your results. Research what your role pays elsewhere. Sign up for one certification or course that's valued in your
field. Or start a small side income with a specific goal. One move, not ten.""",
   "Person preparing raise meeting", "WEEK 3: ONE INCOME MOVE")
sc("""Then write your raise rule. For example, half of every raise goes to savings and investing, automatically, the
month it arrives. Put it somewhere you'll see it, so future you doesn't forget when the excitement of a raise
arrives.""",
   "Sticky note rule", "WEEK 3: THE RAISE RULE")
sc("""Week four, protection. Write your note for market drops. Check that your emergency fund is growing. List any high
interest debt and choose a payoff plan, because interest at twenty percent works against compounding. And schedule
one money review every three months. Same day, same time. Fifteen minutes.""",
   "Calendar quarterly review", "WEEK 4: PROTECT IT")
card("""Week one, save the gap. Week two, invest automatically. Week three, one income move. Week four, protect the plan.""",
     {"type": "stat", "label": "the 30 day setup", "big": "4 WEEKS", "sub": "save, invest, grow, protect"})

ch("Three mistakes that break the habits")
sc("""Even good habits can be broken by a few big mistakes. Mistake one. Cashing out retirement accounts when changing
jobs. It can trigger taxes and penalties and resets years of compounding. Roll the money over instead.""",
   "Job change boxes office", "MISTAKE 1: CASHING OUT")
sc("""Mistake two. Taking on a big new fixed cost, like a large car payment or an expensive house, that forces you to cut
your savings rate for years. And mistake three. Chasing a big win, like putting a large share of savings into a
single stock, a coin, or a scheme promising fast returns. One big loss can undo a decade of slow gains.""",
   "Gambling chips", "MISTAKES 2 AND 3")

ch("Habit stacking for money")
pr("""Here's a practical trick from habit research. It's called habit stacking. You attach a new habit to something you
already do every day or every month.""")
sc("""For example. When my paycheck arrives, I check that the automatic transfers went out. When I pay rent, I look at my
savings rate for the month. When I get a raise, I immediately raise my retirement contribution before I spend
anything. Each new habit rides on an existing one, so you don't have to remember it separately.""",
   "Morning routine coffee", "ATTACH IT TO SOMETHING")
sc("""You can stack small daily habits too. When I make morning coffee, I spend two minutes checking my accounts. When I
want to buy something online over fifty dollars, I add it to a wish list and wait a day. These tiny routines protect
the three big habits from slowly eroding.""",
   "Wish list on phone", "TINY ROUTINES")
sc("""Habit stacking works because it uses cues that already exist in your life. You don't need more willpower. You need
better triggers. And payday is the best money trigger there is, because it happens on a predictable schedule, every
single month, for decades.""",
   "Payday calendar", "PAYDAY IS THE TRIGGER")

ch("What a habit looks like in real life")
sc("""Let's see what these habits look like in an ordinary month. On payday, three things happen automatically. Ten percent
goes to the retirement plan through payroll. Five percent goes to a high yield savings account for goals. And a fixed
amount goes to an index fund in a brokerage account. All before any spending happens.""",
   "Bank app automatic transfers", "PAYDAY, AUTOMATICALLY")
sc("""During the month, spending happens from what's left, without guilt, because the future has already been paid.
There's no daily tracking of every coffee. Just a quick weekly look at the checking balance to make sure nothing
strange is happening.""",
   "Relaxed person coffee shop", "SPEND WITHOUT GUILT")
sc("""Once a quarter, a fifteen minute review. Is the savings rate on track? Are fees low? Any new high interest debt?
Any raise coming? And once a year, a slightly bigger review, including taxes, insurance and beneficiaries. That's it.
Building wealth on autopilot takes less time than most people spend scrolling in a single evening.""",
   "Quarterly review notebook", "15 MINUTES A QUARTER")

ch("Ten things you can do today")
pr("""If you want to start right now, here are ten small actions you can do today. Pick one, or pick all ten.""")
sc("""One. Calculate your savings rate. Two. Set up a twenty five dollar automatic transfer to savings. Three. Check if
you're getting your full employer match. Four. Turn on automatic increase in your retirement plan. Five. Look up the
expense ratio of every fund you own.""",
   "Checklist with pen", "ACTIONS 1 TO 5")
sc("""Six. Write your note for market drops. Seven. Write your raise rule. Eight. List any high interest debt with its
rate. Nine. Pick one income move for the year. And ten. Put a quarterly money review on your calendar. None of these
takes more than thirty minutes. Together, they set up the three habits for life.""",
   "Calendar reminder set", "ACTIONS 6 TO 10")

ch("Why habits beat a high income")
sc("""Here's a comparison that surprises people. Two professionals. One earns two hundred thousand dollars a year but
saves almost nothing, because a big house, nice cars and private everything absorb the whole paycheck. The other earns
seventy thousand and saves fifteen percent, every year, automatically, and invests it in low cost funds.""",
   "Two professionals comparison", "HIGH INCOME VS HABITS")
sc("""After twenty years, the high earner may have a beautiful lifestyle, and very little that would survive a job loss.
The steady saver, at fifteen percent of seventy thousand, around eight hundred seventy five dollars a month at seven
percent, could have over four hundred fifty thousand dollars invested. The habit beat the income.""",
   "Growth chart steady", "THE HABIT WINS")
sc("""Income gives you the potential to build wealth. Habits decide whether you actually do. That's why the three habits
work at almost every income level, and why a high income without them often doesn't.""",
   "Key in lock", "POTENTIAL VS RESULTS")

ch("Three objections")
sc("""Objection one. This is too slow, I want to enjoy my money now. Fair. And you should. The habits don't ask you to
give up enjoyment. They ask you to save a share first, and enjoy the rest guilt free. Many people find they enjoy
spending more when they know their future is handled.""",
   "Friends enjoying dinner", "TOO SLOW?")
sc("""Objection two. The market is too risky. Markets are risky in the short term, which is why the emergency fund comes
first, and why money you need within a few years shouldn't be in stocks. But for long term money, history suggests
the bigger risk is often not investing at all, and losing ground to inflation.""",
   "Risk dial", "TOO RISKY?")
sc("""And objection three. I'll start when things settle down. Things rarely settle down. There's always a new expense,
a new worry or a new headline. The habits are designed to work in an unsettled life. Start small, start now, and
adjust as life changes.""",
   "Busy family life chaos", "WHEN THINGS SETTLE?")

# ---------------- Stories ----------------
ch("Three people, three starting points")
short("She started with $50 a month. Here's what happened.")
sc("""Let's see the three habits with three people. Rosa, twenty four, earns forty two thousand dollars a year as a
medical assistant. She starts by saving just fifty dollars a month and contributing three percent to her retirement
plan to get her employer's match. It feels tiny. For the first five years, her balance barely seems to move.""",
   "Young medical assistant", "ROSA: SMALL START")
sc("""But Rosa follows habit three. She earns a certification, then another, and moves into a better paying role. Each
time, half of the raise goes to savings. By thirty five, she's saving fifteen percent of a much higher income. By her
late forties, the growth on her investments in some years is larger than her contributions. Slowly, then
suddenly.""",
   "Woman professional confident", "ROSA: THE CLIMB")
sc("""Marcus, thirty eight, starts later, with some credit card debt. He clears the debt first, then redirects the same
monthly payment into investing. Because he's used to paying that amount, he doesn't miss it. He has fewer years than
Rosa, so his savings rate needs to be higher, and he uses catch up contributions after fifty. His curve is shorter,
but it still bends upward.""",
   "Man paying off debt", "MARCUS: LATE START")
sc("""And Helen, fifty two, has saved very little. She can't change the past, but she has her peak earning years ahead
and the kids are nearly grown. She saves a large share of her income for thirteen years, keeps costs low, and plans
to work a few years longer than she once expected. Her result is more modest, but it's the difference between a
stressful retirement and a stable one.""",
   "Older woman planning finances", "HELEN: CATCH UP")
sc("""Three people. Three starting points. The same three habits. None of them got rich quickly. All of them got
significantly richer slowly. And for each of them, the hardest part was the beginning, when the habits felt pointless
and the results were invisible.""",
   "Three people walking path", "THE SAME THREE HABITS")

ch("What the suddenly feels like")
sc("""People who reach the steep part of the curve often describe the same feeling. One day they check their account
and realize it grew more in a single good year than they used to earn in a year. Or they notice that a bad month in
the market moved their balance by more than their annual contributions. It's a strange mix of excitement and
responsibility.""",
   "Person surprised looking at laptop", "THE MOMENT YOU NOTICE")
sc("""But the most common feeling isn't excitement. It's calm. Money stops being a source of daily stress. Job decisions
get easier. Emergencies become inconveniences. The suddenly part of wealth isn't really about a number. It's about
freedom arriving, after years of quietly building it.""",
   "Calm lake sunrise", "FREEDOM ARRIVES")
sc("""And here's the part almost everyone says, looking back. I wish I had started earlier, even with less. Not because
the early amounts were large, but because the early years were the ones that made the curve bend later. If you're at
the start right now, this is your early years. Use them.""",
   "Young person starting journey", "START EARLIER")

# ---------------- FAQ ----------------
ch("Questions people ask")
pr("""Let me answer the questions people ask me most about these habits.""")
sc("""Question one. What if I can't save anything right now? Then start with habit three, growing income, and with
cutting one recurring cost. Even ten dollars a week matters, not because of the amount, but because it builds the
habit. When income grows, the habit is ready.""",
   "Small coins jar", "CAN'T SAVE ANYTHING?")
sc("""Question two. Should I pay off debt or invest first? A common order is: a small emergency fund, then grab any
employer match, then pay off high interest debt, then build a full emergency fund, then invest more. Low interest
debt, like some mortgages, can often be paid on schedule while you invest.""",
   "Debt vs invest scale", "DEBT OR INVEST?")
sc("""Question three. How do I stay motivated during the slow part? Track your savings rate, celebrate milestones like
your first ten thousand dollars, and remember the shape of the curve. The slow part is not a sign it isn't working.
It's a sign it's working exactly as expected.""",
   "Milestone celebration", "STAYING MOTIVATED")
sc("""Question four. Is seven percent a realistic return? It's an illustration often used for a diversified stock
portfolio over long periods, before inflation. Real returns vary a lot, and some decades are much worse than average.
That's why the habits matter more than the exact return. You control the saving, the cost and the consistency.""",
   "Long term stock chart", "IS 7% REALISTIC?")
sc("""Question five. What if the market crashes right after I start? Then you're buying at lower prices, which can be
an advantage for someone with decades ahead. It feels terrible in the moment, but early crashes hurt young investors
much less than late ones, because their biggest contributions are still in the future. Keep the habit going.""",
   "Market crash headline", "WHAT IF IT CRASHES?")
sc("""Question six. Do I need a financial advisor for this? Many people can set up these habits on their own with simple,
low cost funds. If you want help, consider a fee only advisor, who charges a clear fee rather than commissions, and ask
whether they act as a fiduciary.""",
   "Advisor meeting table", "DO I NEED AN ADVISOR?")
sc("""And question seven. Is it ever too late? No. The curve is shorter, but it still bends. Starting at fifty with high
savings and a few extra working years can make a big difference. The worst number of years to wait is one more.""",
   "Sunrise new day", "TOO LATE?")

# ---------------- Recap ----------------
ch("Recap")
short("The 3 habits behind almost every ordinary millionaire")
sc("""Quick recap. Habit one: spend less than you earn and automate the gap. Your savings rate is the most important
number you control. Habit two: invest consistently, cheaply, and don't interrupt the compounding. Habit three: keep
growing your income, and send half of every raise to the first two habits.""",
   "Checklist clipboard", "THE THREE HABITS")
sc("""And remember why it's hard: boredom, present bias, fear, comparison, all or nothing thinking, slow habit formation,
lifestyle creep and identity. Start tiny, automate everything, give it at least three months, and let the long, flat
start turn into the steep climb. Slowly, then suddenly.""",
   "Curve rising steeply", "SLOWLY, THEN SUDDENLY")

# ---------------- Close ----------------
ch("What to do next")
pr("""If you want the full step by step plan, from your first dollar to your first million, it's in my playbook. The
link is in the description. And watch my video on lifestyle inflation next. It's the biggest threat to habit three.
I'm Ryan Rover. See you in the next one.""")

save("video51", "3 Money Habits That Build Wealth: Slowly, Then Suddenly", [
    "Ernest Hemingway, The Sun Also Rises (1926): gradually, then suddenly",
    "Thaler and Benartzi, Save More Tomorrow, Journal of Political Economy (2004)",
    "Lally et al., How are habits formed, European Journal of Social Psychology (2010): average about 66 days",
    "BJ Fogg, Tiny Habits (2019); James Clear, Atomic Habits (2018)",
    "Research on automatic enrollment in retirement plans (Madrian and Shea, 2001)",
    "IRS, retirement plan contribution and catch-up rules (check current limits)",
    "Growth and savings rate figures: stated illustrative math (7% nominal; 5% real for independence estimates)",
], "three wealth habits: numbers, psychology, playbook")
