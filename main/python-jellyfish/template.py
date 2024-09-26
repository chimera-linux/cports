pkgname = "python-jellyfish"
pkgver = "1.1.0"
pkgrel = 1
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
sha256 = "2a2eec494c81dc1eb23dfef543110dad1873538eccaffabea8520bdac8aecbc1"


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()


def post_install(self):
    self.install_license("LICENSE")
