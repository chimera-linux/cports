pkgname = "python-omemo-dr"
pkgver = "1.0.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = ["python-devel"]
depends = ["python-cryptography", "python-protobuf"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "OMEMO crypto library"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://dev.gajim.org/gajim/omemo-dr"
source = f"$(PYPI_SITE)/o/omemo-dr/omemo-dr-{pkgver}.tar.gz"
sha256 = "2a8a8c77231d73949bdd375278d4d5a261252bdaee52cb6241acb251c202d361"
