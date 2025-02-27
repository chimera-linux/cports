pkgname = "libptytty"
pkgver = "2.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DTTY_GID_SUPPORT_EXITCODE=1",
    "-DTTY_GID_SUPPORT_EXITCODE__TRYRUN_OUTPUT=",
    '-DPT_WTMPX_FILE="/dev/null/wtmp"',
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Library for pty/tty/utmp/wtmp/lastlog handling"
license = "GPL-2.0-or-later"
url = "http://software.schmorp.de/pkg/libptytty.html"
source = f"http://dist.schmorp.de/libptytty/libptytty-{pkgver}.tar.gz"
sha256 = "8033ed3aadf28759660d4f11f2d7b030acf2a6890cb0f7926fb0cfa6739d31f7"
# no check target
options = ["!check"]


@subpackage("libptytty-devel")
def _(self):
    return self.default_devel()
