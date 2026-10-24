import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

def item(n, title, sub, card_text, paras):
    """paras: list of (text, query, caption)"""
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"TRAP {n}")
    for t, q, c in paras:
        sc(t, q, c)
    sc(*OUT[n])

OUT = {
1: ("""Already in? If your house feels too big for your budget, you have options. Look into refinancing if rates
drop. Appeal your property tax assessment if it seems high. Shop your home insurance every year. Consider
renting a room or a basement unit if local rules allow it. And if none of that works, selling and
downsizing isn't failure. It's a reset that can free up years of progress.""",
    "Home for rent sign", "ALREADY HOUSE POOR?"),
2: ("""Already in? If you've been paying extra on a low rate mortgage while skipping your match, the fix is
easy. Redirect the extra payment to your retirement plan until you get the full match, and build your
emergency fund. The equity you already built isn't lost. You're just changing where the next dollar
goes.""",
    "Redirect arrow sign", "REDIRECT THE NEXT DOLLAR"),
3: ("""Already in? If most of your long term money is sitting in a low interest account, start by moving
your emergency fund to a high yield savings account, which pays more while staying safe. Then, for money
you won't need for many years, consider investing gradually, a set amount each month, so you don't have to
worry about picking the perfect day.""",
    "High yield savings app", "START GRADUALLY"),
4: ("""Already in? Look at the last three months of purchases and circle anything you bought mainly because it
was discounted. Add it up. That's your sale tax. Then unsubscribe from store emails and turn off shopping
app notifications. Fewer reminders mean fewer impulses. Many people cut spending noticeably just by reducing
what they see.""",
    "Unsubscribe email button", "YOUR SALE TAX"),
5: ("""Already in? Many extended warranties can be canceled for a prorated refund, especially in the first
weeks or months. Check your contract. And check your credit card benefits too. Some cards extend the
manufacturer's warranty for free on purchases made with the card. You might already have coverage you're
paying for twice.""",
    "Warranty contract paperwork", "CANCEL AND CHECK"),
6: ("""Already in? This year, when the refund arrives, give it a job the same day. For example, most of it to
high interest debt or your emergency fund, and a small slice for something fun. Next year, adjust your
withholding so the money arrives in your paycheck instead, and automate it straight to savings.""",
    "Bank transfer phone app", "GIVE IT A JOB"),
7: ("""Already in? If student loans feel heavy, look into the federal repayment options available for your
loans, including income driven plans, on the official student aid website. Avoid companies that charge
fees for help you can get for free. And remember, your earnings are the biggest lever. Investing in skills
that raise your income can shrink the loan faster than anything else.""",
    "Student loan website laptop", "KNOW YOUR OPTIONS"),
8: ("""Already in? Some loans allow a co signer to be released after the main borrower makes a certain number
of on time payments and qualifies alone. Ask the lender. The borrower could also refinance the loan in
their own name once their credit improves. Until then, monitor the account closely.""",
    "Bank loan officer meeting", "ASK ABOUT RELEASE"),
9: ("""Already in? If someone owes you money and it's hurting the relationship, have one calm conversation.
Agree on a small, realistic payment plan, or decide to forgive the loan and let it go. Either choice is
better than silent resentment. And next time, decide in advance whether it's a loan or a gift.""",
    "Two people shaking hands", "ONE CALM CONVERSATION"),
10: ("""Already in? Check whether your contract has a rescission period, a window to cancel shortly after
signing. Some resorts have official exit programs. Be very careful with companies that promise to get you
out for a big upfront fee. The FTC warns that some of them are scams. Start with the resort itself.""",
    "Resort reception desk", "START WITH THE RESORT"),
11: ("""Already in? Pick the one upgrade that adds the least joy for its cost, and undo just that one. Maybe it's
a subscription, a lease you can downgrade at renewal, or a membership you rarely use. You don't have to
undo everything. One reversed upgrade can free up hundreds a month.""",
    "Canceling membership card", "UNDO ONE UPGRADE"),
12: ("""Already in? Notice which situations trigger the spending. A certain group, a certain app, a certain
time of year. You don't need to drop your friends. Just suggest one cheaper plan a month, and let your
spending follow your values instead of the group's. Most real friends won't mind at all.""",
    "Friends picnic park", "SUGGEST ONE CHEAPER PLAN"),
13: ("""Already in? If a big share of your portfolio is in one company, you don't have to sell everything at
once. Some people sell a portion on a schedule, for example every quarter, and move it into diversified
funds. If the shares came from an employee plan, ask a tax professional how to reduce the tax bill.""",
    "Calendar quarterly plan", "DIVERSIFY ON A SCHEDULE"),
14: ("""Already in? If you took money out early, don't panic. Restart contributions as soon as possible, and
at least capture your employer match. If you took a 401k loan instead, keep making payments on time, and
learn the rules about what happens if you leave your job, because some loans can become due sooner.""",
    "Restart button", "RESTART CONTRIBUTIONS"),
15: ("""Already in? If you've been prioritizing college over retirement, it's not too late to rebalance. Increase
your retirement contributions, use catch up contributions if you're fifty or older, and have an honest
talk with your kids about cheaper school options, scholarships and aid. Many families find a plan that
works for both generations.""",
    "Family meeting kitchen table", "REBALANCE THE PLAN"),
}

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. The most dangerous money mistakes don't look like mistakes. Nobody brags about
gambling away their savings. But people proudly tell you about the big house they got approved for, the
degree they borrowed for, or the loan they co signed for their brother. Today, fifteen financial traps
disguised as good decisions.""")
short("This 'smart' money move is actually a trap")
card("""Fifteen traps. Each one looks responsible, generous or smart on the surface. Each one can quietly
cost you thousands, or even decades of progress.""",
     {"type": "stat", "label": "financial traps", "big": "15", "sub": "disguised as good decisions"})
sc("""Here's why these traps are so effective. A bad decision that looks bad is easy to avoid. Your friends
warn you, your gut warns you. But a bad decision that looks good gets praise. Your parents congratulate
you. The salesperson calls you smart. Society rewards it. So you walk in with a smile, and only discover
the cost years later, when it's hard to undo.""",
   "Gift box with ribbon", "IT LOOKS LIKE A GIFT")
