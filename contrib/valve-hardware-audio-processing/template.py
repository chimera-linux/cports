pkgname = "valve-hardware-audio-processing"
pkgver = "0.49"
pkgrel = 1
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
sha256 = "1c4c5ab7259f0e0bb57cfb42f55ffd742023ad7b0f3b6f1e30432b68f18ea1af"
# no tests
options = ["!cross", "!check"]


def init_configure(self):
    self.make_install_env = {"DEST_DIR": str(self.chroot_destdir)}


def post_install(self):
    # glibc bin from sof-bin
    self.uninstall("usr/lib/firmware/amd/sof/sof-logger")
