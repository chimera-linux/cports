pkgname = "drawterm"
_commit = "903bcd8dba9cb9dfc70707a28089c469e5302539"
pkgver = "0_git20250629"
pkgrel = 0
build_style = "makefile"
make_env = {"CONF": "linux"}
hostmakedepends = ["pkgconf", "wayland-progs"]
makedepends = [
    "libdecor-devel",
    "libxkbcommon-devel",
    "linux-headers",
    "pipewire-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "Interface to Plan 9 systems"
license = "MIT"
url = "https://drawterm.9front.org"
_wlr_protocols_commit = "2ec67ebd26b73bada12f3fa6afdd51563b656722"
source = [
    f"https://git.9front.org/git/plan9front/drawterm/{_commit}/snap.tar.gz>snap-{_commit}.tar.gz",
    f"!https://gitlab.freedesktop.org/wlroots/wlr-protocols/-/raw/{_wlr_protocols_commit}/unstable/wlr-virtual-pointer-unstable-v1.xml>{_wlr_protocols_commit}.xml",
]
sha256 = [
    "d281e1397e6d63be9db1040245c0d506d8f70ff9522587871b531e2e892bc80d",
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
