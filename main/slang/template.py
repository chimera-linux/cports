pkgname = "slang"
pkgver = "2.3.2"
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
sha256 = "fc9e3b0fc4f67c3c1f6d43c90c16a5c42d117b8e28457c5b46831b8b5d3ae31a"
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
