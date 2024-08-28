pkgname = "argp-standalone"
pkgver = "1.4.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake"]
pkgdesc = "Standalone argp implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/ericonr/argp-standalone"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "879d76374424dce051b812f16f43c6d16de8dbaddd76002f83fd1b6e57d39e0b"
tool_flags = {"CFLAGS": ["-fPIC"]}
options = ["!lto", "!splitstatic"]


def install(self):
    self.install_file("build/libargp.a", "usr/lib")
    self.install_file("argp.h", "usr/include")
