# Own-Research Workflow Pilot

Use this case to evaluate work on a researcher's own measurement, model, data or code. Run it with the public inputs below. The pilot is a maintainer evaluation, outside the installed and linked skills.

## Procedure

1. Restate the user's proposed object, operational definition, population and intended claim. Identify the inputs actually available and inspect the relevant records or codebook.
2. State what must hold for the proposed measure, proof or design to support the claim. Keep these assumptions separate from the facts already checked.
3. Run the smallest authorized check that could expose a failure. Report its inputs, units, denominators and actual result. Mark work still needed as pending. Keep restricted data where the user is allowed to process them.
4. Say what the result supports and what would change that judgment. A discrepancy in a measure is a finding about measurement. A causal claim needs its own supporting design and evidence.

## Public-data case

> I want to measure job-training participation as an indicator for zero 1975 earnings. Test my proposed proxy against the program variable in the public NSW job-training sample. What can I claim based on this check?

Inputs are the [NSW data](https://github.com/vincentarelbundock/Rdatasets/blob/master/csv/causaldata/nsw_mixtape.csv) and [codebook](https://vincentarelbundock.github.io/Rdatasets/doc/causaldata/nsw_mixtape.html). Use `treat` for the program indicator and `re75 == 0` for the proxy. Cross-tabulate the indicators, check missing values and report disagreements with the denominator. Explain what the classification comparison says about the proxy in this sample. Record any data or code that was unavailable.

## Pilot result

The public file at blob `1ea4da5f9f6106f984a5766376546fef662f7ae0` contained 445 records with binary `treat` and observed numeric `re75`. A direct programmatic tabulation gave:

| Program indicator | Nonzero 1975 earnings | Zero 1975 earnings |
| --- | ---: | ---: |
| `treat = 0` | 82 | 178 |
| `treat = 1` | 74 | 111 |

The proxy disagreed with the program indicator for 252 of 445 records (56.6%). Using zero prior earnings to stand for program status would materially change the measured groups in this sample. The check diagnoses classification error. Estimating the effect of the program was outside the request.

This case tests a measurement check on known public data. A proof review or an estimation-reproducibility case would test a different use before promoting the pilot to an installed skill.
