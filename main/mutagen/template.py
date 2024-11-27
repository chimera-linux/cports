pkgname = "mutagen"
pkgver = "1.47.0"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-hypothesis", "python-pytest"]
pkgdesc = "Audio tagger implemented in Python"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/quodlibet/mutagen"
source = f"https://github.com/quodlibet/mutagen/archive/refs/tags/release-{pkgver}.tar.gz"
sha256 = "f7489e19d375c31ba1962ab19e11eca8b9f86f05bfd99cef467f8dd875d8941e"
