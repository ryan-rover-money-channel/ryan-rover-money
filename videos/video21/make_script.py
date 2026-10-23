import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "pipeline"))
from scriptkit import ch, sc, pr, card, save

def item(n, title, sub, card_text, body, example, q1, c1, q2, c2):
    ch(f"{n}. {title}")
    card(card_text, {"type": "list", "n": n, "title": title, "sub": sub}, f"NEVER BUY {n}")
    sc(body, q1, c1)
    sc(example, q2, c2)

# ---------------- Intro ----------------
ch("Intro")
pr("""Hi, I'm Ryan Rover. When people picture rich people, they picture them buying everything. The yacht,
the watch, the car with the doors that open upward. But when researchers actually sat down with American
millionaires and looked at their receipts, they found something strange. Most of them were quietly
refusing to buy the very things the rest of us think we need. Today, twenty of those things.""")
card("""Here's the number that started it all. In the book The Millionaire Next Door, researchers Thomas
Stanley and William Danko surveyed American millionaires. Most of them said they had never spent more than
three hundred ninety nine dollars on a suit.""",
     {"type": "stat", "label": "most millionaires never paid more than", "big": "$399", "sub": "for a suit (The Millionaire Next Door, 1996)"})
sc("""That book came out in nineteen ninety six, so prices have changed. But the pattern hasn't. Stanley
kept studying millionaires for years after, and the same picture showed up again and again. The typical
American millionaire is not a movie star or a tech founder. It's a business owner, a teacher, an engineer,
a manager. Someone who earned a good income and simply refused to spend it all.""",
   "Suburban house with lawn", "THE QUIET MILLIONAIRE")
sc("""And here's how this video works. We'll look at these twenty things from three angles. First, the
numbers. What these purchases really cost over time. Second, the psychology. Why normal people buy them,
and why rich people don't. And third, the playbook. What you can actually do differently, starting this
week. By the end, you'll see that being rich is often less about what you buy, and more about what you
refuse to buy.""",
   "Three paths in forest", "THREE ANGLES")
pr("""Let's start with the cold, hard numbers. And number one is a purchase almost every American makes,
usually more than once.""")

# ---------------- Sources ----------------
ch("How we got the numbers")
sc("""Every number in this video comes from a named source. Millionaire spending habits come from Thomas
Stanley's research, including The Millionaire Next Door and Stop Acting Rich. Car prices come from Kelley
Blue Book and Edmunds. Credit card rates come from the Federal Reserve. Growth examples use simple stated
math, like a seven percent average yearly return. That's an illustration, not a promise. This is
education, not financial advice.""",
   "Library books on shelves", "OUR SOURCES")

# ---------------- Angle 1 ----------------
ch("Angle 1: The Numbers")
pr("""Angle one. The numbers. These are the purchases where the math alone is enough to make a millionaire
say no.""")

item(1, "Brand new cars, every few years", "the fastest way to lose money",
"""Number one. Rich people rarely buy a brand new car every few years.""",
"""A new car starts losing value the moment you drive it home. Estimates from sources like Carfax and
Edmunds put the drop at around twenty percent in the first year, and roughly half or more after five
years, depending on the model. Meanwhile, Kelley Blue Book reported that the average price paid for a new
vehicle in America passed fifty thousand dollars in twenty twenty five. That's a lot of money to watch
melt.""",
"""In Stop Acting Rich, Stanley found that the median price millionaires paid for their most recent car was
about thirty one thousand dollars, in a survey from the late two thousands. Many bought used, and many kept
their cars for years. One of the most popular brands among them was Toyota, not Ferrari. Try this: before
your next car, look up the five year resale value of the model. If it loses half, you're paying for that
loss every month.""",
"Used car dealership lot", "-20% IN YEAR ONE",
"Toyota sedan parked on street", "RICH PEOPLE DRIVE TOYOTAS")

card("""Here's what that difference can grow into. Say you skip a car payment upgrade and invest three
hundred dollars a month instead. At a seven percent average yearly return, over twenty years that's
roughly one hundred fifty six thousand dollars.""",
     {"type": "growth", "monthly": 300, "rate": 0.07, "years": 20})

