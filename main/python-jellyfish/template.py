pkgname = "python-jellyfish"
pkgver = "1.2.1"
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
license = "BSD-2-Clause"
url = "https://jamesturk.github.io/jellyfish"
source = f"$(PYPI_SITE)/j/jellyfish/jellyfish-{pkgver}.tar.gz"
sha256 = "72d2fda61b23babe862018729be73c8b0dc12e3e6601f36f6e65d905e249f4db"


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()


def post_install(self):
    self.install_license("LICENSE")
