pkgname = "bcache-tools"
pkgver = "1.1"
pkgrel = 0
build_style = "makefile"
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = [
    "linux-headers",
    "util-linux-blkid-devel",
    "util-linux-smartcols-devel",
    "util-linux-uuid-devel",
]
pkgdesc = "User space tools for using the linux bcache subsystem"
license = "GPL-2.0-only"
url = "https://bcache.evilpiepirate.org"
source = f"https://git.kernel.org/pub/scm/linux/kernel/git/colyli/bcache-tools.git/snapshot/bcache-tools-{pkgver}.tar.gz"
sha256 = "d1c92274ae03b414dd1a05277bf89dd2a8395496c692e3b143d9e6112d3421f8"
# the upstream makefile has bcache-test commented out in install
options = ["!check"]


def pre_install(self):
    self.mkdir(f"{self.destdir}/usr/bin", True)
    self.mkdir(f"{self.destdir}/usr/sbin", True)
    self.mkdir(f"{self.destdir}/usr/lib", True)
    self.mkdir(f"{self.destdir}/lib/udev/rules.d", True)
    self.mkdir(f"{self.destdir}/usr/share/man/man8", True)


def post_install(self):
    self.mv(f"{self.destdir}/usr/sbin/*", f"{self.destdir}/usr/bin", True)
    self.mv(f"{self.destdir}/lib/*", f"{self.destdir}/usr/lib", True)
