# English Translation of Lecture 2: Introduction

Source: `Lecture2_intro.pdf`

Below is a slide-by-slide English rendering of the lecture content, with the text described by where it appears on each slide.

---

## Slide 1
**Center of slide, large title:**  
**Project Life Cycle in Data Science**

**Below title, centered:**  
**Judith Somekh**

**Top-left:**  
A decorative “data science” image.

---

## Slide 2
**Top-left title:**  
**Business DS life cycle: The CRISP data mining process**

**Left-side bullet list:**
- CRISP – Cross Industry Standard Process for Data Mining (CRISP-DM; Shearer, 2000)
- An iterative process – usually the problem is not solved after one iteration
- The first iteration serves as an exploration of the data
- The first and second steps are another cycle

**Right/center:**  
A CRISP-style lifecycle diagram showing:
- Business Understanding
- Data Understanding
- Data Preparation
- Modeling
- Evaluation
- Deployment  
with arrows indicating iteration.

---

## Slide 3
**Main slide content:**  
A CRISP lifecycle diagram similar to Slide 2.

**Highlighted in red:**  
**Data Understanding**

No additional substantive text besides the diagram.

---

## Slide 4
**Top title:**  
**2. Data Gathering & Understanding**

**Below title / bilingual subtitle:**  
**Data collection & understanding**

This is a section divider slide.

---

## Slide 5
**Top title:**  
**2. Data gathering & understanding**

**Bullets in Hebrew, translated to English:**
- The data include the raw material available from which the solution will be built.
- Usually, finding the right data takes time and effort.
- Data are often collected from multiple sources.
- What are some of the problems that can exist in data?

---

## Slide 6
**Top title:**  
**2. Data gathering & understanding**

**Main bullet list: “Some of the questions worth considering are:”**
- What data do I need for my project?
- Where are the data located?
- How can I obtain them?
- What are the costs?
- What is the most efficient way to store and access all of this?
- How do we preserve data privacy and confidentiality?

---

## Slide 7
**Top title:**  
**2. Data gathering & understanding**

**Bullets:**
- It is important to understand the strengths and limitations of the data, because there is rarely an exact match between the data and the problem.
- Historical data are often collected for purposes unrelated to the current business problem, or with no explicit purpose at all (for example, medical records).
- For example, a customer database, a transaction database, and a marketing response database contain different information, may cover different overlapping populations, and may have different levels of reliability.
- Data costs may vary. Some data will be available for free, while others will need to be purchased or will require effort to obtain (for example, GEO, the Israeli Digital Health Project).
- Sometimes the data do not exist, and entire projects will be required to organize their collection (for example, gene expression data require performing experiments).
- A critical part of the data understanding stage is estimating the costs and benefits of each data source.

---

## Slide 8
**Large Hebrew headline over a news screenshot:**  
**Free medical information for researchers and start-up companies**

**Main visual content:**  
News/article screenshots about digital health and access to medical data.

This slide is mainly an example/illustration.

---

## Slide 9
**Top title:**  
**2. Data understanding: Fraud Detection**

**Main text:**
As data understanding progresses, solution paths may change direction in response, and the team’s efforts may even split.

**Example:**  
Fraud detection – data mining is widely used for fraud detection, and many fraud detection problems include classic data mining tasks.

Sometimes fraud problems that initially look similar turn out to be fundamentally different during the data understanding process.

**Bottom question:**  
**Catching credit card fraud: how would we do that?**

---

## Slide 10
**Top title:**  
**2. Data understanding: Fraud Detection**

**Main text:**
Catching credit card fraud:

To build a predictive model for fraud, we need to label actions as fraudulent / legitimate.

**Questions:**
- Who will perform the labeling?
- How will we identify fraud?
- Who will identify it?
- Is the identification reliable?

---

## Slide 11
**Top title:**  
**2. Data understanding: Fraud Detection**

**Main text:**
Catching credit card fraud:

Charges appear in each customer’s account, so fraudulent charges are usually detected—if not initially by the company, then later by the customer when reviewing account activity.

