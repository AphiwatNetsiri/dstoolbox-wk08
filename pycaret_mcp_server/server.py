"""pycaret-mcp-server (MCP)

แนวคิด (ยึดโครงจาก pandas-mcp-server แบบมาตรฐาน):
- รันเป็น STDIO MCP Server
- expose tools ให้ client เรียกใช้

Tools ที่ให้บริการ:
1) pycaret_compare_diabetes: เปรียบเทียบโมเดลบน dataset ตัวอย่าง (diabetes) แล้วคืนตาราง top N
2) agent_critique_from_row: รับ metrics ของโมเดล (dict) แล้วสรุปข้อสังเกตแบบ Agent AI

วิธีรัน:
  uv run python -m pycaret_mcp_server.server

หมายเหตุ:
ไฟล์นี้ต้องการแพ็กเกจ `mcp` (Anthropic MCP SDK) และ `pycaret`
"""

from __future__ import annotations

from typing import Any, Dict, List


def _ensure_deps() -> None:
    try:
        import mcp  # noqa: F401
    except Exception as e:  # pragma: no cover
        raise RuntimeError(
            "Missing dependency: 'mcp'.\n"
            "Install with: uv add mcp\n"
            "(หรือ uv sync ถ้าเพิ่มไว้ใน pyproject.toml แล้ว)"
        ) from e


def _agent_critique(metrics: Dict[str, Any]) -> str:
    """Rule-based critique (เหมือน Agent AI)"""
    def f(key: str, default: float = 0.0) -> float:
        v = metrics.get(key, default)
        try:
            return float(v)
        except Exception:
            return default

    acc = f("Accuracy")
    auc = f("AUC")
    rec = f("Recall")
    prec = f("Prec.") if "Prec." in metrics else f("Precision")
    f1 = f("F1")

    notes: List[str] = []

    if acc >= 0.80:
        notes.append("Accuracy ดี (≥ 0.80) เหมาะใช้เป็น baseline/production ได้ในหลายกรณี")
    elif acc >= 0.70:
        notes.append("Accuracy ระดับพอใช้ (0.70–0.79) ควรลอง tune/เพิ่ม feature")
    else:
        notes.append("Accuracy ต่ำ (< 0.70) ควรทบทวน preprocessing/feature engineering")

    if f1 < acc - 0.10:
        notes.append("F1 ต่ำกว่า Accuracy มาก → อาจมี class imbalance (ดู confusion matrix)")

    if rec < 0.60:
        notes.append("Recall ต่ำ → เสี่ยง False Negative สูง (งานสุขภาพควรระวัง)")

    if prec < 0.60:
        notes.append("Precision ต่ำ → เสี่ยง False Positive สูง (ลองปรับ threshold/class weight)")

    if auc >= 0.80:
        notes.append("AUC ดี (≥ 0.80) แสดงว่าแยกกลุ่มได้ค่อนข้างดี")
    elif auc > 0:
        notes.append("AUC ยังไม่สูงมาก แนะนำลองโมเดล non-linear หรือ tune เพิ่ม")

    notes.append("แนะนำ: ทดสอบบน hold-out test set และรันหลาย seed เพื่อเช็ค overfitting")
    return "- " + "\n- ".join(notes)


def build_server():
    """Create FastMCP server instance."""
    _ensure_deps()
    from mcp.server.fastmcp import FastMCP

    mcp = FastMCP("pycaret-mcp-server")

    @mcp.tool()
    def pycaret_compare_diabetes(top_n: int = 10) -> Dict[str, Any]:
        """Compare models on PyCaret 'diabetes' dataset and return top N rows."""
        from pycaret.datasets import get_data
        from pycaret.classification import compare_models, pull, setup

        df = get_data("diabetes", verbose=False)
        target = "Outcome" if "Outcome" in df.columns else df.columns[-1]

        setup(
            data=df,
            target=target,
            session_id=123,
            train_size=0.7,
            verbose=False,
            html=False,
        )

        best = compare_models()
        results = pull()
        top_df = results.head(max(1, int(top_n)))
        best_row = results.iloc[0].to_dict()

        return {
            "dataset": "diabetes",
            "target": target,
            "best_model": str(best),
            "top_n": int(top_n),
            "table": top_df.to_dict(orient="records"),
            "best_metrics": best_row,
        }

    @mcp.tool()
    def agent_critique_from_row(metrics: Dict[str, Any]) -> str:
        """Summarize metrics like an evaluation agent."""
        return _agent_critique(metrics)

    return mcp


def main() -> None:
    mcp = build_server()
    mcp.run()


if __name__ == "__main__":
    main()
