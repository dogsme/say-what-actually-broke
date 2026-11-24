# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/dogsme/say-what-actually-broke/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/dogsme/say-what-actually-broke/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

One line of software error copy for [make.fun's "Say What Actually Broke" bounty](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5): the brutal truth about what went wrong, funny on a single read, shippable in a real error dialog.

## The line

> Your file didn't save — the database timed out mid-write, so your last hour is now a ghost. Save again, and keep a copy somewhere we can't lose it.

It names the real failure (a database timeout mid-write), says what was lost, and tells the user exactly what to do next — save again, and keep a copy out of our reach.

## Run

```sh
python3 main.py
```

This writes the single line to `/output/entry.txt` (one line, UTF-8, under 200 characters).

## License

MIT. See [LICENSE](LICENSE).
