from cx_Freeze import setup, Executable

setup(
    name = "OpenCV_recognation_tool_by_mariklolik",
    version = "1.0",
    description = "recognation_tool",
    executables = [Executable("real_time_object_detection.py")]
)