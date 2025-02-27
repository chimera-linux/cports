pkgname = "distrobox"
pkgver = "1.8.1.2"
pkgrel = 0
depends = ["curl", "podman", "polkit"]
pkgdesc = "Use any Linux distribution inside your terminal"
license = "GPL-3.0-only"
url = "https://distrobox.it"
source = f"https://github.com/89luca89/distrobox/archive/{pkgver}.tar.gz"
sha256 = "3ecbce9b8c5b5df941f986798ffa6ea7fdf742223d42204207974c4323d5b9fc"
options = ["!lintcomp"]  # zsh _distrobox_running_containers


def install(self):
    self.do("./install", "--prefix", f"{self.chroot_destdir}/usr")
    self.install_file(self.files_path / "distrobox.conf", "usr/share/distrobox")
    self.install_file("docs/*.md", "usr/share/doc/distrobox", glob=True)
