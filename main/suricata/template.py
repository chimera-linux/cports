pkgname = "suricata"
pkgver = "8.0.1"
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
    "dinit-chimera",
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
sha256 = "bd868f41717e5431cdda3a99386810257aafdbe2dbcbb58d07fb8476a03358a5"


def post_install(self):
    self.install_service(self.files_path / "suricata")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
