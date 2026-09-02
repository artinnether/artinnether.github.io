from html import escape
from pathlib import Path
from urllib.parse import quote

BASE_URL = "https://artinnether.github.io/the_mathematical_physics_project/"
ROOT = Path(__file__).resolve().parents[1]
PAPERS_DIR = ROOT / "papers"

PAPERS = [
    {
        "slug": "lie-groups-universal-enveloping-algebra",
        "title": "From Lie Groups to the Universal Enveloping Algebra",
        "spanish_title": "De grupos de Lie al álgebra envolvente universal",
        "pdf": "notes_lie_algebras_universal_enveloping_algebra.pdf",
        "pdf_alt": "notas_algebras_lie_envolvente_universal.pdf",
        "category": "Lie Algebras",
        "description": "Notes on infinitesimal rotations, the Lie algebra associated with a Lie group, and the construction of the universal enveloping algebra.",
        "keywords": "Lie groups, Lie algebras, infinitesimal rotations, universal enveloping algebra, generators, commutators, mathematical physics",
        "lastmod": "2026-09-02",
    },
    {
        "slug": "c-star-algebras-dagger-notation",
        "title": "On C*-Algebras and the Dagger Notation",
        "spanish_title": "Sobre C*-álgebras y la notación daga",
        "pdf": "C_star_Algebras_and_Dagger_Notation_EN.pdf",
        "pdf_alt": "Algebras_C_estrella_y_Notacion_Daga_ES.pdf",
        "category": "Operator Algebras",
        "description": "Self-contained notes on C*-algebras, bounded operators, Hilbert adjoints, Dirac notation, Pauli matrices, the Bloch sphere, and unbounded operators.",
        "keywords": "C-star algebra, C dagger algebra, bounded operators, Hilbert adjoint, operator norm, Dirac notation, Pauli matrices, Bloch sphere, unbounded operators, quantum mechanics",
        "lastmod": "2026-07-16",
    },
    {
        "slug": "homological-algebra-category-modules",
        "title": "Homological Algebra in the Category of Modules",
        "spanish_title": "Álgebra Homológica en la Categoría de Módulos",
        "pdf": "Homological_Algebra_in_the_Category_of_Modules_EN.pdf",
        "pdf_alt": "Algebra_Homologica_en_la_Categoria_de_Modulos_ES.pdf",
        "category": "Homological Algebra",
        "description": "Notes on chain complexes, chain homotopy, projective and injective resolutions, derived functors, Ext, and Tor in the category of modules.",
        "keywords": "homological algebra, category of modules, chain complexes, projective resolutions, injective resolutions, derived functors, Ext, Tor, algebra",
        "lastmod": "2026-07-06",
    },
    {
        "slug": "feynman-prescription-residues-real-poles",
        "title": "Feynman Prescription, Residues, and Regularization of Real Poles",
        "spanish_title": "Prescripción de Feynman, residuos y regularización de polos reales",
        "pdf": "Feynman_Prescription_Residues_and_Real_Poles_EN.pdf",
        "pdf_alt": "Feynman_Prescription_Residues_and_Real_Poles_ES.pdf",
        "category": "Quantum Field Theory",
        "description": "Self-contained notes on Laurent series, residues, principal value, and the +i epsilon Feynman prescription for real poles.",
        "keywords": "Feynman prescription, residues, real poles, principal value, quantum field theory, i epsilon, mathematical physics",
    },
    {
        "slug": "lambda-phi4-zero-dimensional-feynman-diagrams",
        "title": "Perturbative Expansion and Feynman Diagrams in the Zero-Dimensional Lambda Phi Four Model",
        "spanish_title": "Expansión perturbativa y diagramas de Feynman en el modelo lambda phi cuatro de dimensión cero",
        "pdf": "Expansion_Perturbativa_y_Diagramas_de_Feynman_en_el_Modelo_lambda_phi4_de_Dimension_Cero.pdf",
        "category": "Quantum Field Theory",
        "description": "Notes on the zero-dimensional lambda phi four model, perturbative expansions, generating functions, and Feynman diagram structure.",
        "keywords": "lambda phi four, Feynman diagrams, perturbative expansion, zero dimensional field theory, quantum field theory",
    },
    {
        "slug": "lorentz-invariance-klein-gordon-field-action",
        "title": "Lorentz Invariance of the Klein-Gordon Field and Action",
        "spanish_title": "Invariancia de Lorentz del campo y la acción de Klein-Gordon",
        "pdf": "Lorentz_Invariance_of_the_Klein_Gordon_Field_and_Action.pdf",
        "category": "Relativistic Field Theory",
        "description": "A note on the Klein-Gordon equation, Lorentz invariance of the d'Alembertian, and the Lagrangian action for a real scalar field.",
        "keywords": "Klein-Gordon equation, Lorentz invariance, scalar field, Lagrangian action, relativistic quantum field theory",
    },
    {
        "slug": "dyson-series-vacuum-correlation-functions",
        "title": "Free Vacuum, Interacting Vacuum, Dyson Series and Correlation Functions",
        "spanish_title": "Vacío libre, vacío interactuante, serie de Dyson y funciones de correlación",
        "pdf": "Relacion entre el Vacio Libre, el Vacio Interactuante, Serie de Dyson y las Funciones de Correlacion.pdf",
        "category": "Quantum Field Theory",
        "description": "Notes on free and interacting vacua, the Dyson series, perturbative computation, and correlation functions in quantum field theory.",
        "keywords": "Dyson series, interacting vacuum, free vacuum, correlation functions, perturbation theory, quantum field theory",
    },
    {
        "slug": "adm-hamiltonian-equations-general-relativity",
        "title": "Hamiltonian ADM Equations of General Relativity",
        "spanish_title": "Ecuaciones Hamiltonianas de ADM de la Relatividad General",
        "pdf": "epsilon-Ecuaciones Hamiltonianas de ADM de la Relatividad General.pdf",
        "category": "General Relativity",
        "description": "A mathematical physics note on the ADM Hamiltonian formulation of general relativity and the structure of its equations.",
        "keywords": "ADM formalism, Hamiltonian equations, general relativity, mathematical relativity, canonical gravity",
    },
    {
        "slug": "field-variations-vector-bundles-connection",
        "title": "Field Variations on Vector Bundles with Connection",
        "spanish_title": "Variaciones de campos en haces vectoriales con conexión",
        "pdf": "Field Variations on Vector Bundles with Connection A Unified Active and Passive Interpretation.pdf",
        "category": "Differential Geometry",
        "description": "A geometric study of field variations on vector bundles with connection, including active and passive interpretations.",
        "keywords": "vector bundles, connection, field variations, differential geometry, gauge geometry, mathematical physics",
    },
    {
        "slug": "brachistochrone-problem-calculus-of-variations",
        "title": "The Brachistochrone Problem via Calculus of Variations",
        "spanish_title": "El problema de la braquistócrona mediante cálculo de variaciones",
        "pdf": "The_Brachistochrone_Problem__Time_Minimization_via_Calculus_of_Variations-Corona.pdf",
        "category": "Classical Mechanics",
        "description": "A derivation of the brachistochrone curve as a time-minimization problem using the calculus of variations.",
        "keywords": "brachistochrone problem, calculus of variations, classical mechanics, Euler-Lagrange equation, variational methods",
    },
    {
        "slug": "the-einbein-relativistic-systems",
        "title": "The Einbein in Relativistic Systems",
        "spanish_title": "El einbein en sistemas relativistas",
        "pdf": "The Einbein.pdf",
        "category": "Relativity",
        "description": "A short note on the einbein formalism and its role in relativistic systems and reparametrization-invariant actions.",
        "keywords": "einbein, relativistic systems, reparametrization invariance, relativistic action, mathematical physics",
    },
]