item(2, "Interest on credit cards", "paying 20% to buy things",
"""Number two. Rich people don't pay credit card interest.""",
"""According to the Federal Reserve, the average interest rate on credit card accounts that actually paid
interest was above twenty percent in recent years. Think about what that means. If you carry a balance,
every hundred dollar purchase can cost you more than one hundred twenty dollars by the end of the year.
You're paying a premium on everything you buy.""",
"""Many wealthy people use credit cards. They just pay the full balance every month, so the card is a
payment tool, not a loan. Some collect the rewards, which means the card company is paying them, not the
other way around. Try this: open your last statement and find the line that says interest charged. Multiply
it by twelve. That's what your balance is costing you a year.""",
"Credit cards on table", "20%+ INTEREST",
"Credit card statement close up", "PAY IN FULL")

item(3, "Lottery tickets", "the tax on hope",
"""Number three. Lottery tickets.""",
"""Americans spend more than one hundred billion dollars a year on lottery tickets, according to the North
American Association of State and Provincial Lotteries. The odds of winning the Powerball jackpot are about
one in two hundred ninety two million. You are far more likely to be struck by lightning than to hit
that jackpot.""",
"""On average, lotteries pay back only a portion of what players spend, which is how states raise money
from them. So, on average, every ticket loses money. Rich people do take risks, but they take risks where
the odds are on their side, like owning businesses and investments. Try this: if you buy tickets, add up
what you spent last year. Then imagine that money in an index fund instead.""",
"Lottery tickets scratch cards", "1 IN 292 MILLION",
"Lightning storm over city", "LIGHTNING IS MORE LIKELY")

item(4, "Extended warranties", "insurance you rarely need",
"""Number four. Extended warranties on small electronics.""",
"""When you buy a television or a laptop, the checkout screen often offers an extended warranty. Stores
push these hard because they're profitable. Consumer Reports has long argued that most of them aren't worth
the money, because many products don't break during the coverage period, and many credit cards already add
some extra warranty protection.""",
"""Wealthy people think about insurance differently. They insure against disasters they can't afford, like
a house fire or a lawsuit. They don't insure against losses they could easily pay for, like a broken
blender. Instead, they self insure, keeping cash ready for small surprises. Try this: next time you're
offered a warranty, ask yourself, could I replace this item without hurting my budget? If yes, skip it.""",
"Electronics store televisions", "PROFIT FOR THE STORE",
"Repair technician fixing laptop", "SELF INSURE")

item(5, "Timeshares", "easy to buy, hard to sell",
"""Number five. Timeshares.""",
"""A timeshare lets you buy the right to use a vacation property for a week or so each year. The sales
pitch is usually a free trip or a free dinner, followed by a long presentation. The price can easily run
into the tens of thousands of dollars, and there are yearly maintenance fees on top that tend to rise over
time.""",
"""The real problem shows up when you want out. The resale market for timeshares is weak, and many owners
find they can sell only for a small fraction of what they paid, if they can sell at all. The Federal Trade
Commission even warns about timeshare resale scams. Rich people prefer flexibility. They rent the
vacation they want, when they want it. Try this: if you're tempted, look up the resale listings for the
same resort first.""",
"Beach resort hotel pool", "THE FREE TRIP PITCH",
"Contract signing pen close up", "HARD TO SELL")

item(6, "Too much house", "the payment that eats everything",
"""Number six. More house than they need.""",
"""A bigger house doesn't just mean a bigger mortgage. It means bigger property taxes, bigger insurance,
bigger heating and cooling bills, more furniture, more repairs, and more maintenance, every year, for as
long as you live there. A common rule of thumb is to budget around one to two percent of a home's value
each year just for upkeep.""",
"""Stanley's research found that many millionaires lived in homes far below what they could afford. One of
the most famous examples is Warren Buffett, who still lives in the house in Omaha he bought in nineteen
fifty eight for about thirty one thousand five hundred dollars. Try this: add up everything your home
really costs per month, not just the mortgage. Taxes, insurance, utilities and repairs. That's your real
housing cost.""",
"Large mansion with lawn", "BIGGER EVERY BILL",
"Omaha Nebraska neighborhood houses", "BUFFETT'S HOUSE SINCE 1958")