sc("""We'll look at these traps from three angles. Angle one, the numbers: traps where the math is hidden
behind a good story. Angle two, the psychology: traps that use love, pride and identity against you. And
angle three, the playbook: the traps that hit your long term wealth, and a simple filter to catch any trap
before you step in it.""",
   "Three keys on table", "THREE ANGLES")
pr("""Number thirteen is one that thousands of people fell into at one famous company, and lost almost
everything. Let's start with the numbers.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Every number here comes from a named source. Student loan totals come from the Federal Reserve.
Retirement account rules come from the IRS. Co signing rules come from the Federal Trade Commission's
required cosigner notice. Examples use stated, simple math, like a seven percent average yearly return,
which is an illustration, not a promise. Your situation may be different, so treat this as education, not
financial advice.""",
   "Library research documents", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. Traps where the math hides behind a good story.""")

item(1, "The biggest house you're approved for", "approval is not affordability",
"""Trap number one. Buying the biggest house the bank will approve.""",
[("""Getting approved for a big mortgage feels like a vote of confidence. The bank looked at your numbers and
said yes, so it must be affordable, right? Not necessarily. Lenders approve based on rules about your
income and debts. They don't know about your plans to have kids, change careers, travel or retire early.
Approval tells you the maximum risk the lender will take. Not the right amount for your life.""",
  "Mortgage approval letter", "APPROVED IS NOT AFFORDABLE"),
 ("""A bigger house brings bigger everything. Higher property taxes, higher insurance, higher utilities,
more furniture, more repairs. Many people who max out their approval end up house poor. They own a
beautiful home, but they can't save, can't invest, and live one surprise away from stress. The house was
supposed to be a foundation. It became a ceiling.""",
  "Large empty house interior", "HOUSE POOR"),
 ("""A common guideline is to keep total housing costs around a quarter to under a third of your gross
income, including taxes and insurance, not just the mortgage. Try this: when you get your approval
amount, decide in advance to shop at seventy to eighty percent of it. The extra room in your budget will
be worth more than the extra room in your house.""",
  "House keys and calculator", "SHOP BELOW THE MAX")]),

item(2, "Paying off a cheap mortgage first", "while skipping the match",
"""Trap number two. Rushing to pay off a low rate mortgage while skipping retirement savings.""",
[("""Being debt free is a wonderful goal, and paying extra on a mortgage feels responsible. But the order
matters. If your mortgage rate is low, say three or four percent, and you're not getting your employer's
retirement match, you may be leaving a much better deal on the table. A match can be like an instant fifty
or one hundred percent return on the matched money.""",
  "Mortgage statement extra payment", "THE ORDER MATTERS"),
 ("""Money sent to a mortgage is also locked inside the house. If you lose your job, the bank doesn't care that
you paid extra last year. You still owe the next payment. Money in an emergency fund or investments stays
flexible. Some people end up with lots of home equity and very little cash, which is a fragile place to
be.""",
  "Locked door with key", "LOCKED IN THE HOUSE"),
 ("""This doesn't mean never pay extra. If your rate is high, or you're close to retirement and want lower
expenses, it can make a lot of sense. Try this: before paying extra on your mortgage, check three boxes.
Full employer match, solid emergency fund, and no high interest debt. Then decide.""",
  "Checklist three boxes", "THREE BOXES FIRST")]),

item(3, "Keeping everything in savings", "safe today, poorer tomorrow",
"""Trap number three. Keeping all your money in a savings account forever.""",
[("""Saving is great. Keeping everything in savings forever is a trap. A savings account protects you from
market drops, which is perfect for emergencies and short term goals. But over decades, inflation slowly
eats cash. If prices rise three percent a year and your savings earn one percent, you're losing about two
percent of buying power every year, while feeling completely safe.""",
  "Bank savings passbook", "SAFE AND SHRINKING"),
 ("""Picture fifty thousand dollars sitting in a low interest account for twenty years, losing about two
percent a year in real terms. Its buying power could fall to roughly thirty three thousand dollars in
today's money. The same money invested in a diversified portfolio has historically had a good chance of
growing much more over twenty years, although with ups and downs along the way.""",
  "Grocery receipt prices", "LOSING TO INFLATION"),
 ("""Try this: give every dollar a time horizon. Money you need within a few years stays safe and liquid. Money
for ten or twenty years from now can be invested for growth. The trap isn't saving. It's using one tool
for every job.""",
  "Tools on workbench", "THE RIGHT TOOL FOR THE JOB")]),

item(4, "Buying because it's on sale", "50% off is not 100% savings",
"""Trap number four. Buying something because it's on sale.""",
[("""Sales trigger something powerful in our brains. Fifty percent off feels like making money. But if you
didn't plan to buy it, you didn't save fifty percent. You spent fifty percent. Retailers know this well.
Limited time offers, countdown timers, and strikethrough prices are designed to make you act before you
think.""",
  "Sale sign fifty percent off", "YOU SPENT 50%"),
 ("""Many reference prices, the original price shown next to the sale price, are higher than what most
people ever paid. And seasonal sales create a sense of urgency every few weeks. Black Friday, then holiday
sales, then New Year sales, then spring sales. If you wait, there's almost always another one.""",
  "Black Friday crowd store", "THERE'S ALWAYS ANOTHER SALE"),
 ("""Try this: before any sale purchase, ask, would I buy this at full price? If the answer is no, you
probably don't really need it. Keep a wish list of things you actually want, and only buy from that list
when a real discount appears. That's how sales work for you, instead of you working for sales.""",
  "Wish list on phone", "BUY FROM THE LIST")]),

