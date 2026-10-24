import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short


EXTRA = {
1: ("""How to apply it in 2027: open a separate high yield savings account if you don't have one, name it Emergency Fund, and set an automatic
transfer for the day after payday. Then put a share of your tax refund in it this spring. Those two moves alone can get many people to their
first thousand dollars.""",
  "Savings account and calendar", "2027: OPEN, AUTOMATE, REFUND"),
2: ("""How to apply it in 2027: log into your retirement plan in January and write down your current contribution rate. If it's below fifteen
percent, raise it by at least one or two points now, and schedule another increase for July. If you get a raise this year, send half of it
to your retirement contribution.""",
  "Retirement plan login", "2027: RAISE IT IN JANUARY"),
3: ("""How to apply it in 2027: if you change jobs this year, ask about the match during the offer process, and enroll on day one. Some
employers have waiting periods or require you to opt in. Don't let months of free money slip by because of paperwork.""",
  "New job paperwork", "2027: ENROLL ON DAY ONE"),
4: ("""How to apply it in 2027: write every debt on one page with its balance, rate and minimum payment. Circle the highest rate. That's
your target for the year. Set an automatic extra payment toward it, even fifty dollars a month, and add any windfalls.""",
  "Debt list one page", "2027: CIRCLE THE TARGET"),
5: ("""How to apply it in 2027: if your lease is up this year, compare at least three alternatives before renewing, and use them to
negotiate. If you own, check whether your property taxes and insurance have risen and shop your homeowners policy. Small housing savings
repeat every single month.""",
  "Lease renewal document", "2027: SHOP BEFORE RENEWING"),
6: ("""How to apply it in 2027: use the rule of seventy two on your own accounts. What rate is your savings account earning, and how long until
it doubles? What rate is your credit card charging? Seeing those two numbers side by side is often the push people need to move money to
the right place.""",
  "Two numbers compared", "2027: RUN YOUR NUMBERS"),
7: ("""How to apply it in 2027: look up the expense ratio of every fund you own. It's listed on your account website or the fund's page. If
any fund charges much more than a comparable index fund, consider whether it's worth it. Check for account fees too, like advisory fees or
maintenance charges.""",
  "Fund details page", "2027: LOOK UP YOUR FEES"),
8: ("""How to apply it in 2027: if your car is paid off and reliable, keep driving it and send the old payment amount to savings. If you need a
car, set a total budget before you shop, get financing quotes from a credit union before visiting the dealer, and focus on the total price,
not the monthly payment.""",
  "Credit union auto loan", "2027: TOTAL PRICE, NOT PAYMENT"),
9: ("""How to apply it in 2027: add up your spending for 2026, multiply by twenty five, and write the number down. Then compare it with what you
have invested today. The gap tells you how far you have to go, and the savings rate table can tell you roughly how long it will take.""",
  "Notebook number written", "2027: WRITE YOUR NUMBER"),
10: ("""How to apply it in 2027: pick a date, like New Year's Day or your birthday, and calculate your net worth every year on that date. Keep a
simple list going back year after year. Over a decade, that list becomes one of the most motivating documents you own.""",
  "Yearly list net worth", "2027: PICK A DATE"),
11: ("""How to apply it in 2027: set up your transfers so they happen the same day your pay arrives, and give each one a clear job: emergency
fund, investing, sinking funds. Then forget about them. Check once a month that they ran.""",
  "Payday transfers list", "2027: SAME DAY AS PAYDAY"),
12: ("""How to apply it in 2027: write down your three favorite ways to spend money, the ones that truly make your life better. Then look at your
last three months of spending and circle everything that didn't make you happier. That's where your cuts come from, painlessly.""",
  "List of favorites", "2027: NAME YOUR THREE"),
13: ("""How to apply it in 2027: keep a wish list. When you want something, add it to the list with the date and price. Review the list every
couple of weeks. Many people find that most items no longer feel important, and the few that remain are the ones truly worth buying.""",
  "Wish list on phone", "2027: KEEP A WISH LIST"),
14: ("""How to apply it in 2027: unfollow accounts that make you feel you need to buy things, and follow a few that teach you about money. Your
feed shapes your wants more than you think. Change the feed, and you change the wants.""",
  "Unfollow button", "2027: CHANGE YOUR FEED"),
15: ("""How to apply it in 2027: talk to older family members about scams, since criminals often target them. Agree on a family code word for
emergencies, so a fake call claiming a relative is in trouble can be checked. And set up account alerts for large transactions on every
bank and card account.""",
  "Family conversation", "2027: A FAMILY CODE WORD"),
16: ("""How to apply it in 2027: write down your plan for the next market drop before it happens. For example: when the market falls twenty
percent, I keep my contributions the same and do not sell. Having it in writing makes it much easier to follow when headlines get scary.""",
  "Written plan market drop", "2027: WRITE YOUR DROP PLAN"),
17: ("""How to apply it in 2027: if someone pitches you an investment, ask three questions. How does it make money? What are all the fees? What
happens if I need my money back? If the answers are vague or pressured, walk away.""",
  "Three questions list", "2027: ASK THREE QUESTIONS"),
18: ("""How to apply it in 2027: make a list of every money task you still do manually, like transferring savings, paying bills or investing.
Automate one per week for the next month. By February, your money will mostly run itself.""",
  "Automation checklist", "2027: ONE PER WEEK"),
19: ("""How to apply it in 2027: before your next raise arrives, decide exactly how much will go to savings and how much to your lifestyle. Write
it down. Once the money hits your account, it's much harder to decide calmly.""",
  "Decision written in advance", "2027: DECIDE BEFORE IT ARRIVES"),
20: ("""How to apply it in 2027: plan one experience you'll pay for in cash this year, something that truly matters to you. A trip, a class, a
family event. Put it in a sinking fund. Money becomes much more meaningful when it's connected to the life you want.""",
  "Family trip planning", "2027: PLAN ONE EXPERIENCE"),
21: ("""How to apply it in 2027: put a reminder in your calendar to check one bureau every four months, or all three at once a couple of times a
year. It takes about fifteen minutes and costs nothing.""",
  "Calendar reminders", "2027: SET A REMINDER"),
22: ("""How to apply it in 2027: freeze your credit at all three major bureaus this month. Save the logins or PINs somewhere secure. Consider
doing the same for your children, since child identity theft can go undetected for years.""",
  "Three bureau logos", "2027: ALL THREE BUREAUS"),
23: ("""How to apply it in 2027: review each insurance policy once this year. Is your deductible right for your emergency fund? Is your liability
coverage enough? Do you still need every add on? Many people find savings and gaps at the same time.""",
  "Insurance review", "2027: REVIEW EACH POLICY"),
24: ("""How to apply it in 2027: log into every account with a beneficiary option, including retirement plans, IRAs, life insurance and bank
accounts that allow payable on death designations. Make sure the names are current. Life changes like marriage, divorce and new children are
the most common reasons they go out of date.""",
  "Beneficiary forms", "2027: CHECK EVERY ACCOUNT"),
25: ("""How to apply it in 2027: pick three bills to negotiate in the first quarter: for example internet, phone and car insurance. Call, ask
for a better rate or a loyalty discount, and mention competitor prices. Even one success can save hundreds over the year.""",
  "Phone call negotiation", "2027: THREE CALLS"),
26: ("""How to apply it in 2027: if you're eligible for an IRA, consider contributing early in the year rather than at the deadline, so your money
has more time to grow. And if you have a high deductible health plan, check whether you're using your health savings account fully.""",
  "IRA contribution early", "2027: CONTRIBUTE EARLY"),
27: ("""How to apply it in 2027: when you sign up for a free trial, set a calendar reminder for the day before it ends. Many subscriptions start
as free trials that people simply forget to cancel.""",
  "Free trial reminder", "2027: TRIAL REMINDERS"),
28: ("""How to apply it in 2027: list every irregular expense you had in 2026. Add them up and divide by twelve. That's your monthly sinking fund
total. Set it up as an automatic transfer and split it into buckets.""",
  "List of 2026 expenses", "2027: LIST LAST YEAR'S"),
29: ("""How to apply it in 2027: schedule your first money date in January. Bring three things: a list of accounts and balances, your top goal
for the year, and one thing you'd love to spend on. Start with goals, not blame.""",
  "Couple at table planning", "2027: FIRST DATE IN JANUARY"),
30: ("""How to apply it in 2027: choose one skill that would make you more valuable at work and commit to learning it this year. Ask your employer
about training budgets or tuition help. Many companies offer them, and many employees never use them.""",
  "Training budget form", "2027: ONE SKILL THIS YEAR"),
}