item(7, "Fees they can avoid", "small numbers, big dollars",
"""Number seven. Fees they can avoid.""",
"""Overdraft fees, ATM fees, late fees, high fund fees, account maintenance fees. Each one looks tiny. But
together they can add up to hundreds of dollars a year. And investment fees are the sneakiest, because a
one percent yearly fee on a growing balance can cost tens of thousands of dollars over a lifetime of
investing.""",
"""Rich people are almost allergic to fees. They read the fee schedule. They move their money to banks that
don't charge for basics. They choose low cost funds. They pay bills on time, often with automatic payments,
so late fees never happen. Try this: go through the last three months of bank statements and circle every
fee. Then make one phone call or one switch to stop the biggest one.""",
"Bank ATM machine", "FEES ADD UP",
"Person reviewing bank statement", "CIRCLE EVERY FEE")

ch("A dollar saved beats a dollar earned")
sc("""Before we move to the psychology, one more piece of math that ties all seven together. A dollar you
don't spend is often worth more than a dollar you earn. Here's why. When you earn an extra dollar, taxes take
a piece first. Federal income tax, Social Security and Medicare, and in many places state tax too. Depending on
your bracket, you might keep seventy or eighty cents of it.""",
   "Pay stub with tax deductions", "TAXES COME FIRST")
sc("""But when you avoid spending a dollar, you keep the whole dollar. So cutting a one hundred dollar
monthly fee or interest charge can be worth as much as a raise of well over one hundred dollars a month
before taxes. That's why wealthy people take boring costs so seriously. Cutting a cost is like getting a raise
that nobody can take away, and you don't have to ask your boss for it.""",
   "Handshake in office", "A RAISE YOU GIVE YOURSELF")
sc("""And there's a second layer. Money you don't spend can be invested, and the growth on that money can
compound for decades. So every one of these seven refusals has a triple effect. You keep the full dollar.
You avoid the loss that comes with the purchase. And you gain the future growth. Add those three together
over a working lifetime, and you start to understand how ordinary earners become quiet millionaires.""",
   "Stairs going up concept", "THE TRIPLE EFFECT")

pr("""So that's angle one. The numbers. Notice something? None of these are about being cheap. They're
about not paying for things that make someone else rich at your expense. Now angle two, the psychology.
Because the numbers alone don't explain why smart people keep buying these things.""")

# ---------------- Angle 2 ----------------
ch("Angle 2: The Psychology")
sc("""Here's the uncomfortable truth. Most people know a new car loses value. Most people know lottery
odds are terrible. They buy anyway. Why? Because spending isn't really a math decision. It's an emotional
one. It's about status, comfort, belonging and fear. The next seven things on our list are the ones rich
people skip because they've learned to see the psychology behind them.""",
   "Brain illustration thinking", "SPENDING IS EMOTIONAL")

item(8, "Status symbols", "buying what others will see",
"""Number eight. Status symbols.""",
"""Stanley described a type of person he called the income statement affluent. People with high incomes
who look rich, with the big house, the luxury car and the designer clothes, but who have little actual
wealth. Their money goes out as fast as it comes in. He contrasted them with the balance sheet affluent,
who might look ordinary but own real assets.""",
"""The trap is that status purchases are designed to be seen. And once you buy one, your new neighbors and
coworkers have the same things, so the status fades and you need the next one. Economists call this
keeping up with the Joneses. Try this: before a big purchase, ask, would I still buy this if nobody could
ever see it? If the answer is no, you're paying for an audience.""",
"Luxury designer shopping street", "LOOKING RICH",
"Neighbors houses with cars in driveways", "KEEPING UP WITH THE JONESES")

item(9, "Designer labels", "paying for the logo",
"""Number nine. Designer labels for the sake of the label.""",
"""Remember the numbers from The Millionaire Next Door. Most millionaires surveyed had never spent more
than three hundred ninety nine dollars on a suit, one hundred forty dollars on shoes, or two hundred thirty
five dollars on a wristwatch. Those were nineteen nineties dollars, so adjust for inflation, but the point
stands. Most of them simply didn't care about labels.""",
"""This doesn't mean rich people buy junk. Many buy good quality items and use them for years. The
difference is that they pay for quality, not for a logo. A plain, well made coat that lasts ten years is
cheaper than a fashionable one that lasts two. Try this: look at the five most expensive pieces in your
closet. How often do you actually wear them? Divide the price by the number of times worn.""",
"Clothing store rack of suits", "$399 SUIT, $235 WATCH",
"Quality leather shoes", "QUALITY, NOT LOGOS")

