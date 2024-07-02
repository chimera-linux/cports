pkgname = "netdata"
pkgver = "1.45.6"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_PLUGIN_FREEIPMI=Off",
    "-DENABLE_PLUGIN_NFACCT=Off",
    "-DENABLE_PLUGIN_XENSTAT=Off",
    "-DENABLE_PLUGIN_EBPF=Off",
    "-DENABLE_PLUGIN_SYSTEMD_JOURNAL=Off",
    "-DENABLE_PLUGIN_GO=Off",
    "-DBUILD_FOR_PACKAGING=On",
    "-DCMAKE_INSTALL_PREFIX=/",
]
hostmakedepends = [
    "git",
    "go",
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "cups-devel",
    "elfutils-devel",
    "json-c-devel",
    "libmnl-devel",
    "libuuid-devel",
    "libuv-devel",
    "libyaml-devel",
    "linux-headers",
    "lz4-devel",
    "openssl-devel",
    "protobuf-devel",
    "snappy-devel",
]
pkgdesc = "Netdata monitoring agent"
maintainer = "yanchan09 <yan@omg.lol>"
license = "GPL-3.0-or-later"
url = "https://github.com/netdata/netdata"
source = f"{url}/releases/download/v{pkgver}/netdata-v{pkgver}.tar.gz"
sha256 = "95abd56a3ed30251af4a0285f0cc012f1851ee93b625e0c55f14e86d97759f2c"


def post_install(self):
    self.install_service(self.files_path / "netdata")
