pkgname = "xdg-desktop-portal"
pkgver = "1.20.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "bubblewrap",
    "gettext",
    "glib-devel",
    "meson",
    "pkgconf",
    "python-docutils",
]
makedepends = [
    "flatpak-devel",
    "fuse-devel",
    "gdk-pixbuf-devel",
    "geoclue-devel",
    "gst-plugins-base-devel",
    "json-glib-devel",
    "libportal-devel",
    "pipewire-devel",
]
checkdepends = [
    "bash",
    "dbus",
    "gst-plugins-good",
    "gstreamer",
    "python-dbus",
    "python-dbusmock",
    "python-gobject",
    "python-pytest",
    "umockdev-devel",
]
pkgdesc = "Desktop integration portal"
license = "LGPL-2.1-or-later"
url = "https://github.com/flatpak/xdg-desktop-portal"
source = f"{url}/releases/download/{pkgver}/xdg-desktop-portal-{pkgver}.tar.xz"
sha256 = "9528eb3b060b88ac82f294fbdc6af5f4d3adfa42575f2cd816cab3d3e0a7a68c"


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.install_file(
        self.files_path / "portals.conf", "usr/share/xdg-desktop-portal"
    )


@subpackage("xdg-desktop-portal-devel")
def _(self):
    self.depends = [self.parent]
    return self.default_devel()
