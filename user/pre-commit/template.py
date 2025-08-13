pkgname = "pre-commit"
pkgver = "4.6.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "bash",
    "git",
    "nodeenv",
    "python-cfgv",
    "python-identify",
    "python-pyyaml",
    "python-virtualenv",
]
checkdepends = [
    "python-pytest",
    "python-pytest-env",
    "python-re-assert",
    *depends,
]
pkgdesc = "Git pre-commit hook framework"
license = "MIT"
url = "https://pre-commit.com"
source = f"https://github.com/pre-commit/pre-commit/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0e3034907581cfe794572dbad2183bf55da885aabd75a5fcbb2f62295b548eaa"


def post_extract(self):
    # most of these fail due to the language stuff not being present
    # and/or needing network and whatnot, they also take an eternity
    self.rm("tests/languages", recursive=True)
    # weird handling of git
    self.rm("tests/main_test.py")
    # calls network
    self.rm("tests/repository_test.py")


def post_install(self):
    self.install_license("LICENSE")