def rule(n, title, sub, paras):
    ch(f"Rule {n}. {title}")
    card(f"Rule {n}. {title}.", {"type": "list", "n": n, "title": title, "sub": sub}, f"RULE {n}")
    for t, q, c in paras:
        sc(t, q, c)
    sc(*EXTRA[n])

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. A new year is coming, and with it, a fresh start for your money. But instead of vague resolutions that fade by
February, I want to give you something better: thirty simple money rules to live by in 2027. Rules you can remember, rules you can follow,
and rules that work whether you earn thirty thousand dollars or three hundred thousand.""")
short("30 money rules to live by in 2027")
sc("""Why rules instead of goals? Because goals tell you where you want to go, but rules tell you what to do every day. Rules remove decisions.
When you already know your rule, you don't have to think about it in the moment, when emotions are high and willpower is low.""",
   "Rule book on desk", "RULES REMOVE DECISIONS")
sc("""We'll go through these thirty rules in three groups, three angles. First, ten rules about the numbers: the targets and ratios that keep
your finances healthy. Second, ten rules about the psychology: how to think and behave with money. And third, ten action rules: the playbook
of habits that protect and grow what you have.""",
   "Three stacks of cards", "THREE ANGLES, 30 RULES")
pr("""Stay for rule fifteen. It could protect you from one of the fastest growing threats to your money. Let's start with the numbers.""")

