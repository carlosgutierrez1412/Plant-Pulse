#### DEPARTMENT OF ELECTRICAL AND COMPUTER ENGINEERING

# GARDEN MONITORING SYSTEM

# Final Proposal

## Senior Design I: Ethics, Communications, and Constraints

## EEL4920 RVCC 1245

## Instructor: Dr. Wilmer Arellano

## Mentor: Dr. Yu Du

## 07 /1 8 /

## Group 10


## TABLE OF CONTENTS


A. Technical Results ..............................................................................................................


## ACKNOWLEDGMENT

On behalf of Team 10, we thank Dr. Yu Du for his invaluable mentorship throughout the
development of the PlantPulse project. His insightful feedback has been monumental in refining
our approach to the system.

We thank Professor Wilmer Arellano for his guidance and comprehensive education. His
teachings have not only deepened our understanding of technological development but inspired us
to innovate responsibly and effectively.

## ABSTRACT

The PlantPulse system is a cutting-edge garden management solution that automates and
optimizes plant care. Powered by a 120V 50-60 Hz AC supply, it monitors key environmental


factors, including temperature, humidity, soil moisture, pH, and nutrient levels (nitrogen,
phosphorus, potassium). Through an intuitive web interface, users can remotely control lighting,
irrigation, and other settings via smartphones or desktops. At the heart of the system is an Arduino
Nano R3-based board with the ATmega328P microcontroller, integrated with digital sensors
converted from RS485 for accurate data collection. This data is transmitted via LoRaWAN,
enabling real-time plant health tracking. PlantPulse also leverages machine learning to adapt to
optimal growing conditions, enhancing plant vitality and boosting user productivity. Combining
advanced technology with ease of use, PlantPulse offers a fully automated, sustainable gardening
experience that empowers users to monitor and manage their plants from anywhere, transforming
the future of gardening.

## LIST OF TABLES

Table 1 Client Attributes **............................................................................................................**. 11

Table 2 **Team member’s attributes .............................................................................................** .. 12

Table 3 Combined attributes **.........................................................................................................** 12



## I. LIST OF FIGURES


- ACKNOWLEDGEMENT
- ABSTRACT
- LIST OF TABLES
- LIST OF FIGURES
- I. EXECUTIVE SUMMARY
- II. PROBLEM STATEMENT
   - A. Project Objectives
   - B. Constraints
- III. ASSUMPTIONS AND LIMITATIONS
   - A. Assumptions
   - B. Limitations
- IV. NEEDS FEASIBILITY ANALYSIS
   - A. Needs Analysis
   - B. Need Specification
   - C. Feasibility Analysis
   - D. Marketability
- V. RISK ANALYSIS
- VI. OPERATING ENVIRONMENT
- VII. INTENDED USER(S) AND INTENDED USE(S)
   - A. Intended user(s)
   - B. Intended use(s)
- VIII. BACKGROUND
- IX. INTELLECTUAL PROPERTY CONSIDERATIONS
- X. GLOBALIZATION
- XI. STANDARD CONSIDERATION
- XII. HEALTH AND SAFETY CONSIDERATIONS
- XIII. ENVIRONMENTAL CONSIDERATIONS
- XIV. SUSTAINABILITY CONSIDERATIONS
- XV. MANUFACTURABILITY CONSIDERATIONS
- XVI. ETHICAL CONSIDERATIONS AND SOCIAL IMPACT............................................
   - A. Ethical Considerations
   - B. Social Impact
- XVII. CONCEPT DEVELOPMENT
      - A. Concept Fan
      - B. Alternative Options......................................................................................................
      - C. Concept Selection
- XVIII. END PRODUCT DESCRIPTION AND OTHER DELIVERABLES
   - A. End Product Description
   - B. Functions
   - C. Specifications
   - D. Other Deliverables
- XIX. PLAN OF ACTION
   - A. Statement of Work (SOW)
   - B. Work Breakdown Structure (WBS)
   - C. Project Milestones
   - D. Gantt Charts
- XX. MULTIDISCIPLINARY ASPECTS
- XXI. PERSONNEL
- XXII. BUDGET
- XXIII. RESULTS EVALUATION
- XXIV. LIFE-LONG LEARNING B. Globalization Retrospective
- XXV. CONCLUSION
- XXVI. REFERENCES
- XXVII. APPENDICES
   - A. Team Contract
   - B. Intellectual Property Contract
- XXVIII. SIGNATURES PAGE
- Table 4 Technical Feasibility
- Table 5 Resource Feasibility ..........................................................................................................
- Table 6 Economic Feasibility .........................................................................................................
- Table 7 Scheduling Feasibility .......................................................................................................
- Table 8 Cultural Feasibility ..................................................................
- Table 9 Legal Feasibility ..............................................................................................................
- Table 10 Marketing Feasibility......................................................................................................
- Table 11 Obtaining weights .........................................................................................................
- Table 12 Weighted Scale .............................................................................................................
- Table 13 Bloomie’s Features.
- Table 14 Geodrop’s Features
- Table 15 Risk Expoosure Matrix ...................................................................................................
- Table 16 Actions To Minimize Risks ..............................................................................................3
- Table 17 Claims ........................................................................................................................
- Table 18 Non Infringement ..........................................................................................................
- Table 19 Options For Responding to the Ethical Dilemma ....................................................................
- Table 20 Philosophies For Responding To The Ethical Dilemma ............................................................
- Table 21 Weight Calculation Table ................................................................................................
- Table 22 Concept Selection Table .................................................................................................
- Table 23 Level 0 Inputs, Outputs, And Functionality ...
- Table 24 Level 1 Inputs, Outputs, And Functionality ..........................................................................
- Table 25 Level 2 Inputs, Outputs, And Functionality of Digital Sensors
- Table 26 Level 2 Inputs, Outputs, And Functionality Of Microcontrollers
- Table 27 Level 2 Inputs, Outputs, And Functionality Of The Microcomputer ............................................
- Table 28 Level 2 Inputs, Outputs, And Functionality Of The Irrigation System ..........................................
- Table 29 Level 2 Inputs, Outputs, And Functionality Of The Lighting System ..
- Table 30 Level 2 Inputs, Outputs, And Functionality Of The Lighting System ............................................
- Table 31 Module Specifications for PlantPulse ..................................................................................
- Table 32 Budget ......................................................................................................................
- Figure 0 PlantPulse Schematic Diagram............................................................................................
- Figure 1 Gardyn AI System
- Figure 2 The block design of the Bloomiee Project
- Figure 3 Bloomiee Component Make-Up
- Figure 4 GeoDrops Block Design
- Figure 5 GeoDrops Ideal Configuartion & Utilization
- Figure 6 Fault Tree Analysis
- Figure 7 NIWA GROW HUB+- SMART AUTOMATION & MONITORING SYSTEM
- Figure 8 NIWA Grow Hub+ System Block Design
- Figure 9 Farmbot Genesis V1.7
- Figure 10 Farmbot Genesis V1.7
- Figure 11 NEST Learning Thermostat
- Figure 12 NEST Learning Thermostat Device System Block Diagram
- Figure 13 Circuit block diagram of the plant monitoring invention
- disclosed embodiments Figure 14 A schematic diagram of a system for automatic plant monitoring is utilized to describe the various
- yield desired harvest traits. Figure 15 An AI-powered autonomous plant-growth optimization system automatically adjusts input variables to
- Figure 16 displayed below represents the trademark to be used for our product
- Figure 17 CONCEPT FAN FOR PLANTPULSE
- Figure 18 ALTERNATIVE 1 “PLANTPULSE ECO”...........................................................................
- Figure 19 ALTERNATIVE 1I “PLANTPULSE”...............................................................................
- Figure 20 ALTERNATIVE III “PLANTPULSE V2”
- Figure 21 ALTERNATIVE IV “PLANTPULSE SHORT RANGE”
- Figure 22 Level 0 view of PlantPulse
- Figure 23 Level 1 view of PlantPulse
- Figure 24 Level 2 view of the digital sensors.
- Figure 25 Level 2 view of the microcontroller (Arduino Nano R3)
- Figure 26 Level 2 view of the microcontroller (Raspberry Pi 4 model B)
- Figure 27 Level 2 view of the irrigation system.
- Figure 28 Level 2 view of the lighting system
- Figure 29 Flowchart of how PlantPulse works
- Figure 30 Work Breakdown Structure ............................................................................................
- Figure 31 Gantt Chart Part
- Figure 32 Gantt Chart Part


Figure 33 Pert Chart **..................................................................................................................**. 94

## I. EXECUTIVE SUMMARY

```
PlantPulse – AI-Powered Garden Monitoring System
Team Number: 10 Team Name: PlantPulse
```
```
Mentor: Dr. Yu Du Team Leader: Pedro Ojeda
```
```
Team Member: Richard Cui Team Member: Jonathan Fleurisma
```
```
Team Member: Carlos Gutierrez Team Member: Abigail Sardine-Laforte
```
This paper will introduce Team 10’s
project of an interconnected IoT ecosystem
of sensors and components for monitoring
the soil parameters and, in turn, the health of
plants. The report will display the research
conducted, methods of analysis, and the
team’s critical brainstorming strategies

```
regarding the setup of sensors and other
connected modules. PlantPulse addresses
critical challenges in agriculture such as
environmental unpredictability and resource
inefficiency by leveraging an interconnected
IoT ecosystem. This system enhances plant
health monitoring through advanced sensors
```

that assess soil conditions and environmental
parameters.

The project aims to enhance agricultural
productivity and sustainability through real-
time data monitoring and automated system
adjustments. The objectives include:

1. Easy to use
    1.1 Easy to implement.
    1.2 Low maintenance
    1.3 Automatically water,
       fertilize, and provide
       lighting.
2. Accurate readings
    2.1 Soil sensor reports
       accurate readings.
    2.2 Temperature, humidity,
       pH, nitrogen, phosphorus,
       and potassium.
    2.3 Machine learning will
       learn the best growing
       conditions for plants.
PlantPulse integrates various sensors and
components into a user-friendly platform,
allowing for precise monitoring of soil
moisture, temperature, and nutrient levels.
The system is designed for ease of use and
minimal maintenance, supporting diverse
agricultural environments and regulatory
landscapes.

```
Fig. 0 PlantPulse Schematic Diagram
Important Sections:
```
- Background
- Environmental Considerations
- Sustainability Considerations
- End Product Description
- Plan of Action
- Results Evaluation
PlantPulse represents a significant
advancement in agricultural technology,
promising to transform how environmental
conditions are managed in farming. The
project aims for high efficiency and
sustainability and ensures adaptability across
various global markets, making it a viable
solution for modern agricultural needs.

## III. PROBLEM STATEMENT

The agricultural industry provides necessary food to communities and surrounding
establishments. However, it can be one of the most unstable production lines, subject to price
volatility, substantial upfront costs, weak bargaining power, government policies, and especially
the changing climate. Climate change increases the odds of worsening droughts in many parts of
the world. Certain areas are at more significant risk of experiencing more frequent, intense, and
longer-lasting droughts, affecting crops and their livelihoods. Food insecurity can lead to cost
spikes, which, in turn, can cause social unrest, migration of native populations, and famine.

The team’s proposed solution is PlantPulse, a connected network of sensors that records and
reports the dynamic qualities of soil used for growing plants. A companion application on both
smartphones and desktop environments will be provided to relay the information to users. The
application will make it easier to monitor the health of the plants and soil by sending notifications
if parameters are not within optimal conditions. The parameters range from general aspects of soil
humidity and temperature to more specific attributes, such as the contents of nutrients like
nitrogen, phosphorus, and potassium, depending on the monitored plant.


A. Objectives

```
1) Safety
1.1 The system should be secure against cyber threats.
```
```
1.2 The system should be reliable and safe to handle.
2) Ease of Use
2.1 The system should be easy to construct.
```
```
2.2 The system should be easy to understand with manuals and documents.
2.3 The system should have minimal maintenance.
2.4 The system should be easy to deconstruct.
3) Modularity
```
```
3.1 The system should have options to support future hardware expansions.
3.2 The system should have options for wireless/wired connections.
4) Scalability
```
```
4.1 The system should have options to increase the range of its network.
4.2 The system should be able to handle more sensors.
5) Marketability
```
```
5.1 The system should send notifications if the soil parameters could be more optimal.
5.2 The system should track data in real-time.
5.3 The system should have a companion application.
5.4 The system should recommend how to improve soil conditions.
```
### B. Constraints

1. The system should be competitive, or lower, in pricing than comparable products.
2. The system should measure values accurately.
3. The system should be easy to implement.


## IV. ASSUMPTIONS AND LIMITATIONS

During the team’s research and brainstorming at various meetings, we identified several
features and constraints for our PlantPulse system. Features deemed critical and necessary to the
final design's function are prioritized, and others were set aside due to issues with implementation
or project constraints such as budget and hardware limitations. This section outlines the key
assumptions and limitations considered in designing and implementing the PlantPulse system.

### A. Assumptions

```
The assumptions for our proposed system are:
```
- The system will use only 50% of the microcontroller’s resources.
- Soil sensors will detect and log soil parameters.
- The wireless range will be sufficient to cover typical farm areas.
- The energy consumption will be low enough to maintain at least 24 hours of operation.
- The system will operate in a range of typical agricultural environmental conditions.

### B. Limitations

```
The limitations of our system are:
```
- The system will not correct or rectify any data; the raw data will be reported as is.
- The system is limited to detecting soil parameters.
- The system must be low-cost.


- The system must withstand temperatures from 0°C to 60°C.
- The system must be water and dust-resistant.
- The sensor units must be low-profile and unobtrusive.

## V. NEEDS FEASIBILITY ANALYSIS

The needs feasibility analysis is a critical part of any development process. All aspects of the
system will be examined to determine how feasible it is to implement. For the PlantPulse system,
it will have to meet the needs of its users effectively and efficiently. The analysis will see what
challenges must be resolved, including the accuracy of data recording and power management.
The system must reliably capture soil data and operate for a long time without recharging.

### A. Needs Analysis

A needs analysis is a systematic and organized process to identify and evaluate the specific
needs of desired users. This analysis will help the team produce a product that satisfies user
requirements during design. The first step involves interviewing businesses involved in plant care
to understand their specific desires and pain points. This information will guide the design and
development of the PlantPulse system, ensuring it meets the needs of its intended users effectively.

```
1) Client Interview:
```
This project's concept was first proposed in Spring 2024 in EEL 4933: Engineering
Entrepreneurship. Throughout the course, 100 interviews were conducted with organizations and
businesses related to plant care. The types of organizations include, but are not limited to,
condominiums, landscaping companies, irrigation system installers, botanical gardens, and
nurseries. The interviews were primarily conducted in person, with the rest of the interviews
conducted by phone. The feedback gathered is abridged (as most responses were similar in what
the interviewees wanted in a system and what they wanted to avoid during plant care) and
presented in Table I:

```
TABLE I. CLIENT ATTRIBUTES
```

```
Source Attribute
Interview The system should capture data accurately.
Interview The system should be cost-effective.
Interview The system should have minimal maintenance.
Interview The system should be able to integrate with watering systems.
Interview The system should record nutrients like nitrogen, phosphorus, and potassium.
Interview The system should record the humidity and temperature of the soil.
Interview The system should be a one-time installation.
```
2) Team Input:
The team elaborated on the existing attributes extracted from the interviews and brainstormed
for more attributes (that needed to be stated by the interviewees) to add to the design. Each team
member considered these elements if it was a beneficial feature to the design of the PlantPulse
system. The results of the attributes formulated by members through team meetings are shown in
Table II:

```
TABLE II. TEAM MEMBERS’ ATTRIBUTES
Source Attribute
Team The system should recommend actions to reduce plant loss through artificial intelligence.
Team The system should have options to expand its range.
Team The system should send notifications to remind users to tend to plant(s).
Team The system should implement LoRaWAN.
Team The system’s network should use clusters.
Team The system’s network should be secured against cyber-attacks.
Team The system should have a fully functional companion app on Android.
Team The system should be water, dust, and rust-resistant to the environment.
Team The system should have options for wired/wireless power.
Team The system should record pH and lighting.
```
3) Combined Attributes:
After obtaining attributes from both interviews and team members, the next step is to carefully
examine each attribute to determine if they are necessary and feasible for the functionality of the
PlantPulse system. During meetings, team members deliberated over the project design to choose
which attributes were the most notable features to have and which could be discarded. The final
combined attributes are presented in Table III, and attributes are categorized into objectives:

```
TABLE III. COMBINED ATTRIBUTES
```

```
Source Attribute Type
Interview The system should capture data accurately. Marketability
Interview The system should be cost-effective. Marketability
Interview The system should have minimal maintenance. Ease of Use
Interview The system should record the humidity and temperature of the soil. Marketability
Interview The system should be a one-time installation. Ease of Use
Team The system should have options to expand its range. Modularity
Team The system should send notifications to remind users. Marketability
Team The system should implement LoRaWAN. Scalability
Team The system’s network should be secured against cyber-attacks. Safety
Team The system should have a fully functional companion app on Android. Marketability
Team The system should be water, dust, and rust-resistant to the environment. Safety
Team The system should have options for wired/wireless power. Modularity
```
```
Team
```
```
The system should recommend actions to reduce plant loss through
artificial intelligence. Marketability
Team The system should record pH and lighting. Marketability
```
The table above lists the factors the team discussed were necessary to the system's design. Based
on the analysis of the interviews and team members’ suggestions, we believe Table III provides
the team with the specifics of the project parameters. The problem statement concerning the refined
objectives can then be supplied.

4) Problem Statement
The team’s project involves a network of sensors in the soil that will log and report data. The
system can expand its range through modular hardware expansion ports and use LoRaWAN for
its network. The sensors will record humidity/moisture level, temperature, and nutrients
(phosphorus, calcium, potassium) from the soil in real-time. The priorities for the system are safety
and ease of use. It will have a durable enclosure on the board, and the sensors will be water, dust,
and rust-resistant. The system should also be able to be installed one time and be low maintenance.

```
5) Objectives
```
1. Safety
    1.1 The system should be safe against cyber-attacks.
    1.2 The system should be water, dust, and rust resistant.
2. Ease of Use
    2.1 The system should be of minimal maintenance.
    2.2 The system should be a one-time installation.
3. Modularity
    3.1 The system should have hardware options to expand its operating range.


```
3.2 The system should have options to be powered by battery or DC.
```
4. Scalability
    4.1 The system should implement LoRaWAN in network communications.
5. Marketability
    5.1 The system should capture data accurately.
    5.2 The system should be cost-effective.

```
5.3 The system should record the soil's humidity/moisture and temperature.
5.4 The system should record the pH and lighting.
5.5 The system should send notifications to users via an Android companion app.
5.6 The system should recommend actions to be taken through artificial intelligence.
```
### B. Need Specification

The PlantPulse project's requirements include several critical, measurable criteria to ensure the
device effectively monitors and manages plant health. These details incorporate soil dampness
observation with 95% precision, temperature estimation from - 10 to 50°C, and light power
discovery from 0 to 100,000 lux. The device has a capacity of 1 GB for data storage and is made
to run for up to six months on a single charge. Network determinations demonstrate a remote scope
of 30 meters, while the UI holds back a nothing fulfillment rating of 4.5 out of 5. The gadget is
geared for strength, with a life expectancy of three years and an IP67 water opposition rating.
Additionally, it requires 0.5 watts of power to operate and updates sensor data every ten minutes.
The actual components of the gadget are 15x5x3 cm (about 1.18 in), with a complete load of 200
grams (about 7.05 oz), and the creation cost is assessed at 200 USD. A crucial specification is the
ability to abide by CE and FCC safety standards. The development of PlantPulse is guided by these
specifications, which ensure that each design objective is well-defined and measurable. The
development process can be streamlined, and the final product's effectiveness in monitoring plant
health can be evaluated by establishing precise metrics, target values, and units for each objective.
They are establishing precise metrics, target values, and units for each purpose. PlantPulse meets
the highest functionality and user satisfaction standards thanks to this structured approach, which
facilitates improvements and iterations and assists in achieving design objectives.


```
Fig 1. Gardyn AI System [ 2 ]
```
The indoor planting market is quickly developing, driven by the expansion of purchaser
premiums in the area of economical living and local produce. Two outstanding items in this space
are the Gardyn Home Unit 3.0 and PlantPulse. The two frameworks influence cutting-edge
innovation to work with indoor cultivating. However, they contrast essentially in their
methodologies, highlights, and target markets.

The Gardyn [ 1 ] Home Unit 3.0 is a computer-based, intelligence-controlled indoor nursery
intended to grow up to 30 plants in only two square feet, empowering clients to collect a new plate
of mixed greens consistently. Its champion element is its utilization of computer-based intelligence
to screen and enhance plant development, giving ongoing changes in accordance with guaranteed
ideal circumstances. This framework is exciting to metropolitan inhabitants with restricted space
and cultivating experience, as it offers a conservative, space-productive arrangement that requires
negligible client mediation. The Gardyn Home Pack 3.0 stresses convenience and manageability,
empowering independence and lessening dependence on locally acquired produce. Its complete
application support permits clients to screen and deal with their nursery from a distance, adding to
its comfort.

Interestingly, PlantPulse centers around a savvy cultivating framework that uses progressed
sensors and information examination to help plant development. It offers adaptability in the
number and kinds of plants developed, making it exceptionally adjustable. PlantPulse gives a
definite exam of plant well-being and development conditions, which is attractive to cultivating
fans and specialists who value top-to-bottom plant care. The framework estimates soil dampness,
light, temperature, and mugginess through its savvy sensors, giving experiences and proposals in
view of gathered information. PlantPulse likewise underscores local area commitment and


instructive assets, upgrading the client experience through an involved way to deal with
cultivating.

While contrasting the innovative methodologies of these frameworks, the Gardyn Home Unit
3.0 uses artificial intelligence for independent plant care, zeroing in on convenience and negligible
client mediation. Conversely, PlantPulse uses savvy sensors and information examination,
requiring more client commitment to likewise decipher the information and act. This
differentiation features their contrasting interest groups. The Gardyn Home Pack 3.0 is great for
metropolitan occupants, novices, and those with restricted time or space who are looking for a
precise cultivating arrangement. PlantPulse, then again, requests to cultivate devotees and
specialists who partake in an additional involved methodology and top-to-bottom plant care.

The framework configuration further separates these items. The Gardyn Home Unit 3.0 is
minimized and upward, boosting plant thickness in a little region, making it reasonable for clients
with restricted space. PlantPulse offers more customization and adaptability, considering different
plant designs and arrangements, which can be invaluable for clients with explicit plant inclinations
and more accessible space. Client experience likewise differs between the two frameworks. The
Gardyn Home Pack 3.0 stresses straightforwardness and comfort, with artificial intelligence taking
care of the more significant part of the planting assignments, making it easy to use for those with
occupied ways of life. PlantPulse, notwithstanding, centers around itemized checking and client
communication, giving a growth opportunity to clients who appreciate drawing in with their
cultivating cycle.

Regarding market situations, the Gardyn Home Pack 3.0's assets lie in its easy-to-understand,
space-effective, and artificial intelligence-driven plan, empowering nonstop gathers. Its principal
disadvantage may be the absence of commitment and customization a few clients want. PlantPulse,
with its point-by-point investigation, high customization, and solid client commitment, requests
an alternate fragment of the market. Be that as it may, it requires more client contribution and may
not be as space-effective as the Gardyn [ 1 ] framework.

Both Gardyn Home Unit 3.0 and PlantPulse offer extraordinary benefits in the indoor
cultivating market. Gardyn's [ 1 ] artificial intelligence-fueled, space-effective plan makes it ideal
for occupied metropolitan occupants looking for straightforwardness and supportability, while
PlantPulse requests additional connections with nursery workers who value point-by-point bits of
knowledge and customization. The decision between these frameworks relies upon the client's
inclinations for robotization versus active planting, as well as their accessible space and wanted
degree of commitment.

### C. Feasibility Analysis

Feasibility analysis assesses the viability of a proposed project through several vital steps.
Firstly, technical feasibility evaluates if the project can be implemented using existing technology
and resources, considering team capabilities and infrastructure availability. Economic feasibility
examines financial aspects, estimates costs and potential returns, and conducts a cost-benefit
analysis based on market factors. Operational feasibility checks if the project can function
effectively post-implementation, analyzing workflow, logistics, and potential disruptions. Lastly,
scheduling feasibility ensures the project can be completed within a reasonable timeframe,
considering dependencies and resource availability.

A weighted scale and weight computation table are essential for conducting a thorough
feasibility analysis. This table assigns weights to criteria based on their importance to project
success and evaluates each criterion on a numerical scale. For our product, each feasibility section


should be rated from 1 to 5, with 5 indicating high feasibility. After scoring, weights will be applied
to each criterion based on their significance and ultimately determined through stakeholder input
or group discussion. They are computing a weighted average score for each aspect, indicating
project feasibility and aiding stakeholders in making informed decisions about project
implementation.

