pkgname = "slang"
pkgver = "2.3.3"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["gmake", "pkgconf", "ncurses-devel"]
makedepends = [
    "ncurses-devel", "zlib-devel", "pcre-devel",
    "libpng-devel", "oniguruma-devel"
]
pkgdesc = "S-Lang programming library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.jedsoft.org/slang"
source = f"https://www.jedsoft.org/releases/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "f9145054ae131973c61208ea82486d5dd10e3c5cdad23b7c4a0617743c8f5a18"
# racey
options = ["!parallel"]

def init_configure(self):
    sroot = str(self.profile().sysroot / "usr")
    self.configure_args += [
        f"--with-z={sroot}", f"--with-pcre={sroot}",
        f"--with-png={sroot}", f"--with-onig={sroot}"
    ]
    # force it to use CFLAGS too during linking
    self.configure_env = {
        "LDFLAGS": self.get_cflags(shell = True) + " " + \
                   self.get_ldflags(shell = True)
    }

def post_install(self):
    self.install_license("COPYING")

@subpackage("slang-devel")
def _devel(self):
    return self.default_devel()
