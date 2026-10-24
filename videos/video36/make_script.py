import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

body_hook = None  # set right before item() to start a Short at its first explained scene

def item(n, title, sub, card_text, scenes):
    """scenes: list of (text, query, caption) shown after the list card."""
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"LESSON {n}")
    global body_hook
    if body_hook:
        short(body_hook); body_hook = None
    for text, q, c in scenes:
        sc(text, q, c)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Here's something that surprises a lot of people. Some of the richest people in America can pay a
lower tax rate on their income than a nurse, a teacher or an electrician. And most of the time, it's completely legal. It's
not about secret offshore tricks. It's about how the tax code treats different kinds of money. Today I'll show you how it
works, and which of those same rules you can use yourself.""")
short("A billionaire can pay a lower tax rate than a nurse. Legally.")
card("""Here's the key idea. In the United States, money earned from working is generally taxed at higher rates than money
earned from owning investments held for more than a year. Top federal rates on wages reach thirty seven percent. Top rates on
long term capital gains are twenty percent, plus a three point eight percent surtax for high earners.""",
     {"type": "compare", "left": {"label": "Top rate on wages", "big": "37%", "sub": "plus payroll taxes"},
      "right": {"label": "Top rate, long-term gains", "big": "20%", "sub": "plus 3.8% surtax"},
      "note": "U.S. federal rates; state taxes vary"})
sc("""That single difference explains a lot. Most people's income comes from a paycheck, so most of their money is taxed at
ordinary income rates, plus payroll taxes. The very wealthy usually get most of their income from investments and businesses
they own, which are often taxed at lower rates, and sometimes not taxed at all until much later. Same country, same tax code,
very different results depending on what kind of money you have.""",
   "Paycheck next to stock certificate", "WORK MONEY VS OWNER MONEY")
sc("""We'll explore this from three angles. First, the numbers. The specific rules that let wealthy people pay lower rates.
Second, the psychology. How the wealthy think about taxes differently from most people. And third, the playbook. The legal
tax advantages ordinary people can use, starting this year. Important reminder. This is general education, not tax advice.
Tax laws change often, and your situation is unique, so check with a qualified tax professional before acting.""",
   "Three paths in a park", "THREE ANGLES")
pr("""Let's start with the numbers. And the first lesson is about the two kinds of income.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our numbers. Tax rates and account rules come from the IRS and the Social Security Administration. Research on the
taxes paid by the wealthiest Americans comes from reporting by ProPublica and from analysis by the White House Council of
Economic Advisers and the Office of Management and Budget. Warren Buffett's figures come from his 2011 New York Times op ed.
Rules and thresholds change every year, so always check the latest numbers.""",
   "Tax documents on desk", "OUR NUMBERS")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Seven rules in the tax code that work very differently for people who own assets.""")

item(1, "Two kinds of income", "earned vs invested",
"""Lesson number one. The tax code treats two kinds of income differently.""", [
("""Ordinary income includes wages, salaries, tips, interest and short term investment gains. It's taxed on a progressive
scale, with federal rates ranging from ten percent up to thirty seven percent for the highest earners. The more you earn, the
higher the rate on each additional dollar.""", "Tax bracket chart", "ORDINARY INCOME: 10% TO 37%"),
("""Long term capital gains, meaning profits on investments held for more than a year, and qualified dividends are taxed on a
separate, lower schedule. Federal rates are zero, fifteen or twenty percent, depending on your taxable income. High earners
may also owe a three point eight percent net investment income tax.""", "Stock certificate with tax rates", "LONG TERM GAINS: 0%, 15%, 20%"),
("""So imagine two people who each have one million dollars of income in a year. One earns it as salary. The other earns it
as long term capital gains from selling stock. The salary earner faces the top ordinary rate on much of it. The investor faces a
top rate of twenty percent plus the surtax. The investor's tax bill can be dramatically lower.""", "Two people comparing tax bills", "SAME INCOME, DIFFERENT TAX"),
("""Lawmakers have argued for decades about whether this is fair. Supporters say lower rates encourage investment and avoid
taxing money that was already taxed at the corporate level. Critics say it mostly benefits the wealthy. Either way, it's the law,
and understanding it helps you make better decisions with your own money.""", "Capitol building", "A LONG DEBATE"),
])