item(5, "Extended warranties", "insurance on small risks",
"""Trap number five. Extended warranties on everyday things.""",
[("""At the checkout, you're often offered protection. Two more years of coverage on your TV, laptop or
blender for a modest fee. It feels responsible, like insurance. But many products don't fail during the
extended period, and many failures are already covered by the manufacturer's warranty or by your credit
card's purchase protection.""",
  "Electronics store checkout", "PROTECTION PLAN?"),
 ("""For the store, these plans are often very profitable, because the price is set well above the expected
cost of repairs. That's not a scam. It's just math that's designed to favor the seller. Insurance makes
the most sense for big risks you couldn't afford to cover yourself, like your health, your home or your
income. Not a sixty dollar toaster.""",
  "Toaster kitchen counter", "INSURE BIG RISKS, NOT SMALL ONES"),
 ("""Try this: self insure. Skip most small warranties, and put what you would have paid into a savings
bucket for repairs and replacements. Over time, many people find the bucket covers their occasional
failures, with money left over.""",
  "Savings jar labeled repairs", "SELF INSURE")]),

item(6, "The big tax refund", "an interest free loan",
"""Trap number six. Celebrating a big tax refund.""",
[("""We covered this briefly in another video, but it's worth repeating, because it's so common. A big tax
refund feels like winning. In reality, it means you overpaid your taxes throughout the year, and the
government held your money without paying you any interest.""",
  "Tax refund check", "YOUR OWN MONEY"),
 ("""If you're carrying credit card debt while waiting for a refund, it can be even worse. You're paying
twenty percent on the card while lending the government money at zero percent. Adjusting your withholding
could give you that money every paycheck, which you could use to pay down the card months earlier.""",
  "Credit card and tax forms", "20% VS 0%"),
 ("""Try this: use the IRS withholding estimator on the official IRS website once a year, especially after a
big life change. If a big refund helps you save because you'd spend the money otherwise, that's a valid
choice. Just make it on purpose.""",
  "IRS website on laptop", "MAKE IT ON PURPOSE")]),
