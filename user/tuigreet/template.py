pkgname = "tuigreet"
pkgver = "0.11.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "scdoc"]
makedepends = ["rust-std"]
depends = ["greetd"]
pkgdesc = "Console greeter for greetd"
license = "GPL-3.0-or-later"
url = "https://github.com/apognu/tuigreet"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "7d643ba224c40c6a63f9462a826630543071aea08e732ccd2e880bcd80d939e8"


def post_patch(self):
    from cbuild.util import cargo

    cargo.clear_vendor_checksums(self, "utmp-raw-0.4.0")


def post_build(self):
    with open(self.cwd / "contrib" / "man" / "tuigreet-1.scd", "rb") as i:
        with open(self.cwd / "contrib" / "man" / "tuigreet.1", "w") as o:
            self.do("scdoc", input=i.read(), stdout=o)


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "tuigreet"))
    self.install_man("contrib/man/tuigreet.1")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_file(
        "contrib/example.config.toml",
        "usr/share/examples/tuigreet",
        name="config.toml",
    )
