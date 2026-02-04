You might have noticed rows with negative package weights. If you found that 25% of the dataset had negative weights, would you drop them? If not, what would you do instead?

Ans:	No, data volume is small, dropping rows again may cause underfitting. Since there are package weights, I will replace/fill the negative values with mean instead


Imagine the traffic_level data comes from a paid API that costs us money every time we call it. How would you determine if this feature is 'worth' the cost?
Ans:	I would use feature selection like SelectKBest to rank the most useful attributes. If the score or ranking below average, it can be considered to not use this attribute