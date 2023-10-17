pkgname = "greetd"
pkgver = "0.9.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "bmake",
    "cargo",
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
source = f"https://git.sr.ht/~kennylevinsen/greetd/archive/{pkgver}.tar.gz"
sha256 = "a0cec141dea7fd7838b60a52237692d0fd5a0169cf748b8f8379d8409a3768eb"

system_users = [
    {
        "name": "_greetd",
        "id": None,
        "home": "/var/lib/greetd",
    }
]


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
