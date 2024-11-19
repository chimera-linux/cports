pkgname = "gnome-remote-desktop"
pkgver = "47.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dvnc=true",
    "-Dsystemd=false",
    "-Dtests=false",
    "-Duser=_gnome-remote-desktop",
]
hostmakedepends = ["cmake", "meson", "pkgconf", "asciidoc", "gettext"]
makedepends = [
    "cairo-devel",
    "dbus-devel",
    "fdk-aac-devel",
    "ffmpeg-devel",
    "nv-codec-headers",
    "freerdp-devel",
    "fuse-devel",
    "glib-devel",
    "libdrm-devel",
    "libei-devel",
    "libepoxy-devel",
    "libgudev-devel",
    "libnotify-devel",
    "libsecret-devel",
    "libvncserver-devel",
    "libxkbcommon-devel",
    "opus-devel",
    "pipewire-devel",
    "polkit-devel",
    "tpm2-tss-devel",
]
pkgdesc = "GNOME Remote Desktop server"
maintainer = "Denis Strizhkin <strdenis02@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-remote-desktop"
source = f"{url}/-/archive/{pkgver}/gnome-remote-desktop-{pkgver}.tar.gz"
sha256 = "bfdfc646947aaac02e7c3230386a34872f501d6ddd66484154536949f51bf1f1"
# needs real /sys /proc for some udev things to work
options = ["!check"]


def post_install(self):
    self.install_sysusers(
        self.cwd / "build/data/gnome-remote-desktop-sysusers.conf"
    )
    self.install_tmpfiles(
        self.cwd / "build/data/gnome-remote-desktop-tmpfiles.conf"
    )
