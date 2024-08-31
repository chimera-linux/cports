pkgname = "libpcap"
pkgver = "1.10.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-ipv6",
    "--with-libnl",
    "--with-pcap=linux",
    "--enable-usb",
]
hostmakedepends = ["pkgconf", "flex"]
makedepends = ["libnl-devel", "libusb-devel", "linux-headers"]
pkgdesc = "System-independent interface for user-level packet capture"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.tcpdump.org"
source = f"{url}/release/libpcap-{pkgver}.tar.gz"
sha256 = "37ced90a19a302a7f32e458224a00c365c117905c2cd35ac544b6880a81488f0"
hardening = ["!vis", "!cfi"]
# no check target
options = ["!check"]


def init_configure(self):
    incp = self.profile().sysroot / "usr/include/libnl3"
    self.tool_flags["CFLAGS"] = [f"-I{incp}"]


def post_install(self):
    self.install_license("LICENSE")
    for f in (self.destdir / "usr/share/man/man3").glob("*.3pcap"):
        ff = f.with_name(f.name.removesuffix("pcap"))
        if f.is_symlink():
            tp = f.readlink()
            f.unlink()
            self.ln_s(tp.with_name(tp.name.removesuffix("pcap")), ff)
        else:
            self.mv(f, ff)


@subpackage("libpcap-devel")
def _(self):
    self.depends += ["libnl-devel"]

    return self.default_devel(man="357")


configure_gen = []
