pkgname = "python-img2pdf"
pkgver = "0.6.1"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-pikepdf",
    "python-setuptools",
]
# checkdepends = [
#     "python-numpy",
#     "python-pytest",
#     "python-scipy",
# ]
depends = [
    "python-pikepdf",
]
pkgdesc = "Lossless conversion of raster images to PDF"
license = "GPL-3.0-or-later"
url = "https://gitlab.mister-muffin.de/josch/img2pdf"
source = f"https://files.pythonhosted.org/packages/source/i/img2pdf/img2pdf-{pkgver}.tar.gz"
sha256 = "306e279eb832bc159d7d6294b697a9fbd11b4be1f799b14b3b2174fb506af289"
# tests need scipy
options = ["!check"]
