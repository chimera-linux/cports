pkgname = "python-uv-dynamic-versioning"
pkgver = "0.14.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
    "python-wheel",
]
depends = [
    "python-dunamai",
    "python-hatchling",
    "python-jinja2",
    "python-tomlkit",
]
pkgdesc = "Version info provider for uv/hatch projects"
license = "MIT"
url = "https://github.com/ninoseki/uv-dynamic-versioning"
source = f"$(PYPI_SITE)/u/uv-dynamic-versioning/uv_dynamic_versioning-{pkgver}.tar.gz"
sha256 = "574fbc07e87ace45c01d55967ad3b864871257b98ff5b8ac87c261227ac8db5b"
# needs a git checkout of uv-dynamic-versioning
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