pr("""Six math traps. Now the ones that are harder to see, because they use your emotions.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
pr("""Angle two. Traps that use love, pride and identity against you.""")
short("Why co-signing a loan is one of the riskiest favors you can do")

item(7, "Any degree at any cost", "education is not always an investment",
"""Trap number seven. Borrowing whatever it takes for a degree.""",
[("""Education can be one of the best investments in your life. On average, people with college degrees earn
more over their careers. But on average hides a lot. The cost of the school, the field of study, whether
you finish, and how much you borrow all matter. According to the Federal Reserve, Americans owe more than
one point six trillion dollars in student loans.""",
  "University graduation ceremony", "$1.6 TRILLION+ IN STUDENT LOANS"),
 ("""The trap is treating any degree, at any price, as automatically good. Borrowing a large amount for a
program with modest expected earnings, or for an expensive school when a cheaper one offers a similar
path, can lead to years of large payments. And student loans are generally very hard to discharge in
bankruptcy.""",
  "Student studying with loan papers", "PRICE AND PAYOFF MATTER"),
 ("""A common rule of thumb is to avoid borrowing more in total than you expect to earn in your first year
after graduation. Try this: before choosing a school or program, look up typical earnings for that field
and compare the total cost of several schools. The government's College Scorecard website shows costs and
typical earnings by school and program.""",
  "Laptop college comparison", "COMPARE COST AND EARNINGS")]),

item(8, "Co-signing a loan", "you are the loan",
"""Trap number eight. Co signing a loan for someone you love.""",
[("""Co signing feels generous. Your child, sibling or friend can't qualify alone, and your signature makes the
difference. But co signing doesn't mean vouching for someone. It means you are legally responsible for the
whole debt. The Federal Trade Commission's cosigner notice warns that you may have to pay the full amount
if the borrower doesn't, plus late fees or collection costs.""",
  "Signing contract pen", "YOU ARE THE LOAN"),
 ("""And the loan shows up on your credit report. If the borrower pays late, your score can drop. The debt can
also make it harder for you to qualify for your own loans. Lenders asked for a co signer because they saw
risk. Your signature doesn't remove that risk. It moves it to you.""",
  "Credit report with late payment", "THEIR RISK BECOMES YOURS"),
 ("""Co signing can also strain relationships in a way money gifts don't. If the borrower struggles, you're
suddenly their creditor. Try this: only co sign if you could comfortably pay the entire debt yourself, and
would be okay doing so. If not, consider helping in a different way, like a smaller gift toward a down
payment.""",
  "Family argument at table", "MONEY AND RELATIONSHIPS")]),

item(9, "Lending to friends and family", "loans that become gifts",
"""Trap number nine. Lending money to friends and family.""",
[("""Helping people you love is a good thing. But personal loans between friends and family often go wrong in
predictable ways. There's no clear schedule, no consequences for late payment, and a lot of awkwardness.
The lender starts to resent the borrower. The borrower starts to avoid the lender. Both lose something
more valuable than money.""",
  "Two friends awkward conversation", "LOANS THAT HURT FRIENDSHIPS"),
 ("""A useful approach many people follow: only lend what you'd be willing to give away. If it comes back,
great. If it doesn't, you've decided in advance that the relationship matters more. This protects both your
finances and your peace of mind.""",
  "Hands giving money envelope", "ONLY LEND WHAT YOU'D GIVE"),
 ("""Try this: if you do lend, write down the amount and a simple repayment plan, and both sign it. It's not
about distrust. It's about clarity. Clear expectations protect relationships far better than vague
promises.""",
  "Simple written agreement", "WRITE IT DOWN")]),

