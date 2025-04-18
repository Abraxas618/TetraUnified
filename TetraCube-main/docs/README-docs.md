# TetraCube Documentation System

This folder (`/docs/`) contains the sovereign-grade documentation system for the TetraCube cryptographic suite.

---

## Overview

This documentation is designed to build automatically using [Sphinx](https://www.sphinx-doc.org/) and [Read the Docs](https://readthedocs.org/).

It provides:
- Full module documentation (`modules.rst`)
- Project homepage (`index.rst`)
- Custom sovereign black+green theme (`_static/custom.css`)
- Auto-generated API references

---

## Structure

| File/Folder | Purpose |
|:------------|:--------|
| `conf.py` | Main configuration file for Sphinx and theme settings |
| `index.rst` | Root table of contents and project introduction |
| `modules.rst` | Auto-documentation of TetraCube Python modules |
| `requirements.txt` | Python dependencies for ReadTheDocs to build properly |
| `_static/custom.css` | Custom sovereign-themed CSS for black and green style |

---

## Building Locally

To preview the documentation locally:

```bash
cd docs/
pip install -r requirements.txt
make html
```

The HTML output will be inside `_build/html/`.

Open `index.html` in a browser to view it.

---

## Read the Docs Integration

- `.readthedocs.yaml` in the root of the repository automatically triggers the build
- ReadTheDocs will detect:
  - Python environment
  - Install `docs/requirements.txt`
  - Run Sphinx using `docs/conf.py`

---

## Sovereign Style Customization

The sovereign black+green theme is implemented via:

- `_static/custom.css`
- Linked inside `conf.py` via `app.add_css_file('custom.css')`

Feel free to adjust colors if you wish to evolve the sovereign aesthetic.

---

## Authors

- **Michael Tass MacDonald**
- Aliases: **Abraxas618**, **BaramayStation**

Sovereign custodian of the TetraCube Project.

---

## License

Documentation and source licensed under Apache 2.0 / MIT, consistent with the TetraCube project licensing.

---
