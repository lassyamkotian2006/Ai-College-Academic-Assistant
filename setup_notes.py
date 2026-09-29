import os
import urllib.request

os.makedirs("data", exist_ok=True)

# 1. ALL SUBJECTS & SYLLABI IN CLEAN TEXT FORMAT
notes = {
    "college_rules_and_faqs.txt": """NITTE DEEMED TO BE UNIVERSITY - ACADEMIC REGULATIONS, EXAM, INTERNSHIP & STUDENT FAQS (2nd Year B.Tech)
1. ACADEMIC REGULATIONS & ATTENDANCE:
- Minimum Attendance: 85% attendance is required in each course to appear for SEE. Up to 10% (75%-84%) condonation is allowed on medical grounds.
2. EXAMINATION GUIDELINES (CIE & SEE):
- Evaluation Scheme: 100 marks total (50 CIE + 50 SEE).
- Passing Criteria: Minimum 40% in CIE (20/50), minimum 35% in SEE (18/50), and 40% overall aggregate (40/100).
3. INTERNSHIP GUIDELINES:
- Mandatory 4 to 6 weeks internship between 4th & 5th sem (or 6th & 7th sem), evaluated via certificate, report, and presentation.""",

    "syllabus_oop_25CSE202.txt": """OBJECT ORIENTED PROGRAMMING (Course Code: 25CSE202) - 3rd Sem B.Tech CSE
Course Type: IPCC | Teaching Hours/Week (L:T:P:J:SL): 3:0:2:0:1 | Credits: 04 | Total Hours: 45:0:30:0:15 | CIE + SEE: 50 + 50
UNIT-I (9 Hours):
- Overview of Java: OOP, Two Paradigms, Abstraction, Three OOP Principles.
- Introducing Classes: Class Fundamentals, Declaring Objects, new keyword, Object Reference Variables, Methods, Constructors, Parameterized Constructors, this Keyword, Instance Variable Hiding.
- Methods and Classes: Overloading Methods & Constructors, Objects as Parameters, Argument Passing, Returning Objects, Access Control, static, final, Arrays.
UNIT-II (9 Hours):
- Inheritance: Basics, using super, Multilevel Hierarchy, Constructor Execution Order, Method Overriding, Dynamic Method Dispatch, Abstract Classes, final with Inheritance.
- Packages and Interfaces: Packages, Access Protection, Importing Packages, Defining & Implementing Interfaces, Default & static Interface Methods.
UNIT-III (9 Hours):
- Exception Handling: Fundamentals, Exception Types, Uncaught Exceptions, try, catch, multiple catch, throw, throws, finally, Built-in & Custom Exceptions.
- Multi-Threaded Programming: Java thread model, main thread, creating single & multiple threads, Thread priorities, isAlive(), join(), Thread Synchronization.
UNIT-IV (9 Hours):
- Type Wrappers & Autoboxing: Character, Boolean, Numeric type wrappers, Autoboxing/Unboxing in methods.
- Collections Framework: Collection & List interfaces, ArrayList, LinkedList, For-Each iteration.
- File Handling: Reading and writing Serial Access Files, basic File Methods.
UNIT-V (9 Hours):
- Introduction to JavaFX: Application structure (Application, start(), Stage, Scene, Pane), Menus, UI Controls (Label, Button, TextField, ComboBox, CheckBox, Alert), Layouts (VBox, HBox), Event Handling (setOnAction, EventHandler, setOnKeyPressed, setOnMouseClicked).
LIST OF LAB EXPERIMENTS:
1. Encapsulation and abstraction. 2. Code reusability through inheritance. 3. Runtime polymorphism. 4. Abstract class and super keyword hierarchy. 5. Multithreaded applications with distinct tasks. 6. Producer-consumer inter-thread communication. 7. JavaFX UI with inputs/dialogs. 8. JavaFX layouts. 9. ArrayList, LinkedList, and HashSet operations. 10. Serial access file handling.
Textbooks: Herbert Schildt "Java the Complete Reference" (11th Ed); Kishori Sharan "Learn JavaFX 17".""",

    "syllabus_maths_25MAT204_25MAT208.txt": """MATHEMATICS SYLLABUS (3rd & 4th Sem Common for CSE/ISE/CCE/CYB/CBS/AID/AIM/RAI)
1. III SEMESTER: DISCRETE MATHEMATICAL STRUCTURES (Course Code: 25MAT204)
Course Type: BSC | L-T-P: 3-1-0 | Credits: 04 | Hours: 45+15+0 | CIE + SEE: 50 + 50
- UNIT-I (Mathematical Logic - 9+3 Hrs): Propositional Logic, Connectives, Tautology, Contradiction, Propositional Equivalence, Converse, Inverse, Contrapositive, Rules of inference, Validity of arguments, Quantifiers, Proofs (direct, contradiction, contrapositive).
- UNIT-II (Relations - 9+3 Hrs): Relations & Properties, Equivalence relations, Matrix & Digraph representations, Composition of Relations, Partial Order, Poset, Hasse diagram, Extremal sets, Lattice.
- UNIT-III (Groups and Coding Theory - 9+3 Hrs): Groups, Subgroups, Cyclic groups, Coset Decomposition, Lagrange's Theorem, Coding Theory, Hamming Metric, Generator Matrix, Parity Check Matrix, Group Codes, Hamming Matrix.
- UNIT-IV (Combinatorics - 9+3 Hrs): Binomial & Multinomial Theorems, Combinations with Repetition, Catalan numbers, Principle of Inclusion and Exclusion, Derangements, Rook polynomials.
- UNIT-V (Generating Functions & Recurrence Relations - 9+3 Hrs): Ordinary & Exponential generating functions, Non-negative integer solutions for linear equations, First Order Recurrence relations.
Textbooks: Kenneth H. Rosen "Discrete Mathematics and its Applications"; Ralph P. Grimaldi.

2. IV SEMESTER: STATISTICS AND PROBABILITY THEORY (Course Code: 25MAT208)
Course Type: BSC | L-T-P: 3-1-0 | Credits: 04 | Hours: 45+15+0 | CIE + SEE: 50 + 50
- UNIT-I (Curve Fitting & Regression - 9+3 Hrs): Least square principle, fitting straight lines, polynomials, exponential curves, Correlation, Rank correlation, Linear regression, Angle between regression lines.
- UNIT-II (Probability Theory - 9+3 Hrs): Sample space, Conditional probability, Independence, Bayes' theorem, 1D discrete & continuous random variables, PDF, CDF, Expectation, Variance, 2D Joint & Marginal distributions, Covariance.
- UNIT-III (Probability Distributions - 9+3 Hrs): Moment generating functions, Binomial, Poisson, Uniform, Normal, Exponential distributions, Random sample, Central Limit Theorem, Sampling distributions.
- UNIT-IV (Sampling Distribution & Estimation - 9+3 Hrs): Student's t-distribution, Chi-square distribution, Point & Interval estimation, Confidence intervals, Hypothesis Testing, Null & Alternative hypotheses, Type I & Type II errors, P-values, z-test, t-test, Chi-square goodness of fit.
- UNIT-V (Stochastic Process - 9+3 Hrs): Stochastic matrices, Stationary process, Autocorrelation, Markov chains, Regular Markov chain, Transition probabilities, Birth-death process, Queuing theory (M/M/1 Model).
Textbooks: S.C. Gupta & V.K. Kapoor; Paul L. Meyer; Hogg and Craig.""",

    "syllabus_dps_HSS231_and_resume_qbank.txt": """DEVELOPING PROFESSIONAL SKILLS (Course Code: HSS231 / HU2002-1) - 3rd Sem
Course Type: AEC | Credits: 02 | Hours: 30 | CIE + SEE: 50 + 50
- UNIT-I: Understanding Personality (4 Hrs): 16 MBTI personality types, self-assessment. Campus Placement First Impressions (9 Hrs): Crafting tailored resumes, cover letters, portfolios, self-introduction strategies.
- UNIT-II: Personal Branding & Professional Image (5 Hrs): Online presence via LinkedIn and GitHub. Interviews & Group Discussions (5 Hrs): Interview formats, handling tough questions, GD Do's and Don'ts.
- UNIT-III: Goal Setting & Work Ethics (6 Hrs): Work ethics, professionalism, setting SMART (Specific, Measurable, Achievable, Relevant, Time-bound) goals.
DPS RESUME QUESTION BANK (27 Role Prompts):
Includes drafting resumes for: Software Development Intern at tech startup (IT), Civil Engineering Intern (CV), Mechanical Automotive Intern (MECH), QA Software Tester (IT), Electrical Circuit Design Intern (EEE), University IT Support Technician (IT), CAD Drafter (CV), Robotics Club Competitor (RI), Web Developer Intern (IT), Financial Data Analyst Intern (IT/AIDS), Product Design Intern (EEE), Network Engineering Intern (CCE), Materials Science Intern (MECH), Biotechnology & Bioinformatics Intern (BT), Data Science & ML Intern (AIDS), Cybersecurity & Penetration Testing Intern with CEH (CB), AI & Robotics Developer (RI).""",

    "maths_3rd_sem_vector_and_complex.txt": """ENGINEERING MATHEMATICS III (MA2003-1) - VECTOR CALCULUS & COMPLEX VARIABLES
UNIT 1: VECTOR CALCULUS
- Position Vector: r = xi + yj + zk, |r| = sqrt(x^2 + y^2 + z^2). Velocity v = dr/dt, Acceleration a = d²r/dt².
- Gradient: grad(φ) = ∇φ = (∂φ/∂x)i + (∂φ/∂y)j + (∂φ/∂z)k. Normal to surface φ(x,y,z)=c. Unit Normal: n̂ = ∇φ / |∇φ|.
- Directional Derivative of φ along vector a: D = ∇φ · (a / |a|). Maximum directional derivative is |∇φ|.
- Divergence: div(F) = ∇ · F = ∂F1/∂x + ∂F2/∂y + ∂F3/∂z. If div(F) = 0, F is Solenoidal.
- Curl: curl(F) = ∇ × F. If curl(F) = 0, F is Irrotational (Conservative), and F = ∇φ (φ is scalar potential).
- Cylindrical Coordinates (r, θ, z): x = r cosθ, y = r sinθ, z = z. Orthogonal curvilinear system.
- Spherical Coordinates (r, θ, φ): x = r sinθ cosφ, y = r sinθ sinφ, z = r cosθ.
- Integral Theorems:
  1. Green's Theorem: ∮(M dx + N dy) = ∬(∂N/∂x - ∂M/∂y) dx dy
  2. Stokes' Theorem: ∮ F · dr = ∬ (∇ × F) · n̂ dS
  3. Gauss Divergence Theorem: ∬ F · n̂ dS = ∭ (∇ · F) dV
UNIT 2 & 3: COMPLEX VARIABLES
- Analytic Function f(z) = u(x,y) + i*v(x,y). Cauchy-Riemann (C-R) Equations: ∂u/∂x = ∂v/∂y and ∂u/∂y = -∂v/∂x.
- Harmonic Function: Satisfies Laplace equation ∂²u/∂x² + ∂²u/∂y² = 0. Milne-Thomson method constructs f(z) from u or v.
- Bilinear Transformation: w = (az + b)/(cz + d), ad - bc ≠ 0. Preserves cross-ratio.
- Cauchy's Integral Formula: f(a) = (1 / 2πi) ∮ [f(z)/(z - a)] dz.
- Cauchy's Residue Theorem: ∮ f(z) dz = 2πi * (Sum of residues inside C).""",

    "maths_4th_sem_probability_stats.txt": """MATHEMATICS IV SEM (25MAT208 / MA2008-1) - PROBABILITY, DISTRIBUTIONS, SAMPLING & REGRESSION
1. CURVE FITTING, CORRELATION & REGRESSION:
- Straight Line (y = a + bx): Σy = na + bΣx, Σxy = aΣx + bΣx².
- Parabola (y = ax² + bx + c): Σy = aΣx² + bΣx + nc, Σxy = aΣx³ + bΣx² + cΣx, Σx²y = aΣx⁴ + bΣx³ + cΣx².
- Correlation Coefficient (r): r = Cov(X,Y)/(σx * σy), -1 ≤ r ≤ 1.
- Regression Lines: Y on X is (y - ȳ) = byx(x - x̄); X on Y is (x - x̄) = bxy(y - ȳ). r = ±sqrt(byx * bxy).
2. PROBABILITY, BAYES THEOREM & RANDOM VARIABLES (1D & 2D):
- Addition Rule: P(A U B) = P(A) + P(B) - P(A ∩ B). Conditional Probability: P(A|B) = P(A ∩ B)/P(B).
- Law of Total Probability: P(A) = Σ P(Ai)P(A|Ai).
- Bayes' Theorem: P(Ai|A) = [P(Ai)P(A|Ai)] / [Σ P(Ak)P(A|Ak)].
- Discrete RV: Σ p(xi) = 1, Mean E(X) = Σ xi*p(xi), Variance V(X) = E(X²) - [E(X)]².
- Continuous RV: ∫ f(x)dx = 1, E(X) = ∫ x*f(x)dx, CDF F(x) = P(X ≤ x) = ∫_{-∞}^x f(t)dt.
- Properties: E(aX+b) = aE(X)+b, V(aX+b) = a²V(X).
- 2D RV: Marginal g(x) = ∫f(x,y)dy, h(y) = ∫f(x,y)dx. Independent iff f(x,y) = g(x)h(y) and E(XY) = E(X)E(Y).
3. DISTRIBUTIONS, SAMPLING & HYPOTHESIS TESTING:
- Binomial Distribution: P(X=x) = nCx * p^x * q^(n-x), Mean = np, Variance = npq.
- Poisson Distribution: P(X=x) = (e^(-λ) * λ^x)/x!, Mean = λ, Variance = λ.
- Standard Error: SE = σ / sqrt(n). Sample Mean x̄ = Σxi/n, Sample Variance s² = Σ(xi - x̄)²/(n-1).
- Null Hypothesis (H0): Hypothesis of no difference. Alternative Hypothesis (H1): Complementary to H0.
- Type I Error (α): Rejecting H0 when H0 is true (Producer's risk). Type II Error (β): Accepting H0 when H0 is false (Consumer's risk).
- Central Limit Theorem (CLT): Sample mean distribution approaches Normal distribution as n becomes large.""",

    "kannada_3rd_sem_notes.txt": """3RD SEM KANNADA: BALAKE KANNADA (21HU312) & SAMSKRUTHIKA KANNADA
1. BALAKE KANNADA:
- Pronouns: Naanu (I), Naavu (We), Nanna (My), Namma (Our), Niinu/Niivu (You), Ninna/Nimma (Your), Avanu (He), Avalu (She), Avaru (They), Idu (This), Adu (That).
- Question Words (Prashnaarthaka Padagalu): Enu (What), Yaaru (Who), Yaavudu (Which), Elli (Where), Hege (How), Yaake (Why).
- Sentences: Avana hesaru enu? (What is his name?), Avalu yaaru? (Who is she?), Naanu NITTE vidyaarthi (I am a NITTE student), Ivaru namma taayi (She is my mother), AvaLu nanna tangi (She is my sister), Dhanyavaada saar (Thank you sir), Nimage Kaafi beke? (Do you want coffee?).
2. SAMSKRUTHIKA KANNADA:
- 'Karnataka Samskriti' by Hampa Nagarajaiah (born 1936, Hampasandra). Andayya wrote 'Kabbigara Kava'. Ratnakaravarni wrote 'Bharatesha Vaibhava'.
- Shravanabelagola inscription by Bukkaraya highlights religious harmony ('Sarva Dharma Sahishnute').
- 'Turugol': Cattle raid/rescue. 'Garuda': Bodyguards sacrificing life with the king.
- 'Kavirajamarga' states Kannada land stretched from Kaveri to Godavari.
- 'Karnataka Ekikarana' by G. Venkatasubbaiah (born 1913, Ganjam; wrote 'Igo Kannada', 'Eravalu Padakosha').
- Sir Thomas Munro (1800, Collector of Bellary) first spoke of Kannada unification.
- Karnataka Vidyavardhaka Sangha founded in 1890 at Dharwad by R.H. Deshpande. Aluru Venkatarao wrote 'Karnataka Gathavaibhava'. Unification in 1956.
- Kannada script evolved from Brahmi script; called 'Queen of World Scripts' (Lipigala Rani) by Thomas Hodson.""",

    "r_programming_3rd_sem_notes.txt": """DATA ANALYSIS USING R PROGRAMMING (Course Code: CS1602-1) - 3rd Sem Lab & Question Bank
PART A PROGRAMS:
1. User-defined functions: Check even/odd (`a %% 2 == 0`), print squares (`for(i in 0:n) print(i^2)`), find factors of a number (`if(n %% i == 0)`), sort vectors (`sort(a, decreasing=TRUE/FALSE)`).
2. Lists: Create list containing a vector, matrix, and nested list; name elements (`names(list_data)`), count objects (`length()`), add/update/remove elements (`list_data[4] <- NULL`), unlist and add vectors (`unlist()`).
3. Matrices: 3x3 matrix addition (`m1 + m2`), subtraction (`m1 - m2`), transpose product (`m1 %*% t(m1)`), column sum (`colSums()`), row mean (`rowMeans()`), inverse (`solve()`), index of max/min (`which(m == max(m), arr.ind=TRUE)`).
4. Strings & Factors: Count characters (`nchar()`), uppercase (`toupper()`), palindrome check function (`is_palindrome()`), ordered factor of alternating 1s and 2s labeled "ON" and "OFF".
5. Charts & Plots: Pie chart (`pie()`, rainbow colors, 3D pie chart using `plotrix::pie3D`), Bar chart (`barplot()`), Line chart (`plot(type="o")`), Histogram (`hist()`), Boxplot & Scatterplot on `mtcars` dataset (`boxplot(mpg ~ cyl)`, `pairs(~wt+mpg+disp+cyl)`).
6. Central Tendency: Mean (`mean(x, trim=0.3, na.rm=TRUE)`), Median (`median(v)`), Mode user-defined function (`uniqv[which.max(tabulate(match(v, uniqv)))]`).
PART B DATA FRAMES:
1. Employee CSV Data Frame: `str()`, add Department with `cbind()`, add rows with `rbind()`, subset IT employees with salary > 600 (`subset(df, Dept=="IT" & Salary>600)`).
2. Student Marks Data Frame: Merge on Student ID (`merge()`), reshape data using `melt()` and `cast()` from `reshape2` library.""",

    "daa_4th_sem_notes.txt": """DESIGN AND ANALYSIS OF ALGORITHMS (DAA) - 4th Sem (Units 1, 2 & 3)
UNIT 1: INTRODUCTION TO ALGORITHMS
- Definition: Finite set of unambiguous instructions for solving a problem.
- 5 Criteria: Input (0 or more), Output (at least 1), Definiteness (clear/unambiguous), Finiteness (terminates), Effectiveness.
- Problem Solving Steps: Understand problem -> Computational device capabilities (RAM sequential vs parallel) -> Exact vs Approximate -> Data Structures -> Design Technique -> Specify Algorithm -> Prove Correctness -> Analyze (Time/Space, Asymptotic O, Ω, Θ) -> Code.
UNIT 2: DECREASE AND CONQUER, INSERTION SORT, DFS & BFS
- Decrease by constant (by 1): Insertion Sort, Topological Sort, DFS, BFS.
- Decrease by constant factor (by half): Binary Search, Exponentiation by squaring.
- Variable-size decrease: Euclid's GCD algorithm gcd(m,n) = gcd(n, m mod n).
- Insertion Sort: Worst case Θ(n²), Average case Θ(n²), Best case (already sorted) Θ(n).
- Depth-First Search (DFS): Uses Stack (LIFO), tracks Push/Pop order. Complexity: Matrix Θ(|V|²), List Θ(|V|+|E|).
- Breadth-First Search (BFS): Uses Queue (FIFO), level-by-level concentric traversal. Complexity: Matrix Θ(|V|²), List Θ(|V|+|E|).
UNIT 3: GREEDY TECHNIQUE, MST & HUFFMAN CODING
- Greedy Criteria: Feasible, Locally Optimal, Irrevocable.
- Minimum Spanning Tree (MST): Connected acyclic subgraph connecting all vertices with minimum total edge weight.
- Prim's Algorithm: Grows a single tree by adding the minimum-weight edge connecting tree vertex to non-tree vertex. Time: O(|V|²) or O(|E| log |V|).
- Kruskal's Algorithm: Sorts all edges by weight and adds next minimum edge if it doesn't create a cycle. Time: O(|E| log |E|).
- Huffman Coding: Variable-length prefix-free tree for lossless data compression (smallest two weights merged repeatedly; left=0, right=1).""",

    "idt_4th_sem_notes.txt": """INNOVATION AND DESIGN THINKING (IDT) - 4th Sem
1. Design 360° Thinking Approach (Wallet Reference):
   - Fact (Preferences: Physical, Material, Weight, Colour, Cost, Brand)
   - Form (Shape, Size, Texture, Pockets, Pattern)
   - Function (Main use, when/where used, storage, how carried)
   - Relationships (What is added/removed daily, what you hate to lose, personality reflection, personalization).
2. Key Definitions:
   - Design: Purposeful planning and organizing elements to build something (e.g., ergonomic insulated coffee mug).
   - Innovation: Applying creativity to improve/modify an existing solution for customer needs (e.g., Smartphones combining phone, camera, computer).
   - Invention: Creating something completely new from scratch that never existed before (e.g., Aeroplane by Wright brothers, Car by Karl Benz).
   - Creativity: Ability to generate novel and meaningful ideas and solutions.
3. 5 Phases of Design Thinking:
   1. Empathise (Understand customer challenges by putting yourself in their shoes).
   2. Define (Clearly state user needs and problems).
   3. Ideate (Brainstorm creative ideas and detailed sketches).
   4. Prototype (Create a tangible/real model of the planned product).
   5. Test (Evaluate with customers and refine based on feedback).
4. Project Management Models:
   - Agile Model: Iterative and incremental sprints (Brainstorm -> Design -> Development -> QA -> Deployment). Embraces change, continuous customer involvement.
   - Waterfall Model: Linear and sequential (Requirement Analysis -> System Design -> Implementation -> Testing -> Deployment -> Maintenance). Rigid, customer only involved at start.""",

    "syllabus_dbms_CS2102.txt": """DATABASE MANAGEMENT SYSTEMS (Course Code: CS2102-1) - 4th Sem CSE
Course Type: PCC | L:T:P: 3:0:0 | Credits: 03 | Total Hours: 40 | CIE + SEE: 50 + 50
- UNIT-I (15 Hours): Databases & Users, Three-Schema Architecture & Data Independence, ER Model (Entities, Attributes, Keys, Relationships, Structural Constraints, Weak Entities, ER-to-Relational Mapping), Relational Model Constraints, Relational Algebra (SELECT, PROJECT, Set Operations, JOIN, DIVISION).
- UNIT-II (15 Hours): SQL Data Definition, Constraints, Basic & Complex Retrieval Queries, INSERT/DELETE/UPDATE, Assertions, Triggers, Views, Functional Dependencies, Normalization (1NF, 2NF, 3NF, BCNF), Minimal Cover, Relational Decompositions.
- UNIT-III (10 Hours): Storage & File Organizations, Indexing, B+ Tree Dynamic Indexing, Query Evaluation & Optimization, Transaction Management (ACID Properties), Schedules, Lock-Based Concurrency Control (2PL, Serializability, Recoverability).
Textbooks: Ramez Elmasri & Shamkant B. Navathe (7th Ed); Raghu Ramakrishnan & Johannes Gehrke.""",

    "sepm_4th_sem_notes.txt": """SOFTWARE ENGINEERING AND PROJECT MANAGEMENT (SEPM) - 4th Sem
1. INTRODUCTION TO SOFTWARE ENGINEERING:
   - Systematic, disciplined, quantifiable approach to software development, operation, and maintenance.
   - Core SDLC Phases: Requirement Analysis -> System Design -> Implementation -> Testing -> Deployment -> Maintenance.
   - ACM/IEEE Code of Ethics: Confidentiality, Intellectual Property Rights, acting in public interest, meeting highest professional standards (PRODUCT principle).
   - SRS (Software Requirements Specification): Black-box specification stating 'what' the system should do, not 'how'. Properties: Verifiable, Complete, Unambiguous, Traceable. Functional vs Non-Functional requirements.
2. PROCESS MODELS:
   - Boehm's Spiral Model (1986): Risk-driven iterative model with 4 quadrants: 1. Objective Setting/Planning, 2. Risk Assessment & Reduction, 3. Engineering & Prototyping, 4. Customer Evaluation. Best for large, high-risk systems.
   - Rational Unified Process (RUP): Use-case driven, architecture-centric iterative framework with 4 phases: 1. Inception (scope/business case), 2. Elaboration (baseline architecture/risk mitigation), 3. Construction (build system), 4. Transition (deploy to users).
3. THREE CORE CASE STUDIES:
   - Insulin Pump Control System: Safety-critical embedded medical system simulating the pancreas. Uses micro-sensor to measure blood conductivity -> controller computes glucose & insulin dose -> sends pulses to pump needle. High-level dependability requirements: availability and accurate dosing.
   - MHC-PMS (Mental Health Care-Patient Management System): Clinic information system with centralized DB and offline PC sync. Features: 1. Individual care management, 2. Patient monitoring (alerts & tracking 'sectioned' patients), 3. Administrative monthly reporting. Governed by Data Protection & Mental Health laws.
   - Wilderness Weather Station (WWS): Remote self-contained battery/solar-powered stations communicating via satellite. 3 subsystems: 1. Weather Station System (collects & aggregates parameters), 2. Data Management & Archiving System, 3. Station Maintenance System (remote health monitoring, software updates, power management in high wind).
4. PROJECT MANAGEMENT & ESTIMATION (UNIT 3):
   - Pricing factors: Cost estimate uncertainty (contingency), Pricing to win, Contractual terms.
   - Project Scheduling: Work breakdown, Milestones, Deliverables, Gantt Charts (calendar-based activity allocation).
   - Estimation Models: Experience-based vs Algorithmic Cost Modeling (COCOMO II - Constructive Cost Model II: Application-composition, Early design, Reuse, Post-architecture models). Scale factors: Precedentedness, Team cohesion, Process maturity.""",

    "mp_8086_arm_4th_sem_notes.txt": """MICROPROCESSOR AND EMBEDDED SYSTEMS (Course Code: CS3005-1) - 4th Sem
UNIT 1: INTEL 8086 ARCHITECTURE, ADDRESSING MODES & ALP
- 8086 Features: 16-bit microprocessor, 20-bit address bus (accesses 2^20 = 1 MB memory), 16-bit data bus, segmented memory (4 active 64KB segments: CS, DS, ES, SS).
- Architecture: Divided into BIU (Bus Interface Unit - fetches instructions, calculates 20-bit physical address = Segment * 10H + Offset, has 6-byte FIFO instruction queue) and EU (Execution Unit - ALU, General Registers AX, BX, CX, DX, Pointer/Index Registers SP, BP, SI, DI, and 16-bit Flag Register with 9 active flags: OF, DF, IF, TF, SF, ZF, AF, PF, CF).
- Addressing Modes: Immediate (`MOV AX, 0005H`), Register (`MOV AX, BX`), Direct (`MOV AX, [2500H]`), Register Indirect (`MOV AX, [BX]`), Based-Indexed (`MOV AX, [BX+SI]`), Register Relative (`MOV AX, [BP+100H]`).
- Assembler Directives: ASSUME (binds logical segment to physical segment register), DB (Define Byte), DW (Define Word), DD (Define Doubleword), DQ (Quadword), DT (Ten Bytes), EQU (Equate constant), EVEN (align on even memory address), PROC/ENDP, SEGMENT/ENDS, OFFSET, EXTRN/PUBLIC, MACRO/ENDM.
- Key Instructions: MOV, PUSH/POP, XCHG, IN/OUT, XLAT (table lookup), DAA (Decimal Adjust after Addition), AAA (ASCII Adjust after Addition), CBW, CWD, Shift & Rotate (SHL, SHR, SAR, ROL, ROR, RCL, RCR).

UNIT 2: MODULAR PROGRAMMING, INTERRUPTS, ARM7 & ARDUINO EMBEDDED C
- Procedures vs Macros: Procedures use `CALL` and `RET` (saves memory, uses stack for return address, slower execution due to call overhead); Macros inline code at assembly time (faster execution, takes more memory).
- BIOS & DOS Interrupts: `INT 21H` (DOS functions: AH=01H read char, AH=02H display char, AH=09H display string, AH=2CH get system time, AH=3CH create file, AH=3DH open file, AH=3FH read file, AH=40H write file), `INT 10H` (Video BIOS: AH=00H set video mode, AH=02H set cursor), `INT 16H` (Keyboard BIOS: AH=00H read key, AH=01H check key buffer).
- RISC vs CISC: RISC (Reduced Instruction Set, fixed instruction length, single-cycle execution, load-store architecture, many registers, hardwired control) vs CISC (Complex Instruction Set, variable length, multi-cycle, memory-to-memory ops, microprogrammed control).
- ARM Processor Architecture: 32-bit RISC core, 3-stage pipeline (Fetch, Decode, Execute), 37 total registers (R0-R12 general purpose, R13=SP, R14=LR Link Register, R15=PC Program Counter, CPSR Current Program Status Register with N, Z, C, V flags and mode bits, SPSR Saved PSR).
- Arduino Due & Embedded C: 32-bit Atmel SAM3X8E ARM Cortex-M3 board, 54 digital I/O pins, 12 analog inputs. Functions: `pinMode(pin, INPUT/OUTPUT)`, `digitalWrite(pin, HIGH/LOW)`, `digitalRead(pin)`, `analogRead(pin)`, `analogWrite(pin, pwm)`, `Serial.begin(9600)`, `Serial.println()`.

UNIT 3: 8086 PIN CONFIGURATION, MIN/MAX MODE, INTERRUPTS & MACHINE CODE
- Pin Configuration (40-pin DIP): `MN/MX#` pin selects mode (HIGH = Minimum Mode single processor; LOW = Maximum Mode multiprocessor with 8288 Bus Controller).
- Common Pins: `AD0-AD15` (multiplexed address/data), `ALE` (Address Latch Enable - latches address into 8282), `READY` (synchronizes slow peripherals), `INTR` (maskable interrupt), `NMI` (Non-Maskable Interrupt - Type 2), `RESET`, `BHE#/S7`.
- Minimum Mode Pins: `HOLD` & `HLDA` (bus request/grant for DMA), `DEN#` (Data Enable for 8286 transceiver), `DT/R#` (Data Transmit/Receive), `M/IO#`, `WR#`, `INTA#`.
- Maximum Mode Pins: `RQ#/GT0#` & `RQ#/GT1#` (Request/Grant), `LOCK#` (locks bus for multiprocessor), `QS0, QS1` (Queue Status), `S0#, S1#, S2#` (Status signals to 8288).
- Interrupt Vector Table (IVT): First 1 KB of memory (`00000H` to `003FFH`), stores 256 interrupt vectors (4 bytes each: 2 bytes IP offset + 2 bytes CS segment). Physical address of `INT n` = `n * 4` (e.g., `INT 12H` = `12H * 4 = 00048H`; `INT 08H` = `08H * 4 = 00020H`).
- Predefined Interrupts: Type 0 (Divide by zero), Type 1 (Single step / Trap), Type 2 (NMI), Type 3 (1-byte Breakpoint `INT 3`), Type 4 (Overflow `INTO`).
- Hand Coding MOV Instructions (Machine Code Template):
  Byte 1: `[Opcode (6 bits: 100010 for MOV)] [D bit (1=to REG, 0=from REG)] [W bit (1=16-bit word, 0=8-bit byte)]`
  Byte 2: `[MOD (2 bits: 11=register, 00=no disp, 01=8-bit disp, 10=16-bit disp)] [REG (3 bits)] [R/M (3 bits)]`."""
}

