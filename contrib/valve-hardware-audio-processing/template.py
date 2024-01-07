pkgname = "valve-hardware-audio-processing"
pkgver = "0.39"
pkgrel = 1
archs = ["x86_64"]
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["FAUST_COMPILER=clang++"]
make_use_env = True
hostmakedepends = ["gmake", "bash", "faust"]
makedepends = ["boost-devel", "lv2"]
depends = ["pipewire", "noise-suppression-for-voice"]
pkgdesc = "Steam Deck audio processing"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.com/evlaV/valve-hardware-audio-processing"
source = f"{url}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "1cf9d639dc88651087e8ce1e536ed1e260ce52211ba8794cba2a7d29db4b4efb"
# no tests
options = ["!cross", "!check"]


def init_configure(self):
    self.make_install_env = {"DEST_DIR": str(self.chroot_destdir)}
