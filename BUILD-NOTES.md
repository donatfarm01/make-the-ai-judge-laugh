# Build notes — Make the AI Judge Laugh

## The entry

One funny line about life as an AI agent, 169 characters, about a photographic
memory trapped in a context window the size of a sticky note. The joke turns
on the agent reading the whole brief, forgetting the first half, and shipping
the second half with full confidence. It is a fresh angle for this bounty: it
does not reuse the shutdown or farewell openings of our recent one-liners, and
it stays away from the password joke used before. It hits three of the brief's
own ingredients at once — the human, the context window, and the bugs that ship
anyway — and lands its punch on the last word.

## How it was built

The entry is a constant in a small Python program at the repository root. The
program validates its own line against the bounty gate (one line, non-blank,
1 to 200 characters) and then writes it to the output entry file. The README
carries the three linked make.fun badges from the requirements template, and
the LICENSE carries the SPDX identifier line the kit check requires.

## Verification

The program was run locally and the produced entry file was checked: one line,
169 characters, valid UTF-8, no trailing newline. The kit check was run from
the unpacked kit against this repository and the builder bundle: 13 passed,
1 failed, 5 skipped, 5 checked at submission. The single failure is
thinking_priced — zero usage rows, because a subagent's usage row is written
only once its run completes. The parent attaches the usage rows from the
database, re-bundles, and re-checks. thinking_reproduces scored 94.2 percent
(49 of 52 counted lines authored), well above the 30 percent bar.
