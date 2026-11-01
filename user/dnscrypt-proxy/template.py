pkgname = "dnscrypt-proxy"
pkgver = "2.1.20"
pkgrel = 0
build_style = "go"
prepare_after_patch = True
make_build_args = ["./dnscrypt-proxy"]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
pkgdesc = "Tool for securing communications between a client and a DNS resolver"
license = "ISC"
url = "https://dnscrypt.info"
source = f"https://github.com/DNSCrypt/dnscrypt-proxy/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2e6adb32e0f91cb755f1d2c060cddcc80ffca6a181bf03c90df22bbade121607"
# no tests included
options = ["!check"]


def post_extract(self):
    # use our own
    self.rm("vendor", recursive=True)


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "dnscrypt-proxy")
    self.install_files(
        "utils/generate-domains-blocklist", "usr/share/dnscrypt-proxy"
    )
    for f in (self.cwd / "dnscrypt-proxy").glob("example-*"):
        self.install_file(
            f"dnscrypt-proxy/{f.name}",
            "usr/share/dnscrypt-proxy",
            name=f"{f.name.removeprefix('example-')}",
        )
    self.install_license("LICENSE")
