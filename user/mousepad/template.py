pkgname = "mousepad"
pkgver = "0.7.0"
pkgrel = 0
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
sha256 = "e86c59feb08126d4cace368432c16b2dee8e519aaca8a9d2b409ae1cdd200802"
