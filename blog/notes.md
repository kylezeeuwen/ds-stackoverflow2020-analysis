Data Quality Notes:
---
  * CompTotal is a mess, refer to ConvertedComp
  * Should transform columns (discuss how and why):
    * YearsCode -> exclude 'Less than 1 year' and 'More than 50 years'
    * YearsCodePro -> exclude 'Less than 1 year' and 'More than 50 years'
    * Age1stCode -> exclude 'Younger than 5 years' , 'Older than 85'

Summary Questions:
---
 * Can I predict CDN vs US vs AU vs ENG ?
 * Are there differences in technology interest by region ?
   * would be stronger if using GDP by sector to determine sector similarities and see if code interest correlates
  


Can I predict CDN vs US vs AU vs ENG using the following:
---
 * Age
 * Age1stCode
 * ConvertedComp
 * Employment <-- could filter out with this
 * JobFactors
 * JobSat
 * JobSeek <-- could filter out with this  
 * MainBranch
 * NEWEdImpt
 * OpSys
 * OrgSize
 * UndergradMajor
 * WorkWeekHrs
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

Interesting random thing : 
---
  * NEWPurchaseResearch


Tick All That Apply Questions
---
* NEWJobHuntResearch
* NEWPurchaseResearch
* NEWSOSites
