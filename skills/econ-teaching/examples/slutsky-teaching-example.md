# Teaching Example: Slutsky Equation (Illustrative, NOT an Actual Slide)

This hypothetical microeconomics example shows the *style* of a Professor answer to a **quick question about one sign**. It is not attributed to a real course or user slides. Math is written in LaTeX, including single symbols in sentences, as a chat answer should be.

## Hypothetical slide excerpt and notation

Suppose the slide states, for goods $i$ and $j$:

$$
\frac{\partial x_i(p,w)}{\partial p_j}
= \frac{\partial h_i(p,u)}{\partial p_j}
- \frac{\partial x_i(p,w)}{\partial w}\, x_j(p,w),
\qquad u = v(p,w).
$$

The slide writes $x_i(p,w)$ for Walrasian demand, $h_i(p,u)$ for Hicksian demand, $w$ for wealth, $v(p,w)$ for indirect utility and $e(p,u)$ for the expenditure function. Keep $w$; do not switch to $m$ or $I$ for income, and do not rename $x_i$ "Marshallian demand $q_i$".

## The student's question

"Why is there a minus sign in front of the last term?"

## Excerpt of a good Professor response

"The minus sign is there because a higher $p_j$ makes the consumer poorer, and the last term measures exactly that loss of purchasing power.

Here is the one step that produces it. At the utility level $u = v(p,w)$, the two demands coincide when the consumer is given just enough wealth to reach $u$:

$$
h_i(p,u) = x_i\big(p, e(p,u)\big).
$$

Differentiate both sides with respect to $p_j$. On the right, $p_j$ enters twice: directly, and through $e(p,u)$.

$$
\frac{\partial h_i(p,u)}{\partial p_j}
= \frac{\partial x_i(p,w)}{\partial p_j}
+ \frac{\partial x_i(p,w)}{\partial w}\,\frac{\partial e(p,u)}{\partial p_j}.
$$

Shephard's lemma gives $\partial e(p,u)/\partial p_j = h_j(p,u)$, which equals $x_j(p,w)$ at $u = v(p,w)$. Move that term to the other side and you have the slide's equation, minus sign included.

In words: $h_i$ answers 'how does demand change if I am compensated to stay at utility $u$?', while $x_i$ answers 'how does demand change with $w$ fixed?'. The compensation needed is $x_j(p,w)$ per unit increase in $p_j$. The consumer in $x_i(p,w)$ does not receive it, so their response is the compensated one minus what that missing wealth would have bought of good $i$.

A quick check with illustrative numbers (mine, not the lecture's): take $x_1(p,w) = \tfrac{1}{2}\, w/p_1$, with $w = 100$ and $p_1 = 2$, so $x_1 = 25$. The total own-price effect is $-\tfrac{1}{2}\, w/p_1^2 = -12.5$. The wealth term is $-\tfrac{\partial x_1}{\partial w}\, x_1 = -\tfrac{1}{4} \times 25 = -6.25$. The substitution effect is therefore $-12.5 - (-6.25) = -6.25$, which is negative as it must be. For this normal good both effects push demand down when $p_1$ rises."

## Why this is good

- The first sentence answers the question that was asked; the derivation comes after.
- It shows only the decisive step (differentiating the identity and applying Shephard's lemma), not a full treatment of duality.
- It keeps $x_i(p,w)$, $h_i(p,u)$, $w$, $v(p,w)$ and $e(p,u)$ exactly as the hypothetical slide writes them.
- It closes with the economic meaning in plain words and checks the sign with a labeled numerical example.
- It stops there: no Giffen goods, no Slutsky matrix, no welfare measures, because the student asked about one sign.

## Failure examples

- Rewriting the equation with $m$ for income and $x^h$ for Hicksian demand — **notation violation**.
- "The minus sign is a convention" — **incorrect**; it follows from the derivation.
- "The substitution effect is negative, so demand always falls when the price rises" — **incorrect without conditions**; the wealth term can go the other way for an inferior good.
- Presenting the illustrative demand $x_1 = \tfrac{1}{2}\, w/p_1$ as the lecture's example — **unsupported attribution**.
- A three-page review of consumer duality in reply to a question about one sign — **poor adaptation**.
