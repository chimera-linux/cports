pkgname = "haproxy"
pkgver = "2.9.6"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = [
    "TARGET=linux-musl",
    "USE_GETADDRINFO=1",
    "USE_GZIP=1",
    "USE_LUA=1",
    "USE_NS=1",
    "USE_OPENSSL=1",
    "USE_PCRE2=1",
    "USE_PCRE2_JIT=1",
    "USE_PROMEX=1",
    "USE_PTHREAD_EMULATION=1",
    "USE_QUIC=1",
    "USE_QUIC_OPENSSL_COMPAT=1",
    "USE_THREAD=1",
    "USE_ZLIB=1",
    "V=1",
]
make_install_args = [
    "SBINDIR=/usr/bin",
    "DOCDIR=/usr/share/doc/haproxy",
]
make_check_target = "reg-tests"
make_use_env = True
hostmakedepends = [
    "gmake",
    "pkgconf",
]
makedepends = [
    "linux-headers",
    "lua5.4-devel",
    "openssl-devel",
    "pcre2-devel",
    "zlib-devel",
]
pkgdesc = "TCP/HTTP reverse proxy for high availability environments"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later WITH custom:OpenSSL-exception"
url = "https://www.haproxy.org"
source = (
    f"{url}/download/{pkgver[:pkgver.rfind('.')]}/src/{pkgname}-{pkgver}.tar.gz"
)
sha256 = "208adf47c8fa83c54978034ba5c0110b7463c47078f119bd052342171a3b9a0b"
hardening = ["!vis", "!cfi", "!int"]
# hard depends on vtest which doesn't have releases
options = ["!check"]


def pre_build(self):
    self.do("gmake", "opts")


def post_install(self):
    self.install_file(self.files_path / "haproxy.cfg", "etc/haproxy")
    self.install_files("examples", "usr/share/haproxy")
    self.install_files("doc", "usr/share/haproxy")
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="haproxy.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="haproxy.conf",
    )
    self.install_service(self.files_path / "haproxy")
    self.install_license("LICENSE")
