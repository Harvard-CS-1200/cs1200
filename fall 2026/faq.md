# Fall 2026 Course FAQ


We see a lot of the same questions popping up throughout the semester, and sometimes we make an Ed post answering these questions but people who don't read it at the time will usually come back with the same question a few weeks later. So instead, we're going to start putting answers to these common questions on this webpage -- bookmark it and hopefully it'll be a useful resource for when you have questions!

## Lectures

<details>
<summary>
<b> Where are the detailed lecture notes? What's the textbook? </b>
</summary> <br>

The same as Spring 26, the detailed lecture notes (which were offered till Fall 2024) are now replaced with the course textbook written by Adam Hesterberg and Salil Vadhan (the two original professors of the course!). The textbook is available on [Perusall](https://app.perusall.com/courses/compsci-1200-introduction-to-algorithms-and-their-limitations-251871317/fall_26_cs1200_textbook?filter=all), where you are encouraged to ask questions or leave comments. The specific chapters for each lecture are listed on the [Course Schedule](https://docs.google.com/spreadsheets/u/1/d/1P9DFhJ2pa4CRkKgFCBmTlU3fiKknR1KLHDgiMxTG1ps/edit?gid=0#gid=0) spreadsheet. 

We will still provide 'draft lecture notes' with partially filled class content for you to work through in the class.  

</details>

## Problem Sets

<details>
<summary>
<b> What are the important pset policies to remember? </b>
</summary> <br>


- Problem sets are letter graded (N = not assessable, L = learning, R- = nearly ready to move on, R = ready to move on, R+ = beyond ready).
- Students have 8 late days and can spend at most 3 on a given pset.
- The lowest pset grade will get dropped.


</details>

<details>
<summary>
<b> How should I be testing my code? </b>
</summary> <br>

For every problem set with code, there will also be some local testing functionality we provide for you to confirm that your code works as intended. We recommend using local test cases as a quick way of testing whether your code works -- if you upload your code to Gradescope it can take up to a minute to evaluate whether your code passes test cases, whereas if you run local tests it'll tell you within a second. Only after your code passes local test cases should you upload it to Gradescope.

</details>

<details>
<summary>
<b> Why do I pass local tests but not Gradescope tests? </b>
</summary> <br>

One possible "hack" arises where a student could take a look at the test cases and hardcode some if statements to return the correct answer for those test cases (even if the code in general is incorrect). The solution here is that we include additional test cases on Gradescope so that even if the local tests get hardcoded Gradescope tests will expose errors. Therefore, even if your code passes local tests, it might not pass Gradescope tests. The ideal scenario is that local test cases should be thorough enough that any code which passes local test cases will pass Gradescope test cases as well, but sometimes due to oversight this won't be the case.

</details>

<details>
<summary>
<b> Every proof of correctness is slightly different -- how do I know what to do? </b>
</summary> <br>

First, it's worth noting that for exams proofs of correctness will usually follow very fixed structures that we cover in lecture / problem sets -- for example some correctness proofs on the final will just be for an NP-completeness or unsolvability proof which we'll drill. However, problem sets can require a little more adaptation. <br>

A good starting point is building some intuition for why a proof of correctness is sufficient -- I like thinking about it as examining whether an experiment successfully proves a claim, or whether a historical argument is correct. There's no formula for whether a proof of correctness is sufficient, but by trying to poke holes in the proof you can gain some intuition for what constitutes correctness.

How do you come up with these proofs yourself? In general, this is a hard question to answer -- there's no formula for proving that an algorithm/reduction is correct, and I would say it's probably more accurate to say that correctness is a combination of pattern recognition (seeing when you can apply established techniques) and adaptation (recognizing when you need to adapt techniques to accommodate for edge cases / unique situations). Hopefully by doing the psets you've gained a little bit of both! <br>

However, for this class we actually don't introduce that many new patterns. By outlining a few patterns + examples you'll probably be pretty well-equipped to tackle most things we throw at you. Here's a preliminary attempt at doing that: <br>


- <b>Ad Hoc</b>: Sometimes (not often) you'll need to come up with a proof of correctness for an algorithm that doesn't follow a predetermined structure. Ad hoc means "created or done for a particular purpose as necessary" -- aka "you're kind of on your own" 
    - <b>Size-Augmented Rotation</b>: This was problem 3b on pset 2 in Fall 25 -- there's no precedent in class for proving correctness of a procedure for maintaining size-augmentation. Part of the proof of correctness is explaining why every node you don't update doesn't need to be updated -- this is something that you just have to figure out. 
    - <b>Singleton Bucket Sort</b>: I (Anurag's note: the `I' here and below refers to Maxwell, the original creator of this FAQ) got a few questions during this SRE about what correctness looks like for this algorithm. Here the two properties of a correct Sorting are 1) the answer is a permutation of the input, and 2) $K_i \leq K_{i+1}$. In this case you have to recognize that both can be proved directly with not that much effort. 
    - One thing to note is that even though you're left on your own, usually the proof of correctness is a little bit easier and comes down to finding the 1 or 2 "core claims" that you need to justify. 