ch("Why rules beat resolutions")
sc("""Every January, millions of people make financial resolutions. Save more. Spend less. Pay off debt. And by spring, many have quietly
given up. The problem isn't motivation. It's that resolutions are vague, and vague goals give your brain nothing specific to do.""",
   "New year resolutions list", "RESOLUTIONS FADE")
sc("""Psychologists call specific plans implementation intentions. Research by psychologist Peter Gollwitzer and others found that people who
decide in advance exactly what they'll do in a specific situation are more likely to follow through. When X happens, I do Y. Money rules work
the same way.""",
   "If then plan", "WHEN X, I DO Y")
sc("""When a raise arrives, half goes to savings. When I want something over one hundred dollars, I wait forty eight hours. When the market
drops, I keep investing. Each rule is a decision made once, calmly, that protects you in hundreds of future moments.""",
   "Calm decision", "DECIDE ONCE")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Guidelines in this video come from widely used sources, including the Federal Reserve, the Consumer Financial Protection Bureau, the
Federal Trade Commission, the IRS and Fidelity. Growth examples are stated math and are illustrations, not promises. These rules are
general guidelines, not personal advice, and your situation may call for different numbers.""",
   "Government buildings", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. Ten rules about the numbers.""")
short("10 money numbers everyone should know")

rule(1, "Keep 3 to 6 months of essentials in cash", "your financial airbag", [
("""Rule one. Keep three to six months of essential expenses in a high yield savings account. In recent Federal Reserve surveys, more than a
third of American adults said they couldn't cover a four hundred dollar emergency with cash. An emergency fund is what keeps surprises from
becoming debt.""",
 "Emergency fund jar", "3 TO 6 MONTHS"),
("""If you're starting from zero, start with five hundred dollars, then one thousand, then one month. Every stage protects you more than the
last. In 2027, make this your first priority if you don't have it yet.""",
 "Staircase stages", "START WITH $500"),
])

rule(2, "Save at least 15% for retirement", "including the match", [
("""Rule two. Save at least fifteen percent of your gross income for retirement, including any employer match. It's one of the most common
guidelines from retirement planners. If you start late, aim higher.""",
 "Fifteen percent sign", "15% OR MORE"),
("""If fifteen percent isn't possible yet, raise your contribution by one percent every few months. Many workplace plans offer automatic
increases. Turn them on, and in a couple of years you'll get there without feeling a sudden pinch.""",
 "Percentage stairs", "ONE PERCENT AT A TIME"),
])

rule(3, "Never leave the match on the table", "it's part of your pay", [
("""Rule three. If your employer matches retirement contributions, always contribute enough to get the full match. On a sixty thousand dollar
salary, a four percent match is twenty four hundred dollars a year. Not taking it is turning down a raise.""",
 "401k match illustration", "FREE MONEY"),
("""Check your plan's match formula and vesting schedule this month. If you're not getting the full match, fixing it might be the single
highest return move you make all year.""",
 "Benefits portal login", "CHECK IT THIS MONTH"),
])

rule(4, "Pay off any debt above about 8%", "a guaranteed return", [
("""Rule four. Treat debt above roughly eight percent interest as an emergency. Credit card rates have often averaged above twenty percent in
recent years, according to Federal Reserve data. Paying off a twenty two percent card is like earning a guaranteed twenty two percent
return.""",
 "Credit card interest", "ABOVE 8% = PRIORITY"),
("""List your debts by interest rate, pay minimums on all of them, and attack the highest rate first. When one is gone, roll its payment into
the next.""",
 "Debt list ranked", "HIGHEST RATE FIRST"),
])

