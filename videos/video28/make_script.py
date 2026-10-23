import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save, short

body_hook = None  # set right before item() to start a Short at its first explained scene

def item(n, title, sub, card_text, body, example, fix, q1, c1, q2, c2, q3, c3):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"TRAP {n}")
    global body_hook
    if body_hook:
        short(body_hook); body_hook = None
    sc(body, q1, c1)
    sc(example, q2, c2)
    sc(fix, q3, c3)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. Here's something most money advice gets wrong. It assumes people are broke because
they don't know the right information. Spend less than you earn. Avoid debt. Invest early. We all know that. And
yet millions of smart, hardworking people still struggle. Why? Because the problem usually isn't knowledge. It's
psychology. Your brain has built in shortcuts that work great for everyday life, and terribly for money. Today,
twenty of those mental traps, and how to escape each one.""")
short("Being broke is not a math problem. It's a brain problem.")
card("""Here's a study that changes how you think about being broke. Researchers published in the journal Science
found that the same farmers in India scored noticeably worse on cognitive tests before harvest, when money was
tight, than after harvest, when they had been paid.""",
     {"type": "stat", "label": "same people, worse test scores when money was tight", "big": "Before vs after harvest", "sub": "Mani, Mullainathan, Shafir and Zhao, Science, 2013"})
sc("""Think about what that means. The same people, with the same intelligence, performed worse on mental tests
simply because they were worried about money. The researchers argued that financial stress takes up mental
bandwidth, leaving less room for careful thinking. In other words, being broke doesn't just come from bad
decisions. It can also cause them. That's one of the most important ideas in this entire video, and it's why
willpower alone so often fails.""",
   "Farmer in field at harvest", "MONEY STRESS USES BANDWIDTH")
sc("""We'll go through these twenty traps from three angles. First, the numbers. The ways our brains get money
math wrong, from big interest rates to tiny purchases. Second, the psychology. The emotional traps around fear,
comparison and avoidance. And third, the playbook. The habits of mind that keep us stuck, along with the
research backed tools that actually work to get unstuck. None of this is about blaming anyone. It's about
understanding the machine between your ears, so you can work with it instead of against it.""",
   "Brain illustration with gears", "THREE ANGLES")
pr("""Let's begin with the numbers, and a trap that costs people money every single time they shop.""")

