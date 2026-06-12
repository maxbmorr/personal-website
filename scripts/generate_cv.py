from __future__ import annotations

import argparse
import html
from pathlib import Path
import shutil
import subprocess
import tempfile
import webbrowser


PROFILE = {
    "name": "Maxwell Morrison",
    "title": "Electrical Engineering and Applied Mathematics Student",
    "location": "Newark, DE",
    "email": "maxbmorr@udel.edu",
    "personal_email": "maxbenmorr@gmail.com",
    "phone": "443-825-5800",
    "linkedin": "linkedin.com/in/maxwellbmorrison",
    "website": "maxwellmorrison.net",
    "updated": "June 2026",
    "summary": (
        "University of Delaware student pursuing electrical engineering and applied mathematics, "
        "with interests in signal processing, embedded systems, machine learning, computational "
        "neural information engineering, and practical engineering tools."
    ),
}


EDUCATION = [
    {
        "institution": "University of Delaware",
        "location": "Newark, DE",
        "date": "Expected May 2027",
        "details": [
            "B.S. Electrical Engineering, College of Engineering",
            "B.S. Applied Mathematics, College of Arts and Sciences",
            "GPA: 3.6",
        ],
    },
    {
        "institution": "Dulaney High School",
        "location": "Timonium, MD",
        "date": "May 2023",
        "details": ["High School Diploma"],
    },
]


COURSEWORK = {
    "Electrical Engineering": [
        "ELEG479, Introduction to Biomedical Imaging - A",
    ],
    "Computing / Computational Methods": [
        "ELEG467, Introduction to Computational Methods - A",
        "MATH426, Computational Mathematics - In Progress",
    ],
    "Applied Mathematics": [
        "MATH503, Complex Analysis - In Progress",
        "MATH508, Advanced Calculus with Nonlinear Dynamics - In Progress",
    ],
}


EXPERIENCE = [
    {
        "role": "Undergraduate Researcher",
        "organization": "Computational Neural Information Engineering Laboratory (CNIEL), University of Delaware",
        "location": "Newark, DE",
        "date": "Summer 2026",
        "bullets": [
            "Conducting undergraduate research under Dr. Austin Brockmeier in the Computational Neural Information Engineering Laboratory.",
        ],
    },
    {
        "role": "Supplemental Instructor / Teaching Assistant",
        "organization": "University of Delaware",
        "location": "Newark, DE",
        "date": "Jan. 2025 - Present",
        "bullets": [
            "Supplemental Instructor for CPEG202, Introduction to Digital Logic, under Dr. Nathan Lazarus and Mr. Thomas Lum.",
            "Hold weekly student support hours and assist students with course concepts, lab work, and problem solving.",
            "Support instruction through grading quizzes, exams, and course materials while serving as a primary contact for students.",
        ],
    },
    {
        "role": "Lab Assistant",
        "organization": "University of Delaware",
        "location": "Newark, DE",
        "date": "Jan. 2025 - Present",
        "bullets": [
            "Lab Assistant for ELEG205, Introduction to Analog Circuits, under Dr. Fouad Kiamilev.",
            "Lead weekly lab sessions and support students in circuit analysis, measurement techniques, and lab procedures.",
            "Assist with grading lab coursework and help ensure smooth operation of instructional lab activities.",
        ],
    },
    {
        "role": "Electrical Engineering Intern",
        "organization": "Henry Adams",
        "location": "Baltimore, MD",
        "date": "May 2025 - Aug. 2025",
        "bullets": [
            "Worked in Revit and AutoCAD to develop detailed drawings for contractors.",
            "Performed lighting simulations using AGi-32.",
            "Contributed to arc flash studies using SKM.",
        ],
    },
    {
        "role": "Undergraduate Researcher",
        "organization": "University of Delaware",
        "location": "Newark, DE",
        "date": "Jan. 2025 - Aug. 2025",
        "bullets": [
            "Worked with Dr. Mohsen Badiey and a team of undergraduate researchers on an electronic acoustic recorder.",
            "Developed a system using the ESP-WROOM-32D with custom hardware and firmware.",
            "Contributed to embedded system development in support of underwater acoustics research.",
        ],
    },
]


