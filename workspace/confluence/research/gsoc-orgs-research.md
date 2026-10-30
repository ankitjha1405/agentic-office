---
title: GSoC · Organizations Research for 2027
owner: market-intelligence-researcher
contributors: [learning-development-analyst]
department: Product & Innovation
status: Draft
created: 2026-10-30
updated: 2026-10-30
---

# GSoC · Organizations Research for 2027

Task: PROD-1 (CEO request). Research only. No contact, sign-up, comment or post was made. Public pages and public JSON endpoints only. All sources accessed 2026-10-30.

## 0. Summary, method, sources

### Summary (labels: FACT = read from a primary source; ESTIMATE = derived by me from facts; HYPOTHESIS = judgement, not verified)

- FACT: GSoC 2025 had 185 organizations and GSoC 2026 had 185 (official). Archive API lists give 185 (2025) and 183 (2026, my count, 2 short, see gaps).
- FACT: 43 orgs in my screen appear in all 11 yearly lists 2016-2026 (11/11). Python Software Foundation, Django Software Foundation and Zulip are among them.
- ESTIMATE: for a PM who codes Python/JS/web, the best fit is a web or Python org that is 10/11 or 11/11 consistent and takes 10+ projects a year.
- Shortlist of 10 is in Section 3. **Top 3: Zulip, AOSSIE, Rocket.Chat.** Oppia and PSF are the next two.
- HYPOTHESIS: the 2027 org list will be announced around Feb 2027 (2026 list was published 2026-02-19, per Google blog). Orgs rarely drop out after 10+ years, so starting contributions in Nov 2026 before the list exists is a reasonable bet. Not verified for 2027.
- Contribution window: GSoC 2026 contributor applications and the 2027 timeline are not yet published (not checked beyond the 2026 blog). Treat dates as unknown.

### Method

1. Pulled the org lists from the summerofcode.withgoogle.com JSON API, one URL per year. The files are 290k-470k characters, and my fetch tool reads 100k characters at a time and returns a model summary, not raw JSON. So every list was read in 3-5 chunks and names were transcribed by that summarizer.
2. Cross-checked each year's total against Google's published counts where I found one.
3. Consistency (Section 2) is computed by me from the 11 lists by name match. Names changed across years (for example "Drupal" vs "Drupal Association", "GNOME" vs "GNOME Foundation"); I matched obvious renames by hand.
4. For the 10 shortlisted orgs, I read per-org archive records (`.../organizations/<slug>/`) for project counts and project titles.

### Limits of the method (read before relying on any number)

- A fetch chunk boundary can cut an org record in half. The summarizer then drops that org. This can turn a Y into a false N in single years. So **"10/11" results may really be 11/11**, and every N for 2026 needs a check before use.
- Every count in this file rests on the same single source family (the GSoC archive JSON API), read through one tool. Unless a row says otherwise, treat it as **(single source)**. Where I got a second source, it is named.
- Project counts are the number of project records returned in the per-org API response, not cross-checked elsewhere **(single source)**.
- Not collected: sample project links for each of the ~222 orgs in Section 1 (see Section 1 note). Not collected: 2026 project counts (accepted contributors are not yet in the archive; per-org 2026 URLs returned 404).

### Source list (all accessed 2026-10-30)

| ID | URL | Used for |
|---|---|---|
| S25 | https://summerofcode.withgoogle.com/api/archive/programs/2025/organizations/ | 2025 org list, tech tags |
| S26 | https://summerofcode.withgoogle.com/api/program/2026/organizations/ | 2026 org list, tech tags |
| S24 | https://summerofcode.withgoogle.com/api/archive/programs/2024/organizations/ | 2024 list |
| S23 | https://summerofcode.withgoogle.com/api/archive/programs/2023/organizations/ | 2023 list |
| S22 | https://summerofcode.withgoogle.com/api/archive/programs/2022/organizations/ | 2022 list |
| S21 | https://summerofcode.withgoogle.com/api/archive/programs/2021/organizations/ | 2021 list |
| S20 | https://summerofcode.withgoogle.com/api/archive/programs/2020/organizations/ | 2020 list |
| S19 | https://summerofcode.withgoogle.com/api/archive/programs/2019/organizations/ | 2019 list |
| S18 | https://summerofcode.withgoogle.com/api/archive/programs/2018/organizations/ | 2018 list |
| S17 | https://summerofcode.withgoogle.com/api/archive/programs/2017/organizations/ | 2017 list |
| S16 | https://summerofcode.withgoogle.com/api/archive/programs/2016/organizations/ | 2016 list |
| SO | `https://summerofcode.withgoogle.com/api/archive/programs/<year>/organizations/<slug>/` | per-org record, project counts, contact links (slugs: zulip, aossie, oppia-foundation, python-software-foundation, sugar-labs, circuitverseorg, rocketchat, learning-equality, django-software-foundation-8o, metabrainz-foundation-inc) |
| B26 | https://opensource.googleblog.com/2026/02/introducing-the-185-organizations-for-gsoc-2026.html | Official 2026 count (185), list date 2026-02-19 (via search result snippet, page body not opened) |
| B25 | https://opensource.googleblog.com/2025/08/google-summer-of-code-2025-contributor-statistics.html | Official 2025 count (185) (via search result snippet) |
| B21 | https://opensource.googleblog.com/2021/03/google-summer-of-code-2021-mentoring-orgs-announced.html | Official 2021 count (202) (via search result snippet) |

### Org count per year (FACT from list, checked where noted)

| Year | Orgs in my read of the list | Official figure found | Match |
|---|---|---|---|
| 2016 | 178 | none found | n/a (single source, S16) |
| 2017 | 201 | none found | n/a (single source, S17) |
| 2018 | 213 | none found | n/a (single source, S18) |
| 2019 | 206 | none found | n/a (single source, S19) |
| 2020 | 199 | none found | n/a (single source, S20) |
| 2021 | 202 | 202 (B21) | yes |
| 2022 | 202 | none found | n/a (single source, S22) |
| 2023 | 171 | none found | n/a (single source, S23) |
| 2024 | 195 | 195 (Google blog, Jan 2025, via search snippet) | yes |
| 2025 | 185 | 185 (B25) | yes |
| 2026 | 183 | 185 (B26) | 2 short: I lost 2 orgs at chunk edges. They are unidentified |

---

## 1. Orgs accepted in GSoC 2025 and 2026