- <b>Induction for Loops/Recursion</b>: 
    - <b>Recursion</b>: This is probably the one you're more used to (just remember to use strong induction)
        - <b>Merge Sort</b>: If this algorithm correctly sorts arrays of size $\frac{n}{2}$, then it will sort the full array of size $n$.
        - <b>Weighted QuickSelect</b>: If this algorithm can find the $t$'th element in the left or right subarray, then we'll get our answer for the entire array. 
    -  <b>Loops</b>: When an algorithm involves doing something in a loop, and the body of the loop is sufficiently complicated that it warrants an explanation of what you're doing at each step, you can consider a loop invariant.
        - <b>Insertion Sort</b>: we proved the claim that after $k$ iterations of the outer loop, the first $k$ elements of the array should be sorted (and this way the inductive step can focus on proving that the $k+1$-th iteration inserts the $k+1$-th element into the correct place)
        - <b>Radix Sort</b>: we proved the claim that after $k$ iterations of the outer loop, the elements of the array were sorted by their $k$ least significant digits. The inductive step used the stability of Singleton Bucket Sort to justify why numbers with the same $k+1$-th digit would remain in sorted order.
- <b>"Basic" vs "Advanced" Reductions</b>: I don't have a good definition of what a "basic" reduction is, but the main category we see in this class is reductions to Sorting. These are "basic" in the sense that the oracle is just a step that we abstract away for convenience, but the actual problem solving logic is contained in the reduction itself. For example, for AreaOfConvexPolygon we did all the complex area calculation in the reduction, whereas Sorting was just something convenient that we wanted as part of this routine. By contrast, an "advanced" reduction is more like an argument that the two computational problems are equivalent -- very soon after the midterm we'll see reductions to Single Source Shortest Paths which hint at this, and then we'll see the big NP-completeness and unsolvability reductions which really lean into this idea.
- <b>Correctness for "Basic" Reductions</b>: A proof of correctness for a basic reduction is usually very similar to an ad-hoc proof of correctness. 
    - <b>AreaOfConvexPolygon</b>: This is the main reduction to Sorting that we did on a problem set -- remember that the bar for correctness was pretty low because you just needed to explain why sorting is relevant (so that adjacent points are connected by an edge) and why your triangulation of choice was valid (a convex polygon containing the origin can be deconstructed into triangles at the origin).
- <b>Correctness for "Advanced" Reductions</b> (post-midterm): By contrast, a proof of correctness for an advanced reduction usually needs to argue for the equivalence of two sets of solutions (ie the instance that you construct and pass to the oracle has the same solution set as the original problem). This pretty much always requires a bidirectional proof -- explaining that a solution for problem A corresponds to an equivalent solution to problem B and vice versa. You haven't seen any of these yet, so I'll give examples that will make more sense in the weeks after the midterm:
    - <b>Reductions to Single Source Shortest Paths</b>: Usually this kind of reduction involves an assumption that the original problem is equivalent to a graph that you've constructed as the input to SSSP. Usually the bidirectional proof here involves establishing a mapping from a sequence of moves in the original problem to a path of the same length on the constructed graph, and vice versa. By proving this mapping you demonstrate that the length of the shortest path on the constructed graph is equal to the length of the optimal sequence of moves in the original problem.
    - <b>NP-completeness Reductions</b>: This is an entirely different rabbithole we'll dive into later in the semester -- however, the core idea of establishing mappings between solutions still holds. In this case we want to show that a solution $S$ for $\Pi$ corresponds to an equivalent solution $S'$ for $\Gamma$, and vice versa.
    - <b>Unsolvability Reduction</b>: Again, bidirectional -- this time since it's between problems where the answer is yes/no it'll look more like if the answer for $\Pi$ is yes then the answer to $\Gamma$ is also yes, and vice versa.
</details>


<details>
<summary>
<b> What's the level of formalism expected? </b>
</summary> <br>

There's a difference between <b>rigor</b> and <b>detail</b> in a proof. Rigor refers to the extent to which important statements are justified, whereas detail refers to the level of explanation given to each justification. For problem sets, we ask for rigor -- part of your task is to identify what justifications are necessary to prove the given statements. However, you don't need as much detail -- the TFs grading the problems sets are familiar with these justifications so as long as you identify the right claims and write down the correct justifications you don't need to write pages and pages explaining your justifications.

If you need a reference for how much detail in a proof is appropriate, looking at staff solutions for problem sets is a good idea. Keep in mind that sometimes the staff solutions will go into extra detail in order to provide extra context for students who were unable to solve the original problem -- sometimes you might not even need to match that level of detail.

</details>

