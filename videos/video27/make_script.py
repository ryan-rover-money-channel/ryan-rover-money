import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

body_hook = None  # set right before item() to start a Short at its first explained scene

def item(n, title, sub, card_text, body, example, fix, q1, c1, q2, c2, q3, c3):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"LESSON {n}")
    global body_hook
    if body_hook:
        short(body_hook); body_hook = None
    sc(body, q1, c1)
    sc(example, q2, c2)
    sc(fix, q3, c3)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Most of us learned about money the hard way. A first credit card, a first car loan,
a first month where the paycheck ran out before the bills did. Nobody sat us down and explained how any of it
worked. But in many wealthy families, kids learn these lessons at the kitchen table, years before they ever earn
a paycheck. Today, twenty five money lessons rich parents teach their kids. And here's the good news. You can
teach them to your kids, and you can learn them yourself, at any age.""")
short("Most kids never learn this at school. Rich kids learn it at home.")
card("""Here's why this matters so much. Researchers at the University of Cambridge, in a study for the UK's
Money Advice Service, found that many core money habits are already forming by around age seven.""",
     {"type": "stat", "label": "age when money habits start forming", "big": "~7", "sub": "University of Cambridge, for the Money Advice Service (2013)"})
sc("""Think about that. By the time a child is in second grade, they're already picking up attitudes about
saving, spending and waiting for things they want. Most of those attitudes come from watching their parents.
Not from lectures. From what happens in the grocery store, at the car dealership and around the dinner table.
That's why the money lessons in a family get passed down, generation after generation, whether anyone intends
to teach them or not.""",
   "Child with piggy bank at home", "HABITS START EARLY")
sc("""We'll look at these twenty five lessons from three angles. First, the numbers. The basic math of money
that many wealthy families teach early, like compound interest and opportunity cost. Second, the psychology. The
attitudes about waiting, comparing and enough that shape a lifetime of decisions. And third, the playbook. The
practical tools, from first investment accounts to credit scores, that give kids a head start. Whether you're a
parent, a grandparent, or someone who wishes they'd learned this at twelve, there's something here for you.""",
   "Family at kitchen table talking", "THREE ANGLES")
pr("""Let's start with the numbers. Lesson one is the foundation of everything else.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Our sources. The research on when money habits form comes from the University of Cambridge's study for the
Money Advice Service. Data on how families talk about money comes from T. Rowe Price's Parents, Kids and Money
Survey. Research on giving money to adult children comes from Thomas Stanley's work in The Millionaire Next
Door. Account rules come from the IRS. Growth examples use a stated seven percent average yearly return, an
illustration, not a promise. This is education, not financial advice.""",
   "Library research desk", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Nine lessons about how money actually works, taught in ways a kid can understand.""")

item(1, "Money is earned", "work creates value",
"""Lesson number one. Money comes from creating value for other people.""",
"""Many wealthy parents make sure their kids understand where money comes from. It doesn't come from the ATM or
from a card. It comes from someone doing something valuable for someone else. That might be a job, a business, or
an investment in a business. Kids who understand this early tend to see money as something they can create, not
just something they receive.""",
"""Some families pay for extra chores beyond the basics, like washing the car or helping with yard work. Others
encourage teenagers to get part time jobs, even when the family doesn't need the money. The point isn't the
amount. It's the connection between effort, value and reward. A teenager who earns their first hundred dollars
often treats it very differently from a hundred dollars that was simply handed over.""",
"""Teach it this week. Pick one extra job around the house that a child can do for pay. Talk about why it's
worth money. Someone would otherwise have to do it, or pay someone else to. If you're an adult learning this
lesson yourself, ask the same question about your job. What value do I create, and how could I create more?""",
"Kid washing car in driveway", "MONEY IS EARNED",
"Teenager working first job", "EFFORT, VALUE, REWARD",
"Child doing yard work", "ONE PAID JOB THIS WEEK")

item(2, "Save first, then spend", "the three jars",
"""Lesson number two. Save first, then spend what's left.""",
"""A classic teaching tool is three jars, labeled save, spend and give. Every time a child gets money, whether
it's an allowance, a gift or pay for a chore, it's split between the jars before anything is spent. It's simple,
visual and surprisingly powerful, because it builds the habit of paying yourself first before a child ever sees
a paycheck.""",
"""Adults who pay themselves first, by automatically moving money to savings on payday, tend to save far more than
those who save whatever is left at the end of the month. The three jars are the childhood version of exactly that
system. Kids who grow up with it often find automatic saving completely natural as adults.""",
"""Teach it this week. Set up three jars or three envelopes. Decide on a split together, for example fifty
percent spend, forty percent save, ten percent give. Let the child choose what to do with the spend jar, even if
they make choices you wouldn't. For yourself, set up one automatic transfer to savings the day after payday.""",
"Three jars with coins", "SAVE, SPEND, GIVE",
"Child putting coin in jar", "PAY YOURSELF FIRST",
"Labeled envelopes on table", "SET UP THE JARS")