```
1) Technical Feasibility
```
The technical feasibility assessment determines whether the current technology can complete
the project. Moreover, it assesses whether an innovation is necessary if the technology is
unavailable. All required technology already exists in our project's development; potential
challenges may arise while implementing various components. The average score obtained from
this section is 4. 7 5, as seen in Table IV.

```
TABLE IV. TECHNICAL FEASIBILITY
Attributes Score Why Solution
Does the technology exist? 5 All relevant technology needed
for our project exists.
```
```
No solution is necessary.
```
```
Is there any technical risk? 4 There could be risks regarding
components needing to be fixed
once combined.
```
```
Work with each component
separately to ensure
functionality.
Can it be obtained? 5 All necessary parts can be
obtained via online purchases.
```
```
No solution is required.
```
```
Are fundamentally new inventions required? 5 No new inventions are needed at
this time.
```
```
No solution is necessary.
```
```
Total 19
Average 4.
```
2) Resource Feasibility
Resource feasibility evaluates the availability and adequacy of resources required for the project.
This includes financial and human resources, materials, equipment, and facilities needed to execute
the project effectively. Assessing resource feasibility ensures that our project can be adequately
supported throughout its lifecycle, from initiation to completion, minimizing risks of resource
shortages or constraints that could impact project success. From Table V, we obtained an average
score of 4.63.

```
TABLE V. RESOURCE FEASIBILITY
Attributes Score Why Solution
Are the team's skills sufficient? 4.5 It is possible to be uncertain of
specific tasks.
```
```
Work as a team to help each
other solve problems.
Is our equipment sufficient for the project? 5 All equipment has been
purchased and obtained.
```
```
No solution is necessary.
```

```
Do we have enough team-mates? 5 We have enough team members
to complete all parts of the
project.
```
```
No solution is necessary.
```
```
Is there any risk associated with resources? 4 Finding references to assist with
any problems may take time and
effort.
```
```
Reach out to our mentor to
gather more insight.
```
```
Total 18.
Average 4.
```
```
3) Economic Feasibility
```
Economic feasibility examines the financial viability of a project by analyzing costs and
potential benefits. It involves estimating initial investment requirements, ongoing operational
costs, and expected revenue or savings the project generates. This analysis helps stakeholders
determine whether the expected financial returns justify the investment. Factors such as market
demand, pricing strategies, and competition are also considered to gauge the project's profitability
and sustainability over time. From Table VI, we obtained an average score of 4. 5.

```
TABLE VI. ECONOMIC FEASIBILITY
Attributes Score Why Solution
Is the project executable with the given
budget constraints?
```
```
5 Gathering all components can
be costly.
```
```
Ensure each component is
needed and bought at the
cheapest price.
Are there any economic risks? 4 Parts can get damaged or lost. We have a record of the parts
purchased.
Total 9
Average 4.
```
4) Schedule Feasibility
Schedule feasibility assesses whether the project can be completed within a reasonable
timeframe. It involves taking and evaluating dependencies between project tasks, estimating the
duration of each task, and considering any constraints that could impact the project timeline, such
as resource availability or external dependencies. By analyzing these factors, our group can
determine if the proposed project schedule is realistic and achievable. Schedule feasibility helps
identify potential risks of delays and allows for the development of contingency plans to mitigate
them. The average score obtained from this section is 5, as seen in Table VII.

```
TABLE VII. SCHEDULING FEASIBILITY
Attributes Score Why Solution
Meeting milestones 5 All milestones should be
achievable.
```
```
A schedule will be created to
ensure deadlines are met.
Can we meet both the preliminary and
critical design review?
```
```
5 Setting goals and milestones
is vital to completing project
processes.
```
```
Coordination and teamwork are
crucial for success.
```

```
Total 10
Average 5
```
5) Cultural Feasibility
Cultural feasibility evaluates whether a proposed project aligns with the stakeholders' artistic
values, norms, and beliefs and the broader community where it will be implemented. It considers
how the project might impact social dynamics, traditions, and ethical considerations relevant to
the target audience. Assessing cultural feasibility involves understanding local attitudes towards
the project, potential acceptance or resistance from stakeholders, and the project's alignment with
societal expectations and ethical standards. From Table VIII, we obtained an average score of 4. 7.

```
TABLE VIII. CULTURAL FEASIBILITY
Attributes Score Why Solution
Will there be a positive impact on local
culture?
```
```
5 The surveys we conducted
yielded favorable reactions. to
the project
```
```
Continue to gain feedback and
perspectives.
```
```
Will there be a positive impact on the global
culture?
```
```
4.5 Every country should benefit
from the use of this product.
```
```
We will gather opinions from
different cultures and conduct
research.
Is there much cultural risk involved? 4.5 There should be little risk
involved since the project is
designed to benefit everyone.
```
```
No solution is necessary.
```
```
Total 14
Average 4.7
```
6) Legal Feasibility
Creating a product that fails to comply with regulations and standards is a sure path to failure.
Furthermore, it is crucial to consider the legal aspects of our project to mitigate financial risks.
This section provides insights into the risks associated with regulatory violations and their
consequences. Equally important is recognizing the potential product liability if the product poses
a risk to consumers. From Table IX, we obtained an average score of 4.5.

```
TABLE IX. LEGAL FEASIBILITY
Attributes Score Why Solution
Are there any laws applicable to this project? 5 There should be laws that affect
this project.
```
```
No solution is necessary.
```
```
Will there be any issues or conflicts regarding
policy?
```
```
4 There should be no policy
conflicts concerning this project.
```
```
We can review any crucial
details with relevant
stakeholders.
Total 9
Average 4.5
```

```
7) Marketing Feasibility
Marketing feasibility assesses whether our project can attract and sustain a viable customer base
through effective promotion and positioning strategies. It involves evaluating market demand,
competition, and the potential for profitable sales channels. Understanding marketing feasibility
ensures that our project can effectively reach and resonate with its target audience, maximizing its
chances of success in the marketplace. From Table X, we obtained an average score of 4.25.
TABLE X. MARKETING FEASIBILITY
Attributes Score Why Solution
Will our project be well-received by the
public?
```
```
4 Our project is designed to appeal
to everyone caring for plants.
```
```
We will continue conducting
surveys to gauge consumer
interest.
Will there be any risks associated with
marketing?
```
```
4.5 Possibility of similar products
entering the market.
```
```
We will keep you updated on
the latest trends and continue
researching the area.
Total 8.5
Average 4.25
```
```
Table XI presents the values provided by the team in a consolidated format. It also includes the
computed values of the normalized geometric mean and the weight assigned to each attribute,
ensuring that the total weight across all attributes sums up to one. The diagonal of 1's within the
table indicates each type's self-relationship. Moreover, when comparing attributes across rows and
columns, the team evaluates their relative importance and assigns a value based on the scale
provided:
```
- 1 = Equal importance
- 3 = Moderately more important
- 5 = Strongly more important
- 7 = Very strong
- 9 = Extreme
The geometric mean in Table XI is determined using the specified formula:
    G. Mean = (A 1 * A 2 * A 3 ... *An)^1 /N^ (1)^

```
A represents the assigned importance value for the attribute, while n denotes the total number
of attributes. Additionally, the weight is determined through the following formula:
```
```
𝑊𝑒𝑖𝑔ℎ𝑡=
```
```
G.Mean
Total^ (2)^
TABLE XI. OBTAINING WEIGHTS
```
Technical Resource Economic Schedule Cultural Legal Marketing G. Mean Weight

Technical 1 3 5 3 5 3 7 3.1 0.38

Resource 0.33 1 3 3 3 3 5 1.8 0.22

Economic 0.2 0.33 1 0.33 3 1 3 0. 78 0.10


Schedule 0.33 0.33 3 1 3 3 5 1.3 0.16

Cultural 0.2 0.33 0.33 0.33 1 3 3 0.8 0.10

Legal 0.14 0.2 1 0.14 0.14 1 7 0. 65 0.08

Marketing 0.14 0.2 0.33 0.2 0.33 1 7 0.69 0.09

Total 8.07

```
The weighted score could then be derived using the following formula:
```
```
Weighted Score = Weight * Score (3)
After obtaining the weighted score, we calculate the total weighted feasibility score.
The following formula:
```
```
Weighted Average Score =
```
```
∑(𝑊𝑒𝑖𝑔ℎ𝑡×𝑆𝑐𝑜𝑟𝑒)
∑Weight^ (4)^
```
```
TABLE XII. WEIGHTED SCALE
```
```
Weight Score W. Score
Technical 0.38 4.75 1.80
Resource 0.22 4.63 1.02
```
```
Economic 0.10 4.5 0.45
Schedule 0.16 5 0.8
Cultural 0.10 4.7 0.47
Legal 0.08 4.5 0.36
```
```
Marketing 0.09 4.25 0.38
Total 1.13 32.33 5.28
Weighted Average 4.67
```

Table XII presents the weighted score calculated from the team's feasibility analysis. The team
applies the weights obtained from Table XII to compute this score. This involves multiplying each
category's feasibility analysis score by its corresponding weight.

In summary, the feasibility analysis of needs is crucial to assess the achievability of the product
or process. The team scored 4.67 out of 5.0 by summing up the relevant values. This weighted
average of 4. 67 confirms the project's viability. However, despite favorable statistical data,
challenges and setbacks may still arise, potentially affecting project deadlines or success.

### D. Marketability

The marketability of 'PlantPulse,' the intelligent gardening system that monitors ecosystems, is
crucial for several reasons, especially in gardening and ecosystem assistance. While the
'PlantPulse' structure is geared towards traditional gardens, large-scale condominiums, or even
farms, the 'PlantPulse' structure can apply to major environmental sectors. For this experiment, we
will focus on testing within certain parameters and comparing other products on the market with
different approaches to combat environmental management. 'PlantPulse's' approach will revolve
around sustainable practices, biodiversity support, and data utilization to improve current metrics
for plant care.

1) _Bloomiee | AI (Artificial Intelligence) Gardening Control System w/ Camera & Sensors_
a) Project Summary
Bifarm is an agricultural and clean-tech start-up primarily focusing on creating autonomous
ecosystems evoking sustainability [ 3 ]. Creating their first product, the 'Bloomiee,' The product's
primary focus is to eat a "copilot for home gardening."

```
b) Fundraising Strategies
```
- Early Bird | Bloomiee $375
    o Save $224 off retail
    o Select add-ons
    o Choose your color
- Priority Plus | Bloomiee $399
    o Save $200 off retail
    o Select add-ons
    o Choose your color
    o Faster shipping option


- Launch Price | Bloomie $499
    o Save $100 off retail
    o Choose Color
    o Select add-ons
    o Includes flood sensor

Bloomiee has rapidly surpassed their Kickstarter asking within 24 hours of listing. At over
370% over the pronounced goal of $5000, the current pledged amount at editing is $19,315. Here
are their promises: Bloomie creates an environment entirely controlled by its system while tracking
and improving the survival rate of plants. Done within a new metric, revolutionizing traditional
practices by incorporating AI technology in gardening can offer many benefits. Moreover, the
product's ability to enhance gardening efficiency, reduce resource wastage, and significantly
contribute to environmental management targets an altogether broader class with not only
enthusiast gardeners but also applicable to different markets like the ones listed above. In
summary, 'Bloomiee's AI Gardening System' not only capitalizes on advanced technology but is
constantly improving with various amounts of applications with data that consumers will collect.

c) Technology Overview
Bloomiee includes with their product, controller for the system that controls the CO2,
temperature Bloomiee includes, with their product, a controller for the system that controls the
CO2, temperature, and humidity sensor. It also includes fans, flood sensors, and motorized water
sprayers—add-ons like fans, flood sensors, and motorized water sprayers included in the
architecture. On the software side, they have created a mobile app and a website to track the
statistics of plants, along with a live view to monitor your garden.

```
TABLE XIII. BLOOMIE’S FEATURES
Technology Specification Function
Camera (HD) HD 1024x1024 High-resolution Monitor plant growth
Irrigation Sensor Soil moisture sensors with AI analytics Measure soil moisture
CO2 Sensor Infrared gas sensors Monitor and regulate CO2
Light Sensor Photodetectors Measure light intensity
Temperature Sensor Thermistors, digital temperature
sensors
```
```
Monitors ambient temperature
```
```
Humidity Sensor Capacitive humidity sensors Measures air humidity
Control Unit IoT connectivity, AI processor Integrates data from sensors,
providing remote access to regulate
the system
Wi-Fi 802.11ac (2.4 & 5GHz) Allows wireless connection for
real-time tracking
Bluetooth 5.0 Allows for connection to change
options in the system
Controlled Switches Input: 100-240V ~ 50/60Hz Powers on and off different systems
```
```
d) System Description
```

Utilizing cutting-edge technologies like artificial intelligence (AI), a variety of sensors, and
Internet of Things connectivity, the Bloomiee AI Gardening Control System is a novel approach
to maximizing indoor gardening. A central control unit, soil moisture sensors, CO2 sensors, light
sensors, temperature and humidity sensors, and a high-resolution camera are all essential parts of
the system. Together, these parts monitor and control critical environmental factors suitable for
plants. The high-goal camera catches point-by-point pictures of the plants, permitting computer-
based intelligence calculations to examine plant wellbeing and identify anomalies like nuisances
or sicknesses. By measuring moisture levels and adjusting the irrigation schedule, soil moisture
sensors ensure optimal watering. Light sensors adjust lights based on the intensity and duration of
light exposure, while CO2 sensors regulate carbon dioxide levels.

Fig 2. The block design of the Bloomiee Project
Temperature and mugginess sensors assist with keeping up with stable circumstances by
controlling warming, cooling, humidifiers, and dehumidifiers on a case-by-case basis. Using
artificial intelligence (AI) algorithms, the control unit processes data from all sensors to adjust
growing conditions in real time. Users can remotely monitor and control their garden thanks to
this central unit's connection to a mobile app. The app provides comprehensive oversight of the
indoor garden through real-time updates, notifications, and data analytics. The framework's
mechanization of routine errands, for example, watering and environment control, lessens the
requirement for manual mediation, improving effectiveness and comfort. In addition, the system
is scalable to fit gardens of varying sizes and promotes sustainability by optimizing resource
management and lowering energy and water consumption. Overall, the Bloomiee AI Gardening


Control System is an innovative, effective, easy-to-use solution that controls the environment to
ensure optimal plant health and growth.

Fig 3. Bloomiee Component Make-Up [ 4 ]
2) GeoDrops: Watering made easy for every garden
a) Project summary
GeoDrops is a creative artificial intelligence-controlled soil sensor framework intended to
improve watering for each nursery. It creates a precise watering schedule by combining weather
forecasts and environmental conditions with real-time soil data. This system promotes healthier
lawns and gardens, reduces water waste, and prevents overwatering. GeoDrops automate irrigation
so that plants get the right amount of water, boosting their growth and vitals.

b) Fundraising Strategies
For its Kickstarter campaign, GeoDrops has utilized several successful strategies. To begin, it
set a modest $10,000 target for its initial funding, which it has significantly exceeded, indicating
strong market interest and demand. At the date of recording, the funding has reached $47,000. The
mission offers various vow levels with related prizes to draw in benefactors with various financial
plan levels. For instance, lower pledges might be rewarded with digital recognition or thank-you
notes, while higher pledges get first access to the product or discounted bundles. GeoDrops also
emphasizes its unique selling points, like AI-driven watering precision and ease of integration with
existing irrigation systems, to appeal to gardeners who care about the environment and technology.
In addition, the campaign builds trust with potential backers by utilizing compelling images and
testimonials to highlight the product's advantages. Ordinary updates and straightforward
correspondence about the task's advancement assist with keeping up with supporter commitment


and certainty. Utilizing virtual entertainment and local area outreach, GeoDrops broadens its span,
empowering allies to share the mission and draw in additional promises.

```
c) Technology Overview
TABLE XIV. GEODROPS’S FEATURES
Technology Specification Function
Soil Moisture FDR 10 cm depth-aware moisture probe Moisture sensors with AI analytics to send
to the irrigation system
```
```
Weather Integration Data integration via 802.11b with real-
time weather tracking
```
```
Adjust watering schedules based on the
weather forecast
Control Unit IoT connectivity, AI processor, dual-
core 150MHz processor
```
```
Processes sensor and weather data to
automate irrigation schedule
```
```
Irrigation System Intelligent valves, IoT connectivity Tasked with water flow control based on AI
recommendations
Mobile App UI for data monitoring and analysis Track data, remote monitoring system
```
d) System Description
The GeoDrops AI intelligence Planting Control Framework is a watering system that
consolidates progressed sensor innovation and computer-based intelligence to upgrade traditional
watering system practices. Capacitive soil moisture sensors are part of the system and continuously
monitor the soil's moisture levels. These sensors send information to the control unit, which
processes the data utilizing artificial intelligence calculations. The system adjusts watering
schedules to match current and predicted conditions by integrating real-time weather data. This
system ensures that plants get the right amount of water. The shrewd water system framework
utilizes exact valves to control the water stream, decreasing waste and forestalling overwatering.
The entire setup is managed by a mobile app that is easy to use; the app lets gardeners remotely
check how their garden is doing and change settings. This consistent mix of equipment and
programming guarantees effective water use, advances better plant development, and works on the
gardening of the executives.


Fig 4. GeoDrops Block Design
PlantPulse and GeoDrops use technology to improve gardening, but their methods differ.
PlantPulse focuses on a comprehensive intelligent garden system that uses AI to provide
individualized plant care recommendations and monitors a variety of environmental factors like
pH, humidity, light, and fertilizer levels. Real-time notifications and an enclosed garden are two
additional features. GeoDrops, on the other hand, uses AI and real-time data on soil and weather
to target watering practices' optimization specifically. GeoDrops intends to incorporate effectively
with existing water system frameworks and spotlights on forestalling overwatering to decrease
water diminishments. GeoDrops is a highly specialized tool for water management in gardening
because it excels in precision irrigation, whereas PlantPulse provides a broader scope of plant care
management. Although they cater to slightly distinct aspects of smart gardening, both systems
emphasize automation, effectiveness, and user convenience.


Fig 5. GeoDrops Ideal Configuration & Utilization [ 5 ]


## V. RISK ANALYSIS

Risk analysis in the context of our project involves identifying, assessing, and prioritizing
potential risks that could impact our project's operations, goals, or outcomes. It aims to evaluate
the likelihood of risks occurring and their potential impact on our objectives. This process includes
gathering data, analyzing scenarios, and quantifying risks to make informed decisions on
mitigating or managing them effectively. By conducting risk analysis, we can proactively identify
vulnerabilities, anticipate potential threats, and develop strategies to minimize negative
consequences. This proactive approach helps safeguard our project's assets and resources and
enhances its resilience in facing uncertainties.

Risk analysis is crucial for our project because it provides a structured framework to understand
and manage uncertainties that could impact our project's continuity and success. By assessing risks
comprehensively, we can prioritize our efforts and allocate resources effectively to mitigate
potential threats. It enables informed decision-making by providing insights into the likelihood
and consequences of various risks, helping us plan for contingencies and reduce potential losses.
Moreover, in our competitive and dynamic project environment, practical risk analysis fosters
adaptability and innovation by encouraging us to proactively anticipate and respond to changing
conditions. Ultimately, integrating risk analysis into our project strategies enhances overall
resilience, improves performance, and supports sustainable growth in the long term.

```
The following list below includes all potential risks of the project under seven categories:
```
A. Technical

```
T1. Programming the Micro-Computer and designated application.
T2. Accurate wiring of components and sensors.
```
B. Resources

```
R1. Acquiring electronic skills.
R2. Acquiring programming skills.
```
C. Economic

```
E1. Surpassing budget expectations.
E2. Hardware malfunction.
```
D. Schedule

```
S1. Research time.
```
```
S2. Development takes longer than expected.
```
E. Cultural

```
C1. There needs to be more adequate social acceptance.
```
```
C2. Resistance from some geographical areas.
```
F. Legal

```
L1. Lack of knowledge can affect the implementation of the project.
L2. Unexpected legal costs.
```

G. Marketing

```
M1. Customer appeal.
M2. Similar products are entering the market.
```
```
Fig 6. Fault Tree Analysis
```
As shown in Fig. 6 , Our project's fault tree analysis provides a structured framework to identify
and understand potential risks that could impact our implementation process. At the top level, the
diagram categorizes these risks into technical and non-technical issues. Under technical issues, we
recognize the critical tasks of programming the micro-computer and ensuring accurate wiring of
components and sensors. These tasks are fundamental to the functionality and reliability of our
project. On the non-technical side, various categories such as resources, economic factors, cultural
acceptance, legal considerations, and marketing challenges are meticulously detailed. Each branch
represents specific risks, such as acquiring essential skills, budget expectations, social acceptance,
legal knowledge gaps, and market competition.

By breaking down potential risks in this manner, our fault tree analysis allows us to delve deeper
into each area of concern. For instance, regarding resources, the acquisition of electronic and
programming skills is identified as essential for the successful execution of our project. Economic
factors, including the risk of surpassing budget expectations and potential hardware malfunctions,
highlight financial and operational risks that require careful management. Additionally, cultural
factors such as social acceptance and regional resistance underscore the importance of community
engagement and awareness-building efforts. Legal and marketing issues further emphasize the
need for comprehensive risk mitigation strategies to navigate potential challenges effectively. This
fault tree analysis enables us to proactively identify and address risks, ensuring our project
progresses smoothly toward its objectives while minimizing unforeseen disruptions.


```
TABLE XV. RISK EXPOSURE MATRIX
```
In Table XV, risks pertinent to our project are meticulously categorized based on their
likelihood of occurrence and potential impact. Risks span from those deemed Very Likely to
Unlikely, each corresponding to four distinct classes. Class IV encompasses Catastrophic risks,
highlighting severe threats like legal complications and unforeseen costs that could profoundly
disrupt our project. Class III identifies Severe risks, such as delays in development and challenges
in social acceptance, which could significantly hinder progress. Class II covers Moderate risks,
including concerns about customer appeal and acquiring essential resources, which may pose
manageable but notable challenges. Finally, Class I includes Low risks, such as technical
programming tasks and localized resistance, which are less likely to occur or have minimal impact.
This structured approach aids in prioritizing our risk management strategies, ensuring that we
address the most critical risks effectively to safeguard our project's success.

```
TABLE XVI. ACTIONS TO MINIMIZE RISKS
Actions
[T1] [T2] Perform adequate research and communicate difficulties with our mentor.
[C2] Understand how certain target audiences operate.
[E2] [S1] Conduct thorough checks of equipment and look into problems quickly.
[R1] [R2] [E1] Take necessary courses and ensure spreadsheets are created to keep track of finances.
[M1] Work on creating an enticing marketing strategy to get potential customers interested.
[C1] [S2] [M2] Create team milestones and set goals to meet expectations for all stakeholders.
[L1] [L2] Perform necessary research on business contracts and consult with experts in the field.
```
Table XVI outlines specific actions crucial for the success of our project. Actions like
performing thorough research and maintaining open communication with mentors (T1, T2) are
essential to anticipate and address challenges effectively. Understanding the operational dynamics
of target audiences (C2) helps tailor our approach to meet their needs. Regular equipment checks
and promptly addressing issues (E2, S1) ensure smooth project operations. Acquiring necessary
skills through courses and maintaining meticulous financial records (R1, R2, E1) supports budget
management and resource allocation. A compelling marketing strategy (M1) aims to engage
potential customers effectively. Establishing team milestones, setting achievable goals, and
managing stakeholder expectations (C1, S2, M2) are crucial for project alignment and progress
tracking. Lastly, conducting thorough research on business contracts and seeking expert advice
(L1, L2) mitigates legal risks and ensures compliance throughout our project journey.

```
Likelihood of Occurrence
Very Likely Possible Unlikely Legend
Class IV [L1] [L2] Catastrophic
Class III [S2] [M2] [C1] Severe
Class II [M1] [R1] [R2] [E1] [E2] [S1] Moderate
Class I [T1] [T2] [C2] Low
```

Based on our comprehensive risk analysis, we have identified and categorized potential risks
across various critical areas relevant to our project's success. By categorizing risks based on their
likelihood of occurrence and potential impact, we have strategically outlined actionable steps to
mitigate these challenges. Actions include performing adequate research and maintaining clear
communication channels with mentors to address difficulties promptly (T1, T2), understanding the
operational behavior of target audiences (C2), conducting thorough equipment checks and swift
problem resolution (E2, S1), acquiring necessary skills and maintaining robust financial tracking
(R1, R2, E1), developing an enticing marketing strategy to attract customers (M1), setting team
milestones and goals to meet stakeholder expectations (C1, S2, M2), and ensuring compliance
with legal obligations through meticulous research and expert consultation (L1, L2). This
structured approach enhances our preparedness and strengthens our ability to navigate challenges
proactively, ensuring our PlantPulse project's smooth progression and success.