body_hook = "Billionaires can watch their fortunes grow for decades without paying tax on it."
item(2, "Unrealized gains aren't taxed", "no sale, no tax",
"""Lesson number two. Growth isn't taxed until you sell.""", [
("""In the U.S. tax system, you generally owe tax on an investment gain only when you sell, which is called realizing the gain.
If you buy a stock for ten thousand dollars and it grows to one hundred thousand, you owe nothing on that ninety thousand dollar
gain until you sell. On paper you're richer, but for tax purposes, nothing has happened yet.""", "Stock chart growing", "NO SALE, NO TAX"),
("""For the very wealthy, most of their fortune is often in stock of companies they founded or own. That stock can grow by
billions of dollars without any tax, as long as they don't sell. In 2021, ProPublica analyzed IRS data and reported that the
twenty five richest Americans paid federal income taxes equal to about three point four percent of their wealth growth from 2014
to 2018.""", "Investigative report pages", "ABOUT 3.4% OF WEALTH GROWTH"),
("""That figure is controversial, because it compares taxes to wealth growth, not to taxable income, and wealth growth isn't
income under current law. But it shows how much of the richest people's gains can stay untaxed for years. A separate 2021
White House analysis estimated the wealthiest four hundred families paid an average federal individual income tax rate of about
eight percent when unrealized gains were counted.""", "Economist reviewing data", "ABOUT 8% BY ONE ESTIMATE"),
("""The lesson for regular investors is simple. Holding investments for the long term, instead of constantly selling, lets
your money grow without being slowed down by yearly taxes. It's the same rule the wealthy use, and it's available to anyone with a
brokerage account.""", "Person holding long term", "YOU CAN USE THIS TOO"),
])

body_hook = "Why would a billionaire borrow money? Because loans aren't taxed."
item(3, "Borrowing instead of selling", "loans aren't income",
"""Lesson number three. Borrowing instead of selling.""", [
("""If the wealthy don't sell their assets, how do they pay for their lives? One strategy is borrowing. Banks are often willing
to lend large amounts to wealthy clients, using their stock or other assets as collateral. And under U.S. tax law, borrowed
money isn't income, so a loan isn't taxed.""", "Banker shaking hands", "LOANS AREN'T INCOME"),
("""This is sometimes called buy, borrow, die. Buy assets that grow. Borrow against them to fund your lifestyle, often at
relatively low interest rates. Never sell, so you never realize the gains. The assets keep growing, and the loans are repaid
later, often from the estate.""", "Three step diagram", "BUY, BORROW, DIE"),
("""This doesn't work for everyone, and it carries real risk. If asset values fall sharply, lenders can demand more collateral
or force sales. And interest rates matter. When borrowing costs rise, the strategy becomes more expensive. It works best for
people with enormous assets relative to their spending.""", "Falling chart with warning", "IT HAS REAL RISKS"),
("""For ordinary people, the takeaway isn't to borrow against your investments. It's to understand why the wealthy rarely sell
assets. They know every sale can trigger taxes, so they treat their best assets as things to keep, not things to cash out.""", "Person thinking at desk", "THE WEALTHY RARELY SELL"),
])

item(4, "The step up in basis", "gains that disappear",
"""Lesson number four. The step up in basis.""", [
("""Here's the final piece of buy, borrow, die. When someone dies, their heirs generally receive inherited assets with a new
cost basis equal to the value on the date of death. That's called a step up in basis. All of the gains built up during the
original owner's lifetime can effectively escape capital gains tax.""", "Family inheritance documents", "THE STEP UP"),
("""Here's an example. Someone buys stock for one hundred thousand dollars. Decades later, it's worth five million when they
die. Their heirs inherit it with a basis of five million. If they sell right away, they may owe little or no capital gains tax,
even though the stock grew by four point nine million dollars.""", "Stock certificate passing hands", "$4.9 MILLION GAIN, LITTLE TAX"),
("""Large estates may owe federal estate tax, but only above a very high exemption, which was more than thirteen million dollars
per person in recent years, and the amount is set by Congress and changes over time. Most families never pay federal estate tax
at all.""", "Estate planning meeting", "ESTATE TAX HAS A HIGH EXEMPTION"),
("""The step up applies to regular families too. A home or stock portfolio passed to children can also receive a step up. That's
why estate planning isn't just for the rich. A simple conversation with an estate attorney can save heirs a lot of money.""", "Family home", "IT APPLIES TO FAMILIES TOO"),
])