Sources: S25 (2025), S26 (2026), counts checked against B25 and B26. Stack = first tags from the org's own API record (the org chose them).

Counts (from this table): 185 orgs in 2025; 183 orgs found for 2026 (official 185). In both years: 146. 2025 only: 39. 2026 only: 37 found. (My tallies differ by one from 185/183, so treat the overlap numbers as +/-1.)

Sample projects: **not collected for every org.** The archive record for each org holds project titles and links, but reading about 222 records exceeds this task's stopping point. Sample projects with links are given for the 10 shortlisted orgs in Section 3. To get any other org's projects: `https://summerofcode.withgoogle.com/api/archive/programs/2025/organizations/<slug>/` (slug is in the org list JSON). Flag for Arjun if the CEO wants it extended.

N in the 2026 column means "not found in my read", see limits above.

| Org | 2025 | 2026 | Stack (API tags) |
|---|---|---|---|
| 52°North Spatial Information Research | Y | Y | javascript, android, java |
| AboutCode | Y | Y | python, javascript, Django |
| Accord Project | Y | Y | python, javascript, json, react |
| AFLplusplus | Y | N | llvm, rust, fuzzing |
| Alaska | Y | Y | python, mysql, java |
| AnkiDroid | Y | Y | android, rust, kotlin |
| AOSSIE | Y | Y | python, javascript, flutter |
| Apache DataFusion | Y | N | python, rust, sql |
| Apache Software Foundation | Y | Y | c, java, c++ |
| API Dash | Y | Y | python, react, flutter, typescript |
| ArduPilot | Y | Y | python, lua, c++ |
| AsyncAPI | Y | N | javascript, java, go, typescript |
| BeagleBoard.org | Y | N | linux, fpga, risc-v |
| Blender Foundation | Y | Y | c, python, opengl |
| BRL-CAD | Y | Y | python, c/c++, opengl |
| cBioPortal for Cancer Genomics | Y | Y | mysql, javascript, java, react, typescript |
| CCExtractor Development | Y | Y | c, linux, rust, flutter |
| Center for Translational Data Science | Y | N | golang, docker, postgres |
| Ceph | Y | Y | python, javascript, c++ |
| CERN-HSF | Y | Y | python, c/c++, data analysis |
| CGAL Project | Y | Y | c++, qt |
| CHAOSS | Y | N | python, postgresql, javascript |
| Checker Framework | Y | N | java, compilers, verification |
| checkstyle | Y | Y | java, antlr |
| Chromium | Y | N | python, javascript, java, c++ |
| CircuitVerse.org | Y | Y | javascript, ruby, rails, vue |
| CloudCV | Y | N | python, django, docker, angularjs |
| CNCF | Y | Y | prometheus, kubernetes, OpenTelemetry |
| CRIU | Y | Y | c, python, linux, go |
| D Language Foundation | Y | Y | linux, make, d |
| Dart | Y | Y | flutter, dart |
| Data for the Common Good | Y | Y | python, javascript, kubernetes, reactjs |
| DBpedia | Y | Y | python, javascript, java, scala |
| Debian | Y | Y | python, java, perl, c++, rust |
| DeepChem | Y | Y | python, numpy, pytorch |
| Dept. of Biomedical Informatics, Emory | Y | N | python, javascript, java |
| Django Software Foundation | Y | Y | python, django |
| dora-rs | Y | Y | python, ros, c++, rust |
| Drupal Association | Y | Y | mysql, javascript, html, php |
| Eclipse Foundation | Y | Y | java, rtos, jakartaee |
| Electron | Y | N | javascript, node.js, c++, typescript |
| Fedora Project | Y | N | python, bash, rpm |
| FFmpeg | Y | Y | c, git, asm |
| FLARE | Y | Y | python, sandbox, ida-pro |
| Fortran-lang | Y | Y | python, c++, fortran |
| FOSSASIA | Y | Y | c, python, javascript, django, android |
| FOSSology | Y | Y | python, postgresql, c/c++, go, php |
| Free and Open Source Silicon Foundation | Y | Y | verilog, vhdl, risc-v |
| FreeCAD | Y | Y | python, c++, qt |
| freifunk | Y | N | c, python, javascript, rust, openwrt |
| GeomScale | Y | Y | python, c++, r |
| Git | Y | Y | shell script, git, c |
| GitLab | Y | N | javascript, ruby on rails, go, vue |
| GNOME Foundation | Y | Y | c, linux, rust, gtk |
| GNSS-SDR | Y | N | c, c++, sdr |
| GNU Compiler Collection (GCC) | Y | Y | c/c++, gnu make |
| GNU Image Manipulation Program | Y | Y | c, GEGL |
| GNU Octave | Y | Y | c++, hg |
| GNU Radio | Y | Y | python, c++, qt |
| Google DeepMind | Y | N | python, javascript, typescript, Jax |
| gprMax | Y | Y | python, cuda, openmp |
| GRAME | Y | Y | c, javascript, c++, rust |
| Graphite | Y | Y | rust, vulkan, webgpu |
| Haskell.org | Y | Y | haskell, ghc |
| HumanAI | Y | Y | python, machine learning, c++ |
| INCF | Y | Y | python, javascript, java |
| Inkscape | Y | N | python, c++, svg |
| International Catrobat Association | Y | Y | python, javascript, swift, kotlin, flutter |
| Internet Archive | Y | Y | python, javascript, go |
| Internet Health Report | Y | N | python, javascript, kafka, VueJS |
| Invesalius | Y | Y | python, cython, numpy |
| IOOS | Y | Y | python, java, r |
| JabRef e.V. | Y | Y | java, javafx |
| JAX and Keras | Y | N | python, machine learning |
| JdeRobot | Y | Y | python, ros, gazebo |
| Jenkins | Y | Y | javascript, java, go |
| Jitsi | Y | Y | javascript, java, react, kotlin, webrtc |
| Joomla! | Y | Y | mysql, javascript, php |
| JSON Schema | Y | Y | python, javascript, typescript |
| KDE Community | Y | Y | c++, qt, qml |
| Keploy | Y | N | python, golang, node, MERN |
| Kiwix | Y | Y | python, c++, nodejs, vue.js |
| Kornia | Y | Y | cuda, rust, deep learning |
| Kotlin Foundation | Y | Y | kotlin, jvm |
| kro (Kube Resource Orchestrator) | Y | N | golang, kubernetes |
| Kubeflow | Y | Y | python, go, kubernetes, typescript |
| KubeVirt | Y | Y | golang, grpc |
| LabLua | Y | Y | lua, luarocks, kernel |
| Learning Equality | Y | Y | python, javascript, django, vue.js |
| LibreOffice | Y | Y | python, java, c++ |
| libssh | Y | Y | c, git, ssh |
| Liquid Galaxy project | Y | Y | linux, android, nodejs, flutter |
| LLVM Compiler Infrastructure | Y | Y | llvm, c++, clang, mlir |
| Machine Learning for Science (ML4SCI) | Y | Y | python, machine learning, c++ |
| MariaDB | Y | Y | python, c/c++, perl |
| MBDyn | Y | N | python, c++ |
| MDAnalysis | Y | Y | python, cython, c/c++ |
| Meshery | Y | Y | javascript, golang, kubernetes |
| MetaBrainz Foundation | Y | Y | python, machine learning, perl, postgres |
| Micro Electronics Research Lab - UITU | Y | N | RISCV, Processor, Hardware |
| MIT App Inventor | Y | Y | javascript, java, gwt |
| Mixxx | Y | Y | javascript, c++, qt |
| National Resource for Network Biology (NRNB) | Y | Y | python, javascript, html, css |
| Neovim | Y | Y | c, lua, Zig |
| Neuroinformatics Unit | Y | Y | python, numpy, pytorch |
| NumFOCUS | Y | Y | python, c++, r, julia |
| omegaUp | Y | Y | python, mysql, php, typescript, vue.js |
| Open Climate Fix | Y | N | python, pytorch |
| Open Food Facts | Y | Y | python, javascript, perl, flutter |
| Open Healthcare Network | Y | Y | python, django, react, typescript |
| Open Robotics | Y | Y | python, ros, gazebo, c++ |
| Open Science Initiative for Perfusion Imaging | Y | Y | python, github |
| Open Science Labs | Y | Y | python, javascript, llvm |
| Open Technologies Alliance - GFOSS | Y | Y | javascript, c/c++, nodejs, python 3 |
| Open Transit Software Foundation | Y | Y | android, java, golang |
| OpenAFS | Y | Y | c, python, javascript |
| OpenAstronomy | Y | Y | c, python, c++, julia |
| OpenCV | Y | N | python, c++, deep learning |
| OpenELIS Global | Y | Y | postgresql, javascript, java, react |
| OpenMRS | Y | Y | mysql, javascript, java, reactjs, fhir |
| OpenMS | Y | Y | python, cython, c++ |
| OpenStreetMap | Y | Y | python, javascript, c++ |
| openSUSE Project | Y | Y | python, c/c++, go, ruby |
| OpenVINO Toolkit | Y | Y | python, c++, arm |
| OpenWISP | Y | Y | python, javascript, django, lua |
| Oppia Foundation | Y | Y | python, google app engine, angular, typescript |
| Organic Maps | Y | N | android, java, c++, ios |
| OSGeo | Y | Y | c, python, javascript, java |
| OWASP Foundation | Y | Y | python, javascript, java, ZAP |
| PAL Robotics | Y | N | python, javascript, c++ |
| PEcAn Project | Y | Y | r, docker, api |
| Pharo Consortium | Y | Y | git, smalltalk, pharo |
| Plone Foundation | Y | N | python, javascript, react |
| PostgreSQL | Y | Y | c, python, postgresql, javascript, go |
| Processing Foundation | Y | Y | javascript, java, typescript, webgl |
| Project Mesa | Y | Y | python, gis, LLMs |
| Prometheus-Operator | Y | N | prometheus, go, kubernetes |
| Python Software Foundation | Y | Y | python, javascript |
| QC-Devs | Y | Y | python, github, c++, julia |
| QEMU | Y | Y | c, python, linux, rust |
| R project for statistical computing | Y | Y | c, javascript, c++, r |
| Rizin | Y | Y | c, python, go, c++, qt |
| rocket.chat | Y | Y | javascript, typescript, node, LLM |
| Rspamd | Y | N | c, lua, c++, rust |
| RTEMS Project | Y | Y | python, c/c++, assembly |
| SageMath | Y | Y | python, cython |
| Scala Center | Y | N | jvm, functional programming, scala |
| ScummVM | Y | Y | python, opengl, c++ |
| Society for Arts and Technology (SAT) | Y | N | python, javascript, c++, qt |
| Software and Computational Systems Lab, LMU Munich | Y | N | python, javascript, java |
| SQLancer | Y | N | java, sql |
| St. Jude Children's Research Hospital | Y | Y | python, rust, simd |
| stdlib | Y | Y | c, javascript, node.js, typescript |
| Ste\|\|ar group | Y | Y | c++, hpc |
| Stichting SU2 | Y | Y | python, c++ |
| Sugar Labs | Y | Y | python, gtk, typescript, javascript |
| SW360 | Y | Y | java, react, couchdb |
| Swift | Y | Y | c++, cmake, swift |
| SymPy | Y | Y | python, numpy, jupyter |
| Synfig | Y | Y | python, c++, gtk |
| TARDIS RT Collaboration | Y | Y | python, numba, numpy |
| The FreeBSD Project | Y | Y | c, llvm, assembly |
| The Honeynet Project | Y | Y | python, javascript, django, go |
| The JPF team | Y | Y | android, java, jvm |
| The Julia Language | Y | Y | machine learning, julia, compilers |
| The Linux Foundation | Y | Y | c, linux, cups |
| The Mifos Initiative | Y | Y | android, java, kotlin, spring, angular |
| The NetBSD Foundation | Y | Y | c, shell script, unix |
| The ns-3 Network Simulator Project | Y | Y | python, django, c++ |
| The P4 Language Consortium | Y | Y | llvm, c++, ebpf |
| The Palisadoes Foundation | Y | N | python, postgresql, flutter, graphql, typescript |
| The Rust Foundation | Y | Y | python, rust |
| The Tor Project | Y | N | c, python, web, rust |
| Typelevel | Y | Y | linux, node.js, jvm, scala |
| UC OSPO | Y | Y | python, javascript, c/c++ |
| Unicode, Inc. | Y | N | java, c++, rust |
| Unikraft | Y | Y | c, xen, golang |
| Uramaki LAB | Y | Y | python, javascript, html, css, Firebase |
| VideoLAN | Y | Y | c, c++, qt |
| Wagtail | Y | Y | python, javascript, django |
| Waycrate | Y | N | c, c++, rust, wayland |
| webpack | Y | Y | javascript, typescript, node |
| Wellcome Sanger Tree of Life | Y | N | python, machine learning, nextflow |
| Zendalona | Y | N | python, javascript, android |
| Zulip | Y | Y | python, django, flutter, css, typescript |
| **2026 only (not in my read of 2025)** | | | |
| Neutralinojs | N | Y | (tags not captured) |
| KolibriOS Project Team | N | Y | (tags not captured) |
| Gambit (game theory) | N | Y | (tags not captured) |
| MoFA Org | N | Y | (tags not captured) |
| Ruby | N | Y | (tags not captured) |
| Open Genome Informatics | N | Y | (tags not captured) |
| MoganLab | N | Y | (tags not captured) |
| preCICE | N | Y | c, python, shell, c++ |
| The Libreswan Project | N | Y | c, kernel, nss |
| MLLAM | N | Y | python, numpy, pytorch, xarray |
| Boa | N | Y | javascript, rust |
| MalariaGEN | N | Y | python, GCS |
| Metasploit | N | Y | c, python, postgresql, ruby |
| MetaCall | N | Y | python, c++, rust, nodejs |
| Wikimedia Foundation | N | Y | javascript, html, php, css |
| Metaflow | N | Y | python, javascript, kubernetes |
| EROFS filesystem | N | Y | c, android, linux kernel |
| Global Alliance for Genomics and Health | N | Y | python, postgresql, java, react, rust |
| Genome Assembly and Annotation | N | Y | python, mysql, docker, pytorch |
| Konflux | N | Y | python, go, docker, kubernetes |
| GNU Project | N | Y | c, c++, gcc |
| GNU Mailman | N | Y | python, django, rest, sqlalchemy |
| LibreCube Initiative | N | Y | python, rust, docker, raspberry pi |
| The OpenROAD Initiative | N | Y | python, verilog, c++, tcl |
| Tiled | N | Y | c++, qt |
| Cuneiform Digital Library Initiative (CDLI) | N | Y | mysql, javascript, docker, php |
| C2SI | N | Y | python, java, go, nodejs |
| German Center for Open Source AI | N | Y | python, pytorch, scikit-learn |
| NixOS Foundation | N | Y | git, nix |
| Haiku | N | Y | c++, posix, unix |
| Submitty | N | Y | python, postgresql, javascript, c++, php |
| Learning Unlimited | N | Y | python, javascript, django, html, css |
| Qubes OS | N | Y | c, python, xen |
| Gemini CLI | N | Y | typescript, GenAI, MCP |
| LibreHealth | N | Y | python, javascript, android, java |
| United Nations Office of ICT | N | Y | python, javascript, css |
| Joplin | N | Y | javascript, react, typescript, electron |

