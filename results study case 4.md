# Study Case 4 Suggested Answers
## Number 1
study case 4 number 1 point a inflation violation: DatetimeIndex(['2000-10-01', '2002-01-01', '2002-04-01', '2005-01-01',
               '2005-04-01', '2005-07-01', '2005-10-01', '2006-01-01',
               '2006-04-01', '2006-07-01', '2008-01-01', '2008-04-01',
               '2008-07-01', '2008-10-01', '2009-01-01', '2009-04-01',
               '2009-07-01', '2009-10-01', '2011-07-01', '2011-10-01',
               '2013-04-01', '2013-07-01', '2013-10-01', '2014-01-01',
               '2015-01-01', '2015-04-01', '2015-07-01', '2015-10-01',
               '2016-01-01', '2016-04-01', '2016-07-01', '2016-10-01',
               '2019-04-01', '2019-07-01', '2019-10-01', '2020-01-01',
               '2020-04-01', '2020-07-01', '2020-10-01', '2021-07-01',
               '2021-10-01', '2022-01-01', '2022-04-01', '2022-07-01',
               '2022-10-01', '2023-01-01', '2023-04-01', '2023-07-01',
               '2023-10-01', '2024-01-01'],
              dtype='datetime64[ns]', name='observation_date', freq=None)

study case 4 number 1 point a unemployment violation: DatetimeIndex(['2003-07-01', '2008-10-01', '2009-01-01', '2009-04-01',
               '2009-07-01', '2009-10-01', '2010-01-01', '2010-04-01',
               '2010-07-01', '2010-10-01', '2011-01-01', '2011-04-01',
               '2011-07-01', '2011-10-01', '2012-01-01', '2012-04-01',
               '2012-07-01', '2012-10-01', '2013-01-01', '2013-04-01',
               '2013-07-01', '2013-10-01', '2014-01-01', '2014-04-01',
               '2014-07-01', '2014-10-01', '2020-07-01', '2020-10-01',
               '2021-01-01', '2021-04-01'],
              dtype='datetime64[ns]', name='observation_date', freq=None)

study case 4 number 1 point b current violation: violated

study case 4 number 1 point c:
Inflation gaps:
The extensive list of dates for potential inflation gap violations indicates the difficulty of maintaining a stable inflation rate at the target of 2%. This could be due to:

a. External Shocks: Events like oil price fluctuations, natural disasters, or supply chain disruptions can cause inflation spikes or dips outside the Fed's control.
b. Trade-offs: Balancing inflation with unemployment can be a delicate act. Actions taken to curb inflation (raising interest rates) might lead to higher unemployment in the short term.
c. Limited Foresight: Predicting inflation accurately is challenging. The Fed might react to past inflation data, and future events might impact inflation unexpectedly.

Unemployment gaps:
The dates for potential unemployment gap violations highlight the complexity of achieving maximum employment. Challenges include:

a. Recessions: Economic downturns naturally lead to higher unemployment. The Fed might prioritize mitigating recessions even if it means exceeding the natural unemployment rate.
b. Structural Unemployment: Changes in the economy can lead to skills mismatches between workers and available jobs. The Fed's monetary policy tools might not be effective in addressing these structural issues.
c. Natural Rate Uncertainty: Estimating the natural rate of unemployment is imprecise. The Fed might unintentionally deviate from this target due to inaccurate estimates.

Economic Shocks: The periods of violations often align with major economic shocks:
a. Early 2000s: Dot-com bubble burst and subsequent recession.
b. Great Recession (2007-2009): Financial crisis and global economic downturn.
c. COVID-19 Pandemic: Severe economic disruption caused by the global pandemic.

Challenges for Monetary Policymakers:
1. Dual Mandate Complexity: The Fed’s dual mandate to achieve maximum employment and stable prices can be inherently conflicting. For instance, measures to curb inflation (e.g., raising interest rates) can slow down economic growth and increase unemployment, while measures to reduce unemployment (e.g., lowering interest rates) can spur inflation.
2. External Shocks: Unpredictable economic shocks such as financial crises, pandemics, and geopolitical events can significantly disrupt economic stability. Policymakers must respond to these shocks, often balancing short-term needs against long-term goals, which can lead to temporary violations of mandates.
3. Lagging Indicators: The effects of monetary policy are not instantaneous and often have a lag. Decisions made today may not show their full impact on inflation and unemployment for several quarters, making it challenging to fine-tune policies precisely.


## Number 2
study case 4 number 2 point a: exported to ‘sc_42a.xlsx’
study case 4 number 2 point b, mtm correlation: -0.074
study case 4 number 2 point b, yoy correlation: 0.072

study case 4 number 2 point b interpretation:
The coefficients we calculated are not entirely consistent with the expected relationship in the market for reserves. Explanation:
Expected Relationship: A negative correlation is expected between the month-to-month and year-on-year changes. This means a positive change in non-borrowed reserves (increase) should be accompanied by a negative change in the federal funds rate (decrease).

Our Results:
Month-to-Month: The coefficient of -0.074 is negative, which aligns with the expectation, although the value is very weak. A weak negative correlation suggests a slight tendency for the variables to move in the opposite direction, but not strongly.
Year-on-Year: The coefficient of 0.072 is positive, which is the opposite of the expected relationship. This suggests a weak positive correlation, meaning the variables might move in the same direction to some degree, but again, the effect is weak.

Expected Relationship:
There's an expected inverse relationship between the percent change in nonborrowed reserves and the percentage point change in the federal funds rate in the market for reserves. 

When the Federal Reserve increases the supply of nonborrowed reserves, it generally aims to lower the federal funds rate. More reserves in the banking system reduce the need for banks to borrow from each other, which puts downward pressure on the interest rate for overnight loans, i.e., the federal funds rate.

Conversely, when the Fed decreases the supply of nonborrowed reserves, it aims to raise the federal funds rate. Fewer reserves mean banks have to borrow more from each other, increasing the demand and pushing the federal funds rate up.

Possible Explanations:
Month to Month vs. Year on Year: The market for reserves reacts quickly to changes in supply and demand. Month-to-month changes might capture this dynamic better, explaining the weak negative correlation we observed.
Other Factors: The federal funds rate can be influenced by other factors besides just non-borrowed reserves, such as economic conditions or Fed policy announcements. These can mask the underlying relationship in year-to-year comparisons, potentially leading to the weak positive correlation we observed.
Random Fluctuations: Month-to-month data can be more volatile and prone to random fluctuations compared to year-to-year data. This could weaken the observed correlation, even if the underlying relationship exists.