item(5, "Payroll taxes stop", "the wage cap",
"""Lesson number five. Payroll taxes hit workers harder.""", [
("""Most workers pay payroll taxes on top of income tax. The Social Security tax is six point two percent of wages, and
Medicare tax is one point four five percent. Your employer pays a matching amount. If you're self employed, you generally pay
both halves yourself.""", "Paycheck with deductions", "7.65% FROM EVERY PAYCHECK"),
("""But the Social Security portion only applies up to a yearly wage limit, which was about one hundred seventy six thousand
dollars in 2025 and usually rises each year. Wages above that limit aren't subject to the six point two percent Social Security
tax. So a person earning ten million dollars in salary pays that tax only on the first portion.""", "Cap on a bottle", "SOCIAL SECURITY TAX HAS A CAP"),
("""Investment income, like capital gains and dividends, isn't subject to payroll taxes at all, although high earners may owe
the separate three point eight percent net investment income tax. For someone whose income is mostly from investments, payroll
taxes are a small factor or none at all.""", "Investment statement", "INVESTMENT INCOME SKIPS PAYROLL TAX"),
("""That means a middle income worker can pay a combined federal rate, income plus payroll, that's higher than someone who earns
far more from investments. It's one of the main reasons people say the rich can pay lower rates than the middle class.""", "Two workers comparing", "WHY THE MIDDLE CLASS PAYS MORE"),
])

item(6, "Business owners' deductions", "taxed on profit, not revenue",
"""Lesson number six. Business owners are taxed on profit.""", [
("""An employee is generally taxed on their gross wages, before most expenses. A business owner is taxed on profit, after
legitimate business expenses. Equipment, office costs, business travel, software, and employees' salaries can all reduce taxable
profit when they're ordinary and necessary for the business.""", "Small business owner at desk", "TAXED ON PROFIT"),
("""Real estate investors have another powerful tool, depreciation. The tax code allows owners to deduct part of a rental
building's cost each year, even if the property is actually rising in value. Depreciation can reduce or even eliminate taxable
rental income on paper, although some of it may be recaptured when the property is sold.""", "Rental property", "DEPRECIATION"),
("""Some business owners also qualify for a deduction on qualified business income, which can reduce taxes on certain pass
through business profits. These rules are complex, with limits and conditions, which is why business owners often pay for
professional tax help.""", "Accountant reviewing documents", "COMPLEX BUT POWERFUL"),
("""The key word is legitimate. Deducting personal expenses as business expenses is illegal, and the IRS does audit. But a real
side business with real expenses can give ordinary people access to some of the same advantages.""", "Warning stamp on document", "LEGITIMATE EXPENSES ONLY"),
])

item(7, "Carried interest", "a special rule for fund managers",
"""Lesson number seven. Carried interest.""", [
("""Private equity and hedge fund managers often get paid partly through something called carried interest, a share of the
fund's profits. Under current law, if certain holding period requirements are met, that share can be taxed as long term capital
gains instead of ordinary income.""", "Fund manager in office", "CARRIED INTEREST"),
("""Critics argue that carried interest is really payment for work, so it should be taxed like wages. Supporters argue it's a
return on risk and investment, similar to an ownership stake. Lawmakers have proposed changing it many times, and in 2017 the
required holding period was extended to three years for many cases.""", "Debate illustration", "A CONTROVERSIAL RULE"),
("""Carried interest affects relatively few people, but it's a clear example of a broader pattern. When income can be labeled
as a return on investment instead of a return on labor, it's often taxed at a lower rate.""", "Label being changed", "LABELS MATTER"),
("""For ordinary people, the lesson isn't about carried interest itself. It's that owning assets, through retirement accounts,
index funds, real estate or a business, shifts more of your income into categories the tax code treats more favorably.""", "Person building portfolio", "OWNERSHIP SHIFTS THE TAX"),
])

pr("""That's angle one. Two kinds of income, untaxed growth, borrowing, the step up in basis, payroll tax limits, business
deductions and carried interest. Now angle two. The psychology.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
sc("""The wealthy don't just have different rules available. They think about taxes differently. Most people deal with taxes once
a year, in April, and try to get it over with. Wealthy people treat taxes as a year round part of every financial decision. Here
are seven ways their thinking differs.""",
   "Person thinking about money", "A DIFFERENT MINDSET")

item(8, "After tax thinking", "what you keep matters",
"""Lesson number eight. They think in after tax returns.""", [
("""Most people focus on how much they earn or what their investments return. Wealthy people focus on what they keep. A ten
percent return taxed at thirty seven percent leaves about six point three percent. A ten percent return taxed at fifteen percent
leaves eight and a half. The after tax number is the one that builds wealth.""", "Two numbers compared", "IT'S WHAT YOU KEEP"),
("""This changes decisions. Where to hold investments, when to sell, how to get paid, whether to take a raise as salary or
equity. Every choice gets evaluated through the question, what's the after tax result?""", "Decision tree on whiteboard", "EVERY DECISION, AFTER TAX"),
("""Regular people can adopt this same habit. When comparing two investments or two jobs, ask what you'll actually keep after
taxes, not just the headline number.""", "Person with calculator", "ASK WHAT YOU KEEP"),
("""Try this. Look at last year's tax return and calculate your effective tax rate, total tax divided by total income. Knowing
that number makes the cost of taxes real.""", "Tax return on table", "FIND YOUR EFFECTIVE RATE"),
])

