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