SITEMAP_PDFS = [
    ("notas_algebras_lie_envolvente_universal.pdf", "2026-09-02", "0.9"),
    ("notes_lie_algebras_universal_enveloping_algebra.pdf", "2026-09-02", "0.9"),
    ("Algebras_C_estrella_y_Notacion_Daga_ES.pdf", "2026-07-16", "0.9"),
    ("C_star_Algebras_and_Dagger_Notation_EN.pdf", "2026-07-16", "0.9"),
    ("Algebra_Homologica_en_la_Categoria_de_Modulos_ES.pdf", "2026-07-06", "0.8"),
    ("Homological_Algebra_in_the_Category_of_Modules_EN.pdf", "2026-07-06", "0.8"),
    ("Feynman_Prescription_Residues_and_Real_Poles_ES.pdf", "2026-06-17", "0.8"),
    ("Feynman_Prescription_Residues_and_Real_Poles_EN.pdf", "2026-06-17", "0.8"),
    ("Expansion_Perturbativa_y_Diagramas_de_Feynman_en_el_Modelo_lambda_phi4_de_Dimension_Cero.pdf", "2026-06-09", "0.8"),
    ("Lorentz_Invariance_of_the_Klein_Gordon_Field_and_Action.pdf", "2026-06-06", "0.8"),
    ("Relacion entre el Vacio Libre, el Vacio Interactuante, Serie de Dyson y las Funciones de Correlacion.pdf", "2026-05-27", "0.7"),
    ("Libro.pdf", "2026-05-09", "0.9"),
    ("Control_Theory_Excercises.pdf", "2026-05-09", "0.6"),
    ("Field Variations on Vector Bundles with Connection A Unified Active and Passive Interpretation.pdf", "2026-05-09", "0.7"),
    ("epsilon-Ecuaciones Hamiltonianas de ADM de la Relatividad General.pdf", "2026-04-23", "0.7"),
    ("The_Brachistochrone_Problem__Time_Minimization_via_Calculus_of_Variations-Corona.pdf", "2026-04-23", "0.7"),
    ("The Einbein.pdf", "2026-04-23", "0.7"),
    ("On_the_Functional_Derivative_of_the_Scalar_Field_Action_and__the_Associated_Global_Functional.pdf", "2026-04-23", "0.7"),
    ("Linear_Algebra_Exercises.pdf", "2026-04-23", "0.6"),
    ("Formulacion Matematica de las Imagenes de Heisenberg, Schrodinger y Dirac.pdf", "2026-04-23", "0.7"),
    ("Forma Heurística de la Ecuación de Dirac.pdf", "2026-04-23", "0.7"),
    ("Fijación_Gauge_en_la_Integral_de_Camino_y_el_Determinante_de_Faddeev_Popov.pdf", "2026-04-23", "0.7"),
    ("El_grupo_SU2_como_grupo_de_Lie_y_Vision_Fisica.pdf", "2026-04-23", "0.7"),
    ("Differential_Equations_Exercises.pdf", "2026-04-23", "0.6"),
    ("Composite_Quantum_Systems_and_Their_Wave_Functions-3.pdf", "2026-04-23", "0.7"),
    ("Calculus_excercises.pdf", "2026-04-23", "0.6"),
]