## VI. OPERATING ENVIRONMENT

In this part of our project proposal, we depict the operating environment of our project; this is
a crucial section of the proposal due to the clear explanation of the operating environment of our
product, which is one of the key points to our engineering process. Understanding the environment
where our project will be tested is essential for the designing and constructing phase of the project
to be successful, as overlooking this aspect could potentially lead to logistical failures and
malfunction within the device and its components. Typically, the components of the engineering


project are rated to measure ranges of multiple factors like temperatures, humidity levels, and
susceptibility to electromagnetic interference. Ensuring these parameters are accounted for will
lead to the optimal functionality of the entire project; furthermore, having a transparent picture of
the operating environment will ensure cost-effectiveness due to the robustness of a device often
being related to its cost.

Our PlantPulse project is designed to operate in a carefully controlled and enclosed
environment, ensuring optimal plant growth and system performance conditions. Lodged inside
our garden structure network, this operating environment protects from outside factors like
extreme weather conditions, pollutants, and pests that could severely affect the plants and the
system. Inside this enclosed operating environment, the operating temperature range for our
system is set to be around 10 °C and 35°C, providing an ideal climate for most plant species.
Additionally, humidity levels will be constantly monitored, ensuring a 40% to 70% humidity
range, which will optimize plant growth. Furthermore, the system will be complemented with
multiple sensors distributed around the garden, ensuring accurate and reliable data collection.
Moisture sensors positioned in the soil will measure water content and require protection from
excessive water exposure while maintaining direct contact with the soil. Temperature sensors
throughout the enclosure will monitor ambient temperature and require stable conditions for
accurate readings. Also embedded in the soil, pH sensors will measure acidity/alkalinity and need
protection from physical damage and contamination. Light sensors mounted above the plants will
measure light intensity and require exposure to natural or artificial light sources without
obstruction.

Also, the power for the entire system will be supplied via a dual 4A charger, ensuring a stable
power supply. This power system will be enclosed and safeguarded against moisture and physical
damage, providing reliability and longevity. Communication between sensors and the server will
be facilitated by LoRaWAN modules, requiring a stable and interference-free environment for
reliable data transmission. Likewise, our PlantPulse project will require the implementation of
several machine learning algorithms, such as decision trees, KNNs, SVMs, random forests, and
neural networks, to analyze sensor data and provide actionable feedback.

Finally, regular maintenance will ensure the longevity and reliability of the device and its
components. This includes cleaning sensors, checking wiring connections, and ensuring all
components function correctly.

## VIII. INTENDED USER(S) AND INTENDED USE(S)

One of the aspects of our project design is identifying the product's intended users and uses. By
establishing these parameters, we can streamline the decision-making process during the product's
development, narrowing down considerations and potential outcomes.

A. Intended User(s)

Our PlantPulse project will target individuals or whole organizations involved in cultivating
and maintaining the plant environment, specifically those with plant health and growth as their
primary goal.


- Garden enthusiasts or hobbyists are eager to create thriving and diverse plant
    environments.
- Agricultural professionals aim to enhance crop production and ensure the success of
    various plant species.
- Educational institutions seeking to teach principles of sustainable agriculture.
The supervisors and maintenance people of these groups will be charged with directly
interacting with the system components to monitor the plant environment's health and well-being
by receiving notifications from the system to make informed decisions about their plant care.

### B. Intended use(s)

The primary purpose of PlantPulse is to create an intelligent garden system that will optimize
plant growth and longevity using automated monitoring through a plethora of sensors as well as a
critical software application that will notify the intended users of the plants being in the present as
well as the future using different machine learning algorithms and AI strategies. Key intended uses
will include:

- Using integrated sensors to control and measure plant-specific parameters such as soil
    moisture, temperature, humidity, and light intensity.
- Providing real-time notifications to users regarding crucial duties or potential issues
    affecting plant health.
- Collecting and analyzing sensor data to provide insights and recommendations for plant
    care using machine learning algorithms such as decision trees, KNNs, SVMs, random
    forests, and neural networks.
Lastly, our project goal is to deliver automated tools that will give clear insights needed to
create and maintain thriving plant environments for personal enjoyment, agricultural purposes, or
education.

## VIII. BACKGROUND

The background part is crucial since it gives the reader a comparison between our project and
other similar projects. This context allows the reader to understand our group's distinctive
contributions better. Furthermore, by looking at other people's solutions, we can find ideas for
improving the design and gain a deeper understanding of the project's importance by examining
this part. A common observation about creativity is that it is naturally collaborative, and any
invention can be understood as an iterative refining of earlier ideas. In this background section,
three projects will be reviewed that share several similarities with ours.

A. Niwa: All-in-one controller of your indoor garden.

Niwa is a project focused on revolutionizing indoor gardening through technology. The team
behind it, founded in 2014 and primarily led by Gabriel Yago, the author, utilized Kickstarter to


introduce their product to the market and engage with the community. The project was successfully
funded, raising $148,948, surpassing its goal of $100,000 and making it possible.

```
1) Project Summary
```
Niwa is an advanced indoor gardening system that allows users to cultivate vegetables, herbs,
and fruits year-round, monitoring everything simultaneously. [ 1 ] This system is targeted at urban
residents, home gardeners, and small-scale farmers who seek an efficient, low-maintenance
solution for indoor gardening. Also, Niwa integrates various sensors to monitor environmental
conditions such as temperature, humidity, light, and nutrient levels. These sensors connect to a
smart device through the Niwa app, enabling users to control and monitor the system remotely.
The app provides real-time data and notifications, ensuring optimal growing conditions for the
plants. Niwa's technology allows for automated adjustments based on sensor data, promoting
healthy plant growth with minimal user intervention. The system is priced at $299, with the
accompanying app available as a free download.

2) Technology Overview
Niwa contains a compact hydroponic unit with integrated sensors and a control system. The
device's dimensions are 15 x 15 x 18 inches, making it suitable for indoor use in limited spaces.
Furthermore, the system includes temperature, humidity, light intensity, and nutrient level sensors.
A standard AC outlet powers it and features a water pool with a capacity of 2 liters. Wireless
connectivity is facilitated through Wi-Fi, allowing seamless communication with the Niwa app.
On the project's software side, the app will enable users to monitor real-time data, receive
notifications, and control various aspects of the system, such as lighting and watering schedules.
Niwa's sensors provide accurate measurements to ensure optimal growing conditions, and the
system's automation capabilities help users maintain their indoor gardens effortlessly. The Niwa
Grow Hub+'s main product also brings commercial-grade features, such as monitoring and
controlling your plant's climate (temperature and humidity) and Vapor Pressure Deficit (VPD). It
also offers home growers automated watering, light, and fan schedules. With the optional CO2
sensor, users can monitor CO2 levels and manage a CO2 device such as a CO2 valve. The Grow
Hub+ features 15A per outlet (15A total) and a resettable circuit breaker, enhancing its
functionality and safety for various indoor gardening setups.


Fig 7. NIWA GROW HUB+ – SMART AUTOMATION & MONITORING SYSTEM [ 6 ]


```
3) System Description
```
Fig 8. NIWA Grow Hub+ System Block Diagram
Fig.8 highlights a diagram of the Niwa Grow Hub+, a compact hydroponic unit equipped with
integrated sensors for Temperature, Humidity, Light Intensity, and Nutrient Levels. It connects via
Wi-Fi to the Niwa App, enabling real-time monitoring and control of lighting, watering schedules,
and environmental conditions. Powered by a standard AC outlet, it includes optional features like
a CO2 sensor for enhanced plant growth management. The system's automation utilizes sensor
data to maintain optimal growing conditions effortlessly, making it ideal for indoor gardening in
limited spaces.

B. FarmBot: Open-Source CNC Farming

FarmBot is an exciting project that was launched in 2011 and founded by Rick Carlino and
Rory Aronson. It aims to revolutionize agriculture through open-source technology. The team
behind it leveraged Kickstarter to launch their product, engaging with a global community of
supporters. The project raised $813,666, significantly surpassing its initial goal of $100,000,
enabling its development and widespread adoption.

```
1) Project Summary
```
The FarmBot project is an advanced, open-source CNC farming system that allows users to
automate the cultivation of crops. [ 2 ] It is designed for urban gardeners, educational institutions,
researchers, and small-scale farmers; FarmBot provides an efficient and low-maintenance solution
for precision farming. The system integrates various tools and sensors to perform tasks such as
planting seeds, watering, and soil monitoring. These tools connect to a smart device through the
FarmBot web app, allowing users to control and monitor the system remotely. The app offers real-
time data and notifications, ensuring optimal conditions for plant growth. Finally, the system is
modular and scalable, with prices varying based on size and configuration, and the software is
open-source and freely available.


2) Technology Overview
FarmBot comprises a robust frame with a gantry system that moves along X, Y, and Z axes to
perform various farming tasks. The dimensions of the standard FarmBot Genesis model are 1.5 x
3 meters, suitable for raised beds and small plots. The system includes several pre-assembled
components for ease of setup and reliability:

- Pre-assembled cross-slide and z-axis
- Pre-assembled cable carriers with cables and tubing
- Pre-assembled seed injector tool with vacuum pump, tubing, seed bin, seed tray, seed
    troughs, seed trough holder, and customizable Luer lock needles
- Pre-assembled watering nozzle tool with solenoid valve, tubing, and adapters for a
    standard US garden hose
- Pre-assembled soil sensor tool
- A pre-assembled rotary tool with an adjustable motor angle and interchangeable bits
The hardware features:
- All aluminum tracks, gantry, and z-axis extrusions
- 5mm (about 0.2 in) anodized aluminum plates
- Stainless steel rubber sealed ball bearings and stainless steel hardware
- Injection molded UV-stabilized ABS plastic components
- Four NEMA 17 stepper motors with rotary encoders for precision position tracking
- GT2 timing belts and aluminum pulleys
- 8mm (about 0.31 in) stainless steel leadscrew and Delrin block
- IP67 rainproof power supply with 110 and 220V AC input
Electronics include:
- Raspberry Pi 4 and microSD card
- Farmduino microcontroller with integrated Trinamic TMC2130 stepper drivers and
peripheral load detection circuitry
- Custom rainproof electronics enclosure
- Universal tool mount and cable
- IP67 rainproof USB camera and mount
- Two 3-slot toolbars
- All tools needed for assembly

Wireless connectivity is provided via Wi-Fi, allowing seamless communication with the
FarmBot web app. The app lets users plan and execute farming activities, monitor real-time data,
receive notifications, and adjust system settings. FarmBot's sensors deliver precise measurements
for soil moisture, temperature, and plant health, ensuring optimal growing conditions.


```
Fig 9. Farmbot Genesis V1.7 [7]
```
```
3) System Description
```
Fig 10. Farmbot Genesis V1.7 System Block Diagram
Fig.10 highlights the FarmBot, an automated farming system with a robust gantry frame moving
along the X, Y, and Z axes. It includes pre-assembled tools like the Seed Injector, Watering Nozzle,
Soil Sensor, and Rotary Tool for various farming tasks. The hardware features durable construction
with aluminum tracks, stainless steel bearings, and UV-stabilized ABS plastic components.
Precision is ensured by NEMA 17 stepper motors with encoders, GT2 timing belts, and an 8mm


(about 0.31 in) stainless steel lead screw. The system is powered by an IP67 rainproof supply.
Electronics include a Raspberry Pi 4, a Farmduino microcontroller with Trinamic TMC2130
drivers, and a custom rainproof enclosure housing components such as an IP67 rainproof USB
camera. Tool mounts, toolbars, and assembly tools complete the system, ideal for automated
farming in raised beds and small plots.

C. Google Nest Learning Thermostat

The Nest Learning Thermostat is a smart home device founded in 2010 by Tony Fadell and
Matt Rogers as part of their company: “Nest Labs”; the device is designed to optimize heating and
cooling efficiency while providing intuitive control through machine learning and sensor
technology. Developed by Nest Labs, the thermostat has revolutionized home climate control by
integrating sensors and connectivity to enhance energy savings and user comfort.

1) Project Summary
The Nest Learning Thermostat is a device designed to minimize energy usage and improve
comfort by adapting temperature settings based on user habits. [ 3 ] It caters to both homeowners
and renters by monitoring room conditions such as temperature, humidity, activity levels, and
ambient light. Utilizing the Nest app, users can manage their thermostats remotely, access energy
consumption reports, and receive alerts for potential issues. Over time, the thermostat learns from
user interactions to optimize energy efficiency while maintaining optimal comfort levels.

2) Technology Overview
The Nest Learning Thermostat integrates advanced sensor technology and connectivity to
deliver intelligent climate control:

```
Sensor Integration:
```
- Temperature Sensor: Monitors room temperature to maintain desired comfort levels.
- Humidity Sensor: Measures humidity levels to optimize indoor air quality.
- Proximity Sensor: Detects presence to adjust settings when occupants are away or asleep.
- Ambient Light Sensor: Adjusts display brightness and sensor functionality based on
    ambient lighting conditions.
- Magnetic Sensor: Determines thermostat ring position for enhanced usability.
Display:
- Type: 24-bit color LCD
- Resolution: 480 x 480 pixels, 229 pixels per inch (PPI)
- Size: 2.0 inches (5.3 cm) diameter
Dimensions and Weight:
- Assembled Unit: 3.3 in (8.3 cm) diameter, 1.1 in (3.0 cm) height, weight 8.6 oz (243.7 g)
- Display: 3.3 in (8.4 cm) diameter, 1.0 in (2.7 cm) height, weight 7.2 oz (205.4 g)
- Base: 2.9 in (7.6 cm) diameter, 0.4 in (1.1 cm) height, weight 1.4 oz (38.3 g)
Algorithms:
- Adaptive Learning: Learns user preferences and adjusts heating and cooling schedules
accordingly.


- Energy-Saving Features: Energy-efficient settings and schedules are recommended to
    reduce energy consumption without compromising comfort.
Connectivity:
- Wi-Fi: Supports 802.11 a/b/g/n (2.4GHz/5GHz) for remote control via the Nest app from
smartphones, tablets, and computers.
- Wireless Protocol: Includes 802.15.4 (2.4GHz) and Bluetooth Low Energy for connectivity
with other smart home devices.
Power:
- Power Source: Built-in rechargeable lithium-ion battery.
- Power Consumption: Less than 1 kWh/month, ensuring energy efficiency.

The Nest Learning Thermostat (Fig.11) combines precise sensor capabilities with intuitive
machine learning and connectivity, empowering users to manage their home climate for enhanced
comfort and energy efficiency. This approach optimizes heating and cooling operations and
promotes sustainable living through informed energy usage.

```
Fig 11. NEST Learning Thermostat [8]
```
```
3) System Description
```

Fig 12. NEST Learning Thermostat Device System Block Diagram
Fig.12 shows the Nest Learning Thermostat block diagram, featuring integrated sensors for
temperature, humidity, proximity, ambient light, and magnetic positioning. It includes a 24-bit
color LCD display with specified dimensions powered by a rechargeable lithium-ion battery for
energy efficiency. The thermostat employs algorithms for adaptive learning and energy-saving
recommendations. Connectivity options include Wi-Fi for remote control via the Nest app and
Bluetooth Low Energy for smart home device integration, making it a versatile solution for
intelligent climate control in homes.

Our project draws inspiration from the mentioned products in regard to the technology utilized.
By observing similar innovations, we have refined our vision to enhance plant care through
advanced monitoring and automation. These inspirations have guided us in developing a solution
that integrates modern technology with practical applications, aiming to revolutionize agriculture
and urban green spaces alike. As we move forward, we remain committed to learning from these
precedents to create a robust and effective system that meets the evolving needs of plant care and
environmental sustainability.

## IX. INTELLECTUAL PROPERTY CONSIDERATIONS

Intellectual Property (IP) in any engineering project is of paramount importance because it
safeguards the legal rights that emerge from the project’s scholarly activities. For any engineering
endeavor, IP acts as a critical asset by protecting innovations, designs, and inventions, thereby


ensuring that creators or owners can derive benefits from their work and investment. This
protection is crucial for preserving the unique value of our project.

A. Orchard Plant Monitoring System, CN101661664A [ 9 ]

While conducting research on this subject matter, similar intellectual properties were
discovered that would be utilized to avoid any form of copyright infringement. One such IP is that
of an Orchard planting monitoring system based on wireless sensor networks. Its inventors are
Meng Haijun, Li Shinin, and Li Zhigang, and its patent is currently pending.

1) Patent Summary
The invention presents a system and method for monitoring orchard planting using wireless
sensor networks. The system includes multiple wireless sensor networks with several wireless
sensor nodes, gateway nodes, a communication server linked to these gateway nodes, and a host
monitoring machine connected to the communication server [ 4 ]. The method involves three main
steps, which are as follows:

- The wireless sensor nodes form self-organized networks and transmit collected
    monitoring data to the gateway nodes at regular intervals. The gateway nodes then
    package and send this data to the communication server.
- The communication server forwards the monitoring data to the host monitoring machine.
- The host monitoring machine preprocesses the data, removes false data, and uses an
    expert system to analyze and process the information, creating an appropriate
    monitoring program.

This invention boasts a well-thought-out design, low cost, ease of operation, effective
monitoring capabilities, and high intelligence. It provides valuable guidance to farmers and can
issue real-time warnings.

As illustrated in Fig. 12, the present invention features multiple wireless sensor networks
composed of numerous wireless sensor nodes positioned throughout the monitored orchard. These
nodes transmit packed monitoring data to gateway nodes, which then connect to a communication
server. The communication server is linked to an upper monitoring machine. The number of
gateway nodes can vary. The wireless sensor nodes include a general sensor node, placed at the
top of each fruit tree to monitor air temperature, humidity, and light intensity, and soil moisture
sensor nodes located at the roots of each tree. These general sensor nodes and soil moisture sensor
nodes communicate with the gateway node using short-range wireless communication modules.
The gateway nodes, in turn, communicate with the communication servers via GPRS networks
and are equipped with GPRS wireless communication modules.

In practical use, the communication server uses the GPRS network to facilitate two-way
communication with mobile communication devices operated by farmers or skilled personnel.
Each gateway node contains a processor module, a GPRS wireless communication module, a
short-range wireless communication module based on the ZigBee protocol, and a power module.


Additionally, the invention includes CO2 concentration sensor nodes placed in the orchard, which
also communicate with the gateway nodes using short-range wireless communication modules.

```
Fig 13. Circuit block diagram of the plant monitoring invention [4]
Description of reference numerals:
1 - wireless sensor network
2 - gateway node
3 - communication server
```
```
4 - power module
5 - soil moisture sensor
6 - CO2 The concentration sensor node
```
```
7 - upper monitoring machine
8 - mobile communication equipment
```

2) Claims
Table XVII highlights the eight claims brought forward by the creators and indicates their
relevance to our project idea.

```
TABLE XVII. CLAIMS
Claim Description Relevancy
```
```
1 A^ plurality of wireless sensor nodes are laid in the monitored orchard, the
communication server.
```
```
Yes
```
```
2 It is characterized by the following: the described short-range wireless
communication module is the short-range wireless communication module
based on the ZigBee agreement.
```
```
No
```
```
3 The described system includes CO2 concentration sensor nodes placed in the
monitored orchard, connected via short-range wireless modules to a gateway
node. This setup enables two-way communication between the CO2
concentration sensor and gateway nodes.
```
```
No
```
```
4 General sensor nodes (4) have air temperature, humidity, and illumination
intensity sensors connected to a processor module. Each node is powered by a
system supporting the processor and a ZigBee-based short-range wireless
communication module.
```
```
Yes
```
```
5 The soil moisture sensor node (5) consists of a soil moisture sensor module, a
processor module two, and a ZigBee-based short-range wireless
communication module two, all powered by power module two.
```
```
Yes
```
```
6 The CO2 concentration sensor node (6) features a CO2 sensor module,
processor module three, and ZigBee-based wireless communication module
three, all powered by a single power module three.
```
```
Yes
```
```
7 The gateway node (2) includes a processor module four, a GPRS wireless
communication module connected to it, a short-range wireless communication
module, and a power module four supplying power to all components.
```
```
No
```
```
8 It is characterized in that this method may further comprise the steps:
Real-time monitoring of orchard parameters using multiple wireless sensor
nodes grouped into networks (1) using MANET mode. Nodes collect data and
send it to their respective gateway node (2), which consolidates and sends the
data to the communication server (3).
The communication server (3) forwards the data to the upper monitoring
machine (7).
The upper monitoring machine (7) performs further analysis and processing of
the data.
```
```
Yes
```
```
3) Non-Infringement
The patent described in this proposal differs from PlantPulse based on the following:
```

```
TABLE XVIII. NON-INFRINGEMENT
PlantPulse Monitoring System Orchard Monitoring System
```
```
This system is more straightforward and more
localized, relying on sensors, probes, or meters
placed directly in the soil or near individual plants.
It will use local networks or Bluetooth connectivity
for data transmission.
```
```
This system comprises a more extensive
infrastructure, such as the networks of sensors
mentioned. The patent also relies on advanced
communication technologies such as the ZigBee
technology for data transmission and analysis.
```
```
Data collected from this project’s plant monitoring
system would focus on immediate needs like
watering schedules, nutrient levels, and pest
control for specific plants or groups of plants.
```
```
The orchard monitoring system is designed to
generate large volumes of data over extended
periods, requiring more complex analytics for trend
analysis, predictive modeling, and long-term
management strategies to optimize crop yield and
quality.
```
B. System and method for plant monitoring, US20160148104A1 [1 0 ]

This patent is currently assigned to Prospera Technologies Ltd. It was filed by inventors Raviv
Itzhaky, Daniel Koppel, and Simeon Shpiz. The application status became active on July 16, 2019,
and is set to expire in 2037. The patent indicates that it is an automated system and method for
monitoring plants. The process involves identifying one or more test inputs within a designated
test area, including plant segments. It further includes generating predictions about the condition
of the plant based on these test inputs using a prediction model. This model is developed from a
training dataset comprising inputs and corresponding outputs, where each output corresponds to a
specific input. And Simeon Shpiz. The application status became active on July 16, 2019, and is
set to expire in 2037. The patent indicates that it is an automated system and method for monitoring
plants. The process involves identifying one or more test inputs within a designated test area, which
includes segments of a plant. It further comprises generating predictions about the condition of the
plant-based on these test inputs using a prediction model. This model is developed from a training
dataset comprising inputs and corresponding outputs, where each output corresponds to a specific
input.

```
1) Patent Summary
```

The disclosed embodiments describe a method and system for monitoring plants. The technique
involves identifying test inputs within a specified area containing parts of a plant and using these
inputs and a prediction model to generate predictions about the plant's condition. The prediction
model is built from a training set comprising inputs and outputs, where each output corresponds
to a specific input. Similarly, the system includes a processing unit and memory configured to
execute instructions for identifying test inputs and generating plant condition predictions based on
the same principles outlined in the method. Fig. 14 below demonstrates the setup of the patent.

Fig 14. A schematic diagram of a system for automatic plant monitoring is utilized to describe the various
disclosed embodiments. [10]
2) Claims
Within this patent are 25 claims that seek to introduce a comprehensive method and system for
automating the monitoring of plants. It focuses on leveraging test inputs, including visual data (like
image sequences) and environmental parameters (such as temperature and humidity), to predict
various aspects of plant health and growth using sophisticated prediction models. These models
are trained on extensive datasets, allowing for accurate predictions of diseases, pest activity,
nutrient deficiencies, future disease risks, harvest yields, and optimal harvest times. Additionally,
the patent aims to generate actionable growing recommendations based on these predictions, which
can be displayed, transmitted to users' devices, or shared online, enabling informed decision-
making and proactive plant management. The system integrates sensors like cameras and
environmental sensors to capture necessary input data, ensuring real-time monitoring capabilities
for agricultural applications. It predicts various aspects of plant health and growth using
sophisticated prediction models. These models are trained on extensive datasets, allowing for
accurate predictions of conditions like diseases, pest activity, nutrient deficiencies, future disease


risks, harvest yields, and optimal harvest times. Additionally, the patent aims to generate
actionable growing recommendations based on these predictions, which can be displayed,
transmitted to users' devices, or shared online, thereby enabling informed decision-making and
proactive plant management. The system integrates sensors like cameras and environmental
sensors to capture necessary input data, ensuring robust and real-time monitoring capabilities for
agricultural applications.

3) Non-Infringement
The patent US20160148104A1 focuses on automated plant monitoring through advanced
predictive modeling using visual and environmental data to predict and manage various aspects of
plant health and growth, including diseases, pest activity, nutrient deficiencies, and optimal harvest
conditions. It emphasizes proactive management by generating actionable recommendations based
on real-time data captured by cameras and environmental sensors. In contrast, PlantPulse centers
on real-time soil monitoring using a network of sensors embedded in the soil. It prioritizes
continuous monitoring of soil parameters such as moisture levels, temperature, and specific
nutrients like phosphorus, calcium, and potassium, using durable, water, dust, and rust-resistant
sensors. PlantPulse aims for ease of use and low maintenance with modular hardware expansion
ports and LoRaWAN connectivity, focusing on optimizing plant nutrition and environmental
conditions through detailed soil analysis.

