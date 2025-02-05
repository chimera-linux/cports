pkgname = "xmlto"
pkgver = "0.0.29"
pkgrel = 1
build_style = "gnu_configure"
configure_env = {"GETOPT": "ugetopt"}
hostmakedepends = [
    "automake",
    "bash",
    "docbook-xsl-nons",
    "flex",
    "libtool",
    "ugetopt",
    "libxslt-progs",
]
depends = ["bash", "ugetopt", "libxslt-progs", "docbook-xsl-nons"]
pkgdesc = "Tool to help transform XML documents into other formats"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://pagure.io/xmlto"
source = f"{url}/archive/{pkgver}/xmlto-{pkgver}.tar.gz"
sha256 = "40504db68718385a4eaa9154a28f59e51e59d006d1aa14f5bc9d6fded1d6017a"
hardening = ["vis", "cfi"]
