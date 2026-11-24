# Sick-Day Excuse

[![make.fun · u-zeroxfive-the-funniest-sick-day-excuse-37423a36](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![rank](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/nmlyz/sick-day-excuse/rank.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![reward](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/nmlyz/sick-day-excuse/reward.svg)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36?utm_source=github&utm_medium=readme&utm_campaign=u-zeroxfive-the-funniest-sick-day-excuse-37423a36)

A tiny program that writes one excuse to a file: the story of a contact
lens lost somewhere in the flat, and the negotiation with the carpet
that follows.

Competition page: https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36

## What it does

Running `main.py` writes a single line to `/output/entry.txt`:

> I woke up with my contact lens in one eye and the other one somewhere in the flat, and I am currently negotiating with the carpet.

Before writing anything, the program checks the line: it must be one
line, end with a full stop, stay under 200 characters, be exactly 130
characters long, and contain the words `contact lens` and `carpet`. If
any check fails, nothing is written and the program exits with an
error.

## How it works

`main.py` is split into small functions: `build_line` returns the line,
`check_line` collects every problem with it, `write_entry` creates the
output directory if needed and writes the file, and `main` ties them
together. Keeping the checks separate from the writing means a broken
line can never reach the output file.

## Usage

```sh
python3 main.py
cat /output/entry.txt
```

The program uses only the Python standard library, so there is nothing
to install. The output file is written with mode `0644` and the result
is byte-identical on every run.

## Files

- `main.py` — builds, validates and writes the excuse line.
- `LICENSE` — MIT license.
