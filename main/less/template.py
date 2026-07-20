pkgname = "less"
pkgver = "704"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-regex=posix"]
hostmakedepends = ["automake"]
makedepends = ["ncurses-devel"]
checkdepends = ["perl"]
pkgdesc = "Pager program similar to more(1)"
license = "custom:less OR GPL-3.0-or-later"
url = "https://www.greenwoodsoftware.com/less"
source = f"https://www.greenwoodsoftware.com/less/less-{pkgver}.tar.gz"
sha256 = "20a0b0a2bb2525fa53c7eee9beb854b4c9cf172eabb209af7020743547bfe9fb"
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
