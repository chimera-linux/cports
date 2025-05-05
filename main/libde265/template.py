pkgname = "libde265"
pkgver = "1.0.16"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-option-checking"]
configure_gen = ["./autogen.sh"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Open H.265 codec implementation"
license = "LGPL-3.0-or-later"
url = "http://www.libde265.org"
source = f"https://github.com/strukturag/libde265/archive/v{pkgver}.tar.gz"
sha256 = "ed12c931759c1575848832f70db5071a001ac813db4e4f568ee08aef6e234d4e"
hardening = ["!vis", "!cfi"]


def post_install(self):
    # do not polute /usr/bin with junk
    for f in [
        "bjoentegaard",
        "block-rate-estim",
        "gen-enc-table",
        "rd-curves",
        "tests",
        "yuv-distortion",
    ]:
        self.uninstall(f"usr/bin/{f}")


@subpackage("libde265-devel")
def _(self):
    return self.default_devel()


@subpackage("libde265-progs")
def _(self):
    return self.default_progs()
