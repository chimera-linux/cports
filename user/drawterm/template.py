pkgname = "drawterm"
_commit = "4c336be61aa3d844ec2fdaa317f1d77d30eb876f"
pkgver = "0_git20260718"
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
sha256 = "c69531147b109a276944f47b80de2602349feb682ebebe1d018af0c26f82fbdc"

# no tests
options = ["!check", "!cross"]


def install(self):
    self.install_bin("drawterm")
    self.install_man("drawterm.1")
    self.install_license("LICENSE")
