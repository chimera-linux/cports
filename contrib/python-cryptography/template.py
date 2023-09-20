pkgname = "python-cryptography"
pkgver = "41.0.4"
pkgrel = 0
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
makedepends = ["python-devel", "openssl-devel"]
depends = ["python-cffi"]
checkdepends = [
    "python-pytest-subtests",
    "python-pytest-xdist",
    "python-iso8601",
    "python-pytz",
    "python-cryptography_vectors",
    "python-pretend",
    "python-hypothesis",
    "python-cffi",
]
pkgdesc = "Cryptographic primitives for Python"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause OR Apache-2.0"
url = "https://github.com/pyca/cryptography"
source = f"$(PYPI_SITE)/c/cryptography/cryptography-{pkgver}.tar.gz"
sha256 = "7febc3094125fc126a7f6fb1f420d0da639f3f32cb15c8ff0dc3997c4549f51a"
# unpackaged checkdepends
options = ["!check"]


def do_prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor(wrksrc="src/rust")
    cargo.setup_vendor(self, wrksrc="src/rust")


def init_configure(self):
    from cbuild.util import cargo

    self.env.update(cargo.get_environment(self))


def post_install(self):
    self.install_license("LICENSE.BSD")
