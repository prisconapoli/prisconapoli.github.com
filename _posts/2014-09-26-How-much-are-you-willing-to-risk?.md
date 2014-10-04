---
layout: post
category : lessons
tags: [quantitative trading, risck model, financial market, black box]
---
{% include JB/setup %}

**About risk modeling in quant trading.**

<!--more-->

In my previous post I described a fundamental component in a quantitative system called **alpha model**.

An alfa model aims to determine the *composition* and *quantity* of the portfolio. Its output, indeed, represents a **return forecast** (potential gain) or a **direction forecast** (price is rising or decreasing). Some trading firm use several alpha models simultaneously. The concept of using the information from different signals alpha is particularly interesting. This is the same problem which has to solve any decision maker when faced with a variety of information and opinions. What is the best way to summarize all the relevant information in a sensible decision for business?
Is necessary to keep in mind that exposure is the thing from which a quantitative trader expects to get profits. Exposure to risks not only generates profits in the long run but may have an impact in the strategy day by day. Use an adeguate risk model is necessary to avoid loosing money in Financial Trading.

<div style="text-align:center" markdown="1">
![Black Box structure]({{ site.url }}/assets/images/quantitative-trading/risk-model.png)
</div>

######Black Box structure, credits 'Inside The Black Box' by Rishi Narrang

####Risk Management
Think about risk management as the traditional way *avoids risks and reduce losses* is fairly poor. For a quant trader risk management is more than this. 
It is about an **intentional and a careful selection of exposure size in order to improve the quality and consistency of returns**. 

Quantitative risk models generally limit the size in three primary ways:
1. the manner in which size is limited;
2. how risk is measured;
3. what is having its size limited.

Size limit generally comes in two forms:

* hard constraints;
* penalties.

About the measuring the amount of risk, **volatility** is probably the most important. One accepted way is called *longitudinal measurement*, because it measures the risk calculating the **standard deviation** of the returns of the individual instruments along the time, which is a way to measure the uncertainty. In this context, uncertainty is a synonym for volatility.

Another way to measure uncertainty is evaluating **dispersion**. It can be obtained measuring the **covariance** between instruments that belong the same category (also called *universe*). 


####Summary

Risk management is often confused with a boring exercise in order to reduce the risks. In truth, it is related to the selection and sizing of the exposure in the market, in order to maximize returns starting from a certain level of risk.

Typically, a quant trader can use both theoretical or empirical approachs (or an hybrid) to risk management. 
We should keep in mind that all these approaches have the same goal: identify which systematic risks have been taken, measure the amount of exposure into portfolio, and determine if this risk is acceptable or not.

In the next post we'll see the *Cost Model*, which is used to determine how expensive is make trading.


###Further Information

[Inside the Black Box: The Simple Truth About Quantitative Trading](http://www.amazon.com/Inside-Black-Box-Quantitative-Trading/dp/1480590061) by Rishi K. Narang



