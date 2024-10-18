pkgname = "python-cryptography"
pkgver = "43.0.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "cargo",
    "pkgconf",
    "python-build",
    "python-cffi",
    "python-installer",
    "python-maturin",
    "python-setuptools",
]
makedepends = ["python-devel", "openssl-devel", "rust-std"]
depends = ["python-cffi"]
checkdepends = [
    "python-certifi",
    "python-cryptography-vectors",
    "python-pretend",
    "python-pytest-benchmark",
    "python-pytest-xdist",
    *depends,
]
pkgdesc = "Cryptographic primitives for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause OR Apache-2.0"
url = "https://github.com/pyca/cryptography"
source = f"$(PYPI_SITE)/c/cryptography/cryptography-{pkgver}.tar.gz"
sha256 = "315b9001266a492a6ff443b61238f956b214dbec9910a081ba5b6646a055a805"


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor(wrksrc="src/rust")


def init_build(self):
    from cbuild.util import cargo

    self.env.update(cargo.get_environment(self))


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


def post_install(self):
    self.install_license("LICENSE.BSD")