**Bullets:**
- We can assume that almost all fraud is detected and labeled reliably, because the legitimate customer and the person committing the fraud are different people with opposite interests.
- Credit card transactions therefore have reliable labels (fraud or legitimate), which can be used to train a machine learning model.

---

## Slide 12
**Top title:**  
**2. Data understanding**

**Main text:**
**Medicare fraud:** this is a huge problem in the United States, costing billions of dollars each year.

The fraudsters are healthcare providers who submit false claims for various treatments for patients.

**Bottom question:**  
**Is this a conventional fraud detection problem?**

**Right side:**  
Illustrative medical images.

---

## Slide 13
**Top title:**  
**2. Data understanding**

**Main text repeats and expands:**
Medicare fraud is a huge problem in the United States, costing billions of dollars per year.

The fraudsters are healthcare providers submitting false claims for various treatments for patients.

**Bottom question:**  
**Is this a conventional fraud detection problem?**

**Additional bullet at lower left:**
- When we examine the relationship between the business problem and the data, we understand that the problem is significantly different.

**Questions at bottom:**
- Why?
- How will we identify fraud?
- Who identifies it?

---

## Slide 14
**Top title:**  
**2. Data understanding**

**Main text: Example: Medicare fraud**
- The perpetrators of fraud—healthcare providers submitting false claims, and sometimes their patients—are also legitimate service providers using the billing system.
- The people committing the fraud are a subset of legitimate users; there is no separate disinterested party that will accurately declare which claims are “correct.”
- As a result, Medicare billing data do not contain a reliable target variable indicating fraud, so a supervised learning approach that might work for credit card fraud is not relevant here.
- Such a problem usually requires unsupervised approaches such as clustering, anomaly detection, and co-occurrence grouping of similar data.

**Right side:**  
Illustrative images.

---

## Slide 15
**Top title:**  
**2. Data Science – Analysis methods**  
**Supervised vs. unsupervised methods**

**Main text:**
Statistical learning lies at the intersection of computer science and statistics and refers to a set of tools for understanding data. It combines statistical methods, computational methods, and methods from machine learning.

**Bullets:**
- **Supervised learning:** building a statistical model for predicting or estimating an output based on one or more inputs.
- **Unsupervised learning:** inputs exist, but there is no known corresponding output. Even so, we can learn about relationships and structure from the data. There is no response variable that “supervises” the analysis.

---

## Slide 16
**Top title:**  
**2. Data gathering & understanding**

**Bullets:**
- The fact that both cases are called fraud detection problems is based on a superficial similarity that is actually misleading, because they are two different cases requiring different analyses.
- In data understanding, we must dig beneath the surface to uncover the structure of the business problem and the available data for understanding it, and then match them to one or more data mining and analysis tasks requiring the knowledge, science, and technology we possess.
- It is not unusual for a business problem to contain several data mining and analysis tasks, often of different kinds, requiring integration of the solutions to the different tasks.

---

## Slide 17
**Main slide content:**  
A CRISP lifecycle diagram.

**Highlighted in red:**  
**Data Preparation**

No additional substantive text.

---

## Slide 18
**Top title:**  
**3. Data Cleaning & Preparation**

**Below title / subtitle:**  
**Cleaning and preparing data**

Section divider slide.

---

## Slide 19
**Top title:**  
**3. Data Cleaning & Preparation**

**Main text:**
- Powerful data analysis techniques exist, but they are still limited by certain requirements imposed on the data they use.
- Data entered into analysis usually need to be represented differently from the original form in which they were collected or delivered, and this often requires conversion and cleaning efforts.

**Bottom question:**  
**What kinds of problems can our data have?**

---

## Slide 20
**Top title:**  
**3. Data Cleaning & Preparation**  
**types of problems to be handled**

**Bullets:**
- Inconsistencies
- Duplicates (same record, different values)
- Labels: in the same column some rows could be labeled 0 or 1, while others could be labeled no or yes
- Data types: some of the 0s might be integers, while others could be strings
- Misspelling: for categorical variables, some categories could be misspelled or use different capitalization, such as both `male` and `Male`
- Missing values
- Should they be removed or inferred (imputation)?
- Why not remove them? So what can we do?
- If not handled, they can cause many errors during analysis

