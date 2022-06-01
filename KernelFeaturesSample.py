from typing import Optional


class KernelFeaturesSample:
    def __init__(self):
        self._data_size: Optional[int] = None
        self._total_return_statement: Optional[int] = None
        self._total_control_statement: Optional[int] = None
        self._total_allocation_instruction: Optional[int] = None
        self._total_load_instructions: Optional[int] = None
        self._total_store_instructions: Optional[int] = None
        self._total_multiplication_instruction_float: Optional[int] = None
        self._total_multiplication_instruction_int: Optional[int] = None
        self._total_division_instruction_float: Optional[int] = None
        self._total_division_instruction_int: Optional[int] = None
        self._total_condition_check_instruction: Optional[int] = None
        self._total_addition_instruction_float: Optional[int] = None
        self._total_addition_instruction_int: Optional[int] = None
        self._total_subtraction_instruction_float: Optional[int] = None
        self._total_subtraction_instruction_int: Optional[int] = None
        self._total_function_call_instruction: Optional[int] = None
        self._total_functions: Optional[int] = None
        self._total_blocks: Optional[int] = None
        self._total_instructions: Optional[int] = None
        self._total_float_operation: Optional[int] = None
        self._total_int_operation: Optional[int] = None
        self._total_loop_operation: Optional[int] = None

    def print(self):
        for attr, value in self.__dict__.items():
            print(f"{attr} = {value}")
