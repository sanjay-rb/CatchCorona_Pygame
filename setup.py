import cx_Freeze

execute = [cx_Freeze.Executable("CatchCorona.py")]

cx_Freeze.setup(
    name= "Catch Corona",
    options={
        "build_exe" : {
            "packages":["pygame"],
            "include_files":["corona.png", "doctor.png"]
        }
    }, 
    executables = execute
)