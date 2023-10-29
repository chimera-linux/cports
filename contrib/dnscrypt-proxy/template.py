pkgname = "dnscrypt-proxy"
pkgver = "2.1.5"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Tool for securing communications between a client and a DNS resolver"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "ISC"
url = "https://dnscrypt.info"
source = f"https://github.com/DNSCrypt/dnscrypt-proxy/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "044c4db9a3c7bdcf886ff8f83c4b137d2fd37a65477a92bfe86bf69587ea7355"
file_modes = {
    "var/cache/dnscrypt-proxy": ("_dnscrypt", "_dnscrypt", 0o755),
    "var/log/dnscrypt-proxy": ("_dnscrypt", "_dnscrypt", 0o755),
}
# no tests included
options = ["!check"]
system_users = ["_dnscrypt"]


def post_extract(self):
    # FIXME: I can't get the included vendor path to work, weird dir layout?
    # Remove and re-vendor.
    self.rm("vendor", recursive=True)


def do_build(self):
    self.golang.build(wrksrc="dnscrypt-proxy")


def post_install(self):
    # Cache dir for resolver source lists
    self.install_dir("var/cache/dnscrypt-proxy", empty=True)

    self.install_dir("var/log/dnscrypt-proxy", empty=True)

    self.install_dir("etc/dnscrypt-proxy")
    self.install_file(
        self.files_path / "dnscrypt-proxy.toml", "etc/dnscrypt-proxy"
    )

    self.install_service(self.files_path / "dnscrypt-proxy")

    self.install_license("LICENSE")