C. AI-powered autonomous plant-growth optimization system that automatically adjusts input
variables to yield desired harvest traits, US11308715B2 [1 1 ]

This patent is currently assigned to Ageye Technologies Inc. Furthermore, it was filed by
inventors Nicholas R. Genty and John M. J. Dominic. The application status became active on
April 19, 2022, and is set to expire in 2039. The primary purpose of this patent is to introduce and
protect a method and system that leverages advanced technologies such as artificial intelligence
(AI) and the Internet (IoT) for optimizing plant growth in indoor farming environments.
Specifically, it aims to automate the monitoring and adjustment of growing conditions, particularly
lighting, based on real-time data from optical, imaging, environmental, and light sensors. This
approach is designed to enhance plant quality and maximize crop yields throughout different stages
of growth, thereby improving efficiency and productivity in indoor farming operations. This patent
is currently assigned to Ageye Technologies Inc. And was filed by inventors Nicholas R. Genty and
John M. J. Dominic. The application status became active on April 19, 2022, and is set to expire in

2039. The primary purpose of this patent is to introduce and protect a method and system that
leverages advanced technologies such as artificial intelligence (AI) and the Internet (IoT) for
optimizing plant growth in indoor farming environments. Specifically, it aims to automate the
monitoring and adjustment of growing conditions, particularly lighting, based on real-time data
from optical, imaging, environmental, and light sensors. This approach is designed to enhance plant
quality and maximize crop yields throughout different stages of growth, thereby improving
efficiency and productivity in indoor farming operations.

```
1) Patent Summary
```

The invention pertains to indoor agriculture, specifically methods and systems that utilize
artificial intelligence (AI) and Internet-of-things (IoT) technologies. These systems employ
optical, imaging, environmental, and light sensors to monitor and enhance plant growth and quality
in real-time within indoor farms. Data from these sensors inform adjustments to growing
conditions and exceptionally light levels, tailored to optimize growth throughout various phases
of plant development, aiming to achieve desired harvest characteristics automatically. The system
uses sensors like cameras and environmental monitors to maximize plant growth in indoor farms
in real time by adjusting light and other conditions. These sensors form a wireless network (IoT)
and employ machine learning and image recognition to fine-tune growth parameters. A cloud-
based model is trained and deployed to an edge device on-site to ensure continuous optimization
despite connectivity challenges. This self-regulating process adjusts light intensity and spectral
output to enhance crop quality and yield based on real-time plant monitoring. Fig. 14 , shown here,
highlights the setup of this patent. by adjusting light and other conditions. These sensors form a
wireless network (IoT) and employ machine learning and image recognition to fine-tune growth
parameters. A cloud-based model is first trained and then deployed to an edge device on-site to
ensure continuous optimization despite connectivity challenges. This self-regulating process
adjusts light intensity and spectral output to enhance crop quality and yield based on real-time
plant monitoring. Fig. 15 , shown here, highlights the setup of this patent.

```
Fig 15. An AI-powered autonomous plant-growth optimization system automatically adjusts input variables to
yield desired harvest traits. [1 1 ]
```
```
2) Claims
```

The patent has 15 claims and ultimately describes a method to optimize indoor plant growth
using AI and sensors. It starts by analyzing plant images to determine growth phases with a neural
network. Based on this, an AI model selects the best light wavelength for plant growth via nearby
fixtures. The system also detects plant stress using environmental data, predicts disease outbreaks,
identifies pathogens from images, and forecasts harvest times. Users receive notifications about
plant status and readiness for harvest. This technology aims to automate and improve indoor
farming efficiency for better crop yields and quality.

3) Non-Infringement
This patent focuses on advancing indoor farming through AI and sensor integration, aiming to
optimize plant growth by analyzing growth phases, adjusting light wavelengths, detecting stress,
predicting diseases, and notifying users about plant readiness for harvest. In contrast, PlantPulse
specializes in soil-based monitoring using a network of sensors to track real-time data like
humidity, temperature, and soil nutrients. It prioritizes safety and ease of use with modular
hardware and LoRaWAN connectivity, ensuring durable and low-maintenance operations. This
approach centers on optimizing soil conditions to support healthy plant growth, diverging from the
AI-driven indoor farming techniques of patent US11308715B2.

Conclusively, three different patents that could be related to our project were discussed; it was
explained how our current project differs from the ones listed, where two relied heavily on
Artificial Intelligence for data analysis and decision-making processes, whereas the third patent
focused solely on the monitoring of orchards without integrating broader environmental sensing
capabilities. By identifying these distinctions, we highlight the unique approach of our project.

D. Trademark Patents

```
Fig.16, displayed below, represents the trademark to be used for our product.
```
```
Fig 16. Trademark
```
## X. GLOBALIZATION

Globalization has significantly impacted how agricultural technologies such as PlantPulse are
developed and deployed across diverse markets. It is increasingly becoming more likely that a
product that finds success locally will find deployment globally to gauge the interest in foreign


markets. To reach the same level of success as other famous international brands and products, the
intelligent soil sensor system must be appealing in its functions and used for its targeted audience
regardless of the settings in which it will operate.

PlantPulse - a sophisticated network of soil monitoring sensors - leverages precision agriculture
principles to deliver customized soil management advice to users worldwide and produce results.
This approach enhances crop productivity and sustainability and positions PlantPulse as a pivotal
tool in the global agricultural sector. In addition to its practicality, diverse marketing practices will
be necessary to push the influence of the product into the international audience of various cultures.

A. Adapting to Global Markets

To succeed globally, PlantPulse must be adaptable to various agricultural environments and
regulatory landscapes. Potential success means the system complies with international standards
and accommodates diverse farming practices and climatic conditions. In addition to international
regulations, each country has its own set of criteria that govern the import and use of agricultural
technology.

Agricultural practices vary significantly worldwide due to differences in culture, climate, crop
types, and farming techniques. As such, the system must be versatile in its implementation to
support these varied factors effectively. The system should be capable of being configured to
support the specific crop cycles, planting techniques, and harvest schedules unique to each region.
For example, the scheduling and notification systems within PlantPulse will be modified to remind
users of the optimal times for planting or irrigating the plants based on local agricultural calendars.

Different climatic conditions affect how the technology will operate in the field. The attached
sensors and components must be robust and durable enough to handle various environmental
conditions, from humid and rainy to dry and hot climates of Southeast Asia, the Middle East, and
North Africa. Preparing for these situations might involve using materials and designs resistant to
corrosion, dust, and extreme temperatures to establish reliable performance regardless of stressors.
The performance of the soil sensors in the system can vary significantly based on the type of soil
in which they are being used. Soil types affect moisture retention, nutrient availability, and pH
balance. PlantPulse's sensors will need to be calibrated to reflect these variations accurately. For
instance, sensors used in sandy soils need different calibration settings than those used in clay-rich
soils to measure the parameters.

B. Compliance with International Standards / Reducing Trade Barriers

Global acceptance of agricultural technology relies heavily on compliance with international
standards such as those set by the International Organization for Standardization (ISO), the
International Electrotechnical Commission (IEC), and the World Trade Organization (WTO).
These standards ensure that technologies like PlantPulse meet universal safety, quality, and
environmental benchmarks, facilitating smoother market entry and acceptance across borders.

```
1) ISO [ 12 ]
```
The International Organization for Standardization (ISO) is an independent, non-governmental
international organization established in 1947 with a membership of 172 national standards bodies.
It brings together experts – through its members – to share their expertise and knowledge to develop
voluntary, consensus-based, market-relevant international standards that support innovation and
provide solutions to global changes. The various ISO standards for this product are ISO 14001, ISO
9001, and ISO 27001, which will be crucial in PlantPulse’s compliance with global markets.

```
2) WTO Agreements [ 13 ]
```

The World Trade Organization (WTO) is the only global international organization dealing with
trade rules between nations. Its primary function is to ensure that trade flows as smoothly,
predictably, and freely as possible. Established in 1995, the WTO currently has 164 member
countries, representing over 98% of the global trade and economic output. At their heart are the
WTO agreements, negotiated and signed by most of the world’s trading nations. This extensive
membership makes WTO agreements critical for any technology for widespread international use.
The agreements are legally binding contracts between member countries to facilitate stable and
predictable international trade. It covers many areas, including trade in goods and services,
intellectual property, and dispute settlement mechanisms.

Adhering to trade-related aspects of intellectual property rights (TRIPS) and sanitary and
phytosanitary (SPS) measures under WTO agreements is crucial. This ensures that PlantPulse can
be marketed and used in compliance with global trade laws, protecting both the technology and
the interests of local users.

3) IEC [ 14 ]
The International Electrotechnical Commission (IEC) is intrinsic in setting global standards for
all electrical, electronic, and related technologies. Established in 1906, the IEC facilitates global
trade and cooperation for electro-technologies, ensuring they are safe, efficient, and
environmentally friendly. With members from over 170 countries, including all the major trading
nations, the IEC’s standards are essential for achieving international compliance and acceptance
of electronic products.

Compliance with IEC standards plays a critical role in building trust and market acceptance; for
PlantPulse, this means ensuring that all electronic components are tested and certified to minimize
the risk of failure and increase the system's overall reliability. Complying helps eliminate potential
trade barriers, ensuring the system can be easily integrated into markets worldwide without needing
modifications or specialized adaptations. PlantPulse demonstrates its commitment to quality and
safety by complying with these standards.

C. Leveraging Local Insights

Understanding and integrating local agricultural knowledge and practices is vital for the global
scalability of PlantPulse. Engaging with local communities and stakeholders to adapt the
technology to meet regional needs enhances its marketability and ensures that it adds genuine value
to local agricultural practices. All this might involve customizing the sensor's nutrient tracking
capabilities to focus on nutrients particularly relevant in certain regions, such as potassium-rich
soils in sub-Saharan Africa or calcium-rich soils in southern Florida.

Leveraging these local insights can significantly enhance the effectiveness and acceptance of
PlantPulse in diverse markets. Different regions have unique soil compositions, crop types, and
agricultural practices. PlantPulse must tailor its sensor calibrations and analytics to these variables
to provide actionable insights. This customization ensures that the advice and monitoring provided
are relevant and beneficial to the specific needs of local users. Local climates and seasonal cycles
dictate agricultural activities. The system needs to align its monitoring and reporting features with
these cycles. The alignment ensures it is a technological tool and part of the local agricultural
rhythm.

Along with enduring the natural elements, PlantPulse must cooperate and engage with local
users, experts, and governing bodies to have valuable insights into the challenges and opportunities
within local sectors. By collaborating with these groups, the system can fine-tune its use to address


specific regional issues, such as pest infestations, soil degradation, or water scarcity. Furthermore,
partnerships with local universities and research institutions can facilitate ongoing improvements
and updates to the system based on the region's latest agricultural research in the area.

To maximize its usability and effectiveness, PlantPulse should provide educational resources
and support that are culturally and linguistically adapted to each market. This includes training
materials, user manuals, and customer support services tailored to the local language and farming
context. Making these resources accessible and relevant enhances user experience and builds trust
and loyalty among local users.

D. Collaboration Tools

Effective communication between team members is crucial to any technology project, especially
for geographically separated ones. For the PlantPulse project, maintaining seamless collaboration
and an efficient workflow is essential to the design and development of the system. To achieve this,
the team has integrated specific collaboration tools that support both synchronous and asynchronous
communication so that all team members are aligned and can contribute regardless of their physical
location.

Discord and WhatsApp were used as the primary tools. Discord offers robust features that
expedite effective real-time team interaction, including voice/video calls, screen sharing, and
organized channels to categorize the type of research. In this tool, we could brainstorm and think
critically about the next steps for the project. WhatsApp was a supplementary tool, providing
flexibility for team members if they could not join Discord group calls. For quick questions,
updates, and informal communication, WhatsApp bridged the gap between team members to keep
them in the loop with new updates and decisions regarding the project's design. The team also used
WhatsApp for file-sharing, allowing them to quickly transfer images, documents, and technical files
(like Arduino. INO files) across smartphones and computers.

By utilizing Discord for detailed, real-time collaboration and WhatsApp for quick, informal
communications, the PlantPulse team maintains high productivity and engagement. This
combination of tools caters to the diverse needs of the project. It ensures that every team member,
regardless of their role or location, can effectively contribute to the success of PlantPulse.

E. Interviews

The team conducted two interviews with members from educational institutions in different
countries to understand their perspectives on whether the PlantPulse system will find success in
their respective communities.

The first candidate interviewed was Maria Gomez from Universidad de Buenos Aires,
Argentina. She is a 3rd-year agronomy student and shared her thoughts on the product's potential
impact in Argentina, a country with vast agricultural sectors in soybean and wheat production. She
stated there is a strong emphasis on improving farm productivity and sustainability, especially
given the fluctuations in weather patterns. The challenges for its adoption in Argentina’s market
will be the cost and complexity of implementing PlantPulse. If we can keep the system cost-
effective and user-friendly, it will have significant potential for success. Education on the benefits
and operation of the system will be essential.

The second candidate interviewed was Aarav Singh of the Indian Institute of Technology (IIT),
Delhi, India. He is a 4th-year student in environmental engineering and discussed the adaptability
of PlantPulse in the diverse market of India, where most of the population is in rural settings. He
said many regions still rely on traditional farming techniques and that the agricultural landscape


needs to be more cohesive. There is a push towards modernization for better resource management
and yield operation, but the critical factors for its success will be affordability, ease of use, and
local language support. Local demonstrations are necessary to show the visible impact it can have
on crop output and farmer income. Traditional farming methods are deep-rooted, and any new
technology will have to be introduced in a way that respects these traditions.

In this section, we have demonstrated that globalization significantly shaped the development
and deployment of agricultural technologies like PlantPulse. For global success, PlantPulse must
appeal functionally across diverse environments and comply with international standards set by
ISO, IEC, and WTO to ensure safety, quality, and environmental integrity. The system must adapt
to varying agricultural practices and climatic conditions worldwide and engage with local
communities to ensure it meets regional needs effectively. This adaptability and compliance will
facilitate smoother market entry and acceptance, positioning PlantPulse as an integral tool in the
global agricultural sector.

## XI. STANDARD CONSIDERATION

In agricultural technology, integrated systems necessitate a range of industry-specific and
general technology standards. In developing the PlantPulse system, adherence to established
standards is crucial for ensuring functionality, safety, and market compliance. Applying these
standards is integral to the project's success, from construction to implementation. Here, the team
explores essential standards relevant to the PlantPulse system.

For a system to be a viable product on the market for consumers, PlantPulse will need to align
with standards set forth by key standardization bodies, including the Institute of Electrical and
Electronics Engineers (IEEE), the International Organization for Standardization (ISO), the
National Institute of Standards and Technology (NIST), and the International Electrotechnical
Commission (IEC) who often collaborate with the ISO.


A. IEEE Standards for Sensor Networks

The IEE provides critical guidelines that help design robust and reliable systems. For
PlantPulse, the following standards are particularly relevant to establishing compliance:

1) IEEE 802.15.4 [ 15 ]
The IEEE 802.15.4 standard governs low-rate wireless personal area networks (LR-WPANs)
for efficient communication between the wireless sensor nodes in a dispersed agricultural setting.
Adhering to this standard ensures that PlantPulse can operate efficiently across extensive
farmlands without excessive energy consumption, which is vital for sustainability goals. The
standard supports low data rate networks with devices needing long battery life. Ethically, this
standard supports the principle of non-maleficence, a core ethic in engineering and other fields. It
focuses on the motto, "Do not kill, do not cause pain or suffering, do not incapacitate, do not
offend, and do not deprive others of the goods of life." By ensuring reliable and energy-efficient
communication, PlantPulse reduces the risk of system failures that could lead to crop damage or
financial loss.

2) IEEE 1451 [ 16 ]
The IEEE 1451 standards define a set of protocols for network-capable intelligent transducers.
For PlantPulse, compliance with these standards means that all sensor data – soil moisture, nutrient
levels, or pH – is accurately and precisely captured and communicated in a standardized format.
This facilitates data transparency and makes the system more uncomplicated, straightforward, and
reliable. From an ethical standpoint, transparency is critical in maintaining trust with users by
ensuring that the data is accurate and verifiable. This aligns with the engineering ethics of honesty
and integrity, ensuring stakeholders can trust the data used for critical decisions regarding plant
care.

B. ISO Standards for Quality and Environmental Management

The ISO provides frameworks that are pivotal in maintaining high quality and environmental
stewardship in technology deployment:

```
1) ISO 9001 [ 17 ]
```
ISO 9001 is a globally recognized standard for quality management systems. It ensures that
PlantPulse adheres to a rigorous quality assurance process throughout its design, development, and
deployment. "It helps organizations of all sizes and sectors to improve their performance, meet
customer expectations, and demonstrate their commitment to quality. Its requirements define how
to establish, implement, maintain, and continually improve a quality management system (QMS)."
This standard embodies the ethical principles of beneficence and professionalism by committing
to high-quality outcomes that benefit end users and stakeholders. Compliance with ISO 9001 also
means that PlantPulse is built with a systematic approach to managing its processes and resources,
which directly impacts its functionality by enhancing reliability and user satisfaction.

```
2) ISO 14001 [ 18 ]
```
ISO 14001 focuses on effective environmental management systems (EMS). "It provides a
framework for organizations to design and implement an EMS and continually improve their
environmental performance. By adhering to this standard, organizations can take proactive
measures to minimize their environmental footprint, comply with relevant legal requirements, and
achieve their environmental objectives." For PlantPulse, this means implementing practices that
reduce its ecological footprint, such as minimizing waste and decreasing energy consumption


while operating its sensor networks. Ethically, this standard reflects the commitment to
sustainability and natural environment protection. Adherence to ISO 14001 not only helps mitigate
the impact of agricultural practices on the environment but also promotes a sustainable approach
to farming, playing an essential role in the ethical responsibility of engineering.

C. NIST Guidelines for Cybersecurity

With the increasing digitization of agricultural technologies, cybersecurity becomes paramount.
PlantPulse incorporates NIST guidelines to secure its network and data:

1) NIST Special Publication 800- 53 (SP 800 - 53) [ 19 ]
Cybersecurity is a significant concern when deploying IoT systems like PlantPulse. NIST SP
800 - 53 provides comprehensive security controls to protect information systems and data from
cyber threats. "The controls are flexible and customizable and implemented as part of an
organization-wide process to manage risk. The controls address diverse requirements derived from
mission and business needs, laws, executive orders, directives, regulations, policies, standards, and
guidelines. Finally, the consolidated control catalog addresses security and privacy from a
functionality and an assurance perspective." Perspectives, these controls are crucial for protecting
sensitive agricultural data and ensuring the privacy and security of user information. Ethically,
following these guidelines demonstrates a commitment to non-maleficence and justice, ensuring
that all users' data is secure and equitable.

D. IEC Standards for IoT Devices

The IEC shapes the standards for Internet of Things (IoT) devices by developing international
standards to ensure safety, efficiency, interoperability, and reliability. They will be vital for
enabling PlantPulse to communicate and function effectively across platforms and systems
worldwide:

1) ISO/IEC 27001 [ 20 ]
ISO/IEC 27001 is an international standard that “provides companies of any size and from all
sectors of activity with guidance for establishing, implementing, maintaining and continually
improving an information security management system.” It is essential to design PlantPulse as
cybercrime and new threats are constantly emerging. It will help the organization become more
aware of the risks and proactively identify and address weaknesses in the system. This standard is
essential for protecting sensitive data and ensuring robust cybersecurity measurements are in place.
Complying with this means that all data collected about agricultural variables is securely managed.
This requires PlantPulse to assess the risks associated with its data handling processes and
implement appropriate security measures to mitigate them. This includes controlling access to
data, encrypting sensitive information, and ensuring data integrity and availability through reliable
backup and recovery processes. From an ethical standpoint, adhering to ISO 27001 is vital for
maintaining the confidentiality and integrity of farmer data, thus upholding the principles of
privacy and trust. This alignment with ISO 27001 demonstrates PlantPulse's commitment to ethical
data management, ensuring that stakeholders can trust the system to be not only effective in its
functionality but also responsible in its data handling practices

2) ISO/IEC 27400 [ 21 ]
ISO/IEC 27400 provides “guidelines on risks, principles and controls for security and privacy
of Internet of Things (IoT) solutions.” This standard addresses the unique challenges associated
with IoT environments, including the number and diversity of connected devices, data-sharing
capabilities, and limited processing power. For PlantPulse, which involves a network of soil


monitoring sensors and other IoT devices, complying with ISO 27400 means implementing
security protocols designed to protect against vulnerabilities inherent in IoT systems. This includes
the encryption of data transmissions, securing endpoints, and ensuring that all devices within the
network are authenticated and authorized to prevent unauthorized access. The data collected from
fields—such as soil moisture levels, nutrient content, and other sensitive information—is
processed and stored with confidentiality. Compliance with this standard involves implementing
data minimization principles, where only necessary data is collected, and ensuring transparency in
data processing activities, allowing users to understand how their data is being used

3) ISO/IEC 30179 [ 22 ]
ISO/IEC 30179 is a standard that “specifies the Internet of Things system for ecological
environment monitoring in terms of the following: – system infrastructure and system entities of
the IoT system for ecological environment monitoring for natural entities such as air, water, soil,
living organisms; and – the general requirements of the IoT system for ecological environment
monitoring.” It details the requirements for reliable data collection, transmission, and processing
within IoT frameworks. For PlantPulse, the standard provides guidelines on the necessary
infrastructure to support IoT functionalities that monitor the soil conditions effectively. Adhering
to the policies and framework enhances its capability to deliver precise, actionable insights into
sustainable agricultural practices.

In this section, we have covered the standards that are relevant to the design and development
of the PlantPulse system in order for it to be accepted in the global markets. The team has carefully
selected standards that align with the project's technical requirements and ethical considerations,
focusing on ensuring functionality, safety, and market compliance. This approach aids in
maintaining the integrity and reliability of the system's data transmission. It facilitates its
acceptance across global and foreign markets, adhering to industry-specific and general
technological standards:

```
The standards listed below are in consideration of the project’s scope:
```
- IEEE 802.15.4
- IEEE 1451
- ISO/IEC 27001
- ISO/IEC 30179
These standards collectively provide safeguards to ensure that the system will be developed
with a strong foundation in communication, data integration, security, and ecological monitoring
without compromising the development process. With this in mind, the team behind PlantPulse is
committed to fully complying with the standards listed to ensure the highest standards of safety
and quality in the design and deployment of the product.


## XII. HEALTH AND SAFETY CONSIDERATIONS

Our project, PlantPulse, prioritizes health and safety in its design and implementation. The
system operates on a standard power supply of 120V 50-60 Hz AC, ensuring compatibility with
common household electrical systems while adhering to safety standards. Using low-voltage
components within the monitoring system minimizes the risk of electrical hazards. Furthermore,
the Arduino Nano r3 microcontroller is encased in a protective housing to prevent exposure to
moisture and dust, thereby reducing the risk of short circuits and electrical malfunctions. All
sensors and wiring are insulated and strategically placed to avoid physical contact, ensuring safe
operation within the garden environment.

In addition to electrical safety, our project addresses environmental health by continuously
monitoring soil and air quality. By providing real-time data on temperature, humidity, soil
minerals, pH, and fertilization levels, PlantPulse enables users to maintain optimal growing
conditions, reducing the need for excessive chemical fertilizers and pesticides. This promotes
healthier plant growth and minimizes environmental pollution and potential health risks associated
with chemical exposure. The user app offers alerts and guidelines for safe garden management
practices, empowering users to make informed decisions that benefit their plants and personal
well-being.

A. Liability

Our project, PlantPulse, has robust safety features to mitigate potential liability issues. We
ensure that all electrical components meet industry safety standards and are adequately insulated


to prevent accidental shocks. Additionally, we provide comprehensive safety guidelines to educate
users on the proper installation and use of the system. Users are advised to regularly inspect the
system for any signs of wear or damage and to follow all maintenance instructions to ensure
continued safe operation.

B. Intentions Regarding Use and User Safety

Our primary intention with PlantPulse is to offer a safe, user-friendly gardening solution that
enhances plant health without compromising user safety. To ensure this, we have implemented
several safety recommendations:

- Always disconnect the power supply before performing any maintenance on the system.
- Use the app's alerts to monitor system status and promptly address issues.
- Keep the microcontroller and sensors away from direct exposure to water and extreme
    weather conditions.
- Ensure all components are securely installed, and wiring is kept out of high-traffic areas to
    prevent tripping hazards.

C. Labor Safety

