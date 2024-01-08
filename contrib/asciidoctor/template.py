pkgname = "asciidoctor"
pkgver = "2.0.20"
pkgrel = 0
hostmakedepends = ["ruby"]
depends = ["ruby"]
pkgdesc = "Ruby-based AsciiDoc converter"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://asciidoctor.org"
source = f"!https://rubygems.org/downloads/{pkgname}-{pkgver}.gem"
sha256 = "835eabd445e4ae88f56a5f4e07593c3612b2be72eb661c612c3a8e1e17c57479"


def do_extract(self):
    self.cp(self.sources_path / f"{pkgname}-{pkgver}.gem", ".")


def do_install(self):
    target = f"usr/lib/ruby/gems/{self.ruby_version}"

    self.do(
        "gem",
        "install",
        "--local",
        "--install-dir",
        self.chroot_destdir / target,
        "--ignore-dependencies",
        "--verbose",
        "--no-document",
        f"{pkgname}-{pkgver}.gem",
    )
    self.rm(
        self.destdir / target / "cache",
        recursive=True,
    )

    self.install_dir("usr/bin")
    self.install_link(
        f"../lib/ruby/gems/{self.ruby_version}/bin/{pkgname}",
        f"usr/bin/{pkgname}",
    )

    self.install_dir("usr/share/licenses")
    self.mv(
        self.destdir / target / f"gems/{pkgname}-{pkgver}/LICENSE",
        self.destdir / f"usr/share/licenses/{pkgname}",
    )

    self.install_dir("usr/share/man/man1")
    self.mv(
        self.destdir / target / f"gems/{pkgname}-{pkgver}/man/{pkgname}.1",
        self.destdir / "usr/share/man/man1",
    )
