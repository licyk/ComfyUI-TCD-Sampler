from . import tcd_sampling
from .tcd_sampling import sample_tcd, sample_tcd_euler_a


if not tcd_sampling.INITIALIZED:
    from comfy.k_diffusion import sampling as k_diffusion_sampling
    from comfy.samplers import SAMPLER_NAMES

    setattr(k_diffusion_sampling, "sample_tcd", sample_tcd)
    setattr(k_diffusion_sampling, "sample_tcd_euler_a", sample_tcd_euler_a)
    SAMPLER_NAMES.append("tcd")
    SAMPLER_NAMES.append("tcd_euler_a")
    tcd_sampling.INITIALIZED = True


NODE_CLASS_MAPPINGS = {}