pkgname = "python-digitalocean"
pkgver = "1.17.0"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # needs net
    "--deselect=digitalocean/tests/test_firewall.py",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-jsonpickle",
    "python-requests",
]
checkdepends = ["python-pytest", "python-responses", *depends]
pkgdesc = "Python module to manage DigitalOcean droplets"
maintainer = "ttyyls <contact@behri.org>"
license = "LGPL-3.0-or-later"
url = "https://github.com/koalalorenzo/python-digitalocean"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9c9c788ae03a088d0c03a9a59ff7ac6c492caadd4942d4fc58795ee859fc228f"
