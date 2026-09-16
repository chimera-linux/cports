pkgname = "mandoc"
pkgver = "1.14.6"
pkgrel = 7
build_style = "configure"
make_check_target = "regress"
makedepends = ["zlib-ng-compat-devel"]
checkdepends = ["perl"]
depends = ["less"]
pkgdesc = "UNIX manpage compiler toolset"
license = "ISC"
url = "https://mandoc.bsd.lv"
source = f"{url}/snapshots/mandoc-{pkgver}.tar.gz"
sha256 = "8bf0d570f01e70a6e124884088870cbed7537f36328d512909eb10cd53179d9c"
hardening = ["vis", "cfi"]


def pre_configure(self):
    with open(self.cwd / "configure.local", "w") as cf:
        cf.write(f"""
PREFIX=/usr
SBINDIR=/usr/bin
MANDIR=/usr/share/man
OSNAME="Chimera Linux"
CFLAGS="{self.get_cflags(shell=True)}"
LDFLAGS="{self.get_ldflags(shell=True)}"
CC="{self.get_tool("CC")}"
LN="ln -sf"
HAVE_REWB_BSD=0
UTF8_LOCALE=C.UTF-8
BINM_PAGER=less
MANPATH_DEFAULT="/usr/local/share/man:/usr/share/man"
MANPATH_BASE="/usr/share/man"
""")


def post_install(self):
    self.install_license("LICENSE")


@subpackage("mandoc-apropos")
def _(self):
    self.subdesc = "apropos trigger"
    self.install_if = [self.parent]
    self.triggers = ["/usr/share/man"]
    self.options = ["empty"]

    return []
