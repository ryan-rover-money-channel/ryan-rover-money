import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

def item(n, title, sub, card_text, paras):
    """paras: list of (text, query, caption)"""
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"SCHEME {n}")
    for t, q, c in paras:
        sc(t, q, c)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Everyone wants to get rich faster. That's human. And there's an entire industry built
on that wish. Courses, apps, coins, trading bots, secret systems and opportunities that are only open for a
few more hours. Today, fifteen get rich quick schemes, how each one actually works, and why almost all of
them fail the people who join.""")
short("Get rich quick schemes all share this one secret")
card("""According to the Federal Trade Commission, Americans reported losing more than twelve billion dollars to
fraud in twenty twenty four, and investment scams were the single biggest category of losses.""",
     {"type": "stat", "label": "reported fraud losses, 2024", "big": "$12.5 BILLION", "size": 150, "sub": "Federal Trade Commission"})
sc("""Here's the key idea of this whole video. Most get rich quick schemes have the same secret. The person
getting rich is the one selling the scheme, not the one buying it. The course seller gets rich from courses.
The promoter gets rich from the coin. The person at the top of the pyramid gets rich from the people below.
Once you see that, you see it everywhere.""",
   "Pyramid structure illustration", "WHO REALLY GETS RICH")
sc("""We'll look at fifteen schemes from three angles. Angle one, the numbers: the classic schemes, and the math
that dooms most participants. Angle two, the psychology: the modern schemes that use hype, gurus and the
fear of missing out. And angle three, the playbook: the newest scams of the internet age, and a checklist that
protects you from all of them.""",
   "Magnifying glass investigation", "THREE ANGLES")
pr("""Number eleven is costing Americans billions every year, and most victims never saw it coming. Let's start
with the classics.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Every number here comes from a named source. Fraud losses come from the Federal Trade Commission's Consumer
Sentinel data and the FBI's Internet Crime Complaint Center. Research on day trading and multi level
marketing comes from published academic and nonprofit studies. Lottery odds come from the official game
rules. This video is education, not financial or legal advice. If you think you've been scammed, report it
to the FTC and the FBI.""",
   "FBI building Washington", "OUR SOURCES")

# ---------------- History ----------------
ch("Even Isaac Newton fell for it")
sc("""If you think only gullible people fall for get rich quick schemes, consider Isaac Newton. One of the greatest
scientists in history. In seventeen twenty, he invested in the South Sea Company, a British trading company
whose stock was soaring on hype. He reportedly sold early for a profit, then watched the price keep climbing,
and bought back in near the top.""",
   "Isaac Newton portrait", "ISAAC NEWTON, 1720")
sc("""The bubble burst. The stock collapsed, and Newton reportedly lost a large sum. A famous line is often
attributed to him: that he could calculate the motions of the heavenly bodies, but not the madness of people.
Whether he said it exactly that way or not, the lesson stuck. Intelligence doesn't protect you from crowd
psychology.""",
   "Old London stock exchange painting", "THE MADNESS OF PEOPLE")
sc("""Every generation has its own version. Railway mania in the eighteen forties. Florida land in the nineteen
twenties. Dot com stocks around two thousand. Meme coins today. The technology changes. The human emotions,
greed, envy and the fear of missing out, stay exactly the same.""",
   "Old railway steam train", "EVERY GENERATION HAS ONE")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The classic schemes, and the math that dooms most people who join.""")

item(1, "The Ponzi scheme", "old money pays new promises",
"""Scheme number one. The Ponzi scheme.""",
[("""A Ponzi scheme promises steady, high returns, but there's no real investment behind them. Early investors
are paid with money from newer investors. It's named after Charles Ponzi, who ran one in Boston in nineteen
twenty, promising fifty percent returns in forty five days. The returns looked real, because early investors
really were paid, with other people's money.""",
  "Vintage 1920 Boston street", "CHARLES PONZI, 1920"),
 ("""The biggest Ponzi scheme in history was run by Bernie Madoff, a respected Wall Street figure. For decades,
he reported smooth, reliable gains to his clients. When it collapsed in two thousand eight, the reported
account balances were around sixty five billion dollars, much of it fictional. Charities, retirees and
families lost life savings.""",
  "Wall Street sign", "MADOFF: $65 BILLION ON PAPER"),
 ("""The math is simple and brutal. A Ponzi scheme needs ever more new money to pay old investors. Eventually,
new money slows down, withdrawals speed up, and it collapses. The people who join late, which is most
people, lose. Real investments go up and down. Suspiciously smooth returns that never have a bad year are a
warning sign, not a feature.""",
  "Line chart perfectly smooth", "TOO SMOOTH IS A WARNING")])

