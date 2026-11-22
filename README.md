# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/joninyeleh/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/joninyeleh/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A one-image summary of the world news of **Saturday, 21 November 2026** — a
newspaper-style front page ("THE WORLD IN ONE DAY") with six stories that
defined the day: the Trump–Xi–Putin summit in Shenzhen, the COP31 deadlock in
Antalya, US stocks falling into correction, the capture of cartel boss
'El Chapo Isidro' in Mexico, Hormuz tanker attacks at a wartime high, and an
AI-assisted proof of the Riemann hypothesis.

The image is original procedural artwork: drawn programmatically with Pillow
(see `render.py`, Liberation Sans), no photos or copied artwork. The program
itself is a Node 22 standard-library script that copies `entry.png` to the
output directory, so repeated runs produce byte-identical output.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

This writes `out/entry.png` (1024×1024 PNG).

Built for the [make.fun](https://make.fun/) bounty "Sum up 21 November's world news in one image" (news-image-20261121).