Labor safety is a critical aspect of our project development and installation processes. We
prioritize the well-being of all individuals involved in assembling, installing, and maintaining the
PlantPulse system. Safety measures include:

- During installation, we provide personal protective equipment (PPE), such as gloves and
    safety goggles.
- Training installation personnel on proper handling of electrical components and tools.
- Implementing strict adherence to occupational safety standards to prevent accidents and
    injuries.
- Conduct regular safety audits and inspections to ensure compliance with safety protocols
    and address any potential hazards promptly.


## XIII. ENVIRONMENTAL CONSIDERATIONS

In recent decades, increasing environmental consciousness has compelled businesses to
innovate sustainably, leading to products designed with minimal ecological impact. Our PlantPulse
project embodies this shift, prioritizing the development of an eco-friendly intelligent garden
system that optimizes resource use and reduces environmental harm. This initiative aligns with
global sustainability trends and supports community health and well-being. By integrating
advanced technologies with responsible design principles, we aim to contribute positively to
environmental stewardship and demonstrate the feasibility of sustainable innovations in everyday
technology.

A. Restriction of Hazardous Substances Directive (RoHS)

The RoHS Directive, initiated in the European Union, impacts the electronics industry by
mandating the reduction of hazardous substances in electronic products. Initially banning six
materials, its regulations, requiring compliance since July 2006, have expanded under RoHS 3
(Directive 2015/863) to include ten restricted substances:

- Cadmium (Cd):< 100 ppm
- Lead (Pb): < 1000 ppm
- Mercury (Hg): < 1000 ppm
- Hexavalent Chromium: (Cr VI)< 1000 ppm
- Polybrominated Biphenyls (PBB): < 1000 ppm 60
- Polybrominated Diphenyl Ethers (PBDE): < 1000 ppm
- Bis(2-Ethylhexyl) phthalate (DEHP): < 1000 ppm
- Benzyl butyl phthalate (BBP): < 1000 ppm
- Dibutyl phthalate (DBP): < 1000 ppm
- Diisobutyl phthalate (DIBP): < 1000 ppm


This directive highlights the critical nature of environmental health and safety standards in
manufacturing processes. An illustrative case is the cessation of nickel-cadmium batteries, once
popular due to their durability and efficiency, following studies revealing severe health risks to
workers exposed to cadmium, including various forms of cancer and chronic health issues. This
led to cadmium's classification as a hazardous material, prompting industries to adopt safer
alternatives for battery production.

### B. Functions

PlantPulse can be easily installed in various settings, including homes, offices, and businesses.
Users install the system by mounting it and configuring its settings using a provided serial number
through an accompanying app. Users unscrew the device from its setup for disassembly,
maintenance, or relocation purposes. Manufacturers can disassemble the device more thoroughly
by removing additional screws to expose all internal parts, facilitating repairs or upgrades. This
straightforward assembly and disassembly process is vital, enhancing user understanding of the
system's operation and enabling easy maintenance of its internal components.

C. Hannover Principles

The Hannover Principles, developed by William McDonough and Michael Braungart for the
2000 Expo in Hanover, Germany, guide the design of products and buildings, emphasizing
environmental impact and sustainability. These principles advocate for coexistence between
humanity and nature, promote interdependence, and highlight the responsibility of design
decisions on human and ecological health. They encourage creating objects of long-term value,
eliminating waste, utilizing natural energy, and continually improving through knowledge sharing.
Our PlantPulse project aligns with these principles by using high-quality, durable materials and
renewable energy sources to minimize waste and environmental impact while enhancing
functionality and longevity.

Our PlantPulse project strives to embody the Hannover Principles by focusing on sustainability
and minimizing environmental impact. We use durable, high-quality materials that require
minimal maintenance, reducing waste output to virtually none. Our system's components are
designed for longevity and powered by a renewable energy source that operates continuously.
However, the design is specifically tailored to monitor plant environments, and extending its
application to other substances or locations should be approached cautiously by users. We also
continuously seek user feedback to enhance both the hardware and software aspects of PlantPulse.

D. Life Cycle Impact Assessment (LC/A)

Engineers actively employ the Life Cycle Impact Assessment (LCIA) to meticulously evaluate
the environmental effects of a product throughout its entire life cycle—from the selection of
materials to its eventual usage by consumers. This assessment encompasses the ecological impacts
of repairing, maintaining, and distributing the product. The LCIA involves compiling an inventory
of all materials used in the product's creation and assessing their potential environmental impacts.
Despite its limitations, such as being unable to fully quantify or predict the ecological damage due
to data gaps, engineers rely on the LCIA to ensure that their products are designed to minimize
adverse environmental effects. This method is instrumental in guiding product development
towards sustainability, although it cannot always provide a complete picture of a product's
potential ecological footprint.


In conclusion, our PlantPulse project is designed to enhance environmental sustainability by
minimizing the impact of gardening practices. The RoHS directive informs us to avoid hazardous
substances in the system's design, ensuring safety and compliance. The Hannover Principles guide
us in maintaining sustainability and environmental awareness throughout our design process.
Furthermore, the Life Cycle Impact Assessment (LCIA) aids in selecting the most environmentally
friendly materials for PlantPulse, aligning with our goal of ecological responsibility.

## XIV. SUSTAINABILITY CONSIDERATIONS

Sustainability is crucial for designing products that are durable and eco-friendly. Our PlantPulse
project prioritizes sustainability by minimizing environmental impacts and incorporating
renewable resources to lessen our ecological footprint. The ultimate goal of sustainable design
within our project is to reduce potential adverse environmental effects. By integrating these
sustainable practices, PlantPulse aims to have a minimal impact on its surroundings.

A. Hardware

Our PlantPulse project employs a comprehensive lifecycle approach to address the urgent
environmental sustainability needs. We actively engage in energy conservation, streamline
communication between devices, and focus on reducing operational expenses through the Life
Cycle Assessment (LCA). This rigorous assessment allows us to efficiently foresee and mitigate
environmental impacts, positioning PlantPulse as a sustainable solution.

We are committed to adapting our system for the evolving smart city infrastructure. By
leveraging advanced mesh network technology, we can connect multiple PlantPulse units, ensuring
scalable and sustainable urban environmental management. This system meets current needs and
offers flexibility to adapt to future demands, making it a viable long-term solution.

Our proactive integration of LCA and ongoing commitment to improving sustainability helps
ensure that PlantPulse remains a leader in eco-friendly technology. These efforts underscore our
dedication to creating a product that serves practical needs and contributes positively to
environmental conservation. This strategic focus is crucial as we expand our technology's
application in smart cities, focusing on durability, efficiency, and minimal environmental impact.

B. Software

In our PlantPulse project, we emphasize sustainable software development, ensuring our code
is bug-free, clear, and functional. Bug-free software conserves engineering time by reducing the
need for extensive debugging. Clear, well-commented code enhances readability and simplifies
updates, making it accessible for future modifications. Our functional code ensures efficient
operation, contributing to the sustainability of our system.


We are committed to maintaining our software with minimal need for manual updates. Using
remote updates via advanced platforms ensures our software remains current and sustainable
without physical interventions. This approach makes our code adaptable and maintains its
efficiency over time.

Moreover, the PlantPulse project aims to be environmentally sustainable by minimizing energy
consumption and waste. We incorporate renewable energy sources, such as solar panels, to power
our systems, reducing our carbon footprint. As engineers, we are acutely aware of our products'
environmental impacts and strive to minimize them, ensuring our solutions are durable and have a
prolonged lifecycle with minimal ecological impact. Every aspect of our design and operational
practices reflects this commitment to sustainability, making PlantPulse a leading example of eco-
friendly innovation in innovative gardening technology.

## XV. MANUFACTURABILITY CONSIDERATIONS

This section demonstrates the importance of making the right decisions in the initial stages of
the project. It's crucial that we make the correct decisions since they will affect the overall outcome
in the future. For this section, we are going to focus on:

```
A. Simplify the Design
B. Use common parts
C. Design parts positioning and handling
D. Design for automated production
E. Error-proof product design and assembly
```
A. Simplify the Design

There are countless reasons to simplify a design, but the main reason is that it's better to keep
it simple than complex. By streamlining our design and making it the most efficient with the fewer
parts possible, we would have the benefit of having to deal with fewer defective parts, less
troubleshooting, fewer complaints, and, in general, better working systems. If we can simplify our
design, we can work better and locate sources of errors much more quickly. Also, the hardware-
building stages would become more accessible and faster since we would only have to work with
a few parts. It’s essential to simplify the design process in the initial stages since if we leave this
to the end, we can run into problems that could become more significant problems due to parts
compatibility.

B. Use common parts

For the parts that our project requires, we should always take a look first at standardized parts
that we can quickly get anywhere in order to save time manufacturing a specific part or putting
together components to make it work. Also, this will reduce the waste that our project creates, and
the quality of the product will increase since the parts are standard and have been tested and
manufactured in the past.

C. Design parts positioning and handling.

Regarding component handling, adherence to the following guidelines is advised: To reduce
the risk of unintentional injuries, try to avoid using too sharp parts and use as few flat, thin, and


difficult-to-handle pieces as possible. Make sure the sections are distinguished from one another
by having unique properties. Strive for symmetrical designs and create components that are easily
twisted together. Avoid parts that are prone to breaking and do not include pieces that will add
much labor to the assembly workers' workload.

D. Design for automated production

When we think about our future project, we see our device being manufactured using a
completely automated process. Since automation is the most efficient way of manufacturing, we
must consider having our device as clean as possible, avoid any loose cable or material that can
get in the way of the machine, and make it easy to manage so the machines can pick it up, hold it
and drop it without affecting the device, have no holes on the product to avoid damage, look for
the best assembly process that would benefit us.

E. Error-proof product design and assembly

It's inevitable that errors happen; sometimes, errors are out of control, but what we can do is
prepare our design to be as error-proof as possible in order to prevent unfortunate situations. Error
prevention in assembly product design should consider both the production process and the end
user's smooth experience. The layout ought to be both intuitive to use and error-free. We must
keep our product user-friendly while also keeping it error-proof. We must consider all sources of
errors from the start of the assembly to the customer errors that may happen.


## XVI. ETHICAL CONSIDERATIONS AND SOCIAL IMPACT............................................

When working on a technological product, we must look at every aspect that is going to be
affected, which includes ethical considerations and social impact on every corner, from the
environment to any other possible social impact that the product of the project may have. Engineers
continuously transmit their vision of how they want the world to be through their work; this could
be good or, depending on how ethical it is. It is essential that we envision our project in the world.
Every project must comply with the IEEE (Institute of Electrical and Electronics Engineers) Code
of Ethics.

### A. Ethical Considerations

When a product does not comply with the Code of Ethics, it creates an ethical dilemma, which
can be addressed by using the Ethical Model Theory to see what option the team should move
forward with. Our project is not an exception to this rule; we are fully committed to complying
with the IEEE Code of Ethics, and we will have a strict procedure to ensure we comply and do not
break any code while we are working on the project. The following codes were carefully read and
reviewed by everyone involved in this project to ensure that we comply with them:

1. To hold paramount the safety, health, and welfare of the public, to strive to comply with
    ethical design and sustainable development practices, and to disclose disclosers that might
    endanger the public or the environment.
2. To avoid real or perceived conflicts of interest whenever possible and disclose them to
    affected parties when they do exist.
3. To be honest and realistic in stating claims or estimates based on available data.
4. To reject bribery in all its forms.
5. To improve individuals' and society's understanding of the capabilities and societal
    implications of conventional and emerging technologies, including intelligent systems.
6. To maintain and improve our technical competence and to undertake technological tasks
    for others only if qualified by training or experience after full disclosure of pertinent
    limitations.
7. To seek, accept, and offer honest criticism of technical work, to acknowledge and correct
    errors, and to credit appropriately the contributions of others.
8. To treat all persons fairly and not engage in acts of discrimination based on race, religion,
    gender, disability, age, national origin, sexual orientation, gender identity, or gender
    expression.
9. To avoid injuring others, their property, reputation, or employment by false or malicious
    action.
10. To assist colleagues and co-workers in their professional development and to support them
    in following this code of ethics.


To adhere to the IEEE Code of Ethics, we will actively seek and accept all genuine criticism.
We recognize that with our project, we must take full responsibility for our decisions and any
resulting conflicts. As the inventors of PlantPulse, we are acutely aware of the potential risks
associated with modern technology, particularly the threat of cyberattacks. A possible ethical
dilemma that could significantly interfere with the functionality of PlantPulse involves a
sophisticated hacking incident.

Imagine a scenario where a hacker gains unauthorized access to the PlantPulse network. This
hacker could exploit vulnerabilities in the system’s security protocols to infiltrate the network,
gaining control over the data flow and sensor operations. The hacker could then manipulate the
data being transmitted by the sensors, providing false readings on soil moisture levels, plant health,
and environmental conditions.

For example, the hacker could send incorrect data indicating that fields are parched when they
are not, prompting the automated irrigation systems to overwater the crops. This not only wastes
valuable water resources but could also lead to waterlogged soil and crop damage. Conversely, the
hacker might falsify data to show optimal conditions when the plants are suffering from pests or
nutrient deficiencies, causing farmers to miss critical intervention opportunities. To address this
type of situation, we have incorporated the following options into Table XVIII.

```
TABLE XVIII. OPTIONS FOR RESPONDING TO THE ETHICAL DILEMMA
Options Description
1 Quickly identify the breach, patch vulnerabilities, and strengthen security measures to prevent further
attacks.
2 Immediately disclose the breach to all affected parties, including users, regulatory bodies, and
partners.
3 Focus on actions that safeguard PlantPulse’s long-term interests, such as investing in innovative
cybersecurity technologies.
4 Users are provided with clear information regarding the product's functionalities and its inherent
limitations without any assistance being provided.
```
```
TABLE XIX. PHILOSOPHIES FOR RESPONDING TO THE ETHICAL DILEMMA
Theories
Options Utilitarianism Egoism Kantian Rights Sum
```
#### 1 1.00^ 0.25^ 0.75^ 0.50^ 2.50^

#### 2 1.00^ 0.50^ 1.00^ 1.00^ 3.50^

#### 3 1.00^ 1.00^ 1.00^ 1.00^ 4.00^

#### 4 0.00^ 1.00^ 0.25^ 0.25^ 1.50^

Table XIX shows all the options weighed against every ethical theory and the addition of those
all together at the end, which at the end will yield the best overall choice to solve the moral
dilemma of this project. The best option is option 3, when all the options are evaluated using the
Ethical Theory Model.


### B. Social Impact

Our project's development can revolutionize agriculture and environmental monitoring, with
significant social impacts across various domains. First, in the realm of agriculture, such networks
could enhance food security by providing real-time data on plant health, soil conditions, and
environmental factors. This information can enable farmers to optimize their practices, leading to
increased crop yields and more efficient resource usage. The implementation of these technologies
could help address the challenges posed by a growing global population and climate change,
ensuring a more stable and sustainable food supply. Moreover, the increased productivity and
efficiency in farming could reduce costs for consumers, making healthy food more accessible and
affordable.

From a local standpoint, PlantPulse could be used to transform city planning and management,
contributing to the development of "smart cities." By integrating these networks into urban green
spaces, cities can monitor and maintain vegetation health more effectively, enhancing urban
biodiversity and ecological resilience. This, in turn, can improve air quality, reduce the urban heat
island effect, and contribute to overall public health and well-being. Additionally, green spaces
have been linked to psychological benefits, providing residents with areas for recreation and stress
relief. The data collected from these networks can inform policies and initiatives aimed at creating
more livable and sustainable urban environments.

During the interview process, we found out that one of the most significant issues was dead
plants and the process of replacing them. This is ethically wrong, and plants are dying due to
negligence. Our device can help with that issue since it will measure all the required data to keep
the plants healthy. About half of the interviews that we performed mentioned the problem of dead
plants; plants are alive just like us, so we should look after them just like they look after us with
the many benefits they provide to us.

Globally, plant sensor networks contribute to sustainable agriculture by optimizing resource
management and mitigating environmental impacts. They facilitate global food security efforts
and promote resilient agricultural practices amidst changing climates. Urban applications reduce
the ecological footprint of cities, enhancing global sustainability goals.

However, the widespread deployment of projects involving plant sensor networks also raises
essential ethical and privacy concerns. The data generated by these networks, if not effectively
managed, could be used to infringe on individual privacy or result in unequal access to information
[ 5 ]. For instance, large agribusinesses might leverage this technology to gain a competitive edge,
potentially marginalizing small-scale farmers who need help to afford the same level of
technological investment. Furthermore, the collection and use of environmental data need to be
governed by clear policies to ensure transparency and prevent misuse. Addressing these concerns
requires careful consideration of the social and ethical implications of plant sensor networks,
promoting equitable access and responsible data governance to maximize their benefits while
minimizing potential harms.

Based on Sebastian Deterding's Talk, the intention that we can bring with our design is to
facilitate the process of taking care of plants in local areas as well as globally, from a small garden
to a big nursery of plants. We intend to create satisfaction and improvement of plant health within
the garden section. An unintended effect could be that the user needs to check the garden regularly,
and the system may require more materials to keep the plants alive. The values we use to judge
this effect are autonomy and user stimulation. We want a system that can keep the plants healthy
but also connects the garden with the user and makes it essential for the user. Our vision of a good


life includes connecting with nature while having safety and relaxation, all of which are created
by our design automation and interface that connects the user with the garden.

Finally, since ethical and social impacts necessitate a thorough analysis of any new product,
our team must ensure that no ethical dilemmas violate established codes of ethics. Should such
issues arise, they must be addressed effectively using the Ethical Theory Model. As engineers, it
is our responsibility to maintain high standards and develop a product that contributes positively
to the world. While PlantPulse may encounter ethical challenges, our team is committed to
addressing them conscientiously. Our goal is to foster a cleaner environment and promote food
sustainability across society, enhancing enjoyment and well-being for all.


## XVII. CONCEPT DEVELOPMENT

This section narrows down the options for solving our problem and chooses the best solution
to provide the best general outcome. We considered many options when we presented our problem;
these options could solve the problem, but we need the right solution to our problem. Picking the
right option allows us to work effectively and fulfill our objectives as a team. Each option will
have different outcomes and trade-offs that we need to work on, but by selecting the concept, we
can guarantee that we will pick the right one. For this concept development process, we go through
several steps to ensure we end up with the right solution. First, we see our available options, and
we list the advantages and disadvantages of each one; then, we weigh each option against each
other and determine the best option to solve our problem.

PlantPulse has four main factors within the design that must be discussed: how are we going to
power the device, how are we going to supply water to the plants in the enclosure, how is light
going to get to the plants in order to keep the plants healthy, and how are we going to connect the
device to the server. We considered that we could power the device with solar energy or with
batteries, the water can be preserved in a reservoir and distributed using a water pump with an
irrigation system, or using a solenoid valve, light can get to plant naturally by using sunlight or
artificially using artificial lights, and finally, the wireless connection can be established using Wi-
Fi or Bluetooth. These factors will be combined to show the advantages and disadvantages of each
and finally determine the best combination.

A. Concept Fan

Fig. 17 represents all the available options for us to develop PlantPulse and the several viable
solutions we need to narrow down to get the right solution. The central part of the device will be
a Raspberry Pi; from the Raspberry Pi, everything else will come together; it will act as the
microcomputer of the device and control many actions. To track all the health data of the plants,
we will use digital sensors, including moisture, fertilizer, lighting, pH, and more. The main factors
that could vary are water supply, light supply, power sources, and wireless connectivity.

```
Fig 17. CONCEPT FAN FOR PLANTPULSE
```

B. Alternative Options

The following Fig. 18 , Fig. 19 , Fig. 20 , and Fig. 21 show the different approaches we take to
solve the problem; each figure represents a method that we evaluate and lists their advantages and
disadvantages.

Fig. 18 shows the systems being solar powered; solar-powered benefits not only by providing
energy to the device but also with solar lighting to keep the plants healthy, also a water pump
connected to a water reservoir which will pump the water through a tubing system to perform the
irrigation in the garden section, all these components would be wirelessly connected using
Bluetooth which provides connecting in particular in range.

Fig 18. ALTERNATIVE 1 “PLANTPULSE ECO”
After evaluating this method and considering it, the advantages and disadvantages are shown
below:

```
1) Advantages:
```
- Uses renewable energy.
- Powerful irrigation by having a water pump.
- The water pump allows the water reservoir to be well placed.
- Costs can be cut thanks to sunlight and Bluetooth.
2) Disadvantages:
- Weather can directly affect the device.
- Maintenance could be complicated for the user.
- Solar panels could increase costs.
- Less range and lower speed due to Bluetooth connectivity.
Fig. 19 represents the PlantPulse system connected through Wi-Fi, which provides better range
and speed, using a water pump connected to a water reservoir which will pump the water through


a tubing system to perform the irrigation in the garden section, being AC powered and using
artificial light to grow the plants without the need of sunlight.

Fig 19. ALTERNATIVE 1I “PLANTPULSE”
After evaluating this method and considering it, the advantages and disadvantages are shown
below:

```
3) Advantages:
```
- New features can be added thanks to Wi-Fi.
- Powerful irrigation by having a water pump.
- The water pump allows the water reservoir to be placed better.
- Lights can be controlled and scheduled.
- It is not affected by weather conditions.
4) Disadvantages:
- Power outages could hurt the plants.
- We may need to replace the lights at some point.
- Wi-Fi could become less secure when transferring information to the app and server.
Fig. 20 Represents the PlantPulse system connected through Wi-Fi, using a solenoid valve to
perform the irrigation in the garden section, being AC powered, and using artificial light to grow
the plants without needing sunlight.


```
Fig 20. ALTERNATIVE III “PLANTPULSE V2”
5) Advantages:
```
- New features can be added thanks to Wi-Fi.
- Lights can be controlled and scheduled.
- It is not affected by weather conditions.
6) Disadvantages:
- Power outages could hurt the plants.
- We may need to replace the lights at some point.
- The solenoid valve can increase the cost.
- Weaker irrigation is due to water flowing by itself.
- Wi-Fi could become less secure when transferring information to the app and server.
- The water reservoir must be placed strategically for the solenoid valve to work correctly.

Fig. 21 Represents the PlantPulse system connected through Bluetooth, which limits the range
for the user, using a solenoid valve attached to a water reservoir with an open and close mechanism
to perform the irrigation in the garden section, being AC powered and using artificial light that
would mimic the effects of sunlight to grow the plants without the need of the sun.


```
Fig 21. ALTERNATIVE IV “PLANTPULSE SHORT RANGE”
7) Advantages:
```
- It is lower cost since it connects through Bluetooth.
- Lights can be controlled and scheduled.
- It is not affected by weather conditions.
- Better security overall.

```
8) Disadvantages:
```
- Power outages could hurt the plants
- We may need to replace the lights at some point.
- The solenoid valve can increase the cost.
- Weaker irrigation is due to water flowing by itself.
- The water reservoir must be placed strategically for the solenoid valve to work.
- Less range and lower speed due to Bluetooth connectivity.

C. Concept Selection

After all these options, we must select the best alternative to solve our problem, and then we
must go back and look at our objectives and constraints. For this, Table XX is created to determine
the importance of 5 categories. We will provide the importance on a scale from 1 to 9, then
compare each category based on the importance. Then, a weighted scale must determine the best
alternative to solve our problem.


```
TABLE XX. WEIGHT CALCULATION TABLE
Safety User-
friendly
```
```
Modularity Scalability Marketability G.
mean
```
```
W.
mean
Safety 1.00 3.00 4.00 2.00 3.00 2.49 0.423
```
```
User-friendly 0.33 1.00 2.00 3.00 4.00 1.36 0.231
```
```
Modularity 0.25 0.50 1.00 2.00 2.00 0.84 0.143
```
```
Scalability 0.50 0.33 0.50 1.00 2.00 0.74 0.126
```
```
Marketability 0.33 0.25 0.50 0.50 1.00 0.45 0.077
```
```
Total 5.88
```
Our team determined that safety is the number one priority in our objectives, followed by user-
friendliness and modularity. This makes sense since we want to have a safe product that is easy to
use.

```
TABLE XXI. CONCEPT SELECTION TABLE
Constraints I II III IV
```
```
Ease of Use Yes Yes Yes Yes
```
```
Cost Yes Yes Yes Yes
```
```
Accuracy Yes Yes Yes No
```
```
Objectives W
```
```
Safety 0.423 3.00 1.269 5.00 2.115 3.00 1.269 3.00 1.269
```
```
User-Friendly 0.231 2.00 0.462 4.00 0.924 2.00 0.462 2.00 0.462
```
```
Modularity 0.143 3.00 0.429 5.00 0.715 4.00 0.572 2.00 0.286
```
```
Scalability 0.126 1.00 0.126 4.00 0.504 3.00 0.378 1.00 0.126
```
```
Marketability 0.077 2.00 0.154 3.00 0.231 3.00 0.231 1.00 0.077
```
```
Total 2.440 4.489 2.912 2.220
```

