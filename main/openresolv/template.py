pkgname = "openresolv"
pkgver = "3.13.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--libexecdir=/usr/libexec/resolvconf"]
make_dir = "."
pkgdesc = "Management framework for resolv.conf"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://roy.marples.name/projects/openresolv"
source = f"https://github.com/NetworkConfiguration/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "8c30455bdc37657b6346b88864983ec669b9f303f54cc6eb33c45199f4897f7b"
hardening = ["vis", "cfi"]
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
    # rename
    self.mv(
        self.destdir / "usr/bin/resolvconf",
        self.destdir / "usr/bin/resolvconf-openresolv",
    )
    self.mv(
        self.destdir / "usr/share/man/man8/resolvconf.8",
        self.destdir / "usr/share/man/man8/resolvconf-openresolv.8",
    )


configure_gen = []