item(9, "Year round planning", "not just April",
"""Lesson number nine. They plan all year, not just in April.""", [
("""By the time most people file their taxes, the year is over and most opportunities are gone. Retirement contributions, the
timing of sales, charitable gifts, business purchases, all of these usually need to happen before the year ends to count.""", "Calendar with December circled", "APRIL IS TOO LATE"),
("""Wealthy families often meet with tax advisors in the fall to plan moves before December thirty first. Should they sell some
investments at a loss to offset gains? Should they make a charitable gift this year or next? Should they convert some retirement
money to a Roth?""", "Advisor meeting in autumn", "FALL PLANNING MEETINGS"),
("""You don't need a team of advisors to do a simpler version. A short review in October or November can reveal moves that save
real money.""", "Person reviewing finances", "A SIMPLE FALL REVIEW"),
("""Try this. Put a tax planning reminder in your calendar for early November. Check your retirement contributions, your
investment gains and losses, and any big expenses coming up.""", "Calendar reminder", "NOVEMBER TAX CHECK"),
])

item(10, "Paying for good advice", "advice as an investment",
"""Lesson number ten. They see good tax advice as an investment.""", [
("""Many people try to save money by doing complicated taxes themselves. Wealthy people usually see a good tax professional as
an investment. If a five hundred dollar consultation saves two thousand dollars in taxes, that's a great return.""", "Tax professional at desk", "ADVICE AS AN INVESTMENT"),
("""For simple situations, a regular paycheck, standard deduction, basic retirement contributions, tax software or free filing
programs often work fine. But business income, rental property, stock compensation, big life changes or selling a large
investment can justify professional help.""", "Simple versus complex tax forms", "WHEN HELP IS WORTH IT"),
("""Look for credentials like CPA or enrolled agent, and ask how they charge. A good tax professional should save you more than
they cost and explain their recommendations clearly.""", "Credentials on wall", "CPA OR ENROLLED AGENT"),
("""Try this. If your taxes got more complicated this year, book a one time consultation before year end, not after.""", "Appointment booking", "BOOK BEFORE YEAR END"),
])

body_hook = "The rich don't just earn more. They earn a different kind of money."
item(11, "Owning, not just earning", "assets over wages",
"""Lesson number eleven. They focus on owning, not just earning.""", [
("""For most people, wealth building starts and ends with a paycheck. But wages are the most heavily taxed kind of income for
most people. Wealthy people focus on owning things that grow, like stocks, businesses and real estate, whose gains are often taxed
later and at lower rates.""", "House, stocks and business icons", "OWNERS VS EARNERS"),
("""That doesn't mean your paycheck isn't important. For most people, it's the engine that makes investing possible. The goal is
to turn part of each paycheck into assets, so over time more of your wealth comes from ownership.""", "Paycheck turning into stocks", "TURN WAGES INTO ASSETS"),
("""Over decades, someone who consistently invests can end up with a large portion of their net worth in assets whose growth has
never been taxed. That's the same structure the wealthy use, just at a smaller scale.""", "Growing portfolio chart", "THE SAME STRUCTURE"),
("""Try this. Look at your net worth and ask what percentage comes from assets that can grow, rather than cash or things that lose
value. Aim to increase that percentage every year.""", "Net worth breakdown", "INCREASE YOUR OWNERSHIP"),
])

pr("""Quick pause. If you're learning something about taxes that nobody taught you in school, please subscribe to Ryan Rover
Money. It's free, and it helps us keep making these. Now, lesson twelve.""")

item(12, "Patience pays", "holding beats flipping",
"""Lesson number twelve. They're patient sellers.""", [
("""Sell an investment after eleven months and the gain is generally taxed as ordinary income. Wait just over a year, and it may
qualify for lower long term capital gains rates. A few weeks of patience can make a real difference in what you keep.""", "Calendar showing twelve months", "WAIT OVER A YEAR"),
("""Wealthy investors also avoid unnecessary selling altogether. Every sale can create a tax bill that shrinks the amount left
to compound. Holding great assets for decades lets the full amount keep growing.""", "Old tree with deep roots", "HOLD FOR DECADES"),
("""Frequent traders face the opposite. Short term gains taxed at higher rates, plus trading costs, can seriously drag down
returns, even when their picks are good.""", "Frantic trader", "TRADING CREATES TAXES"),
("""Try this. Before selling any investment in a taxable account, check how long you've held it and what the tax would be.
Sometimes waiting a bit longer is the smartest move.""", "Brokerage holding period screen", "CHECK BEFORE YOU SELL"),
])