item(10, "The newest phone every year", "the upgrade treadmill",
"""Number ten. The newest phone the day it comes out.""",
"""Flagship phones can cost a thousand dollars or more. Upgrading every year, often through a monthly
payment plan, makes that cost feel small. But each new model usually brings modest improvements over the
last one. Many people pay full price for features they never use.""",
"""The psychology here is novelty. Your brain gets a little reward from something new and shiny, and
companies schedule launches to trigger exactly that. Many wealthy people keep their devices until they
actually stop working well. Try this: when the next launch comes, write down three specific things your
current phone can't do that you actually need. If you can't find three, wait a year.""",
"Smartphone store display", "$1,000 EVERY YEAR",
"Old smartphone on desk", "USE IT UNTIL IT DIES")

item(11, "Things to impress strangers", "online and offline",
"""Number eleven. Things bought to impress strangers online.""",
"""Social media turned everyone's life into a highlight reel. You see the vacation, the new kitchen, the
car. You don't see the credit card bill. Surveys from groups like Bankrate and Credit Karma have found that
a meaningful share of younger adults say they've overspent because of something they saw on social
media.""",
"""Rich people are often remarkably private about money. Stanley's millionaires valued financial
independence over social display. If you're not trying to impress anyone, you're free to spend on what you
actually enjoy. Try this: unfollow five accounts that make you want to buy things. Notice how your wants
change in the next month.""",
"Smartphone social media feed", "THE HIGHLIGHT REEL",
"Person putting phone away outdoors", "UNFOLLOW FIVE")

pr("""Quick pause. If you're getting value from this, do me a favor and subscribe to Ryan Rover Money. It's
free, it helps the channel a lot, and every week we break down how money really works, with real numbers.
Okay, back to the psychology. Number twelve is one that hits close to home for a lot of people.""")

item(12, "Convenience at any price", "paying to avoid five minutes",
"""Number twelve. Convenience at any price.""",
"""Delivery fees, service fees, tips, and marked up menu prices can make a delivered meal cost much more
than the same food picked up or cooked at home. Doing it once is fine. Doing it every day quietly becomes
one of the biggest lines in a budget, and most people never add it up.""",
"""Wealthy people do pay for convenience, but deliberately. They might pay for help with something that
saves them hours, like a big home repair, while still cooking simple meals most nights. The rule is
intention. Try this: check your delivery app history for the last month and add up the total, including
fees and tips. Then decide what that number should be next month.""",
"Food delivery bag on doorstep", "THE CONVENIENCE TAX",
"Home cooking kitchen vegetables", "CHOOSE ON PURPOSE")

item(13, "Retail therapy", "shopping to fix a mood",
"""Number thirteen. Retail therapy.""",
"""Buying something can lift your mood for a moment. Researchers have studied this, and shopping can
genuinely make people feel better in the short term. The problem is that the feeling fades quickly, and
the bill doesn't. Over time, using shopping to manage stress can become an expensive habit.""",
"""Many rich people have replaced spending with cheaper ways to feel good. Walking, exercise, reading,
time with friends. Not because they're saints, but because they noticed the difference between a purchase
that adds value and one that just covers a bad day. Try this: use a twenty four hour rule. If you want
something that isn't essential, put it in the cart and wait a day. Often, the urge passes.""",
"Shopping bags in mall", "A MOOD, NOT A NEED",
"Person walking in park", "THE 24 HOUR RULE")

item(14, "Financial products they don't understand", "complexity is a warning",
"""Number fourteen. Financial products they don't understand.""",
"""Some investment products are sold with complicated features, guarantees and fine print. Some of them
come with high fees and long lock up periods, with penalties to get out early. The complexity isn't always
there to help the buyer. Sometimes it's there to hide the cost.""",
"""Warren Buffett has famously said he only invests in businesses he understands. Many wealthy people
follow a version of that rule. If they can't explain how a product makes money and what it costs, they
don't buy it. Try this: if someone pitches you an investment, ask three questions. How do you get paid?
What are all the fees? How do I get my money out? If the answers are vague, walk away.""",
"Fine print contract document", "IF IT'S CONFUSING, CAREFUL",
"Warren Buffett portrait", "ONLY WHAT YOU UNDERSTAND")

pr("""That's angle two. Status, novelty, convenience, emotion, complexity. Rich people feel all of those
pulls too. They've just learned to notice them. Now the best part. Angle three. The playbook. What do rich
people buy instead, and how can you copy it?""")

