pkgname = "python-jellyfish"
pkgver = "1.1.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "cargo",
    "python-build",
    "python-installer",
    "python-maturin",
]
makedepends = ["rust-std"]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python library for approximate and phonetic string matching"
maintainer = "Justin Berthault <justin.berthault@zaclys.net>"
license = "BSD-2-Clause"
url = "https://jamesturk.github.io/jellyfish"
source = f"$(PYPI_SITE)/j/jellyfish/jellyfish-{pkgver}.tar.gz"
sha256 = "a31de6ce7385746df3b65aa3401c30d0881b5abb518cff99090be7ef96129333"


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()


def post_install(self):
    self.install_license("LICENSE")