**Bottom-right question:**  
**How would you solve them?**

---

## Slide 21
**Top title:**  
**3. Data Cleaning & Preparation**  
**types of problems to be handled**

**Bullets:**
- Data conversions
- Format: converting data into tabular format
- Types of data: converting to different data types
- Some analysis techniques are designed for symbolic/categorical data, while others handle only numeric values, or discrete values while the original data are continuous
- Different scales (for example Fahrenheit/Celsius)
- Cleaning noise/confounders
- Example: gene expression experiments
- Outlier detection
- Why can outliers be a problem?
- Normalization and standardization
- Numerical values often need to be normalized or scaled so that they are comparable (for example in PCA)

---

## Slide 22
**Large Hebrew text on left:**  
**A Mars lander crashed because of a unit conversion error**

**Right side:**  
A screenshot of an English news article about a Mars lander crash due to a data glitch / unit error.

This is an illustrative example.

---

## Slide 23
**Title area:**  
**Data leakage**

**Bullets:**
- Leakage is a situation in which a variable collected in historical data provides information about the target variable—information that appears in the historical data but is not actually available when a decision must be made.
- **Example 1:** We want to predict whether a customer will be a “big spender”; knowing the categories of items purchased (or the amount of tax paid) may be highly predictive, but these are not known at decision time.
- **Example 2:** When predicting whether, at a certain point in time, a website visitor will end her session or continue to another page, the variable “total number of webpages visited in the session” is predictive. However, that total is only known after the session ends—at which point the target is already known.

---

## Slide 24
**Main slide content:**  
CRISP lifecycle diagram.

**Highlighted in red:**  
**Modeling**

No additional substantive text.

---

## Slide 25
**Top title:**  
**4. Data Exploration & Modeling**

**Below title / subtitle:**  
**Data exploration and models**

Section divider slide.

---

## Slide 26
**Top title:**  
**4. Data Exploration & Modeling**

**Bullets:**
- The actual data analysis process is based on computational techniques, statistical methods, and algorithms.
- The result of modeling is some form of model that finds patterns and structures in the data.

---

## Slide 27
**Top title:**  
**4.1 Data Exploration**

**Main statement at top:**  
We must understand the patterns, problems, and biases in the data.

**Bullets:**
- This is done by sampling and analyzing a random subset of the data from the full dataset.
- Use histograms or distribution curves to see the general trend, or even build an interactive visualization that allows drilling down to individual data points.
- Investigate the story behind outliers.
- Begin forming hypotheses about the data and the problem we are trying to solve or analyze.

**Examples at bottom:**
- In predicting students’ grades, you could examine the relationship between grades and sleep.
- In predicting real-estate prices, you could draw prices as a spatial heatmap to see whether you can detect trends.

---

## Slide 28
**Title:**  
**Heatmaps: State-by-State Guide to Taxes**

**Legend on left:**
- Most Tax-Friendly
- Tax-Friendly
- Mixed
- Not Tax-Friendly
- Least Tax-Friendly

**Top-right note:**  
Red = least friendly  
Dark blue = most friendly

**Main visual:**  
A U.S. map heatmap example.

---

## Slide 29
**Title:**  
**Heatmap**

**Bullets on left:**
- Patients with cancer and healthy individuals
- The features of each patient are represented by thousands of genes (measured mRNA levels), and the levels change between healthy and diseased states

**On the heatmap image:**
- **Genes (rows)**
- **Patients (columns)**

This slide illustrates biological data as a heatmap.

---

## Slide 30
**Top title:**  
**4.2 Feature engineering**

**Bullets:**
- In machine learning, a feature is a measurable property or characteristic of an observed phenomenon.
- For predicting student grades, one possible feature is the amount of sleep at night.
- **Question:** what other relevant feature ideas can you think of?
- In more complex tasks such as face recognition, features can be histograms counting the number of black pixels.
- According to Andrew Ng: “Coming up with features is difficult, time-consuming, requires expert knowledge. ‘Applied machine learning’ is basically feature engineering.”

---

## Slide 31
**Top title:**  
**4.2 Feature engineering**

