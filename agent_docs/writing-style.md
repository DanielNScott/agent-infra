# Scientific Writing Style Guide

Preferences derived from four papers: an empirical aging/foraging study (npj Aging, 2025), an invited opinion-turned-review on thalamocortical function (Trends in Cognitive Sciences, 2024), a comprehensive review of metaplasticity (Neuropsychopharmacology, 2023), and a theory/simulation paper on plasticity and continual learning (eLife, 2024). These represent distinct genres with different structural demands; observations below are annotated accordingly.

Style emphasizes confident, precise exposition with long, information-dense sentences held together by clear logical connectives. Argumentation proceeds by bridging across scales or domains, setting up competing hypotheses, and adjudicating with evidence. Register is formal academic without stiffness; hedging is selective and calibrated rather than reflexive. First-person plural throughout; no contractions or colloquialisms.

Organization uses explicit roadmaps, descriptive-claim section headers, topic-sentence discipline in every paragraph, and summary recapitulations at section boundaries. Concepts are introduced via concrete analogy and graduated specificity.

## Table of Contents
- [Genre Distinctions](#genre-distinctions)
- [Citations](#citations)
- [Sentence Architecture](#sentence-architecture)
- [Paragraph Structure](#paragraph-structure)
- [Section and Document Organization](#section-and-document-organization)
- [Argumentation and Reasoning](#argumentation-and-reasoning)
- [Conceptual Exposition](#conceptual-exposition)
- [Hedging and Confidence](#hedging-and-confidence)
- [Vocabulary and Diction](#vocabulary-and-diction)
- [Improvement Targets](#improvement-targets)
- [Agent Pitfall Anti-patterns](#agent-pitfall-anti-patterns)

---

## Genre Distinctions

The four source papers represent different genres, and some stylistic patterns are genre-dependent. Distinguishing universal habits from genre-specific ones prevents overgeneralizing from one paper to another.

### Opinion-turned-review (TICS thalamocortical piece)

This paper was written thesis-first from the start. It has the strongest structural organization: sustained analogies, clean roadmaps, claim-based headers. The entire paper functions as a continuous argument, so the "discussion" problem barely arises -- the whole paper is a discussion. This genre permits and rewards the most ambitious rhetorical structure.

### Comprehensive review (Neuropsychopharmacology metaplasticity piece)

A genuine review must cover a field thoroughly, which pulls the writing in more directions than a thesis-driven piece. The longer, harder-to-parse sentences in this paper partly reflect the genre's demand for thoroughness over territory the author does not fully control narratively. Summary recapitulations at section boundaries do heavy lifting precisely because sections cannot be as thesis-driven. Subsection headers name circuit-function pairings rather than asserting claims, because the subsections survey rather than argue.

### Empirical article (npj Aging foraging piece)

Results sections are tightly organized because they follow the analysis pipeline -- this is genre-native, not a special achievement. Discussion sections must address multiple possible interpretations of the results, which creates a structural challenge: drifting between sub-topics (dopamine, perseveration, depression, apathy) without the claim-then-evidence structure the results use. This is the weakest genre for the author's strengths, and the paper reflects that.

### Theory/simulation article (eLife coordinated eligibility piece)

Theory papers with simulations occupy a middle ground between opinion/reviews and empirical articles. The Results section must carry both mathematical derivations and simulation descriptions, which creates a dual organizational demand: the math must build an argument, while the simulations must be described procedurally. Claim-based section headers work naturally here because each simulation demonstrates a specific claim. The introduction faces a challenge distinct from the other genres: it must motivate the theory, relate it to biology, and preview the simulations, without the luxury of empirical results to anchor predictions against. Discussion sections must address both the mathematical contributions and biological plausibility, which can produce the same drift seen in empirical articles.

### Which patterns are universal vs. genre-specific

Universal across genres:
- Declare-then-unpack sentence structure
- Topic-sentence discipline
- Calibrated hedging
- Inline quantitative precision (empirical sections)
- Formal vocabulary mixed with plain phrasing
- Semicolons, em-dashes, and parenthetical qualifiers
- No contractions, colloquialisms, or first-person singular

Strongest in opinion/review genres, less natural in empirical articles:
- Claim-based section headers
- Sustained analogies
- Explicit structural roadmaps
- Summary recapitulations at section boundaries

Strongest in theory/simulation articles, shared with opinion/reviews:
- Claim-based section headers in Results
- Concrete analogies to ground mathematical abstractions
- Explicit connections between formal results and biological mechanisms

---

## Citations

When citing articles in scientific writing, please verify, by consulting surrounding context and the precise claims being made and cited, that articles being cited directly address the claims, rather than merely being topical.

---


## Sentence Architecture

Sentences are long and information-dense, carrying multiple pieces of information joined by semicolons or subordinate clauses. Clarity comes from logical connectives, not from brevity.

### Declare-then-unpack

The signature move is a crisp declarative sentence followed by one that unpacks or qualifies it. The first sentence does the work; the second explains.

Correct:
> Metaplasticity co-opts the plasticity discussed above, generalizing Hebbian change by making it conditional. In the simplest case this means gating plasticity, such that it only happens under certain circumstances but is unchanged in form.

Anti-pattern -- frontloading qualification before the reader knows the claim:
> Although it is only one of several possible interpretations and the evidence remains mixed, it may be the case that metaplasticity could potentially co-opt plasticity in some circumstances.

### Semicolons as paragraph glue

Semicolons link related independent clauses within a single sentence, keeping ideas tightly bound. This creates a flowing, lecture-like rhythm.

Correct:
> On the one hand, these systems need to be highly expressive, in that they can potentially produce numerous possible behaviors; on the other hand, they must be highly efficient, learning from limited data and switching between behaviors rapidly.

Anti-pattern -- choppy short sentences that fragment a unified idea:
> These systems need to be highly expressive. They can potentially produce numerous possible behaviors. On the other hand, they must be highly efficient. They need to learn from limited data. They also need to switch between behaviors rapidly.

### Em-dashes for inline parentheticals

Clarifying asides use em-dashes rather than parentheses, adding technical precision mid-sentence without breaking flow.

Correct:
> Fourth, overstaying can be explained by perseveration--whether cognitive or motor--that is, the inappropriate, or in this case suboptimal, prolongation of behaviours.

Correct:
> These low-dimensionality benefits may be softly imparted on high-dimensional networks via regularization--a process closely related to concepts from Bayesian models--because fixing context information reduces the complexity of other computations.

Anti-pattern -- nested parentheses that force the reader to track bracket depth:
> These benefits may be imparted via regularization (a process related to Bayesian models (because fixing context information (which reduces complexity) simplifies other computations)).

### Mathematical-to-biological bridging sentences

In theory papers, the transition from a mathematical result to its biological interpretation is a critical sentence. The pattern is: state the formal result, then immediately name its biological correlate using "because" or an appositive.

Correct (from the coordinated eligibility paper):
> This representation of the gradient is striking in relation to neuroscience, because the x vector denotes how a given neuron's inputs should be re-weighted (i.e., plasticity of dendritic processes and receptive fields), whereas the g vector denotes how a layer of neurons' collective output is changed (i.e., plasticity of population response patterns).

This sentence does three things in sequence: names the formal object (x and g vectors), identifies the biological correlate (dendritic processes, population responses), and uses parenthetical glosses to make the mapping explicit.

Anti-pattern -- leaving the biological interpretation implicit:
> The gradient decomposes into an outer product of two vectors, x and g.

The reader must independently supply the biological relevance.

### Short sentences as emphatic punctuation

Short sentences are rare and serve as conclusions after long build-ups, or as pivots between arguments.

Correct:
> Many of the studies that we have discussed position the thalamus as exactly the type of low-dimensional controller that could be used to compositionally recruit cortical networks according to context, while simultaneously allowing the cortex to carry out complex computations that power our cognition. All these possibilities are testable.

Anti-pattern -- scattering short sentences throughout, destroying the density of the argument:
> The thalamus may be a controller. It is low-dimensional. It could recruit cortical networks. The cortex carries out complex computations. These ideas are testable.

---

## Paragraph Structure

### Topic-sentence discipline

Every paragraph opens with a sentence that states the paragraph's claim or purpose. The remainder provides evidence, elaboration, or qualification.

Correct:
> Overstaying behaviour therefore had two components: a baseline stay duration offset (relative to the optimal set of stay durations), and a condition-difference exaggeration component. Examining this decomposition further, we computed participant's offset components by...

Anti-pattern -- burying the topic sentence mid-paragraph:
> We computed participant's offset components by taking mean stay durations. We also computed their scale components by projecting mean-subtracted stay durations. Overstaying behaviour therefore had two components: a baseline stay duration offset and a condition-difference exaggeration component.

### Transition sentences at paragraph boundaries

Paragraphs begin with backward-looking connectives that create a continuous argumentative thread.

Examples of correct opening phrases:
> "Building on the facts outlined earlier, we synthesize..."
> "In line with these predictions, L-type calcium currents contribute to plasticity..."
> "To summarize, Bayesian accounts indicate how complex beliefs should be updated..."
> "Complementing these findings, recent work has demonstrated..."

Anti-pattern -- paragraphs that begin without connecting to what preceded them:
> L-type calcium currents contribute to plasticity in a number of ways.

This version forces the reader to reconstruct the logical connection.

### Summary recapitulation at section boundaries

Major sections end with explicit summary paragraphs that restate key points before moving on. These may be labeled ("Summary of cellular and molecular data") or unlabeled but clearly serve that function. This device is most important in comprehensive reviews, where sections cover diverse territory and the reader needs regular footholds. It is less critical in opinion/reviews where the argument is continuous, and least natural in empirical articles where the results speak sequentially.

Correct:
> To recap, basic theories of unconditional Hebbian plasticity qualitatively account for various phenomena. They predict that feed-forward neural pathways, such as thalamo-cortical connections, should develop feature detectors. Local recurrence, as seen between L4 or L2/3 principal neurons, should enhance bidirectional connectivity among similarly tuned neurons, insofar as plasticity reflects symmetric Hebbian rules.

Anti-pattern -- ending a section by trailing off into the next topic without recapitulation:
> ...and these non-classical STDP kernels remain poorly understood. Anyway, metaplasticity makes Hebbian updates conditional.

### Logical connectives in dense summary paragraphs

When a paragraph must convey multiple findings compactly (e.g., a results roadmap or a discussion opening), each sentence should connect to the previous one via a connective that names the logical relationship and its content. Without these connectives, the paragraph reads as a list of independent claims; with them, it reads as a single argument whose steps build on each other.

Three principles govern the revision:

1. The topic sentence states the paragraph's overall claim, so that the reader knows what the subsequent findings are evidence for.
2. Each subsequent sentence opens with a phrase that links it to the preceding one: "These primary measures are also reliable" (extends validity to reliability), "Parameter recovery corroborates this pattern" (independent evidence for the same claim), "Finally" (signals closure).
3. Semicolons join closely related clauses within a single logical step, keeping the step count down without losing information.

Anti-pattern -- a list of findings with no connective tissue:

> PCA of peri-changepoint learning rates and linear regression with normative regressors recover the same dominant axis of individual variation; how strongly subjects modulate their learning rates in response to change-points. Subspace overlap analysis confirms this alignment (Figures 1--3). Split-half analyses across three independent datasets demonstrate that the primary PCA score and CPP regression coefficient are reliably estimated, while higher-order components are not (Figure 4). Parameter recovery reveals near-perfect recovery correlations but structured estimation error whose magnitude depends on subject parameters (Figures 5--6). Centered-regressor models reduce this error and improve reliability without sacrificing fit (Figure 7), alternative cognitive models produce distinguishable behavioral signatures (Figure 8), and regressor collinearity -- driven by changepoint density and run-length variability -- is a stronger determinant of estimation precision than observation noise, with intermediate changepoint rates and moderate run-length variability minimizing estimation error (Figure 9).

Each sentence reports a finding, but the reader must infer how they relate. The paragraph feels like a bulleted list in prose clothing.

Correct -- the same findings with a topic sentence and logical connectives:

> Change-point task analyses yield valid, reliable, and precise individual-difference measures whose quality depends on identifiable analysis and design choices. PCA of peri-changepoint learning rates and linear regression with normative regressors recover the same dominant axis of individual variation, quantifying how strongly subjects modulate their learning rates in response to change-points; subspace overlap analysis confirms this alignment (Figures 1--3). These primary measures are also reliable: split-half analyses across three independent datasets demonstrate consistent PCA scores and CPP regression coefficients, while higher-order components are not stable (Figure 4). Parameter recovery corroborates this pattern, showing near-perfect recovery correlations alongside structured estimation error whose magnitude depends on subject parameters (Figures 5--6). Centered-regressor models reduce this error and improve reliability without sacrificing fit (Figure 7), and alternative cognitive models produce distinguishable behavioral signatures that support construct validity (Figure 8). Finally, regressor collinearity, driven by changepoint density and run-length variability, is a stronger determinant of estimation precision than observation noise, with intermediate changepoint rates and moderate run-length variability minimizing estimation error (Figure 9).

The topic sentence ("valid, reliable, and precise ... whose quality depends on ... choices") frames all six findings as evidence for a single claim. "These primary measures are also reliable" extends the validity finding to reliability. "Corroborates this pattern" ties parameter recovery back to the preceding reliability result. "Finally" signals the last step. No information was added or removed; the only changes are the topic sentence and the connective phrases.

---

## Section and Document Organization

### Explicit roadmaps in introductions

Introductions end with a paragraph previewing the paper's structure. These enumerate sections or arguments in order.

Correct:
> Concretely, the logic of our review proceeds as follows: (1) Calcium and related signalling cascades are key regulators of Hebbian post-synaptic plasticity, and diverse processes impact both. This makes those processes, in part, plasticity controllers, and we review some of their key elements; (2) Hebbian learning algorithms have long been addressed by computational theories... we review these points; Lastly, (3) different brain areas are specialized and this should be reflected in terms of the metaplasticity they express.

Anti-pattern -- an introduction that ends with a vague gesture:
> In this review, we discuss these topics in detail.

### Results roadmaps as argument previews

When a Results section contains multiple subsections, a brief opening paragraph can orient the reader. This paragraph should preview the claims each section establishes, not describe the activities the authors performed.

Correct (rewritten from the coordinated eligibility paper):
> We first show that weight gradients decompose into population-response and receptive-field factors, and that both must overlap for interference or generalization to occur. We then demonstrate that coordinating these factors via metaplasticity can eliminate catastrophic interference while preserving the ability to generalize.

Anti-pattern -- procedural roadmap that describes activities rather than claims (from the coordinated eligibility paper):
> We present our results in a mathematical section and several simulation sections. In the mathematical section we define our basic neural network model and we ask how interference and generalization between tasks are related to weight changes. We find that we can decompose interference and generalization according to "receptive field" (RF) and "population response" (PR) factors of plasticity for each neural network layer.

The anti-pattern tells the reader what the authors did (define, ask, find, decompose) rather than what the results establish. The correct version states conclusions the reader can hold in mind while reading.

### Section headers as claims

Section headers assert the section's conclusion, not merely its topic. This is consistent across opinion/review articles. In comprehensive reviews covering distinct sub-literatures, subsection headers may name a specific topic pairing (e.g., "Amygdala and memory allocation") rather than asserting a conclusion, because the subsection surveys rather than argues. In empirical articles, conventional headers (Introduction, Results, Discussion) dominate.

**Exception: infrastructure subsections.** When a subsection describes data, methods, or other content that is not itself a finding but is necessary for the manuscript to be complete, use a descriptive noun-phrase header naming the content (e.g., "Synthetic benchmarking data", "Programmatic question generation"). Claim-based headers are wrong here because there is no claim — the section exists to inform, not to argue. Apply claim-based headers only to sections whose content constitutes findings or results.

Correct:
> "MD exhibits low-dimensional representations key for efficient learning"
> "Metaplasticity makes Hebbian updates conditional"
> "Controlling plasticity dictates key network properties"

Anti-pattern:
> "Low-dimensional representations"
> "Metaplasticity"
> "Network properties"

These label the topic but do not communicate the argument.

### Subsections via bold subheadings

Within major sections, bold or italic subheadings provide finer-grained organization. In the metaplasticity review, the Architectural Specialization section contains subheadings like "Amygdala and memory allocation", "Hippocampus, pattern separation and pattern completion", and "Corticostriatal circuits and task-rule gating". Each names a specific circuit-function pairing.

---

## Argumentation and Reasoning

### Cross-scale bridging as the core rhetorical move

All four papers are organized around connecting disparate literatures or levels of analysis. This bridging is framed explicitly as the paper's contribution.

Correct:
> We examine connections between these areas, asking how network computations change as a function of diverse features of plasticity and vice versa.

Correct:
> Here, we review evidence that thalamocortical architectures may have evolved to facilitate these objectives of flexibility and efficiency by coordinating distributed computations.

Anti-pattern -- reviewing two literatures in sequence without articulating the bridge:
> First we review plasticity biology. Then we review network computation. Both are important.

### Competing hypotheses presented and adjudicated

Arguments frequently set up two or more competing explanations, present evidence for each, and indicate which the data support.

Correct:
> Previous research showing increased sensitivity to the opportunity cost of time in older adults predicts less overstaying, whereas a hypothesised shift towards exploitative behaviour predicts more overstaying. In an online foraging task, 350 young and older adults decided when to switch... Our findings show ageing is associated with exaggerated overstaying, supporting increased exploitative behaviour in old age.

Anti-pattern -- presenting only the winning hypothesis:
> We hypothesized that older adults would overstay, and they did.

This obscures the reasoning and fails to acknowledge alternatives.

### Naming falsifying conditions and alternative explanations

Strong arguments state what would disprove the interpretation, or what alternative accounts exist.

Correct:
> Several alternatives to the regularization synthesis presented here are possible. The simplest and most likely alternative is that there is little overarching logic to frontal function. Instead, frontal thalamocortical properties may reflect several independent kludges, each incompletely tailored to an important task, with little rationale.

Anti-pattern -- omitting alternative explanations entirely, leaving the reader to generate them.

### Inline quantitative precision

In empirical writing, statistics are woven directly into prose with exact values, not relegated to tables or appendices.

Correct:
> A linear mixed effect model confirmed that older adults stayed more overall (beta = 0.075, SE = 0.018, t(15326) = 4.184, p = 2.9e-5), and showed a small but significant decay rate x age interaction (beta = 0.012, SE = 0.006, t(15326) = 1.98, p = 0.048).

Anti-pattern -- vague qualitative claims:
> Older adults stayed significantly longer (p < 0.05).

---

## Conceptual Exposition

### Extended concrete analogies

Abstract concepts are introduced through extended analogies that run across multiple paragraphs and figures. These ground formal ideas in everyday experience. This technique is strongest in the opinion/review genre (the TICS restaurant/chef analogy) and underused in the comprehensive review, where the hardest conceptual transitions would benefit from it most (see [Improvement Targets](#improvement-targets)).

Correct (the restaurant/chef analogy for Bayesian inference, sustained over four paragraphs):
> For example, one might infer the quality of a restaurant (a latent variable) based on meals experienced there (observations). We might assume that individual meals provide a sense of the chefs' abilities, but that these slowly change over time, and that individual meals may be noisy observations...

> Alternatively, one could have a more complex model... One could have a substandard meal, infer that their favorite chef has quit, and avoid that restaurant completely in the future.

Anti-pattern -- introducing Bayesian inference with equations alone, or with a one-sentence analogy that is dropped immediately.

### Definitions via apposition

Technical terms are defined inline with an appositive phrase on first use, avoiding footnotes or separate definition sections.

Correct:
> Regularization (meaning 'complexity reduction', or 'making things simpler')

Correct:
> ...a set of operations referred to as executive functions, which collectively exert cognitive control

Anti-pattern -- using jargon without definition:
> Regularization in the MD constrains PFC dimensionality.

### Concrete analogies to motivate simulations

When a simulation is designed to test an abstract principle, a concrete analogy before the simulation description grounds the reader's intuition. The analogy should name real-world objects and actions, then map them to the simulation's formal structure.

Correct (from the coordinated eligibility paper, coarse-coding section):
> To motivate this situation, consider the case of object affordances. Many classes of objects are loosely defined by their uses, such that (for example) the category of mugs is a set of things one drinks from. Such uses create natural categories for generalizing learning. If we interpret a target network output as an action, use, or label, then the inputs which should prompt a given output can often be inferred by learning the input transformations which the target output is invariant to.

This analogy runs for a full paragraph before transitioning to the simulation with "In analogy with this example, we simulated a continual learning problem in which object classes had (by definition) the same target outputs."

Anti-pattern -- jumping directly to simulation parameters:
> We simulated a continual learning problem with 80 tasks, 100-dimensional inputs, and 20-dimensional targets using two readout heads.

Without the mug analogy, the reader has no intuition for why coarse-coding over receptive fields should promote generalization.

### Graduated specificity

Concepts are introduced at a general level, then progressively refined with increasing detail in subsequent sentences or paragraphs.

Correct progression:
1. "Plasticity can be controlled at synapses by calcium dynamics and neuromodulatory signals."
2. "Calcium entry leads to a number of signalling cascades, three of which we refer to here as the CaM-CaMKII pathway, AC-cAMP-PKA pathway, and the PLC-DAG-PKC pathways."
3. "Each molecule in these cascades is involved in multiple processes, but the kinases CaMKII, PKA, and PKC contribute to plasticity in significant part by phosphorylating AMPARs..."

Anti-pattern -- jumping to maximum specificity:
> CaMKII phosphorylates GluA1 subunits at Ser831, increasing single-channel conductance.

Without establishing the broader context, the reader cannot place this fact.

---

## Hedging and Confidence

### Calibrated hedging

Hedge when the evidence is genuinely uncertain. Make direct statements when it is clear. The hedging should feel calibrated to the actual state of knowledge.

Correct -- hedging for genuine uncertainty:
> Such a tendency would suggest reduced, rather than heightened sensitivity to opportunity cost of time.

Correct -- confidence for clear evidence:
> Participants consistently overstayed, and this behaviour was strongly associated with sensitivity to reward changes.

Anti-pattern -- reflexive hedging on established facts:
> It may potentially be the case that participants might have possibly overstayed to some extent.

### Signal words for emphasis

"Importantly", "Notably", "Interestingly" flag claims of special significance. Use sparingly and only when the claim genuinely warrants it.

Correct:
> Importantly, compared to optimal behaviour, most participants exhibited overstaying behaviour, and this had a substantial impact on total reward in the task.

Anti-pattern -- overusing signal words until they lose force:
> Importantly, we recruited participants. Notably, they completed the task. Interestingly, we analyzed the data.

---

## Vocabulary and Diction

### Formal vocabulary mixed with plain phrasing

Latinate and formal vocabulary ("instantiate", "adjudicate", "precipitate", "recapitulate") appears naturally alongside plainer phrasing. The mix keeps the text accessible without sacrificing precision.

Correct:
> This retroactive expression is also important for computational models of metaplasticity and may relate considerably to empirical "consolidation" and "synaptic tag and capture" ideas, although there has been little integrated consideration of these observations thus far.

Anti-pattern -- all plain phrasing, losing precision:
> This is also important for models and may be related to other ideas about how memories stick around.

Anti-pattern -- all Latinate, losing accessibility:
> This retroactive instantiation is also consequential for computational formalizations of metaplasticity and may relate substantively to empirical consolidation and synaptic tagging paradigms.

### Pronoun "this" as a forward reference

"This" frequently refers to the entire preceding claim or phenomenon, not just a single noun. This is a deliberate connective device.

Correct:
> This makes those processes, in part, plasticity controllers.

Correct:
> This suggests that overstaying tendency cannot be simply explained by a reduced attention to the task.

### Restatement with "That is" and "i.e."

Claims are often restated in more concrete terms immediately after being made.

Correct:
> In the simplest case this means gating plasticity, such that it only happens under certain circumstances but is unchanged in form. A more complicated situation involves both gating plasticity and modulating its sign, i.e. converting LTP to LTD or vice versa.

### Parenthetical qualifiers

Short parenthetical clarifications appear frequently: "(at least)", "(but far from all)", "(but see ref. X)", "(meaning...)". These are natural and non-disruptive.

Correct:
> ...recapitulates much (but far from all) empirical synaptic data.

### No contractions, no colloquialisms, no first-person singular

Register is consistently formal academic. "We" is standard for the authors. "I" does not appear. Contractions ("don't", "it's") do not appear.

### Lists in prose form

When enumerating items, numbered inline lists ("(1)... (2)... (3)...") or sequential connectives ("First,... Second,... Third,...") are used. Bullet-point lists do not appear in body text.

Correct:
> These include both pre- and postsynaptic modification, as well as intracellular alterations that interact with extracellular signals (e.g., neuromodulation via G-protein coupled receptors).

Anti-pattern -- bullet lists in body text:
> Plasticity involves several mechanisms:
> - Pre-synaptic modification
> - Post-synaptic modification
> - Intracellular alterations

---

## Improvement Targets

Known weaknesses, identified by comparing the four papers against the style principles above. These are areas where the writing falls short of its own standards.

### Sentence-level tautology and redundancy

Occasional sentences end by restating what they began with, adding no information. This tends to occur in discussion sections where summary pressure is high. The fix is ensuring each clause in a long sentence advances the idea rather than circling back to it.

Example of the problem (from the foraging paper):
> Such 'overstaying' may reflect uncertainty about the environment, leading to an adaptive discounting of future reward and, hence, overstaying.

The sentence defines overstaying, explains its cause, and then concludes with the word "overstaying" -- arriving back where it started. A revision would replace the final word with the consequence or implication.

### Grammatical complexity exceeding conceptual complexity

Long, multi-clause sentences are a core strength. But occasionally a sentence accumulates enough subordinate clauses that the reader must re-read to parse grammar, even when the ideas are clear. This is most pronounced in the metaplasticity review, where the material demands more qualification per claim. The genre partly explains this: a comprehensive review forces thoroughness that an opinion piece does not. The improvement is not "write shorter sentences" but "identify when grammatical complexity exceeds conceptual complexity" -- when qualification serves thoroughness rather than the idea.

### Discussion sections as the weakest structural link

Discussion quality varies by genre, but in all cases discussions are less disciplined than the sections preceding them.

In empirical articles, the problem is drift. The foraging paper's discussion handles competing interpretations but wanders between sub-topics without the topic-sentence discipline the results use. The improvement is to give each interpretation its own sub-argument -- a mini paragraph with a topic sentence, supporting evidence, and a verdict -- rather than weaving interpretations together in a single discursive passage.

In comprehensive reviews, the problem is different: the discussion must synthesize the synthesis, which is inherently harder. Discursiveness is more forgivable here, but the summary recapitulations that work well at section boundaries within the paper should also structure the discussion itself.

In opinion/reviews, the problem barely arises because the entire paper is argumentative.

### Uneven analogy deployment

The TICS piece uses sustained analogy effectively. The metaplasticity review, covering arguably harder material, relies on graduated specificity alone. Some of the hardest conceptual transitions in that paper -- from calcium dynamics to network-level consequences, from Hebbian rules to reinforcement learning -- would land better with concrete anchoring examples. The improvement is not "always use analogies" but "use analogies at the hardest conceptual transitions, regardless of genre and audience specialization."

### Procedural roadmaps instead of argumentative previews

Roadmap paragraphs sometimes describe the paper's activities (what the authors did) rather than its claims (what the results establish). This is especially tempting in theory/simulation papers where the workflow is complex. See also [Results roadmaps as argument previews](#results-roadmaps-as-argument-previews) for the correct pattern.

Anti-pattern (from the coordinated eligibility paper):
> We present our results in a mathematical section and several simulation sections. In the mathematical section we define our basic neural network model and we ask how interference and generalization between tasks are related to weight changes.

Revised:
> Our mathematical results establish that interference and generalization between tasks depend on the overlap of two biologically distinct gradient components: population-response and receptive-field factors. Our simulations then demonstrate that coordinating these factors via unsupervised metaplasticity can eliminate catastrophic interference (simulations 1-2), promote generalization (simulations 3-4), and enable compositional learning (simulation 5).

The revision states results as conclusions rather than activities.

### Missing recapitulations between result groups

When a Results section contains logically distinct groups of results (e.g., a mathematical section followed by simulations, or pattern-separation simulations followed by coarse-coding simulations), the boundary between groups needs a recapitulation sentence or paragraph that summarizes what has been established before introducing the next group.

Anti-pattern -- transitioning between result groups without recapitulation (from the coordinated eligibility paper):
> [End of simulation 2 results]... As with our previous simulations, we note that we obtained similar results in reinforcement learning simulations (also discussed in the appendices).
>
> **Coarse-coding receptive field plasticity generalizes learning**
> A network that perfectly pattern separates all learning will completely avoid interference, at the potential cost of also removing positive transfer between tasks (i.e., generalization).

The transition jumps from one result group to the next without consolidating the pattern-separation findings.

Revised:
> Together, the previous two simulations demonstrate that pattern-separating either receptive-field or population-response plasticity can eliminate catastrophic interference, by confining each task's weight changes to orthogonal subspaces. However, perfect separation removes not only destructive overlap between tasks but also constructive overlap -- that is, generalization.
>
> **Coarse-coding receptive field plasticity generalizes learning**
> [continues as before]

### Disclaimers that interrupt argumentative momentum

Sentences that disclaim something the reader has not yet been led to expect break the argument's flow. These typically appear as "Notably, X is not our goal" or "We do not claim Y" before Y has been introduced as a possibility.

Anti-pattern (from the coordinated eligibility paper):
> Notably, determining when and where to apply different sorts of metaplasticity is not our goal.

This sentence appears in the Results roadmap, before the reader has had reason to expect that metaplasticity selection would be a goal. The disclaimer preempts a question the reader has not asked.

Revised -- move the disclaimer to where it is relevant, and frame it as a scope decision rather than a negation:
> Our simulations use fixed metaplasticity rules to isolate the geometric properties of coordinated eligibility; the question of how biological networks select among metaplasticity strategies is a separate problem we address in the discussion.

### Abstracts that bury the headline result

Abstracts sometimes introduce the framework and enumerate its properties without ever stating the central finding in a single, direct sentence. The headline result should appear as a crisp declarative claim, not distributed across several clauses.

Anti-pattern (from the coordinated eligibility paper, paraphrased):
> We found that plasticity between groups of neurons can be decomposed into biologically meaningful factors, with factor geometry controlling interference and generalization. We introduce a "coordinated eligibility theory" in which plasticity is determined according to products of these factors, and is subject to surprise-based metaplasticity. This model computes directional derivatives of loss functions, which need not align with task gradients, allowing it to protect networks against catastrophic interference and facilitate generalization.

The central claim -- that coordinating plasticity factors can simultaneously prevent interference and promote generalization -- is distributed across three sentences and never stated crisply.

Correct pattern (cf. the foraging paper's abstract):
> Our findings show ageing is associated with exaggerated overstaying, supporting increased exploitative behaviour in old age.

A revision of the coordinated eligibility abstract would include a sentence like: "We show that coordinating these factors via surprise-based metaplasticity prevents catastrophic interference while enabling generalization, outperforming gradient descent in continual learning."

### Thin transitions

Transition sentences sometimes specify the logical relationship (agreement, addition, contrast) without specifying the content. "In line with these predictions" and "Complementing these findings" tell the reader the relationship but not what is being connected.

Weak transition:
> Complementing these findings, recent work has demonstrated the utility of uncertainty-based regularization in neural networks.

Stronger transition:
> Building on the facts outlined earlier, we synthesize several additional lines of evidence suggesting that MD-PFC loops function to balance expressiveness and efficiency.

The stronger version names what is being built on and where the argument is going. This problem appears across genres but is worst in the comprehensive review, where subsections cover distinct biological territory and the connections between them are genuinely looser.

---

## Agent Pitfall Anti-patterns

### Excessive hedging

Calibrate hedging to the actual evidence. Well-established findings get direct statements; genuinely uncertain interpretations get hedges.

Anti-pattern:
> It could potentially be argued that the results may suggest a possible role for dopamine in potentially modulating certain aspects of plasticity.

Correct:
> Dopamine has been suggested to control responsiveness to reward in the decision to switch.

### Filler transitions

Every transition should carry information and connect specific claims. Do not write transitions that name only the logical relationship (addition, contrast) without naming the content.

Anti-pattern:
> Moving on, let us now consider another important aspect of this topic.

Correct:
> Complementing these findings, recent work has demonstrated the utility of uncertainty-based regularization in neural networks.

### Flattened argument structure

Each paragraph should advance a claim, not list facts in sequence. State the claim first, then support it with evidence.

Anti-pattern:
> The PFC has ventral, medial, and lateral subdivisions. The MD receives inputs from multiple PFC regions. MD neurons have widespread projections. The MD is smaller than the PFC.

Correct:
> The structural and functional properties of the MD thalamus suggest that it compresses information from multiple prefrontal areas into local, low-dimensional, demixed representations. Specifically, the MD receives driving inputs from multiple PFC regions and, because it contains many fewer neurons than the PFC, there is substantial corticothalamic convergence.

The correct version builds a claim (compression), then supports it with structural evidence (convergence from many-to-few).

### Premature summarization

Place summaries at section boundaries after evidence has been presented, not before.

Anti-pattern:
> In summary, the thalamus is important for cognition. There are several reasons for this. First...

Correct:
> The PFC is necessary for implementing cognitive control, but not sufficient. Lesions to MD produce deficits similar to frontal lesions... [evidence developed over several paragraphs] ... Taken together, these observations of convergence and low dimensionality suggest that MD represents a small number of context variables.

### Symmetry-based transitions

When consecutive sections present analogous results, name what the new section adds and why it matters distinctly. Do not merely note the analogy.

Anti-pattern:
> As with pattern separation, pattern completion (or coarse-coding) can also be applied over population responses.

Correct:
> Pattern separation eliminates interference by confining each task to orthogonal subspaces, but this also prevents constructive transfer. The complementary operation -- coarse-coding population responses -- can selectively merge subspaces to promote generalization between related tasks.

### Stopping at category labels without expanding the mechanism

Naming the category a method belongs to is fine; follow through with concrete mechanistic detail. Do not list categories and move on.

Anti-pattern:
> An alternative family of approaches compiles graph-structural information into the embedding space itself -- either by enriching vector representations with neighborhood context, or by learning joint embeddings that encode both semantic content and topological position.

This lists two categories but expands neither.

Correct:
> An alternative family of approaches, which we introduce here, bring graph-structural information into the embedding space itself. The simplest such method involves selecting related embeddings from the neighborhood of each vector-embedded graph component and aggregating these (for example via averaging), then storing the aggregate as an alternative embedding. This process increases the cosine similarities of structurally related, lexically dissimilar items.

Name the family, then expand at least one member with the concrete operation and its direct effect.

### Allocating prose proportional to background rather than contribution

Compress background; expand the novel contribution. Prose space should be proportional to originality.

Anti-pattern (three sentences on background, one on contribution):
> Knowledge graph systems address this gap by maintaining explicit entity-relationship structure alongside vector stores, enabling graph traversal at query time. However, maintaining a live graph database introduces infrastructure complexity, latency, and coupling between the retrieval layer and the storage backend. An alternative family of approaches compiles graph-structural information into the embedding space itself. These offline strategies promise the retrieval simplicity of pure vector search with some of the structural awareness of graph traversal.

Correct (one clause on background, three sentences on contribution):
> Graph database systems solve this problem, at the cost of infrastructure complexity. An alternative family of approaches, which we introduce here, bring graph-structural information into the embedding space itself. The simplest such method involves selecting related embeddings from the neighborhood of each vector-embedded graph component and aggregating these, then storing the aggregate as an alternative embedding. This process increases the cosine similarities of structurally related, lexically dissimilar items, and thereby improves matching at query time.

### Ending introductions with roadmaps rather than findings

End introductions by previewing findings, not by narrating document structure. A findings preview gives the reader a framework for interpreting what follows; a structural roadmap is a table of contents in prose.

Anti-pattern:
> We describe the data generation process, the question taxonomy, and five retrieval strategies, then report sensitivity, precision, and F1 across question types and hop distances.

Correct:
> As we show, graph-aware embedding strategies outperform vector-only strategies, while joint graph-and-vector strategies saturate performance and vector-only strategies struggle to retrieve exactly the sorts of lexically distinct, structurally related content we expect.

### Bullet-point fragmentation

Use flowing paragraphs with inline enumeration. Do not use bullet-point lists in body text.

Anti-pattern:
> Key findings:
> - Older adults overstayed more
> - This was associated with reward sensitivity
> - Cognitive performance did not explain the effect

Correct:
> Overall, older adults stayed consistently longer compared to young adults across conditions. As participants were generally less optimal in the fast decay conditions, we examined whether this suboptimality was exaggerated in older adults. A linear mixed effect model confirmed that older adults stayed more overall, and showed a small but significant decay rate x age interaction.