item(13, "Strategic giving", "generosity with a tax plan",
"""Lesson number thirteen. They give strategically.""", [
("""Many wealthy people donate appreciated stock instead of cash. If you've held a stock for more than a year and it has grown,
donating it directly to a qualified charity can let you avoid capital gains tax on the growth, and, if you itemize, deduct its fair
market value, within IRS limits.""", "Donation of stock certificate", "DONATE APPRECIATED STOCK"),
("""Some also use donor advised funds, which let them make a large charitable contribution in one year, take the deduction that
year if they itemize, and then recommend grants to charities over time.""", "Donor advised fund illustration", "DONOR ADVISED FUNDS"),
("""People seventy and a half or older can often give directly from an IRA to charity through a qualified charitable
distribution, which can count toward required minimum distributions without adding to taxable income. The rules have specific
limits, so check the current IRS guidance.""", "Retiree writing check to charity", "QUALIFIED CHARITABLE DISTRIBUTIONS"),
("""Try this. If you already give to charity, ask whether giving appreciated investments instead of cash would make your gift go
further.""", "Charity thank you letter", "GIVE SMARTER"),
])

item(14, "Taxes as the biggest bill", "the expense nobody budgets",
"""Lesson number fourteen. They see taxes as one of their biggest expenses.""", [
("""For many households, taxes, federal, state, local, payroll, property and sales, add up to one of the largest expenses in their
lives, sometimes larger than housing. Yet most people spend far more time comparing grocery prices than understanding their taxes.""", "Pie chart of household expenses", "ONE OF THE BIGGEST BILLS"),
("""Wealthy people manage taxes the way they manage any big expense. They look for legal ways to reduce it, plan ahead and track
it. Saving a few percent on a huge expense can matter more than cutting many small ones.""", "Person managing budget", "MANAGE IT LIKE AN EXPENSE"),
("""This isn't about avoiding your fair share. It's about using the rules Congress wrote, many of which were created specifically to
encourage saving for retirement, health care, education and giving.""", "Tax code book", "USE THE RULES AS WRITTEN"),
("""Try this. Add up every tax you paid last year, including payroll, property and state taxes. Seeing the full number is often a
wake up call.""", "Total on calculator", "ADD UP EVERY TAX"),
])

pr("""That's angle two. After tax thinking, year round planning, paying for good advice, owning instead of just earning, patience,
strategic giving and treating taxes as a big expense. Now angle three. The playbook.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
sc("""You don't need to be a billionaire to use tax advantages. Many of the most powerful ones were designed for ordinary workers.
Here are six legal moves that can lower your taxes and help your money grow faster. Remember, rules and limits change every year,
so check the current numbers with the IRS or a tax professional.""",
   "Toolbox on table", "SIX LEGAL MOVES")

item(15, "Use pre tax retirement accounts", "lower your taxable income",
"""Move number fifteen. Use pre tax retirement accounts.""", [
("""Contributions to a traditional four oh one k, and in many cases a traditional IRA, can reduce your taxable income this year.
If you're in the twenty two percent federal bracket, every one thousand dollars you contribute could cut your federal income tax by
about two hundred twenty dollars.""", "Retirement contribution form", "LOWER TAXABLE INCOME"),
("""The money then grows tax deferred. You don't pay tax on dividends or gains each year, so more stays invested and compounding.
You'll pay ordinary income tax when you withdraw it in retirement, ideally when your income and tax rate may be lower.""", "Growing savings jar", "TAX DEFERRED GROWTH"),
("""Add the employer match, and a pre tax four oh one k becomes one of the most powerful wealth building tools available to
regular workers.""", "Employer match illustration", "PLUS THE MATCH"),
("""Try this. Increase your four oh one k contribution by one or two percent. Because it comes out before taxes, your take home pay
falls by less than the amount you contribute.""", "Paycheck comparison", "RAISE IT 1 TO 2%"),
])

item(16, "Use a Roth for tax free growth", "pay now, never again",
"""Move number sixteen. Use Roth accounts for tax free growth.""", [
("""With a Roth IRA or Roth four oh one k, you contribute money you've already paid tax on. But qualified withdrawals in
retirement, including all the growth, are tax free. For a young investor, decades of growth could never be taxed.""", "Roth IRA document", "TAX FREE GROWTH"),
("""Roth accounts are especially attractive when your tax rate today is lower than you expect it to be later, which is common
early in a career. Many people use a mix of traditional and Roth accounts to keep flexibility in retirement.""", "Young professional", "GREAT EARLY IN A CAREER"),
("""Roth IRAs have income limits for direct contributions and yearly contribution limits, so check the current IRS numbers. Roth
four oh one k accounts, offered by many employers, don't have the same income limits.""", "IRS website", "CHECK THE LIMITS"),
("""Try this. If you're eligible and don't have one, open a Roth IRA and set up even a small automatic monthly contribution.""", "Opening account on phone", "OPEN A ROTH"),
])

