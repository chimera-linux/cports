pkgname = "drawterm"
_commit = "877bce095a192ead0e9b6e0d5ce3071482cf0f6e"
pkgver = "0_git20240908"
pkgrel = 0
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
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://drawterm.9front.org"
_wlr_protocols_commit = "2b8d43325b7012cc3f9b55c08d26e50e42beac7d"
source = [
    f"https://git.9front.org/git/plan9front/drawterm/{_commit}/snap.tar.gz",
    f"!https://gitlab.freedesktop.org/wlroots/wlr-protocols/-/raw/{_wlr_protocols_commit}/unstable/wlr-virtual-pointer-unstable-v1.xml>{_wlr_protocols_commit}.xml",
]
sha256 = [
    "04db646aac493605973dca6679af9ee04f783e49094d4a46d52a4433b5f5bf02",
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
