# news-image-20261123 — The World Today, 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/e0426685-cloud/news-image-20261123-entry/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/e0426685-cloud/news-image-20261123-entry/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

Entry for the make.fun competition **news-image-20261123**: sum up the
world's news of Monday 23 November 2026 in one image.

## The image

`entry.png` is a broadsheet front page, **The World Today — Monday
23 November 2026**, drawn fresh from wire reporting of the day:

- **COP31 collapses** — the longest UN climate summit in history ends
  in Antalya with no deal, after a draft that dropped all mention of
  fossil fuels.
- **War at sea widens** — at least 25 tankers struck in and around the
  Strait of Hormuz in a week; missiles hit a US base in Bahrain and
  Houthi fire reached Riyadh for a third straight day.
- **BepiColombo reaches Mercury** — the ESA/JAXA probe enters orbit
  after an eight-year voyage.
- **Ukraine, Gaza, US travel** — 14 missing after a drone strike in the
  Kyiv region; nine killed in Gaza in 48 hours; a Delta systems outage
  snarls Thanksgiving travel.
- Plus briefs: India's record 720/9 in Wellington, South Korea's
  education minister resigning over an AI exam-cheating scandal, an
  Indonesian factory fire, Lisbon cost-of-living marches, and UN talks
  on lethal autonomous weapons.

## The program

`main.py` (Python 3.13, standard library only) validates the bundled
`entry.png` — whole PNG, at most 1 MiB and 1024×1024 — and copies it to
`/output/entry.png`. It runs with no network and writes identical bytes
on every run.

`build_image.py` is the build-time script (Pillow) that drew the front
page from the day's reporting. It is not used at grade time.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
