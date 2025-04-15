pkgname = "drawterm"
_commit = "daf2ab4550e555cdb6c58f2a9e647c2259a634de"
pkgver = "0_git20250112"
pkgrel = 1
build_style = "makefile"
make_env = {"CONF": "linux"}
hostmakedepends = ["pkgconf", "wayland-progs"]
makedepends = [
    "libxkbcommon-devel",
    "linux-headers",
    "pipewire-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Interface to Plan 9 systems"
license = "MIT"
url = "https://drawterm.9front.org"
_wlr_protocols_commit = "ffb89ac790096f6e6272822c8d5df7d0cc6fcdfa"
source = [
    f"https://git.9front.org/git/plan9front/drawterm/{_commit}/snap.tar.gz",
    f"!https://gitlab.freedesktop.org/wlroots/wlr-protocols/-/raw/{_wlr_protocols_commit}/unstable/wlr-virtual-pointer-unstable-v1.xml>{_wlr_protocols_commit}.xml",
]
sha256 = [
    "0080192d1ee0e60840b4fda6362814eded11ed9f364bab4fef626487be1aa94f",
    "3ff6d540be0bc5228195bf072bde42117ea17945a5c2061add5d3cf97d6bb524",
]
# no tests
options = ["!check", "!cross"]


def init_build(self):
    self.make_build_args += [
        f"WLR_VIRTUAL_POINTER={self.chroot_sources_path}/{_wlr_protocols_commit}.xml"
    ]


def install(self):
    self.install_bin("drawterm")
    self.install_man("drawterm.1")
    self.install_license("LICENSE")
