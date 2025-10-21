# Fall 2025 Course FAQ

We see a lot of the same questions popping up throughout the semester, and sometimes we make an Ed post answering these questions but people who don't read it at the time will usually come back with the same question a few weeks later. So instead we're going to start putting answers to these common questions on this webpage -- bookmark it and hopefully it'll be a useful resource for when you have questions!

## Lectures

### The Panopto recordings are too zoomed out to see anything -- how do I see the board?

Both the Panopto recordings and the DCE school recordings should both be available on the Canvas page under the "Panopto" and the "DCE Class Recordings" pages, respectively. In most cases the DCE Class Recordings will be strictly superior because they zoom in on the specific board that is being written on, but sometimes if you want to see the entire board checking out the Panopto recording might be a good idea.

### The DCE recordings focus on one board at a time -- how do I view the entire blackboard?

The Panopto recordings are a good option here! The text might be too small to take detailed notes but looking at the Panopto recording on the side can help give context to how different parts of lecture fit together.

### Where are the detailed lecture notes? What's the textbook?

This year, the detailed lecture notes are being replaced with the course textbook being written by Salil Vadhan and Adam Hesterberg (the two original professors of the course!). The links to textbook chapters can be found on the course website or the course schedule spreadsheet -- we encourage using the Perusall link when possible because it offers a good way to ask questions about the textbook or point out errors.

## Problem Sets

### How should I be testing my code?

For every problem set with code, there will also be some local testing functionality we provide for you to confirm that your code works as intended. We recommend using local test cases as a quick way of testing whether your code works -- if you upload your code to Gradescope it can take up to a minute to evaluate whether your code passes test cases, whereas if you run local tests it'll tell you within a second. Only after your code passes local tests cases should you upload it to Gradescope.

### Why do I pass local tests but not Gradescope tests?

One possible "hack" arises where a student could take a look at the test cases and hardcode some if statements to return the correct answer for those test cases (even if the code in general is incorrect). The solution here is that we include additional test cases on Gradescope so that even if the local tests get hardcoded Gradescope tests will expose errors. Therefore, even if your code passes local tests, it might not pass Gradescope tests. The ideal scenario is that local test cases should be thorough enough that any code which passes local test cases will pass Gradescope test cases as well, but sometimes due to oversight this won't be the case.

### Every proof of correctness is slightly different -- how do I know what to do?

First, it's worth noting that for exams proofs of correctness will usually follow very fixed structures that we cover in lecture / problem sets -- for example pretty much all correctness proofs on the final will just be for an NP-completeness or unsolvability proof which we'll drill. However, problem sets can require a little more adaptation.

In general this is a hard question to answer -- there's no formula for proving that an algorithm/reduction is correct, and I would say it's probably more accurate to say that correctness is a combination of pattern recognition (seeing when you can apply established techniques) and adaptation (recognizing when you need to adapt techniques to accommodate for edge cases / unique situations). Hopefully by doing the psets you've gained a little bit of both!

However, for this class we actually don't introduce that many new patterns. By outlining a few patterns + examples you'll probably be pretty well-equipped to tackle most things we throw at you. Here's a preliminary attempt at doing that:

- **Ad Hoc**: Sometimes (not often) you'll need to come up with a proof of correctness for an algorithm that doesn't follow a predetermined structure. Ad hoc means "created or done for a particular purpose as necessary" -- aka "you're kind of on your own"

    - **Size-Augmented Rotation**: I think this was problem 3b on pset 2 -- there's no precedent in class for proving correctness of a procedure for maintaining size-augmentation. I often pointed out in office hours that part of the proof of correctness is explaining why every node you don't update doesn't need to be updated -- this is something that you just have to figure out.

    - **Singleton Bucket Sort**: I got a few questions during this SRE about what correctness looks like for this algorithm. Here the two properties of a correct Sorting are 1) the answer is a permutation of the input, and 2) $K_i \leq K_{i+1}$. In this case you have to recognize that both can be proved directly with not that much effort.

    - One thing to note is that even though you're left on your own, usually the proof of correctness is a little bit easier and comes down to finding the 1 or 2 "core claims" that you need to justify.

