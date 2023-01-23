pkgname = "less"
pkgver = "608"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-regex=posix"]
makedepends = ["ncurses-devel"]
pkgdesc = "Pager program similar to more(1)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:less OR GPL-3.0-or-later"
url = "http://www.greenwoodsoftware.com/less"
source = f"http://www.greenwoodsoftware.com/less/less-{pkgver}.tar.gz"
sha256 = "a69abe2e0a126777e021d3b73aa3222e1b261f10e64624d41ec079685a6ac209"
hardening = ["vis", "cfi"]

def post_install(self):
    self.install_file(self.files_path / "lesspipe.sh", "usr/bin", mode = 0o755)
    self.install_file(
        self.files_path / "zless.sh", "usr/bin", mode = 0o755, name = "zless"
    )
    self.install_link("less", "usr/bin/more")
    self.install_link("zless", "usr/bin/bzless")
    self.install_link("zless", "usr/bin/xzless")
    self.install_link("zless", "usr/bin/lzless")
    self.install_link("zless", "usr/bin/zstdless")