**Bullets:**
- Feature engineering is the process of using domain knowledge to transform raw data into informative features that represent the business problem being solved.
- This stage directly affects the accuracy of the predictive model built in the next stage.
- Usually we perform two types of tasks in feature engineering:
  - **Feature selection** – choosing features relevant to the analysis
  - **Feature construction** – for example, combining features into one feature

---

## Slide 32
**Top title:**  
**4.2 Feature Selection**

**Bullets:**
- Feature selection is the process of removing features that add more noise than information.
- For this purpose we use filtering methods:
  - **Filter methods** – generate a statistical measure to assign a score to each feature
  - **Wrapper methods** – treat feature selection as a search problem and use heuristics to perform the search
  - **Embedded methods** – use machine learning itself to determine which features contribute best to accuracy

**Bottom visual:**  
A schematic showing all features, informative features, and selected features.

---

## Slide 33
**Top title:**  
**4.2 Feature Construction**

**Bullets:**
- Creating new features from original features.
- For example, when you have a continuous variable but domain knowledge says that only crossing a certain threshold matters.
- Given feature: subject’s age
- If the model only cares whether a person is an adult or a minor, we can place a threshold at age 18 and assign different categories to cases above and below it.
- Other threshold examples: sick/healthy, obese/thin.
- Merging multiple features to make them more informative by taking their sum, difference, or product.
- Example: predicting student grades.
- Given: features representing number of hours of sleep for a student each night.

**Bottom question:**  
**What processing would you perform on these features for prediction?**

---

## Slide 34
**Top title:**  
**4.2 Feature Construction**

This slide repeats the content from Slide 33 and adds the answer.

**Added line at bottom:**  
You should create a feature representing the student’s average amount of sleep.

---

## Slide 35
**Top title:**  
**4.3 Predictive Modeling**

**Bullets:**
- The actual analysis work!
- Includes:
  - Machine learning techniques for building a predictive model and testing its accuracy
  - Use of comprehensive statistical methods and tests to ensure that the model’s results are sensible and meaningful
- Based on the questions asked during the business understanding stage, this is where we decide which model to choose for the problem.
- This is never an easy decision, and there is no single correct answer.
- The chosen model (or models—and it is always preferable to test several) will depend on:
  - the size, type, and quality of your data,
  - how much time and computing resources you are willing to invest,
  - and the type of output you intend to produce.

---

## Slide 36
**Top title:**  
**4.3 Predictive Modeling – Evaluation**

**Main text:**
After training your model, it is critical to evaluate its quality and its success in prediction.

**Bullets:**
- Cross-validation—usually k-fold cross-validation—is commonly used to measure model accuracy.
- This involves splitting the dataset into equally sized groups of instances, building a model on all but one group, and repeating the process with different held-out groups. This allows the model to be trained across all the data rather than relying on a simple train-test split.
- Charts such as ROC curves, which show the true positive rate against the false positive rate, are also used to measure model success.

---

## Slide 37
**Top title:**  
**4.4 Visualization**

**Bullets:**
- Data visualization seems simple, but often it is one of the most challenging tasks.
- Data visualization combines communication, psychology, statistics, and art.
- The ultimate goal is to communicate the data in a simple, effective, and visually pleasing way.
- After extracting the intended insights from your model, you must represent them in a way that the various stakeholders in the project can understand.
- The chart should be clear and tell the story.

---

## Slide 38
**Main slide content:**  
CRISP lifecycle diagram.

**Highlighted in red:**  
**Evaluation**

No additional substantive text.

---

## Slide 39
**Top title:**  
**5. Evaluation (in the business context)**

**Main text:**
**Goal 1:** Rigorously evaluate the results of the data analysis and ensure that they are valid and reliable before moving on.

**Bullets:**
- If we search enough, we will find patterns in any dataset—but they may not survive more careful testing.
- We want to be sure that the models and patterns extracted from the data are real regularities and not just strange phenomena or sampling artifacts.

---

## Slide 40
**Top title:**  
**5. Evaluation (in the business context)**

