pkgname = "hfsutils"
pkgver = "3.2.6"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "HFS filesystem utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.mars.org/home/rob/proj/hfs"
source = f"ftp://ftp.mars.org/pub/hfs/hfsutils-{pkgver}.tar.gz"
sha256 = "bc9d22d6d252b920ec9cdf18e00b7655a6189b3f34f42e58d5bb152957289840"
# Self-tests only available if configured --with-tcl
options = ["!check"]


def install(self):
    for f in [
        "hattrib",
        "hcd",
        "hcopy",
        "hdel",
        "hdir",
        "hformat",
        "hls",
        "hmkdir",
        "hmount",
        "hpwd",
        "hrename",
        "hrmdir",
        "humount",
        "hvol",
    ]:
        self.install_bin(f)
        self.install_man(f"doc/man/{f}.1")

    # extra manpage
    self.install_man("doc/man/hfsutils.1")
