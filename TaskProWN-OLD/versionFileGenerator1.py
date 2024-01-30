import pyinstaller_versionfile

pyinstaller_versionfile.create_versionfile_from_input_file(
    output_file="version1.txt",
    input_file="metadata.yml",
    version="18.30.01.2024"  # optional, can be set to overwrite version information (equivalent to --version when using the CLI)
)
