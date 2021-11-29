pkgname = "awk"
pkgver = "20211104"
pkgrel = 0
_commit="c50ef66d119d87e06a041e5522430265ccdce148"
hostmakedepends = ["byacc"]
pkgdesc = "One true awk"
maintainer = "q66 <q66@chimera-linux.org>"
license = "SMLNJ"
url = "https://github.com/onetrueawk/awk"
source = f"https://github.com/onetrueawk/awk/archive/{_commit}.tar.gz"
sha256 = "ef0fa50b7e7e2e21eafd49bb249f7d80d0b86e9cae291408724dba77484a0c6f"
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
        "YACC=byacc -H awkgram.tab.h -o awkgram.tab.c",
    ])

def do_check(self):
    self.make.check()

def do_install(self):
    self.cp("a.out", "awk")
    self.install_bin("awk")
    self.install_man("awk.1")
    self.install_license("LICENSE")
