pkgname = "libnl"
pkgver = "3.12.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
hostmakedepends = ["automake", "libtool", "pkgconf", "flex", "bison"]
makedepends = ["linux-headers"]
checkdepends = ["bash"]
pkgdesc = "Netlink Protocol Library Suite"
license = "LGPL-2.1-only"
url = "https://github.com/thom311/libnl"
source = f"{url}/releases/download/libnl{pkgver.replace('.', '_')}/libnl-{pkgver}.tar.gz"
sha256 = "fc51ca7196f1a3f5fdf6ffd3864b50f4f9c02333be28be4eeca057e103c0dd18"
options = ["etcfiles"]


@subpackage("libnl-devel")
def _(self):
    return self.default_devel()


@subpackage("libnl-progs")
def _(self):
    return self.default_progs(
        man="18",
        extra=[
            "usr/lib/libnl",
        ],
    )
