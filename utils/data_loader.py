import random
from datasets import load_dataset


class DataLoader:
    def __init__(self, corpus_name, queries_name, relevant_docs_name):
        self.corpus_name = corpus_name
        self.queries_name = queries_name
        self.relevant_docs_name = relevant_docs_name
        self.load_datasets()
        self.process_datasets()

    def load_datasets(self):
        self.corpus = load_dataset(self.corpus_name, "corpus", split="corpus")
        self.queries = load_dataset(
            self.queries_name, "queries", split="queries")
        self.relevant_docs_data = load_dataset(
            self.relevant_docs_name, split="validation")

    def process_datasets(self):
        self.shrink_corpus()
        self.convert_to_dicts()
        self.prepare_relevant_docs()

    def shrink_corpus(self):
        # include corpus sharing the same corpus_id from relevant docs data
        required_corpus_ids = list(
            map(str, self.relevant_docs_data["corpus-id"]))
        # random sample 15000 corpus
        # required_corpus_ids += random.sample(self.corpus["_id"], k=15_000)
        # uodate corpus
        self.corpus = self.corpus.filter(
            lambda x: x["_id"] in required_corpus_ids)

    def convert_to_dicts(self):
        self.corpus = dict(zip(self.corpus["_id"], self.corpus["text"]))
        self.queries = dict(zip(self.queries["_id"], self.queries["text"]))

    def prepare_relevant_docs(self):
        self.relevant_docs = {}
        for query_id, corpus_ids in zip(self.relevant_docs_data["query-id"], self.relevant_docs_data["corpus-id"]):
            query_id = str(query_id)
            corpus_ids = str(corpus_ids)
            if query_id not in self.relevant_docs:
                self.relevant_docs[query_id] = set()
            self.relevant_docs[query_id].add(corpus_ids)