item(3, "Compound interest", "money that grows by itself",
"""Lesson number three. Money can grow on its own, if you give it time.""",
"""Compound interest is when your money earns returns, and then those returns earn returns too. Over time, the
growth snowballs. Many wealthy parents explain it early, because time is the most powerful ingredient, and kids
have more time than anyone. A dollar invested at fifteen has fifty years to grow before a typical retirement
age.""",
"""Some parents make it concrete with a family bank. They offer a generous interest rate on money the child
leaves with them, maybe paid monthly. Watching a balance grow without doing anything is a magical moment for a
kid. It turns an abstract idea into something they can see. Others show a simple chart of what a small monthly
investment becomes over decades.""",
"""Teach it this week. Use a free online compound interest calculator with your child. Try one hundred dollars a
month at a seven percent average yearly return, for ten, twenty and fifty years. Let them see how the line
curves upward. For yourself, run the same numbers on your own savings.""",
"Snowball rolling downhill", "MONEY THAT GROWS",
"Parent and child with tablet chart", "THE FAMILY BANK",
"Compound interest calculator screen", "RUN THE NUMBERS")

card("""Here's what that looks like. One hundred dollars a month, starting at age fifteen and invested until
sixty five, at a seven percent average yearly return, could grow to over five hundred thousand dollars. Total put
in, sixty thousand.""",
     {"type": "growth", "monthly": 100, "rate": 0.07, "years": 50})

body_hook = "Interest can make you rich. It can also make you broke."
item(4, "Interest works both ways", "debt compounds too",
"""Lesson number four. Interest works against you when you borrow.""",
"""The same math that grows savings can grow debt. Wealthy parents often make sure their kids understand this
before they get their first credit card. A card balance at over twenty percent interest, which has been typical in
recent years according to the Federal Reserve, can grow quickly if you only make minimum payments.""",
"""A powerful way to teach this is to let a child borrow a small amount from you, for something they want now,
and charge them interest. When they have to pay back twelve dollars for a ten dollar loan, the lesson sticks far
better than any lecture. Some families do the reverse too, and show how long it takes to pay off a balance with
minimum payments.""",
"""Teach it this week. Look at a real credit card statement together and find the box that shows how long it
would take to pay off the balance with minimum payments. For yourself, list every debt you have with its interest
rate, and target the highest rate first.""",
"Credit card on table", "DEBT COMPOUNDS TOO",
"Child borrowing money from parent", "CHARGE A LITTLE INTEREST",
"Credit card statement minimum payment box", "READ THE WARNING BOX")

item(5, "Price vs value", "cost per use",
"""Lesson number five. The price isn't the same as the value.""",
"""Rich parents often teach kids to think about cost per use. A sixty dollar pair of shoes worn three hundred
times costs twenty cents a wear. A thirty dollar pair worn five times costs six dollars a wear. The cheaper item
was actually more expensive. This simple idea helps kids judge purchases by how much they'll really use them.""",
"""It also works the other way. Some things are expensive and still not worth it, because they won't be used.
The trendy gadget that sits in a drawer after a week. The toy that's forgotten by the next birthday. Asking how
often will I use this before buying is one of the most useful money habits a person can have.""",
"""Teach it this week. Before your child's next purchase, ask them to guess how many times they'll use it, then
divide the price by that number. For yourself, try it on the five most expensive things in your closet or
garage.""",
"Running shoes worn out", "COST PER USE",
"Gadget in drawer unused", "PRICE ISN'T VALUE",
"Price tag and calculator", "DIVIDE BY USES")

