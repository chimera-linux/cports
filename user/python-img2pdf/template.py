pkgname = "python-img2pdf"
pkgver = "0.6.3"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
checkdepends = [
    "python-numpy",
    "python-pytest",
]
depends = [
    "python-pikepdf",
]
pkgdesc = "Lossless conversion of raster images to PDF"
license = "GPL-3.0-or-later"
url = "https://gitlab.mister-muffin.de/josch/img2pdf"
source = f"https://files.pythonhosted.org/packages/source/i/img2pdf/img2pdf-{pkgver}.tar.gz"
sha256 = "219518020f5bd242bdc46493941ea3f756f664c2e86f2454721e74353f58cd95"
# tests need scipy
options = ["!check"]
