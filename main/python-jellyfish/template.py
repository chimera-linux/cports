pkgname = "python-jellyfish"
pkgver = "1.2.0"
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
sha256 = "5c7d73db4045dcc53b6efbfea21f3d3da432d3e052dc51827574d1a447fc23b4"


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()


def post_install(self):
    self.install_license("LICENSE")
