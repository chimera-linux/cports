pkgname = "osinfo-db-tools"
pkgver = "1.12.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "perl"]
makedepends = [
    "glib-devel",
    "json-glib-devel",
    "libarchive-devel",
    "libxml2-devel",
    "libxslt-devel",
    "libsoup-devel",
]
checkdepends = ["python-pytest", "python-requests"]
pkgdesc = "Tools for managing osinfo database files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://libosinfo.org"
source = f"https://gitlab.com/libosinfo/osinfo-db-tools/-/archive/v{pkgver}/osinfo-db-tools-v{pkgver}.tar.gz"
sha256 = "5c2ef41e3395be7df090840d171996510c4c87ea8b40763ddf59ab9fb62e0be3"
hardening = ["vis", "cfi"]
options = ["!cross"]
