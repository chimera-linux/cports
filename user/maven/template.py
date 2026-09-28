pkgname = "maven"
pkgver = "3.9.16"
pkgrel = 0
hostmakedepends = ["openjdk25"]
depends = ["virtual:java-jre!openjdk25-jre"]
pkgdesc = "Software project management and comprehension tool"
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
    "f7031b091ad75a226a06a0c092cbf05860dcfc16d140e6da997e6c6b62dbd03c",
    "80ffca22aed9e8b9713a232f3394fd81d7f20322df75efdb2b047dbd3e3a23bb",
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
