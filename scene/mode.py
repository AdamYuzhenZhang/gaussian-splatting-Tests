# An enum that tells the trainer how to update splats

from enum import Enum

class TrainingMode(Enum):
    DEFAULT = 0  # The default GS
    PLANNER = 1  # Only move splats sideways on plane