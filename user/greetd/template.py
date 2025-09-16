pkgname = "greetd"
pkgver = "0.10.3"
pkgrel = 7
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "dinit-chimera",
    "linux-pam-devel",
    "rust-std",
]
pkgdesc = "Minimal and flexible login manager daemon"
license = "GPL-3.0-or-later"
url = "https://git.sr.ht/~kennylevinsen/greetd"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "ee5cb70e0add4ca9c9fe57e47581ab0002d44c07743fb5492469f3b570db640b"


def pre_prepare(self):
    # the version that is in there is busted on loongarch
    self.do(
        "cargo",
        "update",
        "--package",
        "libc",
        "--precise",
        "0.2.170",
        allow_network=True,
    )


def post_build(self):
    self.do("make", "-C", "man", "all")


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/agreety")
    self.install_bin(f"target/{self.profile().triplet}/release/fakegreet")
    self.install_bin(f"target/{self.profile().triplet}/release/greetd")

    self.do(
        "make",
        "-C",
        "man",
        "install",
        f"DESTDIR={self.chroot_destdir}",
        "PREFIX=/usr",
    )

    self.install_file("config.toml", "etc/greetd")
    self.install_file(
        self.files_path / "greetd.pam", "usr/lib/pam.d", name="greetd"
    )
    self.install_service(self.files_path / "greetd")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
