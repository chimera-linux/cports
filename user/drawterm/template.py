pkgname = "drawterm"
_commit = "789b8fe40e156ad0252230b13dd4ada96f3eed8b"
pkgver = "0_git20240909"
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
    "d5353af6d0557b345cb0df70141cdc9a443a747dc24d888f059750933ee2ad29",
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
