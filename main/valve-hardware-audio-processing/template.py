pkgname = "valve-hardware-audio-processing"
pkgver = "0.56"
pkgrel = 4
# steamdeck only
archs = ["x86_64"]
build_style = "makefile"
make_build_args = ["FAUST_COMPILER=clang++"]
make_install_args = ["SHELL=/usr/bin/bash"]
make_use_env = True
hostmakedepends = ["bash", "faust"]
makedepends = ["boost-devel", "lv2"]
depends = ["bash", "dmidecode", "pipewire", "noise-suppression-for-voice"]
pkgdesc = "Steam Deck audio processing"
license = "GPL-2.0-or-later"
url = "https://gitlab.com/evlaV/valve-hardware-audio-processing"
source = (
    f"{url}/-/archive/{pkgver}/valve-hardware-audio-processing-{pkgver}.tar.gz"
)
sha256 = "d1b9e681cdcd9c75fda45d65a97d853449f863aff3d567a04ad320ed53a5debc"
# no tests
options = ["!cross", "!check"]


def init_configure(self):
    self.make_install_env = {"DEST_DIR": str(self.chroot_destdir)}


def post_install(self):
    # glibc bin from sof-bin
    self.uninstall("usr/lib/firmware/amd/sof/sof-logger")
    self.install_bin(self.files_path / "valve-init-audio-config")
    self.install_service(self.files_path / "valve-audio")
