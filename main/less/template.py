pkgname = "less"
pkgver = "590"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-regex=posix"]
makedepends = ["ncurses-devel"]
pkgdesc = "Pager program similar to more(1)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:less OR GPL-3.0-or-later"
url = "http://www.greenwoodsoftware.com/less"
source = f"http://www.greenwoodsoftware.com/less/less-{pkgver}.tar.gz"
sha256 = "6aadf54be8bf57d0e2999a3c5d67b1de63808bb90deb8f77b028eafae3a08e10"

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
