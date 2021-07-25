pkgname = "openssl"
version = "1.1.1k"
revision = 0
build_style = "configure"
configure_script = "Configure"
configure_args = [
    "--prefix=/usr", "--openssldir=/etc/ssl", "--libdir=lib",
    "shared", "no-ssl3-method", "no-asm", "-Wa,--noexecstack"
]
make_check_target = "test"
make_install_args = ["MANSUFFIX=ssl"]
short_desc = "Toolkit for Secure Sockets Layer and Transport Layer Security"
maintainer = "q66 <q66@chimera-linux.org>"
license = "OpenSSL"
homepage = "https://www.openssl.org"
distfiles = [f"https://www.openssl.org/source/openssl-{version}.tar.gz"]
checksum = ["892a0875b9872acd04a9fde79b1f943075d5ea162415de3047c327df33fbaee5"]
conf_files = ["/etc/ssl/openssl.cnf"]

options = ["bootstrap"]

if not current.bootstrapping:
    hostmakedepends = ["perl"]

from cbuild import cpu

ecargs = cpu.match_target(
    "x86_64*", ["enable-ec_nistp_64_gcc_128", "linux-x86_64"],
    "aarch64*", ["linux-aarch64"],
    "ppc64le*", ["linux-ppc64le"],
    "ppc64*", ["linux-ppc64"],
    "riscv64*", ["linux-generic64"], # linux64-riscv64 for openssl 3
    "*", None
)

if not ecargs:
    broken = f"Unknown CPU: {cpu.target()}"

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
    self.short_desc = short_desc + " - crypto library"

    return [
        "usr/lib/libcrypto.so.*",
        "usr/lib/engines-1.1",
    ]

@subpackage("libssl1.1")
def _libssl(self):
    self.short_desc = short_desc + " - SSL/TLS library"

    return ["usr/lib/libssl.so.*"]

@subpackage("openssl-c_rehash")
def _crehash(self):
    self.short_desc = short_desc + " - c_rehash utility"
    self.depends = ["openssl"]

    if not self.bootstrapping:
        self.depends.append("perl")

    return ["usr/bin/c_rehash"]

@subpackage("openssl-devel")
def _devel(self):
    self.short_desc = short_desc + " - development files"
    self.depends = [
        f"{pkgname}={version}-r{revision}",
        f"libssl1.1={version}-r{revision}",
        f"libcrypto1.1={version}-r{revision}"
    ]

    return [
        "usr/share/man/man3",
        "usr/share/doc",
        "usr/include",
        "usr/lib/pkgconfig",
        "usr/lib/*.a",
        "usr/lib/*.so",
    ]
