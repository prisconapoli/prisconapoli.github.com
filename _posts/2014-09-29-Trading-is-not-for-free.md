---
layout: post
category : lessons
tags: [quantitative trading, cost model, financial market, black box]
---
{% include JB/setup %}

**Few considerations about the transactions cost in quant trading.**

<!--more-->

The basic idea behind a transaction model consists in the fact that make trading is expensive, for which reason one should not trade unless there is a potential return in economic terms. Typically the cost of a transaction is between 20% and 50% of the total return. 

The rule-of-thumb is simple: do trade only if is possible to improve quotations or increase returns. Do not  trade otherwise. 

It is worth to note immediately that the main purpose of a transaction cost model is not to minimize costs, but provide to the portfolio constructor the cost for each trade. The part that takes care to minimize the total cost os the execution algorithm (I'll explain this component in the coming posts). 

Costs are  generally due to commissions and fees paid to brokers, exchanges or regulators for the services they provide. 

One of the most interesting aspect in cost modeling is the concept of slippage. This is the price change between the time that a trader (or a quant system) decides to make a transaction and the time when the order is received by the exchange for execution. Indeed, the market is dynamic and during this little time it can move so the price may vary. Slippage can be considered a sort of indicator for volatility of an instrument. Liquidity can be defined in several ways. You can think it as an indicator of the available size in the offer or sell side, or the depth of order book.

In general, the strategies that suffer the phenomenon of slippage are those which pursuise trend following, because they try to buy or sell instruments that are already moving in the desired direction.
On the other side, the strategies that suffer less the slippage are those based on mean-reverting, as they trade instruments that move against the natural tendency.

Obviously, latency and throughput have a crucial aspect to contrast the slippage. 

####Market impact
Surely it is the most important factor for a quant trader. It is quite simple to understand: when an order comes in the exchange, it finish to change inevitably the price. For small orders, the impact is negligible, but for large orders the impact may be several percentage points. 


####Summary



###Further Information

[Inside the Black Box: The Simple Truth About Quantitative Trading](http://www.amazon.com/Inside-Black-Box-Quantitative-Trading/dp/1480590061) by Rishi K. Narang



