pkgname = "awk"
pkgver = "20220303"
pkgrel = 0
_commit="240201426090f9eca923980e388cab5e66ecc0ef"
hostmakedepends = ["byacc"]
pkgdesc = "One true awk"
maintainer = "q66 <q66@chimera-linux.org>"
license = "SMLNJ"
url = "https://github.com/onetrueawk/awk"
source = f"https://github.com/onetrueawk/awk/archive/{_commit}.tar.gz"
sha256 = "d84c93b6b8a7b8ae60866c3a5bbcf55ca415308b5a24544b62546f55453c25fe"
hardening = ["vis", "cfi"]
# test suite uses local tools that are not present
options = ["bootstrap", "!check"]

def init_configure(self):
    from cbuild.util import make
    self.make = make.Make(self)

def do_build(self):
    self.make.build([
        "CC=" + self.get_tool("CC"),
        "HOSTCC=" + self.get_tool("CC"),
        "CFLAGS=" + self.get_cflags(shell = True) + " " + \
                    self.get_ldflags(shell = True) + " -DHAS_ISBLANK",
        "YACC=yacc -d -o awkgram.tab.c",
    ])

def do_check(self):
    self.make.check()

def do_install(self):
    self.cp("a.out", "awk")
    self.install_bin("awk")
    self.install_man("awk.1")
    self.install_license("LICENSE")
