pkgname = "celluloid"
pkgver = "0.28"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["glib-devel", "gettext", "meson", "pkgconf"]
makedepends = [
    "appstream-glib-devel",
    "glib-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libepoxy-devel",
    "mpv-devel",
]
pkgdesc = "GTK frontend for mpv"
license = "GPL-3.0-or-later"
url = "https://celluloid-player.github.io"
source = f"https://github.com/celluloid-player/celluloid/releases/download/v{pkgver}/celluloid-{pkgver}.tar.xz"
sha256 = "5b36fdf0dfff873d149655064350e370872dc54226dd2cbfcc02fa0c107e533a"
