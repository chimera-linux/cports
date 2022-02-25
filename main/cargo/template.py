pkgname = "cargo"
pkgver = "1.59.0"
pkgrel = 0
hostmakedepends = [
    "cargo-bootstrap", "python", "curl", "cmake", "pkgconf", "zlib-devel"
]
makedepends = ["libcurl-devel", "openssl-devel"]
pkgdesc = "Rust package manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT OR Apache-2.0"
url = "https://rust-lang.org"
source = f"https://github.com/rust-lang/{pkgname}/archive/rust-{pkgver}.tar.gz"
sha256 = "e3bcc26be1a07ecd6eaa07a46a6343558924c39db862ffe1adffca90feb9371f"
# global environment
env = {
    "CARGO_HOME": "/cargo",
    "SSL_CERT_FILE": "/etc/ssl/certs/ca-certificates.crt",
    "OPENSSL_NO_VENDOR": "1",
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
    makedepends += ["rust"]
    depends = ["rust"]

if self.profile().cross:
    env["PKG_CONFIG_ALLOW_CROSS"] = "1"

def init_patch(self):
    if _bootstrap:
        self.env["OPENSSL_STATIC"] = "1"
        self.env["OPENSSL_NO_PKG_CONFIG"] = "1"
        self.env["OPENSSL_DIR"] = str(self.profile().sysroot / "usr")

# TODO: replace with a helper in another place
def pre_patch(self):
    self.do("cargo", "vendor", allow_network = True)

    self.mkdir(".cargo")
    with open(self.cwd / ".cargo/config.toml", "w") as cf:
        cf.write("""
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
""")
        if self.profile().cross:
            sroot = self.profile().sysroot
            trip = self.profile().triplet

            cf.write(f"""
[build]
target = "{trip}"

[target.{trip}]
linker = "{self.get_tool("CC")}"
""")

def do_build(self):
    # PKG_CONFIG being in environment mysteriously brings target sysroot
    # into linker sequence for build script, breaking build entirely
    self.do(
        "env", "-u", "PKG_CONFIG", "cargo", "build",
        "--release", "--offline"
    )

def do_install(self):

    if self.profile().cross:
        _binp = f"target/{self.profile().triplet}/release/cargo"
    else:
        _binp = "target/release/cargo"

    if _bootstrap:
        bdirn = f"cargo-{pkgver}-{self.profile().triplet}"
        self.mkdir(bdirn)
        self.cp(_binp, bdirn)
        self.cp("LICENSE-APACHE", bdirn)
        self.cp("LICENSE-MIT", bdirn)
        self.cp("LICENSE-THIRD-PARTY", bdirn)
        self.do("tar", "cvJf", f"{bdirn}.tar.xz", bdirn)
        self.rm(bdirn, recursive = True)
        self.error("build done, collect your tarball in builddir")
    else:
        self.install_bin(_binp)

    for f in (self.cwd / "src/etc/man").glob("*.?"):
        self.install_man(f)

    self.install_file(
        "src/etc/cargo.bashcomp.sh", "usr/share/bash-completion/completions",
        name = "cargo"
    )
    self.install_file("src/etc/_cargo", "usr/share/zsh/site-functions")

    self.install_license("LICENSE-APACHE")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-THIRD-PARTY")
