pkgname = "python-term-image"
pkgver = "0.7.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools_scm",
]
depends = [
    "python-pillow",
    "python-requests",
]
checkdepends = [*depends, "python-pytest"]
pkgdesc = "Display images in the terminal"
license = "MIT"
url = "https://github.com/AnonymouX47/term-image"
source = f"$(PYPI_SITE)/t/term_image/term_image-{pkgver}.tar.gz"
sha256 = "07320573baa667dcde145d55e94769cbaafeea43b61245245153ff5075b55ffb"
# XXX
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
