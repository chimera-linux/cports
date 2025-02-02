pkgname = "python-tap.py"
pkgver = "3.2.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
depends = ["python"]
pkgdesc = "Test Anything Protocol (TAP) tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/python-tap/tappy"
source = f"$(PYPI_SITE)/t/tap.py/tap_py-{pkgver}.tar.gz"
sha256 = "d03c9e6af0a56fad994f1c69f14041e676811d73eeeef20bf4077c43d621d608"


def check(self):
    whl = list(self.cwd.glob("dist/*.whl"))[0].name
    self.do(
        "python",
        "-m",
        "venv",
        "--clear",
        "--without-pip",
        "--system-site-packages",
        ".testenv",
    )
    self.do("./.testenv/bin/python", "-m", "installer", f"dist/{whl}")
    self.do("./.testenv/bin/python", "-m", "tap")


def post_install(self):
    self.install_license("LICENSE")
