pkgname = "dvd+rw-tools"
pkgver = "7.1"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_use_env = True
hostmakedepends = ["gm4", "gmake"]
makedepends = ["linux-headers"]
pkgdesc = "DVD and blu-ray burning tools"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://fy.chalmers.se/~appro/linux/DVD+RW"
source = f"{url}/tools/dvd+rw-tools-{pkgver}.tar.gz"
sha256 = "f8d60f822e914128bcbc5f64fbe3ed131cbff9045dca7e12c5b77b26edde72ca"
# guilty until proven innocent
hardening = ["!int"]
# no tests
options = ["!check"]
exec_wrappers = [("/usr/bin/gm4", "m4")]


def init_install(self):
    # nice meme
    self.make_install_args += [f"prefix={self.chroot_destdir}/usr"]
