pkgname = "duperemove"
pkgver = "0.11.3"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_install_args = ["SBINDIR=/usr/bin"]
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["glib-devel", "sqlite-devel", "linux-headers"]
pkgdesc = "Tools for deduplicating extents in filesystems like Btrfs"
maintainer = "autumnontape <autumn@cyfox.net>"
license = "GPL-2.0-only AND BSD-2-Clause"
url = "https://github.com/markfasheh/duperemove"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4161e6a7e9b53bb2c190e48eba0aa3028aca27874751aec351550dbae4964da0"
hardening = ["vis", "cfi"]
# no test suite exists
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.xxhash")
