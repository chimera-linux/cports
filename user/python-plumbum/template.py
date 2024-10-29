pkgname = "python-plumbum"
pkgver = "1.9.0"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    "-k",
    # expects a different error message from ls
    "not test_iter_lines_error",
]
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
checkdepends = [
    "bash",
    "openssh",
    "procps",
    "python-psutil",
    "python-pytest",
    "python-pytest-cov",
    "python-pytest-mock",
    "python-pytest-timeout",
]
pkgdesc = "Shell script idioms for Python"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://plumbum.readthedocs.io/en/stable"
source = f"$(PYPI_SITE)/p/plumbum/plumbum-{pkgver}.tar.gz"
sha256 = "e640062b72642c3873bd5bdc3effed75ba4d3c70ef6b6a7b907357a84d909219"


def post_install(self):
    self.install_license("LICENSE")
