pkgname = "maven"
pkgver = "3.9.9"
pkgrel = 0
hostmakedepends = ["openjdk21"]
depends = ["virtual:java-jre!openjdk21-jre"]
pkgdesc = "Software project management and comprehension tool"
maintainer = "natthias <natthias@proton.me>"
license = "Apache-2.0"
url = "https://maven.apache.org"
source = [
    f"https://dlcdn.apache.org/maven/maven-3/{pkgver}/source/apache-maven-{pkgver}-src.tar.gz",
    f"https://dlcdn.apache.org/maven/maven-3/{pkgver}/binaries/apache-maven-{pkgver}-bin.tar.gz",
]
source_paths = [
    ".",
    "bootstrap",
]
sha256 = [
    "8a24c448d4ac397e6b0c019a4d7250068c02d1cdb553299e6bb71c3ccca78b2c",
    "7a9cdf674fc1703d6382f5f330b3d110ea1b512b51f1652846d9e4e8a588d766",
]


def prepare(self):
    self.do(
        "./bootstrap/bin/mvn",
        "org.apache.maven.plugins:maven-dependency-plugin:2.8:go-offline",
        "-Dmaven.repo.local=/cbuild_cache/maven",
        allow_network=True,
    )
    # Workaround upstream issue with fetching dependencies
    self.do(
        "./bootstrap/bin/mvn",
        "verify",
        "--fail-never",
        "-Dmaven.repo.local=/cbuild_cache/maven",
        allow_network=True,
    )


def build(self):
    self.do(
        "./bootstrap/bin/mvn",
        "-o",
        "package",
        "-DskipTests",
        "-Drat.skip=true",
        "-Dmaven.repo.local=/cbuild_cache/maven",
        "-DdistributionTargetDir=out",
    )


def check(self):
    self.do(
        "./bootstrap/bin/mvn",
        "-o",
        "test",
        "-Drat.skip=true",
        "-Dmaven.repo.local=/cbuild_cache/maven",
    )


def install(self):
    self.install_files("apache-maven/out", "usr/lib/", name="maven")

    self.install_dir("usr/bin")
    for bin in ["mvn", "mvnDebug", "mvnyjp"]:
        self.install_link(
            f"usr/bin/{bin}",
            f"../lib/maven/bin/{bin}",
        )