item(10, "The timeshare", "a vacation you keep paying for",
"""Trap number ten. Buying a timeshare.""",
[("""Timeshare presentations are famously persuasive. Free gifts, a beautiful resort, a sales team trained to
make you feel like you're investing in a lifetime of vacations. But many timeshares come with yearly
maintenance fees that tend to rise over time, whether you use the week or not.""",
  "Resort pool tropical", "THE VACATION THAT SELLS ITSELF"),
 ("""And the resale market is often weak. Many owners find their timeshare is worth a small fraction of what
they paid, and some struggle to sell at all. A purchase that felt like an asset can turn into an ongoing
obligation. The Federal Trade Commission has also warned about scams targeting timeshare owners who are
trying to get out.""",
  "For sale sign ignored", "HARD TO SELL"),
 ("""Try this: if you love a resort, compare the full cost of a timeshare, including fees for years, with
simply booking the same kind of vacation each year. And never sign on the day of a presentation. A good
deal will still be a good deal tomorrow.""",
  "Couple on vacation beach", "COMPARE THE FULL COST")]),

item(11, "You deserve it", "the reward that resets you",
"""Trap number eleven. Rewarding yourself because you deserve it.""",
[("""After a promotion, a hard year or a big milestone, it's natural to celebrate. And you should. The trap is
when the reward is permanent. A bigger apartment, a luxury car payment, or an expensive new habit. These
aren't one time treats. They're new fixed costs that follow you for years.""",
  "Celebration champagne toast", "A TREAT OR A NEW COST?"),
 ("""Marketers love the phrase you deserve it, because it turns spending into a moral reward. But deserving
something and being able to afford it are two different questions. And a permanent upgrade can quietly
undo the progress that earned the reward in the first place.""",
  "Luxury shopping bags", "DESERVE VS AFFORD"),
 ("""Try this: celebrate with experiences or one time purchases, and set a budget for it. A great dinner, a
weekend trip, something you've wanted for a while. Then send the rest of the raise to your goals. You get
the joy without resetting your budget.""",
  "Friends dinner celebration", "CELEBRATE ONCE")]),

item(12, "Keeping up appearances", "the expensive kind of normal",
"""Trap number twelve. Spending to match the people around you.""",
[("""When your friends move to nicer neighborhoods, take bigger trips, or send their kids to expensive
activities, it's hard not to follow. It feels like normal life for your stage. But your friends might be
earning more, inheriting money, or borrowing heavily. You can't see their balance sheet. Only their
lifestyle.""",
  "Neighborhood big houses", "MATCHING THE NEIGHBORS"),
 ("""This trap is powerful because saying no can feel like falling behind, or like being left out. But
matching someone else's spending with your own income is one of the fastest routes to debt. Their normal
might be your financial emergency.""",
  "Person feeling left out", "THEIR NORMAL, YOUR EMERGENCY"),
 ("""Try this: find at least one friend who shares your money goals. Plan cheaper ways to spend time
together. Hiking, potlucks, game nights. You'll be surprised how many people are quietly relieved when
someone suggests it.""",
  "Friends hiking together", "FIND YOUR PEOPLE")]),

# ---------------- Mid ----------------
ch("A quick favor")
pr("""Quick pause. If you've spotted one of your own decisions on this list, you're not alone, and it's not too
late to fix. Subscribe to the channel if this is helping. It's free, and it helps me keep making these
videos. Now, the traps that hit your long term wealth.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
pr("""Angle three. The traps that hit your retirement and long term wealth, and a simple filter to catch any
trap before you step in.""")
short("Thousands of employees lost almost everything this way")

item(13, "Loading up on your company's stock", "loyalty isn't diversification",
"""Trap number thirteen. Putting too much money in your own company's stock.""",
[("""Investing in what you know sounds smart. You work there, you believe in the company, and maybe you even
get a discount on shares. But think about the risk. If the company struggles, you could lose your job and
your investments at the same time. Your paycheck and your savings both depend on the same company.""",
  "Corporate office building", "ONE COMPANY, TWO RISKS"),
 ("""The most famous example is Enron. When the energy company collapsed in two thousand one, many employees
had a large share of their retirement savings in Enron stock, by some reports around sixty percent of the
401k plan's assets. They lost their jobs and much of their retirement at the same time. Loyalty was
punished twice.""",
  "Empty office after layoffs", "THE ENRON LESSON"),
 ("""Many advisors suggest keeping any single stock, including your employer's, to a small share of your
portfolio, often ten percent or less. Try this: check how much of your total investments is in your
employer's stock. If it's a big share, consider gradually diversifying, and ask a tax professional about the
best way to do it.""",
  "Pie chart portfolio diversified", "KEEP IT SMALL")]),

