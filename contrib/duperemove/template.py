pkgname = "duperemove"
pkgver = "0.14.1"
pkgrel = 0
build_style = "makefile"
make_build_env = {
    "VERSION": f"v{pkgver}",
    "IS_RELEASE": "1",
}
make_install_args = ["SBINDIR=/usr/bin"]
hostmakedepends = ["pkgconf"]
makedepends = ["glib-devel", "sqlite-devel", "linux-headers"]
pkgdesc = "Tools for deduplicating extents in filesystems like Btrfs"
maintainer = "autumnontape <autumn@cyfox.net>"
license = "GPL-2.0-only AND BSD-2-Clause"
url = "https://github.com/markfasheh/duperemove"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5970a68e37c1b509448f6d82278ca21403cc7722f6267f7da27723b0749088ea"
tool_flags = {"CFLAGS": ["-std=gnu2x"]}
hardening = ["vis", "cfi"]
# no test suite exists
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.xxhash")
