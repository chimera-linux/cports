pkgname = "drawterm"
_commit = "48d53278a8273bb39ca295e8f163563ab04b3530"
pkgver = "0_git20251011"
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
sha256 = "9b6e719705c84d3c744524dd39fc96d2fcf34c142c2bd529dad9ad0180f566bc"

# no tests
options = ["!check", "!cross"]


def install(self):
    self.install_bin("drawterm")
    self.install_man("drawterm.1")
    self.install_license("LICENSE")