item(6, "Every choice costs something", "opportunity cost",
"""Lesson number six. Every time you spend, you're giving something else up.""",
"""Economists call it opportunity cost. If you spend twenty dollars on candy, you can't spend that twenty dollars
on a game you've been saving for. Wealthy parents often teach this by making kids choose, rather than buying both.
The question becomes not can I afford this, but what am I giving up to get it?""",
"""For adults, the biggest opportunity cost is often future growth. A thousand dollars spent today is not just a
thousand dollars. At a seven percent average yearly return, it could have roughly doubled about every ten years.
That's why wealthy people often think twice before big purchases.""",
"""Teach it this week. At the store, give your child a fixed amount and let them choose between two things they
want. Talk about what they gave up. For yourself, before any purchase over a hundred dollars, say out loud what
else that money could do.""",
"Child choosing between two toys", "WHAT ARE YOU GIVING UP?",
"Fork in the road", "OPPORTUNITY COST",
"Shopping with fixed cash", "CHOOSE ONE")

item(7, "Budgeting with an allowance", "practice with small money",
"""Lesson number seven. A budget is just a plan for your money.""",
"""Many financially savvy parents use an allowance as a teaching tool, not just pocket money. As kids get older,
the allowance grows, and so do their responsibilities. A teenager might get a monthly amount that covers their
clothes, entertainment and phone, and has to plan how to make it last.""",
"""This lets kids practice budgeting with small amounts, when mistakes are cheap. Running out of money in the
middle of the month at fifteen is a valuable lesson. Running out at thirty five, with rent and kids, is much more
painful.""",
"""Teach it this week. If your child is old enough, give them responsibility for one category, like clothes or
entertainment, with a fixed monthly amount. Let them plan and make mistakes. For yourself, write a one page plan for
next month's money.""",
"Teenager with budget notebook", "A PLAN FOR YOUR MONEY",
"Teen shopping with cash", "PRACTICE WITH SMALL MONEY",
"Monthly budget on paper", "ONE CATEGORY")

item(8, "Understanding a paycheck", "gross vs net",
"""Lesson number eight. What you earn isn't what you take home.""",
"""Many young adults are shocked by their first paycheck. The salary was one number, but the deposit was much
smaller. Federal income tax, Social Security, Medicare, maybe state tax, health insurance and retirement
contributions all come out first. Wealthy parents often walk their kids through a real pay stub before that first
job.""",
"""Understanding gross versus net pay changes how young people budget, and how they think about job offers.
It also introduces taxes, which play a huge role in wealth building. Kids who learn early that tax advantaged
accounts exist often start using them much sooner.""",
"""Teach it this week. Show your teenager one of your pay stubs, or a sample one online, and go line by line.
What is each deduction? Where does it go? For yourself, check whether you're getting the full employer match on
your retirement plan.""",
"Pay stub close up", "GROSS VS NET",
"Young worker opening paycheck", "THE FIRST PAYCHECK SURPRISE",
"Parent explaining document to teen", "GO LINE BY LINE")

item(9, "Owning vs renting", "be an owner",
"""Lesson number nine. Owners build wealth. Customers pay for it.""",
"""When a kid buys a video game, they're a customer of that company. When they own shares of that company, they
share in its profits. Wealthy families often teach this distinction early. They point out that broad index funds
let ordinary people own small pieces of hundreds of companies.""",
"""Some parents buy a single share of a company their child loves, so the child can follow it and feel what it's
like to be an owner. The goal isn't stock picking. It's understanding that you can be on the earning side of the
economy, not just the spending side.""",
"""Teach it this week. Pick a few companies whose products your family uses every day. Look up their stock
prices together and talk about what it means to own a piece of them. For yourself, ask what you own that
generates income or growth.""",
"Kids playing video games", "CUSTOMER OR OWNER?",
"Stock certificate concept", "OWN A PIECE",
"Family looking at stock app", "COMPANIES YOU USE")

ch("The money talk most families skip")
sc("""Before we move on, let's talk about why these number lessons so often get skipped. In surveys by T. Rowe
Price, many parents have said they feel uncomfortable talking about money with their kids. Some feel they don't
know enough. Others were raised to think money talk is impolite. Some don't want to worry their children.""",
   "Parent hesitating at table", "THE SKIPPED TALK")
sc("""But silence teaches too. When parents never talk about money, kids still learn from what they see. They
see the new car, the shopping bags, the stress when a bill arrives. Without explanations, they fill in the
blanks themselves, and often draw the wrong conclusions.""",
   "Child watching parents argue", "SILENCE TEACHES TOO")
sc("""You don't need to be an expert to have these conversations. You just need to be honest. Saying I made a
mistake with credit cards when I was young, and here's what I learned, can be one of the most valuable lessons a
child ever hears. Your mistakes are free tuition for your kids.""",
   "Parent and teen talking honestly", "YOUR MISTAKES ARE THEIR TUITION")

