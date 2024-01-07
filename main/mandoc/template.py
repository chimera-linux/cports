pkgname = "mandoc"
pkgver = "1.14.6"
pkgrel = 2
build_style = "configure"
make_cmd = "gmake"
make_check_target = "regress"
hostmakedepends = ["gmake"]
makedepends = ["less", "zlib-devel"]
checkdepends = ["perl"]
depends = ["less"]
pkgdesc = "UNIX manpage compiler toolset"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "http://mandoc.bsd.lv"
source = f"{url}/snapshots/{pkgname}-{pkgver}.tar.gz"
sha256 = "8bf0d570f01e70a6e124884088870cbed7537f36328d512909eb10cd53179d9c"
# FIXME int
hardening = ["!int"]
# ld: error: undefined symbol: mchars_alloc
options = ["!lto"]


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


@subpackage("base-man")
def _base(self):
    self.pkgdesc = "Base package for manpages"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.options = ["empty"]

    return []


@subpackage("mandoc-apropos")
def _apropos(self):
    self.pkgdesc = f"{pkgdesc} (apropos trigger)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.triggers = ["/usr/share/man"]

    return [
        "usr/bin/apropos",
        "usr/bin/makewhatis",
        "usr/bin/whatis",
    ]
