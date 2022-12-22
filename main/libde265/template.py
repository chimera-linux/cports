pkgname = "libde265"
pkgver = "1.0.9"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-option-checking"]
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "Open H.265 codec implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "http://www.libde265.org"
source = f"https://github.com/strukturag/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "153554f407718a75f1e0ae197d35b43147ce282118a54f894554dbe27c32163d"

def pre_configure(self):
    self.do(self.chroot_cwd / "autogen.sh")

def post_install(self):
    # do not polute /usr/bin with junk
    for f in [
        "acceleration_speed", "bjoentegaard", "block-rate-estim",
        "gen-enc-table", "hdrcopy", "rd-curves", "tests", "yuv-distortion"
    ]:
        self.rm(self.destdir / "usr/bin" / f)

@subpackage("libde265-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libde265-progs")
def _progs(self):
    return self.default_progs()

# FIXME visibility
hardening = ["!vis"]