rule(5, "Keep housing around 30% of gross income or less", "the biggest lever", [
("""Rule five. A common guideline is to keep housing costs at or below about thirty percent of gross income. Housing is usually the largest
expense in any budget, around a third of household spending in BLS data. Getting this one decision right makes every other goal easier.""",
 "House with percentage", "~30% OR LESS"),
("""In expensive cities, that may not be possible right away. If so, look for ways to bring it down over time: a roommate, a cheaper unit at
renewal, or a smaller home. Every hundred dollars saved on housing is twelve hundred a year.""",
 "Roommates apartment", "BRING IT DOWN OVER TIME"),
])

rule(6, "Use the rule of 72", "know how fast money doubles", [
("""Rule six. Divide seventy two by an interest rate to estimate how many years it takes money to double. At seven percent, money doubles in
about ten years. At ten percent, about seven years.""",
 "Rule of 72 formula", "72 ÷ RATE = YEARS TO DOUBLE"),
("""It works for debt too. At twenty two percent credit card interest, an unpaid balance can roughly double in about three and a half years
if interest keeps compounding. Knowing this one number helps you understand both sides of compounding.""",
 "Debt doubling", "IT WORKS FOR DEBT TOO"),
])

rule(7, "Keep investment fees as low as possible", "small fees, big costs", [
("""Rule seven. Pay attention to the expense ratio, the yearly fee on a fund. Many broad index funds charge well under a quarter of a percent.
Some actively managed funds charge one percent or more.""",
 "Fund fees comparison", "WATCH THE EXPENSE RATIO"),
("""The difference adds up. Investing five hundred dollars a month for thirty years, a six percent net return could grow to about five hundred
two thousand dollars. A five percent net return, the same investment with one percent more in fees, about four hundred sixteen thousand.
That one percent costs roughly eighty six thousand dollars.""",
 "Two growth curves fees", "1% IN FEES = ~$86K"),
])
card("""Five hundred dollars a month for thirty years, at a six percent net return versus five percent after an extra one percent in fees.""",
     {"type": "compare", "left": {"label": "6% net", "big": "~$502K", "sub": "low fee fund"},
      "right": {"label": "5% net", "big": "~$416K", "sub": "1% more in fees"},
      "note": "Illustration. Returns are not guaranteed."})

rule(8, "Keep total car costs under control", "cars are the quiet wealth killer", [
("""Rule eight. A popular guideline is the twenty four ten rule: put at least twenty percent down, finance for no more than four years, and
keep total car costs, including payment, insurance and gas, under ten percent of gross income. Many people use a looser version, but the
idea is the same.""",
 "Car dealership", "THE 20/4/10 RULE"),
("""Cars lose value quickly, especially in the first few years. Buying a reliable used car and keeping it for a long time is one of the most
consistent wealth building habits there is.""",
 "Reliable used car", "BUY RELIABLE, KEEP IT LONG"),
])

rule(9, "Know your number: 25 times spending", "what enough looks like", [
("""Rule nine. Know roughly how much you need to be financially independent. Based on the four percent rule from William Bengen's 1994
research, a common estimate is twenty five times your yearly spending. Spend forty thousand a year, and your number is about one million
dollars.""",
 "Calculator target number", "SPENDING × 25"),
("""It's a rough guideline, and early retirees often use a more cautious multiple. But knowing your number turns retirement from a vague worry
into a concrete target.""",
 "Target on wall", "A CONCRETE TARGET"),
])

rule(10, "Check your net worth once a year", "the scoreboard that matters", [
("""Rule ten. Once a year, add up what you own and subtract what you owe. That's your net worth, the single best measure of financial
progress. Fidelity suggests rough retirement savings targets of about one times your salary by thirty, three times by forty, and six times by
fifty.""",
 "Net worth chart", "ONCE A YEAR"),
("""Don't panic if you're behind. Watch the direction. A net worth that rises every year, even slowly, means your plan is working.""",
 "Rising line chart", "WATCH THE DIRECTION"),
])

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
pr("""Angle two. Ten rules about how to think and behave with money.""")
short("10 money mindset rules that change everything")

rule(11, "Pay yourself first", "the future gets paid before the present", [
("""Rule eleven. Before you pay for anything else, pay your future. Set up automatic transfers to savings and investing on payday. What's left
is yours to spend. This flips the usual order, where people save whatever happens to be left over, which is often nothing.""",
 "Paycheck arrows to savings", "FUTURE FIRST"),
("""This rule works because it doesn't rely on discipline. Once it's set, it happens whether you're motivated or not.""",
 "Automatic transfer", "NO DISCIPLINE REQUIRED"),
])