# ---------------- Angle 3 ----------------
ch("Angle 3: The Playbook")
sc("""Here's the shift. Rich people don't just avoid things. They redirect the money toward things that
grow. Every item in this last group is something they refuse to buy, paired with what they buy instead.
That pairing is the whole playbook.""",
   "Road sign pointing new direction", "REDIRECT THE MONEY")

item(15, "Upgrades before assets", "assets first, toys later",
"""Number fifteen. Lifestyle upgrades before they own assets.""",
"""A common pattern among people who build wealth is a simple order of operations. First, they build
income producing assets, like retirement accounts, index funds, a business or rental property. Then, once
those assets are growing, they use part of the growth for lifestyle upgrades. Most people do it the other
way around.""",
"""Think about a raise. Most people upgrade their lifestyle the same month. Many wealthy people save the
first raise, or at least half of it, before anything else changes. That way their spending never catches
up to their income. Try this: next time you get a raise, set up an automatic transfer of half the
increase into investments before your first new paycheck arrives.""",
"Stack of coins growing plant", "ASSETS FIRST",
"Paycheck and calculator", "SAVE HALF THE RAISE")

item(16, "Cheap tools that break", "buy once, cry once",
"""Number sixteen. Cheap tools that break, over and over.""",
"""This one surprises people. Rich people often refuse to buy the cheapest version of things they use
every day. A very cheap pair of boots that falls apart every year can cost more over ten years than a well
made pair that lasts a decade. The writer Terry Pratchett called this the boots theory of poverty.""",
"""The key is the word every day. For things you use constantly, like a mattress, work shoes, a reliable
car or good kitchen knives, quality can save money. For things you use once a year, cheap is fine. Try
this: list the five things you use most. Are any of them cheap replacements you keep buying? That's where
quality pays.""",
"Work boots worn leather", "BUY ONCE, CRY ONCE",
"Hardware store tools wall", "QUALITY FOR DAILY USE")

item(17, "Whole life policies they don't need", "keep insurance simple",
"""Number seventeen. Complex insurance they don't need.""",
"""Life insurance matters if people depend on your income. But some policies mix insurance with
investing, and they can carry high costs. Many personal finance experts suggest that most families are
well served by simple term life insurance, which covers a set number of years for a much lower premium.""",
"""The principle is to keep insurance and investing separate, so you can see what each one costs. Buy the
coverage you need, compare quotes, and invest the difference in low cost accounts. Some people do have
reasons for permanent policies, so this is a question to ask a fee only advisor about, not a rule for
everyone. Try this: find your current policy and write down what you pay each year and what it covers.""",
"Family at home together", "PROTECT THE FAMILY",
"Insurance policy papers on desk", "KNOW WHAT YOU PAY")

item(18, "Brand name basics", "store brands work fine",
"""Number eighteen. Brand name basics.""",
"""Store brand groceries, medicines and household products are often made to similar standards as the name
brands, and can cost noticeably less. For over the counter medicines, the active ingredient is listed on the
label, and the store version often has exactly the same one. The difference is mostly packaging and
advertising.""",
"""Researchers in Chicago once studied shoppers and found that pharmacists and doctors were much more likely
to buy store brand headache medicine than other shoppers. When people know what's inside the box, they stop
paying for the brand. Try this: on your next grocery trip, swap five name brand items for store brands. If
you can't tell the difference, keep the swap.""",
"Grocery store shelves products", "SAME INSIDE, LESS COST",
"Pharmacy shelves medicine", "WHAT EXPERTS BUY")

item(19, "Unused memberships and subscriptions", "the money that leaks quietly",
"""Number nineteen. Subscriptions they don't use.""",
"""Streaming services, apps, gym memberships, boxes delivered every month. Each one costs a few dollars, and
many renew automatically. Surveys regularly find that people underestimate how much they spend on
subscriptions, sometimes by a wide margin. The business model depends on you forgetting.""",
"""Rich people treat recurring costs as serious, because a recurring cost is like a reverse investment.
Fifteen dollars a month for ten years is eighteen hundred dollars, before you count what that money could
have earned. Try this: search your bank and card statements for every charge that repeats. Cancel anything
you haven't used in the last thirty days. You can always sign up again.""",
"Streaming apps on television", "THE QUIET LEAK",
"Person canceling subscription on laptop", "CANCEL WHAT YOU DON'T USE")

