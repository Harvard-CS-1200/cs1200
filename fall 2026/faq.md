# Fall 2026 Course FAQ

Many questions recur throughout the semester, so this page collects answers to some of the most common ones. Please bookmark it and consult it when questions arise.

This FAQ applies to both **CS1200 (Harvard College)** and **CSCI E-120 (Harvard Extension School)** unless an answer says otherwise. When the two courses have different procedures, they are described separately. The course syllabus remains the authoritative source for course policies; if anything here seems unclear, please ask the course staff on Ed.

## Lectures

<details>
<summary><strong>Where are the detailed lecture notes? What is the textbook?</strong></summary>
<br>

The detailed lecture notes used through Fall 2024 have been replaced by the course textbook written by Adam Hesterberg and Salil Vadhan, the original instructors of the course. The textbook is available on [Perusall](https://app.perusall.com/courses/compsci-1200-introduction-to-algorithms-and-their-limitations-251871317/fall_26_cs1200_textbook?filter=all), where you are encouraged to ask questions and leave comments. The chapters associated with each lecture are listed in the [Course Schedule](https://docs.google.com/spreadsheets/u/1/d/1P9DFhJ2pa4CRkKgFCBmTlU3fiKknR1KLHDgiMxTG1ps/edit?gid=0#gid=0).

We will also provide draft lecture notes with portions for you to complete while attending or watching each lecture.

</details>

## Problem Sets

<details>
<summary><strong>What are the most important problem-set policies?</strong></summary>
<br>

- Problem sets are graded using the course letter-grade scale: N = not assessable, L = learning, R- = nearly ready to move on, R = ready to move on, and R+ = beyond ready.
- College students have 8 total late days; Extension students have 25. At most 3 late days may be used on any one problem set, and partial late days count as full days.
- A problem set submitted more than 3 late days after its deadline automatically receives an N. Each late day beyond a student's total budget reduces the problem-set GPA by 0.0333.
- Late days used on the problem set whose content grade is ultimately dropped do not count toward the total late-day budget.
- Any adjustment resulting from a Problem Set Follow-Up is applied first. We then drop the lowest problem-set content grade.
- Separately, we drop the lowest qualitative reflection-question grade from the participation calculation. We also drop the lowest SRE survey grade.

</details>

<details>
<summary><strong>How should I test my code?</strong></summary>
<br>

For each problem set containing code, we will provide local tests that give quick feedback while you work. You should run these tests before submitting to Gradescope. The local tests are useful but are not exhaustive: passing them does not guarantee that your code is correct or that it will pass all Gradescope tests.

</details>

<details>
<summary><strong>Why does my code pass the local tests but fail Gradescope tests?</strong></summary>
<br>

Gradescope includes additional tests that are not part of the local test suite. These hidden tests check inputs and edge cases that the local tests may not cover and help ensure that a program solves the general problem rather than only the provided examples. Use the problem specification, not just the local tests, as the definition of correct behavior.

</details>

<details>
<summary><strong>Every proof of correctness is different. How do I know what to prove?</strong></summary>
<br>

Proofs on exams will generally use structures that have been taught and practiced in lectures, sections, and problem sets. Problem-set proofs may require more adaptation. A useful first step is to identify the central claim that makes the algorithm correct and then try to find an input or edge case that would invalidate your argument. If you cannot rule out such a counterexample, the proof is incomplete.

There is no single formula for discovering a proof. In this course, most proofs combine **pattern recognition**—recognizing a familiar proof structure—with **adaptation**—modifying that structure to handle the details and edge cases of the problem at hand. Common patterns include the following.

- **Ad hoc arguments.** Some algorithms do not fit a standard template. Identify the one or two essential properties that imply correctness and justify each directly.
  - In the Size-Augmented Rotation problem from a previous offering, one must explain both why the updated nodes receive the correct sizes and why every node not updated retains the correct size.
  - For Singleton Bucket Sort, one can prove separately that the output is a permutation of the input and that adjacent output keys satisfy $K_i \leq K_{i+1}$.
- **Induction for recursion.** Assume that recursive calls are correct on smaller inputs, and then prove that the current call combines their outputs correctly.
  - For Merge Sort, assuming that the recursive calls correctly sort the two smaller arrays, prove that merging them produces a sorted permutation of the original array.
  - For Weighted QuickSelect, use the correctness of the recursive call on the appropriate subarray to establish correctness on the full array.
- **Loop invariants.** State a property that is true before the loop begins, remains true after every iteration, and implies correctness when the loop ends.
  - For Insertion Sort, the relevant invariant is that the processed prefix is sorted.
  - For Radix Sort, the invariant is that after $k$ iterations, the elements are sorted by their $k$ least significant digits.
- **Reductions.** When an algorithm uses another problem as a subroutine, explain why the transformation preserves the information needed to solve the original problem.
  - Some reductions are fairly clear, such as reducing Area-of-convex-polygon to Sorting. Here, you need to remember why sorting is relevant and whether your proof is reflecting this.
  - In reductions intended to show that two computational questions are equivalent, one typically proves both directions: a solution to the original instance yields a solution to the constructed instance, and a solution to the constructed instance yields a solution to the original one.
  - For reductions to Single Source Shortest Paths, this often means relating feasible solutions in the original problem to paths of the same cost in the constructed graph.
  - For NP-completeness and unsolvability reductions, this generally means proving the required correspondence between yes-instances of the two problems.

These are templates, not substitutes for reasoning. Your proof must still explain why the template applies to the particular algorithm and input under consideration.

</details>

<details>
<summary><strong>What level of formality is expected?</strong></summary>
<br>

There is a difference between **rigor** and **detail**. Rigor means that every important claim is justified; detail refers to how much explanation accompanies each justification. We expect rigorous problem-set solutions, but they do not need to be unnecessarily long. Identify the claims on which correctness depends and justify them clearly enough that a knowledgeable reader can verify the argument.

Staff solutions are a useful reference. They sometimes contain more explanation than a submitted solution requires because they are also intended to teach students who did not solve the problem.

</details>

<details>
<summary><strong>I often miss a step in my proofs. How can I improve?</strong></summary>
<br>

We do not expect every first attempt to be perfect. After a problem set is graded, compare your solution carefully with the staff solution and feedback. For every omitted step, ask what possible failure that step was needed to rule out. Over time, this practice should help you recognize the claims that require explicit justification.

Students who receive an L or N may also discuss the feedback or a revision with the instructional staff during office hours or through the support process described in the syllabus. These meetings support learning but do not change the original problem-set grade.

</details>

<details>
<summary><strong>Where can I find my Gradescope feedback, and how should I use it?</strong></summary>
<br>

Open the assignment on Gradescope and select each problem to see its letter grade, rubric items, and written feedback. The rubric indicates what a complete solution was expected to establish. Pay particular attention to problems graded below R and compare them with the staff solutions. This is also useful exam preparation: it helps identify justifications that may feel implicit but must be stated in a complete proof.

</details>

<details>
<summary><strong>How important is earning an R+?</strong></summary>
<br>

Your primary goal should be to earn R grades consistently, showing that you have met the learning objectives. An R+ recognizes work that is nearly perfect or goes beyond expectations in clarity, insight, or exploration. It makes a modest positive contribution to the problem-set GPA, but it is not necessary for strong performance in the course. Focus first on mastering the material rather than trying to turn every R into an R+.

</details>

<details>
<summary><strong>How are the qualitative reflection questions included in problem sets graded?</strong></summary>
<br>

These questions form part of the participation grade. They use the N/L/R/R+ scale; R- is not used for participation. An R response demonstrates specific and thoughtful engagement with your experience in this course. A superficial or generic response may receive an L, and a missing response receives an N. A paragraph is often sufficient, but specificity and thoughtfulness matter more than sentence count. The lowest qualitative reflection-question grade is dropped.

These questions are different from the short Problem Set Follow-Ups described below.

</details>

<details>
<summary><strong>What is a Problem Set Follow-Up, and how does it affect my grade?</strong></summary>
<br>

After each problem set's late deadline, you will complete a short written question asking you to reflect on or extend a concept from that problem set. It is designed to require no more than about five minutes and can ordinarily be answered in one or two sentences. College students complete it in class; Extension students complete it online using Proctorio.

A satisfactory answer leaves the corresponding problem-set content grade unchanged. An unsatisfactory answer changes R+, R, or R- to L, or changes L to N. This is an adjustment to the problem-set grade, not part of the participation grade. The adjustment is applied before the lowest problem-set content grade is dropped.

</details>

## Sender-Receiver Exercises (SREs)

<details>
<summary><strong>When and how do I complete the SREs?</strong></summary>
<br>

There are four SREs. College students complete them with a partner during the designated class meetings. Extension students complete them with a partner over Zoom during the weekend before the corresponding lecture; the course staff will provide a spreadsheet to facilitate pairing and scheduling. Senders should spend at least an hour preparing the assigned proof. Each student submits a short reflection survey after the exercise.

</details>

<details>
<summary><strong>How are SREs graded? Why do I not see an SRE grade on Gradescope?</strong></summary>
<br>

SRE surveys are part of the participation grade and use the N/L/R/R+ scale; R- is not used. A completed survey showing serious engagement will ordinarily receive an R. A superficial submission may receive an L, a missing submission receives an N, and an unusually thoughtful contribution may receive an R+. SRE grades are not released during the semester, but the course staff records them and automatically drops the lowest of the four SRE survey grades.

</details>


<details>
<summary><strong>What should I do if I must miss a lecture, SRE, or Problem Set Follow-Up?</strong></summary>
<br>

- **Ordinary lecture:** College students who miss a lecture that does not contain an SRE, Problem Set Follow-Up, or exam do not need to request an excused absence, but they are responsible for reviewing the missed material. Extension students ordinarily watch the recorded lectures asynchronously.
- **Planned SRE or Problem Set Follow-Up absence:** Email the course staff at least four days before the missed activity and copy your resident or faculty dean, or your advisor if you are a graduate student. For a missed SRE, you are responsible for arranging a makeup with another student, using the spreadsheet supplied by the course staff. The SRE survey deadline will be extended by three days.
- **Illness, injury, or personal emergency:** The missed SRE or Problem Set Follow-Up will be excused if the course staff receives a note from HUHS for an illness or injury, or an email from your resident dean, faculty dean, or graduate advisor for a personal emergency. An SRE makeup is not required, although we strongly recommend reviewing the material with a classmate when you are able.
- **Other missed SRE:** There is no makeup for an unexcused absence such as oversleeping or missing the shuttle. Because the lowest SRE survey grade is dropped, one such absence need not lower the SRE component of the participation grade.
- **Other missed Problem Set Follow-Up:** An unexcused missed Follow-Up changes the corresponding problem-set grade from R+, R, or R- to L, or from L to N.

Extension students who cannot complete a scheduled Zoom SRE or online Problem Set Follow-Up within its assigned window should contact the course staff as early as possible. The documentation and makeup rules above apply to the corresponding remote activity.

Exam conflicts and absences are governed by the separate policies below.

</details>

## Exams

<details>
<summary><strong>How are numerical exam scores translated into grades? Are exams curved?</strong></summary>
<br>

There is no predetermined percentage-to-GPA conversion. After grading an exam, the instructors identify score levels that represent the boundaries between Harvard letter grades, using the [Harvard College grading descriptions](https://infoforfaculty.fas.harvard.edu/book/grading-system), and use linear functions between those thresholds to determine exam GPAs. Thus, the conversion reflects the level of proficiency demonstrated on that particular exam rather than a fixed rule such as “90% always equals an A.”

</details>

<details>
<summary><strong>How much do the exams count toward my final grade?</strong></summary>
<br>

The two 75-minute midterms and the 180-minute final together constitute 50% of the course grade. Within that category, the exams are weighted in proportion to their lengths, in the ratio 75:75:180. Consequently, each midterm constitutes approximately 11.36% of the overall course grade, and the final constitutes approximately 27.27%.

</details>

<details>
<summary><strong>When and where do Extension students take the exams?</strong></summary>
<br>

Extension students choose a 75-minute block for each midterm and a 180-minute block for the final within 24 hours after the corresponding College exam begins. The exams are paper-based. An Extension student who does not take an exam in person must arrange a qualified local proctor. A DCE Exam Manager will provide instructions and confirm proctor information closer to the exam date. See the [Extension School exam policies](https://extension.harvard.edu/enrolled-students/exam-types-and-policies/) for additional information.

</details>

<details>
<summary><strong>What should I do if I have an exam conflict or must miss an exam?</strong></summary>
<br>

- **College midterms:** Email the course heads as soon as possible. We cannot guarantee a makeup time, but we will try to accommodate valid, unavoidable conflicts. If no makeup can be arranged for a valid conflict, the missed exam's weight will be transferred to the exams you do take.
- **College final exam:** Contact the Registrar about final-exam conflicts; your resident dean can assist with this process.
- **Extension exams:** Follow the instructions supplied by the DCE Exam Manager and contact the Exam Manager and course heads promptly if a conflict or emergency affects your assigned exam window or proctor arrangements.


</details>




</details>

