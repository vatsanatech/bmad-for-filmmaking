#!/usr/bin/env python3
"""
BMAD-FILM CEO Report PDF Generator
Converts BMAD-FILM-CEO-REPORT.md to a formatted PDF
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import Flowable
import re
import os

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_MD  = os.path.join(BASE_DIR, "BMAD-FILM-TEAM-REPORT.md")
OUTPUT_PDF = os.path.join(BASE_DIR, "BMAD-FILM-TEAM-REPORT.pdf")

# ── Brand Colours ──────────────────────────────────────────────────────────────
DARK_BG      = colors.HexColor("#0D0D0D")
ACCENT_GOLD  = colors.HexColor("#D4AF37")
ACCENT_RED   = colors.HexColor("#C0392B")
LIGHT_GREY   = colors.HexColor("#F4F4F4")
MID_GREY     = colors.HexColor("#CCCCCC")
TEXT_DARK    = colors.HexColor("#1A1A1A")
TEXT_MEDIUM  = colors.HexColor("#444444")
WHITE        = colors.white
TABLE_HEADER = colors.HexColor("#1A1A1A")
TABLE_ALT    = colors.HexColor("#F9F9F9")
STATUS_PEND  = colors.HexColor("#FFF3CD")
STATUS_DONE  = colors.HexColor("#D4EDDA")
DIVIDER      = colors.HexColor("#D4AF37")

# ── Page Setup ─────────────────────────────────────────────────────────────────
PAGE_W, PAGE_H = A4
MARGIN_L = 2.2 * cm
MARGIN_R = 2.2 * cm
MARGIN_T = 2.2 * cm
MARGIN_B = 2.2 * cm

# ── Styles ─────────────────────────────────────────────────────────────────────
def build_styles():
    base = getSampleStyleSheet()

    styles = {}

    styles["cover_title"] = ParagraphStyle(
        "cover_title",
        fontName="Helvetica-Bold",
        fontSize=26,
        textColor=ACCENT_GOLD,
        spaceAfter=6,
        alignment=TA_CENTER,
        leading=32,
    )
    styles["cover_subtitle"] = ParagraphStyle(
        "cover_subtitle",
        fontName="Helvetica",
        fontSize=13,
        textColor=WHITE,
        spaceAfter=4,
        alignment=TA_CENTER,
        leading=18,
    )
    styles["cover_meta"] = ParagraphStyle(
        "cover_meta",
        fontName="Helvetica",
        fontSize=10,
        textColor=MID_GREY,
        spaceAfter=3,
        alignment=TA_CENTER,
    )
    styles["cover_status"] = ParagraphStyle(
        "cover_status",
        fontName="Helvetica-Bold",
        fontSize=11,
        textColor=ACCENT_RED,
        spaceAfter=3,
        alignment=TA_CENTER,
    )
    styles["h1"] = ParagraphStyle(
        "h1",
        fontName="Helvetica-Bold",
        fontSize=15,
        textColor=ACCENT_GOLD,
        spaceBefore=18,
        spaceAfter=6,
        leading=20,
        borderPad=0,
    )
    styles["h2"] = ParagraphStyle(
        "h2",
        fontName="Helvetica-Bold",
        fontSize=12,
        textColor=TEXT_DARK,
        spaceBefore=12,
        spaceAfter=4,
        leading=16,
    )
    styles["h3"] = ParagraphStyle(
        "h3",
        fontName="Helvetica-Bold",
        fontSize=10.5,
        textColor=TEXT_MEDIUM,
        spaceBefore=8,
        spaceAfter=3,
        leading=14,
    )
    styles["body"] = ParagraphStyle(
        "body",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=TEXT_DARK,
        spaceAfter=5,
        leading=14,
    )
    styles["bullet"] = ParagraphStyle(
        "bullet",
        fontName="Helvetica",
        fontSize=9.5,
        textColor=TEXT_DARK,
        spaceAfter=3,
        leading=13,
        leftIndent=14,
        bulletIndent=4,
    )
    styles["code"] = ParagraphStyle(
        "code",
        fontName="Courier",
        fontSize=8,
        textColor=TEXT_DARK,
        backColor=LIGHT_GREY,
        spaceAfter=4,
        leading=12,
        leftIndent=10,
    )
    styles["caption"] = ParagraphStyle(
        "caption",
        fontName="Helvetica-Oblique",
        fontSize=8,
        textColor=TEXT_MEDIUM,
        spaceAfter=4,
        alignment=TA_CENTER,
    )
    styles["footer"] = ParagraphStyle(
        "footer",
        fontName="Helvetica",
        fontSize=7.5,
        textColor=TEXT_MEDIUM,
        alignment=TA_CENTER,
    )
    return styles


# ── Cover Page ─────────────────────────────────────────────────────────────────
class ColorRect(Flowable):
    """Full-width colour band."""
    def __init__(self, width, height, fill_color):
        super().__init__()
        self.width  = width
        self.height = height
        self.fill   = fill_color

    def draw(self):
        self.canv.setFillColor(self.fill)
        self.canv.rect(0, 0, self.width, self.height, stroke=0, fill=1)


def build_cover(styles, content_width):
    story = []

    # Dark header band
    band_h = 7 * cm
    story.append(ColorRect(content_width, band_h, DARK_BG))
    story.append(Spacer(1, -band_h))          # overlay text on the band

    story.append(Spacer(1, 1.6 * cm))
    story.append(Paragraph("BMAD-FILM", styles["cover_title"]))
    story.append(Paragraph("Breakthrough Method of Agile AI-Driven Filmmaking", styles["cover_subtitle"]))
    story.append(Spacer(1, 0.3 * cm))
    story.append(HRFlowable(width=content_width * 0.45, thickness=1.5,
                             color=ACCENT_GOLD, spaceAfter=8))
    story.append(Spacer(1, 3.2 * cm))          # clear the dark band

    story.append(Spacer(1, 0.8 * cm))
    story.append(Paragraph("Development Status Report", ParagraphStyle(
        "ds", fontName="Helvetica-Bold", fontSize=18,
        textColor=TEXT_DARK, alignment=TA_CENTER, spaceAfter=6)))
    story.append(Spacer(1, 0.4 * cm))

    meta_rows = [
        ("Prepared for", "Team Review"),
        ("Date",         "February 20, 2026"),
        ("Classification", "Internal"),
    ]
    meta_data = [[Paragraph(k, ParagraphStyle("mk", fontName="Helvetica-Bold",
                                               fontSize=9.5, textColor=TEXT_MEDIUM)),
                  Paragraph(v, ParagraphStyle("mv", fontName="Helvetica",
                                               fontSize=9.5, textColor=TEXT_DARK))]
                 for k, v in meta_rows]
    meta_table = Table(meta_data, colWidths=[content_width * 0.35, content_width * 0.55])
    meta_table.setStyle(TableStyle([
        ("ALIGN",       (0, 0), (-1, -1), "LEFT"),
        ("VALIGN",      (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",  (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING",(0,0), (-1, -1), 5),
        ("LINEBELOW",   (0, 0), (-1, -2), 0.5, MID_GREY),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 0.5 * cm))

    # Status badge
    status_data = [[Paragraph(
        "STATUS: Development Complete — Team Testing Pending",
        ParagraphStyle("sb", fontName="Helvetica-Bold", fontSize=10,
                       textColor=ACCENT_RED, alignment=TA_CENTER))]]
    status_table = Table(status_data, colWidths=[content_width * 0.9])
    status_table.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, -1), STATUS_PEND),
        ("BOX",          (0, 0), (-1, -1), 1.2, ACCENT_RED),
        ("TOPPADDING",   (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 8),
        ("ALIGN",        (0, 0), (-1, -1), "CENTER"),
    ]))
    story.append(status_table)
    story.append(PageBreak())
    return story


# ── Table Helpers ──────────────────────────────────────────────────────────────
def make_table(rows, col_widths, content_width, has_header=True):
    """Render a markdown-style table as a styled ReportLab Table."""
    s = getSampleStyleSheet()
    cell_body = ParagraphStyle("cb", fontName="Helvetica",   fontSize=8.5, leading=12, textColor=TEXT_DARK)
    cell_head = ParagraphStyle("ch", fontName="Helvetica-Bold", fontSize=8.5, leading=12, textColor=WHITE)

    data = []
    for i, row in enumerate(rows):
        style = cell_head if (i == 0 and has_header) else cell_body
        data.append([Paragraph(cell.strip(), style) for cell in row])

    # resolve column widths
    if col_widths:
        widths = [content_width * w for w in col_widths]
    else:
        n = len(rows[0])
        widths = [content_width / n] * n

    table = Table(data, colWidths=widths, repeatRows=1 if has_header else 0)
    ts = [
        ("BACKGROUND",    (0, 0), (-1, 0),  TABLE_HEADER),
        ("TEXTCOLOR",     (0, 0), (-1, 0),  WHITE),
        ("ALIGN",         (0, 0), (-1, -1), "LEFT"),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
        ("GRID",          (0, 0), (-1, -1), 0.4, MID_GREY),
        ("LINEBELOW",     (0, 0), (-1, 0),  1.5, ACCENT_GOLD),
    ]
    # alternate row shading
    for idx in range(1, len(data)):
        if idx % 2 == 0:
            ts.append(("BACKGROUND", (0, idx), (-1, idx), TABLE_ALT))
    table.setStyle(TableStyle(ts))
    return table


# ── Section Number → Gold Prefix ──────────────────────────────────────────────
def section_prefix(num_str, styles):
    return Paragraph(
        f'<font color="#D4AF37"><b>{num_str}</b></font>',
        styles["h1"]
    )


# ── MD → ReportLab ─────────────────────────────────────────────────────────────
def parse_md_to_story(md_path, styles, content_width):
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    story = []
    i = 0
    in_code_block = False
    code_lines = []

    # table col-width hints keyed by section number
    table_widths = {
        "2":  [0.45, 0.20, 0.35],
        "4":  [0.40, 0.60],
        "4g": [0.25, 0.75],
        "5":  [0.05, 0.35, 0.15, 0.45],
        "6.3":[0.40, 0.60],
        "7":  [0.30, 0.15, 0.55],
        "8":  [0.30, 0.20, 0.25, 0.25],
        "9":  [0.40, 0.30, 0.30],
        "11": [0.30, 0.35, 0.35],
        "12": [0.22, 0.39, 0.39],
        "14": [0.40, 0.25, 0.35],
    }
    current_section = ""

    while i < len(lines):
        line = lines[i].rstrip("\n")

        # ── code block ─────────────────────────────────────────────────────────
        if line.strip().startswith("```"):
            if in_code_block:
                in_code_block = False
                block_text = "\n".join(code_lines)
                for cl in code_lines:
                    story.append(Paragraph(
                        cl.replace(" ", "&nbsp;").replace("<", "&lt;").replace(">", "&gt;"),
                        styles["code"]
                    ))
                story.append(Spacer(1, 4))
                code_lines = []
            else:
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # ── blank line ─────────────────────────────────────────────────────────
        if not line.strip():
            story.append(Spacer(1, 4))
            i += 1
            continue

        # ── HR ─────────────────────────────────────────────────────────────────
        if re.match(r"^-{3,}$", line.strip()):
            story.append(HRFlowable(width=content_width, thickness=0.6,
                                    color=DIVIDER, spaceAfter=6, spaceBefore=6))
            i += 1
            continue

        # ── headings ───────────────────────────────────────────────────────────
        h1 = re.match(r"^# (.+)$", line)
        h2 = re.match(r"^## (.+)$", line)
        h3 = re.match(r"^### (.+)$", line)

        if h1:
            # skip cover-page headings (already built)
            text = h1.group(1).strip()
            if text.startswith("BMAD-FILM"):
                i += 1
                continue
            # extract section number
            sec = re.match(r"^(\d+)\.", text)
            if sec:
                current_section = sec.group(1)
            story.append(HRFlowable(width=content_width, thickness=1.2,
                                    color=ACCENT_GOLD, spaceBefore=8, spaceAfter=4))
            story.append(Paragraph(text, styles["h1"]))
            i += 1
            continue

        if h2:
            text = h2.group(1).strip()
            # sub-section tracking
            sec = re.match(r"^(\d+\.\d+)", text)
            if sec:
                current_section = sec.group(1)
            story.append(Paragraph(text, styles["h2"]))
            i += 1
            continue

        if h3:
            text = h3.group(1).strip()
            # skip cover meta lines
            if any(k in text for k in ["Prepared for", "Date:", "Classification", "Status:"]):
                i += 1
                continue
            story.append(Paragraph(text, styles["h3"]))
            i += 1
            continue

        # ── markdown table ─────────────────────────────────────────────────────
        if line.strip().startswith("|"):
            table_rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                row_line = lines[i].strip()
                # skip separator row (|---|---|)
                if re.match(r"^\|[-| :]+\|$", row_line):
                    i += 1
                    continue
                cells = [c.strip() for c in row_line.strip("|").split("|")]
                table_rows.append(cells)
                i += 1
            if table_rows:
                widths = table_widths.get(current_section, None)
                story.append(make_table(table_rows, widths, content_width))
                story.append(Spacer(1, 8))
            continue

        # ── bullet list ────────────────────────────────────────────────────────
        if line.strip().startswith(("- ", "* ", "+ ")):
            text = line.strip()[2:].strip()
            # bold inline
            text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
            story.append(Paragraph(f"\u2022 &nbsp;{text}", styles["bullet"]))
            i += 1
            continue

        # ── numbered list ──────────────────────────────────────────────────────
        num_m = re.match(r"^(\d+)\. (.+)$", line.strip())
        if num_m:
            num  = num_m.group(1)
            text = num_m.group(2).strip()
            text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
            story.append(Paragraph(f"<b>{num}.</b> &nbsp;{text}", styles["bullet"]))
            i += 1
            continue

        # ── body paragraph ─────────────────────────────────────────────────────
        text = line.strip()
        # skip pure cover meta lines
        if re.match(r"^(###|Prepared for|Date:|Classification|Status:)", text):
            i += 1
            continue
        # inline bold/italic
        text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
        text = re.sub(r"\*(.+?)\*",   r"<i>\1</i>",   text)
        text = re.sub(r"`(.+?)`",     r"<font name='Courier'>\1</font>", text)
        story.append(Paragraph(text, styles["body"]))
        i += 1

    return story


# ── Page Template ──────────────────────────────────────────────────────────────
def on_first_page(canvas, doc):
    pass   # cover page has its own content


def on_later_pages(canvas, doc):
    w, h = A4
    canvas.saveState()

    # top rule
    canvas.setStrokeColor(ACCENT_GOLD)
    canvas.setLineWidth(0.8)
    canvas.line(MARGIN_L, h - 1.4 * cm, w - MARGIN_R, h - 1.4 * cm)

    # header text
    canvas.setFont("Helvetica-Bold", 7.5)
    canvas.setFillColor(TEXT_MEDIUM)
    canvas.drawString(MARGIN_L, h - 1.2 * cm, "BMAD-FILM — Development Status Report")
    canvas.setFont("Helvetica", 7.5)
    canvas.drawRightString(w - MARGIN_R, h - 1.2 * cm, "Confidential — Internal Use Only")

    # bottom rule
    canvas.line(MARGIN_L, MARGIN_B, w - MARGIN_R, MARGIN_B)

    # footer
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(TEXT_MEDIUM)
    canvas.drawString(MARGIN_L, MARGIN_B * 0.55,
                      "BMAD-FILM v7.0 | February 20, 2026 | claude-sonnet-4-6")
    canvas.drawRightString(w - MARGIN_R, MARGIN_B * 0.55,
                           f"Page {doc.page}")

    canvas.restoreState()


# ── Main ───────────────────────────────────────────────────────────────────────
def generate_pdf():
    styles       = build_styles()
    content_width = PAGE_W - MARGIN_L - MARGIN_R

    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        leftMargin=MARGIN_L,
        rightMargin=MARGIN_R,
        topMargin=MARGIN_T + 0.6 * cm,
        bottomMargin=MARGIN_B + 0.6 * cm,
        title="BMAD-FILM Development Status Report",
        author="BMAD-FILM System",
        subject="CEO Development Status Brief — February 2026",
    )

    story  = build_cover(styles, content_width)
    story += parse_md_to_story(INPUT_MD, styles, content_width)

    doc.build(story,
              onFirstPage=on_first_page,
              onLaterPages=on_later_pages)

    print(f"\n✅  PDF generated successfully:\n    {OUTPUT_PDF}\n")


if __name__ == "__main__":
    generate_pdf()
