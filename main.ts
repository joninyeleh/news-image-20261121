// A make.fun news-image entry (Node 22, standard library only): its image is
// the entry.png beside this file, and the program copies it to the output
// directory. The image is original procedural artwork rendered with Pillow
// (see render.py): a newspaper-style front page, 1024x1024, summarising the
// world news of Saturday, 21 November 2026 in six stories.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