for filename, content in notes.items():
    with open(os.path.join("data", filename), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Created data/{filename}")

# 2. AUTO-DOWNLOAD DIGITAL FILES DIRECTLY FROM GOOGLE DRIVE (NO MANUAL CLICKING NEEDED)
drive_files = {
    "maths_3rd_sem_qbank.pdf": "https://drive.google.com/uc?export=download&id=104VSRD3Uv5k-Bvp-KowVXLrz0KE5Izc7",
    "maths_3rd_sem_mcqs.pdf": "https://drive.google.com/uc?export=download&id=1F_oLKeOn3Euw8wAcCdyv2wq6XY17CJsh",
    "r_programming_qbank.pdf": "https://drive.google.com/uc?export=download&id=1phcmjJHgftLmoOAst8eL-xzP_LmyyBp3",
    "r_programming_lab_manual.pdf": "https://drive.google.com/uc?export=download&id=10RKKkNWPK4kp7zHZT4OhwHz3u7DUF0NQ",
    "balake_kannada_mcqs.pdf": "https://drive.google.com/uc?export=download&id=1CiPGIYH-DmqUzaonmV_M1iRC9cx08Rk3",
    "idt_notes.pdf": "https://drive.google.com/uc?export=download&id=1rvkKVw9XSTXVjJBN1gHIx9nrMTTnpcf_",
    "sepm_insulin_pump.pdf": "https://drive.google.com/uc?export=download&id=1IXxHL3T6AEV7k6iRHvfb9n1mDFtEJZno",
    "sepm_mhc_pms.pdf": "https://drive.google.com/uc?export=download&id=1hr8dYcIgcUw7m_JyUMcckthhZv2V2K6k",
    "sepm_weather_station.pdf": "https://drive.google.com/uc?export=download&id=1aMdbgXZ5895zmIJHkXdjrJypKRjto3Xm",
    "sepm_unit1_2_mcqs.pdf": "https://drive.google.com/uc?export=download&id=1_wzpGd4N3k-7w6lR-NmdAIKqsRr9ptGT",
    "sepm_unit3_mcqs.pdf": "https://drive.google.com/uc?export=download&id=1a211gDehay8-37L8igkkC_Gpp24_7n3r",
    "mp_unit1_qbank.docx": "https://drive.google.com/uc?export=download&id=1OZ4mRKYRBZFQta9p1sUvq3DiNWzZQTKr",
    "mp_unit2_qbank.docx": "https://drive.google.com/uc?export=download&id=1TIf5ufxrDeGAom6oInrLJmh7oOu5ACt1",
    "mp_unit3_qbank.docx": "https://drive.google.com/uc?export=download&id=1Fehu5cJKvn7lhavwFBUZWAdnLn2mOzI_",
    "mp_unit1_mcqs.docx": "https://drive.google.com/uc?export=download&id=1YxhkQuIdp2DGWMwT-6cNsqNkOfWMZWAu",
    "mp_unit2_mcqs.docx": "https://drive.google.com/uc?export=download&id=1d-F8w0nkxGU0VTFVvVntlLqUnKq51hA1",
    "mp_unit3_mcqs.docx": "https://drive.google.com/uc?export=download&id=1LqZPJ2yqzZ9ahTGwoiezQbeioz-EfXPF"
}

print("\n📥 Auto-downloading digital PDFs & DOCX files from Google Drive...")
for filename, url in drive_files.items():
    filepath = os.path.join("data", filename)
    try:
        urllib.request.urlretrieve(url, filepath)
        print(f"   -> Downloaded data/{filename}")
    except Exception as e:
        print(f"   -> Skipped download of {filename} (already covered in text notes)")

print("\n🎉 ALL 3RD & 4TH SEM FILES ARE READY IN data/!")