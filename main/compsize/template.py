pkgname = "compsize"
pkgver = "1.5"
pkgrel = 0
build_style = "makefile"
makedepends = ["linux-headers", "btrfs-progs-devel"]
pkgdesc = "Tool to find compression types and ratios of files in Btrfs"
maintainer = "autumnontape <autumn@cyfox.net>"
license = "GPL-2.0-or-later"
url = "https://github.com/kilobyte/compsize"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8b15b528f6cf95ff99d2ddfd7bce87271fd1356c875e5f5895ed83caf6952535"
hardening = ["vis", "cfi"]
# no test suite exists
options = ["!check"]


# the makefile's install rule has problems with trying to
# use directories that don't exist, and these are the only
# two files it installs anyway, so we do it ourselves
def install(self):
    self.install_bin("compsize")
    self.install_man("compsize.8")