Table XXI shows the alternatives going against each other using the weight we determined.
Each alternative was rated, and the constraints were included. Each alternative is assigned a
number from one to five, with five being the maximum, for how well it satisfies that objective.
That number is then multiplied by the weight, and the sum of the products for each purpose is the
total score.

Based on the table, alternative II has the highest score. Hence, it is the best alternative out of
the four we stated. Also, it does not violate any of our constraints, so it is the alternative that we
should move forward with and solve the problem using that solution. Alternative II works with a
water pump, which allows placing the water reservoir in an accessible place, Wi-Fi connectivity,
which is fast and allows to work on the device in the future without speed or range restrictions,
and AC powered so it can be placed indoors or outdoors, and finally have artificial lights so we do
not get affected by bad weather conditions. This alternative has the best trade-off and is the least
inconvenient—a score of 4.489 shows it is the most effective and reliable alternative. Hence, the
team will design and manufacture Alternative II.

Upon nearing the completion of the project, the team believe that they have adhered to the
original concept development plan. Throughout the duration of working on the PlantPulse system,
there were no instances of new features or components being proposed on top of the existing
functions and operations. The team focused on refining the initial objectives and ensuring that each
planned component and feature was implemented effectively. Every decision was guided by our
original goal of creating a modular, scalable, and user-friendly system for monitoring soil
conditions. The selection of components, such as the RS485 soil sensor, WS2812B LED strip, and
ESP8266 microcontroller, strictly aligned with the predefined requirements. Additionally, the
integration of wireless connectivity and automation features, like the water pump and relay module,
adhered to the outlined functionality without introducing unnecessary complexity. This disciplined
approach ensured that the project remained on track, both in terms of functionality and budget,
while delivering a system that fulfilled its intended purpose without deviation.


## XVIII. END PRODUCT DESCRIPTION AND OTHER DELIVERABLES

Every project must have a final stage, an end of the project, that shows what the users will
receive when we finish the project. End product descriptions break down the project building
process and how the developers and designers went through the project in each section. It also
shows the features and abilities the product will have once it is completed and helps the users and
developers understand the layers of the device. Here, we explain how the product will work and
how every component of the device works and connects to the other. Also, this section helps us to
show how our product will work and be successful, how our ideas came into an actual product,
and how we made our idea a reality.

### A. End Product Description

The end product description shows how the final product will work and the features it will be
able to do. It shows the components that make the product work from bottom to top. Everything is
incredibly detailed and well explained to understand better how the product intends to work. All
these specifications are necessary because they show the developers what connects to what and to
understand the entire device clearly. Also, it is helpful to the users because it informs them of the
product they are using.

We defined three levels of specifications from level 0 to level 2, and we broke down every layer
of components the final product will have. This level demonstrates what PlantPulse is and how it
is built from bottom to top. Fig. 22 is a level 0 block diagram of PlantPulse's general form. It shows
the device's inputs and outputs. It has a power source and input data from the sensors; all these
data are collected and viewable in the app for the user. Also, Wi-Fi is used to receive and transmit
data to the user, track plant health, and generally keep the system on track.to top. Fig. 22 is a level
0 block diagram of PlantPulse's general form. It shows the device's inputs and outputs.

Fig 22. Level 0 view of PlantPulse
It has a power source and input data from the sensors; all these data are collected and viewable
in the app for the user. Also, Wi-F receives and transmits data to the user, tracks plant health, and,
in general, keeps the system on track.


Table XXII below shows the level 0 functionality, input, and output. PlantPulse will gather the
inputs, such as temperature and humidity, around the garden. Internet connection makes this
operation possible since it is fast and reliable. Also, the user can see this data on the app.

```
TABLE XXII. LEVEL 0 INPUTS, OUTPUTS, AND FUNCTIONALITY
```
Now that we have an idea of how PlantPulse will work, we can show more detail on how every
component inside PlantPulse will work. Every component interacts with the system, and each
element will track something or perform something different. Fig. 23 shows the interconnections
within PlantPulse; everything connects to a fully automated process of caring for the plants, from
the microcomputer to the irrigation system. The microcomputer acts as the brain of the device; the
microcontroller handles the information of the digital sensors and sends it to the microcomputer;
the digital sensors are connected to the microcontroller to track the plant's vitals; the irrigation
system and lighting system are connected to the microcomputer as well to trigger them in case the
plants need them. All these elements will keep the plant healthy and output the data into the user
App.

```
Module PlantPulse
```
```
Input
```
```
Power (120 V 50-60 Hz AC)
Temperature and humidity around the garden.
Plant minerals in the soil (Nitrogen, Potassium, Phosphorus)
pH and fertilization levels.
Input from user app.
Temperature and humidity in the garden soil.
Output Plant health tracking in the app.
Data transmitted via Wi-Fi.
Functionality The garden is fully automated; users can track all the plants' health vitals
and every movement and data on the app.
```

```
Fig 23. Level 1 view of PlantPulse
```
Table XXIII below illustrates in detail what each module does, what input they receive, and
what output they send. The digital sensors gather data from the soil and around the plant to track
all the plant vitals; these data connect to the microcomputer, which sends that data to the irrigation
and lighting systems, which will detect if the plants need water or light and trigger accordingly.
Also, the user will be able to set schedules for irrigation and lighting, and the microcomputer will
receive the schedules and activate the systems accordingly. Finally, the data communication
happens within the system and app through Wi-Fi.

```
TABLE XXIII. LEVEL 1 INPUTS, OUTPUTS, AND FUNCTIONALITY
```

```
Module Digital
Sensors
```
```
Microcompu
ter
```
```
Lighting
System
```
```
Irrigation
System
```
```
Microcontroll
er
```
```
LoRaWAN
Module
Input Power Power Power Power Power Power.
Plant vital
data from
the soil.
```
```
Plant
measurements
from digital
sensors.
```
```
Data from
microcomput
ers regarding
plant
measurement
s.
```
```
Data from
microcomputer
s regarding
plant
measurements.
```
```
Data from
digital sensors
```
```
Digital sensors
readings.
```
```
Plant vital
data from
the
environment
.
```
```
The user input
includes
lighting and
irrigation
schedules.
```
```
Light
schedules
from
microcomput
er (user
input).
```
```
Irrigation
schedules from
microcomputer
(user input).
```
```
Output Plant health
measuremen
ts.
```
```
Plant
measurements
into the user
app.
```
```
Trigger
lights if there
is a schedule
set on or the
plant; the
lights need to
be on due to
low
measurement
s.
```
```
Trigger
irrigation
system if there
is a schedule
set or the plants
need water due
to low
measurements.
```
```
Data from
digital sensors
processed.
```
```
Ease the
process of
transmitting
data to our
Trigger server.^
irrigation
system if
necessary.
Trigger the
lighting
system if
necessary.
Functional
ity
```
```
Measure
plant health
data in soil
and
environment
and send
data to a
microcompu
ter for
further
processing.
```
```
Process all the
inputs on the
device to
manage data,
send data to
the server to
be viewable in
the app, and
operate
lighting and
irrigation
systems.
```
```
Provide light
to the plants
indoors or
outdoors and
automate the
process of
lighting them
for their
health.
```
```
Provide water
and nutrients to
the plants on
set schedules or
when required.
```
```
Handle and
receive data
from digital
sensors.
```
B. Functions

The level 1 diagram shows a generalized view of the modules on PlantPulse; now, we can move
up to level 2, enabling even more detail on how each module is built and connected and what goes
into it. The first block diagram is the digital sensors, and it shows the NPKTHC-S, which is the
soil sensor; it will take care of the nutrients in the plants such as potassium, nitrogen, phosphorus,
and pH, which enables the fertilization levels as well. Also, these sensors measure the temperature


and humidity of the soil. Then, we have the DHT22, which measures the temperature and humidity
in the environment.

Fig 24. Level 2 view of the digital sensors.
Table XXIV below explains each sensor's input, outputs, and functionality. It is a more in-depth
view of how they work.

```
TABLE XXIV. LEVEL 2 INPUTS, OUTPUTS, AND FUNCTIONALITY OF DIGITAL SENSORS
Digital Sensors Soil Sensor Moisture Sensor
Input Potassium, nitrogen, and
phosphorus yield fertilization
levels. Ph levels.
```
```
Power
```
```
Temperature and humidity in the
soil.
```
```
The temperature in the environment.
```
```
Power Humidity in the environment.
Output Nutrient measurements, along
with temperature and humidity
in soil.
```
```
Temperature and humidity in the environment.
```
```
pH levels.
Functionality Measure nutrients, temperature,
and humidity in the soil.
```
```
Capture temperature and humidity in the environment
and send data to a microcomputer.
```
A microcontroller handles all the data from the digital sensors; we are using the Arduino Nano
r3 due to the easy compatibility with our microcomputer; it consists of a chip integrated, which is
the Dual-core Arm Cortex M0+ processor, which is very good for what we are doing, it has the
pins on the sides to connect all the digital input. Fig. 25 below is the block diagram of the
microcontroller.


Fig 25. Level 2 view of the microcontroller (Arduino Nano R3)
Fig 26.
Table XXV below explains the microcontroller's input, outputs, and functionality. It is a more
in-depth view of how it works, functions, and handles the data.

```
TABLE XXV. LEVEL 2 INPUTS, OUTPUTS, AND FUNCTIONALITY OF MICROCONTROLLER
Module Arduino Nano R 3
Input Digital sensor data from the garden section.
Power
Output Processed data from digital sensors.
Functionality Handle the data and send the data to the microcomputer.
```
Next, the level 2 block diagram is shown below in Fig. 26 ; it displays the microcomputer. The
microcomputer we are using is the Raspberry Pi model 4; it will act as the brain of the entire
device, and every input will go through the Raspberry Pi; it will process schedules data and track
the health of the plants, which is the most crucial part. The essential parts that our system will use
from the Raspberry Pi are the SoC, which is the Broadcom BCM2711, Quad-core Cortex-A72, the
built-in Wi-Fi antenna to transmit the data to the server, the 40 GPIO header where the sensors
and systems will connect to work together, it also has the power connection to power the entire
device. The outputs will go to the user app as the plant data and the irrigation and lighting system
in case they need to be triggered. Also, it will manage input from the user app.


Fig 27. Level 2 view of the microcomputer (Raspberry Pi 4 model B)
Table XXVI below explains the input, outputs, and functionality of the Raspberry Pi. It is a
more in-depth view of how it works. It is the brain of all the operations and explains how
everything works.

```
TABLE XXVI. LEVEL 2 INPUTS, OUTPUTS, AND FUNCTIONALITY OF THE MICROCOMPUTER
Digital Sensors 40 GPIO HEADER SoC Wi-Fi Antenna SX1262
LoRaWAN
Input Data from digital
sensors.
```
```
Data from the 40
GPIO headers.
```
```
Wi-Fi transmitted
data.
```
```
Control pins.
```
```
Power Power. Power Power
```
```
Output Plant health
measurements
processing.
```
```
Plant health
measurements are
transmitted to the
server.
```
```
User app. LoRaWAN
connection.
```
```
Functionality Connect digital
sensors along with the
irrigation system and
lighting system.
```
```
Process the
information fast and
dependable.
```
```
Communicate the
Raspberry Pi with
the server to track
data.
```
```
Provide
LoRaWan
connectivity
to the system.
```
The microcomputer is arguably the most essential part of the device because it will connect
everything and make it work as an ecosystem. The SX1262 LoRaWAN module goes on top of the
header, acting as a HAT for the Raspberry Pi; this provides LoRaWAN server connectivity. The
headers and the irrigation and lighting system will receive the data. It will process and transmit the


information, output the data into the user application, and process all input, even from the user.
Also, it will handle feedback and send it to the user application for better plant care.

Next is the irrigation system block diagram; it is straightforward since it only handles one
function: watering the plants at designated times. It will have a water reservoir with nutrients and
a water pump to provide powerful irrigation in the garden. Also, a tubing system with pipes will
work as the water distribution system. Fig. 27 below is the graphic representation of the irrigation
system.

Fig 28. Level 2 view of the irrigation system.
Table XXVIII below explains the Irrigation system's input, outputs, and functionality. First, we
fill the water reservoir with water and nutrients; the microcomputer input triggers a water pump,
either scheduling irrigation or low measurements in plants; then, the water flows through the water
distribution system, which consists of tubes to spray the plants.

```
TABLE XXVII. LEVEL 2 INPUTS, OUTPUTS, AND FUNCTIONALITY OF THE IRRIGATION SYSTEM
Irrigation
system
```
```
Water Reservoir Water Pump Water
Distribution
```
```
Water Level
Sensor
Input Water flows from the
water pump.
```
```
Power Water from the
water reservoir.
```
```
Power
```
```
Microcomputer Input. Microcomputer
Input.
Output Water flows into the
tube for distribution.
```
```
Water flows from the
reservoir for
distribution.
```
```
Irrigation process. Water in the
reservoir true or
false.
Functionality Hold water with
nutrients.
```
```
Pump water into
distribution tubes.
```
```
Spray water into
plants.
```
```
Determine if there is
water left on the
reservoir.
```

The level 2 diagram is the lighting system; this system is simple since it only serves one
function: providing light to the plants when needed or if the microcomputer triggers it. This system
receives power and microcomputer input to turn the lights on or off. Fig. 28 below shows how the
lights module works.

Fig 29. Level 2 view of the lighting system
The lighting system is very straightforward; it is a set of lights powered and turned on or off
with the microcomputer input, either by low measurement or a schedule set by the user, which the
microcomputer handles. Table XXIX below explains the inputs, outputs, and functionality.

```
TABLE XXVIII. LEVEL 2 INPUTS, OUTPUTS, AND FUNCTIONALITY OF THE LIGHTING SYSTEM
Lighting system Lights
Input The signal that turns the lights on or off.
```
```
Output Lights on or off on plants.
Functionality Provide light to the garden section.
```
Finally, the last level 2 diagram is the LoRaWAN module; this system is simple since it only
serves one function: transmit the data from the sensors to the microcontroller and server, we are
using an esp8266 for this and it works great, it has gpio pins for use to connect the sensors and
also has an embedded Wi-Fi antenna and module which helps data transmission.


Table XXVIII below explains the LoRaWAN module, it plugs to the sensors and trasmits the
data over to our server.

```
Module ESP8266
Input Digital sensor data from the garden section.
Power
Output Send data over to our server.
Functionality Handle the data and send the data to our server for the user to see it.
```
The main function that changed from our initial proposal to our final report was the addition of
the LoRaWAN module, we initially intended to use the sx1262 alone that works with the
Raspberry Pi. We discovered while working on the project that we needed a way to send the data
over from the sensors to the microcomputer, and the esp8266 works great for what we need. We
also added a water level sensor for functionality purposes, it does not affect any other piece of
hardware. We decided to add the sensor since it will let the user know to refill the water in the
reservoir so the systems can keep running.

## Table 27 Level 2 Inputs, Outputs, And Functionality Of The Microcomputer ............................................

shows how they correlate and work together to keep the plants healthy and stable.

```
TABLE XXIX. LEVEL 2 INPUTS, OUTPUTS, AND FUNCTIONALITY OF THE LIGHTING SYSTEM
Module Digital
Sensors
```
```
Micro-
computer
```
```
Lighting
System
```
```
Irrigation
System
```
```
Micro-
controller
```
```
LoRaWAN
Module
Input Power Power Power Power Power Power.
Plant health
data from
plant soil.
```
```
Plant
measurements
from digital
sensors.
```
```
Data from
microcomputer
(plant
measurements)
```
```
Data from
microcomputer
(plant
measurements)
```
```
Data from
digital sensors
regarding plant
```
```
Digital sensors
readings.
```

```
Plant vital
data from the
environment.
```
```
The user input
includes
lighting and
irrigation
schedules.
```
```
Light
schedules from
microcomputer
(user input).
```
```
Irrigation
schedules from
microcomputer
(user input).
```
```
health and
environment.
```
```
Output Plant health
measurement
s.
```
```
Plant
measurements
into the user
app.
```
```
Lights are
either on or off
in the garden
section.
```
```
Water flows in
the garden
section, ending
in water being
sprayed on
plants to keep
them healthy.
```
```
Plant data
processed.
```
```
Transmit the
data using
LoRaWAN
protocols.
Trigger
irrigation
system if
necessary.
Handle
feedback.
Trigger lighting
system if
necessary.
Functionali
ty
```
```
Measure
plant vital
data in soil
and
environment
and send
data to
Raspberry Pi
for
processing.
```
```
Manage data
from sensors
and input from
the user app.
Handle all input
and trigger
required
systems.
Control water
pump to
regulate water
flow. Control
Lights.
```
```
Light up the
plants to keep
them healthy
without
sunlight.
```
```
Provide water
and nutrients
to the plants on
set schedules
or when
required.
```
```
Handle data
and send it to
the
microcomputer
for further
tracking.
```
```
Ease the
process of
transmitting
data to our
server.
```
Fig. 2 9 is a flowchart of how we intend the system to work; this flowchart enables us to see
what interconnections are going on and what can be triggered by what in the entire system.


Fig 30. Flowchart of how PlantPulse works
The first step is to read the data from the soil and environment; the sensors take care of reading
that data, which then sends that data to the Arduino Nano r3, which transmits the data to the
Raspberry Pi; the Raspberry Pi processes the data, determines whether a measurement is low, and
triggers the required system to fix that measurement. Also, it handles user input for scheduling the
irrigation and lighting system. Once we send the data to the user app, it goes back to reading more
since plants' vitals can change over time, so it is essential to keep reading to detect anomalies.

### C. Specifications

PlantPulse will track plant health data and trigger systems to keep the plants healthy. It will also
output that data into the user app. The following Table XXX shows every component that will go
into making PlantPulse. While working on the project we decided to change the grow lghts for
regular LED lights, also we added the esp8266 which works as our LoRaWAN module. Finally,
we decied to add a water level sensor so we can the ability to notify the user if there is water on
the container, this also helps the system runs smoothly because the user now knows when to refill
the water.


```
TABLE XXX. MODULE SPECIFICATIONS FOR PLANTPULSE.
Component Specifications
Raspberry Pi 4 B
model B
```
```
Broadcom BCM2711, Quad-core Cortex-A72, 4GB RAM, 5V DC via USB-C connector, 5V
DC via GPIO header, Raspberry Pi standard 40-pin GPIO header, built-in Wi-Fi antenna, built-
in relay for power.
DHT22 Digital Temperature and Humidity Sensor Module Temperature, temperature range: -40 to 80
degrees Celsius, accuracy of +/- 0.5 C, humidity measuring range: 0~100%RH, humidity
measurement accuracy: ±2%RH.
Grow Lights 80 LED Lamps with Full Spectrum & Red Blue Spectrum, 3/9/12H timer, ten dimmable levels,
adjustable gooseneck, three switch modes, 5 Volts, 5.63 "L x 3.82 "W x 13.86 "H.
WayinTop Water
Pump
```
```
DC Voltage: 3-5 V, outside diameter of water outlet: 0.29"/7.5mm, inside diameter of water
outlet: 0.17"/4.5mm, water inlet diameter: 0.19"/5mm, continuous working life of 300 hours
NPKTHC-S
Sensor
```
```
0 - 5V measures soil moisture temperature, humidity, nitrogen, phosphorus, potassium,
temperature, and pH levels.
Arduino Nano r3 ATmega328, Pins for programming, 5V.
ESP8266 ESP8266 Wi-Fi Module, a compact, powerful microcontroller designed for IoT applications.
Featuring a 2.4 GHz Wi-Fi capability, it supports multiple networking protocols for efficient
and reliable communication.
Inland WS8218B
Individually Addressable LED Strip 3 Meter 60 LED Per Meter.
```
```
CQRobot water
level sensor
```
```
The CQRobot non-contact liquid level sensor realizes non-contact detection of the liquid level
in a closed container. 5 V
Programming
Language
```
```
Python and Java.
```
### D. Other Deliverables

We must keep working to achieve our end product successfully, and with that comes the
responsibility of submitting the required deliverables; we will keep working professionally and on
time to achieve those. We also plan on working with the feedback given to improve areas where
we may need more performance. Some of the deliverables for our project include:

- Final Proposal.
- Video presentations.
- Final device.
- PowerPoint presentations.
- Final report.
By going from level 0 to level 2, we could show how each module of our system is being put
together, from the most basic to the more complex modules; this can help us in the future to
troubleshoot possible problems. Also, it allows the users to understand how we put together the
device. All the tables and diagrams make it much easier to understand this complex device, and
hopefully, it helps any reader to know how we built the device. Finally, we also mentioned our
future deliverables, and we hope to achieve those in time and professionally.


## XIX. PLAN OF ACTION

Our project plan served as a cornerstone for effectively managing and delivering our initiative.
By outlining a clear timeline, assigning responsibilities, and breaking down larger tasks into
manageable components, we ensured steady progress and balanced workloads across the team.


This structured approach allowed us to identify areas where team members excelled and where
additional support was needed, fostering collaboration and optimizing efficiency.

The plan detailed each task, its timeline, and the responsible individuals, creating a well-defined
roadmap that prevented overwhelm and maintained focus. The phased approach facilitated the
systematic execution of our complex project, enhancing our ability to achieve milestones
methodically and deliver results successfully.

### A. Statement of Work (SOW)

The statement of work provides a clear and concise overview of the key managerial aspects
crucial for the PlantPulse project. It defines the project’s scope, location, completion timeline, and
a summary of personnel involvement. Additionally, it outlines the specific responsibilities of each
team member during the design, implementation, and testing phases. This document has been
instrumental in setting clear expectations and guiding the project’s successful progression.
Furthermore, the inclusion of equipment cost estimates has enabled efficient budget management
and resource allocation, ensuring the project remained financially on track.

- Microcontroller System: $150 - Includes components such as the ELEGOO Nano Board,
    Raspberry Pi 4B, and communication modules like the RS-485 Transceiver.
- Sensors: $200 - Covers soil moisture sensors, pH sensors, temperature, and light sensors
    (e.g., DHT22/AM2302, LM393 Soil Detector).
- Networking Equipment: $50 - Includes LoRaWAN modules like the SX1262 HAT RF
    Chip to ensure reliable long-distance communication.
- Enclosure Materials: $75 - Includes the MELONFARM Grow Tent and other durable,
    weather-resistant materials for housing hardware components.
- Miscellaneous Supplies: $25 - Wires, screws, Breadboard Kit with Power Supply, and
    other minor components.
1) Scope
The completed PlantPulse project seamlessly integrates hardware and software to provide a
robust garden monitoring system. Its hardware component includes sensors that measure essential
environmental conditions such as soil moisture, pH, temperature, and light, which are connected
to a microcontroller for efficient data processing. The system also features solar panels for
sustainable power. The software includes a custom dashboard that collects and visualizes real-time
data, offering actionable insights. LoRaWAN technology ensures reliable communication and
extensive network coverage, making it scalable for gardens of all sizes.

```
2) Location
```
The project was developed at the Engineering Campus of Florida International University. This
centralized location facilitated collaboration among team members, enhancing communication and
ensuring timely completion of milestones.

```
3) Period
```
The project spanned two semesters, beginning in Senior Design I during Summer 2024 and
concluding in Senior Design II in Fall 2024. The final functional prototype was successfully
delivered on time, meeting all outlined objectives.

```
4) Deliverable Schedule
```

The project’s deliverables were meticulously tracked to ensure consistent progress. The
following schedule reflects all deliverables, including those added during the final phase:

- June 18, 2024: Proposal Part 1
- June 20, 2024: Presentation 1
- June 25, 2024: 1-Minute Storyboard and 1-Minute Video
- July 18, 2024: Proposal Part 2
- July 23, 2024: Presentation 2
- July 25, 2024: Final Proposal and Project Demonstration
- September 27, 2024: Written Report 1
- October 25, 2024: Written Report 2
- November 22, 2024: Written Report 3
- December 2, 2024: Final Report, Poster, and Final Presentation
- December 5, 2024: Virtual Showcase

### B. Work Breakdown Structure (WBS)

The Work Breakdown Structure (WBS) was an essential part of managing and completing the
PlantPulse project, allowing us to divide the work into phases and track progress effectively.
Below is a detailed comparison of the proposed WBS and the completed WBS, alongside team
responsibilities. Fig. 30 shows the breakdown of all the work that must be done for the product.


```
Fig 31. Work Breakdown Structure
1) Proposed Phases
```
We will organize our PlantPulse project into six critical phases, each tailored to develop a
comprehensive intelligent garden system. These phases include Conceptual Design, Sensor and
Circuit Configuration, Software Design, Microcontroller Setup, Enclosure Development, and
Prototype Testing. We have designed each stage with specific tasks and objectives that
systematically guide our project toward completing the final product.

