pkgname = "mpv-mpris"
pkgver = "1.2"
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
sha256 = "ecdc66f0182a38164b8bdc79502c575df3d2c4453bae5bff225c4e5ce9dbef6c"
options = ["etcfiles"]


def install(self):
    self.install_file("mpris.so", "usr/lib/mpv-mpris", 0o755)
    self.install_dir("etc/mpv/scripts")
    self.install_link(
        "etc/mpv/scripts/mpris.so",
        "../../../usr/lib/mpv-mpris/mpris.so",
    )
    self.install_license("LICENSE")
