pkgname = "xdotool"
pkgver = "4.20260303.1"
pkgrel = 0
build_style = "makefile"
make_install_args = ["INSTALLMAN=/usr/share/man"]
make_check_target = "test"
make_check_args = ["-j1"]
hostmakedepends = ["perl", "pkgconf"]
makedepends = ["libxinerama-devel", "libxkbcommon-devel", "libxtst-devel"]
checkdepends = [
    "bash",
    "gnome-session",
    "lsof",
    "procps",
    "ruby",
    "setxkbmap",
    "ugetopt",
    "xprop",
    "xserver-xorg-xvfb",
]
pkgdesc = "Command-line X11 automation tool"
license = "BSD-3-Clause"
url = "https://github.com/jordansissel/xdotool"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c1f971a384da588eb99ca0755fc4300316d49c1e612537e3f1de52215e104fa3"
# uses a ruby module (minitest) that used to be bundled and is no more
options = ["!check"]
exec_wrappers = [("/usr/bin/ugetopt", "getopt")]


def post_install(self):
    self.install_license("COPYRIGHT")


@subpackage("xdotool-devel")
def _(self):
    return self.default_devel()
