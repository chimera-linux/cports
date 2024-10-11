pkgname = "libspiel"
pkgver = "1.0.3"
pkgrel = 2
build_style = "meson"
configure_args = ["-Ddocs=false"]
hostmakedepends = ["gobject-introspection", "meson", "pkgconf"]
makedepends = [
    "glib-devel",
    "gstreamer-devel",
    "gst-plugins-base-devel",
    "libspeechprovider-devel",
]
checkdepends = [
    "dbus",
    "dbus-devel",
    "gst-plugins-good",
    "python-dasbus",
    "python-dbus",
    "python-tap.py",
]
pkgdesc = "Speech synthesis client library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://project-spiel.org"
source = f"https://github.com/project-spiel/libspiel/archive/refs/tags/SPIEL_{pkgver.replace('.', '_')}.tar.gz"
sha256 = "9a191f9c9836ce8e5ccbd199ad5ccb8c27f936bbbffa5c0e0241137d85dad974"


@subpackage("libspiel-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()


@subpackage("libspiel-provider-espeak")
def _(self):
    self.depends += ["speech-provider-espeak"]
    # the preferred provider
    self.install_if = [self.parent]
    self.subdesc = "espeak-ng provider metapackage"
    self.options = ["empty"]
    return []