rule(12, "Spend extravagantly on what you love, cut mercilessly on what you don't", "conscious spending", [
("""Rule twelve. This idea, popularized by author Ramit Sethi, is called conscious spending. Identify the two or three things that bring you
real joy, and spend on them without guilt. Then cut costs ruthlessly everywhere else.""",
 "Happy person hobby", "LOVE IT OR CUT IT"),
("""This is how people save a lot without feeling deprived. They aren't spending less on everything. They're spending more on what matters
and nothing on what doesn't.""",
 "Balanced scale", "NOT DEPRIVED"),
])

rule(13, "Wait 48 hours before big purchases", "let the impulse pass", [
("""Rule thirteen. For any non essential purchase above a set amount, say one hundred dollars, wait forty eight hours. For very large purchases,
wait thirty days. Many impulse urges fade once the moment passes.""",
 "Shopping cart wait timer", "48 HOURS"),
("""Remove saved cards from shopping apps and unsubscribe from sale emails. Adding a little friction gives your rational brain time to catch
up with your emotional brain.""",
 "Unsubscribe emails", "ADD FRICTION"),
])

rule(14, "Don't compare your finances to social media", "you only see the highlights", [
("""Rule fourteen. Online, you see vacations, new cars and renovations. You don't see the credit card statements, the loans, or the stress.
Comparing your behind the scenes with someone else's highlight reel will make you feel poor and push you to overspend.""",
 "Social media phone scrolling", "HIGHLIGHTS ONLY"),
("""Measure your progress against your own past. Is your savings rate higher than last year? Is your debt lower? That's the only comparison
that matters.""",
 "Person running own race", "YOU VS. YOU"),
])

rule(15, "If it sounds too good to be true, it is", "scams are exploding", [
("""Rule fifteen. According to the Federal Trade Commission, consumers reported losing more than twelve billion dollars to fraud in 2024, and
investment scams were the largest category of losses. Scammers use fake investment platforms, romance scams, impersonation of banks and
government agencies, and promises of guaranteed returns.""",
 "Scam warning phone", "$12 BILLION+ LOST TO FRAUD"),
("""Protect yourself with simple rules. No legitimate investment guarantees high returns with no risk. Never send money to someone you've only
met online. Never pay with gift cards or crypto because someone says it's urgent. And when in doubt, hang up and call the official number
yourself.""",
 "Hang up phone", "HANG UP AND VERIFY"),
])

rule(16, "Time in the market beats timing the market", "stay invested", [
("""Rule sixteen. Trying to jump in and out of the market to avoid drops usually backfires. Some of the market's best days have historically
come shortly after its worst days. Investors who sell in a panic often miss the recovery.""",
 "Market chart rebound", "STAY INVESTED"),
("""Invest regularly, in good markets and bad. When prices fall, your regular contributions simply buy more shares.""",
 "Buying shares regularly", "KEEP BUYING"),
])

rule(17, "Never invest in what you can't explain", "understand it first", [
("""Rule seventeen. If you can't explain how an investment makes money in two sentences, don't buy it. Complexity often hides high fees, high
risk, or both.""",
 "Confusing chart", "EXPLAIN IT IN 2 SENTENCES"),
("""Broad index funds are easy to explain: you own a small piece of many companies, and you share in their growth. That simplicity is a
feature, not a weakness.""",
 "Simple pie chart", "SIMPLE IS A FEATURE"),
])

rule(18, "Automate every good decision", "systems beat willpower", [
("""Rule eighteen. Automate savings, investing, bill payments, and contribution increases. Every decision you automate is one you never have to
make again when you're tired, busy or tempted.""",
 "Gears automation", "SYSTEMS BEAT WILLPOWER"),
("""Researchers Richard Thaler and Shlomo Benartzi showed with their Save More Tomorrow program that automatic, pre committed increases helped
workers raise their savings rates dramatically. Automation works with human nature, not against it.""",
 "Save More Tomorrow chart", "IT WORKS WITH HUMAN NATURE"),
])

rule(19, "Let your lifestyle rise slower than your income", "beat lifestyle creep", [
("""Rule nineteen. When you get a raise, send at least half of it to savings and investing. Enjoy the other half. Your life still improves,
but your savings rate climbs every year.""",
 "Split raise jar", "HALF OF EVERY RAISE"),
("""Lifestyle creep is how people with good incomes stay stuck. Each upgrade feels small, but together they lock in high fixed costs. This
rule keeps you moving forward.""",
 "Spending creeping", "AVOID THE CREEP"),
])

