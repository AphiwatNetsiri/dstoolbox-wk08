<<<<<<< HEAD
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
"""PyCaret workflow (Week 08)

เป้าหมาย:
1) โหลดชุดข้อมูลตัวอย่าง (diabetes) จาก PyCaret
2) รัน setup() + compare_models() เพื่อจัดอันดับโมเดล
3) ดึงตารางผลลัพธ์ออกมา (pull)
4) สร้าง "Agent critique" แบบ rule-based (ใช้เป็นตัวอย่างการให้ AI ช่วยสรุป/ประเมิน)

วิธีรัน:
  uv run python pycaretflow.py

หมายเหตุ: สคริปต์นี้พยายามเลือกคอลัมน์ target ให้เอง (รองรับชื่อ target หลายแบบ)
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Tuple

import pandas as pd


def _pick_target_column(df: pd.DataFrame) -> str:
    """Pick a target column with common names. Fallback to the last column."""
    candidates = [
        "Outcome",
        "label",
        "Label",
        "target",
        "Target",
        "class",
        "Class",
        "Class variable",
    ]
    for c in candidates:
        if c in df.columns:
            return c
    return df.columns[-1]


def agent_critique(metrics_row: pd.Series) -> str:
    """Simple rule-based critique (ทำตัวเป็น Agent AI) จาก metrics ของโมเดลที่ดีที่สุด"""
    # ค่าในตาราง compare_models ของ PyCaret อาจเป็น float หรือ string
    def f(key: str, default: float = 0.0) -> float:
        v = metrics_row.get(key, default)
        try:
            return float(v)
        except Exception:
            return default

    acc = f("Accuracy")
    auc = f("AUC")
    rec = f("Recall")
    prec = f("Prec.") if "Prec." in metrics_row else f("Precision")
    f1 = f("F1")

    notes = []
    # เกณฑ์ตัวอย่าง (ปรับได้ตามงานจริง)
    if acc >= 0.80:
        notes.append("Accuracy ดี (≥ 0.80) เหมาะสำหรับเป็น baseline หรือใช้งานจริงได้ในหลายกรณี")
    elif acc >= 0.70:
        notes.append("Accuracy ระดับพอใช้ (0.70–0.79) แนะนำ tune/ลองเพิ่ม feature เพื่อดันคะแนน")
    else:
        notes.append("Accuracy ต่ำ (< 0.70) ควรกลับไปดู preprocessing/feature engineering")

    if f1 < acc - 0.10:
        notes.append("F1 ต่ำกว่า Accuracy ค่อนข้างมาก → อาจมี class imbalance (ควรดู confusion matrix)")

    if rec < 0.60:
        notes.append("Recall ค่อนข้างต่ำ → เสี่ยง False Negative สูง (ในงานแพทย์ควรระวัง)")

    if prec < 0.60:
        notes.append("Precision ค่อนข้างต่ำ → อาจมี False Positive เยอะ (ควรตั้ง threshold/ปรับ class weight)")

    if auc >= 0.80:
        notes.append("AUC ดี (≥ 0.80) แปลว่าโมเดลแยกกลุ่มได้ค่อนข้างดี")
    elif auc > 0:
        notes.append("AUC ยังไม่สูงมาก แนะนำลอง model ที่ non-linear หรือ tune เพิ่ม")

    notes.append("ข้อแนะนำ: ทำ cross-validation ซ้ำ/เปลี่ยน seed และทดสอบบน hold-out test set เพื่อตรวจ overfitting")
    return "- " + "\n- ".join(notes)


def run_pycaret_diabetes() -> Tuple[pd.DataFrame, Dict[str, Any]]:
    # import ภายในฟังก์ชัน เพื่อให้ไฟล์ import ได้แม้ผู้ใช้ยังไม่ติดตั้ง pycaret
    from pycaret.datasets import get_data
    from pycaret.classification import compare_models, pull, setup

    df = get_data("diabetes", verbose=False)
    target = _pick_target_column(df)

    # ตั้งค่าพื้นฐาน (ให้ผล reproducible)
    setup(
        data=df,
        target=target,
        session_id=123,
        train_size=0.7,
        verbose=False,
        html=False,
    )

    best = compare_models()
    results = pull()  # dataframe

    meta = {
        "dataset": "pycaret.datasets.get_data('diabetes')",
        "target": target,
        "best_model": str(best),
    }
    return results, meta


def main() -> None:
    out_dir = Path("reports")
    out_dir.mkdir(exist_ok=True)

    results_df, meta = run_pycaret_diabetes()

    # เก็บตารางผลลัพธ์
    results_md = results_df.to_markdown(index=False)
    (out_dir / "compare_models.md").write_text(results_md, encoding="utf-8")
    results_df.to_csv(out_dir / "compare_models.csv", index=False)

    # สรุปโมเดลที่ดีที่สุด (แถวแรกของตารางคือ best model เมื่อเรียงตามค่า default)
    best_row = results_df.iloc[0]
    critique = agent_critique(best_row)

    summary = {
        "meta": meta,
        "best_row": best_row.to_dict(),
        "agent_critique": critique,
    }
    (out_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print("=== PyCaret Compare Models (Top 5) ===")
    print(results_df.head(5).to_string(index=False))
    print("\n=== Agent Critique (rule-based) ===")
    print(critique)
    print("\nSaved to:")
    print(f"- {out_dir / 'compare_models.md'}")
    print(f"- {out_dir / 'compare_models.csv'}")
    print(f"- {out_dir / 'summary.json'}")


if __name__ == "__main__":
    main()
