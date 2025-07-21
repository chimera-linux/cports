pkgname = "python-sphinxcontrib-jquery"
pkgver = "4.1"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python", "python-sphinx"]
pkgdesc = "Extension to include jQuery on newer Sphinx releases"
license = "0BSD"
url = "https://github.com/sphinx-contrib/jquery"
source = f"https://github.com/sphinx-contrib/jquery/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f6a7578b00a8458e5edd38431d3ea4037b928a21ba1f82469ec2015127955c34"
# no tests
options = ["!check"]
