# update with python-pycryptodomex
pkgname = "python-pycryptodome"
pkgver = "3.22.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["python-devel"]
depends = [
    # ctypes loaded
    "gmp",
    "python",
]
pkgdesc = "Self-contained cryptographic library for Python"
subdesc = "PyCrypto compatibility layer"
license = "BSD-2-Clause AND Unlicense"
url = "https://www.pycryptodome.org"
# tests not on pypi
source = f"https://github.com/Legrandin/pycryptodome/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d1499d50dfe0628fe45157956e9c522011f37043a2d3f2457631c97e56f9e6c1"


# this is identical to the default check, we just have to call a different entrypoint
def check(self):
    whl = list(
        map(
            lambda p: str(p.relative_to(self.cwd)),
            self.cwd.glob("dist/*.whl"),
        )
    )

    self.rm(".cbuild-checkenv", recursive=True, force=True)
    self.do(
        "python3",
        "-m",
        "venv",
        "--without-pip",
        "--system-site-packages",
        "--clear",
        ".cbuild-checkenv",
    )

    envpy = self.chroot_cwd / ".cbuild-checkenv/bin/python3"

    self.do(envpy, "-m", "installer", *whl)
    self.do(
        envpy,
        "-m",
        "Crypto.SelfTest",
        path=[envpy.parent],
    )


def post_install(self):
    self.install_license("LICENSE.rst")