def enc(path):
    return quote(path, safe="/:")


def render_paper(paper):
    url = f"{BASE_URL}papers/{paper['slug']}.html"
    pdf_url = f"{BASE_URL}{enc(paper['pdf'])}"
    pdf_alt = paper.get("pdf_alt")
    alt_link = ""
    if pdf_alt:
        alt_link = f'<a href="../{enc(pdf_alt)}" class="secondary-action">Spanish PDF</a>'

    share_text = quote(f"{paper['title']} - The Mathematical Physics Project")
    share_url = quote(url, safe="")

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>{escape(paper['title'])} | The Mathematical Physics Project</title>
  <meta name="description" content="{escape(paper['description'])}" />
  <meta name="keywords" content="{escape(paper['keywords'])}" />
  <meta name="author" content="Omar Corona Tejeda" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <link rel="canonical" href="{url}" />
  <link rel="icon" href="../tmpp_logo.png" type="image/png" />
  <link rel="apple-touch-icon" href="../tmpp_logo.png" />
  <meta property="og:site_name" content="The Mathematical Physics Project" />
  <meta property="og:title" content="{escape(paper['title'])}" />
  <meta property="og:description" content="{escape(paper['description'])}" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{BASE_URL}tmpp_logo.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{escape(paper['title'])}" />
  <meta name="twitter:description" content="{escape(paper['description'])}" />
  <meta name="twitter:image" content="{BASE_URL}tmpp_logo.png" />
  <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "ScholarlyArticle",
      "headline": "{escape(paper['title'])}",
      "alternativeHeadline": "{escape(paper['spanish_title'])}",
      "description": "{escape(paper['description'])}",
      "url": "{url}",
      "encoding": {{
        "@type": "MediaObject",
        "contentUrl": "{pdf_url}",
        "encodingFormat": "application/pdf"
      }},
      "author": {{
        "@type": "Person",
        "name": "Omar Corona Tejeda",
        "url": "{BASE_URL}"
      }},
      "isPartOf": {{
        "@type": "CollectionPage",
        "name": "The Mathematical Physics Project",
        "url": "{BASE_URL}"
      }},
      "about": "{escape(paper['category'])}",
      "inLanguage": "en"
    }}
  </script>
  <style>
    :root {{
      --ink: #111827;
      --muted: #526071;
      --brand: #1f2a30;
      --gold: #d8c28a;
      --paper: rgba(255, 255, 255, 0.76);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      min-height: 100vh;
      color: var(--ink);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: url("../fondo.png") center / cover fixed no-repeat;
    }}
    header {{
      background: linear-gradient(180deg, rgba(31,42,48,0.98), rgba(31,42,48,0.90));
      border-bottom: 1px solid rgba(216, 194, 138, 0.45);
      box-shadow: 0 14px 38px rgba(15, 23, 42, 0.20);
    }}
    nav {{
      width: min(1120px, calc(100% - 32px));
      margin: 0 auto;
      min-height: 86px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 14px;
      color: white;
      text-decoration: none;
      font-weight: 800;
    }}
    .brand img {{
      width: 48px;
      height: 48px;
      border-radius: 999px;
      border: 2px solid rgba(255,255,255,0.78);
    }}
    .nav-links {{
      display: flex;
      flex-wrap: wrap;
      justify-content: flex-end;
      gap: 16px;
      font-size: 0.95rem;
      font-weight: 700;
    }}
    .nav-links a {{ color: white; text-decoration: none; }}
    .nav-links a:hover {{ text-decoration: underline; }}
    main {{
      width: min(1040px, calc(100% - 32px));
      margin: 0 auto;
      padding: 52px 0 72px;
    }}
    .hero {{
      display: grid;
      gap: 24px;
      padding: 36px;
      border: 1px solid rgba(31, 42, 48, 0.12);
      border-radius: 20px;
      background: var(--paper);
      box-shadow: 0 22px 54px rgba(15, 23, 42, 0.10);
      backdrop-filter: blur(7px);
    }}
    .eyebrow {{
      margin: 0;
      color: #526071;
      font-size: 0.78rem;
      font-weight: 800;
      letter-spacing: 0.18em;
      text-transform: uppercase;
    }}
    h1 {{
      max-width: 860px;
      margin: 0;
      color: var(--ink);
      font-size: clamp(2.1rem, 5vw, 4.4rem);
      line-height: 1.03;
      letter-spacing: 0;
    }}
    .summary {{
      max-width: 820px;
      margin: 0;
      color: var(--muted);
      font-size: 1.16rem;
      line-height: 1.72;
    }}
    .actions, .share {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      align-items: center;
    }}
    .primary-action, .secondary-action, .share a {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 44px;
      padding: 0 16px;
      border-radius: 10px;
      color: white;
      text-decoration: none;
      font-weight: 800;
    }}
    .primary-action {{ background: var(--brand); }}
    .secondary-action {{ background: #475569; }}
    .share a {{ background: #2563eb; }}
    .share a:nth-child(2) {{ background: #111827; }}
    .share a:nth-child(3) {{ background: #16a34a; }}
    .details {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 18px;
      margin-top: 18px;
    }}
    .panel {{
      padding: 22px;
      border: 1px solid rgba(31, 42, 48, 0.12);
      border-radius: 12px;
      background: rgba(255, 255, 255, 0.66);
    }}
    .panel h2 {{
      margin: 0 0 10px;
      font-size: 1.08rem;
    }}
    .panel p, .panel li {{
      color: var(--muted);
      line-height: 1.62;
    }}
    .panel ul {{
      margin: 0;
      padding-left: 20px;
    }}
    footer {{
      width: min(1040px, calc(100% - 32px));
      margin: 0 auto;
      padding: 0 0 42px;
      color: var(--muted);
      text-align: center;
    }}
    @media (max-width: 760px) {{
      nav {{ align-items: flex-start; flex-direction: column; padding: 18px 0; }}
      .nav-links {{ justify-content: flex-start; }}
      .hero {{ padding: 24px; }}
      .details {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <header>
    <nav aria-label="Site navigation">
      <a class="brand" href="../">
        <img src="../tmpp_logo.png" alt="" />
        <span>The Mathematical Physics Project</span>
      </a>
      <div class="nav-links">
        <a href="../#latest">Latest</a>
        <a href="../#pdfs">Library</a>
        <a href="../#newsletter">Subscribe</a>
        <a href="../#contacto">Contact</a>
      </div>
    </nav>
  </header>
  <main>
    <article class="hero">
      <p class="eyebrow">{escape(paper['category'])}</p>
      <h1>{escape(paper['title'])}</h1>
      <p class="summary">{escape(paper['description'])}</p>
      <div class="actions">
        <a href="../{enc(paper['pdf'])}" class="primary-action" target="_blank" rel="noopener noreferrer">Read PDF</a>
        <a href="../{enc(paper['pdf'])}" class="secondary-action" download>Download PDF</a>
        {alt_link}
      </div>
      <div class="share" aria-label="Share this paper">
        <a href="https://www.linkedin.com/sharing/share-offsite/?url={share_url}" target="_blank" rel="noopener noreferrer">LinkedIn</a>
        <a href="https://twitter.com/intent/tweet?url={share_url}&text={share_text}" target="_blank" rel="noopener noreferrer">X</a>
        <a href="https://api.whatsapp.com/send?text={share_text}%20{share_url}" target="_blank" rel="noopener noreferrer">WhatsApp</a>
      </div>
    </article>
    <section class="details" aria-label="Paper details">
      <div class="panel">
        <h2>Why this page exists</h2>
        <p>This page gives the PDF a searchable public home with a clear title, summary, metadata, and share links. It helps students, teachers, and researchers discover the resource before opening the document.</p>
      </div>
      <div class="panel">
        <h2>Related search topics</h2>
        <ul>
          {''.join(f'<li>{escape(item.strip())}</li>' for item in paper['keywords'].split(',')[:6])}
        </ul>
      </div>
    </section>
  </main>
  <footer>
    <p>Omar Corona Tejeda - The Mathematical Physics Project</p>
  </footer>
</body>
</html>
"""


def write_sitemap():
    entries = [
        ("", "2026-06-27", "weekly", "1.0"),
    ]
    entries += [(f"papers/{paper['slug']}.html", paper.get("lastmod", "2026-06-27"), "monthly", "0.9") for paper in PAPERS]
    entries += [(pdf, date, "monthly", priority) for pdf, date, priority in SITEMAP_PDFS]
    body = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lastmod, changefreq, priority in entries:
        url = BASE_URL + enc(loc)
        body.extend([
            "  <url>",
            f"    <loc>{url}</loc>",
            f"    <lastmod>{lastmod}</lastmod>",
            f"    <changefreq>{changefreq}</changefreq>",
            f"    <priority>{priority}</priority>",
            "  </url>",
        ])
    body.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(body) + "\n", encoding="utf-8")


def main():
    PAPERS_DIR.mkdir(exist_ok=True)
    for paper in PAPERS:
        (PAPERS_DIR / f"{paper['slug']}.html").write_text(render_paper(paper), encoding="utf-8")
    write_sitemap()


if __name__ == "__main__":
    main()
