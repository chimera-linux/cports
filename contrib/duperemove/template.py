pkgname = "duperemove"
pkgver = "0.12"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_env = {
    "VERSION": f"v{pkgver}",
    "IS_RELEASE": "1",
}
make_install_args = ["SBINDIR=/usr/bin"]
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["glib-devel", "sqlite-devel", "linux-headers"]
pkgdesc = "Tools for deduplicating extents in filesystems like Btrfs"
maintainer = "autumnontape <autumn@cyfox.net>"
license = "GPL-2.0-only AND BSD-2-Clause"
url = "https://github.com/markfasheh/duperemove"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "53c0e1526d8bdb16ff18ad8a417570c829f8a11dea27060061c73dd6387326f4"
tool_flags = {"CFLAGS": ["-std=gnu2x"]}
hardening = ["vis", "cfi"]
# no test suite exists
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.xxhash")
