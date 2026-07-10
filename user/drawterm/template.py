pkgname = "drawterm"
_commit = "fbfcaea5d4bebb1899b21182b4a2b4f513b4dbc8"
pkgver = "0_git20260702"
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
source = f"https://git.9front.org/git/plan9front/drawterm/{_commit}/snap.tar.gz>snap-{_commit}.tar.gz"
sha256 = "791d9942ba51c09cffaf092edd6921a65191820eab2685f6795fe025306d73d7"

# no tests
options = ["!check", "!cross"]


def install(self):
    self.install_bin("drawterm")
    self.install_man("drawterm.1")
    self.install_license("LICENSE")
