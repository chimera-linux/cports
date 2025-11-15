pkgname = "haproxy"
pkgver = "3.2.9"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "EXTRA=admin/halog/halog",
    "TARGET=linux-musl",
    "USE_GETADDRINFO=1",
    "USE_LUA=1",
    "USE_NS=1",
    "USE_OPENSSL=1",
    "USE_PCRE2=1",
    "USE_PCRE2_JIT=1",
    "USE_PROMEX=1",
    "USE_PTHREAD_EMULATION=1",
    "USE_QUIC=1",
    "USE_QUIC_OPENSSL_COMPAT=1",
    "USE_ZLIB=1",
    "V=1",
]
make_install_args = [
    "EXTRA=admin/halog/halog",
    "SBINDIR=/usr/bin",
    "DOCDIR=/usr/share/doc/haproxy",
]
make_check_target = "reg-tests"
hostmakedepends = [
    "pkgconf",
]
makedepends = [
    "dinit-chimera",
    "linux-headers",
    "lua5.4-devel",
    "openssl3-devel",
    "pcre2-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "TCP/HTTP reverse proxy for high availability environments"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later WITH custom:OpenSSL-exception"
url = "https://www.haproxy.org"
source = (
    f"{url}/download/{pkgver[: pkgver.rfind('.')]}/src/haproxy-{pkgver}.tar.gz"
)
sha256 = "e660d141b29019f4d198785b0834cc3e9c96efceeb807c2fff2fc935bd3354c2"
hardening = ["!vis", "!cfi", "!int"]
# hard depends on vtest which doesn't have releases
options = ["!check"]


def init_build(self):
    self.make_build_args += ["cmd_LD=" + self.get_tool("CC")]


def post_install(self):
    self.install_file(self.files_path / "haproxy.cfg", "etc/haproxy")
    self.install_files("examples", "usr/share/haproxy")
    self.install_files("doc", "usr/share/haproxy")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "haproxy")
    self.install_license("LICENSE")
