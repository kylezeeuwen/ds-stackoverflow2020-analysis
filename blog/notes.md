
* https://towardsdatascience.com/what-metrics-should-we-use-on-imbalanced-data-set-precision-recall-roc-e2e79252aeba
* https://medium.com/@josh_2774/how-do-you-become-a-developer-5ef1c1c68711

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

(DONE) pickle with params
(DONE) compare against svm
(DONE) extract greatest co-efficient
(    ) move some helpers into model_helpers
(    ) move some helpers into data_preperation
(DONE) how much faster out of docker. out of jupyter. Not much
(DONE) can i script jupyter to python- via convert 
(DONE) verify 0.1 -> 0.5 -> 1.0 - not much benefit
(    ) look at nunique again
(    ) start graphing
(DONE) round before data framing
(IN PROGRESS) check coefficients

(    ) readd my hand picks

(DONE) why are some coefficients missing : 
     * result_df.query('row_label == "full_country" and cutoff == 250').coefficients
     * because those models are just NOPE machines 

real objective -> try to choose each of the countries, pick out the strongest co-efficients. look at num samples to variation in FP/FN/TPP/etc


Notes on Lesson 2
---
Three Steps to captivate:
* Pull in reader
  * title and image
  * image first, then title to match
  * "two sentences and an image to capture reader"
    * asking questions that they have aslo asked
    * or current events
* Keep engaged
  * strong story telling
     * a story that is relatable to themselves 
  * personal voice
  * article structure
      * up to 3 lines per idea, no more than 5
* Close Post
  * reiterate main points
  * call to action
    
* Logistics of post
  * short and sweet - 1 - 2 pages, 500 - 700 words, make outline, less than 8 min read
  * use questions to form outline
    * intro
    * takeaway 1  
    * takeaway 2  
    * takeaway 3
    * conclusion
      * ok to post unfinished thoughts  