pkgname = "python-pillow"
pkgver = "9.5.0"
pkgrel = 0
build_style = "python_module"
make_check_target = "Tests"
hostmakedepends = ["python-setuptools"]
makedepends = [
    "python-devel", "libjpeg-turbo-devel", "openjpeg-devel", "libtiff-devel",
    "libwebp-devel", "lcms2-devel", "freetype-devel",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python Imaging Library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:PIL"
url = "https://python-pillow.org"
source = f"$(PYPI_SITE)/P/Pillow/Pillow-{pkgver}.tar.gz"
sha256 = "bf548479d336726d7a0eceb6e767e179fbde37833ae42794602631a070d630f1"

def init_check(self):
    # make sure the tests can find their lib
    self.make_check_env["PYTHONPATH"] = str(
        list((self.cwd / "build").glob("lib.*"))[0].relative_to(self.cwd)
    )

def post_install(self):
    self.install_license("LICENSE")
