import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

body_hook = None  # set right before item() to start a Short at its first explained scene

def item(n, title, sub, card_text, body, example, fix, q1, c1, q2, c2, q3, c3):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"DIFFERENCE {n}")
    global body_hook
    if body_hook:
        short(body_hook); body_hook = None
    sc(body, q1, c1)
    sc(example, q2, c2)
    sc(fix, q3, c3)
    if n in EXTRA:
        sc(EXTRA[n][0], EXTRA[n][1], EXTRA[n][2])

EXTRA = {
 2: ("""Endowments at some of the oldest American universities show what a very long horizon can do. Funds that spend only a
small share each year, and reinvest the rest, have grown over generations into some of the largest pools of money in the
world. The principle works at any scale. Patience plus a modest spending rate lets money outlive the people who saved it.""",
     "Old university campus", "THE ENDOWMENT MODEL"),
 3: ("""Think of a founder whose entire net worth is in one company's stock. If that company thrives, they become even
richer. If it collapses, as many once famous companies have, their fortune can collapse with it. Old money families have
usually lived through enough cycles to know that no single company, industry or country stays on top forever.""",
     "Abandoned old factory", "NOTHING STAYS ON TOP FOREVER"),
 5: ("""For regular families, the same mindset shows up in simple choices. Contributing to a four oh one k before taxes,
using a Roth IRA for tax free growth, holding investments more than a year so gains may qualify for lower long term
capital gains rates, and keeping receipts and records. None of it is glamorous, but over a lifetime it can add up to a
large amount of money kept instead of paid.""", "Tax forms organized in folder", "BORING BUT POWERFUL"),
 7: ("""It's also about protecting heirs from themselves. A twenty year old who suddenly inherits millions with no
guidance is at real risk. Structures that release money gradually, or that require a trustee's approval for big
withdrawals, can give young heirs time to grow up before they're handed the keys to everything.""",
     "Young adult receiving keys", "PROTECTING HEIRS FROM THEMSELVES"),
 1: ("""Here's a simple way to picture it. Imagine two people who each have two million dollars. One spends it like
income, buying a bigger house and better cars. The other invests it and spends only a small share of what it earns each
year. Twenty years later, the first person may have very little left, while the second person may have more than they
started with, and has been living on it the whole time.""", "Two paths diverging in woods", "SAME MONEY, DIFFERENT FUTURE"),
 4: ("""History is full of examples. Many professional athletes earn more in a few years than most people earn in a
lifetime, yet a widely cited Sports Illustrated report in two thousand nine claimed that a large share of former NFL and
NBA players faced financial stress within a few years of retiring. Whatever the exact share, the pattern is familiar.
Big income, big lifestyle, big debts, and then the income stops.""", "Empty sports stadium", "WHEN THE INCOME STOPS"),
 6: ("""Think about lottery winners. Many receive a fortune overnight, with no experience managing large sums, and with
friends and family suddenly asking for help. Researchers studying lottery winners in Florida found that larger winners
were less likely to file for bankruptcy in the short term, but that over time the protective effect faded considerably.
Sudden money without a spending discipline is fragile.""", "Lottery balls drawing", "SUDDEN MONEY IS FRAGILE"),
 8: ("""There's a famous phrase sometimes used to describe this attitude. Money talks, wealth whispers. Whether or not
anyone can prove who said it first, it captures the idea well. Those who have had wealth for a long time often see no
reason to announce it. For them, the real luxury is privacy, time and freedom, none of which come with a logo.""",
     "Quiet country estate", "MONEY TALKS, WEALTH WHISPERS"),
 9: ("""You can see this in the idea of heirloom quality. A good wool coat, a solid wood table, a leather bag that ages
well. These items are often bought once and repaired rather than replaced. Over decades, the cost per year can be
lower than buying cheaper versions again and again. It's frugality and elegance at the same time.""",
     "Heirloom watch and leather goods", "HEIRLOOM QUALITY"),
 10: ("""Psychologists have long observed that people often use possessions to signal identity and status, especially
when they feel insecure about their position. That's not a moral failing. It's very human. But knowing it gives you a
choice. Next time you feel the urge to buy something to show others, ask whether you'd still want it if nobody would
ever see it.""", "Person looking in shop window", "WOULD YOU BUY IT IF NOBODY SAW?"),
 11: ("""Old money investors often talk about having time on their side. They don't need to make a fortune this year,
because they already have one. That frees them to wait for good opportunities, and to say no to most pitches. For
regular investors, the same mindset helps. You don't need to get rich this year. You need to stay invested for the
next thirty.""", "Old clock on wall", "TIME ON THEIR SIDE"),
 12: ("""For ordinary people, this can be as simple as finding one trusted tax preparer, one good insurance agent, and
perhaps one fee only financial planner, and sticking with them for years. Over time, they learn your situation, and you
learn whether you can trust their advice. That kind of relationship is worth more than any single tip.""",
     "Long term advisor relationship", "ONE TRUSTED TEAM"),
 13: ("""This is also why old money families often encourage meaningful work, even for heirs who don't need the
income. Work gives purpose, identity and skills. Heirs who find meaningful roles, in a family business, a career or
philanthropy, are often far more likely to preserve wealth than those who drift without direction.""",
     "Young professional at work", "PURPOSE BEYOND MONEY"),
 14: ("""Many self made fortunes were built by people who put almost everything on one idea. But once the fortune exists,
the smartest builders often change strategy and start acting like keepers. They sell part of their concentrated
position, diversify, and protect the downside. Building and keeping really are two different skills.""",
     "Founder ringing stock exchange bell", "BUILDING AND KEEPING ARE DIFFERENT"),
 15: ("""A family meeting doesn't need to be formal. It can be a dinner where you share one goal, one decision and one
lesson. Older kids can learn how the household budget works. Adult children can learn where important documents are
kept. Those simple conversations prevent confusion and conflict later, which is exactly where many family fortunes
break down.""", "Family dinner conversation", "IT CAN BE A DINNER"),
 16: ("""Some families use what are sometimes called incentive trusts, which release money when heirs reach certain
milestones, like finishing school or matching their own earned income. Whether or not you ever set up a trust, the
principle is valuable. Money works best when it supports effort and responsibility, rather than replacing them.""",
     "Graduation ceremony", "MONEY THAT SUPPORTS EFFORT"),
 17: ("""Andrew Carnegie, one of the richest Americans of his era, famously argued that the man who dies rich dies
disgraced, and gave away most of his fortune to libraries, universities and other causes. More recently, the Giving
Pledge, started by Warren Buffett and Bill and Melinda French Gates, invites billionaires to commit to giving away the
majority of their wealth.""", "Carnegie library building", "ANDREW CARNEGIE"),
 18: ("""The research by Barber and Odean looked at tens of thousands of household brokerage accounts in the nineteen
nineties. The households that traded the most earned noticeably lower returns than the market, largely because of
trading costs and poorly timed decisions. Doing less was often the winning strategy.""",
     "Stock trading screens", "DOING LESS WINS"),
 19: ("""Think of the immigrant shop owner, the first generation college graduate who starts a company, or the
tradesperson who builds a contracting business from a single truck. Their drive, frugality and appetite for work are
exactly what old money families try to keep alive in later generations, often without success.""",
     "Small business owner smiling", "FIRST GENERATION DRIVE"),
 20: ("""Picture someone who builds a small business with long hours and smart risks, then pays themselves a modest
salary, invests the profits in diversified index funds, writes a will, teaches their kids to work, and talks openly with
their family about money. That person is building the first chapter of an old money story.""",
     "Family business storefront", "THE FIRST CHAPTER"),
}

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. There are two kinds of rich in America. There's old money, families who have been
wealthy for generations, quietly, often without anyone noticing. And there's new money, people who made their
fortune themselves, often fast, and often very visibly. They both have money. But they tend to think about it,
spend it and protect it very differently. Today, twenty differences between old money and new money, and the
lessons you can steal from both, whatever your bank balance looks like.""")
short("Most family fortunes vanish by the third generation. Here's why.")
card("""Here's a number you'll hear a lot in wealth management. A widely cited study by the Williams Group found
that about seventy percent of wealthy families lose their wealth by the second generation, and about ninety percent
by the third.""",
     {"type": "compare", "left": {"label": "By generation 2", "big": "~70%", "sub": "of family wealth lost"},
      "right": {"label": "By generation 3", "big": "~90%", "sub": "of family wealth lost"},
      "note": "Williams Group research, widely cited and debated"})
sc("""That research is debated, and different studies measure it differently. But the pattern is so common it has
an old saying. Shirtsleeves to shirtsleeves in three generations. The first generation builds the fortune in
work shirts. The second enjoys it. The third is back in shirtsleeves. Old money families are, by definition, the
ones who broke that pattern. That's why their habits are worth studying.""",
   "Old family portrait photographs", "SHIRTSLEEVES TO SHIRTSLEEVES")