pr("""That's angle one. Money is earned, save first, compound interest, interest on debt, price versus value,
opportunity cost, budgeting, paychecks and ownership. Now angle two. The psychology. Because knowing the math
isn't enough. The attitudes are what really get passed down.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
sc("""The most important money lessons often aren't about numbers at all. They're about patience, comparison,
security and what it means to have enough. Rich parents who raise financially healthy kids tend to focus as much
on these attitudes as on the math.""",
   "Parent and child walking together", "ATTITUDES MATTER MORE")

item(10, "Wait for what you want", "delayed gratification",
"""Lesson number ten. Learning to wait.""",
"""When kids want something, wealthy parents often don't just buy it. They help the child save for it. Waiting
weeks or months for a toy teaches patience, planning and the satisfaction of earning something. It's the
childhood version of saving for a house or retirement.""",
"""The famous marshmallow studies suggested that children who could wait for a bigger reward did better later in
life. Newer research has added nuance, showing family circumstances matter a lot. But the skill of waiting is still
something families can practice together.""",
"""Teach it this week. Next time your child asks for something, make a savings chart and help them track their
progress toward it. For yourself, try a thirty day wait before any non essential purchase over a hundred dollars.""",
"Child looking at toy in store window", "LEARNING TO WAIT",
"Marshmallow on plate", "THE MARSHMALLOW TEST",
"Savings chart on fridge", "TRACK THE PROGRESS")

item(11, "Don't compare", "someone always has more",
"""Lesson number eleven. Someone will always have more.""",
"""Kids notice what their friends have. The newer phone, the bigger house, the cooler shoes. Wealthy parents
often teach that comparison is a trap, because there's always someone with more. They focus their kids on their
own goals instead.""",
"""Many quiet millionaires model this themselves. They live in modest homes and drive ordinary cars, even when
they could afford more. Their kids learn that you don't need to show your wealth to have it.""",
"""Teach it this week. When your child compares themselves with a friend, ask, what do you actually want, and
why? For yourself, unfollow a few accounts that make you feel like you need more.""",
"Kids comparing phones", "SOMEONE ALWAYS HAS MORE",
"Modest family home", "NO NEED TO SHOW IT",
"Person unfollowing on phone", "FOCUS ON YOUR GOALS")

item(12, "Money isn't a secret", "talk about it",
"""Lesson number twelve. Money is something families talk about.""",
"""In many wealthy families, money is a normal topic. Kids hear their parents discuss investments, budgets and
decisions. They learn the vocabulary early. Words like interest, dividend, net worth and budget feel familiar, not
intimidating.""",
"""Talking about money doesn't mean sharing every detail or burdening kids with adult worries. It means
explaining decisions in age appropriate ways. We're not buying a new car because we'd rather save for your
college. That one sentence teaches more than a semester of lectures.""",
"""Teach it this week. At dinner, explain one money decision your family made recently, and why. For yourself,
have one honest money conversation with a partner or friend.""",
"Family dinner conversation", "A NORMAL TOPIC",
"Parent explaining to child", "AGE APPROPRIATE",
"Couple talking money at table", "ONE HONEST CONVERSATION")

item(13, "Small mistakes are cheap tuition", "let them fail early",
"""Lesson number thirteen. Let them make small mistakes now.""",
"""Some of the best money lessons come from mistakes. Spending a whole allowance on the first day and having
nothing left for the weekend. Buying a toy that breaks in a week. Wealthy parents often resist the urge to rescue
kids from these small mistakes.""",
"""A twenty dollar mistake at ten is far cheaper than a twenty thousand dollar mistake at thirty. When kids
experience the consequences of money choices while the stakes are small, they build judgment that protects them
later.""",
"""Teach it this week. Next time your child makes a money mistake, don't fix it. Ask what they learned and what
they'd do differently. For yourself, write down your biggest money mistake and the lesson it taught you.""",
"Broken toy on floor", "A CHEAP LESSON",
"Child thinking about choice", "LET THEM FAIL SMALL",
"Notebook with lessons learned", "WHAT DID YOU LEARN?")

