pkgname = "rink"
pkgver = "0.8.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf", "asciidoctor"]
makedepends = ["rust-std", "openssl3-devel"]
pkgdesc = "Unit aware calculator repl"
license = "MPL-2.0"
url = "https://rinkcalc.app/about"
source = (
    f"https://github.com/tiffany352/rink-rs/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "40048e84c2b606e50bf05dec2813acedeb48066cd48537d0dea453a72d000d60"


def post_build(self):
    for page in [
        "rink.1",
        "rink.5",
        "rink.7",
        "rink-defs.5",
        "rink-dates.5",
    ]:
        self.do(
            "asciidoctor", "-b", "manpage", "-D", "man", f"docs/{page}.adoc"
        )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/rink")
    self.install_license("LICENSE-MPL")

    for page in [
        "rink.1",
        "rink.5",
        "rink.7",
        "rink-defs.5",
        "rink-dates.5",
    ]:
        self.install_man(f"man/{page}")

    for data_file in [
        "definitions.units",
        "datepatterns.txt",
        "currency.units",
    ]:
        self.install_file(f"core/{data_file}", "usr/share/rink")
