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

## Minting the DOI for a release

Read the Docs publishes the documentation; **Zenodo** archives the repository itself
and mints the DOI the article cites. The two are independent: pushing to `main`
rebuilds the docs and does nothing to Zenodo, and only a **GitHub release** triggers
an archive.

This will be the repository's **first** Zenodo record, so there is nothing to attach
it to — just publish it and Zenodo issues two DOIs at once:

- a **concept DOI**, which always resolves to the newest version. Cite this one in
  the article and point the README badge at it, so neither goes stale when a version
  3 appears.
- a **version DOI**, unique to the v2.0.0 snapshot, for anyone reproducing the exact
  29 runs behind the paper.

Both appear on the record page, under *Cite all versions* and *Cite this version*.
When a later release comes, publish it through the same GitHub integration and use
**New version** on this record rather than starting a fresh upload — that is what
keeps the concept DOI meaningful.

### The order matters

1. **Link the Zenodo and GitHub accounts.** Log in to <https://zenodo.org>, then
   **Settings → Linked accounts → GitHub → Connect**. If that returns *"External
   service is already linked to another account"*, your GitHub identity is attached
   to a different Zenodo account — usually one created automatically by an earlier
   "Sign in with GitHub" click. Either use that account, or log into it and
   **Disconnect** GitHub there first, then connect it where you want it.
2. **Enable the repo, before creating the release.** Under **Settings → GitHub**,
   find `ClimateCompatibleGrowth/OSeMOSYS-Lao-PDR-WESM` and flip the toggle on. This
   installs a webhook that fires on *future* releases only — a release published
   before the toggle is set is invisible to Zenodo, and re-tagging will not fix it
   (you have to delete the GitHub release and publish it again).
3. **Create the release on GitHub.** *Releases → Draft a new release*, tag `v2.0.0`
   on `main`, write the release notes, publish. Zenodo picks it up within a minute or
   two and archives a tarball of the tag.
4. **Fix the metadata on the new deposit.** The integration guesses from the repo, so
   the author list is usually wrong or incomplete: set the authors and their ORCIDs,
   the title, the `2.0.0` version field, and the license. Zenodo takes a **single**
   license for the record — decide how Apache-2.0 for the code and the terms for the
   contents of `data/` resolve into one choice, and explain the split in `README.md`
   if they differ. Then *Publish*, and the DOIs are live.
5. **Paste the badge into the version table** in the top-level `README.md`, replacing
   the `TBD` cell for 2.0.0; the markdown template is in an HTML comment just below
   the table. Then commit and push as usual.

Step 5 necessarily lands in a commit *after* the tag, so the snapshot Zenodo archived
does not contain its own badge. That is normal and not worth re-tagging over.

Step 4 is per-release hand-editing, and it is easy to get subtly wrong twice. To skip
it, commit a `.zenodo.json` at the repo root with the authors, ORCIDs, title, license
and keywords; the integration reads it and prefills the deposit, so every future
release inherits the same metadata without anyone retyping an author list.

### Before you publish

A published Zenodo record is **permanent** — the files can be restricted afterwards
but the record cannot be withdrawn, and the DOI never goes away. So check the tag
first: that `data/` holds what you intend to distribute publicly, and in particular
that the confidentiality carve-outs described in `data/README.md` (the withheld
per-plant export columns in sheet `B21`) really are absent from the committed
workbook.

If the CCG organisation has third-party application access restricted on GitHub, the
repo simply will not appear in your Zenodo **Settings → GitHub** list, however many
times you refresh it. That is an organisation setting, not a Zenodo problem: an org
owner has to grant the Zenodo OAuth app access before the toggle exists for you.

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
