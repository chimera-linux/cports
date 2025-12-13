pkgname = "mousepad"
pkgver = "0.6.5"
pkgrel = 1
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = [
    "gettext-devel",
    "meson",
    "pkgconf",
    "xfce4-dev-tools",
]
makedepends = [
    "glib-devel",
    "gspell-devel",
    "gtk+3-devel",
    "gtksourceview4-devel",
    "libxfce4ui-devel",
    "polkit-devel",
]
pkgdesc = "Xfce text editor"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/mousepad/start"
source = f"$(XFCE_SITE)/apps/mousepad/{pkgver[:-2]}/mousepad-{pkgver}.tar.xz"
sha256 = "21762bc8c3c4f120a4a509ce39f4a5a58dbc10e3f0da66cdc6d9a8c735fff2ac"
