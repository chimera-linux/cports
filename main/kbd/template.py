pkgname = "kbd"
pkgver = "2.7.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-tests"]  # tests force autom4te
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libtool",
    "pkgconf",
]
makedepends = ["linux-pam-devel", "linux-headers"]
pkgdesc = "Linux keyboard utilities"
license = "GPL-2.0-or-later"
url = "http://www.kbd-project.org"
source = f"$(KERNEL_SITE)/utils/kbd/kbd-{pkgver}.tar.xz"
sha256 = "f167d899d92b56ccf12f6f49355173f93870a95f15d8aeebf5fdcd28a621aca8"
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
    self.install_dir("usr/lib/kbd")
    self.rename("usr/bin/findkeys", "usr/lib/kbd/findkeys", relative=False)

    for f in ["sun", "amiga", "atari", "i386/olpc"]:
        self.uninstall(f"usr/share/keymaps/{f}")