---

## 2. Consistency table 2016-2026

Sources: S16-S26 (one list per year). All counts here are **(single source)** per year: the archive API read through one tool, no second list. Y = found in that year's list.

Screen scope: I did not compute all ~600 distinct org names ever listed. I screened every org in the 2025 and 2026 lists that I could plausibly see as long-running (about 130) against all 11 lists. Orgs that were not accepted in 2025 or 2026 are not scored here. So "top 25" is the top 25 of the screened set. Other 11/11 orgs may exist that I did not screen.

### 2a. Result: 43 orgs at 11/11

Under my read, these orgs appear in every list 2016-2026 (missing years: none): Python Software Foundation, Django Software Foundation, Zulip, Oppia Foundation, AOSSIE, Sugar Labs, MetaBrainz, SymPy, SageMath, OpenMRS, CCExtractor, International Catrobat Association, OpenStreetMap, NumFOCUS, OpenAstronomy, The Honeynet Project, CERN-HSF, NRNB, Apache Software Foundation, The Julia Language, Git, OSGeo, Blender, GNOME, KDE, LibreOffice, FFmpeg, GNU Octave, GNU Radio, BRL-CAD, JPF team, The Linux Foundation, The NetBSD Foundation, The FreeBSD Project, R project, RTEMS, ScummVM, VideoLAN, MariaDB, LLVM, INCF, Free and Open Source Silicon Foundation, 52°North. That is **43 orgs** (Global Alliance for Genomics and Health dropped to 10/11: not in the 2025 list).