item(2, "The pyramid and the MLM", "recruit to earn",
"""Scheme number two. Pyramid schemes and the problem with many multi level marketing companies.""",
[("""A pyramid scheme pays people mainly for recruiting others, not for selling real products to real customers.
It's illegal. Multi level marketing, or MLM, is legal when it's built around genuine product sales. But
many MLMs reward recruiting heavily, and the structure means most participants are at the bottom.""",
  "Pyramid chart drawing", "RECRUIT TO EARN"),
 ("""A survey by the AARP Foundation in twenty eighteen found that nearly half of MLM participants said they lost
money, and about another quarter said they broke even. The Federal Trade Commission has warned that in many
MLMs, the vast majority of participants make little or no money, after counting what they spend on inventory,
fees and events.""",
  "Boxes of unsold inventory", "MOST LOSE OR BREAK EVEN"),
 ("""The math is the problem. If each person needs to recruit five people, who each recruit five more, you run
out of people in a surprisingly small number of levels. By level ten or so, you'd need millions of new
recruits. The people near the top can earn a lot. Everyone else is chasing a shrinking pool.""",
  "Crowd thinning out", "YOU RUN OUT OF PEOPLE"),
 ("""Try this: before joining any business opportunity, ask for the company's income disclosure statement, which
many MLMs publish. Look at what the typical participant earns, not the top one percent. Then subtract your
costs. That's your realistic outcome.""",
  "Income disclosure document", "READ THE DISCLOSURE")])
card("""If every person recruits five new people, the number needed doubles quickly. By the tenth level, a
pyramid would need nearly ten million people.""",
     {"type": "compare", "left": {"label": "Level 3", "big": "125", "sub": "people needed"},
      "right": {"label": "Level 10", "big": "~9.8M", "sub": "people needed"},
      "note": "Simple math: 5 to the power of each level."})

item(3, "The lottery", "the most popular long shot",
"""Scheme number three. The lottery.""",
[("""The lottery isn't a scam. It's legal, the odds are published, and some of the money supports public
programs. But it's the most popular get rich quick plan in America. And the odds are extraordinary. The odds
of winning the Powerball jackpot are about one in two hundred ninety two million, according to the game's
official rules.""",
  "Lottery tickets", "1 IN 292 MILLION"),
 ("""On average, lotteries pay out less than they take in. That's how they fund prizes and public programs. So
for players as a group, the expected return is negative. Someone has to win, but the typical player loses
most of what they spend, year after year.""",
  "Lottery ticket losing", "THE AVERAGE PLAYER LOSES"),
 ("""Here's the uncomfortable part. Studies have found that lower income households often spend a larger share
of their income on lottery tickets. The lottery sells hope most effectively to people who feel they have
few other paths.""",
  "Convenience store counter", "HOPE FOR SALE"),
 ("""Try this: if you play for fun, set a small monthly limit and treat it as entertainment, like a movie ticket.
And consider investing the same amount on a schedule. Twenty dollars a week invested for thirty years at a
seven percent average return could grow to roughly one hundred thousand dollars. Not a jackpot. But much
more likely.""",
  "Small investment app", "A MORE LIKELY JACKPOT")])

item(4, "Day trading", "most traders lose",
"""Scheme number four. Day trading as a way to get rich.""",
[("""Day trading means buying and selling stocks, options or currencies within the same day, trying to profit
from small price moves. Apps have made it free and easy, and social media is full of screenshots of big wins.
But the research is sobering.""",
  "Trading screens multiple monitors", "BUY AND SELL TODAY"),
 ("""One well known study of day traders in Brazil, by researchers Fernando Chague, Rodrigo De Losso and Bruno
Giovannetti, followed people who day traded for more than three hundred days. They found that about ninety
seven percent lost money. Only a tiny fraction earned more than the minimum wage from it.""",
  "Loss chart red", "ABOUT 97% LOST MONEY"),
 ("""Why do most lose? You're competing against professional firms with faster computers, better data and lower
costs. Every trade can have costs, like spreads and taxes on short term gains. And emotions, fear and greed,
make people sell low and buy high. Day trading is a contest where most players are outmatched.""",
  "Computer servers data center", "OUTMATCHED"),
 ("""Try this: if you want to learn about markets, start with a small amount you can afford to lose, and keep your
real long term money in diversified, low cost funds. Separate the hobby from the plan.""",
  "Two separate jars", "SEPARATE HOBBY FROM PLAN")])
card("""In a study of Brazilian day traders who persisted for over three hundred days, about ninety seven percent
lost money.""",
     {"type": "stat", "label": "persistent day traders", "big": "~97% LOST", "size": 170, "sub": "Chague, De Losso and Giovannetti, 2019"})