PROJECTS = [
    {
        "name": "Drone Eye",
        "tags": "Senior Design, Computer Vision, LiDAR",
        "description": (
            "Computer-vision and machine-learning drone detection system using LiDAR for depth perception "
            "and a custom-trained model to detect drones and estimate Cartesian coordinates through a graphical interface."
        ),
    },
    {
        "name": "Diabeasy",
        "tags": "UD Hackathon, Python",
        "description": "Encrypted Tkinter application for tracking insulin usage and calculating dosage amounts.",
    },
    {
        "name": "PitchMAX",
        "tags": "Hardware, Firmware",
        "description": (
            "Lower-cost pitch calling system inspired by PitchCom, using custom hardware and firmware "
            "to communicate called pitches between players."
        ),
    },
    {
        "name": "PyroPlan",
        "tags": "UD Hackathon, Web App, Simulation",
        "description": (
            "Web platform for modeling fire spread in level 1 materials server-side, making simulation "
            "accessible without local software installation."
        ),
    },
    {
        "name": "Mom Blood Sugar Tracker",
        "tags": "Healthcare, Web App",
        "description": (
            "Web platform that lets multiple caregivers submit orders and coordinate blood sugar and "
            "insulin-related care."
        ),
    },
]


PRESENTATIONS = [
    {
        "title": "DroneEye",
        "event": "University of Delaware Research Day",
        "date": "2026",
        "details": [
            "Presented a drone detection system using computer vision, machine learning, and LiDAR-based depth perception.",
            "Received the Research Day People's Choice Award for DroneEye.",
        ],
    },
]


AWARDS = [
    "2026 Research Day People's Choice Award Winner for DroneEye, Department of Electrical and Computer Engineering, University of Delaware",
    "Institute of Electrical and Electronics Engineers Delaware Bay Section Student Activities Award, Department of Electrical and Computer Engineering, University of Delaware",
    "Eagle Scout, 2021",
    "Dean's List",
]


AFFILIATIONS = [
    "IEEE Student Chapter",
    "IEEE Eta Kappa Nu",
    "Troop 97 (Scouts BSA)",
]


SKILLS = [
    "Signal processing",
    "Machine learning",
    "Embedded systems",
    "Digital logic",
    "Analog circuits",
    "Python",
    "Tkinter",
    "Revit",
    "AutoCAD",
    "AGi-32",
    "SKM",
    "ESP-WROOM-32D",
]


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def render_item(title: str, subtitle: str, date: str, bullets: list[str]) -> str:
    bullet_html = "\n".join(f"<li>{esc(bullet)}</li>" for bullet in bullets)
    return f"""
      <article class="entry">
        <div class="entry-head">
          <div>
            <h3>{esc(title)}</h3>
            <p class="subtitle">{esc(subtitle)}</p>
          </div>
          <p class="date">{esc(date)}</p>
        </div>
        <ul>{bullet_html}</ul>
      </article>
    """


