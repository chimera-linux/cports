pkgname = "greetd"
pkgver = "0.10.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "bmake",
    "cargo-auditable",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "linux-pam-devel",
    "rust-std",
]
pkgdesc = "Minimal and flexible login manager daemon"
maintainer = "natthias <natthias@proton.me>"
license = "GPL-3.0-or-later"
url = "https://git.sr.ht/~kennylevinsen/greetd"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "d6151a8683f386c53a010b6dfe37cf4c842bc03313bed7a917be96309372d1df"


def post_build(self):
    self.do("make", "-C", "man", "all")


def do_install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/agreety")
    self.install_bin(f"target/{self.profile().triplet}/release/fakegreet")
    self.install_bin(f"target/{self.profile().triplet}/release/greetd")

    self.install_man("man/*.1", glob=True)
    self.install_man("man/*.5", glob=True)
    self.install_man("man/*.7", glob=True)

    self.install_file("config.toml", "etc/greetd")
    self.install_file(
        self.files_path / "greetd.pam", "etc/pam.d", name="greetd"
    )
    self.install_service(self.files_path / "greetd")
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="greetd.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="greetd.conf",
    )
