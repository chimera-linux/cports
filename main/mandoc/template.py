pkgname = "mandoc"
pkgver = "1.14.6"
pkgrel = 4
build_style = "configure"
make_check_target = "regress"
makedepends = ["zlib-ng-compat-devel"]
checkdepends = ["perl"]
depends = ["less"]
pkgdesc = "UNIX manpage compiler toolset"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://mandoc.bsd.lv"
source = f"{url}/snapshots/mandoc-{pkgver}.tar.gz"
sha256 = "8bf0d570f01e70a6e124884088870cbed7537f36328d512909eb10cd53179d9c"
hardening = ["vis", "cfi"]


def pre_configure(self):
    with open(self.cwd / "configure.local", "w") as cf:
        cf.write(
            f"""
PREFIX=/usr
SBINDIR=/usr/bin
MANDIR=/usr/share/man
OSNAME="Chimera Linux"
CFLAGS="{self.get_cflags(shell=True)}"
LDFLAGS="{self.get_ldflags(shell=True)}"
CC="{self.get_tool("CC")}"
HAVE_REWB_BSD=0
UTF8_LOCALE=C.UTF-8
"""
        )


def post_install(self):
    self.install_license("LICENSE")

    self.install_dir("etc")
    # from void
    with open(self.destdir / "etc/man.conf", "w") as conf:
        conf.write(
            """# man(1)/apropos(1)/makewhatis(8) configuration, see man.conf(5).

# Default search path for manual pages.
# Add, delete, or reorder as desired.
manpath /usr/local/share/man
manpath /usr/share/man
"""
        )

    # drop hardlinks
    for b in ["apropos", "whatis", "makewhatis", "man"]:
        fp = self.destdir / f"usr/bin/{b}"
        fp.unlink()
        fp.symlink_to("mandoc")

    fp = self.destdir / "usr/share/man/man1/whatis.1"
    fp.unlink()
    fp.symlink_to("apropos.1")


@subpackage("mandoc-apropos")
def _(self):
    self.subdesc = "apropos trigger"
    self.install_if = [self.parent]
    self.triggers = ["/usr/share/man"]
    self.options = ["empty"]

    return []
