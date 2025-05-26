pkgname = "python-cryptography"
pkgver = "45.0.3"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {"MATURIN_PEP517_ARGS": "--offline"}
hostmakedepends = [
    "cargo",
    "pkgconf",
    "python-build",
    "python-cffi",
    "python-installer",
    "python-maturin",
    "python-setuptools",
]
makedepends = ["python-devel", "openssl3-devel", "rust-std"]
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
license = "BSD-3-Clause OR Apache-2.0"
url = "https://github.com/pyca/cryptography"
source = f"$(PYPI_SITE)/c/cryptography/cryptography-{pkgver}.tar.gz"
sha256 = "ec21313dd335c51d7877baf2972569f40a4291b76a0ce51391523ae358d05899"


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor(wrksrc="src/rust")


def init_build(self):
    from cbuild.util import cargo

    self.env.update(cargo.get_environment(self))
    # because maturin is stupid
    self.env["CARGO_HOME"] = str(self.chroot_cwd / "src/rust/.cargo")


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


def post_install(self):
    self.install_license("LICENSE.BSD")
