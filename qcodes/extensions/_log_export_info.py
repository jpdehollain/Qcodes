from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

LOG = logging.getLogger(__name__)


def log_dataset_export_info(path: Path | None, **kwargs: Any) -> None:
    automatic = kwargs.get("automatic_export", False)
    auto_str = "automatically" if automatic else "manually"
    LOG.info("Dataset has been exported to: %s this was triggered %s.", path, auto_str)
