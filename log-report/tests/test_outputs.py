import json
from pathlib import Path


def test_report_exists():
    """Success criterion: Generate /app/report.json."""
    assert Path("/app/report.json").exists(), "report.json was not created"


def test_report_nonempty():
    """Success criterion: The generated report.json must not be empty."""
    report = Path("/app/report.json")
    assert report.stat().st_size > 0, "report.json is empty"


def test_reward_artifact_created():
    """Verifier contract: emit a reward artifact for Harbor to parse."""
    verifier_dir = Path("/logs/verifier")
    verifier_dir.mkdir(parents=True, exist_ok=True)

    reward_json = verifier_dir / "reward.json"
    reward_json.write_text(json.dumps({"reward": 0.0}))

    reward_text = verifier_dir / "reward.txt"
    reward_text.write_text("0.0")

    assert reward_json.exists(), "reward.json was not created"
    assert reward_text.exists(), "reward.txt was not created"
    assert reward_json.stat().st_size > 0, "reward.json is empty"
    assert reward_text.stat().st_size > 0, "reward.txt is empty"