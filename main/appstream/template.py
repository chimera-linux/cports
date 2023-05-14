pkgname = "appstream"
pkgver = "0.16.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dsystemd=false", "-Dstemming=false"]
hostmakedepends = ["pkgconf", "meson", "gperf", "gettext-tiny", "itstool", "xsltproc", "gtk-doc-tools"]
makedepends = ["glib-devel", "libxmlb-devel", "gobject-introspection", "libxml2-devel", "libyaml-devel", "libcurl-devel"]
pkgdesc = "Tools and libraries to work with AppStream metadata"
maintainer = "eater <=@eater.me>"
license = "LGPL-2.1"
url = "http://www.freedesktop.org/wiki/Distributions/AppStream"
source = f"https://github.com/ximion/appstream/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "266c75a302064ad7e50905a365fa64537268c318cb1cf19dd003911a781d6797"

@subpackage("appstream-devel-static")
def _static(self):
  return self.default_static()

@subpackage("appstream-devel")
def _devel(self):
  return self.default_devel()
