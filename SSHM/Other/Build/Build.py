import sys
from pathlib import Path
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def build():
    t = TasksForCommonProjectStructure()
    t.standardized_tasks_build_for_cpp_project(
        str(Path(__file__).absolute()), "QualityCheck", ["Windows","Linux"], 1, sys.argv)


if __name__ == "__main__":
    build()
