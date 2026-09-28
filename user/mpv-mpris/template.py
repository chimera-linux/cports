pkgname = "mpv-mpris"
pkgver = "1.3"
pkgrel = 0
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
sha256 = "47deb26641b2f45edbbaf48a9136177b565b64f544f0fa7b956739fc7a4fc0a8"
options = ["etcfiles"]


def install(self):
    self.install_file("mpris.so", "usr/lib/mpv-mpris", 0o755)
    self.install_dir("etc/mpv/scripts")
    self.install_link(
        "etc/mpv/scripts/mpris.so",
        "../../../usr/lib/mpv-mpris/mpris.so",
    )
    self.install_license("LICENSE")