rule(20, "Money is a tool, not a scoreboard", "use it for a good life", [
("""Rule twenty. The goal isn't the biggest number. It's a life with security, freedom and meaning. Use money to buy time, experiences,
health and peace of mind.""",
 "Family enjoying time", "A TOOL FOR A GOOD LIFE"),
("""Research by psychologists including Elizabeth Dunn has suggested that spending on experiences, on others, and on buying back time can
increase happiness more than spending on more stuff. Keep that in mind when you plan your spending.""",
 "Friends experience", "EXPERIENCES AND TIME"),
])

# ---------------- Mid ----------------
ch("A quick favor")
pr("""Quick pause. If these rules are useful, subscribe to the channel. It's free, and it helps me keep making these videos for you all year.
Now, the last ten. The action rules.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
pr("""Angle three. Ten action rules. The habits that protect and grow your money.""")
short("10 money habits to start in 2027")

rule(21, "Check your credit reports regularly", "catch errors and fraud", [
("""Rule twenty one. You can check your credit reports from the three major bureaus for free at annualcreditreport dot com, the official
site. Look for accounts you don't recognize and errors in your payment history.""",
 "Credit report website", "FREE REPORTS"),
("""Errors happen, and they can raise your borrowing costs. Disputing them is free. And unfamiliar accounts can be an early warning of identity
theft.""",
 "Dispute letter", "DISPUTE ERRORS"),
])

rule(22, "Freeze your credit", "free protection", [
("""Rule twenty two. A credit freeze stops new lenders from accessing your credit report, which makes it much harder for criminals to open
accounts in your name. Under federal law, freezing and unfreezing your credit with each bureau is free.""",
 "Lock on credit card", "FREEZE IS FREE"),
("""You can temporarily lift the freeze when you apply for a loan or a new card. It takes a few minutes online, and it's one of the best
protections available.""",
 "Laptop unlock", "LIFT IT WHEN NEEDED"),
])

rule(23, "Insure against catastrophe, not inconvenience", "protect what matters", [
("""Rule twenty three. Insurance is for events that would wreck your finances: serious illness, disability, death of an earner, a house fire,
a major lawsuit. Make sure those are covered with health, disability, term life if others depend on you, home or renters, and adequate
liability coverage.""",
 "Insurance documents", "COVER THE CATASTROPHES"),
("""For small risks, like a phone screen or a minor car dent, extended warranties and low deductibles often cost more than they're worth.
Your emergency fund can cover those.""",
 "Extended warranty offer", "SKIP THE SMALL STUFF"),
])

rule(24, "Name your beneficiaries and have a will", "protect the people you love", [
("""Rule twenty four. Make sure every retirement account and life insurance policy has up to date beneficiaries. In many cases, beneficiary
designations can override what a will says.""",
 "Beneficiary form", "UPDATE BENEFICIARIES"),
("""And have at least a basic will, especially if you have children. It's one of the kindest things you can do for your family, and it often
costs far less than people expect.""",
 "Signing will", "HAVE A WILL"),
])

rule(25, "Always negotiate", "the ask costs nothing", [
("""Rule twenty five. Negotiate your salary, your rent renewal, your insurance, your internet bill, and large purchases. Not every negotiation
works, but asking politely costs nothing.""",
 "Negotiation handshake", "ASK"),
("""Salary matters most. A raise compounds into future raises and retirement contributions for the rest of your career. Research typical pay
for your role, bring evidence of your results, and ask.""",
 "Salary research laptop", "SALARY FIRST"),
])

rule(26, "Use tax advantaged accounts first", "keep more of your money", [
("""Rule twenty six. Before investing in a regular brokerage account, use tax advantaged accounts: your workplace plan, an IRA, and a health
savings account if you qualify. Check the IRS website for the 2027 contribution limits, since they're adjusted for inflation.""",
 "IRS website", "TAX ADVANTAGES FIRST"),
("""Over decades, the tax savings can add up to tens of thousands of dollars or more. It's one of the simplest ways to make your money grow
faster without taking more risk.""",
 "Tax savings growth", "GROW FASTER, SAME RISK"),
])

rule(27, "Review subscriptions twice a year", "stop the silent leaks", [
("""Rule twenty seven. In a 2022 survey by C plus R Research, people underestimated their monthly subscription spending by more than half.
Twice a year, list every recurring charge and cancel what you don't use.""",
 "Subscriptions list phone", "TWICE A YEAR"),
("""Put the reviews on your calendar, for example in January and July. And rotate streaming services instead of keeping them all at once.""",
 "Calendar January July", "JANUARY AND JULY"),
])

rule(28, "Build sinking funds for predictable costs", "no more surprise bills", [
("""Rule twenty eight. Car repairs, holidays, birthdays and annual bills aren't emergencies. They're predictable, just irregular. Set aside a
small amount every month in separate savings buckets for each one.""",
 "Labeled savings buckets", "PLAN THE IRREGULAR"),
("""Sinking funds protect your emergency fund and your budget. When the bill arrives, the money is already there.""",
 "Calm bill payment", "THE MONEY IS WAITING"),
])

