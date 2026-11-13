# AI-Sounding Patterns in Economics Prose

Language models choose the phrasing that suits the widest range of readers, so their prose signals importance, balance and completeness instead of adding information. These patterns are adapted for economics writing from the MIT-licensed [humanizer](https://github.com/blader/humanizer) skill and Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guide.

Use the patterns to make prose clearer. One occurrence is rarely a problem; act when a pattern adds no content or recurs. Every edit still follows the rules in [Terminology and Notation](terminology-and-notation.md): a technical term that looks like a pattern word stays.

## Words that are technical in economics

Some words that are AI tells in general prose are standard terms here. Keep them when they carry their technical meaning:

- *robust* (robust standard errors, robust to), *significant* (statistically significant), *key* in a defined sense, *mechanism*, *channel*, *landscape* only in its literal sense, *underlying* (underlying parameter), *highlight* only when the writer quotes or describes a figure that does so.
- *Crucial*, *pivotal*, *notably* and similar words are tells only when they decorate a sentence that would be just as true without them.

## Patterns to remove

### 1. Contrast with a claim nobody made

"This is not merely a measurement issue; it is a fundamental challenge to identification." The negative half adds weight without adding a claim. State the claim. Keep a contrast when it corrects a belief the literature actually holds, and then name that belief.

> **Before:** Our contribution is not just empirical but conceptual.
> **After:** We also show that the standard sufficient-statistic formula omits the general-equilibrium price response.

### 2. Closers and announcements that repeat the point

A last sentence that restates the paragraph ("This highlights the importance of credit constraints."), a sentence that announces what is coming ("We now turn to the crucial question of…"), or a paragraph that opens by repeating its heading. Cut it unless it adds a fact. A short roadmap in the introduction is a convention and stays.

### 3. Inflated significance

"plays a crucial role", "sheds new light on", "a growing body of literature", "has profound implications for", "an important contribution to the literature". Replace the phrase with the specific fact: which result, how large, for whom.

> **Before:** These findings have profound implications for policy.
> **After:** The estimates imply that the transfer raises consumption by 0.4 dollars per dollar in the first year, roughly twice the value assumed in the program's cost-benefit analysis.

(Only write the second version if the writer's results give those numbers.)

### 4. Borrowed authority and vague association

"Economists have long argued", "it is widely recognized", "the literature suggests", "X is closely linked to Y". Name the papers the writer cites and what they found, or state the relation precisely (X raises Y, X is a component of Y). If the writer has given no source, keep the claim modest and flag that it needs a citation. Never supply a citation.

### 5. Stacked or empty hedges

"could potentially suggest", "may arguably indicate", "it is possible that this might". Keep one hedge where the evidence calls for it. Keep every hedge that states a condition, scope or assumption, because that is content.

### 6. Lists of three by habit

"efficiency, equity, and sustainability" where only one of the three is discussed. Keep the items the text develops. Keep three when there are three.

### 7. Dashes as the default connector

Frequent em dashes in place of commas, colons, parentheses or full stops. Economics writing does use dashes, so do not remove all of them. Reduce them where another punctuation mark states the relation more clearly, and keep about the writer's rate if their own writing uses them. Leave dashes in math, ranges and compound names alone.

### 8. Bold labels and decorative formatting

Bulleted lists with a bold label on every item, bold scattered through running prose, title case in section headings when the template uses sentence case, emojis and arrows. Papers and theses are written in paragraphs; turn a labeled list into prose when the labels carry nothing of their own. Follow the journal or university template where it sets formatting.

### 9. Long verbs for simple ones

"serves as", "stands as", "functions as", "plays the role of", "boasts". Use *is*, *are* or *has*, unless the writer is defining a role in a model.

### 10. Writing about the document

"In this section, we will discuss…", "It is important to note that…", "It is worth mentioning that…", "As mentioned above…". Make the statement directly. Keep cross-references that tell the reader where to find something ("see Appendix B").

### 11. Chat residue

Openings and closings from a conversation: "Certainly", "Here is a revised version", "I hope this helps", "Let me know if…". Remove them from any text meant to stand on its own.

### 12. Generic filler sentences

Sentences that would fit any paper: "Understanding this question is important for policymakers and researchers alike." Replace with the specific reason this question matters, from the writer's own material, or cut.

## When to leave text alone

- Quotations, titles, proper names and passages that discuss a phrase instead of using it.
- Standard formulas of the genre: "We thank … for helpful comments", "All errors are our own", the roadmap paragraph, the referee report's opening summary.
- Passive voice where the actor does not matter or the convention expects it ("Standard errors are clustered at the county level").
- The writer's own deliberate style, especially if they have supplied a sample.
