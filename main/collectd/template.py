pkgname = "collectd"
pkgver = "5.12.0"
pkgrel = 2
build_style = "gnu_configure"
configure_args = ["--disable-werror"]
hostmakedepends = [
    "automake",
    "bison",
    "flex",
    "libtool",
    "pkgconf",
]
makedepends = [
    "curl-devel",
    "hiredis-devel",
    "i2c-tools-devel",
    "iptables-devel",
    "jansson-devel",
    "libdbi-devel",
    "libmicrohttpd-devel",
    "libmnl-devel",
    "libnotify-devel",
    "libpcap-devel",
    "libvirt-devel",
    "libxml2-devel",
    "linux-headers",
    "lm-sensors-devel",
    "lua5.4-devel",
    "musl-bsd-headers",
    "protobuf-c-devel",
    "rabbitmq-c-devel",
    "rrdtool-devel",
]
pkgdesc = "System statistics collection daemon"
license = "MIT"
url = "https://collectd.org"
source = f"https://github.com/collectd/collectd/releases/download/collectd-{pkgver}/collectd-{pkgver}.tar.bz2"
sha256 = "5bae043042c19c31f77eb8464e56a01a5454e0b39fa07cf7ad0f1bfc9c3a09d6"


def post_install(self):
    self.install_license("COPYING")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "collectd")
    self.install_files("contrib", "usr/share/doc", name="collectd")
