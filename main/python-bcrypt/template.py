pkgname = "python-bcrypt"
pkgver = "5.0.0"
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
license = "Apache-2.0"
url = "https://github.com/pyca/bcrypt"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "00426239c15a99c6b3f61a43d5c825fb53ee64921ceb0bdf95d22d581bdba67e"


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc="src/_bcrypt").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)
    # siigh
    self.make_env["CARGO_HOME"] = str(self.chroot_cwd / "src/_bcrypt/.cargo")
