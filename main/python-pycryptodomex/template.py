# update with python-pycryptodome
pkgname = "python-pycryptodomex"
pkgver = "3.21.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-2-Clause AND Unlicense"
url = "https://www.pycryptodome.org"
# tests not on pypi
source = f"https://github.com/Legrandin/pycryptodome/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "195e5cdfbb550b03f83f2af2aa4652c14b64783574d835fe61bb06c8fc06ba21"


def post_extract(self):
    # makes it build the new non-PyCrypto compatible api
    self.do("touch", ".separate_namespace")


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
        "Cryptodome.SelfTest",
        path=[envpy.parent],
    )


def post_install(self):
    self.install_license("LICENSE.rst")
