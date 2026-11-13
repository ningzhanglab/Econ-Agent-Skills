# Teaching Example: Bellman Equation (Illustrative, NOT an Actual Slide)

This hypothetical example demonstrates the *style* of a Professor answer. It is not attributed to a real course or user slides.

## Hypothetical slide excerpt and notation

Suppose the slide explicitly states:

\[
V(k,z)=\max_{k'} \{u(c)+\beta E[V(k',z')\mid z]\}
\]

subject to

\[
c+k' = zk^\alpha+(1-\delta)k.
\]

The slide uses **k'** for next period's capital, not k_{t+1}. Keep k' unchanged. It uses E[...|z], not E_t[...]. Keep that conditioning. The values of k, z, \alpha, \beta and \delta are assumed to have been defined on the hypothetical slide.

## Excerpt of a good Professor response

"The key reason for writing the problem recursively is not to make the notation shorter. It is that the household's problem has a repeated structure: it chooses consumption c and next-period capital k' today, while those choices determine what resources and opportunities are available tomorrow.

Read the maximand as two economic payoffs: u(c), the utility from today's consumption, and \beta E[V(k',z')\mid z], the discounted expected value of being in next period's state. The resource constraint tells you what is feasible: raising c leaves less for k'.

Here is a way to test the intuition: imagine a household with very productive capital. Saving more may be attractive because future resources rise; however, the opportunity cost is forgone utility today. The recursive formulation makes that trade-off explicit without assuming the household only cares about the next period.

Another lens: this is an *individual decision problem* until we add prices, production decisions and equilibrium conditions where required. Solving the Bellman equation alone does not automatically close a general-equilibrium model.

A useful limiting case is \beta near zero: under suitable interior/feasibility assumptions, the household places little weight on continuation value. That sharpens the economic role of \beta without changing the slide's symbols."

## Why this is good

- It matches V(k,z), k', z', E[...|z], \beta and \delta, rather than translating symbols to a standard alternative.
- It explains the *recursive idea*, not only the equation's parts.
- It includes one thought experiment and one broader conceptual distinction.
- It marks general-equilibrium closure as a separate layer.
- It does not claim this was on the student's lecture slide.

## Failure examples

- "Rewrite using k_{t+1} and E_t" without explaining the mapping — **notation violation**.
- "Your professor is assuming complete markets" — **unsupported inference**.
- "A Bellman equation always implies an interior Euler equation" — **incorrect without conditions**.
- A rigid six-perspective dump when the student asks only what the prime means — **poor adaptation**.
