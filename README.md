# The Mathematical Physics Project

A bilingual digital library of mathematical physics notes, PDFs, exercises, and research resources by Omar Corona Tejeda.

Website: https://artinnether.github.io/the_mathematical_physics_project/

## What You Can Find Here

- Mathematical physics notes and research-style PDFs.
- Quantum field theory resources, including Feynman prescriptions, residues, real poles, perturbative expansions, and Feynman diagrams.
- General relativity and ADM Hamiltonian formulation notes.
- Differential geometry and vector bundle materials.
- Linear algebra, calculus, differential equations, and control theory exercises.
- Bilingual material in Spanish and English where available.

## Featured Topics

- Mathematical physics
- Quantum field theory
- Feynman diagrams
- General relativity
- Differential geometry
- Calculus of variations
- Functional derivatives
- Linear algebra
- Differential equations
- Advanced undergraduate and graduate physics

## Suggested Citation

Corona Tejeda, Omar. *The Mathematical Physics Project*. Digital library of mathematical physics notes and exercises.
https://artinnether.github.io/the_mathematical_physics_project/

## Share

If this project helps your study, teaching, or research, share the website with students, colleagues, and physics/math communities:

https://artinnether.github.io/the_mathematical_physics_project/

## Repository Notes

This is a static GitHub Pages site. Main files:

- `index.html`: public landing page and resource library.
- `papers/`: topic landing pages for selected PDFs.
- `sitemap.xml`: search engine discovery map.
- `robots.txt`: search engine crawl instructions.
- `PROMOTION.md`: reusable launch and sharing checklist for new PDFs.
- `tools/generate_topic_pages.py`: generator for searchable paper pages and sitemap entries.
- `tools/paper_thumbnails.json`: source PDF, page, crop coordinates, and language for each featured figure.
- `tools/extract_paper_thumbnails.py`: reproduces the original PDF crops in `assets/` (requires `pdfplumber` and `Pillow`). Run `python3 tools/extract_paper_thumbnails.py` from the repository root.

When adding a publication, include it in both Latest and the full library, and add every language variant to `resourceDates` in `index.html`. The main book stays first, followed by the newest dated publications. Featured images use `data-src-es` / `data-src-en` and translated alt text; use a shared crop only when it has no language-specific prose. Gauge and Klein-Gordon notes have no illustrations, so their thumbnails reproduce equations from the PDFs. The thumbnail manifest records the exact selection for every card.

## Contact

Use the contact form on the website or the social links in the footer.