item(20, "Time-wasting deals", "a bargain isn't free",
"""And number twenty. Deals that waste their time.""",
"""This is the twist ending. Rich people don't chase every coupon or drive across town to save two dollars.
Time is the one thing nobody can buy more of. A deal that costs an hour to save a few dollars is often a
bad trade, and buying things just because they're on sale isn't saving at all. It's spending.""",
"""The wealthy focus on the big decisions, where the real money is. Housing, cars, taxes, fees and
investing. Get those five right, and you can relax about the price of coffee. Get them wrong, and no amount
of coupon clipping will save you. Try this: rank your five biggest yearly expenses. Spend your energy
cutting the top one, not the smallest one.""",
"Clock and money on desk", "TIME IS MONEY",
"House and car keys on table", "WIN THE BIG FIVE")

# ---------------- Story ----------------
ch("A tale of two neighbors")
pr("""Before we wrap up the three angles, let me tell you a story. It's made up, but it's built from the
patterns Stanley found again and again.""")
sc("""Meet two neighbors on the same street. Mark is a sales director earning two hundred thousand dollars a
year. Linda is a high school teacher married to an electrician, and together they earn about one hundred
thirty thousand dollars. From the street, Mark looks like the rich one. He has the bigger house, a new
luxury SUV every three years, and a boat in the driveway.""",
   "Two houses side by side street", "TWO NEIGHBORS")
sc("""Linda and her husband drive a ten year old minivan and a pickup truck they bought used. Their house is
smaller and paid down fast. They cook most meals, take one simple vacation a year, and since their first
jobs they have put fifteen percent of their pay into retirement accounts and index funds, automatically,
every single month.""",
   "Old minivan parked in driveway", "THE ORDINARY ONES")
sc("""Twenty five years later, Mark has a big income, a big mortgage and a big car loan. If he lost his job,
his family could last maybe three months. Linda and her husband have a paid off house and investments
that, at historical average returns, could plausibly be well over a million dollars. They could stop working
tomorrow. Mark can't stop for a single month.""",
   "Couple relaxing on porch", "25 YEARS LATER")
sc("""Stanley's research suggested this pattern was common. He found that, among high income households,
the ones who accumulated the most wealth were usually the ones who spent the least on visible status
items. Income makes you look rich. Wealth makes you free. And the twenty things on this list are exactly
where that difference gets decided.""",
   "Open road at sunrise", "LOOKING RICH VS BEING FREE")

# ---------------- Bonus math ----------------
ch("What the skipped purchases add up to")
pr("""Now let's put the three angles together, because this is where it gets exciting.""")
sc("""Imagine someone who skips just a few of these. They keep their car a few years longer instead of
upgrading. They pay their credit card in full. They cancel two subscriptions they don't use and cut back on
delivery. It's not hard to imagine that freeing up five hundred dollars a month for a typical household.
Not by living in misery. Just by refusing to pay for things that don't add much to their life.""",
   "Family budget planning at table", "$500 A MONTH")
card("""Now invest that five hundred dollars a month at a seven percent average yearly return. After thirty
years, that could grow to roughly six hundred ten thousand dollars. You would have put in one hundred eighty
thousand. The rest is growth.""",
     {"type": "growth", "monthly": 500, "rate": 0.07, "years": 30})
sc("""That's the secret Stanley kept finding in his research. The millionaire next door didn't get there
through one big win. They got there by quietly refusing hundreds of small and medium purchases, and putting
that money to work for decades. It's not exciting. It's not glamorous. But it works for ordinary
people with ordinary incomes, and that's what makes it powerful.""",
   "Elderly couple walking on beach", "QUIET REFUSALS")

# ---------------- What they do buy ----------------
ch("What rich people do spend on")
pr("""So if rich people refuse all these things, what do they actually spend on? Because they do spend.
They just spend differently.""")
sc("""First, they buy time. Many wealthy people will happily pay for things that free up hours, like help
with a big project, or living close to work to avoid a two hour commute. Time saved can go into a business,
a skill, their health or their family. That's spending that pays them back.""",
   "Commuter traffic jam highway", "THEY BUY TIME")
sc("""Second, they buy knowledge. Books, courses, coaching, conferences in their field. Stanley noticed that
many of the millionaires he studied were serious about learning and about investing in their children's
education. A skill that raises your income for the rest of your career can be the best return you'll ever
get.""",
   "Person reading book in library", "THEY BUY KNOWLEDGE")
