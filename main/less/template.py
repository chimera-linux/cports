pkgname = "less"
pkgver = "661"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--with-regex=posix"]
hostmakedepends = ["automake"]
makedepends = ["ncurses-devel"]
checkdepends = ["perl"]
pkgdesc = "Pager program similar to more(1)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:less OR GPL-3.0-or-later"
url = "https://www.greenwoodsoftware.com/less"
source = f"https://www.greenwoodsoftware.com/less/less-{pkgver}.tar.gz"
sha256 = "2b5f0167216e3ef0ffcb0c31c374e287eb035e4e223d5dae315c2783b6e738ed"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_file(self.files_path / "lesspipe.sh", "usr/bin", mode=0o755)
    self.install_file(
        self.files_path / "zless.sh", "usr/bin", mode=0o755, name="zless"
    )
    self.install_link("usr/bin/more", "less")
    self.install_link("usr/share/man/man1/more.1", "less.1")
    self.install_link("usr/bin/bzless", "zless")
    self.install_link("usr/bin/xzless", "zless")
    self.install_link("usr/bin/lzless", "zless")
    self.install_link("usr/bin/zstdless", "zless")