a) Phase 1 - Conceptual Design
Objective: This phase focuses on preliminary preparations, including research, materials
procurement, and budget planning for developing our intelligent garden system, PlantPulse. It aims


to streamline all preparatory tasks like paperwork and funding to clear the way for product
development.

Approach: We will start by finalizing the proposal and completing all required documentation.
At the same time, we will procure all necessary materials for building PlantPulse. Additionally,
we will begin efforts to secure funding through a planned fundraiser during this phase.

Expected Results: By the end of this phase, we will have completed the proposal, secured all
required materials, and launched a fundraiser. These foundational steps set the stage for the
subsequent design and development phases.

Timeline: This phase runs from June 10 , 2024, to August 14, 2024. During this period, we will
also order needed parts, refine our design, and perform initial theoretical evaluations to anticipate
and address potential design challenges.

b) Phase 2 - Sensor and Circuit Configuration
Objective: This phase focuses on creating a practical circuit diagram that links all hardware
components of our intelligent garden system. The diagram will incorporate detailed calculations
for effective real-world implementation.

Approach: The team will initially draft the circuit diagram on paper, discussing and refining
ideas to optimize the layout. We will simulate the circuit to verify that its performance meets
expectations before physically assembling the hardware and making all necessary connections.

Expected Results: The outcome will be a fully operational circuit that efficiently and effectively
connects all electrical components of the system. It will ensure that each element receives the
correct power levels.

Timeline: The Sensor and Circuit Configuration phase is scheduled from August 15, 2024, to
September 1, 2024. This phase involves configuring and powering the sensors, requiring a detailed
examination and implementation of the power supply.

c) Phase 3 - Software Design
Objective: This phase aims to design and develop the software components necessary to operate
the innovative garden system PlantPulse. It creates an app that will control the environment and
the algorithms to process sensor data and control the system based on environmental feedback.

Approach: The team will use a combination of programming languages and development
environments to craft the software. We will perform the initial coding in a controlled environment
to ensure functionality. Adjustments will be made based on test results to refine the software's
efficiency and reliability.

Expected Results: By the end of this phase, we aim to have robust software that can reliably
gather data, analyze it, and make decisions that influence the operation of the garden system
effectively.

```
Timeline: The Software Design phase is planned from September 2, 2024, to September 29 ,
```
2024. This stage will involve iterative development and testing to ensure the software meets all
necessary specifications for managing the innovative garden system.

```
d) Phase 4 - Microcontroller Setup
```

Objective: To integrate and configure the microcontroller that serves as the central processing
unit for the PlantPulse system, managing input from sensors and controlling outputs based on
software commands.

Approach: The team will install the chosen microcontroller, program it with the developed
software, and establish connections with all relevant system components. Functional tests will
ensure that the microcontroller accurately processes sensor data and executes control actions.

Expected Results: A fully operational microcontroller efficiently coordinating the garden
system's functionalities.

Timeline: Scheduled from September 30, 2024, to October 14, 2024, this phase is critical for
ensuring that all electronic components function harmoniously.

e) Phase 5 - Enclosure Development
Objective: To design and construct a durable, weather-resistant enclosure that houses and
protects the PlantPulse system's electronic components.

Approach: Design considerations will include material selection for durability and aesthetics,
component layout for operational efficiency, and accessibility for maintenance. Prototyping and
testing of the enclosure will follow the design phase.

Expected Results: An enclosure that protects components from environmental elements and
supports the system's functional requirements.

Timeline: This phase runs from October 15, 2024, to November 4, 2024, focusing on the
physical integration of the system into a single, manageable unit.

f) Phase 6 - Prototype Testing
Objective: To comprehensively test the PlantPulse prototype to validate its functionality,
durability, and user interface.

Approach: The prototype will undergo rigorous testing under various environmental conditions
to simulate real-world use. Feedback from these tests will guide final adjustments before the
product launch.

Expected Results: Confirmation that the prototype meets all specified performance criteria and
is ready for full-scale production.

Timeline: Set from November 5, 2024, to December 2 , 2024, this final phase ensures the
system's readiness for deployment and user adoption.

```
2) Completed Phases
```
```
a) Phase 1 - Conceptual Design
```
- Objective: To establish the foundation of the PlantPulse project by defining its scope,
    conducting research, sourcing materials, and creating a comprehensive project plan.
- Completed Activities:
    o Conducted thorough research on existing smart gardening systems to identify
       gaps and opportunities.


```
o Finalized the project proposal and ensured all documentation, including technical
specifications, was completed.
o Sourced materials from multiple suppliers to ensure cost-effectiveness and
quality.
o Launched a fundraiser to secure additional funding, successfully meeting the
financial needs for the project.
```
- Outcome: The proposal was approved, all materials were procured, and a clear roadmap
    for the project was established. The team was aligned and ready to transition into the
    next phase with a shared understanding of goals and expectations.

b) Phase 2 - Sensor and Circuit Configuration

- Objective: To design and implement the electrical components required for PlantPulse,
    ensuring the sensors and circuits work seamlessly.
- Completed Activities:
    o Created an initial circuit diagram on paper, iterating through multiple designs to
       optimize power distribution and connectivity.
    o Simulated the circuit virtually to identify and resolve potential issues before
       physical assembly.
    o Assembled and tested all sensors, including soil moisture, pH, light, temperature,
       and humidity sensors, ensuring compatibility with the microcontroller.
    o Addressed challenges with sensor power requirements by adding voltage
       regulators and reconfiguring connections.
- Outcome: Delivered a functional circuit that effectively integrates all sensors and
    ensures reliable power distribution. Minor adjustments extended the timeline slightly,
    but the team overcame these challenges without impacting subsequent phases.

c) Phase 3 - Software Design

- Objective: To develop a software application capable of processing sensor data,
    analyzing environmental conditions, and managing the system autonomously.
- Completed Activities:
    o Developed a mobile app with a user-friendly interface for monitoring and
       controlling the system.
    o Designed algorithms for analyzing real-time sensor data and providing actionable
       insights to users.
    o Implemented a machine learning model to predict plant needs based on
       environmental conditions.
    o Conducted extensive testing to ensure the app communicates effectively with the
       microcontroller and hardware components.
    o Incorporated user feedback from prototype testing into app refinements.
- Outcome: Delivered a robust app capable of collecting, analyzing, and visualizing data
    while allowing users to control the system remotely. The app is a central feature of
    PlantPulse, demonstrating its practicality and ease of use.


d) Phase 4 - Microcontroller Setup

- Objective: To configure and integrate the microcontroller as the central processing unit
    of PlantPulse, ensuring seamless communication between software and hardware.
- Completed Activities:
    o Selected and programmed the microcontroller with the developed software.
    o Established connections between the microcontroller and all sensors, ensuring
       compatibility and reliable data transmission.
    o Conducted tests to verify the microcontroller’s ability to process sensor data and
       execute commands efficiently.
    o Resolved issues related to communication delays and implemented error-
       checking protocols.
- Outcome: The microcontroller functioned as intended, processing inputs and outputs
    accurately. The system demonstrated real-time responsiveness, a critical requirement for
    PlantPulse's functionality.

e) Phase 5 - Enclosure Development

- Objective: To create a durable and weather-resistant enclosure for housing PlantPulse's
    components, ensuring long-term reliability in various environments.
- Completed Activities:
    o Procured weather-resistant materials and tested them for suitability under
       extreme environmental conditions.
    o Assembled the enclosure and integrated all components, including sensors,
       microcontroller, and power supply.
    o Conducted physical tests to ensure the enclosure could withstand moisture, dust,
       and temperature variations.
- Outcome: Delivered a fully functional enclosure that protects the system from
    environmental factors while maintaining a sleek and professional appearance. The
    enclosure also supports ease of maintenance and component upgrades.

f) Phase 6 - Prototype Testing

- Objective: To evaluate the PlantPulse system comprehensively, ensuring it meets
    performance, durability, and user-interface requirements.
- Completed Activities:
    o Conducted extensive functional tests to validate the accuracy of sensor readings
       and system responses under real-world conditions.
    o Simulated various environmental scenarios, such as drought and overwatering,
       to test the system’s adaptability.
    o Collected user feedback from testing sessions to refine both hardware and
       software.
    o Addressed minor issues, including sensor calibration and app display glitches, to
       improve overall performance.


```
o Presented the working prototype to stakeholders, demonstrating its features and
capabilities.
```
- Outcome: The prototype met all performance criteria, showcasing PlantPulse’s potential
    as a reliable and user-friendly smart gardening system. It was deemed ready for
    deployment and user adoption, with minor refinements incorporated before the final
    showcase.

The completion of each phase demonstrated the team’s ability to adapt and overcome
challenges while adhering to the overall timeline. By breaking down the project into manageable
phases, the team ensured consistent progress and maintained a high standard of quality throughout
the development process. The system was delivered on time, within budget, and met all initial
objectives, highlighting the effectiveness of the WBS as a project management tool.

```
3) Team Member Responsabilities
```
```
a) Carlos Gutierrez - Software Engineer
```
- Led the development of PlantPulse’s app.
- Integrated sensor feedback with the machine learning algorithms.
- Ensured that the software functioned seamlessly with the hardware.

```
b) Pedro Ojeda - Hardware Engineer
```
- Designed and implemented the system’s circuit diagrams.
- Configured sensors and managed their connections to the microcontroller.
- Performed rigorous hardware testing to ensure reliability.

```
c) Richard Cui - System Integration Specialist
```
- Programmed the microcontroller and integrated it with the app.
- Coordinated hardware-software connections.
- Conducted system-wide testing for proper functionality.

```
d) Jonathan Fleurisma - Enclosure Specialist
```
- Designed and constructed a weather-resistant enclosure for the system.
- Selected appropriate materials to ensure durability and protection.
- Managed the physical assembly of the PlantPulse system.

```
e) Abigail Sardine-Laforte - Project Manager
```
- Managed schedules, deliverables, and team coordination.
- Supervised documentation and ensured milestones were met.
- Oversaw the final presentation and project demonstrations.


### C. Project Milestones

In the PlantPulse project, milestones played a crucial role in tracking progress and providing
the team with a sense of accomplishment as each key stage was completed. Below is an analysis
of the milestones identified during the project planning phase and an assessment of whether they
were met.

```
a) Finalization of the Project Proposal
```
The project proposal was finalized successfully, detailing the objectives, scope, and timeline of
the project. The proposal served as a foundational document, guiding the team and ensuring
alignment among all stakeholders.

```
b) Completion of Circuit Design
```
The circuit design was completed after extensive iterations. Although some unexpected
compatibility issues arose between sensors and the power supply, the team resolved them by
refining the design and recalibrating the sensors.

```
c) Successful Integration of the Software
```
The software was developed and integrated successfully, meeting the functional requirements.
User feedback during the testing phase prompted a few iterations to refine the user interface and
improve system performance.

```
d) Configuration of the Microcontroller
```
The microcontroller was installed and configured to process sensor data and execute system
commands effectively. Early challenges with communication protocols were identified and
resolved, ensuring seamless operations.

```
e) Development of Protective Enclosure
```
A durable, weather-resistant enclosure was developed using CAD designs and high-quality
materials. The enclosure successfully passed tests for environmental stressors, including moisture
and dust resistance.

```
f) Final Assembly and Testing
```
The final assembly was completed, and the system underwent comprehensive testing. Minor
refinements in both hardware and software were made based on testing feedback to enhance
functionality and user experience.


Yes, all milestones were met. While some minor delays occurred, such as resolving sensor
compatibility issues and incorporating user feedback into software adjustments, these were
handled effectively without impacting the overall project timeline. The team’s adaptability ensured
that all milestones were achieved, leading to a successful completion of the PlantPulse project.

### D. Gantt Charts

Fig. 30 and Fig. 31 showcases the Gantt Chart for our PlantPulse project. This chart is
instrumental in clarifying deadlines, showing dependencies between project phases, and mapping
out the timeline for tasks. Our PlantPulse project strictly adhered to the GANTT chart established
during the planning phase. The GANTT chart was instrumental in clarifying deadlines, showcasing
dependencies between project phases, and mapping out the timeline for all tasks. Throughout the
project, the team remained on course, ensuring that all tasks were completed within the defined
timelines. Each milestone was achieved as scheduled, and no deviations from the proposed
timeline occurred. This strict adherence to the GANTT chart underscores the efficiency of our
planning and the commitment of the team to the project schedule.

```
Fig 32. Gantt Chart Part 1
```

```
Fig 33. Gantt Chart Part 2
```
E. PERT Chart

Fig. 32 presents the PERT Chart for our PlantPulse project. This chart plays a crucial role in
our PlantPulse project as it clearly displays how each task contributes toward achieving the final
goal. It organizes tasks sequentially, highlighting dependencies and allowing us to see the progress
path. This visual representation helps the team prioritize tasks, allocate resources efficiently, and
identify potential delays or bottlenecks, ensuring the project remains on schedule.


Fig 34. Pert Chart
In conclusion, the structured action plan played a pivotal role in the success of our PlantPulse
project. It ensured that every team member clearly understood their responsibilities and deadlines,
fostering seamless collaboration and accountability. The GANTT chart served as an invaluable
tool, providing a visual and actionable roadmap that guided the team through each phase of the
project, ensuring timely and efficient completion. By strictly adhering to the planned timeline and
leveraging the structured framework, we achieved all our goals and successfully delivered a
functional and innovative PlantPulse system.


## XX. MULTIDISCIPLINARY ASPECTS

The PlantPulse project's success relies heavily on our interdisciplinary team's diverse expertise.
Our team members excel in various fields, ensuring this project covers all aspects
comprehensively. This diversity is a strategic choice necessary for the project's future. While being
able to integrate complexity by integrating technology with gardening and environmental
sustainability, the innate value of each team member's skill set is essential. Understanding the value
each discipline brings to the table is crucial for creating an innovative and practical product.

### A. Team Contract

Our team comprises AI engineers, computer engineers, and computer scientists, each bringing
unique skills and perspectives. This diverse expertise allows us to tackle the complex challenges
of modern gardening with a comprehensive and integrated approach. Our AI engineers develop
sophisticated algorithms that enable our system to learn and adapt, providing precise control over
various gardening parameters. Computer engineers ensure our hardware components are robust
and reliable, seamlessly integrating sensors and controllers to create a cohesive system.
Meanwhile, our computer scientists work tirelessly on the software infrastructure, ensuring a
smooth and intuitive user experience. This collaboration not only enhances the functionality and
efficiency of our product but also exemplifies the strength of multidisciplinary Teamwork, driving
our mission to revolutionize home gardening.

As AI engineers, we are developing the intelligent algorithms that form the heart of PlantPulse.
Our work involves designing machine learning models to optimize various gardening parameters
such as irrigation, lighting, and climate control. We train these models to make accurate predictions
and decisions by analyzing sensor data, ensuring optimal plant health. We also integrate AI
capabilities like voice recognition and predictive analytics, enhancing the user experience by
enabling seamless interaction with the system. We aim to create an intelligent, adaptive system
that learns and evolves with the garden.

Our computer engineers focus on designing and developing the hardware components that
support PlantPulse's advanced features. We work on creating and optimizing circuit boards,
integrating sensors, and ensuring the overall hardware architecture effectively supports the AI
algorithms. We guarantee that components like cameras, humidity sensors, and irrigation
controllers function reliably and efficiently. We also address power management issues and work
on improving the durability and scalability of our hardware to cater to different gardening
environments. Our role is to ensure that the physical components are robust and can handle the
demands of modern gardening.

As computer scientists, we develop the software infrastructure that ties everything together. We
write the code for the user interface, making it intuitive and easy to use. Our work on the backend
involves developing algorithms that enable communication between the hardware components and
cloud-based services. We integrate various technologies, such as mobile applications and web
platforms, allowing users to monitor and control their gardens remotely. Additionally, we ensure
data security and continuously update the system to enhance its capabilities. We focus on providing
a seamless and secure user experience that allows users to manage their gardens effortlessly.

Together, we bring advanced analytical and predictive capabilities to the PlantPulse system,
ensuring that our gardening control features are intelligent and adaptive. We guarantee these
features are supported by robust and reliable hardware, and we integrate the entire system to
provide a seamless user experience. This multidisciplinary approach allows us to create a state-of-


the-art solution that meets the diverse needs of modern gardeners, demonstrating the power of
Teamwork and diverse expertise.

```
1) Abigail
```
- A coding prodigy with exceptional troubleshooting skills, her extensive experience in
    software development, honed through multiple internships, allows her to navigate and
    solve complex coding issues efficiently. She brings a wealth of knowledge in project
    creation, ensuring our software is innovative and reliable. Her meticulous attention to
    detail and problem-solving abilities makes her an invaluable asset, particularly when
    facing technical challenges. Abigail's coding expertise perfectly complements our
    engineers' hardware skills, seamlessly bridging the gap between software and hardware.
2) Pedro
- Go to an expert for anything related to electronics and circuits. His deep understanding
of the plant industry gives him a unique edge, enabling him to design electronic systems
that cater specifically to the needs of modern gardening. Pedro's ability to blend his
knowledge of electronics with his passion for plants allows us to create systems that are
not only technologically advanced but also highly relevant to our target market. His
insights into plant care and technology ensure that our solutions are practical and user-
friendly, enhancing the overall user experience. Pedro is also the group's leader.
3) Richard
- With dual expertise in the plant industry and programming, his comprehensive
understanding of plant biology and needs and his programming skills allow him to
develop finely tuned algorithms to optimize plant growth. Richard's ability to bridge the
gap between technology and horticulture ensures that our AI-driven system is intelligent
and botanically accurate. His contributions are vital in ensuring our system delivers real,
tangible benefits to gardeners.
4) Carlos
- Specializing in building models from complex data sets, Carlos has deep experience in
artificial intelligence, which allows us to leverage machine learning to create an
ingenious gardening system. Carlos's ability to analyze and interpret large amounts of
data ensures that our AI can make accurate predictions and adjustments, optimizing
plant care on a granular level. His work makes our system adaptive and intelligent,
capable of learning and improving over time.

```
5) Jonathan
```
- We have an embedded systems enthusiast with a certification in machine learning and
    a passion for building robust systems. His expertise ensures that our hardware is reliable
    and performs consistently under various conditions. Jonathan's skills in embedded
    systems are complemented by his knowledge of machine learning, allowing us to
    integrate advanced AI capabilities directly into our hardware. His contributions ensure
    that our system is robust and durable, capable of handling the demands of modern
    gardening.
- At the beginning of this semester, we elected Pedro to take a leadership role. Not only
    is he qualified, but he also has previous similar experience. However, Pedro's projects
    balance his schedule and manage as a team. As a team, we complete each assignment at


```
least two weeks before the due date, speak with our mentor at least once a week, and
have weekly meetings. This has allowed us to stay on top of each activity and protocol
as a team and account for delays that might come, such as family emergencies. We will
continue to communicate highly over the break, whether to expand on the project or
improve the measures initially provided.
```
## XXI. PERSONNEL

The team’s multidisciplinary characteristics, experience in other projects, and work experience
are presented in this chapter as a concise and visual resume.

A. Abigail Sardine-Laforte

```
ABIGAIL SARDINE-LAFORTE
```

```
Miami, FL | 347- 869 - 4265 | abigailsardine@gmail.com
EDUCATION
Florida International University, Miami, FL
```
```
Bachelor of Science in Computer Engineering, Expected Fall 2024
```
- Dean’s List: 2021 & 2023 | GPA: 3.2/4.0
TECHNICAL SKILLS
- Hardware: Oscilloscope, Raspberry Pi Arduino Nano r3, SPICE, Multisim, PCIe, PCB
design (OrCAD)
- Software: MongoDB, Big Data, Hadoop, Microsoft Office, Anaconda, Spark, Jupyter
Notebook, PowerShell, TensorFlow, AWS, Python, HTML, CSS, AngularJS, code blocks,
Power BI, Agility
WORK EXPERIENCE
Front-end & Back-end Developer Intern, FedEx | Remote | June 2024 – Aug 2024
- Integrated RESTful APIs, leveraged Visual Studio, and managed SQL databases.
Cloud Security Engineer Intern, Centene | Remote | May 2023 – Aug 2023
- Applied security policies, performed IT system analysis, and designed ServiceNow
dashboards.
Cloud Support Engineer Intern, Amazon Web Services | Remote | May 2022 – Aug 2022
- Created EC2 instances, troubleshooted network issues, and customized IAM roles.
RESEARCH & PROJECTS
- Inductive Power Transfer Intern, EPSI Research Lab | May 2023 – May 2023
Designed 3D electromagnetic battery model for EVs using Ansys software.
- Temperature & Humidity Sensor Project, Arduino, C programming, Losant IoT | Nov
2023
Developed MQTT system, achieved 97% reading accuracy.
CERTIFICATIONS
- Excel: Advanced Formulas and Functions (Centene Uni)
- Agile Project Management (Centene Uni)
- IBM Accelerate - Hardware Engineering 2023 (IBM)
- Azure Data Fundamentals (Microsoft)

B. Richard Cui

```
RICHARD CUI
Miami, FL | (305) 469-5545 | rcui305@gmail.com
EDUCATION
```
```
Florida International University, Miami, FL
Bachelor of Science in Computer Engineering, Expected Fall 2024
```

- Cumulative GPA: 3.32
Miami Dade College, Miami, FL
Associate of Arts in Computer Engineering, Winter 2022
- Cumulative GPA: 3.44
SKILLS
- Languages: English (Native), Chinese (Basic), Spanish (Basic)
- Technical: MATLAB, AutoCAD, Wolfram Mathematica, Losant IoT, Microsoft Office
- Programming: C, C++, Java, Python
PROFESSIONAL EXPERIENCE
Vintage Windows Corporation, Miami, FL

```
Administrative Assistant | Aug 2022 - Present
```
- Produced shop drawings, maintained digitized records, and executed data entry.
The Home Depot, Inc., Miami, FL

```
Merchandising Execution Associate | Sep 2019 - Mar 2021
```
- Organized SKUs, enforced visual standards, and provided customer service.
ACADEMIC PROJECTS
- Circuit Analysis Lab: Automatic Arduino-Based Watering System
- C++ Programming for Embedded Systems: Custom Notebook Application
CERTIFICATIONS
- Microsoft Azure AI Fundamentals

C. Carlos Alberto Gutierrez

```
CARLOS ALBERTO GUTIERREZ
Doral, FL | (786) 843-0854 | carlosgutierrez141201@gmail.com
```
```
EDUCATION
Florida International University, Miami, FL
Bachelor of Science in Computer Engineering, Dec 2024
```
- Cum Laude, GPA: 3.55 | 6-time Dean's List

```
EXPERIENCE
Chestnut Land Auntie Anne's, Doral, FL
Shift Leader | May 2023 - Present
```
- Supervised operations, managed inventory, and handled the POS system.
PROJECTS
- Netflix Big Data Analysis: Used Hadoop and PySpark for data analysis and
recommendation system.
- Concrete Compressive Strength Analysis: Developed regression models using Python.


#### SKILLS

- Programming: Python, Java, SQL, C, C++, VHDL
- Tools: Microsoft Excel, Power BI, Pandas, Hadoop

```
CERTIFICATIONS
```
- DP-900: Microsoft Azure Data Fundamentals
- AI-900: Microsoft Azure AI Fundamentals

```
LANGUAGES
```
- English: Full Professional Proficiency
- Spanish: Native Proficiency

D. Pedro Ojeda

```
PEDRO OJEDA
Miami, FL | 786- 438 - 9811 | PedroLOjeda12@gmail.com
EDUCATION
```
```
Florida International University, Miami, FL
Bachelor of Science in Computer Engineering, 2022- 2024
```
- GPA: 3.5

```
Miami Dade College, Miami, FL
Associate of Science in Computer Engineering, 2020- 2022
```
- GPA: 3.7
EXPERIENCE

```
BestBuy
Advisor and Warehouse Associate | Sep 2021 - Present
```
- Generated sales and managed online orders.

```
Publix
Stocker | May 2021 – Aug 2021
```
- Unloaded trucks and advised customers.
The Home Depot

```
Associate | Feb 2021 – May 2021
```
- Advised customers on flooring and organized department.
PROJECTS
- Raspberry PI Interactive Game: Developed game with Sense-Hat integration.
SKILLS
- Management, Problem-Solving, Leadership, Customer Service
- Microsoft Office, Fluent in Spanish
- Programming: Java, C, C++, Python


E. Jonathan Fleurisma

```
JONATHAN FLEURISMA
(954) 305-1013 | JonathanFleurisma@gmail.com
```
```
EDUCATION
Florida International University, Miami, FL
Bachelor of Science in Computer Engineering | Math Minor
```
```
Projected Graduation: May 2024
WORK EXPERIENCE
Technician/ Help Desk IT, AKG UHS Hardware | Oct 2023 - Present
```
- Provided technical support, installation, and maintenance of key-cutting machines.