- **Induction for Loops/Recursion**: 

    - **Recursion**: This is probably the one you're more used to (just remember to use strong induction)

        - **Merge Sort**: If this algorithm correctly sorts arrays of size $\frac{n}{2}$, then it will sort the full array of size $n$.

        - **Weighted QuickSelect**: If this algorithm can find the $t$'th element in the left or right subarray, then we'll get our answer for the entire array.

    - **Loops**: When an algorithm involves doing something in a loop, and the body of the loop is sufficiently complicated that it warrants an explanation of what you're doing at each step, you can consider a loop invariant.

        - **Insertion Sort**: we proved the claim that after $k$ iterations of the outer loop, the first $k$ elements of the array should be sorted (and this way the inductive step can focus on proving that the $k+1$-th iteration inserts the $k+1$-th element into the correct place)

        - **Radix Sort**: we proved the claim that after $k$ iterations of the outer loop, the elements of the array were sorted by their $k$ least significant digits. The inductive step used the stability of Singleton Bucket Sort to justify why numbers with the same $k+1$-th digit would remain in sorted order.

- **"Basic" vs "Advanced" Reductions**: I don't have a good definition of what a "basic" reduction is, but the main category we see in this class is reductions to Sorting. These are "basic" in the sense that the oracle is just a step that we abstract away for convenience, but the actual problem solving logic is contained in the reduction itself. For example, for AreaOfConvexPolygon we did all the complex area calculation in the reduction, whereas Sorting was just something convenient that we wanted as part of this routine. By contrast, an "advanced" reduction is more like an argument that the two computational problems are equivalent -- very soon after the midterm we'll see reductions to Single Source Shortest Paths which hint at this, and then we'll see the big NP-completeness and unsolvability reductions which really lean into this idea.

- **Correctness for "Basic" Reductions**: A proof of correctness for a basic reduction is usually very similar to an ad-hoc proof of correctness. 

    - **AreaOfConvexPolygon**: This is the main reduction to Sorting that we did on problem set 2 -- remember that the bar for correctness was pretty low because you just needed to explain why sorting is relevant (so that adjacent points are connected by an edge) and why your triangulation of choice was valid (a convex polygon containing the origin can be deconstructed into triangles at the origin).

- **Correctness for "Advanced" Reductions** (post-midterm): By contrast, a proof of correctness for an advanced reduction usually needs to argue for the equivalence of two problems. This pretty much always requires a bidirectional proof -- explaining that a solution for problem A corresponds to an equivalent solution to problem B and vice versa. You haven't seen any of these yet, so I'll give examples that will make more sense in the weeks after the midterm:

    - **Reductions to Single Source Shortest Paths**: Usually this kind of reduction involves an assumption that the original problem is equivalent to a graph that you've constructed as the input to SSSP. Usually the bidirectional proof here involves establishing a mapping from a sequence of moves in the original problem to a path of the same length on the constructed graph, and vice versa. By proving this mapping you demonstrate that the length of the shortest path on the constructed graph is equal to the length of the optimal sequence of moves in the original problem.

    - **NP-completeness Reductions**: This is an entirely different rabbithole we'll dive into later in the semester -- however, the core idea of establishing mappings between solutions still holds. In this case we want to show that a solution $S$ for $\Pi$ corresponds to an equivalent solution $S'$ for $\Gamma$, and vice versa.

    - **Unsolvability Reduction**: Again, bidirectional -- this time since it's between problems where the answer is yes/no it'll look more like if the answer for $\Pi$ is yes then the answer to $\Gamma$ is also yes, and vice versa.


### What's the level of formalism expected?

Salil answered this at the beginning of Lecture 8 on September 25th -- here's an attempt to summarize what he said:

There's a difference between **rigor** and **detail** in a proof. Rigor refers to the extent to which important statements are justified, whereas detail refers to the level of explanation given to each justification. For problem sets, we ask for rigor -- part of your task is to identify what justifications are necessary to prove the given statements. However, you don't need as much detail -- the TFs grading the problems sets are familiar with these justifications so as long as you identify the right claims and write down the correct justifications you don't need to write pages and pages explaining your justifications.

If you need a reference for how much detail in a proof is appropriate, looking at staff solutions for problem sets is a good idea. Keep in mind that sometimes the staff solutions will go into extra detail in order to provide extra context for students who were unable to solve the original problem -- sometimes you might not even need to match that level of detail.

### I can't tell whether my proofs are complete and always get marked down for missing something -- what do I do?

Luckily the revision video system makes it really easy to bounce back even if you forget a bunch of details in your proofs! Don't abuse the revision video system, but I think a really good system is just writing down a proof that you think feels complete, seeing what feedback we give, submitting a revision video if your pset grade takes a dip, and using that feedback to inform how you write future proofs. We don't expect perfect thorough proofs in every problem set, but we do hope that by submittign your best effort and revising up to an R if needed you get better over time at writing proofs!

