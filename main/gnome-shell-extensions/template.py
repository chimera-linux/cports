pkgname = "gnome-shell-extensions"
pkgver = "41.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "gettext-tiny"]
depends = [f"gnome-shell>={pkgver}", "nautilus"]
pkgdesc = "Optional extensions for GNOME shell"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/GnomeShell/Extensions"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "d0e6f2273f08d52d925fc2bb66b47b28e5ef50d1b8a14020877c662423d507d3"