item(5, "Sports betting apps", "the house always has an edge",
"""Scheme number five. Sports betting as income.""",
[("""Since a twenty eighteen Supreme Court decision allowed states to legalize sports betting, it has exploded
across much of the country. Apps offer promotions, live bets during games, and parlays with huge payouts.
Some people see it as a way to make money from what they know about sports.""",
  "Sports betting app phone", "BETTING IN YOUR POCKET"),
 ("""But sportsbooks build an edge into the odds, often called the vig, or the house edge. To break even on
standard bets, you need to win more than half the time, consistently. Very few people can do that over the
long run. And sportsbooks can limit accounts that win too much.""",
  "Casino sportsbook screens", "THE HOUSE EDGE"),
 ("""Researchers have begun studying the financial effects of legal sports betting. Some early studies found
signs of higher debt and financial stress in states after betting was legalized, particularly among younger
men. It's entertainment with a cost, not an income plan.""",
  "Young man stressed phone", "ENTERTAINMENT, NOT INCOME"),
 ("""Try this: if you bet, set a strict monthly budget for it, like any entertainment, and never chase losses. And
if betting stops feeling like fun, the national problem gambling helpline, one eight hundred GAMBLER, offers
free, confidential help.""",
  "Helpline phone", "KNOW WHERE TO GET HELP")])
pr("""Those are the classics. The modern ones use something more powerful than math. They use your emotions.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
pr("""Angle two. The psychology. Five modern schemes built on hype, gurus and the fear of missing out.""")
short("The guru getting rich is selling you the course")

item(6, "The pump and dump", "hype up, cash out",
"""Scheme number six. The pump and dump.""",
[("""In a pump and dump, promoters buy a cheap stock or coin, then hype it everywhere. Social media, chat groups,
paid influencers. The price shoots up as new buyers pile in. Then the promoters sell, or dump, at the top.
The price crashes, and the latecomers are left holding something worth very little.""",
  "Rocket chart then crash", "HYPE UP, CASH OUT"),
 ("""This used to happen with penny stocks through phone calls and spam emails. Today it happens with small
crypto tokens and thinly traded stocks through social media and messaging apps. The Securities and Exchange
Commission has brought many cases against people running these schemes.""",
  "Chat group phone messages", "NOW ON SOCIAL MEDIA"),
 ("""The psychology is fear of missing out. You see the price rising, you see people celebrating, and you jump in
because you don't want to be the one who missed it. But by the time something is everywhere, the early
buyers are often getting ready to sell to you.""",
  "Crowd rushing", "FEAR OF MISSING OUT"),
 ("""Try this: if someone is urging you to buy something right now, before it moons, ask, why are they telling
me? If they already own it, they benefit when you buy. That's a conflict, and sometimes it's a scheme.""",
  "Person questioning phone", "WHY ARE THEY TELLING ME?")])

item(7, "The mania", "everyone's getting rich",
"""Scheme number seven. Joining a mania.""",
[("""Manias aren't always scams. Sometimes there's a real technology or asset underneath. But when prices rise
mostly because people expect them to keep rising, it can turn into a bubble. History is full of them, from
tulip bulbs in the sixteen hundreds, to dot com stocks around two thousand, to the NFT craze of twenty twenty
one.""",
  "Tulips field Netherlands", "TULIPS TO NFTs"),
 ("""In twenty twenty one, some digital collectibles, NFTs, sold for millions of dollars. Within a couple of years,
trading volumes had collapsed and many NFTs were worth a tiny fraction of their peak prices. The people who
bought near the top, often with money they couldn't afford to lose, took the biggest hits.""",
  "Digital art on screen", "THE NFT CRASH"),
 ("""The psychological driver is social proof. When everyone around you is making money, it feels foolish not to
join. Your neighbor, your coworker and your cousin are all bragging about gains. Nobody brags about losses,
so you only hear one side.""",
  "Friends celebrating phones", "YOU ONLY HEAR THE WINS"),
 ("""Try this: when you hear about a new thing that's making everyone rich, write down the date and the price, and
wait three months before doing anything. You'll learn more from watching than from jumping in.""",
  "Notebook date written", "WAIT AND WATCH")])