body_hook = "There's one account with a triple tax break, and most people ignore it."
item(17, "The HSA triple advantage", "the most tax efficient account",
"""Move number seventeen. Use a health savings account if you can.""", [
("""If you have a qualifying high deductible health plan, you may be able to contribute to a health savings account, or HSA. HSAs
offer what's often called a triple tax advantage. Contributions can be tax deductible, growth is tax free, and withdrawals for
qualified medical expenses are tax free.""", "Health savings account card", "TRIPLE TAX ADVANTAGE"),
("""Many people use their HSA like a checking account for medical bills. But some HSA providers let you invest the balance. If you
can afford to pay current medical costs out of pocket and let the HSA grow, it can become a powerful long term account.""", "HSA investment options", "INVEST YOUR HSA"),
("""After age sixty five, you can generally withdraw HSA money for non medical expenses too, paying ordinary income tax, similar
to a traditional IRA. Medical withdrawals remain tax free at any age. Keep receipts, because qualified expenses can often be
reimbursed later.""", "Receipts in folder", "KEEP YOUR RECEIPTS"),
("""Try this. Check whether your health plan is HSA eligible during open enrollment, and if you have an HSA, see whether you can
invest the balance in low cost funds.""", "Open enrollment screen", "CHECK ELIGIBILITY"),
])

item(18, "Hold for the long term", "the 0% bracket",
"""Move number eighteen. Hold investments long term and know about the zero percent rate.""", [
("""Long term capital gains and qualified dividends can be taxed at zero percent for people with taxable income below certain
thresholds. Those thresholds are adjusted each year, and for many lower and middle income households, especially married couples,
they're higher than people expect.""", "Zero percent sign", "THE 0% RATE EXISTS"),
("""That means some retirees and modest earners can sell investments with gains and owe no federal tax on those gains, as long as
their taxable income stays within the bracket. Some people use low income years to realize gains on purpose.""", "Retiree reviewing statement", "USE LOW INCOME YEARS"),
("""And for everyone, holding investments for more than a year before selling generally qualifies gains for the lower long term
rates instead of ordinary income rates.""", "Calendar one year", "HOLD OVER A YEAR"),
("""Try this. Look up the current long term capital gains brackets on the IRS website and see which rate applies to your taxable
income.""", "IRS bracket table", "KNOW YOUR RATE"),
])

item(19, "Harvest your losses", "turn bad years into tax savings",
"""Move number nineteen. Use tax loss harvesting in taxable accounts.""", [
("""If an investment in a regular taxable account has fallen below what you paid, you can sell it to realize a loss. That loss can
offset capital gains, and if losses exceed gains, up to three thousand dollars a year can generally offset ordinary income. Extra
losses can be carried forward to future years.""", "Loss on stock chart", "LOSSES CAN OFFSET GAINS"),
("""Many investors then buy a similar, but not substantially identical, investment to stay invested in the market. That way they
keep their market exposure while capturing the tax benefit.""", "Swapping similar funds", "STAY INVESTED"),
("""Watch out for the wash sale rule. If you buy the same or a substantially identical investment within thirty days before or
after the sale, the loss can be disallowed for now. Many brokerages track this, but it's your responsibility.""", "Thirty day calendar", "THE WASH SALE RULE"),
("""Try this. Near the end of the year, review your taxable account for investments with losses, and consider whether harvesting
them makes sense for your situation.""", "Year end review", "YEAR END REVIEW"),
])

item(20, "Build ownership income", "a real side business",
"""Move number twenty. Build income from ownership.""", [
("""A real side business can open up legitimate deductions, like equipment, software, a portion of a home office if you qualify,
and business mileage. Self employed people can also open retirement accounts like a SEP IRA or a solo four oh one k, which can
allow larger contributions.""", "Person working on side business", "A REAL SIDE BUSINESS"),
("""Rental real estate is another path, with depreciation and expense deductions. But it comes with real work, risk and rules,
including limits on deducting rental losses for many taxpayers.""", "Small rental property", "REAL ESTATE HAS RULES"),
("""The goal isn't to start a business just for tax breaks. It's to build something that earns money, and then make sure you're
using every legitimate deduction and account available to owners.""", "Business growth chart", "EARN FIRST, THEN OPTIMIZE"),
("""Try this. If you have side income, track every legitimate business expense in a simple spreadsheet or app from day one, and
keep business and personal money in separate accounts.""", "Expense tracking app", "TRACK FROM DAY ONE"),
])

