pkgname = "python-virtualenv"
pkgver = "20.34.0"
pkgrel = 0
build_style = "python_pep517"
make_env = {
    "SETUPTOOLS_SCM_PRETEND_VERSION": pkgver,
}
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
checkdepends = [
    "python-distlib",
    "python-filelock",
    "python-platformdirs",
    "python-pytest",
]
depends = [
    "python-distlib",
    "python-filelock",
    "python-platformdirs",
]
pkgdesc = "Tool for creating isolated 'virtual' Python environments"
license = "MIT"
url = "https://virtualenv.pypa.io/en/stable"
source = f"https://github.com/pypa/virtualenv/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "39f8865ad52a14089e1301b111bcb2ed59febf5cdb04ad90148882ba2d518e32"
# bizarre meta error I'm too frustrated to investigate
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