item(8, "The trading course", "the guru's real business",
"""Scheme number eight. The trading course.""",
[("""You've seen the ads. A young person with a sports car, a beach and a laptop, promising to teach you their
trading system. For a few hundred or a few thousand dollars, you can learn the secret. Often with a monthly
membership for signals and a private chat group.""",
  "Luxury car beach laptop", "THE GURU LIFESTYLE"),
 ("""Here's the question to ask. If the system reliably made lots of money, why would they sell it? The honest
answer, in many cases, is that the course is the business. Selling courses to thousands of people produces
steady income, while trading produces uncertain results.""",
  "Online course sales page", "THE COURSE IS THE BUSINESS"),
 ("""Regulators have taken action against some trading educators for misleading claims about earnings. And the
lifestyle in the ads is sometimes rented. The car, the house, the private jet photo. The goal is to make you
feel that success is close, and that the course is the only thing in the way.""",
  "Rented supercar", "SOMETIMES IT'S RENTED"),
 ("""Try this: before buying any course that promises income, search the person's name with words like complaint,
lawsuit or refund. And remember, real investing education, like how index funds work, is available for free
from sources like the SEC's investor education website.""",
  "SEC investor education website", "FREE REAL EDUCATION")])

item(9, "The seminar", "free lunch, expensive upsell",
"""Scheme number nine. The free seminar.""",
[("""Free real estate seminars, free wealth workshops, free dinners. They usually end with an upsell. A mentoring
program, an advanced course or a coaching package that can cost thousands, sometimes tens of thousands of
dollars. The free event is the funnel.""",
  "Hotel conference room seminar", "THE FREE FUNNEL"),
 ("""The most famous example may be Trump University, which offered real estate seminars and expensive mentoring
packages. Former students sued, saying they were misled, and in twenty sixteen a settlement of twenty five
million dollars was reached, without an admission of wrongdoing. Many other seminar companies have faced
similar complaints and legal actions.""",
  "Courthouse building", "A $25 MILLION SETTLEMENT"),
 ("""Seminars use a powerful set of persuasion tools. Free food creates a feeling that you owe something. Limited
time discounts create urgency. Success stories create social proof. And the high price itself makes the
product feel valuable.""",
  "Limited time offer sign", "THE PERSUASION TOOLKIT"),
 ("""Try this: go to any free seminar with your credit cards left at home. Take notes, then wait at least a week
before buying anything. If it's truly valuable, it will still be available.""",
  "Wallet left at home", "LEAVE THE CARDS AT HOME")])

item(10, "The passive income dream", "easy money, hard reality",
"""Scheme number ten. The easy passive income business.""",
[("""Dropshipping, print on demand, automated online stores, affiliate empires, YouTube automation. Sellers promise
that you can set it up once and earn while you sleep. Some people really do build real businesses this way.
But it's almost never fast, easy or passive.""",
  "Laptop on beach", "EARN WHILE YOU SLEEP?"),
 ("""Real online businesses need marketing, customer service, product quality, returns, and constant adjustment.
Advertising costs can eat the profits. Competition is fierce, because the same course taught the same
strategy to thousands of other people at the same time.""",
  "Online store dashboard", "THOUSANDS DOING THE SAME"),
 ("""The scheme isn't the business model itself. It's the promise that it's easy, and the expensive course or
software you need to buy first. The people reliably earning passive income are often the ones selling the
dream.""",
  "Money flowing to seller", "SELLING THE DREAM"),
 ("""Try this: if you want to start an online business, start small and cheap. Test one idea with your own effort
and a small budget before paying anyone for a system. Real businesses grow from real customers, not from
course modules.""",
  "Small business owner packaging", "START SMALL AND CHEAP")])

# ---------------- Mid ----------------
ch("A quick favor")
pr("""Quick pause. If this video might protect someone you love from one of these schemes, share it with them.
And subscribe to the channel if it's helping you. It's free, and it helps me keep making these videos. Now,
the newest scams, and how to protect yourself.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
pr("""Angle three. Five scams of the internet age, and the checklist that stops them.""")
short("This investment scam starts with a wrong number text")

item(11, "Pig butchering", "the long con",
"""Scheme number eleven. Pig butchering.""",
[("""The name is ugly, and so is the scam. It often starts with a wrong number text, a dating app match or a
friendly message on social media. Over weeks or months, the scammer builds trust, sometimes romance. Then they
mention how they've been making money investing in crypto, and offer to show you.""",
  "Wrong number text message", "IT STARTS WITH A TEXT"),
 ("""They direct you to a fake investment platform that looks real. You invest a little, and the platform shows
big gains. You might even withdraw a small amount, which builds trust. So you invest more. When you try to
withdraw the larger sum, there are suddenly fees, taxes or excuses. Then the person disappears.""",
  "Fake trading app screen", "THE FAKE PLATFORM"),
 ("""The FBI's Internet Crime Complaint Center has reported that investment fraud, much of it involving
cryptocurrency, causes billions of dollars in reported losses every year, more than any other type of
crime it tracks. Victims include people of every age and education level.""",
  "FBI internet crime report", "BILLIONS EVERY YEAR"),
 ("""Try this: never invest through a platform recommended by someone you've only met online, no matter how
long you've talked. Never send money to someone you haven't met in person. And if you've been targeted,
report it at the FBI's IC3 website.""",
  "Report button website", "NEVER INVEST WITH STRANGERS")])