rule(29, "Talk about money with the people you share life with", "one team", [
("""Rule twenty nine. If you have a partner, talk about money regularly: goals, debts, spending, and fears. Money is one of the most commonly
reported sources of stress in relationships. Regular, calm conversations prevent bigger conflicts later.""",
 "Couple money talk", "TALK REGULARLY"),
("""Try a monthly money date: thirty minutes, a quick review, and one decision for the month ahead. End it with something fun.""",
 "Money date coffee", "A MONTHLY MONEY DATE"),
])

rule(30, "Invest in yourself every year", "your biggest asset", [
("""Rule thirty. For most people, their ability to earn is their biggest financial asset. Every year, invest in it: a new skill, a
certification, a course, better health, or stronger relationships in your field.""",
 "Person studying course", "YOUR BIGGEST ASSET"),
("""A skill that raises your income by even a few thousand dollars a year can be worth more than almost any investment decision. And unlike
the market, it's something you control.""",
 "Career growth", "SOMETHING YOU CONTROL"),
])

sc("""Notice how the action rules work together. Checking your reports, freezing your credit and naming beneficiaries protect what you have.
Negotiating, tax advantages and investing in yourself grow it. Sinking funds, subscription reviews and money conversations keep the whole
system running smoothly. None of them takes long. Together, they make your finances far more resilient.""",
   "Interlocking gears", "THEY WORK TOGETHER")

# ---------------- Month by month ----------------
ch("A month by month plan for 2027")
sc("""Here's a simple way to roll these rules out over the year. January: rules two, eleven and eighteen. Raise your retirement contribution,
pay yourself first, and automate. February: rules twenty one and twenty two. Check and freeze your credit. March: rules four and twenty five.
Target your highest rate debt and negotiate three bills.""",
   "Calendar January to March", "JANUARY TO MARCH")
sc("""April: rule one, using your tax refund to build your emergency fund. May: rules seven and twenty six, fees and tax advantaged accounts.
June: rules twenty three and twenty four, insurance and beneficiaries. July: rule twenty seven, the mid year subscription review.""",
   "Calendar April to July", "APRIL TO JULY")
sc("""August: rule twenty eight, sinking funds for the holidays. September: rule thirty, pick a skill. October: rule sixteen, write your
market drop plan. November: rule twelve, plan spending you love for the holidays. And December: rules nine and ten, your number and your net
worth. By the end of the year, all thirty rules are part of your life.""",
   "Calendar August to December", "AUGUST TO DECEMBER")

# ---------------- Stories ----------------
ch("What a year of rules can do")
short("What one year of following money rules can do")
sc("""Let's imagine one person following these rules for a year. Carmen earns fifty eight thousand dollars and starts 2027 with about eight
hundred dollars in savings, a three thousand dollar credit card balance, and a five percent retirement contribution with a five percent
match she wasn't fully getting.""",
   "Young woman at desk January", "CARMEN IN JANUARY")
sc("""In January, she raises her contribution to get the full match and automates everything. In March, she negotiates her internet and
insurance, saving about sixty dollars a month. In April, she puts most of her tax refund toward the card. By summer, the card is gone, and its
payment flows into her emergency fund.""",
   "Credit card paid off", "CARMEN BY SUMMER")
sc("""By December, Carmen has about four thousand dollars in her emergency fund, no credit card debt, a higher retirement balance, frozen credit,
updated beneficiaries, and a clear yearly net worth number. Nothing dramatic happened. She just followed a handful of rules, month after
month.""",
   "Woman confident December", "CARMEN IN DECEMBER")
sc("""This is an illustration, not a promise. But it shows how simple rules, applied consistently, can change a financial life in a single
year. And the second year is usually easier than the first, because the systems are already in place.""",
   "Second year easier path", "YEAR TWO IS EASIER")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. Which rule matters most? If you only follow one, make it rule eleven, pay yourself first, with automation. It quietly powers
most of the others.""",
   "Number one trophy", "THE MOST IMPORTANT RULE")
sc("""Question two. What if I can't follow a rule because of my situation? That's fine. These are guidelines, not laws. If your housing is
above thirty percent or you can't save fifteen percent yet, focus on moving in the right direction. Progress beats perfection.""",
   "Direction arrow", "PROGRESS BEATS PERFECTION")
