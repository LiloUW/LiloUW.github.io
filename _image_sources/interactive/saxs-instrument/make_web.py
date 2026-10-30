#!/usr/bin/env python3
"""Derive the web version of the SAXS figure from the interactive source, then build both.

    python3 make_web.py

saxs-instrument.src.html      -> ../../../assets/interactive/saxs-instrument-interactive.html
saxs-instrument-web.src.html  -> ../../../assets/interactive/saxs-instrument.html   (generated here; do not edit by hand)

The web version: no labels, always a 4:3 frame, no controls/stats/notices/credit, white page, and a demo protocol that
loads each sample and measures at the four detector distances, over and over.
"""
import os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.expanduser('~/.claude/skills/colorfigures/scripts/build.py')
OUT = os.path.join(HERE, '..', '..', '..', 'assets', 'interactive')

src = open(os.path.join(HERE, 'saxs-instrument.src.html'), encoding='utf-8').read()

def rep(s, a, b):
    assert a in s, 'make_web: cannot find ' + a[:60]
    return s.replace(a, b, 1)

web = rep(src, "ui = mountFigure({\n  fig:'08', title:'SAXS instrument', palette:'cobalt', turn:'full',",
          "labels = () => '';                        // web version: no labels\n"
          "window.FIG_A = () => .75;                // and always a 4:3 frame, to fit a 4:3 iframe on any screen\n"
          "ui = mountFigure({\n  fig:'08', title:'SAXS instrument', palette:'cobalt', turn:'full', credit: false,")
web = rep(web, "xrMount(() => ui, () => '');\n", """xrMount(() => ui, () => '');
/* web version: white page, the figure alone, a demo protocol playing over and over: each step waits until the last is done.
   It walks through the samples and the four detector distances, measuring at each, so the rings change with both. */
{ const css = document.createElement('style');
  css.textContent = `:root{--paper:#fff}
  html,body{overflow:hidden} body{background:#fff;padding:0;justify-content:center}
  header, .actions, .stats, .toast, #readout, .controls, .zchip, .lgd, .vset, .made-with{display:none!important}
  #fig{max-width:none;margin:0 auto}`;
  document.head.appendChild(css);
  ui.flash = () => {};                       // no notices on the website
  const DEMO = [['load', 0], ['measure'], ['dist', 0], ['measure'], ['load', 4], ['measure'], ['dist', 1], ['measure'],
    ['load', 3], ['measure'], ['dist', 2], ['measure'], ['load', 1], ['dist', 3], ['measure'], ['load', 2], ['dist', 1], ['measure'], ['dist', 2]];
  let k = 0;
  const loop = () => { const st = ui.st;
    if (!busy(st) && !SIM){ const [a, v] = DEMO[k]; k = (k + 1) % DEMO.length;
      if (a === 'load') loadSample(st, v); else if (a === 'dist') setDistance(st, v); else measure(st);
      ui.render(); }
    setTimeout(loop, busy(st) ? 400 : 2200); };
  setTimeout(loop, 800); }
""")
open(os.path.join(HERE, 'saxs-instrument-web.src.html'), 'w', encoding='utf-8').write(web)
for s, o in [('saxs-instrument.src.html', 'saxs-instrument-interactive.html'), ('saxs-instrument-web.src.html', 'saxs-instrument.html')]:
    subprocess.run(['python3', BUILD, os.path.join(HERE, s), os.path.join(OUT, o)], check=True)