# ---------------- Sources ----------------
ch("How we got the research")
sc("""Our sources are published research in behavioral economics and psychology. Work by Nobel Prize winners Daniel
Kahneman and Richard Thaler, research by Sendhil Mullainathan and Eldar Shafir on scarcity, studies by Drazen Prelec,
Dan Ariely, Brigitte Madrian and others. I'll name each study as we go. Some famous psychology findings have had
trouble replicating, so I've focused on well established ones, and I'll flag uncertainty where it exists. Growth
examples use a stated seven percent average yearly return, an illustration, not a promise. This is education, not
financial advice.""",
   "Academic journals on shelf", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. Seven ways your brain gets money math wrong, often without you noticing.""")

item(1, "Anchoring", "the first number wins",
"""Trap number one. Anchoring. The first number you see shapes every number after it.""",
"""In a famous experiment, Amos Tversky and Daniel Kahneman spun a wheel of fortune that landed on either a low
or a high number, then asked people to estimate a completely unrelated quantity. People who saw the higher number
gave much higher estimates. A random number, with no connection to the question, pulled their answers. That's
anchoring, and stores, car dealers and salespeople use it every day.""",
"""Think of the original price crossed out next to the sale price. Or the expensive model placed beside the one
the store really wants you to buy. Or the car's sticker price that makes the negotiated price feel like a win. The
anchor makes a high price seem reasonable, even when it isn't. You leave feeling you saved money, when you may have
simply spent less than an inflated starting point.""",
"""Escape it. Before you shop, decide your own number, based on your budget and research, and write it down. Ignore
the crossed out price completely. Ask yourself, would I pay this if I had never seen the original price? If not,
it's not a deal. It's an anchor.""",
"Wheel of fortune spinning", "THE FIRST NUMBER WINS",
"Sale price tag with crossed out price", "THE CROSSED OUT PRICE",
"Shopping list with budget", "SET YOUR OWN NUMBER")

item(2, "Mental accounting", "not all dollars feel equal",
"""Trap number two. Mental accounting. Treating some dollars as less real than others.""",
"""Richard Thaler, who won the Nobel Prize in economics, described how people put money into mental buckets. Money
from a paycheck feels serious. Money from a tax refund, a bonus or a casino win feels like play money. Rationally,
every dollar is the same. But emotionally, we spend found money much more easily.""",
"""This is why tax refunds often disappear quickly, and why people can keep money in a low interest savings
account while carrying a credit card balance at twenty percent. The savings bucket feels untouchable, while the
debt bucket feels separate. In reality, using the savings to pay off the expensive debt, while keeping an emergency
cushion, would often leave them much better off.""",
"""Escape it. Treat every dollar as the same dollar. Before a windfall arrives, decide in writing exactly where it
will go. And look at your whole financial picture at once, savings and debts together, so the buckets don't trick
you.""",
"Labeled buckets with coins", "MENTAL BUCKETS",
"Tax refund check", "PLAY MONEY",
"Notebook with full financial picture", "ONE DOLLAR IS ONE DOLLAR")

item(3, "Present bias", "now beats later, every time",
"""Trap number three. Present bias. Today always feels more important than tomorrow.""",
"""Economists have shown that people value rewards now far more than rewards later, even when the later reward is
much bigger. Ask people whether they want one hundred dollars today or one hundred ten dollars in a week, and many
take the money now. But ask about one hundred dollars in a year versus one hundred ten in a year and a week, and
most will wait. The extra week is the same, but the present pulls harder.""",
"""With money, present bias is why saving for retirement feels so hard. Retirement is decades away, and the
weekend is right here. It's also why buy now pay later and credit cards are so tempting. They let you enjoy the
present and push the cost into a future that feels abstract.""",
"""Escape it. Make the future feel real. Some research suggests that people who view age progressed photos of
themselves save more. You can also take the decision out of the present entirely, with automatic transfers that
happen before you can be tempted.""",
"Calendar today circled", "NOW BEATS LATER",
"Buy now pay later button on phone", "PUSHING COSTS TO THE FUTURE",
"Older person portrait", "MEET FUTURE YOU")

body_hook = "Most people can't picture how fast money grows. Can you?"
item(4, "Exponential growth bias", "we think in straight lines",
"""Trap number four. Exponential growth bias. We underestimate how fast things compound.""",
"""Economists Victor Stango and Jonathan Zinman studied what they called exponential growth bias. Most people
think of growth in straight lines, but compound interest grows in a curve. So people tend to underestimate how
quickly savings can grow over long periods, and how quickly debt can grow at high interest rates.""",
"""Here's an example. One hundred dollars a month at a seven percent average yearly return for forty years. Most
people guess well under one hundred thousand dollars. The actual result is roughly two hundred sixty thousand. On the
debt side, people underestimate how much a high interest balance grows when they only pay the minimum. The research
found that people with stronger exponential growth bias tended to borrow more and save less.""",
"""Escape it. Stop guessing. Use a compound interest calculator for both savings and debt. Seeing the actual curve,
on screen, is the best cure for straight line thinking.""",
"Exponential curve graph", "WE THINK IN STRAIGHT LINES",
"Calculator with growth chart", "THE ACTUAL CURVE",
"Online compound interest calculator", "STOP GUESSING")

card("""Here's that curve. One hundred dollars a month, for forty years, at a seven percent average yearly return,
grows to roughly two hundred sixty two thousand dollars. You'd put in forty eight thousand.""",
     {"type": "growth", "monthly": 100, "rate": 0.07, "years": 40})

item(5, "The sunk cost trap", "throwing good money after bad",
"""Trap number five. The sunk cost fallacy. Sticking with something because you've already paid for it.""",
"""Researchers Hal Arkes and Catherine Blumer showed that people often continue investing in something simply
because they've already put money into it, even when quitting would be better. Money that's already spent and can't
be recovered is a sunk cost. Rationally, it shouldn't affect future decisions. Emotionally, it does.""",
"""Think of repairing an old car again and again because you've already spent so much on it. Or holding a losing
investment because selling would make the loss feel real. Or finishing a meal you don't enjoy because you paid for
it. In each case, the past payment pushes you toward more spending, or more loss.""",
"""Escape it. When making a decision, ask only about the future. Ignoring what I've already spent, what's the best
choice from here? If you were starting fresh today, would you choose this? If not, it may be time to let go.""",
"Old car in repair shop", "SUNK COST",
"Stock chart going down", "HOLDING A LOSER",
"Fresh start road sign", "ONLY THE FUTURE COUNTS")

