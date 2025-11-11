pkgname = "mpv-mpris"
pkgver = "1.1"
pkgrel = 2
build_style = "makefile"
make_check_target = "test"
make_use_env = True
hostmakedepends = ["pkgconf"]
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
license = "MIT"
url = "https://github.com/hoyon/mpv-mpris"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "71008aa181bccf4bc7b2b5b9673e9993b1d1f5b7e2c189dc3724ab23ef1f6ebb"


def install(self):
    self.install_file("mpris.so", "etc/mpv/scripts", 0o755)
    self.install_license("LICENSE")
