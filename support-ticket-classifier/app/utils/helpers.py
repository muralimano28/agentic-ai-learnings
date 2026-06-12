from app.utils.system_instructions import system_instruction_for_json_response, system_instruction_for_one_word_response
from app.utils.example_prompts import example_prompts_for_json_response, example_prompts_for_one_word_response

def get_system_instruction(use_json_output:bool = True):
    if use_json_output:
        return system_instruction_for_json_response
    else:
        return system_instruction_for_one_word_response

def get_examples(use_json_output:bool = True):
    if use_json_output:
        return example_prompts_for_json_response
    else:
        return example_prompts_for_one_word_response