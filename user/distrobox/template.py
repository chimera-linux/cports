pkgname = "distrobox"
pkgver = "1.8.2.5"
pkgrel = 0
depends = ["curl", "podman", "polkit"]
pkgdesc = "Use any Linux distribution inside your terminal"
license = "GPL-3.0-only"
url = "https://distrobox.it"
source = f"https://github.com/89luca89/distrobox/archive/{pkgver}.tar.gz"
sha256 = "0c3bc4785ee3be3b89f93abb7cc0a9f60e56989e81319af140a4b60403b18f80"
options = ["!lintcomp"]  # zsh _distrobox_running_containers


def install(self):
    self.do("./install", "--prefix", f"{self.chroot_destdir}/usr")
    self.install_file(self.files_path / "distrobox.conf", "usr/share/distrobox")
    self.install_file("docs/*.md", "usr/share/doc/distrobox", glob=True)