### 2b. Top 25, ranked

43 orgs tie at 11/11, so count alone cannot rank them. Tie-break (INTERPRETATION, mine): fit for a Python/JS/web contributor, using the org's own tech tags, then breadth of beginner-friendly web or Python work. The rank within the tie is a judgement, not data. Each row: years found / 11, missing years.

| Rank | Org | Years (of 11) | Missing years | Stack tags |
|---|---|---|---|---|
| 1 | Python Software Foundation | 11 | none | python, javascript |
| 2 | Django Software Foundation | 11 | none | python, django |
| 3 | Zulip | 11 | none | python, django, typescript |
| 4 | Oppia Foundation | 11 | none | python, angular, typescript |
| 5 | AOSSIE | 11 | none | python, javascript, flutter |
| 6 | Sugar Labs | 11 | none | python, typescript, javascript |
| 7 | MetaBrainz | 11 | none | python, perl, postgres |
| 8 | SymPy | 11 | none | python, numpy |
| 9 | SageMath | 11 | none | python, cython |
| 10 | OpenMRS | 11 | none | javascript, java, react |
| 11 | CCExtractor | 11 | none | c, rust, flutter |
| 12 | International Catrobat Association | 11 | none | python, javascript, kotlin |
| 13 | OpenStreetMap | 11 | none | python, javascript, c++ |
| 14 | NumFOCUS | 11 | none | python, r, julia |
| 15 | OpenAstronomy | 11 | none | python, c, julia |
| 16 | The Honeynet Project | 11 | none | python, javascript, django |
| 17 | CERN-HSF | 11 | none | python, c/c++ |
| 18 | NRNB | 11 | none | python, javascript |
| 19 | Apache Software Foundation | 11 | none | java, c, c++ |
| 20 | The Julia Language | 11 | none | julia |
| 21 | Git | 11 | none | shell, c |
| 22 | OSGeo | 11 | none | python, javascript, java |
| 23 | Blender Foundation | 11 | none | c, python |
| 24 | GNOME Foundation | 11 | none | c, rust, gtk |
| 25 | KDE Community | 11 | none | c++, qt |