item(12, "The AI trading bot", "new words, old trick",
"""Scheme number twelve. The AI trading bot.""",
[("""Every new technology brings new scams that use its name. Today, it's artificial intelligence. Ads promise
an AI trading bot that makes guaranteed daily profits, or a quantum algorithm that never loses. Regulators,
including the SEC and the Commodity Futures Trading Commission, have warned investors about these claims.""",
  "Robot trading screen", "AI TRADING BOT"),
 ("""Some of these are simply Ponzi schemes with modern branding. Others are fake platforms that never invest your
money at all. Many use deepfake videos of celebrities or famous investors appearing to endorse them.""",
  "Deepfake video warning", "DEEPFAKE ENDORSEMENTS"),
 ("""The truth is that if an AI system reliably produced guaranteed profits, its owners would have no reason to
sell it to you for a monthly fee. Big financial firms do use algorithms, but they don't guarantee profits,
and they don't advertise on social media.""",
  "Data center servers", "NO ONE SELLS A MONEY MACHINE"),
 ("""Try this: whenever you see the words guaranteed and returns together, stop. Legitimate investments always
carry risk, and honest firms say so.""",
  "Stop sign", "GUARANTEED RETURNS = STOP")])

item(13, "The guaranteed note", "high yield, no risk",
"""Scheme number thirteen. The guaranteed high yield investment.""",
[("""This scheme often targets retirees. A promissory note, a private fund or a special program that promises ten
or twelve percent a year, guaranteed, with no risk. It's often sold by a friendly agent, at a church, a club,
or through a trusted community.""",
  "Retirees at community event", "TEN PERCENT, GUARANTEED?"),
 ("""The SEC and state securities regulators have repeatedly warned about promissory note fraud and unregistered
investments. Often, the investment isn't registered, the seller isn't licensed, and the returns are paid from
new investors' money, a Ponzi scheme in disguise.""",
  "Securities regulator warning", "UNREGISTERED, UNLICENSED"),
 ("""Try this: before investing in anything, check the seller on FINRA BrokerCheck and the SEC's Investment Adviser
Public Disclosure website, both free. And check whether the investment is registered with the SEC or your
state securities regulator.""",
  "BrokerCheck website", "CHECK THE SELLER"),
 ("""And remember that safe, insured products already exist for people who want stability. Treasury bonds,
FDIC insured savings accounts and certificates of deposit. They won't pay ten percent guaranteed. That's
exactly the point. Real safety comes with modest returns. If someone offers both high returns and total
safety, they're offering something that doesn't exist.""",
  "Treasury bonds document", "REAL SAFETY IS MODEST")])

item(14, "The cash gifting circle", "friendship as a pyramid",
"""Scheme number fourteen. Gifting circles and blessing looms.""",
[("""These schemes spread through friends and social media. You give money, say one hundred or one thousand
dollars, to someone at the center of a circle. Then you recruit others, and eventually you move to the
center and receive gifts worth many times what you put in.""",
  "Women circle group meeting", "THE GIFTING CIRCLE"),
 ("""It's a pyramid scheme dressed up as community and generosity. The math is the same as scheme number two.
The circles need endless new members, and most people who join lose their money. Regulators have warned that
calling it a gift doesn't make it legal.""",
  "Circle diagram growing", "A PYRAMID IN DISGUISE"),
 ("""Try this: if an opportunity requires you to recruit others to get paid, and there's no real product being
sold, walk away. And gently warn the friend who invited you. They may be a victim too.""",
  "Friends talking honestly", "WALK AWAY, WARN A FRIEND"),
 ("""These circles can also damage friendships for years. When the circle collapses, the people who
recruited their friends often feel responsible for the losses. The money is gone, and so is the trust. It's
one more reason why schemes that run on friendship are so harmful.""",
  "Broken friendship concept", "IT COSTS FRIENDSHIPS")])

