pkgname = "osinfo-db-tools"
pkgver = "1.10.0"
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
source = f"https://gitlab.com/libosinfo/{pkgname}/-/archive/v{pkgver}/{pkgname}-v{pkgver}.tar.gz"
sha256 = "3677ee201cfebcb673b543b9f6fe43d67bc6fb1b55a2540c1af8ce13358c7e6f"
hardening = ["vis", "cfi"]
options = ["!cross"]