item(14, "Enough is a number", "the finish line",
"""Lesson number fourteen. Knowing what's enough.""",
"""Some wealthy families talk openly about the idea of enough. Without a sense of enough, no amount of money ever
feels like it's sufficient. There's always a bigger house, a nicer car, a better vacation. With it, people can
enjoy what they have and make clearer choices.""",
"""Teaching kids about enough helps them resist endless consumption, and protects them from feeling poor no
matter how much they earn. It's one of the most valuable gifts a parent can give.""",
"""Teach it this week. Ask your child, what would be enough for you? A toy, a phone, a room? Talk about how it
feels to have enough. For yourself, write down what enough looks like for your family.""",
"Peaceful family at home", "ENOUGH",
"Endless shopping aisle", "THERE'S ALWAYS MORE",
"Written list on notebook", "WHAT IS ENOUGH?")

body_hook = "Your kids are watching how you treat money. Here's the lesson."
item(15, "Money is a tool", "not a scoreboard",
"""Lesson number fifteen. Money is a tool, not a measure of a person.""",
"""Rich parents who raise grounded kids often teach that money doesn't make someone better or worse. It's a tool
for security, freedom and helping others. Kids who see money as a scoreboard can grow up anxious or arrogant. Kids
who see it as a tool tend to use it more wisely.""",
"""This lesson shows up in how parents talk about others. Do they admire people for their cars, or for their
character? Kids notice. And they absorb those values far more from watching than from listening.""",
"""Teach it this week. Point out someone you admire for their kindness, work ethic or generosity, not their
wealth. For yourself, notice when you judge people by what they own.""",
"Toolbox with tools", "A TOOL",
"Person helping neighbor", "CHARACTER OVER CARS",
"Volunteer helping community", "WHO DO YOU ADMIRE?")

pr("""Let me pause for a second. If you're finding this useful, whether you're a parent or just learning these
lessons for yourself, please subscribe to Ryan Rover Money. It's free and it helps the channel reach more
families. Now, lesson sixteen.""")

item(16, "Generosity", "give some away",
"""Lesson number sixteen. Give some of it away.""",
"""Many wealthy families make giving part of their money system from the very beginning. Remember the three jars.
Save, spend and give. Kids learn that money can help others, and that generosity is part of a good life. Stanley
found that many millionaires gave regularly to causes they cared about.""",
"""Giving also changes how kids see their own money. It builds gratitude and perspective. And research on
happiness has found that spending money on others can make people happier than spending it on themselves.""",
"""Teach it this week. Let your child choose a cause for their give jar. A local animal shelter, a food bank, a
friend in need. For yourself, set a small regular giving amount, even five dollars a month.""",
"Child donating at food bank", "GIVE SOME AWAY",
"Volunteers sorting donations", "GRATITUDE AND PERSPECTIVE",
"Donation jar at shelter", "CHOOSE A CAUSE")

item(17, "Wealth is quiet", "don't show it off",
"""Lesson number seventeen. Real wealth is usually quiet.""",
"""Many wealthy parents teach their kids not to talk about money outside the family, and not to show it off.
It's partly about safety, and partly about values. They don't want their kids to feel superior, or to be targets
for people who want something from them.""",
"""This lesson also helps kids understand that the flashy people they see online aren't necessarily rich. As
Morgan Housel wrote in The Psychology of Money, wealth is what you don't see. It's the money not spent.""",
"""Teach it this week. Talk with your kids about why it's wise to keep family finances private. For yourself,
notice the difference between people who look rich and people who are financially secure.""",
"Quiet suburban street", "WEALTH IS QUIET",
"Flashy car social media post", "WHAT YOU DON'T SEE",
"Family privacy concept", "KEEP IT PRIVATE")

ch("How kids really learn: watching, not listening")
sc("""Here's the hardest truth for parents. Kids learn far more from what you do than from what you say. You can
explain compound interest perfectly, but if you buy everything on impulse, that's the lesson they'll keep. The
Cambridge research found that kids pick up money habits largely by watching the adults around them.""",
   "Child watching parent shopping", "WATCHING, NOT LISTENING")
sc("""That's actually good news. It means you don't need perfect lessons. You need to model the behavior. Let
them see you compare prices, say no to an impulse buy, put money into savings, and give to others. Narrate your
decisions out loud sometimes. I'd like that, but I'm going to wait and think about it.""",
   "Parent comparing prices in store", "MODEL THE BEHAVIOR")
sc("""And if your own money habits aren't where you want them, the best lesson might be letting kids watch you
improve. Seeing a parent pay off debt, build savings and stick to a plan teaches resilience, and that it's never
too late to change.""",
   "Parent celebrating debt payoff", "LET THEM WATCH YOU IMPROVE")

