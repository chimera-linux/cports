pkgname = "musl-static-nolto"
pkgver = "1.2.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--prefix=/usr", "--disable-gcc-wrapper"]
make_cmd = "gmake"
hostmakedepends = ["gmake"]
depends = [f"musl-devel={pkgver}-r{pkgrel}"]
# provides a musl-static, but lower priority
provides = [f"musl-static={pkgver}-r{pkgrel}"]
pkgdesc = "Musl C library (static)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.musl-libc.org"
source = f"http://www.musl-libc.org/releases/musl-{pkgver}.tar.gz"
sha256 = "9b969322012d796dc23dda27a35866034fa67d8fb67e0e2c45c913c3d43219dd"
# segfaults otherwise
hardening = ["!scp"]
# does not ship tests
options = ["!check", "!lto"]

def do_install(self):
    self.install_file("build/lib/libc.a", "usr/lib")
