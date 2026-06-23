pkgname = "xdg-desktop-portal"
pkgver = "1.22.1"
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
sha256 = "d4879ddb3d65ff1a8f19187497e6f13dc5d267bcac404a5d501218be355753d3"


def post_install(self):
    self.uninstall("usr/lib/systemd")
    self.install_file(
        self.files_path / "portals.conf", "usr/share/xdg-desktop-portal"
    )


@subpackage("xdg-desktop-portal-devel")
def _(self):
    self.depends = [self.parent]
    return self.default_devel()
