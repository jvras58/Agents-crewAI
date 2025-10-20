"""Função para carregar o prompts a partir de um arquivo YAML."""
import yaml


def load_prompt(yaml_path: str) -> dict:
    """Carrega o prompt a partir de um arquivo YAML."""
    with open(yaml_path, encoding='utf-8') as f:
        return yaml.safe_load(f)
