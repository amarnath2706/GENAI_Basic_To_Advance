from haystack.utils import Secret
from haystack.components.embedders import SentenceTransformersTextEmbedder
from haystack.components.builders import PromptBuilder
from haystack_integrations.components.retrievers.pinecone import PineconeEmbeddingRetriever
from haystack.components.generators import HuggingFaceTGIGenerator
from haystack import Pipeline
from QA_System.ingestion import ingest
from QA_System.utils import pinecone_config
import os
from dotenv import load_dotenv