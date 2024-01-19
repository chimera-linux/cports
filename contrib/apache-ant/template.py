pkgname = "apache-ant"
pkgver = "1.10.14"
pkgrel = 0
hostmakedepends = ["openjdk17-jdk"]
# FIXME: depends on unversioned providers are somewhat broken in apk
# depends = ["virtual:java-jre!openjdk17-jre"]
pkgdesc = "Java build system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://ant.apache.org"
source = (
    f"https://archive.apache.org/dist/ant/source/apache-ant-{pkgver}-src.tar.xz"
)
sha256 = "9eea3cd8a793574a07fde2f87b203dc86339492baeb539367d5aa5be497aea24"
env = {"JAVA_HOME": "/usr/lib/jvm/java-17-openjdk"}
options = ["!cross"]

_pfx = "usr/share/apache-ant"


def do_prepare(self):
    self.do("./bootstrap.sh")
    self.do(
        "./bootstrap/bin/ant",
        "-Ddest=optional",
        "-f",
        "fetch.xml",
        allow_network=True,
    )


def do_build(self):
    self.do(
        "./bootstrap/bin/ant",
        f"-Ddist.dir={self.chroot_destdir / _pfx}",
        "jars",
    )


def do_install(self):
    self.do(
        "./bootstrap/bin/ant",
        f"-Ddist.dir={self.chroot_destdir / _pfx}",
        "dist",
    )
    self.install_file(self.files_path / "apache-ant.sh", "etc/profile.d")
    self.install_dir("usr/bin")
    self.install_dir("usr/share/doc")
    self.install_link("../share/apache-ant/bin/ant", "usr/bin/ant")
    self.mv(
        self.destdir / _pfx / "manual",
        self.destdir / "usr/share/doc/apache-ant",
    )
    self.rm(self.destdir / _pfx / "bin/*.bat", glob=True)
    self.rm(self.destdir / _pfx / "bin/*.cmd", glob=True)
