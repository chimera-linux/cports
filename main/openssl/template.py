pkgname = "openssl"
pkgver = "1.1.1l"
pkgrel = 0
build_style = "configure"
configure_script = "Configure"
configure_args = [
    "--prefix=/usr", "--openssldir=/etc/ssl", "--libdir=lib",
    "shared", "no-ssl3-method", "no-asm", "-Wa,--noexecstack"
]
make_install_args = ["MANSUFFIX=ssl"]
make_check_target = "test"
hostmakedepends = ["pkgconf", "perl"]
pkgdesc = "Toolkit for Secure Sockets Layer and Transport Layer Security"
maintainer = "q66 <q66@chimera-linux.org>"
license = "OpenSSL"
url = "https://www.openssl.org"
source = f"https://www.openssl.org/source/openssl-{pkgver}.tar.gz"
sha256 = "0b7a3e5e59c34827fe0c3a74b7ec8baef302b98fa80088d7f9153aa16fa76bd1"
options = ["bootstrap"]

if self.stage > 0:
    makedepends = ["linux-headers"]

match self.profile().arch:
    case "x86_64":
        configure_args += ["enable-ec_nistp_64_gcc_128", "linux-x86_64"]
    case "aarch64" | "ppc64le" | "ppc64":
        configure_args += [f"linux-{self.profile().arch}"]
    case "riscv64":
        configure_args += ["linux-generic64"] # linux64-riscv64 for openssl 3
    case _:
        broken = f"Unknown CPU architecture: {self.profile().arch}"

def pre_configure(self):
    self.configure_args += self.get_cflags()
    self.configure_args += self.get_ldflags()

def do_build(self):
    self.make.invoke("depend")
    self.make.build(["MAKEDEPPROG=" + self.get_tool("CC")])

@subpackage("libcrypto1.1")
def _libcrypto(self):
    self.pkgdesc = f"{pkgdesc} (crypto library)"

    return [
        "usr/lib/libcrypto.so.*",
        "usr/lib/engines-1.1",
    ]

@subpackage("libssl1.1")
def _libssl(self):
    self.pkgdesc = f"{pkgdesc} (SSL/TLS library)"

    return ["usr/lib/libssl.so.*"]

@subpackage("openssl-c_rehash")
def _crehash(self):
    self.pkgdesc = f"{pkgdesc} (c_rehash utility)"
    self.depends = ["openssl"]

    if self.stage > 0:
        self.depends.append("perl")

    return ["usr/bin/c_rehash"]

@subpackage("openssl-static")
def _static(self):
    return self.default_static()

@subpackage("openssl-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}",]

    return self.default_devel()
