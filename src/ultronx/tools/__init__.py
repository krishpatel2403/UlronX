"""Tools primitive — tool system with ABC interface and built-in tools."""

from __future__ import annotations

from ULTRONX.tools._stubs import BaseTool, ToolExecutor, ToolSpec

# Import built-in tools to trigger @ToolRegistry.register() decorators.
# Each is wrapped in try/except so the package loads even before the
# individual tool modules are created.
try:
    import ULTRONX.tools.calculator  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.think  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.retrieval  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.llm_tool  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.file_read  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.web_search  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.weather  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.fx_macro  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.code_interpreter  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.code_interpreter_docker  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.repl  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.storage_tools  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.mcp_adapter  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.channel_tools  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.http_request  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.docker_shell_exec  # noqa: F401
    import ULTRONX.tools.shell_exec  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.memory_manage  # noqa: F401
except ImportError:
    pass
try:
    import ULTRONX.tools.user_profile_manage  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.skill_manage  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.file_write  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.apply_patch  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.git_tool  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.db_query  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.pdf_tool  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.image_tool  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.audio_tool  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.knowledge_tools  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.text_to_speech  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.digest_collect  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.scan_chunks  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.knowledge_sql  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.apple_calendar  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.knowledge_search  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.browser  # noqa: F401
    import ULTRONX.tools.browser_axtree  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.tools.proactive_tools  # noqa: F401
except ImportError:
    pass

__all__ = ["BaseTool", "ToolExecutor", "ToolSpec"]
