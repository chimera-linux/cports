pkgname = "meson"
_mver = "0.58"
version = f"{_mver}.1"
revision = 1
build_style = "python_module"
hostmakedepends = ["python-devel", "python-setuptools"]
depends = ["ninja", "python-setuptools"]
short_desc = "Meson build system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
homepage = "https://mesonbuild.com"
changelog = f"https://github.com/mesonbuild/meson/blob/master/docs/markdown/Release-notes-for-{_mver}.0.md"
distfiles = [f"https://github.com/mesonbuild/{pkgname}/releases/download/{version}/{pkgname}-{version}.tar.gz"]
checksum = ["3144a3da662fcf79f1e5602fa929f2821cba4eba28c2c923fe0a7d3e3db04d5d"]

# FIXME: tests, install completions etc.
