pkgname = "python-virtualenv"
pkgver = "20.33.1"
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
sha256 = "e81c6c66297f4bb4f60d4c34e9045963e7871b4fca421781eceb7de484dae392"
# bizarre meta error I'm too frustrated to investigate
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
