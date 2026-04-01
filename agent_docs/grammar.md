# Grammar Preferences for Agent Instructions

## P1: Use explicit delimiters, not subordinating conjunctions

Use structured delimiters to introduce exceptions or conditions. Subordinating conjunctions blur clause boundaries.

- Bad: "except that when a spec change alters responsibilities, update artifacts"
- Good: "with one exception: when a spec change alters responsibilities, update artifacts"

## P2: Use transitive constructions, not intransitive

Prefer subject-verb-object. Intransitive verbs leave the agent or object implicit.

- Bad: "to stay consistent"
- Good: "to keep them consistent"

## P3: Use precise verbs, not vague periphrasis

Name the operation. Vague verbs ("make sure," "ensure") obscure what action to take.

- Bad: "Make sure the output matches the expected format"
- Good: "Verify that the output matches the expected format"

## P4: Use direct imperatives, not hedged instructions

Do not hedge imperatives with "should," "feel free to," or future-tense periphrasis. These constructions create ambiguity about whether the instruction is mandatory.

- Bad: "Feel free to update the planning artifacts if needed"
- Good: "Update the planning artifacts when spec changes require it"
- Bad: "you will need to propagate changes"
- Good: "Propagate changes across all planning artifacts"

## P5: Delete throat-clearing and filler

Metastatements ("it's important to note that"), purposive padding ("in order to"), and restatement frames ("essentially, what this means is") dilute imperative force. Connectives that link clauses logically ("as a result," "however," "therefore") are not filler.

- Bad: "It's important to note that the checklist should be updated"
- Good: "Update the checklist before writing the report"
- Bad: "In order to maintain consistency"
- Good: delete if purpose is obvious from context
- Bad: "Essentially, what this means is that each function should have a single responsibility"
- Good: "Each function has a single responsibility"

## P6: Use imperative voice, not agentless passives

In instructions, the agent reading the sentence is the actor. Passives create ambiguity about whether the sentence describes a state or commands an action.

- Bad: "Specifications are written for each function in the resource tree"
- Good: "Write a specification for each function in the resource tree"

## P7: Attach participial phrases to their grammatical subject

Dangling participials misattach modifiers and bury sequential dependencies.

- Bad: "After reading the artifacts and checking for errors, the report can be written"
- Good: "Read the artifacts, check for errors, then write the report"

## P8: Use restrictive relative clauses, not locative "where"; resolve ambiguous pronouns

Use "that" for logical (non-spatial) relationships. Resolve pronouns with ambiguous antecedents.

- Bad: "Update artifacts where they conflict with specifications"
- Good: "Update each artifact that conflicts with the specifications"

## P9: Coordinate parallel obligations explicitly

Do not use free participials for independent requirements. Coordinating with "and" makes obligations parallel and independently binding.

- Bad: "The implementation follows the spec, matching data contracts exactly"
- Good: "The implementation follows the spec and matches data contracts exactly"

## P10: Separate prohibitions from justifications

Do not use causal subordinators ("as this," "since this") with ambiguous demonstratives. Split into two sentences: one for the prohibition, one for the reason.

- Bad: "Functions not present in the resource tree should not be created, as this introduces scope beyond the plan"
- Good: "Do not create functions absent from the resource tree. Unplanned functions introduce scope beyond the plan."

## P11: Do not stack hedges

Double hedges ("helps ensure," "should be able to") compound weakeners. Each additional hedge further dilutes the claim.

- Bad: "This helps ensure that the artifacts remain in sync"
- Good: "This keeps the artifacts consistent with each other"

## P12: Use content-specifying modifiers, not locative domain frames

Say what the object contains or does, not which category it belongs to. Locative frames ("in the X domain") classify without committing to what is present. Content-specifying modifiers directly state what the object holds.

- Bad: "a knowledge graph in the professional-networking domain"
- Good: "a knowledge graph containing professional-networking information"
- Bad: "a dataset in the medical domain"
- Good: "a dataset of medical records"

## P13: Write headings as imperative instructions, not noun-phrase rankings

Imperative headings tell the reader what to do. Noun-phrase rankings ("X over Y") name a preference without commanding action.

- Bad: "Explicit delimiters over subordinating conjunctions"
- Good: "Use explicit delimiters, not subordinating conjunctions"

## P14: Do not insert counts unless counts are the subject matter

Never count items in prose unless directly requested or the data under discussion are themselves counts. A count preceding a list the reader is about to see adds no information. Counts are informative only when the number itself is the claim.

- Bad: "Five retrieval strategies trade off structural awareness against simplicity"
- Good: "Retrieval strategies trade off structural awareness against simplicity"
- Bad: "We evaluate three hypotheses"
- Good: "We evaluate the following hypotheses"
- OK: "The resulting graph contains approximately 5500 nodes" (the count is the data)
- OK: "Context set sizes range from two nodes to nearly 100" (the count is the finding)
