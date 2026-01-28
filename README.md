<<<<<<< HEAD
# DS Toolbox WK08
# แก้โค้ดหน้าขาว : D:\wk08-main\dstoolbox-wk08\.venv\html\view-source_https___wichit2s.github.io__static_courses_dstoolbox_slides_wk08.html
A modern web project for Data Science Toolbox Week 08.

## Project Structure

```
dstoolbox-wk08/
├── index.html      # Main HTML file
├── style.css       # Stylesheet
├── script.js       # JavaScript
├── .gitignore      # Git ignore file
├── README.md       # This file
└── .venv/          # Python virtual environment
```

## Features

- Responsive HTML5 structure
- Modern CSS3 styling with gradient backgrounds
- Interactive JavaScript functionality
- Clean and professional design

## Getting Started

1. Open `index.html` in your web browser
2. Or use a local server:
   ```bash
   # Using Python 3
   python -m http.server 8000
   
   # Using Python 2
   python -m SimpleHTTPServer 8000
   ```
3. Visit `http://localhost:8000` in your browser

## Development

The project is set up with:
- A virtual environment (`.venv`) for Python dependencies
- HTML, CSS, and JavaScript for the frontend
- Ready to expand with additional features

## License

MIT License - Feel free to use this project as a starter template.
=======
# Week 08 Assignment (DSToolbox)

งานที่ทำ (ตามใบงาน):
1) ✅ fix `wk08.html` / `html/slides_wk08.html` (แก้หน้าขาวจาก .slide display:none)
2) ✅ `pycaretflow.py` รัน workflow ของ PyCaret + สร้างสรุปแบบ Agent AI ลงไฟล์รายงาน
3) ✅ `pycaret_mcp_server` เขียน MCP Server สำหรับ PyCaret (ยึดแนวคิดจาก pandas-mcp-server)

## 1) Slides (wk08.html)

- ไฟล์สไลด์: `html/slides_wk08.html` และสำเนา `wk08.html`
- FIX ที่ทำ:
  - ใส่ class `active` ให้สไลด์แรกเป็น fallback
  - เพิ่ม JS fallback ถ้าไม่มีสไลด์ไหน active ให้โชว์สไลด์แรก

เปิดดูสไลด์ผ่าน GitHub Pages ได้ (แก้ลิงก์เป็น repo ของคุณ):
- `https://<username>.github.io/<repo>/wk08.html`
- `https://<username>.github.io/<repo>/html/slides_wk08.html`

## PyCaret Model Comparison Results

## 2) PyCaret Workflow Script (pycaretflow.py)

รันเพื่อสร้างรายงานผล compare_models + สรุปแบบ Agent AI:

```bash
uv run python pycaretflow.py
```
# Week 08 Assignment — Data Science Modules & Workflow (PyCaret + MCP)

งานที่ทำ (ตามใบงาน):

- ✅ fix `wk08.html` / `html/slides_wk08.html` (แก้หน้าขาวจาก `.slide { display: none }`)
- ✅ `pycaretflow.py` รัน workflow ของ PyCaret และสร้างรายงานผล
- ✅ `pycaret_mcp_server` MCP server สำหรับ PyCaret (simple stdio-based)

## Project Structure

```
WK08-main/
  pycaretflow.py
  pyproject.toml
  README.md
  wk08.html
  html/
    slides_wk08.html
  pycaret_mcp_server/
    server.py
  reports/
```

## Highlights

- Slides: fixed blank-screen issue by ensuring the first slide is a fallback and adding a JS fallback when no `.slide.active` exists.
- PyCaret: `pycaretflow.py` runs `setup()` and `compare_models()`, writes `reports/compare_models.md`, `reports/compare_models.csv`, and `reports/summary.json` (including an "agent critique").
- MCP server: small stdio MCP module under `pycaret_mcp_server` exposing helpers for model summaries and agent critique.

## How to run

Recommend Python 3.10 or 3.11 (PyCaret may not support 3.12). Example using `uv` task runner used in this project:

```powershell
cd WK08-main
uv sync
uv run python pycaretflow.py
```

To run the MCP server (stdio):

```powershell
uv run python -m pycaret_mcp_server.server
```

## Output files

- `reports/compare_models.md` — markdown table of model comparison
- `reports/compare_models.csv` — CSV table
- `reports/summary.json` — meta + best model + agent critique

## Checklist

- [x] Fix `wk08.html` (blank screen)
- [x] Add `pycaretflow.py` workflow and reports
- [x] Add `pycaret_mcp_server` MCP server
- [ ] Push to GitHub and share link

---

If you'd like, I can push the resolved conflicts and continue the rebase, or open any of these files for further edits.

