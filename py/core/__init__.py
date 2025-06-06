import logging

# Keep '*' imports for enhanced development velocity
from .agent import *
from .base import *
from .main import *
from .parsers import *
from .providers import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create a console handler and set the level to info
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Create a formatter and set it for the handler
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)
ch.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(ch)

# Optional: Prevent propagation to the root logger
logger.propagate = False

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("LiteLLM").setLevel(logging.WARNING)

__all__ = [
    "ThinkingEvent",
    "ToolCallEvent",
    "ToolResultEvent",
    "CitationEvent",
    "Citation",
    "R2RAgent",
    "SearchResultsCollector",
    "R2RRAGAgent",
    "R2RXMLToolsRAGAgent",
    "R2RStreamingRAGAgent",
    "R2RXMLToolsStreamingRAGAgent",
    "AsyncSyncMeta",
    "syncable",
    "MessageType",
    "Document",
    "DocumentChunk",
    "DocumentResponse",
    "IngestionStatus",
    "GraphExtractionStatus",
    "GraphConstructionStatus",
    "DocumentType",
    "R2RDocumentProcessingError",
    "R2RException",
    "Entity",
    "GraphExtraction",
    "Relationship",
    "GenerationConfig",
    "LLMChatCompletion",
    "LLMChatCompletionChunk",
    "RAGCompletion",
    "Prompt",
    "AggregateSearchResult",
    "WebSearchResult",
    "GraphSearchResult",
    "ChunkSearchSettings",
    "GraphSearchSettings",
    "ChunkSearchResult",
    "WebPageSearchResult",
    "SearchSettings",
    "select_search_filters",
    "SearchMode",
    "HybridSearchSettings",
    "Token",
    "TokenData",
    "Vector",
    "VectorEntry",
    "VectorType",
    "IndexConfig",
    "Agent",
    "AgentConfig",
    "Conversation",
    "Message",
    "TokenResponse",
    "User",
    "AppConfig",
    "Provider",
    "ProviderConfig",
    "AuthConfig",
    "AuthProvider",
    "CryptoConfig",
    "CryptoProvider",
    "EmailConfig",
    "EmailProvider",
    "LimitSettings",
    "DatabaseConfig",
    "DatabaseProvider",
    "EmbeddingConfig",
    "EmbeddingProvider",
    "CompletionConfig",
    "CompletionProvider",
    "RecursiveCharacterTextSplitter",
    "TextSplitter",
    "generate_id",
    "validate_uuid",
    "yield_sse_event",
    "convert_nonserializable_objects",
    "num_tokens",
    "num_tokens_from_messages",
    "SearchResultsCollector",
    "R2RProviders",
    "R2RApp",
    "R2RBuilder",
    "R2RConfig",
    "R2RProviderFactory",
    "AuthService",
    "IngestionService",
    "MaintenanceService",
    "ManagementService",
    "RetrievalService",
    "GraphService",
    "AudioParser",
    "BMPParser",
    "DOCParser",
    "DOCXParser",
    "ImageParser",
    "ODTParser",
    "OCRPDFParser",
    "VLMPDFParser",
    "BasicPDFParser",
    "PDFParserUnstructured",
    "PPTParser",
    "PPTXParser",
    "RTFParser",
    "CSVParser",
    "CSVParserAdvanced",
    "EMLParser",
    "EPUBParser",
    "JSONParser",
    "MSGParser",
    "ORGParser",
    "P7SParser",
    "RSTParser",
    "TSVParser",
    "XLSParser",
    "XLSXParser",
    "XLSXParserAdvanced",
    "MDParser",
    "HTMLParser",
    "TextParser",
    "PythonParser",
    "JavaScriptParser",
    "TypeScriptParser",
    "CSSParser",
    "SupabaseAuthProvider",
    "R2RAuthProvider",
    "JwtAuthProvider",
    "ClerkAuthProvider",
    # Email
    # Crypto
    "BCryptCryptoProvider",
    "BcryptCryptoConfig",
    "NaClCryptoConfig",
    "NaClCryptoProvider",
    "PostgresDatabaseProvider",
    "LiteLLMEmbeddingProvider",
    "OpenAIEmbeddingProvider",
    "OllamaEmbeddingProvider",
    "OpenAICompletionProvider",
    "R2RCompletionProvider",
    "LiteLLMCompletionProvider",
    "UnstructuredIngestionProvider",
    "R2RIngestionProvider",
    "ChunkingStrategy",
]
