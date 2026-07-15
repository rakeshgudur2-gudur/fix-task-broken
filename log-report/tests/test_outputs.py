from pathlib import Path

def test_report_exists():
    """Success criterion: Generate /app/report.json."""
    assert Path("/app/report.json").exists(), "report.json was not created"

def test_report_nonempty():
    """Success criterion: The generated report.json must not be empty."""
    report = Path("/app/report.json")
    assert report.stat().st_size > 0, "report.json is empty"