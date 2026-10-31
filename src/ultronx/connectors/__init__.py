"""Data source connectors for Deep Research."""

from ULTRONX.connectors._stubs import (
    Attachment,
    BaseConnector,
    Document,
    SyncStatus,
)
from ULTRONX.connectors.store import KnowledgeStore

__all__ = ["Attachment", "BaseConnector", "Document", "KnowledgeStore", "SyncStatus"]

# Auto-register built-in connectors
import ULTRONX.connectors.obsidian  # noqa: F401

try:
    import ULTRONX.connectors.gmail  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.gmail_imap  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.gdrive  # noqa: F401
except ImportError:
    pass  # httpx may not be installed

try:
    import ULTRONX.connectors.notion  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.granola  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.gcontacts  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.imessage  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.apple_notes  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.apple_music  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.apple_contacts  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.apple_calendar  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.slack_connector  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.outlook  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.imap  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.gcalendar  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.dropbox  # noqa: F401
except ImportError:
    pass  # httpx may not be installed

try:
    import ULTRONX.connectors.whatsapp  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.oura  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.apple_health  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.strava  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.spotify  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.google_tasks  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.weather  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.github_notifications  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.hackernews  # noqa: F401
except ImportError:
    pass

try:
    import ULTRONX.connectors.news_rss  # noqa: F401
except ImportError:
    pass
