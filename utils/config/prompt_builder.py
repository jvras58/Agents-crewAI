"""Módulo para construção de prompts de agentes."""

import os
from typing import Optional

from utils.config.load_yaml import load_prompt


def build_prompt(prompt_path: str) -> dict:
    """Constrói o prompt completo a partir de um arquivo YAML,
    integrando exemplos no backstory se presentes."""
    prompt = load_prompt(prompt_path)

    backstory_base = prompt.get('backstory', '')
    examples = prompt.get('examples', [])
    if examples:
        backstory_base += '\n\nExemplos de respostas:\n'
        for ex in examples:
            backstory_base += (
                f"- Pergunta: {ex['question']}\n  Resposta: {ex['answer']}\n"
            )
    prompt['backstory'] = backstory_base
    return prompt


def build_prompt_by_name(agent_name: str, base_path: Optional[str] = None) -> dict:
    """Constrói o prompt pelo nome, assumindo o arquivo YAML está em {base_path}/{agent_name}_prompt.yaml.
    Se base_path não for fornecido, usa utils/prompts/."""
    if base_path is None:
        base_path = os.path.join(os.path.dirname(__file__), '..', 'prompts')
    prompt_path = os.path.join(base_path, f'{agent_name}_prompt.yaml')
    return build_prompt(prompt_path)
