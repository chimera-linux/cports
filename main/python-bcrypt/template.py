pkgname = "python-bcrypt"
pkgver = "4.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "cargo",
    "python-build",
    "python-installer",
    "python-setuptools-rust",
]
makedepends = ["python-devel", "rust-std"]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Bcrypt password hashing for python"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0"
url = "https://github.com/pyca/bcrypt"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "36c757ad7a317627256b7f0be570b16ee1639c6faf398f9f7a7bd4f21bd289ee"


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc="src/_bcrypt").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)