pr("""That's angle two. Waiting, not comparing, open money talk, small mistakes, enough, money as a tool,
generosity and quiet wealth. Now angle three. The playbook. Eight practical tools wealthy parents use to give
their kids a real financial head start.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
sc("""The playbook lessons are where wealthy families often pull ahead. Not because they have secret tools, but
because they know these tools exist and use them early. Most of them are available to any family.""",
   "Toolbox open on table", "THE TOOLS")

body_hook = "A teenager with a summer job can open this account."
item(18, "Open accounts early", "custodial and Roth IRAs",
"""Lesson number eighteen. Open accounts early.""",
"""Many wealthy parents open savings and investment accounts for their kids. Custodial accounts let parents
invest on a child's behalf. And if a child has earned income, from a job or babysitting, for example, they may be
able to contribute to a custodial Roth IRA, up to the amount they earned or the annual limit, whichever is lower.
Check the current IRS rules.""",
"""A Roth IRA started in the teenage years has decades of potential tax free growth ahead of it. Even a few
thousand dollars invested at fifteen can grow significantly by retirement. Some parents even match their kids'
contributions, like an employer match.""",
"""Teach it this week. If your teenager has a job, research custodial Roth IRA options with a brokerage. Consider
matching part of what they contribute. For yourself, make sure you're using your own tax advantaged accounts.""",
"Teen opening bank account with parent", "START EARLY",
"Roth IRA paperwork", "DECADES OF GROWTH",
"Parent and teen on laptop", "MATCH THEIR SAVINGS")

item(19, "Credit basics", "build it before you need it",
"""Lesson number nineteen. Understand credit before you need it.""",
"""A credit score affects the interest rate on car loans and mortgages, and sometimes rental applications and
insurance prices. Wealthy parents often explain how credit scores work before their kids leave home. Pay on time,
keep balances low, and don't open too many accounts at once.""",
"""Some parents add their teenager as an authorized user on a card they manage responsibly. Depending on the card
issuer, this can help the child start a credit history. Others help their young adult open a secured card and use
it for one small bill paid in full every month.""",
"""Teach it this week. Show your teen what a credit score is and pull your own free credit report together at
annualcreditreport.com. For yourself, set every card to autopay at least the minimum, so you're never late.""",
"Credit score on phone", "BUILD IT EARLY",
"Parent and teen with credit card", "AUTHORIZED USER",
"Credit report on laptop", "CHECK YOUR REPORT")

item(20, "Negotiate", "the first number isn't final",
"""Lesson number twenty. You can ask for a better deal.""",
"""Wealthy parents often let their kids watch them negotiate, whether it's a car price, a phone bill, or a
contract. Kids learn that the first number isn't always final, and that a polite question can save real money.""",
"""Negotiation is also a career skill. Research has shown that starting salaries affect a lifetime of earnings,
because raises are often based on what you already make. Young people who negotiate their first salary can
benefit for years.""",
"""Teach it this week. Let your kids listen while you call to ask for a lower rate on a bill. Talk afterward about
what worked. For yourself, research the salary range for your role before your next review.""",
"Business negotiation handshake", "THE FIRST NUMBER ISN'T FINAL",
"Parent on phone with child listening", "LET THEM WATCH",
"Salary research on laptop", "KNOW YOUR WORTH")

item(21, "Protect what you have", "insurance basics",
"""Lesson number twenty one. Protect what you build.""",
"""Rich families tend to understand insurance. Not insuring everything, but protecting against disasters that
would be financially devastating. Health insurance, car insurance, renters or homeowners insurance, and life
insurance when others depend on you.""",
"""Young adults often skip renters insurance or choose the bare minimum car coverage to save money. Then one
accident or theft sets them back years. Teaching kids how insurance works before they leave home can prevent that.""",
"""Teach it this week. Walk your teen through your car or home insurance policy. What does it cover? What's a
deductible? For yourself, check that your coverage still fits your life.""",
"Insurance documents on desk", "PROTECT WHAT YOU BUILD",
"Car accident scene", "ONE ACCIDENT",
"Parent explaining insurance to teen", "WHAT'S A DEDUCTIBLE?")

