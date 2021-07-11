
* https://towardsdatascience.com/what-metrics-should-we-use-on-imbalanced-data-set-precision-recall-roc-e2e79252aeba

Candidate Questions:
---
 * Can I predict CDN vs US vs AU vs ENG ?
    * no it appears not on first pass : notebook/milestone/country_prediction_fail_attempt1.ipyn

 * Are there differences in technology interest by region ?
   * would be stronger if using GDP by sector to determine sector similarities and see if code interest correlates

 * do some groups withold salary info more ?
   * by country
   * by age
   * by education 

Data Quality Notes:
---
  * (DONE) CompTotal is a mess, refer to ConvertedComp
  * (DONE) Should transform columns (discuss how and why):
    * YearsCode -> exclude 'Less than 1 year' and 'More than 50 years'
    * YearsCodePro -> exclude 'Less than 1 year' and 'More than 50 years'
    * Age1stCode -> exclude 'Younger than 5 years' , 'Older than 85'

Can I predict CDN vs US vs AU vs ENG using the following:
---
 * Age
 * Age1stCode
 * ConvertedComp
 * Employment <-- could filter out with this
 * JobFactors <-- throwing this away for now as i have to parse it first
 * JobSat
 * JobSeek <-- could filter out with this  
 * MainBranch
 * NEWEdImpt
 * OpSys
 * OrgSize
 * UndergradMajor
 * WorkWeekHrs
 * YearsCode
 * YearsCodePro
  
Biggest risk : trying to predict a categorical. Perhaps better to just look for statistical differences in some responses

Interesting what tech you work with questions:
---
* MiscTechDesireNextYear
* MiscTechWorkedWith
* NEWCollabToolsDesireNextYear
* NEWCollabToolsWorkedWith
* PlatformDesireNextYear
* PlatformWorkedWith
* WebframeDesireNextYear
* WebframeWorkedWith
* DatabaseDesireNextYear
* DatabaseWorkedWith

Interesting random thing : 
---
  * NEWPurchaseResearch


Tick All That Apply Questions
---
* NEWJobHuntResearch
* NEWPurchaseResearch
* NEWSOSites
* JobFactors

July 15 WIP
---

Candidate Questions:
  * Can I build a is_usa predictor
  * Can I hand pick variables better than just considering all for the is_usa question
  * Which variables are used for the is_usa
  * Are there some countries that I can predict better for ?
  * Do the best co-efficients vary from country to country

4 cutoffs <--
feature candidate sets
  * hand selected
  * everything - excluding the dodgy ones that need processing
  * (DEFER) everything - process the dodgy ones

rows - all countries, country subsets
rows - 10%, 50%, 100%

(    ) how much faster out of docker. out of jupyter
(    ) can i script jupyter to python
(    ) verify 0.1 -> 0.5 -> 1.0
(    ) look at nunique again
(    ) start graphing
(DONE) round before data framing
(IN PROGRESS) check coefficients
(    ) readd my hand picks
(    ) compare against svm
(    ) why are some coefficients missing : 
           * result_df.query('row_label == "full_country" and cutoff == 250').coefficients

real objective -> try to choose each of the countries, pick out the strongest co-efficients. look at num samples to variation in FP/FN/TPP/etc