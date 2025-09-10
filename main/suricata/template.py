pkgname = "suricata"
pkgver = "8.0.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-gccmarch-native",
    "--enable-af-packet",
    "--enable-bundled-htp",
    "--enable-gccprotect",
    "--enable-geoip",
    "--enable-hiredis",
    "--enable-luajit",
    "--enable-nspr",
    "--enable-nss",
    "--enable-python",
]
make_dir = "."
make_install_args = ["install", "install-conf"]
hostmakedepends = ["automake", "cargo", "libtool", "linux-headers", "pkgconf"]
makedepends = [
    "cbindgen",
    "hiredis-devel",
    "jansson-devel",
    "libevent-devel",
    "libmaxminddb-devel",
    "libpcap-devel",
    "libyaml-devel",
    "luajit-devel",
    "lz4-devel",
    "nspr-devel",
    "nss-devel",
    "pcre2-devel",
    "python-pyyaml",
]
depends = ["python-pyyaml"]
pkgdesc = "High Performance Network IDS, IPS and Security Monitoring engine"
license = "GPL-2.0-or-later"
url = "https://suricata.io"
source = (
    f"https://www.openinfosecfoundation.org/download/suricata-{pkgver}.tar.gz"
)
sha256 = "51f36ef492cbee8779d6018e4f18b98a08e677525851251279c1f851654f451f"


def post_install(self):
    self.install_service(self.files_path / "suricata")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
