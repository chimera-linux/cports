pkgname = "osinfo-db-tools"
pkgver = "1.11.0"
pkgrel = 0
build_style = "meson"
make_check_env = {"MAKE": "gmake"}
hostmakedepends = ["meson", "pkgconf", "perl"]
makedepends = [
    "glib-devel",
    "json-glib-devel",
    "libarchive-devel",
    "libxml2-devel",
    "libxslt-devel",
    "libsoup-devel",
]
checkdepends = ["gmake", "python-pytest", "python-requests"]
pkgdesc = "Tools for managing osinfo database files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://libosinfo.org"
source = f"https://gitlab.com/libosinfo/osinfo-db-tools/-/archive/v{pkgver}/{pkgname}-v{pkgver}.tar.gz"
sha256 = "b03429cad1dadf5e20bd2d24c4b130df35882ed22ebfbadb5f7acd50c6218ee2"
hardening = ["vis", "cfi"]
options = ["!cross"]
