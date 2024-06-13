pkgname = "python-cryptography"
pkgver = "42.0.8"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "cargo",
    "pkgconf",
    "python-build",
    "python-cffi",
    "python-installer",
    "python-setuptools-rust",
    "python-wheel",
]
makedepends = ["python-devel", "openssl-devel", "rust-std"]
depends = ["python-cffi"]
checkdepends = [
    "python-certifi",
    "python-cryptography-vectors",
    "python-hypothesis",
    "python-iso8601",
    "python-pretend",
    "python-pytest-benchmark",
    "python-pytest-subtests",
    "python-pytest-xdist",
    "python-pytz",
] + depends
pkgdesc = "Cryptographic primitives for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause OR Apache-2.0"
url = "https://github.com/pyca/cryptography"
source = f"$(PYPI_SITE)/c/cryptography/cryptography-{pkgver}.tar.gz"
sha256 = "8d09d05439ce7baa8e9e95b07ec5b6c886f548deb7e0f69ef25f64b3bce842f2"


def do_prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor(wrksrc="src/rust")
    cargo.setup_vendor(self, wrksrc="src/rust")


def init_configure(self):
    from cbuild.util import cargo

    self.env.update(cargo.get_environment(self))


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


def post_install(self):
    self.install_license("LICENSE.BSD")