item(6, "The pain of paying", "cards make spending painless",
"""Trap number six. Painless payments make you spend more.""",
"""Drazen Prelec and Duncan Simester ran a famous study where people bid on tickets to sold out basketball games.
Those told they had to pay by credit card were willing to pay substantially more, in some cases about double,
compared with those paying cash. Paying with cash creates a small feeling of pain. Cards, and especially tapping a
phone, remove most of it.""",
"""Today, almost everything is designed to remove that pain. One click checkout, saved cards, subscriptions that
renew automatically, tap to pay. Each one makes spending feel lighter, and more frequent. It's not that cards are
evil. It's that they quietly remove one of the brain's natural brakes.""",
"""Escape it. Add friction back. Delete saved cards from shopping sites. Use cash for categories where you tend to
overspend, like eating out. And check your card balance often, so the spending feels real again.""",
"Basketball arena crowd", "CARD BIDS WERE HIGHER",
"Tap to pay at checkout", "PAINLESS PAYMENT",
"Cash in wallet", "ADD FRICTION BACK")

item(7, "The power of free", "zero is a magic number",
"""Trap number seven. The word free makes us lose our judgment.""",
"""In experiments by Dan Ariely and colleagues, people chose between a fancy chocolate truffle for a small price
and a cheap chocolate for one cent. Many chose the truffle. But when both prices dropped by one cent, making the
cheap one free, people switched dramatically to the free one, even though the price difference stayed the same.
Zero isn't just a low price. It feels like a different category.""",
"""Businesses use this constantly. Free shipping if you spend thirty five dollars. Buy one, get one free. A free
trial that turns into a paid subscription. Free gifts with purchase. Often, the free part leads us to spend more than
we planned.""",
"""Escape it. When you see free, ask what it's costing you. Did you add items just to qualify for free shipping?
Will you remember to cancel that free trial? Put a reminder in your calendar the day you sign up for any trial.""",
"Chocolate truffles on plate", "THE MAGIC OF ZERO",
"Free shipping banner online", "FREE SHIPPING OVER $35",
"Calendar reminder cancel trial", "CANCEL BEFORE IT CHARGES")

ch("Why smart people fall for these")
sc("""You might think these traps only fool careless people. They don't. Kahneman described two systems of thinking.
System one is fast, automatic and emotional. System two is slow, careful and logical. Most daily decisions, including
most spending, run on system one. It's efficient, but it's also where these traps live.""",
   "Fast and slow road signs", "FAST AND SLOW THINKING")
sc("""Even experts fall for them when they're tired, rushed or emotional. That's why stores play music, use
countdown timers and put candy at the checkout. They're designed to catch system one when system two is off duty.
Being smart doesn't protect you. Being prepared does.""",
   "Checkout aisle with candy", "BUILT TO CATCH YOU")
sc("""The solution isn't to try harder in every moment. Nobody can think carefully about every purchase. The
solution is to make a few big decisions in advance, when system two is awake, and let systems carry them out. That's
the theme you'll see again and again in the playbook.""",
   "Planning at desk calmly", "DECIDE IN ADVANCE")

pr("""That's angle one. Anchoring, mental accounting, present bias, exponential growth bias, sunk costs, painless
payments and the power of free. Now angle two. The psychology. These traps are more emotional, and in many ways more
powerful.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
sc("""The emotional traps are about fear, shame, comparison and hope. They explain why people avoid looking at
their accounts, keep up with friends they can't afford to keep up with, and expect things to get better on their
own. They're deeply human, and recognizing them is the first step to escaping them.""",
   "Person sitting alone thinking", "THE EMOTIONAL TRAPS")

body_hook = "When money is tight, your brain literally works differently."
item(8, "The scarcity tunnel", "money stress narrows your focus",
"""Trap number eight. The scarcity tunnel.""",
"""In their book Scarcity, Sendhil Mullainathan and Eldar Shafir described how running short of money creates
tunnel vision. When you're worried about this month's rent, it's very hard to think about retirement, or even next
month. The urgent crowds out the important.""",
"""This is why payday loans and high interest credit can seem reasonable in the moment. They solve the problem
inside the tunnel, today's bill, while creating a bigger problem outside it. It's not a lack of intelligence. It's
what scarcity does to anyone's thinking.""",
"""Escape it. Build even a small buffer, a few hundred dollars, as fast as you can. Many people find that even a
small cushion widens the tunnel. And make important long term decisions, like setting up retirement contributions,
during calmer moments, so they run automatically when stress returns.""",
"Tunnel with light at end", "THE SCARCITY TUNNEL",
"Payday loan storefront", "SOLVING TODAY, HURTING TOMORROW",
"Small savings jar", "A SMALL BUFFER WIDENS IT")

