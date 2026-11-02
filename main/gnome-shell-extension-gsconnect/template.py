pkgname = "gnome-shell-extension-gsconnect"
pkgver = "74"
pkgrel = 0
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
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7eda214a9d48e3e8f674c4f37d551835d7c10f3695c5830294ff1562f4dbd184"
# All tests fail in latest release https://github.com/GSConnect/gnome-shell-extension-gsconnect/issues/1786
options = ["etcfiles", "!check"]
