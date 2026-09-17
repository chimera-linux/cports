pkgname = "gnome-shell-extension-gsconnect"
pkgver = "72"
pkgrel = 1
# until release with gnome 51
_commit = "0be3a14d8a6db8bbd287d694e3397ce9f9888f0f"
build_style = "meson"
configure_args = ["-Dinstalled_tests=false"]
make_check_wrapper = ["dbus-run-session", "--", "wlheadless-run", "--"]
hostmakedepends = [
    "bash",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "gtk+3-update-icon-cache",
    "libxml2-progs",
    "meson",
    "pkgconf",
]
makedepends = ["dbus-devel"]
depends = ["evolution-data-server", "gnome-shell", "gsound", "openssl3"]
checkdepends = ["dbus", "gnome-shell", "xwayland-run"]
pkgdesc = "KDE Connect implementation for GNOME"
license = "GPL-2.0-or-later"
url = "https://github.com/GSConnect/gnome-shell-extension-gsconnect"
source = f"{url}/archive/{_commit}.tar.gz"
# source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "88ae39996b69f3a7e7d4f90bd1cec37991c01692eb82bb5c889fb49355280356"
# All tests fail in latest release https://github.com/GSConnect/gnome-shell-extension-gsconnect/issues/1786
options = ["etcfiles", "!check"]
