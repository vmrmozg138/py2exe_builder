from cx_Freeze import setup, Executable

base = None    

executables = [Executable("docx_dataExtractor.py", base=base)]

packages = ["package1", "package2"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "docxtransformer",
    options = options,
    version = "0.0.1",
    description = 'pilot version',
    executables = executables
)