item(15, "The recovery scam", "victims targeted twice",
"""Scheme number fifteen. The recovery scam.""",
[("""This is one of the cruelest. After someone loses money to a scam, they're contacted by a person claiming to
be a lawyer, an investigator or even a government agent who can recover their money, for an upfront fee.
It's often the same scammers, or their partners, targeting the victim a second time.""",
  "Phone call from lawyer", "TARGETED TWICE"),
 ("""The FTC and FBI have warned that legitimate government agencies don't charge fees to recover lost money,
and won't contact you asking for payment in gift cards, crypto or wire transfers.""",
  "Gift cards payment warning", "NO UPFRONT FEES"),
 ("""Try this: if you've lost money to a scam, report it directly to the FTC at report fraud dot FTC dot gov, and
to the FBI's IC3. Contact your bank immediately. And be extremely skeptical of anyone who contacts you
offering to get it back for a fee.""",
  "Reporting fraud online", "REPORT, DON'T PAY"),
 ("""And if you've been scammed, please know this. It is not your fault that someone lied to you. Scammers are
professionals who do this all day. Reporting helps investigators find patterns and sometimes recover money,
and talking about it helps protect the next person.""",
  "Comforting hand on shoulder", "IT'S NOT YOUR FAULT")])

ch("The scam checklist")
pr("""Here's the checklist that catches nearly every scheme in this video. Ten red flags. If you see two or more,
walk away.""")
short("10 red flags that expose almost any money scam")
sc("""Red flag one. Guaranteed high returns with little or no risk. Red flag two. Pressure to act right now. Red flag
three. You make money mainly by recruiting others. Red flag four. Payment by gift card, wire transfer or crypto
to a person.""",
   "Red flags lined up", "RED FLAGS 1 TO 4")
sc("""Red flag five. The seller isn't registered or licensed, and you can't find them on BrokerCheck. Red flag six.
Returns that are suspiciously smooth, every month. Red flag seven. You can't clearly explain how the money is
made.""",
   "Warning signs board", "RED FLAGS 5 TO 7")
sc("""Red flag eight. You were contacted out of the blue, especially online. Red flag nine. Celebrity endorsements
you can't verify. And red flag ten. Fees appear when you try to withdraw your money. If you see any of these,
stop and talk to someone you trust before sending a single dollar.""",
   "Person thinking before acting", "RED FLAGS 8 TO 10")
card("""Guaranteed returns. Pressure. Recruiting. Gift cards or crypto. Unlicensed seller. Smooth returns. Unclear
model. Unsolicited contact. Fake celebrities. Withdrawal fees.""",
     {"type": "stat", "label": "the scam checklist", "big": "10 RED FLAGS", "size": 170, "sub": "two or more? walk away"})

ch("What actually works")
pr("""So if get rich quick doesn't work, what does? The answer is boring. And that's exactly why it works.""")
sc("""Get rich slowly. Spend less than you earn. Build an emergency fund. Avoid high interest debt. Invest
consistently in diversified, low cost funds, and hold them for decades. Increase your income through skills
and career growth. None of it is exciting. All of it is available to ordinary people.""",
   "Slow growing tree", "GET RICH SLOWLY")
card("""Five hundred dollars a month, invested at a seven percent average yearly return for thirty years. You'd put
in one hundred eighty thousand dollars. That's the slow path, and it's far more reliable than any scheme.""",
     {"type": "growth", "monthly": 500, "rate": 0.07, "years": 30})
sc("""That's an illustration, not a promise. Markets go up and down, and there are bad years. But notice that this
path doesn't need you to be lucky, to be early, or to find a secret. It just needs time and consistency. Every
scheme in this video is selling you a shortcut around those two things. There isn't one.""",
   "Long straight road", "NO SHORTCUT")

# ---------------- Too good math ----------------
ch("The math of too good to be true")
pr("""Let's do some quick math on the returns schemes promise, because it exposes them instantly.""")
sc("""Many scams promise one percent a day. It sounds modest. One percent. But compounded daily for a year, one
percent a day turns one thousand dollars into roughly thirty seven thousand dollars. If that were real and
repeatable, a few thousand dollars would make you one of the richest people on Earth within a few years. That's
how you know it isn't.""",
   "Calculator big number", "1% A DAY = 37X A YEAR")
sc("""Charles Ponzi promised fifty percent in forty five days. Some modern schemes promise ten percent a month.
Compare that with the long run average of broad stock markets, often cited at around seven to ten percent a
year before inflation, with plenty of bad years along the way. When someone promises in a month what the
market historically delivered in a year, with no risk, the numbers are telling you the truth.""",
   "Stock market long term chart", "A MONTH VS A YEAR")
card("""One percent a day sounds small. Compounded for a year, it would turn one thousand dollars into about thirty
seven thousand. That's why no real investment offers it.""",
     {"type": "compare", "left": {"label": "Promised", "big": "1% a day", "sub": "sounds modest"},
      "right": {"label": "Means", "big": "~37x", "sub": "in a single year"},
      "note": "Simple compounding math. Real investments don't do this."})
