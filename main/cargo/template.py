pkgname = "cargo"
pkgver = "1.89.0"
_cargover = f"0.{int(pkgver[2:4]) + 1}.{pkgver[5:]}"
pkgrel = 0
build_style = "cargo"
# PKG_CONFIG being in environment mysteriously brings target sysroot
# into linker sequence for build script, breaking build entirely
make_build_wrapper = ["env", "-u", "PKG_CONFIG"]
hostmakedepends = [
    "cargo-bootstrap",
    "cmake",
    "curl",
    "pkgconf",
    "python",
]
makedepends = ["curl-devel", "openssl3-devel", "sqlite-devel"]
pkgdesc = "Rust package manager"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
source = f"https://github.com/rust-lang/cargo/archive/{_cargover}.tar.gz"
sha256 = "6e38bf4131c667b41b8a5b78bc39232ece2d476a75de1f72f82ce07f425b2e3b"
# global environment
env = {
    "SSL_CERT_FILE": "/etc/ssl/certs/ca-certificates.crt",
    "RUST_BACKTRACE": "1",
}
# disable check at least for now
options = ["!check"]

if self.current_target == "custom:bootstrap":
    hostmakedepends += ["rust-bootstrap"]
    makedepends += ["rust-bootstrap", "openssl3-devel-static"]
    options += ["!debug"]
else:
    hostmakedepends += ["rust"]
    makedepends += ["rust-std", "libgit2-devel"]
    depends = ["rust"]


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()


def init_prepare(self):
    if self.current_target == "custom:bootstrap":
        self.make_env["LIBGIT2_NO_VENDOR"] = "0"
        self.make_env["OPENSSL_STATIC"] = "1"
        self.make_env["OPENSSL_NO_PKG_CONFIG"] = "1"
        self.make_env["OPENSSL_DIR"] = str(self.profile().sysroot / "usr")


def prepare(self):
    # we patch the lockfile so vendor after patch
    pass


@custom_target("bootstrap", "build")
def _(self):
    binp = f"target/{self.profile().triplet}/release/cargo"
    bdirn = f"cargo-{pkgver}-{self.profile().triplet}"
    self.mkdir(bdirn)
    self.cp(binp, bdirn)
    self.cp("LICENSE-APACHE", bdirn)
    self.cp("LICENSE-MIT", bdirn)
    self.cp("LICENSE-THIRD-PARTY", bdirn)
    self.do("tar", "cvJf", f"{bdirn}.tar.xz", bdirn)
    self.rm(bdirn, recursive=True)


def install(self):
    binp = f"target/{self.profile().triplet}/release/cargo"

    self.install_bin(binp)

    for f in (self.cwd / "src/etc/man").glob("*.?"):
        self.install_man(f)

    self.install_file(
        "src/etc/cargo.bashcomp.sh",
        "usr/share/bash-completion/completions",
        name="cargo",
    )
    self.install_file("src/etc/_cargo", "usr/share/zsh/site-functions")

    self.install_license("LICENSE-APACHE")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
