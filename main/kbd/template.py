pkgname = "kbd"
pkgver = "2.6.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-tests"]  # tests force autom4te
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "pkgconf",
    "automake",
    "libtool",
    "gettext-tiny-devel",
]
makedepends = ["linux-pam-devel", "linux-headers"]
pkgdesc = "Linux keyboard utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://www.kbd-project.org"
source = f"$(KERNEL_SITE)/utils/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "33e3bb3c3f55933b10f053b14b5f69a2e24c28543e9ec7690246fe47628dd94f"
hardening = ["vis", "cfi"]


def post_patch(self):
    # rename conflicting keymaps
    with self.pushd("data/keymaps/i386"):
        self.mv("qwerty/cz.map", "qwerty/cz-qwerty.map")
        self.mv("fgGIod/trf.map", "fgGIod/trf-fgGIod.map")

    # fixes from fedora
    # 7-bit maps are obsolete; so are non-euro maps
    with self.pushd("data/keymaps/i386/qwerty"):
        self.cp("pt-latin9.map", "pt.map")
        self.cp("sv-latin1.map", "se-latin1.map")

    with self.pushd("data/keymaps/i386/azerty"):
        self.mv("fr.map", "fr-old.map")
        self.cp("fr-latin9.map", "fr.map")
        self.cp("fr-latin9.map", "fr-latin0.map")  # legacy alias


def post_install(self):
    self.install_dir("usr/libexec/kbd")
    self.mv(self.destdir / "usr/bin/findkeys", self.destdir / "usr/libexec/kbd")

    for f in ["sun", "amiga", "atari", "i386/olpc"]:
        self.rm(self.destdir / f"usr/share/keymaps/{f}", recursive=True)