sc("""We'll compare old and new money from three angles. First, the numbers. How each group earns, invests,
borrows and handles taxes. Second, the psychology. How they think about status, risk, time and identity. And third,
the playbook. The practical systems old money families use to keep wealth for generations, and the strengths new
money brings that old money often lacks. I want to be clear. These are broad patterns, not rules. Plenty of
individuals break the stereotypes in both directions.""",
   "Old mansion and modern glass house", "THREE ANGLES")
pr("""Let's start with the numbers. And the first difference is about where the money actually comes from.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our sources. Family wealth transfer research comes from the Williams Group, published in the book Preparing
Heirs by Roy Williams and Vic Preisser. Billionaire data comes from UBS's Billionaire Ambitions reports. Millionaire
profiles come from Ramsey Solutions' National Study of Millionaires and Thomas Stanley's research. The Vanderbilt
story comes from the book Fortune's Children by Arthur T. Vanderbilt the second. Tax rules come from the IRS. This is
education, not financial advice, and not tax or legal advice.""",
   "Historic library books", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Seven financial differences between old money and new money.""")

item(1, "Assets vs income", "money that works vs money that's earned",
"""Difference number one. Old money lives on assets. New money often lives on income.""",
"""Many new money fortunes come from a high income or a single big event, like selling a company, a big contract or
a successful career in sports or entertainment. That money arrives as cash, and it's easy to spend. Old money
families, by contrast, typically live on what their assets produce. Rents, dividends, interest and business profits.
The core assets stay untouched, and only part of the income is spent.""",
"""That's a crucial difference. If you spend from income, a job loss or a bad year can end everything. If you
spend only part of what your assets produce, the wealth can keep growing even while you live on it. Many old money
families follow a version of this rule for decades. Spend some of the returns, never the principal.""",
"""The lesson for anyone. Start building assets that produce income, like index funds, a retirement account, a
rental property or a small business. Over time, aim for a day when part of your living costs are covered by what
your assets earn, not just by what you earn.""",
"Rental properties street", "ASSETS VS INCOME",
"Dividend statement document", "SPEND RETURNS, NOT PRINCIPAL",
"Small business storefront", "BUILD INCOME ASSETS")

item(2, "Generations vs years", "the time horizon",
"""Difference number two. Old money thinks in generations. New money often thinks in years.""",
"""When you've just made your fortune, the natural questions are about the next few years. What should I buy? How do
I enjoy this? Old money families often frame decisions around decades and generations. Will this still matter for our
grandchildren? That longer view changes everything, from how they invest to how they spend.""",
"""A long time horizon makes compounding work at full strength. Money invested for fifty years, or for multiple
lifetimes, can grow enormously, even at modest returns. It also makes families more patient with market drops,
because a bad year is a tiny part of a hundred year plan.""",
"""The lesson for anyone. Stretch your time horizon. When you invest, think in decades, not months. Ask yourself
what decision your seventy year old self would thank you for.""",
"Family tree illustration", "GENERATIONS VS YEARS",
"Old oak tree", "A HUNDRED YEAR PLAN",
"Grandparent with grandchild", "THINK IN DECADES")

item(3, "Diversified vs concentrated", "spreading vs betting",
"""Difference number three. Old money spreads its bets. New money is often concentrated.""",
"""New fortunes are frequently built by concentration. A founder owns a huge stake in one company. An athlete has
one skill that pays enormously. Concentration is how many fortunes are made. But it's also how many are lost, when a
single company or career declines.""",
"""Old money families tend to diversify across many assets. Stocks, bonds, real estate, private businesses and
more. They accept that diversification may mean they won't get the very highest returns, in exchange for protecting
the wealth from any single disaster. Their goal is not to get rich. It's to stay rich. As one saying in wealth management puts it, concentration builds
wealth, and diversification protects it.""",
"""The lesson for anyone. Concentration can build wealth, for example in your own career or business. But once you
have savings, spread them out. Broad low cost index funds are a simple way for ordinary investors to own small pieces
of many companies.""",
"Single tall building alone", "CONCENTRATED",
"Diversified portfolio pie chart", "SPREAD THE BETS",
"Index fund growth chart", "STAY RICH")

body_hook = "The rich use debt very differently than everyone else."
item(4, "Debt as a tool vs debt as a lifestyle", "borrowing for assets",
"""Difference number four. How they use debt.""",
"""Some new money spends on visible things with borrowed money. Luxury cars on loans, huge mortgages on show homes,
big credit lines. When income drops, that debt becomes dangerous. Many famous athletes and entertainers who went broke
had large debts tied to their lifestyle.""",
"""Old money families, when they borrow, tend to borrow against assets for specific purposes, often at low rates,
and rarely for consumption. Some wealthy families borrow against their investment portfolios instead of selling,
which can have tax advantages. But that strategy carries real risks and only makes sense with large, diversified
assets and careful planning.""",
"""The lesson for anyone. Avoid borrowing for things that lose value. If you do borrow, borrow for things that can
grow or produce income, keep the debt manageable, and know exactly what it costs.""",
"Luxury cars in driveway", "DEBT FOR LIFESTYLE",
"Bank loan meeting", "DEBT AS A TOOL",
"Calculator and loan documents", "BORROW FOR ASSETS")

item(5, "Tax planning vs tax surprises", "the boring advantage",
"""Difference number five. Old money plans for taxes years ahead.""",
"""Many people with new money get a painful surprise at tax time, especially after selling a company or receiving a
large payout. Old money families typically work with tax professionals and plan years ahead, using legal strategies
like retirement accounts, charitable giving, trusts and careful timing of sales.""",
"""One well known rule is the step up in basis. Under current US tax law, when someone inherits certain assets like
stocks, the cost basis is generally reset to the value at the time of death. That can greatly reduce capital gains
taxes for heirs. Laws change, and details matter, so families work with professionals on this.""",
"""The lesson for anyone. You don't need a family office to plan for taxes. Use tax advantaged retirement accounts,
understand how long you hold investments before selling, and keep good records. A little planning can save a lot.""",
"Tax documents and calculator", "PLAN AHEAD",
"Financial advisor meeting", "LEGAL STRATEGIES",
"Retirement account form", "USE TAX ADVANTAGED ACCOUNTS")

item(6, "Spending rate", "living below the returns",
"""Difference number six. How much they spend.""",
"""New money can spend at a pace that outruns even a large fortune. Big houses, staff, cars, travel and gifts for
friends and family. The fortune feels endless, until it isn't. Stories of lottery winners and athletes who went broke
are common because big sudden wealth often comes with big sudden spending.""",
"""Many old money families follow a spending discipline. Some foundations and endowments, for example, aim to spend
around four to five percent of their assets each year, so the principal can keep up with inflation over time. Families
that last often follow something similar.""",
"""The lesson for anyone. Know your spending rate. What share of your income do you spend? What share of your
investments would you need to withdraw to live? Keeping that number sustainable is how wealth survives.""",
"Luxury shopping spree", "SPENDING TOO FAST",
"University endowment building", "A SPENDING DISCIPLINE",
"Notebook with spending rate", "KNOW YOUR RATE")

item(7, "Protection vs exposure", "trusts, insurance and structure",
"""Difference number seven. How they protect wealth.""",
"""Old money families often use legal structures, like trusts, family partnerships and insurance, to protect wealth
from lawsuits, divorce, poor decisions and taxes. These structures can also control how heirs receive money, for
example in stages rather than all at once.""",
"""New money is often more exposed. Assets may sit in one person's name, without a will or estate plan. Surveys have
found that many Americans, including many with significant assets, don't have a will. That leaves families vulnerable
to court processes and conflicts.""",
"""The lesson for anyone. At minimum, have a will, name beneficiaries on every account, and carry enough insurance,
including liability coverage. If you have significant assets or young children, talk to an estate planning attorney.""",
"Trust documents legal", "PROTECTING WEALTH",
"Courthouse building", "EXPOSED WITHOUT A PLAN",
"Will and beneficiary forms", "THE BASICS FOR EVERYONE")

ch("The Vanderbilt warning")
short("The richest family in America lost almost everything. Here's how.")
sc("""Here's what happens when new money never learns these lessons. Cornelius Vanderbilt built one of the largest
fortunes in American history in the eighteen hundreds, through shipping and railroads. When he died in eighteen seventy
seven, he was among the richest people in the country.""",
   "Grand Central Terminal New York", "CORNELIUS VANDERBILT")
sc("""His descendants built enormous mansions on Fifth Avenue and in Newport, and spent on a scale that's hard to
imagine. According to the book Fortune's Children, written by a Vanderbilt descendant, the fortune was largely gone
within a few generations. At a family reunion in nineteen seventy three, the book says, not one of the gathered
descendants was a millionaire.""",
   "Newport Rhode Island mansion", "THE FORTUNE DISAPPEARED")
sc("""Compare that with families like the Rockefellers, who used trusts, family offices, philanthropy and strong family
governance. Their wealth has lasted far longer. The difference wasn't how much money they started with. It was the
systems they built around it.""",
   "Rockefeller Center New York", "SYSTEMS, NOT SIZE")

pr("""That's angle one. Assets versus income, generations versus years, diversification, how they use debt, tax
planning, spending rate and protection. Now angle two. The psychology. Because the biggest differences between old and
new money are in their heads.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
sc("""Money changes how people feel, and how they want others to see them. New wealth often comes with something to
prove. Old wealth often comes with something to protect. Those two mindsets lead to very different behavior.""",
   "Two people contrasting styles", "PROVE VS PROTECT")

body_hook = "Old money whispers. New money shouts. Here's the difference."
item(8, "Quiet vs loud", "stealth wealth",
"""Difference number eight. Old money tends to be quiet. New money is often loud.""",
"""Big logos, flashy cars and social media displays are more common with new wealth. Old money families often prefer
discretion. Unbranded clothing, older cars, understated homes. This style is sometimes called quiet luxury or stealth
wealth.""",
"""There are practical reasons for being quiet. Visible wealth attracts scammers, lawsuits, and people who want
something. It can also create resentment. Old money families often teach their children not to discuss money outside
the family.""",
"""The lesson for anyone. You don't need to show what you have. Privacy protects you, and it frees you from the
pressure to keep up appearances. Let your accounts grow quietly.""",
"Designer logos on clothing", "LOUD",
"Understated classic clothing", "QUIET LUXURY",
"Private home behind trees", "PRIVACY PROTECTS")

item(9, "Quality vs brands", "buying to keep",
"""Difference number nine. Old money buys quality. New money often buys brands.""",
"""Old money families often value well made items that last for decades, even generations. Furniture, watches,
clothing and homes that are maintained and passed down. New money is more likely to chase the newest and most
recognized brands.""",
"""Buying quality to keep is often cheaper over time. A well made item used for thirty years costs very little per
year. A trendy item replaced every season costs a fortune.""",
"""The lesson for anyone. For things you use daily, buy quality and take care of it. Skip trends. Ask whether you'd
still want this item in ten years.""",
"Antique wooden furniture", "BUYING TO KEEP",
"Trendy fashion store", "CHASING BRANDS",
"Well maintained leather bag", "TEN YEAR TEST")

item(10, "Security vs proving", "nothing to prove",
"""Difference number ten. Old money feels secure. New money often feels the need to prove itself.""",
"""When you grow up with wealth, you don't need to show it to feel successful. When you've just made it, especially
after growing up without money, there can be a strong urge to show the world you've arrived.""",
"""That urge is human and understandable. But it's expensive. Buying things to prove something to others is a race
with no finish line, because there's always someone with more.""",
"""The lesson for anyone. Find your security in your balance sheet, your skills and your relationships, not in what
other people see.""",
"Calm confident person", "NOTHING TO PROVE",
"Person showing off luxury", "THE URGE TO SHOW",
"Person reading financial statement", "SECURITY ON THE BALANCE SHEET")

item(11, "Patience vs speed", "slow money",
"""Difference number eleven. Old money is patient. New money often moves fast.""",
"""Many new fortunes were built with speed, fast growth, bold bets, quick decisions. That works well when you're
building. But when it comes to protecting wealth, speed can be dangerous. Quick investments in exciting opportunities
are how many fortunes shrink.""",
"""Old money tends to move slowly. Long due diligence, long holding periods, and a willingness to miss out on hot
trends. They often sound boring, and that's the point.""",
"""The lesson for anyone. When it comes to your savings, slow down. Be suspicious of urgency. Good investments rarely
require you to decide today.""",
"Fast sports car racing", "SPEED",
"Turtle walking slowly", "PATIENCE",
"Person reading documents carefully", "SLOW DOWN")

pr("""Quick pause. If you're enjoying this, please subscribe to Ryan Rover Money. It's free and it helps us keep making
long, honest videos about money. Okay, difference twelve.""")

item(12, "Networks vs transactions", "relationships compound",
"""Difference number twelve. Old money invests in relationships.""",
"""Old money families often maintain long relationships with advisors, lawyers, bankers and other families, sometimes
across generations. These networks provide trusted advice, opportunities and protection.""",
"""New money may move from advisor to advisor, or rely on whoever pitches them first. That can lead to bad advice and
high fees. Trust takes time to build, and it compounds like money.""",
"""The lesson for anyone. Build long term relationships with trustworthy professionals and mentors. Look for
fiduciaries, people legally required to act in your best interest.""",
"Business people having dinner", "RELATIONSHIPS COMPOUND",
"Advisor shaking hands with client", "TRUSTED ADVICE",
"Mentor and mentee meeting", "FIND A FIDUCIARY")

item(13, "Identity beyond money", "who you are without it",
"""Difference number thirteen. Old money families often build identity around values, not wealth.""",
"""Families that keep wealth for generations often emphasize shared values, like education, service, work ethic and
philanthropy. Money is seen as a tool to support those values, not the identity itself.""",
"""When identity is tied only to money, people can make reckless decisions to protect their status. When identity is
tied to values, money decisions become clearer.""",
"""The lesson for anyone. Write down what your family stands for. Let those values guide spending and saving
decisions.""",
"Family volunteering together", "VALUES FIRST",
"Family meeting at table", "MONEY SUPPORTS VALUES",
"Written family values", "WHAT WE STAND FOR")

item(14, "Risk appetite", "builders vs keepers",
"""Difference number fourteen. New money takes big risks. Old money manages risk.""",
"""This is where new money has a real strength. Building a fortune usually requires taking risks. Starting a company,
changing careers, betting on yourself. Many old money heirs, raised to protect wealth, become too cautious to build
anything new.""",
"""The best approach often combines both. Take smart risks with your career and a small part of your money, while
protecting the core of your wealth with diversification and insurance.""",
"""The lesson for anyone. Separate your money into two buckets. A protected core, and a small amount for calculated
risks you understand.""",
"Entrepreneur launching startup", "BUILDERS TAKE RISKS",
"Safe vault door", "KEEPERS MANAGE RISK",
"Two buckets labeled", "CORE AND RISK")

pr("""That's angle two. Quiet versus loud, quality versus brands, security versus proving, patience versus speed,
networks, identity and risk. Now angle three. The playbook. How old money keeps it, and what new money does better.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
sc("""Keeping wealth for generations doesn't happen by accident. It takes systems. The families that last often share
a handful of practices. And some of them are surprisingly easy to copy, even for a family with no fortune at all.""",
   "Family estate with gardens", "THE SYSTEMS")

item(15, "Family meetings", "talking about money openly",
"""Difference number fifteen. Old money families hold family meetings about money.""",
"""Many wealthy families hold regular meetings to discuss investments, values, philanthropy and responsibilities. Some
have written family constitutions. The Williams Group research suggested that breakdowns in trust and communication
within families were among the biggest reasons wealth was lost.""",
"""New money often keeps money secret, even from spouses and children. Then, when wealth is passed on, heirs are
unprepared and families fight.""",
"""The lesson for anyone. Hold a simple family money meeting once or twice a year. Share goals and values, and age
appropriate details.""",
"Family meeting around table", "FAMILY MEETINGS",
"Family arguing", "WHEN COMMUNICATION BREAKS",
"Calendar with family meeting", "ONCE OR TWICE A YEAR")

item(16, "Preparing heirs", "teaching before giving",
"""Difference number sixteen. Old money prepares heirs before giving them money.""",
"""The same research found that unprepared heirs were a major cause of lost fortunes. Old money families often teach
children about money early, give them responsibilities gradually, and sometimes release inheritances in stages.""",
"""Thomas Stanley also found that large ongoing gifts to adult children were linked with those children accumulating
less wealth of their own. Preparation matters more than the amount.""",
"""The lesson for anyone. Teach your kids about money early, let them earn, let them make small mistakes, and give
responsibility before giving large sums.""",
"Parent teaching child about money", "TEACH BEFORE GIVING",
"Young adult signing documents", "STAGED INHERITANCE",
"Teen working first job", "LET THEM EARN")

item(17, "Philanthropy", "giving as a family",
"""Difference number seventeen. Old money gives as a family.""",
"""Many old money families run foundations or give together. Philanthropy can unite family members around shared
values, teach younger generations about responsibility, and, under US law, offer legal tax benefits.""",
"""New money is increasingly generous too. Many self made billionaires have pledged to give away large parts of their
fortunes. The habit of giving keeps money in perspective.""",
"""The lesson for anyone. Choose a cause as a family and give together, even small amounts. It builds values that
outlast money.""",
"Charity gala event", "GIVING AS A FAMILY",
"Volunteers at food bank", "SHARED VALUES",
"Family donation jar", "START SMALL")

item(18, "Long term holding", "buy and keep",
"""Difference number eighteen. Old money holds for decades.""",
"""Old money families often keep land, businesses and investments for generations. Long holding periods reduce taxes,
trading costs and the risk of emotional mistakes. They let compounding do its work.""",
"""New money investors may trade more frequently, chasing trends. Research on individual investors, like studies by
Brad Barber and Terrance Odean, has found that frequent traders tended to earn lower returns after costs.""",
"""The lesson for anyone. Buy diversified investments and hold them for the long term. Check them occasionally, not
constantly.""",
"Farmland passed down generations", "BUY AND KEEP",
"Stock trader with many screens", "TRADING TOO MUCH",
"Calendar long term investing", "HOLD FOR DECADES")

body_hook = "Self made money has one big advantage old money doesn't."
item(19, "What new money does better", "hustle and reinvention",
"""Difference number nineteen. What new money does better.""",
"""New money has real strengths. Hunger, creativity, risk taking and a willingness to work extremely hard. Ramsey
Solutions' study found that most American millionaires were first generation. And UBS has reported that self made
entrepreneurs create a large share of new billionaire wealth each year.""",
"""Old money heirs sometimes lose that drive. Without the need to build, some drift. That's one reason fortunes fade.
The families that last often find ways to keep entrepreneurship alive in each generation.""",
"""The lesson for anyone. Keep the hustle of new money. Build skills, take smart risks and create value. Then add the
protection habits of old money.""",
"Entrepreneur working late", "HUSTLE AND REINVENTION",
"Startup team brainstorming", "FIRST GENERATION WEALTH",
"Person building a business", "KEEP THE DRIVE")

item(20, "The best of both", "build like new, keep like old",
"""And difference number twenty. The best approach combines both.""",
"""Build like new money. Work hard, take smart risks, grow your income and create value. Keep like old money. Spend
below your means, diversify, plan for taxes, protect with structure, think long term, and prepare the next
generation.""",
"""That combination is exactly what many self made millionaires do. They build with hunger, then protect with
discipline. And some of them become the founders of new old money families.""",
"""The lesson for anyone. Ask yourself which side you're stronger on. Building or keeping. Then work on the other
side.""",
"Building construction and old building", "BUILD LIKE NEW",
"Old family estate", "KEEP LIKE OLD",
"Person reflecting on goals", "WORK ON THE OTHER SIDE")

# ---------------- Mistakes ----------------
ch("Five classic new money mistakes")
sc("""Let's name the classic mistakes that sink new fortunes, so you can avoid them at any level. Mistake one. Upgrading
everything at once. A sudden jump in lifestyle locks in high fixed costs that are hard to reverse. Mistake two. Lending
or giving money to everyone who asks, without limits. It can drain a fortune and damage relationships at the same time.""",
   "Person handing out money", "MISTAKES 1 AND 2")
sc("""Mistake three. Investing in friends' businesses or exciting deals without proper due diligence. Mistake four.
Ignoring taxes until the bill arrives. And mistake five. Assuming the income will continue forever. Careers end, markets
change, and companies fail. Old money families plan as if the good times might not last, which is exactly why theirs
often do.""",
   "Person surprised by tax bill", "MISTAKES 3, 4 AND 5")
sc("""The antidote to all five is a pause. When new money arrives, whether it's a big raise, a bonus or an inheritance,
many planners suggest parking it somewhere safe for a few months before making big decisions. Time cools emotions and
lets a clear plan form. The money will still be there in three months. A rushed decision, on the other hand, can be
very hard to undo.""",
   "Calm person thinking by window", "PAUSE BEFORE YOU SPEND")

# ---------------- Wealth transfer ----------------
ch("The great wealth transfer")
sc("""Why does this matter now? Because America is in the middle of what's often called the great wealth transfer.
Research firms like Cerulli Associates have estimated that tens of trillions of dollars will pass from older Americans
to heirs and charities over the coming decades. UBS has also reported that inherited wealth is creating a large share
of new billionaires.""",
   "Older couple handing keys to young adult", "THE GREAT WEALTH TRANSFER")
sc("""If the old pattern holds, much of that money will be gone within a generation or two. The families who keep it
will be the ones with old money habits. Communication, preparation, diversification, spending discipline and long term
thinking.""",
   "Family meeting with advisor", "WHO WILL KEEP IT?")
sc("""And for families without big inheritances, the same habits can start something new. Every old money family began
with someone who built and then protected. That person could be you.""",
   "Young family planning future", "IT COULD START WITH YOU")

# ---------------- 30 year plan ----------------
ch("Starting your own old money family")
pr("""So how would an ordinary family start becoming old money, from scratch? Here's a simple thirty year outline.""")
sc("""Years one to ten. Build. Grow your income, live below it, and invest the difference automatically in diversified,
low cost funds. Pay off high interest debt. Build an emergency fund. Write a will and name beneficiaries. Teach your kids
the basics, like saving, earning and waiting for things they want.""",
   "Young family budgeting", "YEARS 1 TO 10: BUILD")
sc("""Years eleven to twenty. Grow and protect. Keep raising your savings rate with every raise. Add income producing
assets, maybe a rental property or a small business, if they fit your skills. Review insurance and estate plans. Start
family money meetings, and give older kids real responsibility for part of their own spending.""",
   "Family reviewing documents", "YEARS 11 TO 20: GROW AND PROTECT")
sc("""Years twenty one to thirty. Keep and pass on. Shift toward preserving wealth, with careful diversification and a
sustainable spending rate. Involve adult children in family decisions and philanthropy. Prepare them before passing
anything on. By then, you've done what every old money family once did. You built something, and taught the next
generation how to keep it.""",
   "Multi generation family together", "YEARS 21 TO 30: KEEP AND PASS ON")

# ---------------- Copy list ----------------
ch("What to copy this year")
sc("""From old money, copy these. Live on less than you earn. Build income producing assets. Diversify. Think in decades.
Have a will and name beneficiaries. Teach your kids about money. And keep your wealth quiet.""",
   "Checklist old money habits", "COPY FROM OLD MONEY")
sc("""From new money, copy these. Grow your income. Take calculated risks with your career. Build skills that create
value. Be willing to start something. And stay hungry. Together, those habits are a powerful combination at any income
level.""",
   "Checklist new money habits", "COPY FROM NEW MONEY")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. Is old money always better with money? No. Plenty of old money families lose their wealth, and
plenty of new money builders manage it brilliantly. These are patterns, not rules. The habits matter more than the
label.""",
   "Question mark sign", "IS OLD MONEY BETTER?")
sc("""Question two. Do I need to be rich to use trusts and estate planning? Not necessarily. A basic will and beneficiary
designations are important for almost everyone. Trusts can be useful for families with young children, property in
multiple states, or complex situations. An estate planning attorney can help you decide.""",
   "Lawyer office meeting", "TRUSTS FOR EVERYONE?")
sc("""Question three. What's the single most important old money habit? Probably spending only part of what your assets
earn, and never the principal. That one rule, followed over decades, is how fortunes survive.""",
   "Growing tree with roots", "THE MOST IMPORTANT HABIT")
sc("""Question four. Is quiet luxury just another trend to buy into? It can be. Some brands now sell expensive plain
clothing labeled as quiet luxury. That misses the point. The old money idea isn't buying a different look. It's caring
less about looks altogether, and putting the money into assets instead.""",
   "Plain expensive clothing store", "QUIET LUXURY AS A TREND")

# ---------------- Recap ----------------
ch("Recap: all 20 differences")
sc("""Quick recap. Angle one, the numbers. Assets versus income, generations versus years, diversified versus
concentrated, debt as a tool, tax planning, spending rate, and protection.""",
   "Checklist on clipboard", "THE NUMBERS: 1 TO 7")
sc("""Angle two, the psychology. Quiet versus loud, quality versus brands, security versus proving, patience versus
speed, networks, identity beyond money, and risk appetite.""",
   "Person thinking at window", "THE PSYCHOLOGY: 8 TO 14")
sc("""Angle three, the playbook. Family meetings, preparing heirs, philanthropy, long term holding, what new money does
better, and the best of both.""",
   "Notebook with plan", "THE PLAYBOOK: 15 TO 20")

# ---------------- Close ----------------
ch("What to do next")
pr("""Here's what I find most encouraging about this topic. Every old money family, without exception, started with
one person who built something and decided to protect it. Their habits weren't secret, and they weren't complicated.
Spend less than you earn, own assets, think long term, and teach the next generation. You don't need a famous last name to think like old money, or a startup exit to build like new money. Build
like new, keep like old. If you want the full plan, it's in my playbook, linked in the description. Tell me in the
comments, are you more of a builder or a keeper? I'm Ryan Rover. See you in the next one.""")

save("video30", "Old Money vs New Money: 20 Differences", [
    "Roy Williams and Vic Preisser, Preparing Heirs (2003): Williams Group research on family wealth transitions (about 70% lost by generation 2, 90% by generation 3)",
    "UBS, Billionaire Ambitions reports (inherited vs self-made billionaire wealth)",
    "Ramsey Solutions, National Study of Millionaires (most millionaires first generation)",
    "Thomas J. Stanley, The Millionaire Next Door (1996): economic outpatient care",
    "Arthur T. Vanderbilt II, Fortune's Children: The Fall of the House of Vanderbilt (1989)",
    "IRS, basis of inherited property (step-up in basis)",
    "Barber and Odean, Trading Is Hazardous to Your Wealth (Journal of Finance, 2000)",
    "Cerulli Associates, US wealth transfer projections",
], "old money vs new money, 20 differences from 3 angles: numbers, psychology, playbook")