<details>
<summary>
<b> I can't tell whether my proofs are complete and always get marked down for missing something -- what do I do? </b>
</summary> <br>

We don't expect perfect thorough proofs in every problem set, but we do hope that by submitting your best effort and comparing it with the Staff provided solution/Feedback on your pset, you get better over time at writing proofs!

</details>

<details>
<summary>
<b> Where do I find my Gradescope feedback? How do I interpret it? </b>
</summary> <br>

If you navigate to the assignment on Gradescope you can click through each problem to see what feedback you got, as well as the letter grade you got for a particular problem. Reading through the rubrics is important -- it can help you get an idea of what we expected to see from you in the proof. This can be particularly helpful for exams, where sometimes you include some justification on the problem set but forget to include it on the exam when it's actually something we take off points for missing. Looking at problems where you got below an R and reading rubric items that indicate what we were looking for in a full-credit solution is a great way to understand what you're missing and where you should add more justification.

</details>

<details>
<summary>
<b> How important is getting an R+? </b>
</summary> <br>

The important thing to note is that getting all R's should be the primary goal, and having an R+ is nice but not necessary. Notice that according to the "Letter grades" section of the syllabus, an R- is equivalent to a 3, an R is equivalent to a 4, and an R+ is equivalent to a 4.33 on the 4.0 scale. Taking into account the 8 pset grades and problem sets being 30% of the overall grade, that means that going from an R to an R+ will net you a 0.01 increase in your overall class GPA -- assuming a uniform GPA distribution, the probability of this bump taking you across a grade cutoff is a little under 4%. So it might be worth going for the R+ if you have extra time, but I wouldn't lose sleep over it. 

</details>


<details>
<summary>
<b> Are reflection questions graded? How are they graded? </b>
</summary> <br>

Reflection questions are graded on our letter grade scale, with the exception that we do not assign the R- letter grade because we want to communicate that either a reflection question response was sufficient, or it was severely insufficient (and thus worth an L). Good responses are usually about a paragraph, with something like 7 or 8 sentences. Most importantly, please make sure your answer is specific to this class and your experiences in it. If your answer could have been edited lightly to apply to another class at Harvard, points will be taken off. Finally, remember that the lowest participation grade is dropped -- if you get an L on a reflection question it won't immediately affect your grade.

</details>

## SREs

<details>
<summary>
<b> How are SREs graded? I don't see my grade on Gradescope? </b>
</summary> <br>

SREs are graded on completion, as long as you submit a response that shows that you took the activity seriously. If you submitted the SRE reflection survey you will receive full credit for the SRE -- Gradescope is finicky about certain things so we can't actually get the 3/3 to show up on your end but you don't need to worry about that if you submitted the survey.

</details>

<details>
<summary>
<b> What if I have to miss a class? </b>
</summary> <br>

Here's the attendance policy:

- If you will be absent from a lecture which does not contain an SRE or an exam, you do not need us to excuse you -- as long as you have a valid reason, you're good to go.
- If you will be absent for any of the midterms, reach out to us ASAP so we can help you with scheduling a makeup (worst case if the makeup doesn't work either we'll have the final exam count for your entire exam GPA)
- If you will be absent from an SRE for something like sickness, mental health, personal issues, then please reach out to your Resident Dean or Faculty Dean and make sure that they are able to communicate that to the course heads (either they email us, or you email us with your resident or faculty dean cc'ed). In this case, a makeup isn't required, but we strongly recommend that you attempt to review the material on the SRE with a classmate.
- If you have another valid excuse for missing an SRE, but one that doesn't warrant reaching out to your Resident or Faculty Dean, please let us know by the lecture before so that we can help you organize a makeup. We recommend notifying us either by emailing the course heads, or through a private Ed post in the "Logistics" category. 
    - A makeup will be required - you will be finding a partner either by yourself or via a spreadsheet we will provide. Your SRE survey deadline on Gradescope will be extended by 3 days.
- Finally, maybe you overslept or missed the shuttle - this is a real problem for an exam, but if you do this on an SRE we provide one participation grade drop! As long as you don't do it multiple times, your participation grade will be perfectly fine.

</details>

## Exams

<details>
<summary>
<b> How do exams get curved? </b>
</summary> <br>

We determine curves by looking at exams and figuring out approximately which percentage thresholds should correspond to letter grade thresholds (i.e. the course heads will select exams that we believe are at the boundary between A-/B+, B-/C+, etc). Then, we set linear functions between the thresholds to determine your GPA based on your exam performance. Refer to the College description of letter grades [here](https://infoforfaculty.fas.harvard.edu/book/grading-system).

</details>

<details>
<summary>
<b> How much do exams count for? </b>
</summary> <br>

Your exam GPA will count for 50% of your final grade, and that portion is split between the midterms and final according to how long each takes (75 to 180 minutes). So each of midterms ends up being about 11.36% of your grade, and the final is about 27.27% of your grade.

</details>

