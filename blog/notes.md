# Basics

* Size: (64461, 61)

# Schema

* df.dtypes
* Respondent                     int64 - Randomized respondent ID number (not in order of survey response time)  
* MainBranch                    object - Which of the following options best describes you today? Here, by "developer" we mean "someone who writes code."  
* Hobbyist                      object - Do you code as a hobby?  
* Age                          float64 - What is your age (in years)? If you prefer not to answer, you may leave this question blank.  
* Age1stCode                    object - At what age did you write your first line of code or program? (e.g., webpage, Hello World, Scratch project)  
* CompFreq                      object - Is that compensation weekly, monthly, or yearly?  
* CompTotal                    float64 - What is your current total compensation (salary, bonuses, and perks, before taxes and deductions), in `CurrencySymbol`? Please enter a whole number in the box below, without any punctuation. If you are paid hourly, please estimate an equivalent weekly...  
* ConvertedComp                float64 - Salary converted to annual USD salaries using the exchange rate on 2020-02-19, assuming 12 working months and 50 working weeks.  
* Country                       object - Where do you live?  
* CurrencyDesc                  object - Which currency do you use day-to-day? If your answer is complicated, please pick the one you're most comfortable estimating in.  
* CurrencySymbol                object - Which currency do you use day-to-day? If your answer is complicated, please pick the one you're most comfortable estimating in.  
* DatabaseDesireNextYear        object - Which database environments have you done extensive development work in over the past year, and which do you want to work in over the next year? (If you both worked with the database and want to continue to do so, please check both boxes in that row.)  
* DatabaseWorkedWith            object - Which database environments have you done extensive development work in over the past year, and which do you want to work in over the next year? (If you both worked with the database and want to continue to do so, please check both boxes in that row.)  
* DevType                       object - Which of the following describe you? Please select all that apply.  
* EdLevel                       object - Which of the following best describes the highest level of formal education that you’ve completed?  
* Employment                    object - Which of the following best describes your current employment status?  
* Ethnicity                     object - Which of the following describe you, if any? Please check all that apply. If you prefer not to answer, you may leave this question blank.  
* Gender                        object - Which of the following describe you, if any? Please check all that apply. If you prefer not to answer, you may leave this question blank.  
* JobFactors                    object - Imagine that you are deciding between two job offers with the same compensation, benefits, and location. Of the following factors, which 3 are MOST important to you?  
* JobSat                        object - How satisfied are you with your current job? (If you work multiple jobs, answer for the one you spend the most hours on.)  
* JobSeek                       object - Which of the following best describes your current job-seeking status?  
* LanguageDesireNextYear        object - Which programming, scripting, and markup languages have you done extensive development work in over the past year, and which do you want to work in over the next year? (If you both worked with the language and want to continue to do so, please check b...  
* LanguageWorkedWith            object - Which programming, scripting, and markup languages have you done extensive development work in over the past year, and which do you want to work in over the next year? (If you both worked with the language and want to continue to do so, please check b...  
* MiscTechDesireNextYear        object - Which other frameworks, libraries, and tools have you done extensive development work in over the past year, and which do you want to work in over the next year? (If you both worked with the framework and want to continue to do so, please check both b...  
* MiscTechWorkedWith            object - Which other frameworks, libraries, and tools have you done extensive development work in over the past year, and which do you want to work in over the next year? (If you both worked with the framework and want to continue to do so, please check both b...  
* NEWCollabToolsDesireNextYear  object - Which collaboration tools have you done extensive development work in over the past year, and which do you want to work in over the next year? (If you worked with the tool and want to continue to do so, please check both boxes in that row.)  
* NEWCollabToolsWorkedWith      object - Which collaboration tools have you done extensive development work in over the past year, and which do you want to work in over the next year? (If you worked with the tool and want to continue to do so, please check both boxes in that row.)  
* NEWDevOps                     object - Does your company have a dedicated DevOps person?  
* NEWDevOpsImpt                 object - How important is the practice of DevOps to scaling software development?  
* NEWEdImpt                     object - How important is a formal education, such as a university degree in computer science, to your career?  
* NEWJobHunt                    object - In general, what drives you to look for a new job? Select all that apply.  
* NEWJobHuntResearch            object - When job searching, how do you learn more about a company? Select all that apply.  
* NEWLearn                      object - How frequently do you learn a new language or framework?  
* NEWOffTopic                   object - Do you think Stack Overflow should relax restrictions on what is considered “off-topic”?  
* NEWOnboardGood                object - Do you think your company has a good onboarding process? (By onboarding, we mean the structured process of getting you settled in to your new role at a company)  
* NEWOtherComms                 object - Are you a member of any other online developer communities?  
* NEWOvertime                   object - How often do you work overtime or beyond the formal time expectation of your job?  
* NEWPurchaseResearch           object - When buying a new tool or software, how do you discover and research available solutions? Select all that apply.  
* NEWPurpleLink                 object - You search for a coding solution online and the first result link is purple because you already visited it. How do you feel?  
* NEWSOSites                    object - Which of the following Stack Overflow sites have you visited? Select all that apply.  
* NEWStuck                      object - What do you do when you get stuck on a problem? Select all that apply.  
* OpSys                         object - What is the primary operating system in which you work?  
* OrgSize                       object - Approximately how many people are employed by the company or organization you currently work for?  
* PlatformDesireNextYear        object - Which platforms have you done extensive development work in over the past year, and which do you want to work in over the next year? (If you both worked with the platform and want to continue to do so, please check both boxes in that row.)  
* PlatformWorkedWith            object - Which platforms have you done extensive development work in over the past year, and which do you want to work in over the next year? (If you both worked with the platform and want to continue to do so, please check both boxes in that row.)  
* PurchaseWhat                  object - What level of influence do you, personally, have over new technology purchases at your organization?  
* Sexuality                     object - Which of the following describe you, if any? Please check all that apply. If you prefer not to answer, you may leave this question blank.  
* SOAccount                     object - Do you have a Stack Overflow account?  
* SOComm                        object - Do you consider yourself a member of the Stack Overflow community?  
* SOPartFreq                    object - How frequently would you say you participate in Q&A on Stack Overflow? By participate we mean ask, answer, vote for, or comment on questions.  
* SOVisitFreq                   object - How frequently would you say you visit Stack Overflow?  
* SurveyEase                    object - How easy or difficult was this survey to complete?  
* SurveyLength                  object - How do you feel about the length of the survey this year?  
* Trans                         object - Are you transgender?  
* UndergradMajor                object - What was your primary field of study?  
* WebframeDesireNextYear        object - Which web frameworks have you done extensive development work in over the past year, and which do you want to work in over the next year? (If you both worked with the framework and want to continue to do so, please check both boxes in that row.)  
* WebframeWorkedWith            object - Which web frameworks have you done extensive development work in over the past year, and which do you want to work in over the next year? (If you both worked with the framework and want to continue to do so, please check both boxes in that row.)  
* WelcomeChange                 object - Compared to last year, how welcome do you feel on Stack Overflow?  
* WorkWeekHrs                  float64 - On average, how many hours per week do you work? Please enter a whole number in the box.  
* YearsCode                     object - Including any education, how many years have you been coding in total?  
* YearsCodePro                  object - NOT including education, how many years have you coded professionally (as a part of your work)?  