item(14, "Raiding your 401(k) to pay off debt", "trading a big future for a small relief",
"""Trap number fourteen. Cashing out your 401k to pay off debt.""",
[("""When debt feels overwhelming, the retirement account can look like a rescue. The money is right there.
But early withdrawals usually come with a heavy cost. Before age fifty nine and a half, many withdrawals
are subject to income tax plus a ten percent additional tax, according to IRS rules, although there are
some exceptions.""",
  "Retirement account statement", "INCOME TAX PLUS 10%"),
 ("""That means withdrawing ten thousand dollars could leave you with much less after taxes and penalties,
sometimes six or seven thousand, depending on your tax bracket. And you lose all the future growth that
money would have produced. At seven percent a year, ten thousand dollars could grow to about seventy six
thousand over thirty years.""",
  "Money disappearing illustration", "$10,000 TODAY, $76,000 LATER"),
 ("""Changing jobs is another moment people cash out. Instead, many people roll the money into an IRA or a new
employer's plan, which can keep the tax advantages. Try this: before touching retirement money, look at
every other option first. Budget cuts, a debt payoff plan, a lower interest loan, a hardship program with
your creditors.""",
  "Person planning with laptop", "LAST RESORT, NOT FIRST")]),
card("""Ten thousand dollars left invested at a seven percent average yearly return for thirty years. That's
what an early withdrawal really costs.""",
     {"type": "growth", "start": 10000, "monthly": 0, "rate": 0.07, "years": 30})

item(15, "Paying for college before retirement", "you can borrow for one, not the other",
"""Trap number fifteen. Paying for your kids' college instead of saving for your own retirement.""",
[("""This one comes from love. Parents want to give their kids the best start, so they pour money into college
savings, or pay tuition directly, while their own retirement savings fall behind. It feels like the
right thing to do.""",
  "Parents with college student", "OUT OF LOVE"),
 ("""But there's a hard truth financial planners often repeat. Your kids can borrow for college, apply for
scholarships, work part time, or choose a less expensive school. There are no scholarships for retirement.
If you reach sixty five without enough saved, the people most likely to help you are, ironically, your
kids.""",
  "Elderly parent with adult child", "NO SCHOLARSHIPS FOR RETIREMENT"),
 ("""This doesn't mean don't help at all. It means put your own oxygen mask on first. Try this: make sure
you're on track for retirement, including your employer match, before contributing large amounts to
college savings. Then help as much as you comfortably can, and talk openly with your kids about what you
can and can't cover.""",
  "Airplane oxygen mask", "YOUR OXYGEN MASK FIRST")]),

# ---------------- Why we fall ----------------
ch("Why smart people fall for them")
pr("""Before the filter, let's talk about why smart people fall for these traps. It's not about intelligence.
It's about persuasion.""")
sc("""Psychologist Robert Cialdini spent years studying how people are persuaded, and described several
principles that show up in almost every sales situation. One is social proof. We tend to do what people
like us are doing. If everyone at work has a new car, or all your friends bought a house at the top of
their budget, it starts to feel normal and safe.""",
   "Crowd following leader", "SOCIAL PROOF")
sc("""Another is authority. When a banker approves you, or someone with a title recommends a product, we
tend to trust it. But a banker approving a loan isn't advising you. They're making a business decision
for the bank. And a salesperson with an impressive title still gets paid when you buy.""",
   "Banker in suit at desk", "AUTHORITY")
