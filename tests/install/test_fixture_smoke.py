"""Smoke test that the tmp_ULTRONX_home fixture works."""

from __future__ import annotations

from pathlib import Path

from ULTRONX.core import config as config_mod


def test_fixture_redirects_default_config_dir(tmp_ULTRONX_home: Path) -> None:
    assert config_mod.DEFAULT_CONFIG_DIR == tmp_ULTRONX_home
    assert tmp_ULTRONX_home.exists()
    assert (tmp_ULTRONX_home / ".state").exists()
    assert (tmp_ULTRONX_home / ".state" / "models").exists()


def test_fixture_redirects_config_path(tmp_ULTRONX_home: Path) -> None:
    assert config_mod.DEFAULT_CONFIG_PATH == tmp_ULTRONX_home / "config.toml"
