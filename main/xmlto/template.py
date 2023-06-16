pkgname = "xmlto"
pkgver = "0.0.28"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["ac_cv_path_BASH=/usr/bin/bash"]
configure_env = {"GETOPT": "ugetopt"}
hostmakedepends = [
    "bash",
    "xsltproc",
    "docbook-xsl-nons",
    "ugetopt",
    "automake",
    "libtool",
    "flex",
]
depends = ["bash", "ugetopt", "xsltproc", "docbook-xsl-nons"]
pkgdesc = "Tool to help transform XML documents into other formats"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "http://cyberelk.net/tim/software/xmlto"
source = f"http://anduin.linuxfromscratch.org/BLFS/{pkgname}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "1130df3a7957eb9f6f0d29e4aa1c75732a7dfb6d639be013859b5c7ec5421276"
hardening = ["vis", "cfi"]
