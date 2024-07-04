pkgname = "libde265"
pkgver = "1.0.15"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-option-checking"]
configure_gen = ["./autogen.sh"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Open H.265 codec implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "http://www.libde265.org"
source = f"https://github.com/strukturag/libde265/archive/v{pkgver}.tar.gz"
sha256 = "d4e55706dfc5b2c5c9702940b675ce2d3e7511025c6894eaddcdbaf0b15fd3f3"
hardening = ["!cfi"]  # TODO


def post_install(self):
    # do not polute /usr/bin with junk
    for f in [
        "acceleration_speed",
        "bjoentegaard",
        "block-rate-estim",
        "gen-enc-table",
        "rd-curves",
        "tests",
        "yuv-distortion",
    ]:
        self.uninstall(f"usr/bin/{f}")


@subpackage("libde265-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libde265-progs")
def _progs(self):
    return self.default_progs()
