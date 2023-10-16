pkgname = "python-pillow"
pkgver = "10.1.0"
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
sha256 = "e6bf8de6c36ed96c86ea3b6e1d5273c53f46ef518a062464cd7ef5dd2cf92e38"


def init_check(self):
    # make sure the tests can find their lib
    self.make_check_env["PYTHONPATH"] = str(
        list((self.cwd / "build").glob("lib.*"))[0].relative_to(self.cwd)
    )


def post_install(self):
    self.install_license("LICENSE")
