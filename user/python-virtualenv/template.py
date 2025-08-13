pkgname = "python-virtualenv"
pkgver = "21.7.0"
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
depends = [
    "python-distlib",
    "python-filelock",
    "python-platformdirs",
    "python-python_discovery",
]
checkdepends = [
    "bash",
    "python-devel",
    "python-flaky",
    "python-pip",
    "python-pytest",
    "python-pytest-env",
    "python-pytest-mock",
    "python-pytest-timeout",
    "python-pytest-xdist",
    "python-setuptools",
    "python-time-machine",
    *depends,
]
pkgdesc = "Tool for managing Python virtual environments"
license = "MIT"
url = "https://virtualenv.pypa.io/en/stable"
source = f"$(PYPI_SITE)/v/virtualenv/virtualenv-{pkgver}.tar.gz"
sha256 = "7f9519b9432ff11b6e1a3e94061664efc2ff99ea21780e3cf4f6bd0a5da8b37c"


def post_extract(self):
    # these tests use the network
    self.rm("tests/unit/create/test_creator.py")
    self.rm("tests/unit/seed/embed/test_bootstrap_link_via_app_data.py")


def post_install(self):
    self.install_license("LICENSE")