item(9, "The ostrich effect", "not looking makes it worse",
"""Trap number nine. The ostrich effect. Avoiding information when you expect bad news.""",
"""Researchers George Loewenstein, Duane Seppi and Niklas Karlsson found that investors logged in to check their
accounts more often when markets were up, and less often when markets were down. People avoid information that
might make them feel bad. With money, that can mean unopened bills, unchecked balances and ignored debt.""",
"""The problem is that money problems grow in the dark. Fees pile up, fraud goes unnoticed, and debt compounds. By
the time people finally look, the problem is much bigger, which makes the next look even scarier.""",
"""Escape it. Make looking small and routine. Five minutes, once a week, same time, with a coffee. Open every
account, read every number, and close it. Familiarity shrinks fear. After a few weeks, most people find the weekly check takes less time and causes far less
anxiety than they expected.""",
"Ostrich head in sand", "THE OSTRICH EFFECT",
"Pile of unopened mail", "PROBLEMS GROW IN THE DARK",
"Coffee and laptop weekly check", "FIVE MINUTES A WEEK")

item(10, "Social comparison", "keeping up with the Joneses",
"""Trap number ten. Social comparison.""",
"""We judge our lives by comparing them with others. Researchers at the Federal Reserve Bank of Philadelphia found
that when someone in a neighborhood won the lottery, their neighbors were more likely to buy visible things like cars,
and later more likely to face financial distress. Seeing others spend makes us spend.""",
"""Social media turned this up to the maximum. You compare your everyday life with everyone else's highlight reel.
The vacation, the new kitchen, the car. You never see their credit card statements. And comparison is a game you can't
win, because there's always someone with more.""",
"""Escape it. Compare yourself with your past self instead. Are you better off than last year? Unfollow accounts that
make you feel poor. And remember, the people who look richest are often the most in debt.""",
"Neighbors new car in driveway", "THE JONESES",
"Social media highlight reel", "EVERYONE'S HIGHLIGHT REEL",
"Person journaling progress", "COMPARE WITH YOUR PAST SELF")

item(11, "Hedonic adaptation", "the thrill always fades",
"""Trap number eleven. Hedonic adaptation. We get used to everything.""",
"""A classic study by Philip Brickman and colleagues in nineteen seventy eight compared lottery winners with other
people and found that, after a while, the winners were not dramatically happier in everyday life. Psychologists call
this hedonic adaptation. We quickly get used to new things, and they stop making us happy.""",
"""That's why the new car, the bigger house or the upgraded phone feels amazing for a few weeks, and then just feels
normal. And then we want the next upgrade to recapture the thrill. That cycle, sometimes called the hedonic treadmill,
keeps people spending more without feeling any happier.""",
"""Escape it. Notice the fade. After your next big purchase, check in with yourself a month later. Is it still
exciting? Use that knowledge next time. And spend more on experiences and time with people, which research suggests
tends to bring longer lasting satisfaction.""",
"Lottery winner celebrating", "THE THRILL FADES",
"Treadmill at gym", "THE HEDONIC TREADMILL",
"Friends on a hike", "EXPERIENCES LAST LONGER")

pr("""Let me pause here for a moment. If this is helping you understand your own money behavior, please subscribe to
Ryan Rover Money. It's free and it helps more people find these videos. Okay, trap twelve, which explains why so many
people never change anything at all.""")

item(12, "Status quo bias", "doing nothing feels safe",
"""Trap number twelve. Status quo bias. We stick with whatever we already have.""",
"""People tend to stay with their current situation, even when switching would clearly help. The same bank with high
fees. The same insurance company every year. The same expensive phone plan. Changing feels like effort and risk, so we
don't.""",
"""Brigitte Madrian and Dennis Shea studied a company that switched its retirement plan to automatic enrollment.
Participation among new employees jumped dramatically, from well under half to the large majority. Nothing else
changed. People simply stuck with the default, whatever it was.""",
"""Escape it. Use status quo bias to your advantage. Set good defaults, like automatic savings and automatic bill
payments, so doing nothing means doing the right thing. And once a year, review your bank, insurance and phone plan, and
switch if there's a better option.""",
"Comfortable couch in living room", "DOING NOTHING FEELS SAFE",
"Retirement enrollment form", "THE POWER OF DEFAULTS",
"Automatic savings setup", "SET GOOD DEFAULTS")

item(13, "Optimism bias", "it won't happen to me",
"""Trap number thirteen. Optimism bias. Believing bad things happen to other people.""",
"""Neuroscientist Tali Sharot and other researchers have documented that most people tend to underestimate their
chances of bad events, like job loss, illness or accidents, and overestimate their chances of good events. Optimism
helps us get out of bed in the morning, but it can leave us unprepared.""",
"""With money, optimism bias is why people skip emergency funds, carry too little insurance, and assume their income
will keep rising. Most of the time things work out. But the times they don't can be financially devastating.""",
"""Escape it. Plan for the bad scenario while hoping for the good one. Build an emergency fund of three to six months
of expenses. Check your insurance for major gaps. Then you can stay optimistic, with a safety net underneath.""",
"Sunny optimistic person", "IT WON'T HAPPEN TO ME",
"Storm clouds over house", "WHEN IT DOES HAPPEN",
"Safety net concept", "PLAN FOR THE BAD CASE")