def render_cv() -> str:
    education_html = "\n".join(
        render_item(
            item["institution"],
            item["location"],
            item["date"],
            item["details"],
        )
        for item in EDUCATION
    )
    experience_html = "\n".join(
        render_item(
            item["role"],
            f"{item['organization']} | {item['location']}",
            item["date"],
            item["bullets"],
        )
        for item in EXPERIENCE
    )
    projects_html = "\n".join(
        f"""
        <article class="entry compact">
          <div class="entry-head">
            <div>
              <h3>{esc(project["name"])}</h3>
              <p class="subtitle">{esc(project["tags"])}</p>
            </div>
          </div>
          <p>{esc(project["description"])}</p>
        </article>
        """
        for project in PROJECTS
    )
    presentations_html = "\n".join(
        render_item(
            item["title"],
            item["event"],
            item["date"],
            item["details"],
        )
        for item in PRESENTATIONS
    )
    awards_html = "\n".join(f"<li>{esc(award)}</li>" for award in AWARDS)
    affiliations_html = "\n".join(f"<li>{esc(item)}</li>" for item in AFFILIATIONS)
    skills_html = "\n".join(f"<li>{esc(skill)}</li>" for skill in SKILLS)
    coursework_html = "\n".join(
        f"""
        <div class="course-group">
          <h3>{esc(category)}</h3>
          <ul>{"".join(f"<li>{esc(course)}</li>" for course in courses)}</ul>
        </div>
        """
        for category, courses in COURSEWORK.items()
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(PROFILE["name"])} | CV</title>
  <style>
    :root {{
      --ink: #172033;
      --muted: #526070;
      --line: #d8dee8;
      --accent: #1f6f78;
    }}

    * {{
      box-sizing: border-box;
    }}

    body {{
      margin: 0;
      background: #f4f6f8;
      color: var(--ink);
      font-family: Arial, Helvetica, sans-serif;
      font-size: 10.8pt;
      line-height: 1.45;
    }}

    .page {{
      width: min(8.5in, calc(100% - 32px));
      margin: 24px auto;
      background: #fff;
      padding: 0.58in;
      box-shadow: 0 16px 42px rgba(23, 32, 51, 0.12);
    }}

    header {{
      border-bottom: 2px solid var(--accent);
      padding-bottom: 18px;
      margin-bottom: 22px;
    }}

    h1 {{
      margin: 0 0 5px;
      font-size: 27pt;
      line-height: 1;
      letter-spacing: 0;
    }}

    .headline {{
      margin: 0 0 10px;
      color: var(--accent);
      font-weight: 700;
    }}

    .contact {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px 14px;
      margin: 0;
      color: var(--muted);
      font-size: 9.6pt;
    }}

    .summary {{
      margin: 14px 0 0;
      max-width: 7.1in;
    }}

    section {{
      margin-top: 22px;
    }}

    h2 {{
      margin: 0 0 10px;
      border-bottom: 1px solid var(--line);
      padding-bottom: 5px;
      color: var(--accent);
      font-size: 12.8pt;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    h3 {{
      margin: 0;
      font-size: 11.5pt;
    }}

    .entry {{
      break-inside: avoid;
      page-break-inside: avoid;
      margin-top: 13px;
    }}

    .entry:first-child {{
      margin-top: 0;
    }}

    .entry-head {{
      display: flex;
      justify-content: space-between;
      gap: 20px;
      align-items: flex-start;
    }}

    .subtitle,
    .date {{
      margin: 3px 0 0;
      color: var(--muted);
      font-size: 9.7pt;
    }}

    .date {{
      flex: 0 0 auto;
      text-align: right;
      font-weight: 700;
    }}

    ul {{
      margin: 6px 0 0 18px;
      padding: 0;
    }}

    li {{
      margin-top: 3px;
    }}

    .grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }}

    .skills {{
      columns: 2;
    }}

    .coursework {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
    }}

    .course-group ul {{
      margin-top: 6px;
    }}

    .updated {{
      margin: 12px 0 0;
      color: var(--muted);
      font-size: 9pt;
    }}

    .compact p {{
      margin: 6px 0 0;
    }}

    @media print {{
      body {{
        background: #fff;
      }}

      .page {{
        width: auto;
        margin: 0;
        padding: 0;
        box-shadow: none;
      }}

      @page {{
        size: letter;
        margin: 0.55in;
      }}
    }}
  </style>
