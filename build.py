#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "projectPrototype"
version = "1.0"
summary = "Sistema para gestionar proceedings de eventos academicos."
description = "Este proyecto facilita la publicacion, revision y gestion de trabajos para los eventos academicos."
url = "https://github.com/LeoGB29/projectPrototype"

default_task = "publish"


@init
def set_properties(project):
    
    # dependencias
    project.depends_on("Flask")
    project.depends_on("Flask-SQLAlchemy")
    
    # compilacion
    project.set_property("coverage_break_build", False)
    project.set_property("verbose", True)
    project.set_property("dir_source_unittest_python", "tests")
