import random
from typing import List

from KernelFeaturesSample import KernelFeaturesSample


class KernelFeaturesGenerator:
    def __init__(self):
        self._default_start_value = 5
        self._default_stop_value = 100
        self._samples = []

    def generate_samples(self, n: int) -> List[KernelFeaturesSample]:
        for _ in range(n):
            sample = KernelFeaturesSample()
            sample._data_size = self._get_random_data_size()
            sample._total_return_statement = self._get_random_total_return_statement()
            sample._total_control_statement = self._get_random_total_control_statement()
            sample._total_allocation_instruction = self._get_random_total_allocation_instruction()
            sample._total_load_instructions = self._get_random_total_load_instructions()
            sample._total_store_instructions = self._get_random_total_store_instructions()
            sample._total_multiplication_instruction_float = self._get_random_total_multiplication_instruction_float()
            sample._total_multiplication_instruction_int = self._get_random_total_multiplication_instruction_int()
            sample._total_division_instruction_float = self._get_random_total_division_instruction_float()
            sample._total_division_instruction_int = self._get_random_total_division_instruction_int()
            sample._total_condition_check_instruction = self._get_random_total_condition_check_instruction()
            sample._total_addition_instruction_float = self._get_random_total_addition_instruction_float()
            sample._total_addition_instruction_int = self._get_random_total_addition_instruction_int()
            sample._total_subtraction_instruction_float = self._get_random_total_subtraction_instruction_float()
            sample._total_subtraction_instruction_int = self._get_random_total_subtraction_instruction_int()
            sample._total_function_call_instruction = self._get_random_total_total_function_call_instruction()
            sample._total_functions = self._get_random_total_functions()
            sample._total_blocks = self._get_random_total_blocks()
            sample._total_instructions = self._get_random_total_instructions()
            sample._total_float_operation = self._get_random_total_float_operation()
            sample._total_int_operation = self._get_random_total_int_operation()
            sample._total_loop_operation = self._get_random_total_loop_operation()
            self._samples.append(sample)
        return self._samples

    def _get_rand_range(self, start: int = None, stop: int = None) -> int:
        if start is None:
            start = self._default_start_value
        if stop is None:
            stop = self._default_stop_value
        return random.randrange(start, stop)

    def _get_random_data_size(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_return_statement(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_control_statement(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_allocation_instruction(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_load_instructions(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_store_instructions(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_multiplication_instruction_float(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_multiplication_instruction_int(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_division_instruction_float(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_division_instruction_int(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_condition_check_instruction(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_addition_instruction_float(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_addition_instruction_int(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_subtraction_instruction_float(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_subtraction_instruction_int(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_total_function_call_instruction(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_functions(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_blocks(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_instructions(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_float_operation(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_int_operation(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)

    def _get_random_total_loop_operation(self, start: int = None, stop: int = None) -> int:
        return self._get_rand_range(start, stop)
