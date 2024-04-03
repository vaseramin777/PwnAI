# Configuration file for the Sphinx documentation builder.
# This file only contains a selection of the most common options. For a full
# list see the documentation: 
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import importlib
import inspect
import sys
from datetime import date
from pathlib import Path

import git

# Add the parent directory to the system path to import the pythontemplate
# module.
sys.path.insert(0, str(Path("../..").absolute()))

from pythontemplate import __version__

# Initialize the Git repository object to access commit information.
git_repo = git.Repo(".", search_parent_directories=True)  # type: ignore[reportPrivateImportUsage]
git_commit = git_repo.head.commit

# -- Project information --------------------------------
