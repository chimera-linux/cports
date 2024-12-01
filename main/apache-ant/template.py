pkgname = "apache-ant"
pkgver = "1.10.15"
pkgrel = 1
hostmakedepends = ["openjdk17-jdk"]
depends = ["virtual:java-jre!openjdk17-jre"]
pkgdesc = "Java build system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://ant.apache.org"
source = (
    f"https://archive.apache.org/dist/ant/source/apache-ant-{pkgver}-src.tar.xz"
)
sha256 = "6c6e4c15233cb7b9851283051f99a9f04aa0e3291375138ea50399717d489878"
env = {"JAVA_HOME": "/usr/lib/jvm/java-17-openjdk"}
options = ["!cross"]

_pfx = "usr/share/apache-ant"


def prepare(self):
    self.do("./bootstrap.sh")
    self.do(
        "./bootstrap/bin/ant",
        "-Ddest=optional",
        "-f",
        "fetch.xml",
        allow_network=True,
    )


def build(self):
    self.do(
        "./bootstrap/bin/ant",
        f"-Ddist.dir={self.chroot_destdir / _pfx}",
        "jars",
    )


def install(self):
    self.do(
        "./bootstrap/bin/ant",
        f"-Ddist.dir={self.chroot_destdir / _pfx}",
        "dist",
    )
    self.install_file(self.files_path / "apache-ant.sh", "etc/profile.d")
    self.install_dir("usr/bin")
    self.install_link("usr/bin/ant", "../share/apache-ant/bin/ant")
    self.rename(f"{_pfx}/manual", "usr/share/doc/apache-ant", relative=False)
    self.uninstall(f"{_pfx}/bin/*.bat", glob=True)
    self.uninstall(f"{_pfx}/bin/*.cmd", glob=True)