sc("""Question three. What if my partner doesn't want to follow these rules? Start with the ones you can do on your own, like your own
retirement contribution, your credit freeze and your subscriptions. Share results, not lectures. When a partner sees the emergency fund
grow or a debt disappear, they're often more willing to join in.""",
   "Couple different views", "A PARTNER WHO ISN'T ON BOARD")
sc("""Question four. How do I remember all thirty? You don't need to. Print the list, or save it on your phone, and review it once a month
during your money check. Over time, the rules you use most become automatic, and you'll only need the list for the rest.""",
   "Printed list on fridge", "HOW TO REMEMBER THEM")
sc("""And question five. Are these rules different for 2027 than for any other year? Mostly not. Good money rules are timeless. What changes
each year are the details: contribution limits, interest rates, tax rules, and new types of scams. Check the official sources each year for
the latest numbers.""",
   "Timeless clock", "TIMELESS RULES")

# ---------------- Recap ----------------
ch("Recap: all 30 rules")
short("All 30 money rules in 60 seconds")
sc("""Let's recap all thirty. The numbers. One: three to six months of essentials in cash. Two: save fifteen percent for retirement. Three:
never leave the match on the table. Four: pay off debt above about eight percent. Five: housing around thirty percent or less.""",
   "Checklist rules 1 to 5", "RULES 1 TO 5")
sc("""Six: use the rule of seventy two. Seven: keep investment fees low. Eight: keep car costs under control. Nine: know your number, twenty five
times spending. Ten: check your net worth once a year.""",
   "Checklist rules 6 to 10", "RULES 6 TO 10")
sc("""The psychology. Eleven: pay yourself first. Twelve: spend on what you love, cut what you don't. Thirteen: wait forty eight hours. Fourteen:
don't compare to social media. Fifteen: if it sounds too good to be true, it is.""",
   "Checklist rules 11 to 15", "RULES 11 TO 15")
sc("""Sixteen: time in the market beats timing. Seventeen: never invest in what you can't explain. Eighteen: automate every good decision.
Nineteen: let lifestyle rise slower than income. Twenty: money is a tool, not a scoreboard.""",
   "Checklist rules 16 to 20", "RULES 16 TO 20")
sc("""The action rules. Twenty one: check your credit reports. Twenty two: freeze your credit. Twenty three: insure against catastrophe.
Twenty four: name beneficiaries and have a will. Twenty five: always negotiate.""",
   "Checklist rules 21 to 25", "RULES 21 TO 25")
sc("""Twenty six: use tax advantaged accounts first. Twenty seven: review subscriptions twice a year. Twenty eight: build sinking funds. Twenty
nine: talk about money with your partner. And thirty: invest in yourself every year.""",
   "Checklist rules 26 to 30", "RULES 26 TO 30")

sc("""One last thought. Rules can sound restrictive, but these thirty do the opposite. They free you from having to make the same hard
decisions again and again. They protect you from scams, debt and panic. And they leave you with more money, more time and more choices.
That's what a good year with money really looks like. Here's to making 2027 that year, for you and the people you love.""",
   "Fireworks new year celebration", "HERE'S TO 2027")
sc("""And if you only remember three rules from today, remember these. Pay yourself first. Never leave the match on the table. And if it
sounds too good to be true, it is.""",
   "Three highlighted rules", "IF YOU REMEMBER THREE")

# ---------------- Close ----------------
ch("What to do next")
pr("""You don't need to follow all thirty at once. Pick three for January, three for February, and so on. By the end of 2027, you'll have
built a money system most people never do. And watch my final video in this series: the complete playbook from broke to one million
dollars. I'm Ryan Rover. See you in the next one.""")

save("video59", "30 Money Rules to Live By in 2027", [
    "Federal Reserve, Economic Well-Being of U.S. Households (SHED), $400 emergency question",
    "Federal Reserve, G.19 Consumer Credit (credit card interest rates)",
    "Federal Trade Commission, Consumer Sentinel Network data on fraud losses (2024)",
    "U.S. Bureau of Labor Statistics, Consumer Expenditure Survey (housing share)",
    "William P. Bengen, Determining Withdrawal Rates Using Historical Data (1994)",
    "Fidelity, retirement savings guidelines by age",
    "Ramit Sethi, I Will Teach You to Be Rich (conscious spending)",
    "Richard H. Thaler and Shlomo Benartzi, Save More Tomorrow (2004)",
    "Elizabeth Dunn and Michael Norton, Happy Money (2013)",
    "AnnualCreditReport.com and FTC guidance on free credit freezes",
    "C+R Research, subscription spending survey (2022)",
    "IRS, annual contribution limits for 401(k), IRA and HSA",
], "30 money rules for 2027: numbers, psychology, action")
