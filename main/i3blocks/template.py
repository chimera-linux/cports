pkgname = "i3blocks"
pkgver = "1.5"
pkgrel = 1
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
make_dir = "."
make_build_args = ["SYSCONFDIR=/etc"]
hostmakedepends = ["automake", "bash-completion", "pkgconf"]
pkgdesc = "Flexible scheduler for i3bar"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/vivien/i3blocks"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "41764d771043d0c06c23d75b1e3ca6b2b94279191483d03f10c5e034d6722ebf"
hardening = ["vis", "cfi"]


def post_install(self):
    # spurious file
    self.uninstall("usr/share/bash-completion/completions/bash-completion")
