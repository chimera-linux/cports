pkgname = "meson"
_mver = "0.58"
pkgver = f"{_mver}.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-devel", "python-setuptools"]
depends = ["ninja", "python-setuptools"]
pkgdesc = "Meson build system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://mesonbuild.com"
source = f"https://github.com/mesonbuild/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "7634ec32955d3f897d623b88e9d2988451035f43d73c17a29caf767387baedb7"
# checkdepends not available yet
options = ["!check"]

# FIXME: tests, install completions etc.
