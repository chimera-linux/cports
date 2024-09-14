pkgname = "gnome-boxes"
pkgver = "46.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "gobject-introspection",
    "itstool",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "gtk+3-devel",
    "libarchive-devel",
    "libhandy-devel",
    "libosinfo-devel",
    "libportal-devel",
    "libsoup-devel",
    "libusb-devel",
    "libvirt-glib-devel",
    "libxml2-devel",
    "spice-gtk-devel",
    "webkitgtk-devel",
]
depends = [
    "libvirt",
    "qemu",
]
pkgdesc = "QEMU frontend for GNOME"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only"
url = "https://apps.gnome.org/Boxes"
source = f"$(GNOME_SITE)/gnome-boxes/{'.'.join(pkgver.rsplit('.')[:-1])}/gnome-boxes-{pkgver}.tar.xz"
sha256 = "900c177f6762640370a6634cf9e7d3cd8207e498367a8a667a6b731b04116036"
# gobject-introspection
# FIXME: lto makes the os-downloader crash (pick any os and it aborts instantly in os-downloader.vala)
options = ["!cross", "!lto"]

_arch = self.profile().arch
match _arch:
    case "x86_64" | "aarch64" | "riscv64":
        depends += [f"qemu-system-{_arch}"]
    case "ppc64le" | "ppc64":
        depends += ["qemu-system-ppc64"]