sc("""Here's a simple rule. If the promised return is far above what the broad stock market has historically
earned, and the seller says the risk is low or zero, one of those two claims is false. Usually both.""",
   "Scale imbalanced", "ONE OF THEM IS FALSE")

# ---------------- Why we fall ----------------
ch("Why smart people fall for it")
pr("""Let's talk about why smart, careful people still fall for these schemes. It's not about intelligence.""")
sc("""First, trust. Most schemes spread through people we trust. A friend, a church member, a coworker, a
family member, or someone we've been talking to online for months. Scammers call this affinity fraud. They
target communities where trust is high and questions feel rude.""",
   "Church community gathering", "AFFINITY FRAUD")
sc("""Second, stress. People facing money problems, retirement worries or a big life change are more likely to
take risks for a big payoff. Scammers look for those moments. A layoff, a divorce, the loss of a spouse, or
the fear that savings won't last.""",
   "Stressed person bills", "STRESS OPENS THE DOOR")
sc("""Third, small wins. Many schemes let you win early. A small withdrawal that works, a first trade that profits,
a few weeks of gains on the dashboard. Those wins create confidence, and confidence leads to bigger
deposits. Fourth, shame. Once people have lost money, they often keep going, hoping to win it back, or stay
silent because they're embarrassed. Both help the scammer.""",
   "Slot machine small win", "SMALL WINS, BIG DEPOSITS")

sc("""One last thought on what actually works. The slow path has a hidden benefit. It doesn't require you to
watch screens, chase tips, or trust strangers. It runs quietly in the background while you live your life,
work, and spend time with people you love. A scheme asks for your money and your attention. The slow path
asks only for your patience.""",
   "Family relaxing park", "PATIENCE, NOT ATTENTION")

# ---------------- Talk to someone ----------------
ch("When someone you love is in one")
pr("""What if it's not you, but someone you love who's caught in a scheme? Here's how to help, without pushing
them away.""")
sc("""Start with curiosity, not judgment. Ask questions. How does it make money? Have you been able to withdraw?
Who else is involved? People defend their decisions when they feel attacked. They think more clearly when
they're asked to explain.""",
   "Two people having coffee talk", "CURIOSITY, NOT JUDGMENT")
sc("""Then look things up together. Search the company name with the word scam or complaint. Check BrokerCheck and
the SEC's website. Look for regulator warnings. Finding the evidence together is much more powerful than being
told they're wrong.""",
   "Searching on laptop together", "LOOK IT UP TOGETHER")
sc("""Suggest a simple test. Try to withdraw a meaningful amount of money. Legitimate investments let you take
your money out, sometimes with clear, disclosed fees or tax consequences. If withdrawals are blocked, delayed
or require new payments, that's often the moment people realize the truth.""",
   "Withdraw button on app", "THE WITHDRAWAL TEST")
sc("""And stay close, even if they don't listen at first. Many victims say they were too embarrassed to admit
the loss. If they know you won't say I told you so, they're more likely to come to you before they send the
next payment.""",
   "Family hug support", "STAY CLOSE")

# ---------------- Stories ----------------
ch("Two neighbors, one opportunity")
short("Two neighbors, one 'opportunity', two very different endings")
sc("""Let's finish with two neighbors. Gary, fifty eight, received a friendly message from someone he met online.
Over two months, they became friends. Then she showed him a crypto platform where she'd been earning big
returns. Gary started with five thousand dollars. The app showed gains every week.""",
   "Older man on laptop at home", "GARY: THE NEW FRIEND")
sc("""He invested more, eventually much of his retirement savings. When he tried to withdraw, the platform asked for
a tax payment first. Then another fee. Then his friend stopped answering. Gary lost most of what he put in.
He was embarrassed and didn't tell anyone for months, which is very common with scam victims.""",
   "Man sitting alone worried", "THE WITHDRAWAL FEES")
sc("""His neighbor, Linda, got a similar message. But she had a rule. Never invest with someone I haven't met in
person, and never through a platform someone else picks. She looked up the platform, found warnings about it
online, and reported the account. Then she told Gary about it, too late for his money, but in time to stop him
from paying a recovery scammer who contacted him next.""",
   "Woman on phone reporting", "LINDA: THE RULE")
sc("""The difference wasn't intelligence. Gary was a smart, educated man. The difference was a rule decided in
advance, before emotions got involved. That's the real protection. Not being clever in the moment. Having
rules that make the decision for you.""",
   "Notebook written rules", "A RULE DECIDED IN ADVANCE")

