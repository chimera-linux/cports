pkgname = "cargo-crev"
pkgver = "0.26.3"
pkgrel = 0
build_wrksrc = "cargo-crev"
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["openssl3-devel", "libgit2-devel", "rust-std", "sqlite-devel"]
pkgdesc = "Cryptographically verifiable code review system for cargo"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MPL-2.0 OR MIT OR Apache-2.0"
url = "https://github.com/crev-dev/cargo-crev"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    "https://github.com/rust-lang/git2-rs/archive/refs/tags/git2-0.20.0.tar.gz",
]
source_paths = [".", "git2"]
sha256 = [
    "887f3af119b1501be27a35b293087ce2a1c94ae05e00c6052bc91ae86db680b2",
    "d4b8b2b2526944d6cb75ecf8bcc2c1757fc1fa6deef94b6d32410b1f84f38d1b",
]
# takes forever to run literally 2 unittests
options = ["!check"]


def post_prepare(self):
    from cbuild.util import cargo

    # nuke lockfiles that may still hold the old ver
    self.rm("vendor/cargo/Cargo.lock")
    self.rm("vendor/gix/Cargo.lock")

    cargo.clear_vendor_checksums(self, "cargo")
    cargo.clear_vendor_checksums(self, "gix")

    self.mv("git2/libgit2-sys", ".")
    self.mv("git2/git2-curl", ".")

    # nuke the old git2 stuff and replace with new
    for crt in ["libgit2-sys", "git2-curl", "git2"]:
        self.rm(f"vendor/{crt}", recursive=True)
        self.mv(crt, "vendor")

    # write updated checksums from lockfile
    cargo.write_vendor_checksum(
        self,
        "libgit2-sys",
        "e1a117465e7e1597e8febea8bb0c410f1c7fb93b1e1cddf34363f8390367ffec",
    )
    cargo.write_vendor_checksum(
        self,
        "git2-curl",
        "be8dcabbc09ece4d30a9aa983d5804203b7e2f8054a171f792deff59b56d31fa",
    )
    cargo.write_vendor_checksum(
        self,
        "git2",
        "3fda788993cc341f69012feba8bf45c0ba4f3291fcc08e214b4d5a7332d88aff",
    )


def post_install(self):
    self.install_license("LICENSE-MIT")
