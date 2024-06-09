pkgname = "python-jellyfish"
pkgver = "1.0.4"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "cargo",
    "python-build",
    "python-installer",
    "python-maturin",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python library for approximate and phonetic string matching"
maintainer = "Justin Berthault <justin.berthault@zaclys.net>"
license = "BSD-2-Clause"
url = "https://jamesturk.github.io/jellyfish"
source = f"$(PYPI_SITE)/j/jellyfish/jellyfish-{pkgver}.tar.gz"
sha256 = "72aabb3bedd513cdd20712242fd51173b59972c0b146b7a0b9c6f32f1656293f"


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def do_prepare(self):
    from cbuild.util import cargo

    self.cargo = cargo.Cargo(self)
    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_install(self):
    self.install_license("LICENSE")