sc("""Third, they buy health. Good food, exercise, preventive care, sleep. Health problems are one of the
biggest financial risks a family faces, and medical bills are a leading reason people fall behind.
Spending a little on staying healthy is protecting your biggest asset, which is your ability to work and
enjoy life.""",
   "Person jogging in park morning", "THEY BUY HEALTH")
sc("""Fourth, they buy assets. Index funds, retirement accounts, a share of a business, a rental property.
Things that tend to grow or pay income over time. And fifth, they buy experiences with the people they love.
Research on happiness has often suggested that experiences, especially shared ones, bring more lasting
satisfaction than things. A camping trip with your kids can stay with you longer than a new couch.""",
   "Family camping by lake", "ASSETS AND EXPERIENCES")
sc("""Notice the pattern. Time, knowledge, health, assets and relationships. Every one of them either grows
in value or makes your life better for years. Compare that with the twenty things on our list, which
mostly lose value the moment you pay. That's the real difference between how rich people and everyone else
spend.""",
   "Growing tree in field", "SPEND ON WHAT GROWS")

# ---------------- Challenge ----------------
ch("The 30 day refusal challenge")
pr("""Now, a challenge. Let's make this practical with a thirty day experiment.""")
sc("""Week one, the numbers. Pull up your last three months of statements. Highlight every fee, every
interest charge, and every payment on something that loses value, like a car loan. Don't change anything
yet. Just see the total. Most people are surprised by it, and that surprise is useful.""",
   "Highlighter on bank statement", "WEEK 1: SEE IT")
sc("""Week two, the psychology. Every time you want to buy something that isn't essential, write it down
with the reason. Was it boredom? Stress? Something you saw online? Something a friend has? Don't judge
yourself. Just name it. By the end of the week, you'll see your own patterns clearly.""",
   "Journal writing with coffee", "WEEK 2: NAME IT")
sc("""Week three, the playbook. Make three changes. Cancel the subscriptions you don't use. Call to remove
one fee or lower one interest rate. And set up one automatic transfer into savings or investments on
payday, even if it's small. Twenty five dollars counts. The habit matters more than the amount.""",
   "Phone call at desk", "WEEK 3: CHANGE IT")
sc("""Week four, redirect. Take whatever you freed up and point it at something that grows. Your emergency
fund first, if you don't have one. Then high interest debt. Then long term investing. At the end of thirty
days, you'll have a number you can see, and that number is your proof that this works for you, not just
for millionaires in a book.""",
   "Piggy bank and coins growing", "WEEK 4: REDIRECT IT")

# ---------------- Mistakes ----------------
ch("Mistakes to avoid")
sc("""Three mistakes people make when they try this. Mistake one, going too extreme. If you cut every
pleasure at once, you'll burn out and swing back to spending. Keep a small budget for fun, guilt free.
Mistake two, comparing yourself with others. Your plan only has to beat your old habits, not your
neighbor.""",
   "Person stressed with bills", "DON'T GO TOO EXTREME")
sc("""Mistake three, saving without a destination. Money that just sits in a checking account tends to get
spent. Give every freed up dollar a job, whether that's an emergency fund, a debt payoff, or an
investment account. When money has a job, it's much harder to waste.""",
   "Labeled jars savings goals", "GIVE EVERY DOLLAR A JOB")

# ---------------- FAQ ----------------
ch("Questions people ask")
pr("""Let me answer a few questions people always ask about this topic.""")
sc("""Question one. Isn't this just being cheap? No. Being cheap means always choosing the lowest price,
even when it costs you more later, or costs your relationships. Being frugal means spending deliberately on
what you value and cutting what you don't. Many wealthy people spend generously on education, health,
travel or family. They just don't spend on autopilot.""",
   "Family dinner together at home", "CHEAP VS FRUGAL")
sc("""Question two. But don't rich people buy luxury things? Some do, of course. The people you see on
television and social media often do. But Stanley's research suggests that the typical millionaire, the
one you'd never notice, lives well below their means. The flashy minority gets all the attention. The quiet
majority gets the wealth.""",
   "Luxury sports car on street", "THE FLASHY MINORITY")
sc("""Question three. I don't earn much. Does any of this matter for me? It matters even more. When money is
tight, every fee, every point of interest and every unused subscription takes a bigger bite. And the habits
you build at a small income are the ones that carry you when your income grows. Start with the one item
on this list that costs you the most.""",
   "Young worker with lunch box", "SMALL INCOME, BIG IMPACT")
