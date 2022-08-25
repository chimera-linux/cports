pkgname = "kbd"
pkgver = "2.5.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--datadir=/usr/share/kbd",
    "--localedir=/usr/share/kbd/locale",
    "--disable-tests" # tests force autom4te
]
make_cmd = "gmake"
hostmakedepends = ["gmake", "flex", "pkgconf"]
makedepends = ["linux-pam-devel", "linux-headers"]
pkgdesc = "Linux keyboard utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://www.kbd-project.org"
source = f"$(KERNEL_SITE)/utils/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "ccdf452387a6380973d2927363e9cbb939fa2068915a6f937ff9d24522024683"

def post_patch(self):
    # Rename keymap files with the same names
    # this is needed because when only name of keymap is specified
    # loadkeys loads the first keymap it can find, which is bad
    # this should be removed when upstream adopts the change
    with self.pushd("data/keymaps/i386"):
        self.mv("qwertz/cz.map", "qwertz/cz-qwertz.map")
        self.mv("olpc/es.map", "olpc/es-olpc.map")
        self.mv("olpc/pt.map", "olpc/pt-olpc.map")
        self.mv("fgGIod/trf.map", "fgGIod/trf-fgGIod.map")
        self.mv("colemak/en-latin9.map", "colemak/colemak.map")

    # fixes from fedora
    # 7-bit maps are obsolete; so are non-euro maps
    with self.pushd("data/keymaps/i386/qwerty"):
        self.cp("pt-latin9.map", "pt.map")
        self.cp("sv-latin1.map", "se-latin1.map")

    with self.pushd("data/keymaps/i386/azerty"):
        self.mv("fr.map", "fr-old.map")
        self.cp("fr-latin9.map", "fr.map")
        self.cp("fr-latin9.map", "fr-latin0.map") # legacy alias

def post_install(self):
    for f in ["sun", "amiga", "atari"]:
        self.rm(self.destdir / f"usr/share/kbd/keymaps/{f}", recursive = True)