sc("""A third is scarcity. Limited time offers, only two left, this price ends today. When something seems
scarce, we want it more and think less. That's why timeshare presentations, car dealers and online stores
lean so heavily on deadlines. And a fourth is reciprocity. Accept a free gift, a free dinner or a free
vacation night, and you feel a quiet pressure to give something back. Like your signature.""",
   "Countdown timer on screen", "SCARCITY AND RECIPROCITY")
sc("""Knowing these principles doesn't make you immune, but it helps. When you notice social proof,
authority, scarcity or a free gift in a money decision, treat it like a yellow light. Slow down, and run
the filter.""",
   "Yellow traffic light", "A YELLOW LIGHT")

# ---------------- Filter ----------------
ch("The trap filter")
pr("""So how do you spot a trap before you step in it? Here's a simple filter. Seven questions you can ask about
any big money decision.""")
short("7 questions that catch any money trap before it's too late")
sc("""Question one. Who benefits if I say yes? Follow the money. If a salesperson, a lender or a store
benefits much more than you do, slow down. Question two. What's the total cost, not the monthly cost?
Monthly prices hide the size of commitments.""",
   "Person thinking with notebook", "QUESTIONS 1 AND 2")
sc("""Question three. Is this a one time cost, or a new permanent one? Permanent costs deserve much more
caution. Question four. What happens if things go wrong? If I lose my job, get sick or the market drops,
does this decision make it worse?""",
   "Umbrella in storm", "QUESTIONS 3 AND 4")
sc("""Question five. Would I make this choice if nobody could see it? This catches decisions driven by pride,
guilt or appearances. Question six. Can I easily undo it? Easy to reverse decisions are low risk. Hard to
reverse ones, like co signing or a timeshare, need extra thought.""",
   "Undo arrow symbol", "QUESTIONS 5 AND 6")
sc("""And question seven. Will I feel the same way in thirty days? Big decisions made under pressure,
excitement or emotion often look different a month later. If it's a good decision, it will still be good in
thirty days. If someone says the offer expires today, that's usually the clearest warning sign of all.""",
   "Calendar thirty days", "QUESTION 7: 30 DAYS")
card("""Who benefits? Total cost? Permanent? What if it goes wrong? Would I do it unseen? Can I undo it? Will I
feel the same in thirty days?""",
     {"type": "stat", "label": "the trap filter", "big": "7 QUESTIONS", "size": 180, "sub": "ask them before any big money decision"})

# ---------------- Stories ----------------
ch("Three traps in real life")
sc("""Let's see how these traps play out with three examples. First, Nicole and James. They were approved for
a six hundred thousand dollar home, and bought right at the limit. Their friends congratulated them. Two
years later, a baby arrived, childcare costs jumped, and property taxes rose. They stopped contributing to
retirement and started using credit cards for unexpected bills.""",
   "Couple in large new house", "NICOLE AND JAMES")
sc("""Their fix wasn't dramatic. They refinanced when they could, rented out the basement for a few years,
and rebuilt their emergency fund. But they lost several years of retirement contributions. Looking back,
they say a house at eighty percent of their approval would have given them the same happiness, with
none of the stress.""",
   "Basement apartment rental", "THE QUIET FIX")
sc("""Second, Robert. His younger brother needed a car loan and couldn't qualify, so Robert co signed.
Eighteen months later, his brother lost his job and stopped paying. The lender came to Robert. He paid
the remaining balance to protect his credit, but the relationship with his brother was strained for years.
Robert says he'd have rather given his brother a few thousand dollars toward a cheaper car.""",
   "Brothers serious conversation", "ROBERT: THE CO SIGNER")
sc("""And third, Diane. She worked at a growing company for fifteen years and kept most of her retirement in
company stock, because the price kept going up. When the industry changed, the stock fell sharply, and
layoffs followed. She kept her job, but her retirement savings shrank dramatically. She now keeps no more
than a small share in any single company. Diversification isn't exciting. It's protection.""",
   "Woman looking at falling stock chart", "DIANE: ONE BASKET")
sc("""Notice that none of these people were reckless. Each decision looked responsible, generous or loyal at
the time. That's what makes these traps so hard to see. And that's why a simple filter, asked every time,
is more powerful than willpower or luck.""",
   "Road with hidden potholes", "THEY LOOKED RESPONSIBLE")