**Bullets:**
- **Controlled evaluation:** first test a model within a controlled “laboratory” process.
- **Evaluation of external considerations:** even if a model passes strict evaluation tests in a controlled environment, there may still be external considerations that make it impractical.
- For example, a common flaw in detection analyses (such as fraud detection, spam detection, and intrusion monitoring) is that they generate too many false alarms.
- A model may appear highly accurate in laboratory terms, but evaluation in the actual business context may reveal that it still produces too many false alarms to be economically feasible.
- Additional considerations must be addressed, such as:
  - how much it will cost the team to deal with all those false alarms,
  - what the meaning and cost of customer dissatisfaction will be.

---

## Slide 41
**Top title:**  
**5. Evaluation**

**Main text:**
Evaluation in the real environment: in some cases we will extend evaluation into the real environment, for example by instrumenting a live system in the real setting to allow randomized experiments.

**Bottom question:**  
**Why do you think this is necessary?**

---

## Slide 42
**Top title:**  
**5. Evaluation**

**Main text repeats and expands:**
Evaluation in the real environment: in some cases we will extend evaluation into the real environment, for example by using instrumentation in a live system that enables randomized experiments.

**Example:**
- In the example of customer churn in cellular companies—if laboratory testing suggests that a data-driven model can help reduce churn, we may want to move to real-world evaluation in a live system that applies the model randomly to some customers while keeping others as a control group.
- Such experiments must be carefully planned.

**Bottom prompt:**  
**Considering the changing environment: what might change when the model is implemented in the company?**

---

## Slide 43
**Top title:**  
**5. Evaluation**

**Text similar to Slide 42, with an added final point:**
- We may also want to train our systems to ensure that the world does not change in a way that harms the model’s decision-making.
- For example, behavior can change—in some cases, such as fraud or spam, directly in response to deployment of the models.

---

## Slide 44
**Top title:**  
**5. Evaluation → 1. Business Understanding**

**Main text:**
We want to ensure that the model meets the original business goals.

After going through the entire lifecycle, it is time to return to the drawing board. Remember, this is a circular lifecycle, so it is an iterative process.

This is the point where you evaluate how the success of your model relates back to your original understanding of the business and its goals.

**Questions in the text:**
- Does it address the problems that were identified?
- Does the analysis yield solid solutions?

If new insights arose during the first iteration of the lifecycle (which usually happens), you can now inject that new knowledge into the next iteration in order to produce even stronger insights and use the power of data to generate strong and exceptional outcomes for your business or project.

---

## Slide 45
**Large question on left:**  
**Q: What do data scientists spend the most time doing?**

**Below in Hebrew, translated:**  
What percentage of the time do you think each task takes?

**Right side:**  
CRISP lifecycle diagram.

This is a prompt/discussion slide.

---

## Slide 46
**Top title:**  
**Cleaning Big Data: Most Time-Consuming, Least Enjoyable Data Science Task, Survey Says / Forbes**

**Main text:**
A survey of about 80 data scientists was conducted for the second year in a row by CrowdFlower, provider of a “data enrichment” platform for data scientists.

**Highlights:**
- Most are happy with having the sexiest job of the 21st century.
- Data preparation accounts for about 80% of the work of data scientists.
- Data scientists spend 60% of their time cleaning and organizing data. Collecting data sets comes second at 19%, meaning data scientists spend around 80% of their time preparing and managing data for analysis.
- 76% of data scientists view data preparation as the least enjoyable part of their work.
- 57% regard cleaning and organizing data as the least enjoyable part, and 19% say this about collecting datasets.

---

## Slide 47
**Top title:**  
**Big Data Survey / Forbes**

**Main text:**
A survey of about 80 data scientists was conducted for the second year in a row by CrowdFlower, provider of a “data enrichment” platform for data scientists.

**Highlights:**
- Most are happy with having the sexiest job of the 21st century.
- Data preparation accounts for about 80% of the work of data scientists.

**Right side / chart text:**  
**What data scientists spend the most time doing**
- Building training sets: 3%
- Cleaning and organizing data: 60%
- Collecting data sets: 19%
- Mining data for patterns: 9%
- Refining algorithms: 4%
- Other: 5%

**Left side:**  
A donut/pie chart visualizing those percentages.
