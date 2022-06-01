from typing import Optional


class Job:
    def __init__(self):
        self.cpu_suitability: Optional[float] = None
        self.gpu_suitability: Optional[float] = None
        self._device: Optional[str] = None

    def get_suitable_job_type(self):
        if self.cpu_suitability > self.gpu_suitability:
            return CpuJob()
        else:
            return GpuJob()


class CpuJob(Job):
    def __init__(self):
        super().__init__()
        self._device = "CPU"


class GpuJob(Job):
    def __init__(self):
        super().__init__()
        self._device = "GPU"
