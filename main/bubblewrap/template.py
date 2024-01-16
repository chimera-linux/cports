pkgname = "bubblewrap"
pkgver = "0.8.0"
pkgrel = 0
build_style = "gnu_configure"
make_check_args = ["-j1"]
hostmakedepends = ["pkgconf", "xsltproc", "docbook-xsl-nons"]
makedepends = ["libcap-devel"]
checkdepends = ["bash", "libcap-progs"]
pkgdesc = "Unprivileged sandboxing tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://github.com/containers/bubblewrap"
source = f"{url}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "957ad1149db9033db88e988b12bcebe349a445e1efc8a9b59ad2939a113d333a"
tool_flags = {"CFLAGS": ["-Wno-error,-Wformat-nonliteral"]}
hardening = ["vis", "cfi"]

configure_gen = []
