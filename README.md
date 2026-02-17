# Week09 — myapp (Demo Profile Landing)

This repository contains a small static profile landing page (demo/fake CV) built with TailwindCSS (CDN) and served with Nginx inside a Docker container.

Purpose
- Simple, modern, Gen Z-style profile landing page for Week09 Docker assignment.
- Demonstrates responsive layout, animated background (CSS-only), and containerized static hosting.

Files
- `index.html` — complete single-file static site (Tailwind via CDN, CSS animations included).
- `Dockerfile` — builds an image from `nginx:alpine` and copies `index.html` into the web root.
- `docker-compose.yml` — optional compose file to run the site as service `myapp` mapped to host port 8080.

Quick Preview
- Open `index.html` directly in a browser for a local preview (requires network for Tailwind CDN).

Build & Run (Docker)

1) Build the Docker image (from project root):

```bash
docker build -t week09-myapp .
```

2) Run container directly:

```bash
docker run -d --name week09-myapp -p 8080:80 week09-myapp
```

3) Or use docker compose (recommended for quick start):

```bash
docker compose up -d
```

Then open: http://localhost:8080

Notes & Tips
- Tailwind is loaded via CDN inside `index.html`. You need internet access in the container/environment to fetch it.
- To change the public port, edit `docker-compose.yml` or the `-p` flag when running `docker run`.
- This is a static page — no backend required. All assets are inline/SVG; adding external assets requires copying them into the build context and updating the `Dockerfile`.

Customize
- Edit `index.html` to change name, copy, colors, or layout. The design uses utility classes from Tailwind and a small set of custom CSS inside a `<style>` block.

Files (paths)
- `index.html` — main page
- `Dockerfile` — Docker image recipe
- `docker-compose.yml` — compose convenience file

License
- Demo content for coursework. Use freely for the assignment.

สรุปสั้น ๆ (ภาษาไทย)
- สร้าง image: `docker build -t week09-myapp .`
- รัน: `docker run -d --name week09-myapp -p 8080:80 week09-myapp`
- หรือใช้ `docker compose up -d` แล้วเปิด `http://localhost:8080`
<<<<<<< HEAD
# DS Toolbox WK08
# แก้โค้ดหน้าขาว : D:\wk08-main\dstoolbox-wk08\.venv\html\view-source_https___wichit2s.github.io__static_courses_dstoolbox_slides_wk08.html
A modern web project for Data Science Toolbox Week 08.


# WK08 fix

[[View Slides](html/slides_wk08.html)](https://AphiwatNetsiri/dstoolbox-wk08/html/slides_wk08.html)

## PyCaret Model Comparison Results

### Model Performance Summary

| Model                           | Accuracy | AUC    | Recall | Precision | F1     | Kappa  | MCC    | TT (Sec) |
| ------------------------------- | -------- | ------ | ------ | --------- | ------ | ------ | ------ | -------- |
| Logistic Regression             | 0.7689   | 0.8047 | 0.5602 | 0.7208    | 0.6279 | 0.4641 | 0.4736 | 0.488    |
| Ridge Classifier                | 0.7670   | 0.8060 | 0.5497 | 0.7235    | 0.6221 | 0.4581 | 0.4690 | 0.006    |
| Linear Discriminant Analysis    | 0.7670   | 0.8055 | 0.5550 | 0.7202    | 0.6243 | 0.4594 | 0.4695 | 0.007    |
| Random Forest Classifier        | 0.7485   | 0.7911 | 0.5284 | 0.6811    | 0.5924 | 0.4150 | 0.4238 | 0.038    |
| Naive Bayes                     | 0.7427   | 0.7955 | 0.5702 | 0.6543    | 0.6043 | 0.4156 | 0.4215 | 0.007    |
| Gradient Boosting Classifier    | 0.7373   | 0.7914 | 0.5550 | 0.6445    | 0.5931 | 0.4013 | 0.4059 | 0.028    |
| Ada Boost Classifier            | 0.7372   | 0.7799 | 0.5275 | 0.6585    | 0.5796 | 0.3926 | 0.4017 | 0.020    |
| Extra Trees Classifier          | 0.7299   | 0.7788 | 0.4965 | 0.6516    | 0.5596 | 0.3706 | 0.3802 | 0.034    |
| Quadratic Discriminant Analysis | 0.7282   | 0.7894 | 0.5281 | 0.6558    | 0.5736 | 0.3785 | 0.3910 | 0.007    |
| Light Gradient Boosting Machine | 0.7133   | 0.7645 | 0.5398 | 0.6036    | 0.5650 | 0.3534 | 0.3580 | 0.051    |

### Best Performing Model

**Logistic Regression** achieved the highest accuracy at **76.89%** with an excellent AUC score of 0.8047, making it the recommended model for diabetes prediction.

### Dataset

- Diabetes classification dataset from PyCaret
- 768 samples with 9 features
- Binary classification task


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
- `https://AphiwatNetsiri/dstoolbox-wk08/html/slides_wk08.html`
- `https://AphiwatNetsiri/dstoolbox-wk08/html/slides_wk08.html`

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

