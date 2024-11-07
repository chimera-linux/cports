pkgname = "dnscrypt-proxy"
pkgver = "2.1.5"
pkgrel = 11
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Tool for securing communications between a client and a DNS resolver"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "ISC"
url = "https://dnscrypt.info"
source = f"https://github.com/DNSCrypt/dnscrypt-proxy/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "044c4db9a3c7bdcf886ff8f83c4b137d2fd37a65477a92bfe86bf69587ea7355"
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
