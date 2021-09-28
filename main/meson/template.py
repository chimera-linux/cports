pkgname = "meson"
_mver = "0.58"
version = f"{_mver}.1"
revision = 0
build_style = "python_module"
hostmakedepends = ["python-devel", "python-setuptools"]
depends = ["ninja", "python-setuptools"]
pkgdesc = "Meson build system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
homepage = "https://mesonbuild.com"
sources = [f"https://github.com/mesonbuild/{pkgname}/releases/download/{version}/{pkgname}-{version}.tar.gz"]
sha256 = ["3144a3da662fcf79f1e5602fa929f2821cba4eba28c2c923fe0a7d3e3db04d5d"]

options = ["!check"]

# FIXME: tests, install completions etc.
