pkgname = "rhash"
pkgver = "1.4.6"
pkgrel = 2
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
license = "0BSD"
url = "https://github.com/rhash/RHash"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "9f6019cfeeae8ace7067ad22da4e4f857bb2cfa6c2deaa2258f55b2227ec937a"
tool_flags = {"CFLAGS": ["-fPIC"]}


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
