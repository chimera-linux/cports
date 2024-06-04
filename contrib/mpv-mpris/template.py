pkgname = "mpv-mpris"
pkgver = "1.1"
pkgrel = 1
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "test"
make_use_env = True
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["ffmpeg-devel", "glib-devel", "mpv-devel"]
depends = ["mpv"]
checkdepends = [
    "bash",
    "dbus",
    "jq",
    "mpv",
    "playerctl",
    "socat",
    "sound-theme-freedesktop",
    "xauth",
    "xserver-xorg-xvfb",
]
pkgdesc = "MPRIS plugin for mpv"
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://github.com/hoyon/mpv-mpris"
source = f"https://github.com/hoyon/mpv-mpris/archive/{pkgver}.tar.gz"
sha256 = "71008aa181bccf4bc7b2b5b9673e9993b1d1f5b7e2c189dc3724ab23ef1f6ebb"


def do_install(self):
    self.install_file("mpris.so", "etc/mpv/scripts", 0o755)
    self.install_license("LICENSE")
