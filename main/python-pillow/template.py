pkgname = "python-pillow"
pkgver = "10.0.0"
pkgrel = 0
build_style = "python_module"
make_check_target = "Tests"
hostmakedepends = ["python-setuptools"]
makedepends = [
    "python-devel",
    "libjpeg-turbo-devel",
    "openjpeg-devel",
    "libtiff-devel",
    "libwebp-devel",
    "lcms2-devel",
    "freetype-devel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python Imaging Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:PIL"
url = "https://python-pillow.org"
source = f"$(PYPI_SITE)/P/Pillow/Pillow-{pkgver}.tar.gz"
sha256 = "9c82b5b3e043c7af0d95792d0d20ccf68f61a1fec6b3530e718b688422727396"


def init_check(self):
    # make sure the tests can find their lib
    self.make_check_env["PYTHONPATH"] = str(
        list((self.cwd / "build").glob("lib.*"))[0].relative_to(self.cwd)
    )


def post_install(self):
    self.install_license("LICENSE")