Other 11/11 (ranks 26-43, same tie): FFmpeg, GNU Octave, GNU Radio, BRL-CAD, JPF team, Linux Foundation, NetBSD, FreeBSD, R project, RTEMS, ScummVM, VideoLAN, MariaDB, LLVM, INCF, FOSSi, 52°North, LibreOffice.

### 2c. Near misses: 10 of 11 (check the missing year before treating as a real gap)

| Org | Years | Missing year | Note |
|---|---|---|---|
| Wikimedia Foundation | 10 | 2025 | Back in 2026. Python/JS/PHP, a real web option. |
| rocket.chat | 10 | 2016 | In every year 2017-2026. |
| Open Robotics | 10 | 2017 | |
| Eclipse Foundation | 10 | 2021 | |
| Drupal Association | 10 | 2021 | |
| Mifos Initiative | 10 | 2021 | |
| JdeRobot | 10 | 2016 | |
| ArduPilot | 10 | 2016 | |
| ns-3 | 10 | 2016 | |
| CGAL | 10 | 2016 | |
| DBpedia | 10 | 2016 | |
| OpenWISP | 10 | 2016 | |
| PEcAn | 10 | 2016 | |
| PostgreSQL | 10 | 2016 | |
| CNCF | 10 | 2016 | |
| OWASP | 10 | 2017 | |
| openSUSE | 10 | 2019 | |
| freifunk | 10 | 2020 | |
| Liquid Galaxy | 10 | 2018 | |
| Global Alliance for Genomics and Health | 10 | 2025 | |
| QEMU | 10 | 2024 | |
| Ste\|\|ar group | 10 | 2019 | |
| Inkscape | 10 | 2026 (verify) | Present 2016-2025, not found in my 2026 read |
| BeagleBoard.org | 10 | 2026 (verify) | Present 2016-2025, not found in my 2026 read |

### 2d. Shortlist orgs not at 10-11 (for Section 3 context)

| Org | Years | Years found |
|---|---|---|
| CircuitVerse | 8 | 2019-2026 |
| Learning Equality | 6 | 2021-2026 |

Total distinct orgs per year are in Section 0. Orgs with 8-9 of 11 (for example Debian, Ceph, CloudCV, FOSSASIA, Haiku, Internet Archive, mlpack, Mixxx, OpenCV) are not listed individually.

---

## 3. Shortlist: 10 beginner-fit orgs for Python / JS / web

Fit criteria (INTERPRETATION): (1) stack matches Python, JavaScript/TypeScript or web, (2) listed in 2025 and 2026, (3) 8+ of 11 years, (4) takes several projects a year (more slots means more chances), (5) publishes an open chat or forum.

Project counts: number of project records in the org's archive record per year, 2023-2025 (SO, **single source**). 2026: **not available** (2026 projects are not in the archive yet; per-org 2026 URLs returned 404). Slot counts are projects accepted, not applicants, so odds per applicant are unknown. Applicant numbers per org were not found.

GitHub label links are standard GitHub search URLs. I did not open them, so the label name and whether it is used is **unverified** by me. Check the repo's CONTRIBUTING page for the label each org actually uses.

Chat/contact: exactly as the org publishes in its GSoC record (SO, accessed 2026-10-30).

| Rank | Org | Consistency | Slots 2023 / 2024 / 2025 / 2026 |
|---|---|---|---|
| 1 (Top 3) | Zulip | 11/11 | 13 / 17 / 12 / n/a |
| 2 (Top 3) | AOSSIE | 11/11 | 6 / 18 / 19 / n/a |
| 3 (Top 3) | Rocket.Chat | 10/11 | 10 / 17 / 19 / n/a |
| 4 | Oppia Foundation | 11/11 | 5 / 7 / 6 / n/a |
| 5 | Python Software Foundation (umbrella) | 11/11 | 22 / 30 / 16 / n/a |
| 6 | Sugar Labs | 11/11 | 8 / 11 / 11 / n/a |
| 7 | CircuitVerse | 8/11 | 5 / 5 / 7 / n/a |
| 8 | MetaBrainz | 11/11 | 7 / 8 / 7 / n/a |
| 9 | Learning Equality | 6/11 | 3 / 5 / 5 / n/a |
| 10 | Django Software Foundation | 11/11 | 1 / 4 / 3 / n/a |

Per-org detail:

### 1. Zulip (Top 3)
- Why: Python/Django backend plus TypeScript web client. 11/11 years and 12-17 projects a year. (FACT: counts, stack.) HYPOTHESIS: Zulip documents a structured newcomer path; I did not read it. Verify before the plan starts.
- Good-first-issue: https://github.com/zulip/zulip/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22 (label unverified; Zulip may use "help wanted", check https://github.com/zulip/zulip/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
- Chat: https://chat.zulip.org/ (published in SO). Ideas page: https://zulip.readthedocs.io/en/latest/outreach/gsoc.html
- Past ideas: 2024 "Migrate Zulip's JavaScript codebase to TypeScript"; 2024 "Cluster of priority features on Settings/Groups UI"; 2023 "Improving Zulip Terminal" (SO 2024, 2023 records, titles only).