### Where do I find my Gradescope feedback? How do I interpret it?

If you navigate to the assignment on Gradescope you can click through each problem to see what feedback you got, as well as the letter grade you got for a particular problem. Reading through the rubrics is important -- it can help you get an idea of what we expected to see from you in the proof. This can be particuarly helpful for exams, where sometimes you include some justification on the problem set but forget to include it on the exam when it's actually something we take off points for missing. Looking at problems where you got below an R and reading rubric items that indicate what we were looking for in a full-credit solution is a great way to understand what you're missing and where you should add more justification.

### How important is getting an R+?

The important thing to note is that getting all R's should be the primary goal, and having an R+ is nice but not necessary. Notice that according to the "Letter grades" section of the syllabus, an R- is equivalent to a 3, an R is equivalent to a 4, and an R+ is equivalent to a 4.33 on the 4.0 scale. Taking into account the 10 pset grades and problem sets being 45% of the overall grade, that means that going from an R to an R+ will net you a 0.015 increase in your overall class GPA -- assuming a uniform GPA distribution, the probability of this bump taking you across a grade cutoff is a little under 5%. So it might be worth going for the R+ if you have extra time, but I wouldn't lose sleep over it. For further context, I fiddled with some numbers and going from an R to an R+ is equivalent to getting approximately 1-2 additional points on the final exam.

### Are reflection questions graded? How are they graded?

Reflection questions are graded on our letter grade scale, with the exception that we do not assign the R- letter grade because we want to communicate that either a reflection question response was sufficient, or it was severely insufficient (and thus worth an L). Good responses are usually about a paragraph, with something like 7 or 8 sentences. Most importantly, please make sure your answer is specific to this class and your experiences in it. If your answer could have been edited lightly to apply to another class at Harvard, points will be taken off. Finally, remember that the lowest participation grade is dropped -- if you get an L on a reflection question it won't immediately affect your grade.

## SREs

### How are SREs graded? I don't see my grade on Gradescope?

SREs are graded on completion! If you submitted the SRE reflection survey you will receive full credit for the SRE -- Gradescope is finicky about certain things so we can't actually get the 3/3 to show up on your end but you don't need to worry about that if you submitted the survey.

### What if I have to miss a class?

Here's the attendance policy:

- If you will be absent from a lecture which does not contain an SRE or an exam, you do not need us to excuse you - as long as you have a valid reason, you're good to go.
- If you will be absent for the midterm, reach out to us ASAP so we can help you with scheduling a makeup (worst case if the makeup doesn't work either we'll have the final exam count for your entire exam GPA)
- If you will be absent from an SRE for something like sickness, mental health, personal issues, then please reach out to your Resident Dean and make sure that they are able to communicate that to the course heads (either they email us, or you email us with your resident dean cc'ed). In this case, a makeup isn't required, but we strongly recommend that you attempt to review the material on the SRE with a classmate.
- If you have another valid excuse for missing an SRE, but one that doesn't warrant reaching out to your Resident Dean, please let us know by the lecture before so that we can help you organize a makeup. Most people have been doing this by emailing the staff - from here on out, we recommend notifying us through a private Ed post in the "Logistics" category. 
    - A makeup will be required - you may either find another student in the class who will be missing the same SRE, or use this spreadsheet to find a partner from the extension school (the spreadsheet is normally used to pair up extension school students). Your SRE survey deadline on Gradescope will be the same as the one we assign to the extension school students (which is generally the rest of the week).
- Finally, maybe you overslept or missed the shuttle - this is a real problem for an exam, but if you do this on an SRE we provide a participation grade drop! As long as you don't do it multiple times, your participation grade will be perfectly fine.

## Exams

### How do exams get curved?

We determine curves by looking at exams and figuring out approximately which percentage thresholds should correspond to letter grade thresholds (ie the course heads will select exams that we believe are at the boundary between A-/B+, B-/C+, etc). Then, we set linear functions between the thresholds to determine your GPA based on your exam performance

### How much do exams count for?

Your exam GPA will count for 40% of your final grade, and that portion is split between the midterm and final according to how long each takes (75 to 180 minutes). So the midterm ends up being about 11.75% of your grade, and the final is about 28.25% of your grade.