# ---------------- FAQ ----------------
ch("Questions people ask")
pr("""Let me answer a few questions people ask about these traps.""")
sc("""Question one. Is buying a home a trap? No. Buying a home you can comfortably afford, with an emergency
fund left over, can be a great decision. The trap is buying at the absolute limit of your approval, with no
margin. The house is fine. The stretch is the problem.""",
   "Happy family new home", "IS BUYING A TRAP?")
sc("""Question two. What if I've already co signed? Stay informed. Ask the borrower for access to the account,
or regular updates. Set up alerts if you can. If they start to struggle, act early. Talk to them and the
lender before late payments pile up. And avoid co signing again unless you'd be comfortable paying the
whole debt.""",
   "Phone with account alerts", "ALREADY CO SIGNED?")
sc("""Question three. Is life insurance a trap? Term life insurance can be a smart, affordable way to protect
people who depend on your income. Permanent policies, like whole life, are more complex and much more
expensive, and they suit some situations, like certain estate planning needs. The trap is buying a
complex policy mainly as an investment without understanding the costs. Ask how the agent is paid, and
compare.""",
   "Insurance policy documents", "LIFE INSURANCE?")
sc("""Question four. How do I say no to family without hurting them? Be honest and kind. Something like, I
love you and I want to help, but I'm not able to lend money or co sign right now. Then, if you can, offer
another kind of help, like time, advice, or a small gift. A clear no often protects the relationship
better than a reluctant yes.""",
   "Family hug", "SAYING NO WITH LOVE")
sc("""And question five. What's the most common trap of all? Probably the permanent upgrade after a raise. It
looks completely reasonable, it's socially approved, and it quietly locks in higher spending for years.
The fix is to decide where your next raise goes before you get it.""",
   "Pay raise letter", "THE MOST COMMON TRAP")

sc("""Question six. How do I undo a trap without feeling ashamed? Remember that every trap on this list was
designed, or socially approved, to look like a good decision. Falling for one doesn't mean you're bad with
money. It means you're human. The skill isn't never making mistakes. It's noticing them early, fixing
the next decision, and not letting pride keep you stuck in the old one.""",
   "Person walking forward confident", "NO SHAME, JUST NEXT STEPS")
sc("""And question seven. Which trap should I fix first? Start with the one that costs you the most every
month. For many people, that's housing or a car. For others, it's high interest debt, or a missing employer
match. Fix the biggest monthly leak first, then the next one. Small fixes, stacked over a year, add up
faster than you'd expect.""",
   "Water leak bucket", "FIX THE BIGGEST LEAK FIRST")

# ---------------- Recap ----------------
ch("Recap: all 15 traps")
short("15 financial traps disguised as good decisions")
sc("""Quick recap. The math traps: the biggest house you're approved for, paying off a cheap mortgage before
your match, keeping everything in savings, buying because it's on sale, extended warranties on small
things, and the big tax refund.""",
   "Checklist clipboard", "THE MATH TRAPS")
sc("""The emotional traps: any degree at any cost, co signing, lending to family, the timeshare, you deserve
it upgrades, and keeping up appearances.""",
   "Heart and money illustration", "THE EMOTIONAL TRAPS")
sc("""And the long term traps: loading up on company stock, raiding your 401k, and paying for college before
retirement. Plus the filter: who benefits, total cost, permanent or not, what if it goes wrong, would I do
it unseen, can I undo it, and will I feel the same in thirty days.""",
   "Long road to horizon", "THE LONG TERM TRAPS")

# ---------------- Close ----------------
ch("What to do next")
pr("""If you want the full plan for avoiding traps and building wealth step by step, it's in my playbook. The
link is in the description. And if you liked this one, watch my video on twenty money myths that keep you
poor. They're close cousins of these traps. I'm Ryan Rover. See you in the next one.""")

save("video45", "15 Financial Traps Disguised as Good Decisions", [
    "Federal Reserve, Consumer Credit G.19 (student loans outstanding above $1.6 trillion)",
    "IRS, retirement plan early distributions (10% additional tax before 59 1/2, with exceptions); IRS Tax Withholding Estimator",
    "Federal Trade Commission, Cosigning a Loan (required cosigner notice); FTC guidance on timeshare resale scams",
    "U.S. Department of Education, College Scorecard",
    "Enron collapse (2001): employee 401(k) concentration in company stock, as widely reported",
    "Growth and inflation figures: stated illustrative math",
], "15 financial traps: numbers, psychology, playbook")