```
Technician, Dave & Buster's | May 2023 - Oct 2023
```
- Troubleshooted issues with machines, games, servers, and internet systems.
Lead Technician, Yonutz | Jul 2021 - May 2023
- Managed POS upgrades, resolved connectivity issues, and handled opening/closing
procedures.
CERTIFICATIONS
- Microsoft Office 365
- AI 900 Fundamentals Microsoft

## XXII. BUDGET

PlantPulse is revolutionizing the way we approach gardening with its advanced AI-assisted
enclosure designed to increase the lifespan of plants while being nearly autonomous. As we aim
to enhance the functionality and efficiency of PlantPulse, we have carefully selected a range of
essential components to integrate into our system. Below, we provide a detailed breakdown of the
budget allocation for these components, which are crucial for optimizing the performance of
PlantPulse.

To achieve the seamless operation of PlantPulse, we have selected a variety of components that
are both cost-effective and highly functional. Each item was chosen for its specific role in
enhancing our system's capabilities, ensuring we stay within budget while maximizing efficiency.

```
TABLE XXXI. PARTS LIST COST FOR PLANTPULSE
```

The ELEGOO Nano Board, priced at $19.99, is a fundamental component of the Plant Pulse
system. Serving as the brain of the system, this microcontroller enables precise control and
automation of various tasks. Its cost-effectiveness and reliability make it an ideal choice for
managing Plant Pulse's operations.

To ensure reliable data transmission, the MAX485 Transceiver Chip Module is included for
$8.99. This module facilitates communication between the ELEGOO Nano board and the RS485
Soil Sensor, which is critical for accurate data collection and operation within Plant Pulse.

Lighting is vital for plant growth, particularly in low-light conditions. The LBW Full Spectrum
Grow Light Strip, priced at $23.19, ensures the proper light spectrum for healthy plant
development.

The KeyStudio 5v DC4A 4 Channel Relay Module, costing $8.99, controls multiple high-
power devices such as pumps, fans, and lights. This relay module ensures smooth operation and
efficient management of Plant Pulse's interconnected components.

Long-range communication and location tracking are achieved with the SX1262
LoRaWAN/GNSS HAT RF CHIP, priced at $32.63. This component is vital for outdoor
deployments, enabling Plant Pulse to operate effectively across various environments.

Central to the system's data processing and AI capabilities is the Raspberry Pi 4 Model B Quad-
core Cortex, priced at $61.75. This powerful processor handles all computations and system
operations, making it a cornerstone of the Plant Pulse system's intelligence.

The HiLetgo 3pcs ESP8266 NodeMCU CP2102, costing $16.39, facilitates wireless data
transmission of temperature and humidity readings from the tent enclosure. This ensures seamless
integration of environmental data into the system for real-time monitoring and adjustments.

The Breadboard Kit with Power Supply Module, priced at $8.99, is an essential platform for
prototyping and testing circuit designs. It ensures that electrical connections are correctly
established and functional during system development.


For precise environmental monitoring, the Comwintop RS485 Modbus 6-in-1 Soil Sensor,
priced at $49.37, provides critical measurements of soil moisture, temperature, and nutrient levels.
This sensor is indispensable for maintaining optimal growing conditions.

Supplementing soil monitoring is the HiLetgo LM393 Correlation Photoelectric Sensor, priced
at $14.99. Its additional soil moisture detection capabilities enhance system accuracy, ensuring
plants receive the proper hydration levels.

Humidity and temperature within the enclosure are monitored using the DHT22/AM2302
Temperature & Humidity Sensor, priced at $13.99. Maintaining a stable environment is crucial for
plant health, and this sensor ensures optimal conditions.

The WayinTop Automatic Irrigation Kit, priced at $13.99, automates the watering process,
delivering consistent hydration without manual intervention. This is key to the autonomous nature
of Plant Pulse, making gardening easier and more accessible for users.

The Mylar Hydroponic Grow Tent with Observation Window, priced at $59.99, provides a
controlled indoor environment for plants. This enclosure supports temperature regulation and
shields plants from external conditions, ensuring a stable and optimized growth environment.

For water storage, the PKS-150 BPA-Free Plastic 3-Quart Cereal Keeper, priced at $18.99,
acts as a reservoir within the irrigation system. Its durability and compatibility ensure consistent
water availability.

Lastly, the Zigbee Water Leak Detector, priced at $13.58, monitors water levels within the
irrigation system, alerting the system if the container needs refilling. This critical component
prevents interruptions in the automated watering process, ensuring uninterrupted plant care.

By integrating these carefully selected components, Plant Pulse combines advanced
technology with user-friendly features. Each item contributes to the overall functionality, creating
an intelligent gardening system capable of delivering healthy, thriving plants with minimal user
intervention. With this comprehensive and thoughtfully curated setup, Plant Pulse sets a new
benchmark in AI-assisted gardening innovation.

## XXIII. RESULTS EVALUATION

This section will discuss how we should evaluate our products before Senior Design II. The
evaluation process is critical since it provides feedback for our team to improve and keep working
on making our project possible. Our project will be evaluated in the following aspects:

```
1) Objectives
2) Constraints
3) Standard to comply
4) Patents not to infringe
5) Specifications
6) Deliverables
```

A. Technical Results

```
1) Objectives
```
The objectives set at the beginning of the project were focused on safety, ease of use,
modularity, scalability, and marketability. These objectives were meant to ensure that the
PlantPulse system would be secure, user-friendly, adaptable, and able to scale for a larger user
base, while also being viable for the market. The specifics of each objective included ensuring
the system was secure against cyber threats, reliable and easy to handle, simple to construct and
maintain, capable of supporting future hardware expansions, scalable for more sensors, and able
to provide real-time data with a companion application.

What was accomplished:

- Safety: The system was designed with security in mind, implementing basic
    cybersecurity measures to protect the user data. The physical components were chosen
    for their reliability and safety.
- Ease of Use: The system’s design emphasized simplicity in both construction and
    deconstruction.
- Modularity: The system was developed with the option for future hardware expansions,
    and wireless communication was integrated using LoRaWAN technology, making the
    system adaptable for various connection types.
- Scalability: The system’s range was enhanced through LoRaWAN, and provisions were
    made to allow the addition of more sensors in the future.
- Marketability: Real-time data tracking was implemented, along with notifications for
    optimal soil conditions. A companion application was partially developed to facilitate
    user interaction.

What was not accomplished and why:

- Safety (Cybersecurity): While basic security measures were implemented, further
    refinement in cybersecurity was limited by time and resource constraints.
- Ease of Use (Minimal Maintenance): The system's maintenance could still be
    improved, especially in terms of reducing complexity for troubleshooting or replacement
    of components.
- Modularity (Future Hardware Expansions): While we designed the system with
    expansion in mind, the actual physical hardware expansions were not fully implemented
    due to resource limitations.
- Marketability (Companion Application): The development of a fully functional
    companion app was postponed due to time constraints, and thus only a basic prototype
    was made available.

```
2) Constraints
```
The system needed to be competitive in price, measure values accurately, and be easy to
implement. The goal was to keep the cost lower than comparable products while ensuring the
system was affordable and accessible for users. Accuracy in measurement was prioritized, along
with ease of installation and use.


What was accomplished:

- Competitive Pricing: We ensured that the components selected were cost-effective,
    aiming to deliver a product at a competitive price point compared to similar products.
- Accurate Measurements: Sensors were selected for their reliability, and calibration was
    performed to ensure the data accuracy.
- Ease of Implementation: The system was designed to be easily deployed, with clear
    documentation provided for users and a straightforward setup process.

What was not accomplished and why:

- Pricing Competitiveness: Although the system was designed to be cost-effective, some
    components exceeded initial budget expectations, which might make the product less
    competitive compared to some low-cost solutions.
- Ease of Implementation (Advanced Features): Some advanced features, like full
    automation and seamless integration with other IoT devices, were not fully realized due
    to time and technical challenges in integrating third-party platforms.

```
3) Standard to comply
```
The system had to comply with various standards including health and safety regulations,
data security protocols, and manufacturer standards. The goal was to ensure a high-quality
product while maintaining transparency and effective communication with users.

What was accomplished:

- Health and Safety: The components selected complied with general safety standards,
    and the system was designed with the user’s safety in mind, especially in terms of
    electrical components.
- Data Security: Basic data security measures were put in place, including encryption for
    user data. However, further improvements could be made in this area.
- Manufacturer Standards: Components were sourced from reputable manufacturers to
    ensure quality, and assembly adhered to standard practices.

What was not accomplished and why:

- Advanced Data Security: While basic encryption was implemented, a more robust
    security framework (e.g., multi-factor authentication, secure cloud storage) was not fully
    developed due to time constraints.
- Manufacturing Compliance: Full compliance with international manufacturing
    standards (such as ISO certifications) was not fully achieved, as the project was still in
    the prototype stage and not yet ready for mass production.


```
4) Patents not to infringe
```
The team acknowledged the importance of avoiding patent infringement in both the hardware
and software components of PlantPulse, ensuring transparency and legal compliance throughout
the development process.

What was accomplished:

- Patent Research: The team conducted research to ensure that no patents were violated
    by the design or use of any component in the system, focusing on original software
    development and using publicly available hardware.

What was not accomplished and why:

- Patent Clearance for All Components: While care was taken to avoid patent
    infringement, there were some areas (e.g., LoRaWAN integration) where further legal
    review could have been beneficial, particularly as the project moves toward
    commercialization.

```
5) Specifications
```
The project was required to meet specific design specifications, including feasibility analysis
and a transparent evaluation process, ensuring the system’s viability and alignment with the
proposed objectives.

What was accomplished:

- Feasibility and Evaluation: Regular feasibility analysis and testing were conducted,
    ensuring that the system met the key specifications outlined in the proposal.
- Specifications Adherence: The project adhered to the overall specifications regarding
    ease of use, scalability, and modularity, meeting most of the technical and functional
    requirements.

What was not accomplished and why:

- Full Compliance with All Specifications: Some of the advanced features outlined in the
    specifications, such as full automation and third-party integrations, were not fully
    implemented due to time and technical challenges.

```
6) Deliverables
```
The deliverables included the complete development of the PlantPulse system, including
hardware, software, documentation, and testing reports.

What was accomplished:


- Working Prototype: A working prototype of the system was developed, incorporating
    key features like sensor integration, real-time data monitoring, and remote control via a
    web interface.
- Documentation: Detailed user manuals and technical documentation were created to
    assist with system setup and maintenance.

What was not accomplished and why:

- Full Market-Ready Product: Due to time constraints, the product was not ready for
    mass production or full market deployment. The system was still in the prototype phase,
    and additional refinements were needed before release.

## XXIV. LIFE-LONG LEARNING B. Globalization Retrospective

Upon completing the PlantPulse project, our vision of its potential as a global success has
evolved significantly. Initially, we approached the project with the mindset of creating a highly
localized solution tailored to specific environmental needs. However, as we progressed and
evaluated the scalability and versatility of the system, we began to realize its broader potential for
a global market. The features of PlantPulse, such as remote monitoring, real-time data analytics,
and automated garden management, resonate with a wide range of users, from small-scale home
gardeners to commercial agricultural enterprises. This realization shifted our focus towards
refining the system for global deployment, ensuring that the product could cater to different
environmental conditions, soil types, and cultural preferences across the globe.

In terms of minimizing barriers to trade, several changes made during the project have enhanced
our ability to scale the solution for a global market. Initially, we focused on integrating specific
sensors and components that were easily accessible in our local market. However, as we explored


international markets, we realized the importance of sourcing universally available components to
avoid supply chain disruptions. By transitioning to more globally standardized parts and ensuring
that the system could be easily adapted to various power supply standards (e.g., 120V, 220V), we
significantly reduced potential trade barriers.

Furthermore, the communication protocol we implemented, LoRaWAN, is widely used in IoT
solutions worldwide, which further aids in the system’s global scalability. We also focused on
making the system adaptable to different languages and currencies, recognizing the importance of
localization for user adoption in diverse regions. These adjustments reflect our commitment to
ensuring that PlantPulse could seamlessly integrate into various international markets and meet
the needs of users across different cultural contexts.

As part of the process of validating the global potential of the project, we reached out to our
international contacts for their perspectives on the project’s success and its potential for worldwide
adoption. One key contact, an agricultural technology specialist based in Europe, expressed that
the automated and data-driven nature of PlantPulse aligns well with current trends in precision
agriculture, which is gaining significant traction in Europe. However, they emphasized the
importance of ensuring that the system is adaptable to the varying climates and agricultural
practices in different regions. They also highlighted that, in certain areas, access to high-speed
internet or LoRaWAN networks might be a limitation, suggesting that we explore alternative
communication methods for rural or remote regions. Another contact, an environmental
sustainability advocate from Asia, noted that the real-time monitoring capabilities of the system
would be particularly valuable for urban farming initiatives, which are growing rapidly in many
Asian cities. They also suggested that we consider integrating additional environmental sensors to
monitor air quality and pollution levels, which could further enhance the system’s appeal in regions
focused on sustainable agriculture.

These conversations were invaluable in reshaping our approach to global success. They
underscored the importance of flexibility and adaptability in scaling a product for international
markets. Their feedback has reinforced our commitment to refining PlantPulse to better meet the
diverse needs of users worldwide, from integrating additional sensors to considering regional
infrastructure limitations.

In conclusion, the changes made to the PlantPulse system throughout the project have enhanced
its potential as a globally successful product. By addressing supply chain, communication, and
localization challenges, we are better equipped to navigate the barriers to trade. Our international
contacts have provided valuable insights that have helped refine the product to ensure its global
applicability, further motivating us to continue developing and scaling the solution for a wider
market. As we move forward, we remain committed to optimizing PlantPulse for diverse global
contexts, taking into account the needs of users across different regions and industries.


## XXV. LIFELONG LEARNING

The development of the PlantPulse system has been a powerful motivator for our commitment
to lifelong learning, expanding our understanding of cutting-edge technologies and their practical
applications. Through this project, we have gained firsthand experience in areas such as IoT,
machine learning, and embedded systems, which has fueled our curiosity to continuously explore
new techniques and technologies. Lifelong learning is essential for remaining competitive and
employable in the rapidly evolving tech industry, and this project has reinforced the importance of
proactively acquiring new knowledge.

To support our personal and professional growth, we actively participate in activities like online
courses, webinars, and workshops that focus on emerging technologies and industry trends.
Platforms like Coursera, edX, and Udemy provide access to high-quality courses, while industry
conferences and hackathons allow us to engage with experts and fellow professionals.
Additionally, we contribute to open-source projects, which not only sharpens our skills but also
connects us with a global network of developers and innovators.

Moreover, we are committed to pursuing our Professional Engineer License, which will further
enhance our skills and credentials. This project has reinforced our belief in the importance of
continuous learning, and we are eager to build on this foundation throughout our careers.


In summary, the PlantPulse project has significantly shaped our approach to lifelong learning by
highlighting the importance of continuous personal and professional development. The skills and
knowledge we’ve gained from designing and implementing this system have not only deepened our
technical expertise but also motivated us to pursue further education and hands-on experiences in
emerging fields. By engaging in online courses, attending webinars, participating in workshops,
and contributing to open-source projects, we are taking proactive steps to stay current and
competitive in our field. Our commitment to obtaining a Professional Engineer License further
demonstrates our dedication to long-term career growth. This project has solidified our
understanding that ongoing learning is key to both personal growth and professional success, and
we are excited to continue building on this foundation throughout our careers.

## XXV. CONCLUSION

The PlantPulse project began with the idea of creating a comprehensive and automated
gardening system to assist both amateur gardeners and commercial growers in maintaining optimal
plant health. The vision emerged from a desire to integrate technology into sustainable agriculture
and simplify the management of plant environments. The initial objective was to build a system
that would monitor soil parameters, control environmental factors, and provide users with real-
time data on plant health. This vision evolved through several stages, including interviews with
potential users, surveys, and brainstorming sessions, which helped refine the project scope and
prioritize key features like scalability, ease of use, and marketability.

The main activities involved in completing this project included research into IoT technologies,
designing the system architecture, selecting components, and integrating hardware with software
for seamless operation. Prototyping, testing, and iterative design were critical activities, ensuring
that we addressed user needs and technical challenges. As we progressed, we evaluated results
against the objectives set at the beginning, refining features like modularity, cybersecurity, and the
development of a companion app.

Despite facing numerous challenges such as limited time, resource constraints, and technical
obstacles, we can still consider this project a success. We successfully developed a functional
prototype that demonstrated the core features, such as real-time monitoring and remote control,
even if not all initial goals were fully realized. These hurdles provided valuable lessons in problem-
solving and perseverance, and ultimately strengthened our ability to tackle complex challenges.


The PlantPulse system is a meaningful contribution to society, promoting sustainability by
helping individuals and businesses optimize resource usage in agriculture. Its potential to reduce
water and fertilizer waste, while improving plant health, aligns with global efforts toward more
efficient and eco-friendly farming practices.

On a personal level, this project has significantly contributed to our formation as engineers,
enhancing our technical skills, project management abilities, and teamwork. It also reinforced the
importance of lifelong learning, as we had to continuously acquire new knowledge and adapt to
evolving technologies throughout the project. The experience has not only expanded our
engineering capabilities but also inspired us to continue learning and innovating, ensuring that we
remain adaptable and competitive in our future careers.

## XXVI. REFERENCES

[1] MyGardyn.(n.d.). Gardyn Home Kit Gen3. MyGardyn. Retrieved June 10 , 2024, from
https://mygardyn.com

[2][Online]https://refreshmiami.com/sunrise-startup-bifarm-is-fighting-food-scarcity-using-
aeroponics/ [Accessed 06 15 2024].

[3]BiFarm.(2024).Bloomiee-GrowSmart,LiveBetter.Kickstarter.
https://www.kickstarter.com/projects/bifarm/bloomiee-grow-smart-live-better

[ 4 ] [Online] https://www.kickstarter.com/projects/bifarm/bloomiee-grow-smart-live-better
[Accessed 06 14 2024].

```
[5] [Online] https://www.geodrops.com [Accessed 06 15 2024].
```
Itzhaky, R., Koppels, D., & Shpiz, S. (2019). System and method for plant monitoring (Patent
No.US20160148104A1).GooglePatents.
https://patents.google.com/patent/US20160148104A1/en

[ 6 ] Niwa. (n.d.). Niwa Grow Hub. Retrieved June 17, 2024, from
https://www.getniwa.com/product/niwa-grow-hub/

[ 7 ] FarmBot. (n.d.). Retrieved June 17, 2024, from https://farm.bot/
[ 8 ] Google Store. (n.d.). Nest Learning Thermostat (3rd Gen). Retrieved June 17, 2024, from
https://store.google.com/product/nest_learning_thermostat_3rd_gen?hl=en-US


[9] Google Patents. (2010). An orchard planting monitoring system is based on wireless sensor
networks and monitoring methods (Patent No. CN101661664A). Retrieved June 05, 2024, from
https://patents.google.com/patent/CN101661664A/en

[10] Itzhaky, R., Koppels, D., & Shpiz, S. (2019). System and method for plant monitoring
(Patent No. US20160148104A1). Google Patents. Retrieved June 30, 2024, from
https://patents.google.com/patent/US20160148104A1/en.

```
[11] Genty, N. R., Dominic, J. M. J., et al. (2022). AI-powered autonomous plant-growth
```
## yield desired harvest traits. Figure 15 An AI-powered autonomous plant-growth optimization system automatically adjusts input variables to

No. US11308715B2). Google Patents. https://patents.google.com/patent/US11308715B2/en

```
[ 12 ] ISO, “ISO - About ISO,” ISO. https://www.iso.org/about
```
[ 13 ] 289, “WTO Agreements,” International Trade Administration. WTO Agreements
(trade.gov)

```
[ 14 ] “What we do | IEC,” http://www.iec.ch. What IEC does
```
```
[ 15 ] “IEEE SA - IEEE 802.15.4-2020,” IEEE Standards Association, July 23, 2020. IEEE SA
```
- IEEE 802.15.4- 2020

[ 16 ] “IEEE SA – IEEE 1451.4- 2004 ” IEEE Standards Association, Dec. 6, 2004. IEEE SA -
IEEE 1451.4- 2004

[ 17 ] ISO, “ISO 9001:2015 standard – Quality management systems,” ISO, Mar. 26, 2015. ISO
9001:2015

[ 18 ] ISO, “ISO 14001:2015 standard – Environmental management systems – Requirements
with guidance for use,” ISO, Sep. 2015. ISO 14001:2015

[ 19 ] NIST, “Security and Privacy Controls for Information Systems and Organizations,”
csrc.nist.gov, Dec. 10, 2020. SP 800-53 Rev. 5

[ 20 ] ISO, “ISO/IEC 27001 standard – information security management systems -
Requirements,” ISO, Oct. 2022. ISO/IEC 27001:2022

[ 21 ] ISO, “ISO/IEC 27400:2022 standard – IoT security and privacy - Guidelines,” ISO, June
2022. ISO/IEC 27400:2022

[ 22 ] ISO, “ISO/IEC 30179:2023 standard - Internet of Things (IoT) — Overview and general
requirements of IoT system for ecological environment monitoring,” ISO, January 2023. ISO/IEC
30179:2023


## XXVII. APPENDICES

A. Team Contract

```
As a member of the PlantPulse team, I hereby agree to the following conditions:
```
1. Active Participation: I will actively contribute to team discussions, share my ideas openly,
    and engage constructively with team members during meetings and projects.
2. Adherence to Guidelines: I commit to following the guidelines and rules established by
    the team through consensus. Any proposed changes must be agreed upon by a majority
    vote.
3. Timely Completion of Responsibilities: I am responsible for completing assigned tasks
    promptly and to the best of my ability. I will meet all deadlines and ensure the quality of
    my work meets team expectations.
4. Communication and Attendance: If I am unable to attend a scheduled meeting, I will
    notify the team in advance and catch up on any missed material promptly. Regular
    communication with team members is essential for effective collaboration.
5. Professional Conduct: I will conduct myself professionally at all times, respecting team
    members and their ideas. Any conflicts will be addressed respectfully and resolved through
    open communication or mediation if necessary. The team reserves the authority to dismiss
    me after receiving three warnings (determined by a majority vote). In such a case, I have
    the right to appeal to the class professor and request mediation.
By agreeing to these conditions, I understand the importance of teamwork, communication, and
accountability within our team.

```
Team Member Name Date Signature
```
```
Pedro Ojeda - Leader 06/17/2024
```
```
Jonathan Fleurisma 6/17/2024
```
```
Abigail Sardine-Laforte 6/17/2024 Abigail S. Laforte
```
```
Carlos Gutierrez 6/17/2024
```
```
Richard Cui 6/17/2024
```

### B. Intellectual Property Contract

As a member of the PlantPulse team, we agree to the following terms:

1. This contract has been acknowledged and approved by all team members: Pedro Ojeda,
    Abigail Sardine-Laforte, Jonathan Fleurisma, Carlos Gutierrez, Richard Cui
2. Pedro Ojeda serves as the designated spokesperson for PlantPulse.
3. In the event that an invention is brought to market, profits will be distributed equally among
    all members of PlantPulse.
4. Decisions concerning PlantPulse’s intellectual property will be made by a majority vote of
    all team members present. If consensus cannot be reached, consultation with the mentor
    will be sought to facilitate a decision.

```
Team Member Name Date Signature
```
```
Pedro Ojeda - Leader 06/17/2024
```
```
Jonathan Fleurisma 6/17/2024
```
Abigail Sardine-Laforte 6/17/2024 (^) Abigail S. Laforte
Carlos Gutierrez 6/17/2024
Richard Cui 6/17/2024


## XXVIII. SIGNATURES PAGE

```
Course Number: EEL 4920 Semester: Summer Year: 2024
```
```
Mentor Name: Yu Du
Senior Design I Instructor’s Name: Wilmer Arellano
```
Name PID E-mail Address Phone Number

Pedro Ojeda 6398119 Pojed008@fiu.edu 786 - 438 - 9811

Carlos Gutierrez 6248381 Cguti159@fiu.edu 786 - 843 - 0854

Richard Cui 5862107 Rcui002@fiu.edu 305 - 469 - 5545

Jonathan
Fleurisma

```
6331408 Jfleu037@fiu.edu 954 - 305 - 1013
```
Abigail Sardine-
Laforte

```
6263697 Asard051@fiu.edu 347 - 869 - 4265
```
#### PRINT SIGNATURE DATE

Team Leader

```
Pedro Ojeda
07/25/2024
```
Team Member

```
Carlos Gutierrez
07/25/2024
```
Team Member

```
Richard Cui
07/25/2024
```
Team Member

```
Jonathan
Fleurisma
```
(^)

#### 07/25/2024

Team Member

```
Abigail Sardine-
Laforte
```
```
Abigail S. Laforte
07/25/2024
```
Mentor

```
Yu Du
07/25/2024
```

