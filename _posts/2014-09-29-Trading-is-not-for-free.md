---
layout: post
category : lessons
tags: [quantitative trading, cost model, financial market, black box]
---
{% include JB/setup %}

**Few considerations about the transactions cost in quant trading.**

<!--more-->

The basic idea behind a transaction model consists in the fact that make trading is expensive, for which reason one should not trade unless there is a potential return in economic terms. Typically the cost of a transaction is between 20% and 50% of the total return. 

The rule-of-thumb is simple: **do trade only if is possible to improve quotations or increase returns. Do not trade otherwise**. 

It is worth to note that the main purpose of a transaction cost model is not to minimize costs, but *provide to the portfolio constructor the cost for each trade*. The part that takes care to minimize the total cost is the **execution algorithm** (I'll explain this component in the coming posts). 

Costs are generally due to commissions and fees paid to brokers, exchanges or regulators for the services they provide. 

<div style="text-align:center" markdown="1">
![Black Box structure]({{ site.url }}/assets/images/quantitative-trading/cost-model.png)
</div>

######Black Box structure, credits 'Inside The Black Box' by Rishi Narrang

####Slippage
One of the most interesting aspect in cost modeling is the concept of **slippage**.

This is the price change between the time that a trader (or a quant system) decides to make a transaction and the time when the order is received by the exchange for execution. Indeed, the market is *dynamic* and during this little time it can move so the price may vary. Slippage can be considered a sort of indicator for *instrument's volatility*. Liquidity can be defined in several ways: its an indicator for the available size in the offer or in the sell side, or order book depth.

In general, strategies that suffer the phenomenon of slippage are those which pursuise *trend following*, because they try to buy or sell instruments that are already moving in the desired direction.
On the other side, the strategies that suffer less the slippage are those based on *mean-reverting*, as they trade instruments that move against the natural tendency.

Obviously, in the *High Frequency Trading* context both latency and throughput have a crucial aspect to contrast the slippage. 

####Market impact
Surely the market has the most important impact for a quant system. It is quite simple to understand: **when an order comes in the exchange, it finish to change inevitably the price**. For small orders, the impact is negligible, but for large orders the impact may be several percentage points. 

####Models of transaction cost 

There most used are:

**Flat**: is the simplest type, a flat model which indicates that the cost for making trading is always the same, regardless of the order size

**Linear**: the transaction cost increases with the order size 

**Piecewise linear**: they provide a greater accuracy compared to linear models, but they are still simple to use

**Quadratic**: these models are very onerous from a computational point of view, as the functions involved are not always linear. It is without doubt the most accurate method for an estimation.


####Summary

A transaction model is used to provide an accurate estimate of the costs related to trading activities. The next post will be about the *Portfolio Construction Model*, the component that uses the information coming from *Alpha, Cost and Transaction Models* to build a portfolio.

###Further Information

[Inside the Black Box: The Simple Truth About Quantitative Trading](http://www.amazon.com/Inside-Black-Box-Quantitative-Trading/dp/1480590061) by Rishi K. Narang

[Moving Average Crossover](http://en.wikipedia.org/wiki/Moving_average_crossover), Wikipedia

[High Frequency Trading](http://en.wikipedia.org/wiki/High-frequency_trading), Wikipedia



