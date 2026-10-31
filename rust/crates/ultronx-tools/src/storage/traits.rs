//! MemoryBackend trait for all storage backends.

use ULTRONX_core::{ULTRONXError, RetrievalResult};
use serde_json::Value;

pub trait MemoryBackend: Send + Sync {
    fn backend_id(&self) -> &str;
    fn store(
        &self,
        content: &str,
        source: &str,
        metadata: Option<&Value>,
    ) -> Result<String, ULTRONXError>;
    fn retrieve(
        &self,
        query: &str,
        top_k: usize,
    ) -> Result<Vec<RetrievalResult>, ULTRONXError>;
    fn delete(&self, doc_id: &str) -> Result<bool, ULTRONXError>;
    fn clear(&self) -> Result<(), ULTRONXError>;
    fn count(&self) -> Result<usize, ULTRONXError>;
}
