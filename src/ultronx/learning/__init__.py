"""Learning primitive -- router policies, reward functions, learning."""

from __future__ import annotations

from ULTRONX.learning._stubs import (
    QueryAnalyzer,
    RewardFunction,
    RouterPolicy,
    RoutingContext,
)
from ULTRONX.learning.agents.agent_evolver import AgentConfigEvolver
from ULTRONX.learning.learning_orchestrator import LearningOrchestrator
from ULTRONX.learning.optimize.llm_optimizer import LLMOptimizer
from ULTRONX.learning.optimize.optimizer import OptimizationEngine
from ULTRONX.learning.optimize.store import OptimizationStore
from ULTRONX.learning.routing.complexity import (
    ComplexityQueryAnalyzer,
    score_complexity,
)
from ULTRONX.learning.routing.heuristic_reward import HeuristicRewardFunction
from ULTRONX.learning.routing.router import (
    HeuristicRouter,
    build_routing_context,
)
from ULTRONX.learning.training.data import TrainingDataMiner
from ULTRONX.learning.training.lora import HAS_TORCH, LoRATrainer, LoRATrainingConfig


def ensure_registered() -> None:
    """Ensure all learning policies are registered in RouterPolicyRegistry."""
    from ULTRONX.learning.routing.heuristic_policy import (
        ensure_registered as _reg_heuristic,
    )

    _reg_heuristic()

    from ULTRONX.learning.routing.learned_router import (
        ensure_registered as _reg_learned,
    )

    _reg_learned()

    # Intelligence training (optional deps)
    try:
        import ULTRONX.learning.intelligence  # noqa: F401
    except ImportError:
        pass

    # Orchestrator-specific training (optional deps)
    try:
        import ULTRONX.learning.intelligence.orchestrator  # noqa: F401
    except ImportError:
        pass

    # Agent optimizers (optional deps)
    try:
        import ULTRONX.learning.agents.dspy_optimizer  # noqa: F401
    except ImportError:
        pass
    try:
        import ULTRONX.learning.agents.gepa_optimizer  # noqa: F401
    except ImportError:
        pass
    try:
        import ULTRONX.learning.agents.ace_optimizer  # noqa: F401
    except ImportError:
        pass


__all__ = [
    "AgentConfigEvolver",
    "ComplexityQueryAnalyzer",
    "HAS_TORCH",
    "HeuristicRewardFunction",
    "HeuristicRouter",
    "LLMOptimizer",
    "LearningOrchestrator",
    "LoRATrainer",
    "LoRATrainingConfig",
    "OptimizationEngine",
    "OptimizationStore",
    "QueryAnalyzer",
    "RewardFunction",
    "RouterPolicy",
    "RoutingContext",
    "TrainingDataMiner",
    "build_routing_context",
    "ensure_registered",
    "score_complexity",
]
