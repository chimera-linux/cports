pkgname = "dnscrypt-proxy"
pkgver = "2.1.7"
pkgrel = 7
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Tool for securing communications between a client and a DNS resolver"
license = "ISC"
url = "https://dnscrypt.info"
source = f"https://github.com/DNSCrypt/dnscrypt-proxy/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6394cd2d73dedca9317aeee498b6c2520b841cea042d83f398c3355a13c50f7c"
# no tests included
options = ["!check"]


def post_extract(self):
    # use our own
    self.rm("vendor", recursive=True)


def build(self):
    self.golang.build(wrksrc="dnscrypt-proxy")


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_file(
        self.files_path / "dnscrypt-proxy.toml", "etc/dnscrypt-proxy"
    )
    self.install_service(self.files_path / "dnscrypt-proxy")
    self.install_license("LICENSE")
