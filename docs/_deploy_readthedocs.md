# Deploying the docs (maintainer note)

This file is **excluded from the Sphinx build** (see `exclude_patterns` in
`docs/conf.py`), so it never appears on the published site. It is a note to
maintainers, not documentation.

## How deployment works

Read the Docs builds from **git**, not from your local machine. Nothing you build
locally is ever published — `docs/_build/` is gitignored. The published site is
rebuilt automatically when you **push to the default branch** (`main`). The build
recipe is `.readthedocs.yaml` at the repo root: Ubuntu 22.04, Python 3.11,
`docs/requirements.txt`, config `docs/conf.py`, and it produces HTML plus PDF and
htmlzip.

So the whole loop is: **edit → preview locally → commit → push → RTD rebuilds.**

## One-time setup (not done yet)

As of this writing the repo has **no commits and no remote**. Until that is fixed
there is nothing for Read the Docs to build.

```powershell
cd C:\git\OSeMOSYS-Lao-PDR-WESM
git add -A
git commit -m "Version 2: model file, 29 scenario data files, and docs"
git remote add origin https://github.com/ClimateCompatibleGrowth/OSeMOSYS-Lao-PDR-WESM.git
git push -u origin main
```

Then, on <https://readthedocs.org>: **Import a Project**, pick the GitHub repo, and
let it build. Check that the resulting URL matches the one referenced in
`README.md` and `docs/index.md` (`osemosys-lao-pdr-wesm.readthedocs.io`); if it
differs, update those references. Importing also installs the webhook that triggers
every later build.

## Making a change (the routine loop)

```powershell
conda activate vig_base
cd C:\git\OSeMOSYS-Lao-PDR-WESM

# 1. edit the .md files in docs\

# 2. preview locally
python -m sphinx -b html docs docs\_build\html
start docs\_build\html\index.html

# 3. check it builds clean — warnings are errors on RTD-quality builds
python -m sphinx -b html -W docs docs\_build\html

# 4. ship it
git add -A
git commit -m "docs: <what changed>"
git push
```

The RTD build starts within a few seconds of the push and takes a couple of minutes.
Watch it under **Builds** on the project page; if it fails, the log there shows the
same Sphinx errors you would have seen in step 3.

Use `-E -a` to force a full rebuild after changing `conf.py` or renaming a page —
Sphinx's incremental cache misses those:

```powershell
python -m sphinx -b html -E -a docs docs\_build\html
```

## Environment

Build with the **`vig_base`** conda env: it has Sphinx 9.1.0, myst-parser,
sphinx-rtd-theme and linkify-it-py. The `base` env has Sphinx but is missing
myst-parser and sphinx-rtd-theme and will fail. RTD ignores both and installs
`docs/requirements.txt` itself, so local and remote versions can differ — which is
why a clean local build is a good signal but not a guarantee.

## Things that catch people out

- **A new page must be added to the `toctree` in `docs/index.md`.** Otherwise Sphinx
  warns that the document is not in any toctree and it is unreachable on the site.
- **Downloadable files are referenced relative to `docs/`**, e.g.
  ``{download}`... <../data/model.v.5.4.txt>` ``. The file must be committed to git
  or the RTD build fails even though your local build passed. The scenario zip is
  1.6 MB and is copied into the build output on every run.
- **`docs/_build/` is gitignored** — never commit it, and never expect it to appear
  on the site.
- **Cross-references between pages** use ``{doc}`page_name` `` with no `.md`
  extension, e.g. ``{doc}`execution_guide` ``.
- **RTD also builds PDF and htmlzip** (`formats:` in `.readthedocs.yaml`). A change
  that renders fine in HTML can still break the PDF build; check the Builds log if
  the PDF matters to you.