item(22, "Start something", "the lemonade stand lesson",
"""Lesson number twenty two. Try starting something of your own.""",
"""Many self made millionaires started small businesses as kids. Lemonade stands, lawn mowing, selling crafts,
reselling items online. Stanley found that many millionaires were business owners. Early entrepreneurship teaches
pricing, customer service, costs and profit.""",
"""Even a tiny business teaches lessons a classroom can't. What happens when you price too high? Too low? What
are your costs? What did you actually make after expenses? Those questions build business thinking that lasts a
lifetime.""",
"""Teach it this week. Help your child start a tiny business, even for one weekend. Track costs, sales and profit
together. For yourself, consider one skill you could turn into a small side income.""",
"Kids lemonade stand", "THE LEMONADE STAND",
"Teen mowing lawn for money", "COSTS AND PROFIT",
"Child counting money from sales", "TRACK THE PROFIT")

body_hook = "Teach your kids these three questions before they get scammed."
item(23, "Spot scams", "if it sounds too good",
"""Lesson number twenty three. If it sounds too good to be true, it probably is.""",
"""Scams target every age, including teenagers and young adults, often through social media, gaming platforms and
texts. The Federal Trade Commission has reported that younger adults report losing money to fraud more often than
older adults in some categories, even if older adults tend to lose larger amounts.""",
"""Wealthy parents teach kids to be skeptical of guaranteed returns, urgent deadlines, requests for gift cards,
and anyone asking for passwords or codes. These red flags apply to almost every scam.""",
"""Teach it this week. Share three questions with your kids. Is someone rushing me? Are they asking for gift cards,
crypto or codes? Does it promise easy money? If yes to any, stop and ask a parent. For yourself, use the same
questions.""",
"Scam warning on phone", "TOO GOOD TO BE TRUE",
"Teen on phone suspicious message", "RED FLAGS",
"Gift cards on table", "THREE QUESTIONS")

item(24, "The family plan", "wills and beneficiaries",
"""Lesson number twenty four. Have a plan for the family.""",
"""Wealthy families usually have wills, named beneficiaries on accounts, and sometimes trusts. Many explain the
basics to their kids as they grow up, so the next generation understands how wealth is protected and passed on.""",
"""Every family can do the basics. A will, beneficiaries on retirement accounts and life insurance, and a plan for
who would care for young children. These aren't just for the rich. They protect any family from confusion and
conflict.""",
"""Teach it this week. If your kids are older, explain in simple terms what a will is and why it matters. For
yourself, check the beneficiaries on every account you have.""",
"Family lawyer office", "THE FAMILY PLAN",
"Will document and pen", "NOT JUST FOR THE RICH",
"Beneficiary form", "CHECK YOUR BENEFICIARIES")

item(25, "Not everything is handed over", "independence is the gift",
"""And lesson number twenty five. Rich parents don't give their kids everything.""",
"""This one surprises people. In The Millionaire Next Door, Stanley described what he called economic outpatient
care, the substantial financial gifts some parents give to their adult children. His research suggested that
adult children who received large ongoing gifts often accumulated less wealth than similar people who didn't.""",
"""The lesson many wealthy parents take from this is that independence is the real gift. They help with
education or a first home, perhaps, but they don't fund an entire lifestyle. They want their kids to know how to
earn, save and build on their own.""",
"""Teach it this week. Think about one thing you do for your child that they could learn to do themselves, with
money or otherwise. Hand it over, with support. For yourself, ask whether you depend on help that's holding you back.""",
"Young adult moving into apartment", "INDEPENDENCE IS THE GIFT",
"The Millionaire Next Door book", "ECONOMIC OUTPATIENT CARE",
"Parent hugging adult child", "HELP, DON'T FUND")

# ---------------- Ages ----------------
ch("What to teach at every age")
sc("""Let's put this into a simple timeline. Ages three to five. Coins and counting, the idea that things cost
money, and that you sometimes have to wait. Ages six to ten. The three jars, small savings goals, and the
difference between needs and wants. Ages eleven to thirteen. An allowance with real responsibilities, comparison
shopping, and compound interest.""",
   "Young children counting coins", "AGES 3 TO 13")
sc("""Ages fourteen to eighteen. A first job, reading a pay stub, a first bank account and debit card, a custodial
Roth IRA if they have earned income, how credit works, and scams. Ages eighteen and up. Budgeting on their own,
building credit responsibly, choosing insurance, using an employer retirement plan from their very first job, and
taking full responsibility for their own money.""",
   "Teenager at first job", "AGES 14 AND UP")

# ---------------- Never learned ----------------
ch("If nobody taught you")
sc("""Maybe you're watching this and thinking, nobody taught me any of this. You're not alone. A growing number
of states now require a personal finance course in high school, but for most adults today, that came too late.
Most people learned by trial and error.""",
   "Adult studying at night", "IF NOBODY TAUGHT YOU")
