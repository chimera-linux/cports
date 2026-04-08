pkgname = "firejail"
pkgver = "0.9.80"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_dir = "."
hostmakedepends = ["gawk"]
makedepends = ["linux-headers"]
pkgdesc = "Linux namespaces and seccomp-bpf sandbox"
license = "GPL-2.0-only"
url = "https://github.com/netblue30/firejail"
source = f"{url}/releases/download/{pkgver}/firejail-{pkgver}.tar.xz"
sha256 = "0ccfb835c7a33c0dd5b4c522b8677c8af867eb65d4ef97a726d13cbc251164db"
file_modes = {"usr/bin/firejail": ("root", "root", 0o4755)}
hardening = ["vis", "cfi"]
# Disable tests as they require many dependencies (sudo, file, expect, firefox, xterm, etc.)
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
