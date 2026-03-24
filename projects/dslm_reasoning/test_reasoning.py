import pytest
from reasoning_engine import ReasoningEngine, TaskStatus

def test_task_initiation():
    engine = ReasoningEngine(agent_id="TEST-AGENT")
    tid = engine.initiate_task("Test Goal")
    assert tid in engine.tasks
    assert engine.tasks[tid]["status"] == TaskStatus.PENDING.value

def test_full_decomposition_loop():
    engine = ReasoningEngine(agent_id="TEST-AGENT-LOOP")
    tid = engine.initiate_task("Loop Goal")
    result = engine.decompose_and_solve(tid)
    assert result["status"] == TaskStatus.COMPLETED.value
    assert len(result["plan"]) == 4
    assert len(result["logs"]) == 4
