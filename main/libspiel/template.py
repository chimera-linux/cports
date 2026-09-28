pkgname = "libspiel"
pkgver = "1.0.4"
pkgrel = 2
build_style = "meson"
configure_args = ["-Ddocs=false"]
hostmakedepends = ["gobject-introspection", "meson", "pkgconf"]
makedepends = [
    "glib-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
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
license = "LGPL-2.1-or-later"
url = "https://project-spiel.org"
source = f"https://github.com/project-spiel/libspiel/archive/refs/tags/SPIEL_{pkgver.replace('.', '_')}.tar.gz"
sha256 = "6060024bd640c1d94d3860731e15a7171aa440b3a52d3bebf83d23088096eb75"


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
