pkgname = "python-sphinxcontrib-jquery"
pkgver = "4.1"
pkgrel = 0
build_style = "python_pep517"
make_install_target = f"sphinxcontrib_jquery-{pkgver}-*-*-*.whl"
hostmakedepends = ["python-setuptools", "python-pip", "python-wheel", "python-flit_core"]
depends = ["python", "python-sphinx"]
pkgdesc = "Extension to include jQuery on newer Sphinx releases"
maintainer = "eater <=@eater.me>"
license = "0BSD"
url = "https://github.com/sphinx-contrib/jquery"
source = f"https://github.com/sphinx-contrib/jquery/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f6a7578b00a8458e5edd38431d3ea4037b928a21ba1f82469ec2015127955c34"
# no tests
options = ["!check"]