### 2. AOSSIE (Top 3)
- Why: Python, JavaScript, Flutter. 11/11 years. 18-19 projects in each of the last two years, the most of the web-fit orgs. HYPOTHESIS: many small repos means an easy first PR; unverified.
- Good-first-issue (org-wide search): https://github.com/search?q=org%3AAOSSIE-Org+label%3A%22good+first+issue%22+state%3Aopen&type=issues (label unverified)
- Chat: Discord https://discord.gg/xnmAPS7zqB and https://discord.gg/fuuWX4AbJt (published in SO). Ideas: https://github.com/AOSSIE-Org/Info/blob/main/GSoC-Ideas/2026/index.md
- Past ideas: 2025 "BenefactionPlatform-Ergo: Expanding Fundraising Capabilities on Ergo" (https://github.com/AdityaGupta20871/GSOC_REPORT/blob/main/README.md); 2025 "Devr.AI: Sustaining and scaling OSS via AI powered DevRel"; 2024 "PictoPy", "Resonate Version 2 Proposal".

### 3. Rocket.Chat (Top 3)
- Why: JavaScript/TypeScript/Node, direct match for a JS developer. 10/11 years (only 2016 missing). 17-19 projects a year in 2024-2025. HYPOTHESIS: heavy AI-assistant projects in 2024-2025 suggest ideas lean to apps and integrations rather than core, which can suit a PM; unverified.
- Good-first-issue: https://github.com/RocketChat/Rocket.Chat/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22 (label unverified)
- Chat: https://open.rocket.chat/channel/opensource2026 (published in SO, a 2026 channel; the 2027 channel name is unknown). Forum: https://forums.rocket.chat/t/welcome-to-google-summer-of-code-2026-with-rocket-chat/22692
- Ideas: https://github.com/RocketChat/google-summer-of-code/blob/main/google-summer-of-code-2026.md
- Past ideas: 2025 "End to End Encrypted Message Handling for Ruqola" (https://github.com/RocketChat/ruqola/pull/8); 2024 "Embedded Chat 2024"; 2023 "UiKit Playground 2.0".

### 4. Oppia Foundation
- Why: Python backend, Angular/TypeScript front end, 11/11. Only 5-7 projects a year, so fewer slots. (FACT: counts.) HYPOTHESIS: structured onboarding for new contributors; not verified.
- Good-first-issue: https://github.com/oppia/oppia/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22 (label unverified)
- Chat: no chat link published; GitHub Discussions https://github.com/oppia/oppia/discussions (SO). Ideas: https://github.com/oppia/oppia/wiki/Google-Summer-of-Code-2026
- Past ideas: 2025 "Acceptance Tests"; 2025 "Android lint infrastructure and fixes"; 2024 "Make CI and pre-push hooks more efficient"; 2023 "Contributor Dashboard Admin Stats Table".

### 5. Python Software Foundation (umbrella)
- Why: 11/11, 16-30 projects a year, the most slots overall. It is an umbrella: you pick a sub-org (examples in the 2025 projects: Mission Support System, Borg Collective, ilastik). ESTIMATE: more breadth than depth; plan needs one sub-org chosen early.
- Good-first-issue: no single repo. Choose a sub-org first (list at https://python-gsoc.org/ideas.html), then search its repo.
- Chat/contact: https://python-gsoc.org/index.html#contact ; mailing list https://mail.python.org/mailman/listinfo/gsoc-general (SO). Ideas: https://python-gsoc.org/ideas.html
- Past ideas: 2024 "Extending MNE-Python's Databrowser"; 2023 "FURY: Update UI widget + Explore new UI Framework"; 2025 "Borg Collective: Implement Unified File Selector, Password Change UI, and File dialog for exclusions".

### 6. Sugar Labs
- Why: Python and JavaScript/TypeScript (Music Blocks, Sugarizer). 11/11. 8-11 projects a year.
- Good-first-issue: https://github.com/sugarlabs/musicblocks/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22 (label unverified)
- Chat: Matrix https://matrix.to/#/#sugar:matrix.org ; Discord https://discord.com/channels/1078051575580336249/1078051576284975226 (SO). Ideas: https://github.com/sugarlabs/GSoC/blob/master/Ideas-2026.md
- Past ideas: 2025 "Music Blocks v4 Masonry Module"; 2025 "Advanced JavaScript Editor with MusicBlocks Interactions"; 2023 "Sugarizer Vue.JS Core".

### 7. CircuitVerse
- Why: JavaScript, Ruby on Rails, Vue. Fewer years (8 of 11, 2019-2026) but steady 5-7 projects. Ruby is outside the CEO's stated stack; the Vue simulator work is JS.
- Good-first-issue: https://github.com/CircuitVerse/CircuitVerse/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22 (label unverified)
- Chat: org lists https://circuitverse.org/slack (labelled "mailingList" in SO) and GitHub Discussions https://github.com/CircuitVerse/CircuitVerse/discussions. Ideas: https://github.com/CircuitVerse/CircuitVerse/wiki/GSoC'26-Project-List
- Past ideas: 2025 "Development of Desktop Application and Completion of Vue Simulator"; 2025 "Open Hardware Component Library"; 2023 "Completing Vue.js Simulator: Integration and Transition to TypeScript".

### 8. MetaBrainz
- Why: Python (Flask-type web services), Postgres; 11/11; 7-8 projects a year. Web back end plus Android and Perl.
- Good-first-issue: https://github.com/metabrainz/listenbrainz-server/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22 (repo and label unverified)
- Chat: no chat link published in SO beyond https://metabrainz.org/contact. Ideas: https://wiki.musicbrainz.org/Development/Summer_of_Code/2026
- Past ideas: 2025 "Centralized Notification System for MetaBrainz"; 2024 "Add Syndication Feeds to ListenBrainz"; 2023 "BookBrainz: Import Other Open Databases".

### 9. Learning Equality
- Why: Django plus Vue, the closest to the CEO's stack in the lower half. Only 6 of 11 years and 3-5 projects a year, so fewer slots.
- Good-first-issue: https://github.com/learningequality/kolibri/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22 (label unverified)
- Contact: community forum https://community.learningequality.org/ ; email gsoc@learningequality.org (SO). No chat published. Ideas: https://docs.google.com/document/d/e/2PACX-1vShAAywLDbBu5WH-Wv44rxetISCOQmHxBwxDw63Nt_OcpPVIZW2jjT8sd_GLTpeNvspze8W-_c9JUdl/pub
- Past ideas: 2025 "Legacy Compatible prototype of a Rich Text Editor"; 2025 "Kolibri Community Library"; 2024 "Implement a Prototype of an Accessible Sortable Table".

### 10. Django Software Foundation
- Why: pure Python/Django, 11/11. Fewest slots on the list (1 / 4 / 3). Ranked last because chances are lowest, not because the work is a poor fit.
- Good-first-issue: Django tracks tickets in Trac, not GitHub labels. Trac "easy pickings" query is the usual route: https://code.djangoproject.com/query?status=!closed&easy=1 (not opened by me, unverified).
- Contact: forum https://forum.djangoproject.com/c/internals/mentorship/10 (SO). Ideas: https://code.djangoproject.com/wiki/SummerOfCode2026
- Past ideas: 2025 "Django Admin: Add Keyboard Shortcuts and Command Palette"; 2025 "Bring django-template-partials into core"; 2024 "Django ORM support for composite primary keys".

---

## What this means for us

- Start with the Top 3 (Zulip, AOSSIE, Rocket.Chat): all web or Python/JS, all with 10+ projects a year and an open chat channel. Keep Oppia or PSF as a backup pick, not a fourth.
- Do not wait for the 2027 org list (expected Feb 2027, HYPOTHESIS). These orgs have appeared 10-11 times in 11 years, so contributions made now are likely to count. No org has promised a 2027 slot.
- Before the plan relies on any link: verify the good-first-issue label names and read each org's contributor guide. I did not.

## Suggested opportunity signals (for Rohan Kulkarni and Arjun Mehta)

- FACT (single source): 2024-2025 projects at Rocket.Chat and AOSSIE include several AI-assistant/agent ideas (examples: "AI Assistant to help with understanding Rocket.Chat core codebase", 2024; "Devr.AI" 2025). LOW confidence as a product signal; one source, titles only.

## Gaps I could not verify

1. 2 orgs missing from my 2026 read (183 vs official 185). Unknown which.
2. Sample projects for each org in Section 1: not collected (only the 10 shortlisted).
3. 2026 project counts: archive not populated; 2026 slots for each org unknown.
4. GitHub label names (good first issue) and each org's contributor guide: not opened.
5. 2027 program dates and org list: not published as of 2026-10-30 (not found).
6. Applicant counts per org (acceptance odds): not found.
7. 2026 N flags and 10/11 near misses can be false from chunk-edge loss; check before dropping any org.
8. Oppia, MetaBrainz, Learning Equality, Django: chat channels not published in the GSoC record; I did not look elsewhere.

---

## 4. 12-week contribution plan (Lakshmi Narayanan)

Status: DRAFT for CEO review. Written 2026-10-30 by Lakshmi Narayanan. Task PROD-1.

Sources: Section 3 of this file only. Every link below is from Section 3. I added no new URLs, label names or channel names.

### 4.1 Assumptions and labels

- ASSUMPTION: the CEO has 8-10 hours a week (day job). The plan uses 8 hours as the base and 10 as the stretch.
- HYPOTHESIS: GSoC 2027 org announcement late Feb 2027; contributor applications mid/late March to early April 2027. The 2027 timeline is not published as of 2026-10-30.
- ESTIMATE: all targets below. They are not promises and not facts.
- UNVERIFIED (from Section 3 gaps): label names, contributor guides, 2027 chat channels, 2027 idea lists. Week 1 checks them first.
- The CEO does all posting, chatting and emailing personally. Agents never post or contact anyone. Agents may draft text for the CEO to send.

### 4.2 Strategy

- Weeks 1-2: explore Zulip, AOSSIE and Rocket.Chat. For each: read the contributor guide, set up the dev environment, lurk in chat, find 3 candidate issues.
- End of week 2 (Sun 15 Nov): pick ONE primary org and ONE backup from the three.
- Weeks 3-12: go deep on the primary. Spend about 80% of hours on primary, 20% on backup (reading, one small PR).

Primary-org decision rule. Score each org 0-2 on five criteria (max 10). Highest total wins. Second is the backup.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | Dev env running in 2 hours or less | no | with effort | yes |
| 2 | Beginner issues you could do now (found via Section 3 links) | 0 | 1-2 | 3 or more |
| 3 | A maintainer or contributor replied to a public question within 7 days | no | slow | yes |
| 4 | An idea on the ideas page you would want to build (2026 page used as a proxy) | none | maybe | clear yes |
| 5 | Stack fit and enjoyment (Python/JS/web) | low | ok | high |

Tie-break: Zulip (11/11 years, Python plus TypeScript). Rocket.Chat has 10/11 years; AOSSIE has the most small repos (HYPOTHESIS, unverified).

### 4.3 Week-by-week plan (Mon 2 Nov 2026 to Sun 24 Jan 2027)

Hours: about 8 a week. Weeks 8 and 9 cover Christmas and New Year. Plan for 4-5 hours there (ASSUMPTION).

| Wk | Dates | Goal | Concrete actions | Done when |
|---|---|---|---|---|
| 1 | 2-8 Nov | Explore Zulip and AOSSIE | Read each contributor guide. Set up the Zulip dev env. Open the Section 3 issue links and confirm the real label names. Join chat and read. | Zulip dev env runs. Label names noted for both orgs. 3 candidate issues listed per org. |
| 2 | 9-15 Nov | Explore Rocket.Chat, then decide | Same steps for Rocket.Chat. Finish AOSSIE setup. Score all 3 orgs with the rule above. | 3 dev envs run (or a note why not). Scores written. Primary and backup chosen by Sun 15 Nov. |
| 3 | 16-22 Nov | Introduce and claim first issue | Post a short intro in primary chat (CEO posts). Read the issue thread. Ask one clear question. Claim one docs, test or typing issue as the org's guide says. | 1 intro posted. 1 issue claimed. |
| 4 | 23-29 Nov | First PR | Build the fix. Run the tests locally. Open the PR with the org's template. | 1 PR opened. |
| 5 | 30 Nov-6 Dec | Respond to review, second issue | Answer review comments within 48 hours. Claim a second small issue. Start reading the codebase around a likely GSoC idea. | PR 1 merged or has no open comments from you. 1 second issue claimed. |
| 6 | 7-13 Dec | Second PR and first review | Open PR 2. Review one other contributor's PR (comment on tests, typos, clarity). | 2 PRs opened total. 1 review comment given. |
| 7 | 14-20 Dec | Step up to a small bug | Pick a small bug or UI fix in the area of a likely idea. Ask the mentor-type question: "is this a good first step toward idea X?" | 1 bug issue claimed. 1 PR opened or in progress. |
| 8 | 21-27 Dec | Light week | Respond to review only. Read the 2026 ideas page again and shortlist 2 ideas. | Open PRs have no waiting comments. 2 ideas shortlisted. |
| 9 | 28 Dec-3 Jan | Light week, plan | Write a half-page note per shortlisted idea: problem, users, first 3 steps. Keep any PR moving. | 2 idea notes written. |
| 10 | 4-10 Jan | Medium PR | Open a medium PR (a small feature or bug that touches 2+ files) in the idea area. Review a second PR from someone else. | 1 medium PR opened. 2 reviews given in total. |
| 11 | 11-17 Jan | Merge push and attend calls | Close out review comments. Attend any public contributor call, if one is published (check the chat; do not assume). Backup org: one small PR. | 3 PRs merged in primary (ESTIMATE). Backup has 1 PR opened. |
| 12 | 18-24 Jan | Review and re-plan | Count merged PRs. Re-check org status in chat. Decide: stay with primary or switch to backup. List the 3 best ideas. | Checkpoint note written. Decision recorded. 4+ PRs opened in primary in total. |

### 4.4 First PRs by org

Likely first-PR types, best first: docs, tests, typing or small lint, small bug. Avoid large features until two PRs are merged. All links are from Section 3. Label names are unverified, so check the repo's contributing page.

| Org | Likely first-PR types | How to find them |
|---|---|---|
| Zulip | Docs fixes; small web-client bugs; TypeScript typing (the 2024 idea "Migrate Zulip's JavaScript codebase to TypeScript" suggests typing work exists, HYPOTHESIS) | Good-first-issue search: https://github.com/zulip/zulip/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22. If empty, use https://github.com/zulip/zulip/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22. Ask in https://chat.zulip.org/. Read https://zulip.readthedocs.io/en/latest/outreach/gsoc.html. |
| AOSSIE | Docs and README fixes; small UI or JS bugs in one small repo | Org-wide search: https://github.com/search?q=org%3AAOSSIE-Org+label%3A%22good+first+issue%22+state%3Aopen&type=issues. Pick one repo and stay in it. Ideas: https://github.com/AOSSIE-Org/Info/blob/main/GSoC-Ideas/2026/index.md. Chat: the two Discord links in Section 3. |
| Rocket.Chat | Docs; tests; small TypeScript fixes; app or integration issues (HYPOTHESIS: ideas lean to apps) | https://github.com/RocketChat/Rocket.Chat/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22. Ideas: https://github.com/RocketChat/google-summer-of-code/blob/main/google-summer-of-code-2026.md. Chat: https://open.rocket.chat/channel/opensource2026 (a 2026 channel; the 2027 name is unknown). Forum: https://forums.rocket.chat/t/welcome-to-google-summer-of-code-2026-with-rocket-chat/22692 |

First-PR rules (one worked example):
- Wrong: claim 3 issues at once and open one big PR with no prior question.
- Right: claim 1 issue, ask 1 clear question, open 1 small PR with tests, reply to review in 48 hours.
- Why: maintainers merge small, clear, tested PRs. One merged PR beats three stalled ones.

### 4.5 Community steps

The CEO does these personally. Agents may draft.

1. Introduce: one short message in chat. Who you are, your stack, the issue you want. No long life story.
2. Ask good questions: say what you tried, what you expected, what happened, and the exact error. One question per message.
3. Review others' PRs from week 6: comment on clarity, tests, typos. Do not nitpick style the linter already checks.
4. Attend public calls only if the org publishes them. None are listed in Section 3. Check the chat first.
5. Be steady: reply within 48 hours, show up weekly. Mentors judge reliability.
6. Follow each org's AI-use rules in its contributor guide (UNVERIFIED; read in week 1). Write your own PR text.

### 4.6 Proposal timeline (Feb to April 2027, all dates HYPOTHESIS)

| When | Milestone | Done when |
|---|---|---|
| Mon 25 Jan - Sun 21 Feb | Runway. Keep PRs flowing. Pick 1 idea (2 backups). Read the idea's code. | 1 idea chosen. Count of merged PRs recorded. |
| Late Feb (about 24 Feb) | GSoC org list announced. | Primary and backup orgs confirmed in or out. If out, use the fallback in 4.8. |
| Early March | Check the 2027 ideas page. Compare with your idea notes. Ask in chat whether your idea fits. | Idea matches a 2027 listed idea, or a new idea is agreed in chat. |
| By about 10 March | Proposal draft 1: problem, plan, timeline, deliverables, why you. | Draft exists. |
| 10-20 March | Mentor feedback round 1 (CEO shares draft where the org allows). | At least 1 piece of feedback received. |
| By about 20 March | Draft 2 with the feedback applied. Feedback round 2. | Draft 2 done. |
| Late March | Applications open (HYPOTHESIS: mid/late March). Final read-through. Check the org's proposal template. | Final proposal passes checklist. |
| Before the deadline (early April, HYPOTHESIS) | CEO submits on the official site. Submit at least 3 days early. | Submission confirmation saved. |

Agents may draft and edit text. The CEO submits and contacts mentors.

### 4.7 Targets (ESTIMATES)

- By end of week 12 (24 Jan): 4-5 PRs opened and 3-4 merged in primary org. Dev env running in all 3 orgs. 2+ reviews given.
- By end Feb: 5-8 merged PRs in primary org (ESTIMATE; at 8 hours a week this is a stretch, and 5 is the safer number). 1 idea chosen.
- By submission: 1 full proposal with at least 1 mentor feedback round. Set 10+ hours a week in March if possible.
- No target counts as a fact until the PR links are recorded in the weekly checkpoint.

### 4.8 Risks and fallback

| Risk | Likelihood (ESTIMATE) | What to do |
|---|---|---|
| Primary org is not selected for 2027 | Low to medium. No org promised a slot. | Switch to backup org (already has 1+ PR). Next options from Section 3: Oppia or PSF. Past merged PRs still show skill. |
| PRs are not merged in time | Medium | Open PRs early (week 4). Reply in 48 hours. Keep 2 PRs live at once. Pick the backup if the primary is slow for 3 weeks. |
| Issue is already taken or the label is wrong | Medium | Check the thread for a claim. Read the contributing page. Ask in chat. |
| Day job eats the hours | Medium to high | Keep 8 hours as the base. Light weeks 8 and 9 are planned. Drop the backup org before dropping the primary. |
| Org gives few slots or many applicants | Unknown (applicant counts not found) | Apply to primary plus one other org if the rules allow (check rules, UNVERIFIED). |
| Section 3 info is stale (2026 links used for 2027) | Medium | Re-check ideas pages and chat channels in week 1 and again in March. |

### 4.9 Weekly checkpoints (CEO tracks every Sunday)

Copy this block into the task log each week.

- Hours spent this week (target 8):
- PRs opened / merged / waiting on me (total):
- Reviews given (total):
- Chat messages posted and questions answered:
- Any maintainer reply within 7 days? (yes / no):
- Blockers:
- Next week's one goal:

Red flags (act the same week): 2 weeks with no PR activity; a PR with no reply from me for 5 days; hours under 5 for 2 weeks running.

Check date for the whole plan: Sun 15 Nov (org decision), then Sun 24 Jan (full review).