body_hook = "Losing a hundred dollars hurts twice as much as winning it."
item(14, "Loss aversion", "losses hurt twice as much",
"""Trap number fourteen. Loss aversion. Losing hurts more than winning feels good.""",
"""Kahneman and Tversky found that losses feel roughly twice as painful as equivalent gains feel good. Losing one
hundred dollars hurts more than finding one hundred dollars pleases. This shapes many money decisions, often in
unhelpful ways.""",
"""Loss aversion can make people panic sell investments during market drops, locking in losses. It can make them
avoid investing at all, keeping money in cash that slowly loses value to inflation. And it can make them hold losing
investments too long, hoping to avoid admitting a loss.""",
"""Escape it. Decide your plan before the market drops. Write down what you'll do in a crash, which for many long
term investors is to keep investing. And stop checking investments daily. The more often you look, the more often
you'll see losses.""",
"Person upset over loss", "LOSSES HURT MORE",
"Stock market falling screen", "PANIC SELLING",
"Investment plan written down", "DECIDE BEFORE THE DROP")

ch("The emotions behind money")
sc("""Underneath these traps are a few basic emotions. Fear, shame, envy and hope. Fear makes us avoid looking. Shame
makes us hide problems. Envy makes us compare and spend. Hope makes us believe things will sort themselves out. None of
these emotions are wrong. They're human. But left unexamined, they run our finances.""",
   "Faces showing different emotions", "FEAR, SHAME, ENVY, HOPE")
sc("""Surveys by the American Psychological Association have consistently found money to be one of the top sources
of stress for Americans. And stress, as we saw with the farmers study, makes good decisions harder. It becomes a cycle.
Money worries create stress, stress leads to worse decisions, and worse decisions create more money worries.""",
   "Stressed person with bills", "THE STRESS CYCLE")
sc("""Breaking that cycle usually starts with one small win. Paying off one card. Saving the first five hundred
dollars. Canceling three subscriptions. Small wins create relief, relief creates bandwidth, and bandwidth makes the next
good decision easier. Momentum is real. Many people who turned their finances around say the hardest part wasn't the math. It was
the first step, and the second one came much more easily.""",
   "Person celebrating small win", "ONE SMALL WIN")

pr("""That's angle two. The scarcity tunnel, the ostrich effect, social comparison, hedonic adaptation, status quo bias,
optimism bias and loss aversion. Now angle three. The playbook. Six traps about habits and identity, and the research
backed tools that help people escape them.""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
sc("""The good news about mental traps is that they're predictable. And anything predictable can be planned for.
Behavioral economists haven't just discovered the traps. They've also tested tools that help people avoid them. This
last group pairs each trap with its antidote.""",
   "Chess board strategy", "PREDICTABLE MEANS PLANNABLE")

item(15, "Decision fatigue", "too many choices drain you",
"""Trap number fifteen. Decision fatigue.""",
"""Every day you make hundreds of decisions, and many people find that their judgment gets worse as the day goes on.
That's one reason late night online shopping can be so tempting, and why people tend to grab convenience food after a
long day. Research on decision fatigue is debated, but the experience of being too tired to choose well is familiar to
almost everyone.""",
"""Stores and apps make it worse with endless options. Research by Sheena Iyengar and Mark Lepper suggested that too
many choices can make people less likely to choose at all, or less satisfied with what they choose. With money, too
many options can lead to doing nothing, or choosing badly.""",
"""Escape it. Reduce decisions. Plan meals for the week, so dinner isn't a nightly choice. Choose a simple investment,
like a broad low cost index fund or target date fund, so you're not constantly deciding. Avoid shopping when you're
tired.""",
"Tired person at night with phone", "DECISION FATIGUE",
"Supermarket aisle with many choices", "TOO MANY OPTIONS",
"Weekly meal plan on fridge", "REDUCE DECISIONS")

body_hook = "This simple trick tripled people's savings rates."
item(16, "No commitment device", "willpower runs out",
"""Trap number sixteen. Relying on willpower instead of commitment.""",
"""Richard Thaler and Shlomo Benartzi designed a program called Save More Tomorrow. Employees agreed in advance to
increase their retirement savings rate each time they got a raise. Because the increase happened in the future, and
came out of a raise rather than their current pay, it didn't feel like a loss. In the first company to use it,
participants' average savings rate rose from about three and a half percent to over thirteen percent in under four
years.""",
"""That's a commitment device. A decision made in advance that binds your future self. People who rely on willpower
alone tend to struggle, because willpower is weakest exactly when temptation is strongest. Commitment devices remove the
need for willpower in the moment.""",
"""Escape it. Commit in advance. Ask your employer whether your retirement plan offers automatic yearly increases, and
turn them on. Or set a calendar reminder to raise your savings rate by one percent every time you get a raise.""",
"Signing a commitment document", "SAVE MORE TOMORROW",
"Chart rising savings rate", "3.5% TO 13.6%",
"Calendar reminder raise savings", "COMMIT IN ADVANCE")

item(17, "A broke identity", "I'm just bad with money",
"""Trap number seventeen. A broke identity.""",
"""Many people carry a story about themselves. I'm bad with money. People like me don't invest. I'll never get ahead.
Psychologists have long noted that beliefs about ourselves shape our behavior. If you believe you're bad with money,
you're less likely to try, and more likely to give up after a setback.""",
"""Identities often come from childhood. What your parents said about money, how your family handled it, and what
happened around you. But identities aren't permanent. Many first generation millionaires grew up with very little and
built a new story about money.""",
"""Escape it. Change the sentence. Instead of I'm bad with money, try I'm learning to manage money. Then prove it to
yourself with one small action this week. Identity follows behavior. Every small win is a vote for the person you're
becoming.""",
"Person looking in mirror", "I'M JUST BAD WITH MONEY",
"Old family photographs", "WHERE THE STORY STARTED",
"Person writing new goals", "CHANGE THE SENTENCE")

