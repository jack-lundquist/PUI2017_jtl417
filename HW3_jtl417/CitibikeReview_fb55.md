 ## HYPOTHESIS FORMULATION

You should state why your idea is interesting in your report and what motivates it. 

The Null/Alternatively seems to be  formulated appropriately and in accordance with the original question, and the significance level is clearly stated (note: that is a **significance** level, not a confidence level, though you will see both in the literature)

## DATA

The data supports the analysis and seems appropriately pre-processed. The plots are very useful to give a hint of the answer.

## STATISTICAL TEST

You are testing the difference between the mean of two samples.
While standard tests to assess difference in means between 2 (or more) samples include the ANOVA (analysis of variance) or t-test,
this test strictly applies to continuous variables, whereas here your variable (rides count) is discreat. 
However, with large counts, this may be overlooked and the discrete number of rides treated as continuous (often seen in the literature)
The anov exists in both parametric and non parametric form, whilc t-test assumes normality.

If the data can be treated as Poisson, since the IV is a count, then tests such as Poisson mean difference, E-test and C-test can be used, 
but the human behavior component makes it unlikely that the Poisson assumption holds. 

There is no reason to believe your population distributions are inherently Gaussian so a better choice is the chi sq test for proportion, 
which is non parametric, or the Fisher exact test, also non-parametric. However, since your sample size is large, of the two tests mention the appropriate one to use is the chi sq test for proportion (contingency table)


NOTE: For whichever test you chose, you want the one-tailed version

# Additional suggestions
Your hypothesis does not specifically state if you are going to look at subscribers, costumers, or both, 
but when looking at weekday vs weekend you are obviously comparing samples that may have a different distribution of reider type. 
You should discuss how this relates to your question and whether your question is assessing anything other than this split between costumer type

Friday may be a "special day" straddling the week and the weekend (we see this in many analyses that have to do with human mobility) and to a lesser extent monday .
In addition because you use January there will be "vacation days" that may not be representative of week-day behavior. This should be discussed.