# ---------------- Story ----------------
ch("The billionaire and the office")
short("Warren Buffett said he paid a lower tax rate than his office staff.")
sc("""In 2011, Warren Buffett wrote an opinion piece in The New York Times called Stop Coddling the Super Rich. He said that in
2010, the federal income and payroll taxes he paid were about seventeen point four percent of his taxable income. That was a lower
percentage than any of the other twenty people in his office.""",
   "Newspaper opinion page", "BUFFETT'S 17.4%")
sc("""According to Buffett, the tax burdens of his office staff ranged from thirty three to forty one percent, and averaged thirty
six percent. The difference wasn't illegal tricks. Most of his income came from investments taxed at lower rates, while his staff
mostly earned wages taxed at ordinary rates plus payroll taxes.""",
   "Office staff at desks", "STAFF PAID 33% TO 41%")
sc("""Buffett argued that the rules should change. Whether you agree or not, his example shows the core lesson of this video.
The tax code rewards owning assets more than earning wages. You can't change the code, but you can change the mix of your income
over time by building ownership.""",
   "Person building portfolio", "THE CORE LESSON")

# ---------------- Example ----------------
ch("One worker, three changes")
pr("""Let's make this concrete with a simple example. Meet Sam, who earns seventy thousand dollars a year in salary and has
never thought much about taxes. Here are three legal changes Sam could make. The exact savings depend on Sam's full situation,
so treat these as rough illustrations.""")
sc("""Change one. Sam raises their four oh one k contribution from three percent to ten percent of salary. That's an extra four
thousand nine hundred dollars a year going in before taxes. In the twenty two percent federal bracket, that could lower Sam's
federal income tax by roughly one thousand dollars a year, while capturing more of the employer match and growing tax deferred.""",
   "Worker adjusting retirement contribution", "CHANGE 1: MORE PRE TAX SAVING")
sc("""Change two. Sam switches to an HSA eligible health plan at open enrollment, after checking that it makes sense for their
health needs, and contributes a few thousand dollars a year. Those contributions can also reduce taxable income, and if Sam
invests the balance, it can grow tax free for future medical costs.""",
   "Health plan comparison", "CHANGE 2: AN HSA")
sc("""Change three. Sam opens a Roth IRA and invests a few hundred dollars a month in a low cost index fund. No tax break today,
but decades of growth that may never be taxed. Now Sam has pre tax money, tax free money and health money, which gives
flexibility to manage taxes in retirement.""",
   "Roth IRA on laptop", "CHANGE 3: A ROTH IRA")
sc("""None of these changes required a higher income, a business or a team of advisors. Just a few forms and a little planning.
That's how ordinary workers start using the same basic idea the wealthy use. Keep more, invest more, and let ownership grow over
time.""",
   "Happy worker at home", "NO HIGHER INCOME REQUIRED")

# ---------------- By age ----------------
ch("Tax moves at every age")
sc("""In your twenties and early career, your tax rate is often lower than it will be later. That can make Roth contributions
especially attractive, because you pay tax now at a low rate and can withdraw growth tax free later. Always grab the employer
match first.""",
   "Young worker with laptop", "EARLY CAREER: THINK ROTH")
sc("""In your peak earning years, pre tax contributions often become more valuable, because each dollar saved avoids a higher tax
rate. This is also when HSAs, catch up contributions after fifty and careful year end planning can make the biggest difference.""",
   "Professional in office", "PEAK EARNING: THINK PRE TAX")
sc("""Near and in retirement, planning shifts to withdrawals. Which accounts to draw from first, whether to convert some money to
Roth in low income years, and how to manage required minimum distributions. A tax professional can be especially valuable here.""",
   "Retired couple with advisor", "RETIREMENT: PLAN WITHDRAWALS")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. Is this tax evasion? No. Tax avoidance means using legal rules to reduce taxes. Tax evasion means illegally
