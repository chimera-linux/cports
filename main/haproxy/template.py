pkgname = "haproxy"
pkgver = "3.3.3"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "EXTRA=admin/halog/halog",
    "TARGET=linux-musl",
    "USE_GETADDRINFO=1",
    "USE_KTLS=1",
    "USE_LUA=1",
    "USE_NS=1",
    "USE_OPENSSL=1",
    "USE_PCRE2=1",
    "USE_PCRE2_JIT=1",
    "USE_PROMEX=1",
    "USE_PTHREAD_EMULATION=1",
    "USE_QUIC=1",
    "USE_SHM_OPEN=1",
    "USE_ZLIB=1",
    "V=1",
]
make_install_args = [
    "EXTRA=admin/halog/halog",
    "SBINDIR=/usr/bin",
]
hostmakedepends = ["pkgconf"]
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
sha256 = "0ea2d0e157cdd2aff3d600c2365dadf50e6a28c41d3e52dcced53ce10a66e532"
# builds successfully but fails to run if enabled
hardening = ["!vis", "!cfi", "!int"]
# hard depends on vtest which doesn't have releases
options = ["!check"]


def init_build(self):
    self.make_build_args += ["cmd_LD=" + self.get_tool("CC")]


def post_install(self):
    self.install_file(self.files_path / "haproxy.cfg", "etc/haproxy")
    self.install_files("examples", "usr/share/haproxy")
    self.uninstall("usr/doc/haproxy")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "haproxy")
    self.install_license("LICENSE")


@subpackage("haproxy-cli-scripts")
def _(self):
    self.subdesc = "administration bash scripts"
    self.depends = [self.parent, "bash"]
    self.install_if = [self.parent, "bash"]
    return ["cmd:haproxy-dump-certs", "cmd:haproxy-reload"]
