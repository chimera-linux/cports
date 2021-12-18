pkgname = "meson"
pkgver = "0.60.1"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-devel", "python-setuptools"]
depends = ["ninja", "python-setuptools"]
pkgdesc = "Meson build system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://mesonbuild.com"
source = f"https://github.com/mesonbuild/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "5add789c953d984b500858b2851ee3d7add0460cf1a6f852f0a721af17384e13"
# checkdepends not available yet
options = ["!check"]

# FIXME: tests, install completions etc.
