pkgname = "python-tinycss2"
pkgver = "1.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
depends = ["python-webencodings"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "CSS parser for python"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/Kozea/tinycss2"
source = f"$(PYPI_SITE)/t/tinycss2/tinycss2-{pkgver}.tar.gz"
sha256 = "10c0972f6fc0fbee87c3edb76549357415e94548c1ae10ebccdea16fb404a9b7"


def post_install(self):
    self.install_license("LICENSE")