sc("""Notice something else about Gary's story. The scam didn't feel like a scam at any point along the way. It
felt like friendship, then like a lucky opportunity, then like a temporary problem with fees. Every step was
small. That's how most people lose large amounts. Not in one big decision, but in a series of small ones that
each seemed reasonable.""",
   "Footsteps on path", "A SERIES OF SMALL STEPS")

# ---------------- FAQ ----------------
ch("Questions people ask")
pr("""Let me answer a few questions people ask about these schemes.""")
sc("""Question one. Is crypto a scam? Crypto itself is a technology and an asset class, and some people invest in
it as a small, high risk part of their portfolio. But crypto is also used in many scams, because transfers are
fast and hard to reverse. Be very careful about who you're dealing with, and never invest more than you can
afford to lose.""",
   "Bitcoin coins", "IS CRYPTO A SCAM?")
sc("""Question two. Are all MLMs pyramid schemes? Not legally. Some sell real products to real customers. But many
participants still lose money. Read the income disclosure, count all your costs, and be very cautious if the
pitch is more about recruiting than about the product.""",
   "Products display table", "ARE ALL MLMs SCAMS?")
sc("""Question three. What if I already lost money? First, stop sending money, no matter what fees are demanded.
Contact your bank right away. Report the scam to the FTC and the FBI's IC3. Save every message and receipt. And
talk to someone you trust. Shame keeps victims quiet, and silence helps scammers.""",
   "Person talking to friend support", "ALREADY LOST MONEY?")
sc("""Question four. How do I protect my parents? Talk about scams openly and often, without judgment. Share
specific examples, like the wrong number text. Agree on a family rule: no big money moves without a
conversation first. And consider setting up account alerts together.""",
   "Adult child with elderly parent", "PROTECT YOUR PARENTS")
sc("""Question five. How can I tell a real investment adviser from a fake one? Look them up on FINRA BrokerCheck and
the SEC's Investment Adviser Public Disclosure site. Ask if they're a fiduciary. Ask where your money will be held.
Legitimate advisers usually use a well known independent custodian, a separate firm that holds your assets,
so they can't simply take your money. If the answer is send it to me directly, walk away.""",
   "Financial adviser office", "REAL OR FAKE ADVISER?")
sc("""Question six. What's the single best protection? A waiting period. Most scams depend on speed, because
time lets you think, ask and search. Make a personal rule that any investment over a small amount waits at least
one week, and gets discussed with someone you trust. Scammers hate that rule. Honest people don't mind it at
all.""",
   "Calendar one week later", "THE WAITING PERIOD")
sc("""And question seven. Is there any legitimate way to get rich fast? Some people do get rich fast, through a
successful business, a rare skill or luck. But these are exceptions, usually after years of work nobody saw.
For most people, the reliable path is slower, and it works better than any shortcut.""",
   "Entrepreneur working late", "ANY FAST WAY?")

# ---------------- Recap ----------------
ch("Recap: all 15 schemes")
sc("""Quick recap. The classics: Ponzi schemes, pyramids and many MLMs, the lottery, day trading and sports
betting. The modern hype schemes: the pump and dump, the mania, the trading course, the free seminar and the
passive income dream.""",
   "Checklist clipboard", "THE FIRST TEN")
sc("""And the internet age scams: pig butchering, AI trading bots, guaranteed high yield notes, gifting circles and
recovery scams. One truth connects them all. In a get rich quick scheme, the person getting rich is usually the
one selling it.""",
   "Pyramid illustration", "THE LAST FIVE")

# ---------------- Close ----------------
ch("What to do next")
pr("""If you want the real, slow and reliable plan for building wealth, it's in my playbook. The link is in the
description. And watch my video on twenty money myths that keep you poor. Many of these schemes start with one of
those myths. I'm Ryan Rover. See you in the next one.""")

save("video49", "15 Get Rich Quick Schemes and Why They Fail", [
    "Federal Trade Commission, Consumer Sentinel Network data (reported fraud losses of $12.5 billion in 2024; investment scams the largest category)",
    "FBI Internet Crime Complaint Center (IC3), annual Internet Crime Reports (investment fraud losses)",
    "AARP Foundation, Multilevel Marketing: Research Study (2018)",
    "FTC, Business Guidance Concerning Multi-Level Marketing",
    "Chague, De Losso and Giovannetti, Day Trading for a Living? (2019)",
    "Powerball official game rules (jackpot odds about 1 in 292.2 million)",
    "SEC and CFTC investor alerts (pump and dump, AI trading claims, promissory notes); FINRA BrokerCheck",
    "Bernard Madoff case (2008); Trump University settlement (2016); Murphy v. NCAA (2018)",
    "Growth figures: stated illustrative math",
], "get rich quick schemes: numbers, psychology, playbook")
