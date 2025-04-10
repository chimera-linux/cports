pkgname = "python-bcrypt"
pkgver = "4.3.0"
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
sha256 = "5cf3964765a9e2ed592ceb721948592f6227abcf22dd7314c897363ddd49ac3e"


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc="src/_bcrypt").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)
    # siigh
    self.make_env["CARGO_HOME"] = str(self.chroot_cwd / "src/_bcrypt/.cargo")
