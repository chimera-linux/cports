pkgname = "gnome-video-effects"
pkgver = "0.5.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "gettext-tiny"]
makedepends = ["gstreamer-devel"]
pkgdesc = "Collection of GStreamer effects for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-video-effects"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "4dc68e9b38fdfc1e8e0414e2d7ee83ace78efdee76f30506cc9dcd07394ad0c8"

# FIXME visibility
hardening = ["!vis"]