</head>
<body>
  <main class="page">
    <header>
      <h1>{esc(PROFILE["name"])}</h1>
      <p class="headline">{esc(PROFILE["title"])}</p>
      <p class="contact">
        <span>{esc(PROFILE["location"])}</span>
        <span>{esc(PROFILE["email"])}</span>
        <span>{esc(PROFILE["personal_email"])}</span>
        <span>{esc(PROFILE["phone"])}</span>
        <span>{esc(PROFILE["linkedin"])}</span>
        <span>{esc(PROFILE["website"])}</span>
      </p>
      <p class="summary">{esc(PROFILE["summary"])}</p>
      <p class="updated">Last updated {esc(PROFILE["updated"])}</p>
    </header>

    <section>
      <h2>Education</h2>
      {education_html}
    </section>

    <section>
      <h2>Selected Coursework</h2>
      <div class="coursework">{coursework_html}</div>
    </section>

    <section>
      <h2>Research, Teaching, and Engineering Experience</h2>
      {experience_html}
    </section>

    <section>
      <h2>Projects</h2>
      {projects_html}
    </section>

    <section>
      <h2>Presentations</h2>
      {presentations_html}
    </section>

    <section class="grid">
      <div>
        <h2>Awards</h2>
        <ul>{awards_html}</ul>
      </div>
      <div>
        <h2>Affiliations</h2>
        <ul>{affiliations_html}</ul>
      </div>
    </section>

    <section>
      <h2>Technical Skills</h2>
      <ul class="skills">{skills_html}</ul>
    </section>
  </main>
</body>
</html>
"""


def find_browser() -> Path | None:
    browser_names = ("chrome", "chrome.exe", "msedge", "msedge.exe", "chromium", "chromium.exe")
    for browser_name in browser_names:
        found = shutil.which(browser_name)
        if found:
            return Path(found)

    common_paths = (
        Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
        Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
        Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    )
    for path in common_paths:
        if path.exists():
            return path

    return None


def write_pdf(html_path: Path, pdf_path: Path) -> None:
    browser = find_browser()
    if browser is None:
        raise RuntimeError(
            "Could not find Chrome, Edge, or Chromium. Install one of those browsers, "
            "or run with --no-pdf and print cv.html to PDF manually."
        )

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    profile_dir = tempfile.mkdtemp(prefix="cv-browser-profile-")
    try:
        command = [
            str(browser),
            "--headless=new",
            "--disable-gpu",
            "--disable-extensions",
            "--disable-crash-reporter",
            "--disable-crashpad",
            "--no-first-run",
            "--no-default-browser-check",
            f"--user-data-dir={profile_dir}",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            html_path.as_uri(),
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            fallback_command = command.copy()
            fallback_command[1] = "--headless"
            result = subprocess.run(fallback_command, capture_output=True, text=True)
    finally:
        shutil.rmtree(profile_dir, ignore_errors=True)

    if result.returncode != 0:
        message = (result.stderr or result.stdout or "Unknown browser PDF error").strip()
        raise RuntimeError(f"PDF generation failed: {message}")

    if not pdf_path.exists():
        raise RuntimeError("PDF generation finished, but the PDF file was not created.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a printable CV as HTML and PDF.")
    parser.add_argument(
        "-o",
        "--output",
        default="cv.html",
        help="Output HTML path. Defaults to cv.html in this directory.",
    )
    parser.add_argument(
        "--pdf-output",
        default="cv.pdf",
        help="Output PDF path. Defaults to cv.pdf in this directory.",
    )
    parser.add_argument(
        "--no-pdf",
        action="store_true",
        help="Only generate HTML. Do not create a PDF.",
    )
    parser.add_argument(
        "--open",
        action="store_true",
        help="Open the generated PDF, or the HTML if --no-pdf is used.",
    )
    args = parser.parse_args()

    public_dir = Path(__file__).resolve().parent.parent / "public"
    output = Path(args.output)
    if not output.is_absolute():
        output = public_dir / output
    pdf_output = Path(args.pdf_output)
    if not pdf_output.is_absolute():
        pdf_output = public_dir / pdf_output

    output.parent.mkdir(parents=True, exist_ok=True)
    cv_html = "\n".join(line.rstrip() for line in render_cv().splitlines()) + "\n"
    output.write_text(cv_html, encoding="utf-8")
    print(f"Generated {output}")

    open_target = output
    if not args.no_pdf:
        write_pdf(output, pdf_output)
        print(f"Generated {pdf_output}")
        open_target = pdf_output

    if args.open:
        webbrowser.open(open_target.as_uri())


if __name__ == "__main__":
    main()