sc("""The good news is that every one of these twenty five lessons works for adults too. Start with three jars of
your own, as automatic transfers. Learn compound interest with a calculator. Check your credit report. Open a
retirement account if you haven't. It's never too late to give yourself the money education you didn't get.""",
   "Adult opening investment account", "IT'S NEVER TOO LATE")
sc("""And if you do have kids, nieces, nephews or grandkids, you can break the cycle. The lessons you learn now can
become the kitchen table conversations that change your family's future for generations.""",
   "Grandparent with grandchild", "BREAK THE CYCLE")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. Should allowance be tied to chores? Families disagree on this. Some pay for all chores, some
give an allowance for learning money skills and expect basic chores as part of being in a family, with extra paid
jobs available. Either way, the key is consistency and using the money to teach.""",
   "Child doing dishes", "ALLOWANCE AND CHORES")
sc("""Question two. How much should I tell my kids about our family's finances? Share values and decisions,
adjusted for their age. You don't need to share exact salaries with young children, but older teens can benefit
from understanding real numbers, like how much the family spends on groceries or housing.""",
   "Parent and teen talking at table", "HOW MUCH TO SHARE")
sc("""Question three. What if I'm not good with money myself? Then learn together. Watching a parent learn and
improve is a powerful lesson. You don't need to be perfect. You need to be honest and willing to grow.""",
   "Parent and child reading together", "LEARN TOGETHER")
sc("""Question four. When should my child get a debit card or a credit card? Many families start with a debit
card linked to a teen account around the early teenage years, with parental controls. A credit card usually comes
later, often as an authorized user first, and then their own card in early adulthood, used for small purchases paid
in full every month. The goal is practice with guardrails before the stakes are high.""",
   "Teen with debit card at store", "DEBIT OR CREDIT CARD?")
sc("""Question five. Should I pay for my kids' college? That's a personal choice, and many families help in some
way. But many financial planners suggest prioritizing your own retirement savings first, because students can borrow
or earn scholarships for college, but nobody lends you money for retirement. A five twenty nine plan is one
tax advantaged way to save for education if you have room in your budget.""",
   "Graduation caps in the air", "PAYING FOR COLLEGE")

# ---------------- Recap ----------------
ch("Recap: all 25 lessons")
sc("""Quick recap. Angle one, the numbers. Money is earned, save first, compound interest, interest works both
ways, price versus value, opportunity cost, budgeting with an allowance, understanding a paycheck, and owning versus
renting.""",
   "Checklist on clipboard", "THE NUMBERS: 1 TO 9")
sc("""Angle two, the psychology. Wait for what you want, don't compare, money isn't a secret, small mistakes are
cheap tuition, enough is a number, money is a tool, generosity, and wealth is quiet.""",
   "Person thinking at window", "THE PSYCHOLOGY: 10 TO 17")
sc("""Angle three, the playbook. Open accounts early, credit basics, negotiate, protect what you have, start
something, spot scams, the family plan, and not everything is handed over.""",
   "Notebook with plan", "THE PLAYBOOK: 18 TO 25")

# ---------------- Close ----------------
ch("What to do next")
pr("""The best inheritance isn't money. It's knowing how money works. Pick one lesson from each angle and share it
with someone you love this week. If you want the full plan, it's in my playbook, linked in the description. And
tell me in the comments, what's one money lesson you wish someone had taught you as a kid? I'm Ryan Rover. See you
in the next one.""")

save("video27", "25 Money Lessons Rich Parents Teach Their Kids", [
    "Whitebread and Bingham, University of Cambridge, Habit Formation and Learning in Young Children (Money Advice Service, 2013)",
    "T. Rowe Price, Parents, Kids & Money Survey",
    "Thomas J. Stanley and William D. Danko, The Millionaire Next Door (1996): economic outpatient care",
    "Federal Reserve, G.19 Consumer Credit (credit card rates above 20%)",
    "IRS, Roth IRA eligibility (earned income) and contribution limits",
    "Federal Trade Commission, Consumer Sentinel data by age",
    "Morgan Housel, The Psychology of Money (2020); Dunn, Aknin and Norton, Spending Money on Others Promotes Happiness (Science, 2008)",
    "Next Gen Personal Finance, state personal finance graduation requirements",
    "Growth example: monthly compounding at 7% average yearly return (illustration, not a promise)",
], "25 money lessons rich parents teach their kids, from 3 angles: numbers, psychology, playbook")
