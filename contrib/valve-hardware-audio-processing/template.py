pkgname = "valve-hardware-audio-processing"
pkgver = "0.55"
pkgrel = 0
# steamdeck only
archs = ["x86_64"]
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["FAUST_COMPILER=clang++"]
make_install_args = ["SHELL=/usr/bin/bash"]
make_use_env = True
hostmakedepends = ["gmake", "bash", "faust"]
makedepends = ["boost-devel", "lv2"]
depends = ["pipewire", "noise-suppression-for-voice"]
pkgdesc = "Steam Deck audio processing"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.com/evlaV/valve-hardware-audio-processing"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "be4582c7e3030fcd918026ca6de422e31a93f113e244594ae4c4a30b46d05376"
# no tests
options = ["!cross", "!check"]


def init_configure(self):
    self.make_install_env = {"DEST_DIR": str(self.chroot_destdir)}


def post_install(self):
    # glibc bin from sof-bin
    self.uninstall("usr/lib/firmware/amd/sof/sof-logger")
