pkgname = "cargo"
pkgver = "1.75.0"
_cargover = f"0.{int(pkgver[2:4]) + 1}.{pkgver[5:]}"
pkgrel = 0
build_style = "cargo"
# PKG_CONFIG being in environment mysteriously brings target sysroot
# into linker sequence for build script, breaking build entirely
make_build_wrapper = ["env", "-u", "PKG_CONFIG"]
hostmakedepends = [
    "cargo-bootstrap",
    "python",
    "curl",
    "cmake",
    "pkgconf",
    "zlib-devel",
]
makedepends = ["libcurl-devel", "openssl-devel"]
pkgdesc = "Rust package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
source = f"https://github.com/rust-lang/cargo/archive/{_cargover}.tar.gz"
sha256 = "52d57889715cdfe0070b13f6d4dbfc4affdafc763483269e78b6ebd7166fdb83"
# global environment
env = {
    "SSL_CERT_FILE": "/etc/ssl/certs/ca-certificates.crt",
    "RUST_BACKTRACE": "1",
}
# disable check at least for now
options = ["!check"]

# you can use this to generate bootstrap binaries for cargo
# these are mostly static and only bootstrap toolchain is used
# do not use a temporary directory mode when running this!
_bootstrap = False

if _bootstrap:
    hostmakedepends += ["rust-bootstrap"]
    makedepends += ["rust-bootstrap", "openssl-devel-static"]
    options += ["!debug"]
else:
    hostmakedepends += ["rust"]
    makedepends += ["rust-std", "libgit2-devel"]
    depends = ["rust"]


def init_prepare(self):
    if _bootstrap:
        self.make_env["LIBGIT2_NO_VENDOR"] = "0"
        self.make_env["OPENSSL_STATIC"] = "1"
        self.make_env["OPENSSL_NO_PKG_CONFIG"] = "1"
        self.make_env["OPENSSL_DIR"] = str(self.profile().sysroot / "usr")


def do_install(self):
    _binp = f"target/{self.profile().triplet}/release/cargo"

    if _bootstrap:
        bdirn = f"cargo-{pkgver}-{self.profile().triplet}"
        self.mkdir(bdirn)
        self.cp(_binp, bdirn)
        self.cp("LICENSE-APACHE", bdirn)
        self.cp("LICENSE-MIT", bdirn)
        self.cp("LICENSE-THIRD-PARTY", bdirn)
        self.do("tar", "cvJf", f"{bdirn}.tar.xz", bdirn)
        self.rm(bdirn, recursive=True)
        self.error("build done, collect your tarball in builddir")
    else:
        self.install_bin(_binp)

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
