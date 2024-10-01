pkgname = "python-tap.py"
pkgver = "3.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-babel",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "Test Anything Protocol (TAP) tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/python-tap/tappy"
source = f"$(PYPI_SITE)/t/tap.py/tap.py-{pkgver}.tar.gz"
sha256 = "3c0cd45212ad5a25b35445964e2517efa000a118a1bfc3437dae828892eaf1e1"


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