item(18, "Learned helplessness", "why bother trying",
"""Trap number eighteen. Learned helplessness.""",
"""Psychologist Martin Seligman described learned helplessness, when people who repeatedly experience setbacks they
can't control stop trying, even when things become controllable. With money, after years of struggling, some people
simply stop believing their actions make a difference.""",
"""It's understandable. If every raise has been swallowed by rising costs, and every savings attempt has been wiped out
by an emergency, giving up can feel rational. But it often keeps people stuck long after opportunities have improved.""",
"""Escape it. Start with something you can fully control and complete quickly. Cancel one subscription. Call to remove
one fee. Save twenty dollars. Each small success proves that your actions matter. That proof is the antidote to
helplessness.""",
"Person sitting discouraged", "WHY BOTHER?",
"Rain on window", "YEARS OF SETBACKS",
"Checkmark on list", "PROVE YOUR ACTIONS MATTER")

item(19, "Planning fallacy", "everything takes longer and costs more",
"""Trap number nineteen. The planning fallacy.""",
"""Kahneman and Tversky described the planning fallacy, our tendency to underestimate how long things will take and how
much they'll cost, even when we've been wrong before. Renovations go over budget. Weddings cost more than planned.
Monthly budgets forget irregular expenses.""",
"""With money, the planning fallacy shows up in budgets that leave no room for irregular costs, like car repairs, gifts,
medical bills and annual subscriptions. Those surprises aren't really surprises. They're just expenses that don't
happen every month.""",
"""Escape it. Add a buffer to every plan. Many people add ten to twenty percent to project budgets. And create sinking
funds, separate savings for predictable irregular costs like car maintenance, holidays and insurance premiums.""",
"Construction over budget", "IT ALWAYS COSTS MORE",
"Calendar with irregular expenses", "NOT REALLY SURPRISES",
"Labeled savings jars sinking funds", "SINKING FUNDS")

item(20, "Going it alone", "shame keeps us silent",
"""And trap number twenty. Struggling in silence.""",
"""Money is still one of the most taboo topics in many families and friendships. People talk about health, relationships
and politics, but not their debts or salaries. Shame keeps money problems hidden, and hidden problems are harder to
solve.""",
"""When people do talk about money, with a partner, a friend, a counselor or a support group, they often find others
face the same struggles. Accountability also helps. Telling someone your goal makes you more likely to follow through.""",
"""Escape it. Find one person you trust to talk money with. Share one goal and one struggle. If debt feels
overwhelming, nonprofit credit counseling agencies can help. You don't have to figure it out alone.""",
"Person alone at kitchen table", "THE TABOO TOPIC",
"Friends talking over coffee", "YOU'RE NOT ALONE",
"Counselor office meeting", "FIND ONE PERSON")

# ---------------- A day of traps ----------------
ch("A day full of traps")
pr("""To see how these traps work together, let's follow one person through a single ordinary day.""")
sc("""Meet Sam. In the morning, Sam gets an email. Flash sale, forty percent off, ends at midnight. The original price
is crossed out, and the sale price suddenly looks cheap. That's anchoring and urgency working together. Sam adds a jacket
to the cart, and then two more items, because shipping is free over fifty dollars. That's the power of free.""",
   "Email notification flash sale", "MORNING: THE FLASH SALE")
