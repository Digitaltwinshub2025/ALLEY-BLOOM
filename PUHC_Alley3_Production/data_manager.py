import json
import os
from typing import Any, Dict, List, Optional


class DataManager:
    def __init__(self, base_dir: Optional[str] = None):
        self._base_dir = base_dir or os.path.dirname(os.path.abspath(__file__))
        self._data_dir = os.path.join(self._base_dir, "data")
        self._scenarios_file = os.path.join(self._data_dir, "scenarios.json")

    def _ensure_data_dir(self) -> None:
        os.makedirs(self._data_dir, exist_ok=True)

    def load_scenarios(self) -> List[Dict[str, Any]]:
        self._ensure_data_dir()
        if not os.path.exists(self._scenarios_file):
            return []
        try:
            with open(self._scenarios_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, list):
                return data
            if isinstance(data, dict) and "scenarios" in data and isinstance(data["scenarios"], list):
                return data["scenarios"]
            return []
        except Exception:
            return []

    def _write_scenarios(self, scenarios: List[Dict[str, Any]]) -> bool:
        self._ensure_data_dir()
        try:
            with open(self._scenarios_file, "w", encoding="utf-8") as f:
                json.dump(scenarios, f, indent=2)
            return True
        except Exception:
            return False

    def get_scenario_by_id(self, scenario_id: str) -> Optional[Dict[str, Any]]:
        scenarios = self.load_scenarios()
        for s in scenarios:
            if s.get("id") == scenario_id:
                return s
        return None

    def save_scenario(self, scenario_data: Dict[str, Any]) -> bool:
        scenario_id = scenario_data.get("id")
        if not scenario_id:
            return False

        scenarios = self.load_scenarios()
        updated = False
        for i, s in enumerate(scenarios):
            if s.get("id") == scenario_id:
                scenarios[i] = scenario_data
                updated = True
                break

        if not updated:
            scenarios.append(scenario_data)

        return self._write_scenarios(scenarios)

    def delete_scenario(self, scenario_id: str) -> bool:
        scenarios = self.load_scenarios()
        new_scenarios = [s for s in scenarios if s.get("id") != scenario_id]
        if len(new_scenarios) == len(scenarios):
            return False
        return self._write_scenarios(new_scenarios)


data_manager = DataManager()
