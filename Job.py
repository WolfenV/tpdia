from typing import Optional


class Job:
    def __init__(self, classification_result: float):
        self._classification_result = classification_result
        self.cpu_suitability = classification_result
        self.gpu_suitability = 1 - classification_result
        self._device: Optional[str] = None

    def get_suitable_job_type(self):
        if self.cpu_suitability > self.gpu_suitability:
            return CpuJob(self._classification_result)
        else:
            return GpuJob(self._classification_result)

    def __str__(self):
        return f"{self._device} job: {self.cpu_suitability:.3f}/{self.gpu_suitability:.3f} (CPU/GPU suitability)"


class CpuJob(Job):
    def __init__(self, classification_result: float):
        super().__init__(classification_result)
        self._device = "CPU"


class GpuJob(Job):
    def __init__(self, classification_result: float):
        super().__init__(classification_result)
        self._device = "GPU"