sc("""At lunch, Sam taps a phone to pay for a meal that costs more than planned. It doesn't feel like spending, because
there's no cash leaving a wallet. That's the pain of paying, or rather, the lack of it. Later, a coworker shows off new
headphones. Sam starts browsing for a pair. That's social comparison.""",
   "Phone tap payment at cafe", "LUNCH: PAINLESS PAYMENT")
sc("""In the evening, Sam is tired after a long day. Cooking feels impossible, so dinner is delivered. That's decision
fatigue. A notification says the investment account is down this week. Sam doesn't open it. That's the ostrich effect.
And before bed, Sam thinks, I'll start saving next month, once things calm down. That's present bias and optimism bias in
one sentence.""",
   "Delivery food at night", "EVENING: TIRED CHOICES")
sc("""Sam isn't reckless or foolish. Sam is completely normal. Every one of those choices felt reasonable in the moment.
Now imagine that same day with a few systems in place. No saved card on shopping sites. Savings that move automatically on
payday. A meal plan for the week. Investment alerts turned off. The same person, the same brain, and a very different
result.""",
   "Calm person planning week", "SAME BRAIN, BETTER SYSTEMS")

# ---------------- How businesses use them ----------------
ch("How businesses use these traps")
sc("""Here's something worth knowing. Many of these traps are well understood by the companies that sell to you.
Retailers, apps and lenders employ people who study consumer behavior for a living. That doesn't make them villains, but
it does mean the playing field isn't level. Let's look at a few common designs, so you can spot them.""",
   "Marketing team meeting", "THE OTHER SIDE")
sc("""Countdown timers and limited time offers create urgency, which pushes decisions into fast, emotional thinking.
Subscription models rely on status quo bias, because many people never cancel. Free trials rely on the power of free and
on us forgetting the renewal date. Decoy pricing places an expensive option next to the one they want you to buy, which
makes it look reasonable by comparison. That's anchoring by design.""",
   "Countdown timer on website", "URGENCY AND DECOYS")
sc("""Buy now pay later services split a purchase into small payments, which plays on present bias and the pain of
paying. Loyalty points make spending feel like earning. And endless scrolling feeds are designed to keep you looking,
which means seeing more ads and more things other people have. None of this is secret. It's simply how modern selling
works.""",
   "Shopping app on phone", "SPLIT PAYMENTS AND POINTS")
sc("""Once you recognize these designs, they lose much of their power. A countdown timer becomes a signal to slow down,
not speed up. A free trial becomes a calendar reminder. A split payment becomes a total price you add up yourself.
Awareness won't make you immune, but it gives your careful system a chance to step in.""",
   "Person thinking before buying online", "AWARENESS GIVES YOU A CHANCE")

# ---------------- Toolkit ----------------
ch("Your anti trap toolkit")
pr("""Let's pull everything together into a simple toolkit. Five tools that beat most of these traps at once.""")
sc("""Tool one. Automate. Automatic savings, investments and bill payments beat present bias, status quo bias and
decision fatigue in one move. Tool two. Add friction to spending. Delete saved cards, use cash for problem categories,
and wait twenty four hours before non essential purchases. That beats the pain of paying, anchoring and the power of
free.""",
   "Automatic transfers on phone", "TOOLS 1 AND 2")
sc("""Tool three. Look regularly. A weekly five minute money check beats the ostrich effect and keeps optimism bias
honest. Tool four. Decide in advance. Write down your plan for windfalls, raises and market drops. That beats mental
accounting, loss aversion and the scarcity tunnel.""",
   "Weekly planner and coffee", "TOOLS 3 AND 4")
sc("""And tool five. Talk about it. A money buddy, a partner or a counselor beats shame, learned helplessness and the
broke identity. Five tools. Twenty traps. You don't have to win every battle with your brain. You just need a system
that wins most of them for you.""",
   "Two people shaking hands", "TOOL 5")

# ---------------- FAQ ----------------
ch("Questions people ask")
sc("""Question one. Are poor people just making bad choices? No. That's the key insight of scarcity research. Anyone,
regardless of intelligence, tends to make worse decisions under financial stress. The choices are a symptom as much as a
cause. That's why systems and buffers matter more than lectures.""",
   "Thoughtful person looking out window", "BAD CHOICES?")
sc("""Question two. Which trap is the most expensive? For many people, the combination of present bias and painless
payments, which leads to high interest credit card debt. Interest above twenty percent compounds quickly, and exponential
growth bias makes people underestimate how fast it grows.""",
   "Credit card debt statement", "THE MOST EXPENSIVE TRAP")
