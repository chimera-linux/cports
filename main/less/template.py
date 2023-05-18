pkgname = "less"
pkgver = "633"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-regex=posix"]
make_cmd = "gmake"
hostmakedepends = ["gmake"]
makedepends = ["ncurses-devel"]
pkgdesc = "Pager program similar to more(1)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:less OR GPL-3.0-or-later"
url = "http://www.greenwoodsoftware.com/less"
source = f"http://www.greenwoodsoftware.com/less/less-{pkgver}.tar.gz"
sha256 = "2f201d64b828b88af36dfe6cfdba3e0819ece2e446ebe6224813209aaefed04f"
hardening = ["vis", "cfi"]
# test suite not shipped
options = ["!check"]

def post_install(self):
    self.install_file(self.files_path / "lesspipe.sh", "usr/bin", mode = 0o755)
    self.install_file(
        self.files_path / "zless.sh", "usr/bin", mode = 0o755, name = "zless"
    )
    self.install_link("less", "usr/bin/more")
    self.install_link("less.1", "usr/share/man/man1/more.1")
    self.install_link("zless", "usr/bin/bzless")
    self.install_link("zless", "usr/bin/xzless")
    self.install_link("zless", "usr/bin/lzless")
    self.install_link("zless", "usr/bin/zstdless")
