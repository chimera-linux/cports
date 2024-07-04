_trip = "arm-none-eabi"
pkgname = f"binutils-{_trip}"
pkgver = "2.42"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    f"--target={_trip}",
    f"--with-sysroot=/usr/{_trip}",
    "--prefix=/usr",
    "--sbindir=/usr/bin",
    "--libdir=/usr/lib",
    "--mandir=/usr/share/man",
    "--infodir=/usr/share/info",
    "--without-debuginfod",
    "--with-system-zlib",
    "--with-mmap",
    "--with-pic",
    "--disable-install-libbfd",
    "--disable-multilib",
    "--disable-werror",
    "--disable-shared",
    "--disable-gold",
    "--disable-nls",
    "--enable-default-hash-style=gnu",
    "--enable-deterministic-archives",
    "--enable-64-bit-bfd",
    "--enable-threads",
    "--enable-plugins",
    "--enable-relro",
]
# requires specific version of autoconf
configure_gen = []
make_cmd = "gmake"
hostmakedepends = ["gmake", "flex", "texinfo"]
makedepends = ["zlib-ng-compat-devel"]
pkgdesc = "GNU binutils for ARM bare metal targets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/binutils"
source = f"$(GNU_SITE)/binutils/binutils-{pkgver}.tar.xz"
sha256 = "f6e4d41fd5fc778b06b7891457b3620da5ecea1006c6a4a41ae998109f85a800"
# resistance is futile
options = ["!check", "!lto", "linkundefver"]

if self.profile().cross:
    configure_args += [
        f"--host={self.profile().triplet}",
        f"--with-build-sysroot={self.profile().sysroot}",
    ]


def post_install(self):
    # fix up hardlinks
    for f in (self.destdir / f"usr/{_trip}/bin").iterdir():
        self.uninstall(f"usr/bin/{_trip}-{f.name}")
        self.install_link(
            f"usr/bin/{_trip}-{f.name}", f"../{_trip}/bin/{f.name}"
        )
    # this is also a hardlink
    self.uninstall(f"usr/{_trip}/bin/ld")
    self.install_link(f"usr/{_trip}/bin/ld", "ld.bfd")
    # remove unnecessary dupe
    self.uninstall("usr/lib")