hiding income or lying to the IRS. Everything in this video is about legal strategies. Evasion can lead to penalties and even
criminal charges.""",
   "Legal versus illegal scale", "AVOIDANCE VS EVASION")
sc("""Question two. Do I need to be rich to use these strategies? No. Retirement accounts, Roth IRAs, HSAs, long term holding and
the zero percent capital gains rate are available to millions of ordinary people. Many are most valuable for middle income
households.""",
   "Ordinary family at home", "NOT JUST FOR THE RICH")
sc("""Question three. Should I choose traditional or Roth? It depends on whether you expect your tax rate to be higher now or in
retirement. Many people split contributions between both for flexibility. A tax professional can help you decide.""",
   "Two account options", "TRADITIONAL OR ROTH?")
sc("""Question four. What about state taxes? States vary widely. Some have no income tax, some tax capital gains like regular income
and some have special rules for retirement income. Check your state's rules, because they can change the math.""",
   "Map of states", "STATE TAXES VARY")

sc("""Question five. Will these rules change? Very possibly. Tax laws change regularly, and many proposals have targeted rules like
the step up in basis, carried interest and the taxation of unrealized gains for the very wealthy. That's why it's smart to focus on
durable habits, like saving in tax advantaged accounts and holding investments for the long term, and to review your plan every
year as the rules evolve.""",
   "Calendar with law book", "WILL THE RULES CHANGE?")

# ---------------- Mistakes ----------------
ch("Tax mistakes that cost regular people")
sc("""Mistake one. Skipping retirement accounts. Not using a four oh one k, IRA or HSA when you're eligible means paying more tax
than you need to, year after year, and losing decades of tax advantaged growth.""",
   "Unused retirement form", "SKIPPING TAX ADVANTAGED ACCOUNTS")
sc("""Mistake two. Selling too soon. Selling investments held one year or less can mean paying ordinary income rates on gains that
might have qualified for lower long term rates with a little patience.""",
   "Calendar with early sale", "SELLING TOO SOON")
sc("""Mistake three. Cashing out a retirement account early. Withdrawals before age fifty nine and a half can trigger income tax
plus a ten percent penalty in many cases, and the money loses all its future tax advantaged growth.""",
   "Early withdrawal penalty", "CASHING OUT EARLY")

sc("""Mistake four. Ignoring the tax on frequent trading in a taxable account. Every short term gain is taxed like a paycheck, and
every trade is a new tax decision. Many people who think they're beating the market discover they're behind once taxes and costs
are included. Buying and holding broad funds keeps taxes low and decisions simple.""",
   "Trader with tax bill", "FREQUENT TRADING TAXES")
sc("""Mistake five. Never checking beneficiaries and estate basics. Without updated beneficiaries and a simple will, families can
face delays, legal costs and taxes that were avoidable. A few hours of planning can protect the step up in basis and make sure
your money goes where you want.""",
   "Will and beneficiary forms", "IGNORING ESTATE BASICS")

# ---------------- Recap ----------------
ch("Recap")
sc("""Quick recap. Angle one, the numbers. Two kinds of income, untaxed growth, borrowing, the step up in basis, payroll tax
limits, business deductions and carried interest.""",
   "Checklist on clipboard", "THE NUMBERS: 1 TO 7")
sc("""Angle two, the psychology. After tax thinking, year round planning, good advice, ownership, patience, strategic giving and
treating taxes as a big expense.""",
   "Person thinking", "THE PSYCHOLOGY: 8 TO 14")
sc("""Angle three, the playbook. Pre tax accounts, Roth accounts, the HSA, long term holding, tax loss harvesting and ownership
income.""",
   "Notebook with plan", "THE PLAYBOOK: 15 TO 20")

# ---------------- Close ----------------
ch("What to do next")
pr("""The rich pay less tax mainly because of what kind of money they have. You can start shifting your own money in that direction,
one paycheck at a time. If you want my full step by step plan, it's in my playbook, linked in the description. Tell me in the
comments, which tax account are you going to use this year? I'm Ryan Rover. See you in the next one.""")

save("video36", "How the Rich Pay Less Tax Than You (Legally)", [
    "IRS: federal income tax brackets, long-term capital gains rates, net investment income tax",
    "IRS: retirement accounts (401k, IRA, Roth), HSAs, tax-loss harvesting and wash sale rule, qualified charitable distributions",
    "Social Security Administration: contribution and benefit base (2025 wage limit)",
    "ProPublica, The Secret IRS Files (June 2021): 3.4% 'true tax rate' for the 25 richest Americans, 2014-2018",
    "White House CEA and OMB (September 2021): estimated 8.2% average federal individual income tax rate for the 400 wealthiest families",
    "Warren Buffett, Stop Coddling the Super-Rich (The New York Times, August 14, 2011)",
    "Tax Cuts and Jobs Act of 2017: three-year holding period for carried interest",
    "IRS: estate tax basic exclusion amount and step-up in basis rules",
    "Not tax advice; rules and thresholds change yearly",
], "how the rich pay less tax legally, 20 lessons from 3 angles: numbers, psychology, playbook")
