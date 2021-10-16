pkgname = "less"
pkgver = "581.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-regex=posix"]
makedepends = ["ncurses-devel"]
pkgdesc = "Pager program similar to more(1)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:less OR GPL-3.0-or-later"
url = "http://www.greenwoodsoftware.com/less"
source = f"http://www.greenwoodsoftware.com/less/less-{pkgver}.tar.gz"
sha256 = "ce34b47caf20a99740672bf560fc48d5d663c5e78e67bc254e616b9537d5d83b"

def post_extract(self):
    # permissions are bad by default and patch refuses it
    (self.cwd / "Makefile.in").chmod(0o644)

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