sc("""Question three. Can I really change how my brain works? You don't need to change your brain. You need to change
your environment. Automatic transfers, removed saved cards and a weekly check work with your brain as it is. That's why
they're so effective.""",
   "Organized desk environment", "CHANGE YOUR ENVIRONMENT")
sc("""Question four. Where should I start? Pick the trap that cost you the most last year. For many people, that's
debt or impulse spending. Choose one tool from the toolkit and apply it this week. Then add another next month.""",
   "Starting line on track", "WHERE TO START")
sc("""Question five. Do these traps affect rich people too? Absolutely. Wealthy people fall for anchoring, loss
aversion and social comparison as well. The difference is that many have built systems, like automatic investing and
advisors who enforce discipline, and they often have cushions that make mistakes less painful. Systems and buffers, not
superhuman willpower.""",
   "Business executive thinking", "RICH PEOPLE TOO?")
sc("""Question six. How do I help a partner or family member caught in these traps? Start with curiosity, not criticism.
Share what you've learned about the traps as something that affects everyone, including you. Then suggest one system you
could try together, like a weekly money check or automatic savings. People change more easily when they don't feel
judged.""",
   "Couple talking supportively", "HELPING SOMEONE ELSE")
sc("""Question seven. Is it bad to be optimistic about money? Not at all. Optimism keeps people investing for the long
term and trying again after setbacks. The trick is to pair optimism with preparation. Expect things to work out over time,
and still keep an emergency fund, insurance and a plan for bad years. Hopeful and prepared is the best combination.""",
   "Sunrise over hills hopeful", "OPTIMISTIC AND PREPARED")

# ---------------- Recap ----------------
ch("Recap: all 20 traps")
sc("""Quick recap. Angle one, the numbers. Anchoring, mental accounting, present bias, exponential growth bias, sunk
costs, the pain of paying, and the power of free.""",
   "Checklist on clipboard", "THE NUMBERS: 1 TO 7")
sc("""Angle two, the psychology. The scarcity tunnel, the ostrich effect, social comparison, hedonic adaptation, status
quo bias, optimism bias and loss aversion.""",
   "Person thinking at window", "THE PSYCHOLOGY: 8 TO 14")
sc("""Angle three, the playbook. Decision fatigue, relying on willpower instead of commitment, a broke identity, learned
helplessness, the planning fallacy, and struggling in silence.""",
   "Notebook with plan", "THE PLAYBOOK: 15 TO 20")

# ---------------- Close ----------------
ch("What to do next")
pr("""Remember the farmers from the beginning. Same people, same intelligence, different results, just because of
money stress. Being broke isn't a character flaw. It's often a brain doing exactly what brains do, in a world designed to take
advantage of it. Once you see the traps, you can build systems around them. If you want the full plan, it's in my
playbook, linked in the description. Tell me in the comments which trap you recognized in yourself. I'm Ryan Rover. See
you in the next one.""")

save("video28", "The Psychology of Being Broke: 20 Mental Traps", [
    "Mani, Mullainathan, Shafir and Zhao, Poverty Impedes Cognitive Function (Science, 2013); Mullainathan and Shafir, Scarcity (2013)",
    "Tversky and Kahneman, Judgment under Uncertainty: Heuristics and Biases (Science, 1974); Kahneman and Tversky, Prospect Theory (1979); Kahneman, Thinking, Fast and Slow (2011)",
    "Richard Thaler, mental accounting; Thaler and Benartzi, Save More Tomorrow (Journal of Political Economy, 2004)",
    "Stango and Zinman, Exponential Growth Bias and Household Finance (Journal of Finance, 2009)",
    "Arkes and Blumer, The Psychology of Sunk Cost (1985); Prelec and Simester, Always Leave Home Without It (Marketing Letters, 2001)",
    "Shampanier, Mazar and Ariely, Zero as a Special Price (Marketing Science, 2007)",
    "Karlsson, Loewenstein and Seppi, The Ostrich Effect (2009); Agarwal, Mikhed and Scholnick, Federal Reserve Bank of Philadelphia (lottery neighbors)",
    "Brickman, Coates and Janoff-Bulman, Lottery Winners and Accident Victims (1978); Tali Sharot, The Optimism Bias (2011)",
    "Madrian and Shea, The Power of Suggestion (Quarterly Journal of Economics, 2001); Iyengar and Lepper, When Choice is Demotivating (2000)",
    "Martin Seligman, learned helplessness; American Psychological Association, Stress in America",
    "Growth example: monthly compounding at 7% average yearly return (illustration, not a promise)",
], "the psychology of being broke, 20 mental traps from 3 angles: numbers, psychology, playbook")
