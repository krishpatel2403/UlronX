"""Skill source resolvers — Hermes, OpenClaw, generic GitHub."""

from ULTRONX.skills.sources.base import ResolvedSkill, SourceResolver
from ULTRONX.skills.sources.github import GitHubResolver
from ULTRONX.skills.sources.hermes import HERMES_REPO_URL, HermesResolver
from ULTRONX.skills.sources.openclaw import OPENCLAW_REPO_URL, OpenClawResolver

__all__ = [
    "GitHubResolver",
    "HERMES_REPO_URL",
    "HermesResolver",
    "OPENCLAW_REPO_URL",
    "OpenClawResolver",
    "ResolvedSkill",
    "SourceResolver",
]
