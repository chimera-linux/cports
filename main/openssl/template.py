pkgname = "openssl"
pkgver = "1.1.1k"
pkgrel = 0
build_style = "configure"
configure_script = "Configure"
configure_args = [
    "--prefix=/usr", "--openssldir=/etc/ssl", "--libdir=lib",
    "shared", "no-ssl3-method", "no-asm", "-Wa,--noexecstack"
]
make_install_args = ["MANSUFFIX=ssl"]
make_check_target = "test"
pkgdesc = "Toolkit for Secure Sockets Layer and Transport Layer Security"
maintainer = "q66 <q66@chimera-linux.org>"
license = "OpenSSL"
url = "https://www.openssl.org"
source = f"https://www.openssl.org/source/openssl-{pkgver}.tar.gz"
sha256 = "892a0875b9872acd04a9fde79b1f943075d5ea162415de3047c327df33fbaee5"
options = ["bootstrap"]

if not current.bootstrapping:
    hostmakedepends = ["pkgconf", "perl"]

ecargs = {
    "x86_64": ["enable-ec_nistp_64_gcc_128", "linux-x86_64"],
    "aarch64": ["linux-aarch64"],
    "ppc64le": ["linux-ppc64le"],
    "ppc64": ["linux-ppc64"],
    "riscv64": ["linux-generic64"], # linux64-riscv64 for openssl 3
}.get(current.build_profile.arch, None)

if not ecargs:
    broken = f"Unknown CPU: {current.build_profile.arch}"

configure_args += ecargs

def pre_configure(self):
    #self.configure_args += self.CPPFLAGS
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

    if not self.bootstrapping:
        self.depends.append("perl")

    return ["usr/bin/c_rehash"]

@subpackage("openssl-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}",]

    return self.default_devel(man = True)
