pkgname = "rhash"
pkgver = "1.4.5"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--sysconfdir=/etc",
    "--enable-openssl",
    "--disable-openssl-runtime",
    "--enable-lib-static",
    "--enable-lib-shared",
]
make_build_target = "all"
make_build_args = ["lib-shared"]
make_install_target = "install"
make_install_args = ["install-lib-shared"]
makedepends = ["openssl3-devel"]
pkgdesc = "Utility for computing hash sums and creating magnet links"
maintainer = "q66 <q66@chimera-linux.org>"
license = "0BSD"
url = "https://github.com/rhash/RHash"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "6db837e7bbaa7c72c5fd43ca5af04b1d370c5ce32367b9f6a1f7b49b2338c09a"


def init_configure(self):
    self.configure_args += [
        "--cc=" + self.get_tool("CC"),
        "--ar=" + self.get_tool("AR"),
        "--extra-cflags=" + self.get_cflags(shell=True),
        "--extra-ldflags=" + self.get_ldflags(shell=True),
    ]


def post_install(self):
    self.make.invoke(
        None,
        [
            "-C",
            "librhash",
            "install-lib-headers",
            "PREFIX=/usr",
            "DESTDIR=" + str(self.chroot_destdir),
        ],
    )

    self.install_link("usr/lib/librhash.so", "librhash.so.1")

    self.install_license("COPYING")


@subpackage("rhash-devel")
def _(self):
    return self.default_devel()