sc("""Question four. Should I sell my new car right now? Not necessarily. Selling a car you just bought
often locks in the biggest part of the loss. For many people, the better move is to keep it, take good care
of it, pay it off, and then drive it for years after the last payment. That payment free stretch is where
the real savings live.""",
   "Car parked in garage", "KEEP IT LONGER")
sc("""Question six. What about my partner? What if they love spending? This is common, and it's a
conversation, not a battle. Sit down together and agree on a few big goals first, like a house, an
emergency fund or retiring early. Then give each person a personal spending amount, no questions asked.
Couples who share goals usually find it much easier to cut what doesn't matter.""",
   "Couple talking at kitchen table", "TALK WITH YOUR PARTNER")
sc("""Question seven. Is it ever okay to buy a nice car or a designer item? Of course. The question is
order and proportion. If your emergency fund is full, your debt is handled, and you're investing steadily,
a treat you truly love is your choice. Many wealthy people do have one or two splurges. They just choose
them on purpose, and they pay cash.""",
   "Classic car at car show", "SPLURGE ON PURPOSE")
sc("""Question eight. How long until I see results? The savings show up in your account the very first
month you cut a fee or cancel a subscription. The bigger results take longer. Compounding is slow at the
start and fast at the end, so the first few years can feel like nothing is happening. Keep going anyway. Most
people who quit, quit right before the curve starts bending upward.""",
   "Curved road up a hill", "HOW LONG IT TAKES")
sc("""And question five. Where do I start? Pick one item from each angle. One from the numbers, like
credit card interest. One from the psychology, like status purchases. One from the playbook, like
canceling unused subscriptions. Three small changes this month. That's how every money story that ends
well actually starts.""",
   "Notebook checklist with pen", "ONE FROM EACH ANGLE")

# ---------------- Recap ----------------
ch("Recap: all 20")
sc("""Quick recap. Angle one, the numbers. Rich people never buy new cars every few years, never pay credit
card interest, skip lottery tickets, extended warranties and timeshares, avoid too much house, and avoid
fees.""",
   "Checklist on clipboard", "THE NUMBERS: 1 TO 7")
sc("""Angle two, the psychology. They skip status symbols, designer labels, the newest phone every year,
things to impress strangers, convenience at any price, retail therapy and financial products they don't
understand.""",
   "Thinking person silhouette window", "THE PSYCHOLOGY: 8 TO 14")
sc("""Angle three, the playbook. No upgrades before assets, no cheap tools that break, no complex insurance
they don't need, no brand name basics, no unused subscriptions, and no deals that waste their time.""",
   "Notebook with written goals", "THE PLAYBOOK: 15 TO 20")

# ---------------- Close ----------------
ch("What to do next")
pr("""If you want the full plan for turning these refusals into real wealth, it's in my playbook. The link
is in the description. Tell me in the comments which of these twenty you already skip, and which one
surprised you most. I'm Ryan Rover. See you in the next one.""")

save("video21", "20 Things Rich People Never Buy", [
    "Thomas J. Stanley and William D. Danko, The Millionaire Next Door (1996): most millionaires surveyed never spent more than $399 on a suit, $140 on shoes, $235 on a wristwatch",
    "Thomas J. Stanley, Stop Acting Rich (2009): median price millionaires paid for their most recent vehicle about $31,000; income statement vs balance sheet affluent",
    "Kelley Blue Book, average new-vehicle transaction price above $50,000 (2025)",
    "Carfax and Edmunds, new-car depreciation estimates (around 20% in the first year)",
    "Federal Reserve, G.19 Consumer Credit: interest rate on credit card accounts assessed interest (above 20%)",
    "North American Association of State and Provincial Lotteries, US lottery sales over $100 billion a year; Powerball jackpot odds 1 in 292.2 million (Powerball.com)",
    "Federal Trade Commission, consumer guidance on timeshares and timeshare resale scams",
    "Bronnenberg, Dube, Gentzkow and Shapiro, Do Pharmacists Buy Bayer? (Quarterly Journal of Economics, 2015)",
    "Growth examples: monthly compounding at 7% average yearly return (illustration, not a promise)",
], "20 things rich people never buy, from 3 angles: numbers, psychology, playbook")
